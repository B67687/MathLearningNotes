from __future__ import annotations

import logging
import os
import time
from pathlib import Path

import nbformat
import requests


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "translated-notebooks"
DEFAULT_ENDPOINT = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions"
DEFAULT_MODEL = "qwen-mt-turbo"
REQUEST_TIMEOUT_SECONDS = 60
REQUEST_DELAY_SECONDS = float(os.environ.get("QWEN_REQUEST_DELAY_SECONDS", "0.3"))
SKIP_DIRS = {
    ".git",
    ".github",
    ".ipynb_checkpoints",
    "translated-notebooks",
}


class TranslationError(RuntimeError):
    pass


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def get_api_key() -> str:
    return (os.environ.get("QWEN_API_KEY") or os.environ.get("DASHSCOPE_API_KEY") or "").strip()


def get_endpoint() -> str:
    return (os.environ.get("QWEN_API_ENDPOINT") or DEFAULT_ENDPOINT).strip()


def get_model() -> str:
    return (os.environ.get("QWEN_MODEL") or DEFAULT_MODEL).strip()


def translate_text(text: str, api_key: str) -> str:
    if not text or not text.strip():
        return text

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": get_model(),
        "messages": [{"role": "user", "content": text}],
        "translation_options": {
            "source_lang": "auto",
            "target_lang": "Chinese",
        },
    }

    try:
        response = requests.post(
            get_endpoint(),
            headers=headers,
            json=payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise TranslationError(f"Unexpected translation response format: {exc}") from exc
    except requests.RequestException as exc:
        raise TranslationError(f"Translation request failed: {exc}") from exc
    finally:
        if REQUEST_DELAY_SECONDS > 0:
            time.sleep(REQUEST_DELAY_SECONDS)


def translate_notebook(notebook_path: Path, api_key: str) -> bool:
    try:
        with notebook_path.open("r", encoding="utf-8") as handle:
            notebook = nbformat.read(handle, as_version=4)
    except nbformat.reader.NotJSONError:
        logging.error("Skipping invalid notebook JSON: %s", notebook_path)
        return False
    except OSError as exc:
        logging.error("Failed to read %s: %s", notebook_path, exc)
        return False

    changed = False
    for cell in notebook.cells:
        if cell.cell_type != "markdown":
            continue

        translated = translate_text(cell.source, api_key)
        if translated != cell.source:
            cell.source = translated
            changed = True

    output_path = OUTPUT_DIR / notebook_path.relative_to(ROOT)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        nbformat.write(notebook, handle)

    logging.info("Translated %s -> %s", notebook_path.relative_to(ROOT), output_path.relative_to(ROOT))
    return changed


def find_notebooks() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("*.ipynb") if not should_skip(path)
    )


def main() -> int:
    api_key = get_api_key()
    if not api_key:
        logging.error("QWEN_API_KEY or DASHSCOPE_API_KEY must be configured.")
        return 1

    notebooks = find_notebooks()
    if not notebooks:
        logging.info("No notebook files found.")
        return 0

    translated_count = 0
    for notebook_path in notebooks:
        try:
            if translate_notebook(notebook_path, api_key):
                translated_count += 1
        except TranslationError as exc:
            logging.error("Stopping after translation failure in %s: %s", notebook_path, exc)
            return 1

    logging.info("Translation process completed. %s notebooks updated.", translated_count)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
