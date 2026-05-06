#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "markdown-notes"
SKIP_PARTS = {
    ".git",
    ".github",
    ".ipynb_checkpoints",
    "__pycache__",
    "_site",
    "archive",
    "markdown-notes",
}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_PARTS for part in path.parts)


def normalize_title(path: Path, notebook: dict) -> str:
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        source = "".join(cell.get("source", []))
        for line in source.splitlines():
            match = re.match(r"^\s*#\s+(.+?)\s*$", line)
            if match:
                return match.group(1).strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def markdown_source(cell: dict) -> str:
    return "".join(cell.get("source", [])).rstrip()


def code_source(cell: dict) -> str:
    source = "".join(cell.get("source", [])).rstrip()
    if not source:
        return ""
    return f"```python\n{source}\n```"


def front_matter(title: str, source: Path) -> str:
    relative_source = source.relative_to(ROOT).as_posix()
    return "\n".join(
        [
            "---",
            f"title: {json.dumps(title, ensure_ascii=False)}",
            f"source_notebook: {json.dumps(relative_source, ensure_ascii=False)}",
            "original_human_author: B67687",
            "conversion: exported from original notebook",
            "canonical_status: markdown-mirror",
            "---",
            "",
        ]
    )


def convert_notebook(path: Path, output_root: Path) -> Path:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    title = normalize_title(path, notebook)
    parts = [front_matter(title, path)]

    for cell in notebook.get("cells", []):
        cell_type = cell.get("cell_type")
        if cell_type == "markdown":
            content = markdown_source(cell)
        elif cell_type == "code":
            content = code_source(cell)
        else:
            content = ""

        if content:
            parts.append(content)
            parts.append("")

    relative = path.relative_to(ROOT).with_suffix(".md")
    destination = output_root / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    return destination


def iter_notebooks(selected: list[str]) -> list[Path]:
    if selected:
        return [Path(item).resolve() if Path(item).is_absolute() else ROOT / item for item in selected]
    return sorted(path for path in ROOT.rglob("*.ipynb") if not should_skip(path))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export notebooks to durable Markdown mirrors."
    )
    parser.add_argument(
        "notebooks",
        nargs="*",
        help="Optional notebook paths relative to the repository root.",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Output directory. Defaults to markdown-notes/.",
    )
    args = parser.parse_args()

    output_root = Path(args.output)
    if not output_root.is_absolute():
        output_root = ROOT / output_root

    converted = []
    for notebook in iter_notebooks(args.notebooks):
        if not notebook.exists():
            raise SystemExit(f"Notebook not found: {notebook}")
        converted.append(convert_notebook(notebook, output_root))

    for path in converted:
        print(path.relative_to(ROOT).as_posix())

    print(f"Converted {len(converted)} notebook(s).")


if __name__ == "__main__":
    main()
