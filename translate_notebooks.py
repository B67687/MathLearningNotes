from __future__ import annotations

import argparse
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


def env_value(*names: str, default: str = "") -> str:
    for name in names:
        value = os.environ.get(name)
        if value and value.strip():
            return value.strip()
    return default


def get_api_key() -> str:
    return env_value("DASHSCOPE_API_KEY", "QWEN_API_KEY")


def get_endpoint() -> str:
    return env_value("DASHSCOPE_API_ENDPOINT", "QWEN_API_ENDPOINT", default=DEFAULT_ENDPOINT)


def get_model() -> str:
    return env_value("QWEN_MODEL", default=DEFAULT_MODEL)


def translate_text(text: str, api_key: str, session: requests.Session) -> str:
    if not text or not text.strip():
        return text

    payload = {
        "model": get_model(),
        "messages": [{"role": "user", "content": text}],
        "translation_options": {
            "source_lang": "auto",
            "target_lang": "zh",
        },
    }

    try:
        response = session.post(
            get_endpoint(),
            json=payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        if not response.ok:
            raise TranslationError(
                f"Translation request failed with status {response.status_code}: "
                f"{response.text.strip()}"
            )
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise TranslationError(f"Unexpected translation response format: {exc}") from exc
    except requests.RequestException as exc:
        raise TranslationError(f"Translation request failed: {exc}") from exc
    finally:
        if REQUEST_DELAY_SECONDS > 0:
            time.sleep(REQUEST_DELAY_SECONDS)


def translate_notebook(notebook_path: Path, api_key: str, session: requests.Session) -> bool:
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

        translated = translate_text(cell.source, api_key, session)
        if translated != cell.source:
            cell.source = translated
            changed = True

    output_path = OUTPUT_DIR / notebook_path.relative_to(ROOT)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        nbformat.write(notebook, handle)

    logging.info("Translated %s -> %s", notebook_path.relative_to(ROOT), output_path.relative_to(ROOT))
    return changed


def find_all_notebooks() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.ipynb") if not should_skip(path))


def resolve_notebook_paths(input_paths: list[str]) -> list[Path]:
    resolved_paths: list[Path] = []
    seen: set[Path] = set()

    for input_path in input_paths:
        candidate = (ROOT / input_path).resolve()
        try:
            relative = candidate.relative_to(ROOT)
        except ValueError:
            logging.warning("Skipping notebook outside repository: %s", input_path)
            continue

        if should_skip(relative) or candidate.suffix != ".ipynb" or not candidate.exists():
            logging.warning("Skipping invalid notebook path: %s", input_path)
            continue

        if candidate not in seen:
            seen.add(candidate)
            resolved_paths.append(candidate)

    return sorted(resolved_paths)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Translate Jupyter notebooks into Chinese.")
    parser.add_argument("notebooks", nargs="*", help="Notebook paths relative to the repository root.")
    parser.add_argument("--all", action="store_true", help="Translate all notebooks in the repository.")
    parser.add_argument(
        "--file-list",
        help="Path to a newline-delimited file containing notebook paths relative to the repository root.",
    )
    return parser.parse_args()


def load_requested_notebooks(args: argparse.Namespace) -> list[Path]:
    if args.all:
        return find_all_notebooks()

    requested_paths = list(args.notebooks)
    if args.file_list:
        requested_paths.extend(
            line.strip()
            for line in Path(args.file_list).read_text(encoding="utf-8").splitlines()
            if line.strip()
        )

    if not requested_paths:
        return []

    return resolve_notebook_paths(requested_paths)


def main() -> int:
    args = parse_args()

    api_key = get_api_key()
    if not api_key:
        logging.error("DASHSCOPE_API_KEY or QWEN_API_KEY must be configured.")
        return 1

    notebooks = load_requested_notebooks(args)
    if not notebooks:
        logging.info("No notebook files selected for translation.")
        return 0

    logging.info("Using endpoint: %s", get_endpoint())
    logging.info("Using model: %s", get_model())

    translated_count = 0
    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
    )

    for notebook_path in notebooks:
        try:
            if translate_notebook(notebook_path, api_key, session):
                translated_count += 1
        except TranslationError as exc:
            logging.error("Stopping after translation failure in %s: %s", notebook_path, exc)
            return 1

    logging.info("Translation process completed. %s notebooks updated.", translated_count)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
