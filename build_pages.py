from __future__ import annotations

import html
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("PAGES_OUTPUT_DIR", ROOT / "_site"))
EXCLUDED_PARTS = {
    ".git",
    ".github",
    ".opencode",
    ".ipynb_checkpoints",
    "__pycache__",
    "_site",
    "archive",
    "markdown-notes",
}
STATIC_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".ico",
    ".txt",
    ".yml",
    ".yaml",
}

NOTEBOOK_THEME_OVERRIDES = """
<style>
  body.jp-Notebook {
    background: #f6f8fa;
    color: #1f2328;
    margin: 0 auto;
    padding: 24px;
  }

  body.jp-Notebook {
    --jp-ui-font-color0: rgba(31, 35, 40, 1);
    --jp-ui-font-color1: rgba(31, 35, 40, 0.92);
    --jp-ui-font-color2: rgba(31, 35, 40, 0.72);
    --jp-ui-font-color3: rgba(31, 35, 40, 0.56);
    --jp-content-font-color0: rgba(31, 35, 40, 1);
    --jp-content-font-color1: rgba(31, 35, 40, 0.92);
    --jp-content-font-color2: rgba(31, 35, 40, 0.72);
    --jp-content-font-color3: rgba(31, 35, 40, 0.56);
    --jp-layout-color0: #ffffff;
    --jp-layout-color1: #ffffff;
    --jp-layout-color2: #f6f8fa;
    --jp-rendermime-table-row-background: #f6f8fa;
    --jp-rendermime-table-row-hover-background: #eaeef2;
    --jp-cell-editor-background: #ffffff;
    --jp-cell-editor-active-background: #ffffff;
    --jp-cell-editor-border-color: #d0d7de;
    --jp-cell-editor-active-border-color: #0969da;
  }

  body.jp-Notebook .jp-Cell,
  body.jp-Notebook .jp-InputArea,
  body.jp-Notebook .jp-OutputArea-output,
  body.jp-Notebook .jp-RenderedHTMLCommon,
  body.jp-Notebook .jp-RenderedMarkdown,
  body.jp-Notebook .jp-RenderedText,
  body.jp-Notebook .jp-RenderedLatex {
    color: #1f2328;
    line-height: 1.65;
  }

  body.jp-Notebook .jp-InputArea-editor,
  body.jp-Notebook .jp-CodeMirrorEditor,
  body.jp-Notebook .highlight,
  body.jp-Notebook .jp-RenderedHTMLCommon pre,
  body.jp-Notebook .jp-RenderedText pre {
    background: #ffffff;
    color: #1f2328;
  }

  body.jp-Notebook .jp-RenderedText pre .ansi-white-fg,
  body.jp-Notebook .jp-RenderedText pre .ansi-white-intense-fg,
  body.jp-Notebook .jp-RenderedText pre .ansi-default-inverse-fg {
    color: #1f2328;
  }

  body.jp-Notebook .jp-RenderedHTMLCommon a,
  body.jp-Notebook .jp-RenderedMarkdown a {
    color: #0969da;
  }

  body.jp-Notebook .jp-RenderedHTMLCommon h1,
  body.jp-Notebook .jp-RenderedHTMLCommon h2,
  body.jp-Notebook .jp-RenderedHTMLCommon h3,
  body.jp-Notebook .jp-RenderedHTMLCommon h4,
  body.jp-Notebook .jp-RenderedHTMLCommon h5,
  body.jp-Notebook .jp-RenderedHTMLCommon h6 {
    color: #1f2328;
  }

  body.jp-Notebook .jp-RenderedHTMLCommon table {
    display: block;
    overflow-x: auto;
    border-collapse: collapse;
  }

  body.jp-Notebook .jp-RenderedHTMLCommon th,
  body.jp-Notebook .jp-RenderedHTMLCommon td {
    border: 1px solid #d0d7de;
    padding: 6px 13px;
  }

  body.jp-Notebook .jp-RenderedHTMLCommon code:not(pre code) {
    background: rgba(175, 184, 193, 0.2);
    border-radius: 6px;
    color: #1f2328;
    padding: 0.15em 0.35em;
  }

  body.jp-Notebook mjx-container,
  body.jp-Notebook .MathJax {
    color: #1f2328 !important;
  }
</style>
"""


def should_skip(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def handle_remove_readonly(func, path, excinfo) -> None:
    os.chmod(path, stat.S_IWRITE)
    func(path)


def clear_output_dir() -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR, onexc=handle_remove_readonly)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_braced_group(text: str, start_index: int) -> tuple[str | None, int]:
    if start_index >= len(text) or text[start_index] != "{":
        return None, start_index

    depth = 0
    parts: list[str] = []
    index = start_index

    while index < len(text):
        character = text[index]
        if character == "{":
            if depth > 0:
                parts.append(character)
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return "".join(parts), index + 1
            if depth < 0:
                break
            parts.append(character)
        else:
            parts.append(character)
        index += 1

    return None, start_index


def unwrap_textcolor_macros(text: str) -> str:
    token = "\\textcolor"
    output: list[str] = []
    index = 0

    while index < len(text):
        if text.startswith(token, index):
            cursor = index + len(token)
            while cursor < len(text) and text[cursor].isspace():
                cursor += 1

            _, cursor = read_braced_group(text, cursor)
            if cursor == index + len(token):
                output.append(text[index])
                index += 1
                continue

            while cursor < len(text) and text[cursor].isspace():
                cursor += 1

            body, end_index = read_braced_group(text, cursor)
            if body is None:
                output.append(text[index])
                index += 1
                continue

            output.append(unwrap_textcolor_macros(body))
            index = end_index
            continue

        output.append(text[index])
        index += 1

    return "".join(output)


def strip_color_declarations(text: str) -> str:
    return re.sub(r"\\color\s*\{[^{}]+\}", "", text)


def is_list_line(line: str) -> bool:
    return bool(re.match(r"^\s*(?:[-*+]|\d+\.)\s+", line))


def is_indented_table_line(line: str) -> bool:
    return bool(re.match(r"^(?: {4}|\t)\|.+\|\s*$", line))


def is_table_separator(line: str) -> bool:
    normalized = re.sub(r"^(?: {4}|\t)", "", line, count=1)
    return bool(
        re.fullmatch(r"\|?(?:\s*:?-{3,}:?\s*\|)+\s*:?-{3,}:?\s*\|?\s*", normalized)
    )


def normalize_list_indented_tables(text: str) -> str:
    lines = text.splitlines()
    normalized: list[str] = []
    previous_nonblank = ""
    index = 0

    while index < len(lines):
        line = lines[index]
        if is_indented_table_line(line):
            block_end = index
            while block_end < len(lines) and is_indented_table_line(lines[block_end]):
                block_end += 1

            block = lines[index:block_end]
            if len(block) >= 2 and is_table_separator(block[1]) and is_list_line(previous_nonblank):
                normalized.extend(
                    re.sub(r"^(?: {4}|\t)", "", block_line, count=1)
                    for block_line in block
                )
                index = block_end
                continue

        normalized.append(line)
        if line.strip():
            previous_nonblank = line
        index += 1

    return "\n".join(normalized)


def preprocess_markdown_text(text: str) -> str:
    updated = unwrap_textcolor_macros(text)
    updated = strip_color_declarations(updated)
    updated = normalize_list_indented_tables(updated)
    return updated


def create_preprocessed_notebook(notebook_path: Path) -> tuple[Path, Path | None]:
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    changed = False

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue

        original = "".join(cell.get("source", []))
        updated = preprocess_markdown_text(original)
        if updated == original:
            continue

        cell["source"] = updated.splitlines(keepends=True)
        changed = True

    if not changed:
        return notebook_path, None

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".ipynb",
        prefix=f"{notebook_path.stem}.pages-",
        dir=notebook_path.parent,
        delete=False,
        encoding="utf-8",
        newline="\n",
    ) as handle:
        json.dump(notebook, handle, ensure_ascii=False, indent=1)
        handle.write("\n")
        temporary_path = Path(handle.name)

    return temporary_path, temporary_path


def run_nbconvert(notebook_path: Path) -> Path:
    relative_path = notebook_path.relative_to(ROOT)
    destination = OUTPUT_DIR / relative_path.with_suffix(".html")
    destination.parent.mkdir(parents=True, exist_ok=True)

    source_path, temporary_path = create_preprocessed_notebook(notebook_path)
    command = [
        sys.executable,
        "-m",
        "nbconvert",
        "--to",
        "html",
        "--output",
        destination.stem,
        "--output-dir",
        str(destination.parent),
        str(source_path),
    ]

    try:
        subprocess.run(command, check=True)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)

    rewrite_html_links(destination)
    return destination


def rewrite_note_links(text: str) -> str:
    updated = re.sub(
        r"(?P<prefix>[\(/\"'=])(?P<target>[^\"')>]+?)\.ipynb(?P<suffix>[\"')>#?])",
        r"\g<prefix>\g<target>.html\g<suffix>",
        text,
    )
    return re.sub(
        r"(?P<prefix>[\(/\"'=])(?P<target>[^\"')>]+?)\.md(?P<suffix>[\"')>#?])",
        r"\g<prefix>\g<target>.html\g<suffix>",
        updated,
    )


def rewrite_html_links(html_path: Path) -> None:
    content = html_path.read_text(encoding="utf-8")
    updated = rewrite_note_links(content)
    if NOTEBOOK_THEME_OVERRIDES not in updated and "</head>" in updated:
        updated = updated.replace("</head>", f"{NOTEBOOK_THEME_OVERRIDES}\n</head>", 1)
    if updated != content:
        html_path.write_text(updated, encoding="utf-8")


def copy_static_files() -> None:
    for path in ROOT.rglob("*"):
        if path.is_dir() or should_skip(path):
            continue
        if path == ROOT / "README.md":
            continue
        if path.suffix.lower() not in STATIC_SUFFIXES:
            continue

        destination = OUTPUT_DIR / path.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)


def render_markdown(markdown_text: str) -> str:
    try:
        import markdown
    except ImportError as exc:
        raise RuntimeError(
            "The 'markdown' package is required to build the Pages homepage. "
            "Install it with 'pip install markdown'."
        ) from exc

    return markdown.markdown(
        markdown_text,
        extensions=[
            "extra",
            "toc",
            "tables",
            "fenced_code",
            "sane_lists",
        ],
        output_format="html5",
    )


def parse_front_matter(markdown_text: str) -> tuple[dict[str, str], str]:
    if not markdown_text.startswith("---\n"):
        return {}, markdown_text

    end_marker = markdown_text.find("\n---\n", 4)
    if end_marker == -1:
        return {}, markdown_text

    front_matter_text = markdown_text[4:end_marker]
    metadata: dict[str, str] = {}
    for line in front_matter_text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"')

    body = markdown_text[end_marker + len("\n---\n") :]
    return metadata, body.lstrip()


def page_title(markdown_path: Path, metadata: dict[str, str], markdown_text: str) -> str:
    if metadata.get("title"):
        return metadata["title"]

    for line in markdown_text.splitlines():
        match = re.match(r"^\s*#\s+(.+?)\s*$", line)
        if match:
            return match.group(1).strip()

    return markdown_path.stem.replace("-", " ").replace("_", " ").title()


def html_page(title: str, body: str, note: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5.8.1/github-markdown.min.css">
    <style>
      body {{
        box-sizing: border-box;
        margin: 0;
        background: #f6f8fa;
        color: #1f2328;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      }}
      .page {{
        max-width: 980px;
        margin: 0 auto;
        padding: 32px 16px 48px;
      }}
      .markdown-body {{
        background: #ffffff !important;
        color: #1f2328 !important;
        border: 1px solid #d0d7de;
        border-radius: 12px;
        padding: 32px;
      }}
      .markdown-body :where(p, li, ul, ol, dl, td, th, blockquote, strong, em) {{
        color: #1f2328 !important;
      }}
      .markdown-body :where(h1, h2, h3, h4, h5, h6) {{
        color: #1f2328 !important;
      }}
      .markdown-body a {{
        color: #0969da !important;
      }}
      .markdown-body code {{
        color: #1f2328 !important;
        background-color: rgba(175, 184, 193, 0.2) !important;
      }}
      .markdown-body pre,
      .markdown-body pre code {{
        color: #e6edf3 !important;
        background: #1f2328 !important;
      }}
      .site-note,
      .site-note code {{
        color: #1f2328 !important;
      }}
      @media (prefers-color-scheme: dark) {{
        body {{
          background: #f6f8fa;
          color: #1f2328;
        }}
        .markdown-body {{
          background: #ffffff !important;
          color: #1f2328 !important;
          border-color: #d0d7de !important;
        }}
      }}
      .site-note {{
        margin-bottom: 16px;
        padding: 12px 16px;
        border-left: 4px solid #0969da;
        background: #ddf4ff;
        border-radius: 8px;
      }}
      @media (max-width: 767px) {{
        .page {{
          padding: 16px 10px 32px;
        }}
        .markdown-body {{
          padding: 20px;
        }}
      }}
    </style>
  </head>
  <body>
    <main class="page">
      <div class="site-note">
        {note}
      </div>
      <article class="markdown-body">
        {body}
      </article>
    </main>
  </body>
</html>
"""


def render_markdown_file(markdown_path: Path) -> Path:
    relative_path = markdown_path.relative_to(ROOT)
    destination = OUTPUT_DIR / relative_path.with_suffix(".html")
    destination.parent.mkdir(parents=True, exist_ok=True)

    raw_text = markdown_path.read_text(encoding="utf-8")
    metadata, body_text = parse_front_matter(raw_text)
    title = page_title(markdown_path, metadata, body_text)
    body_text = preprocess_markdown_text(body_text)
    body_text = rewrite_note_links(body_text)
    body = render_markdown(body_text)
    page = html_page(
        title,
        body,
        "Markdown notes are the canonical source. Archived notebooks are kept for provenance.",
    )
    destination.write_text(page, encoding="utf-8")
    return destination


def build_homepage() -> None:
    readme_path = ROOT / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8")
    readme_text = rewrite_note_links(readme_text)
    body = render_markdown(readme_text)
    page = html_page(
        "MathLearningNotes",
        body,
        "Markdown notes are the canonical source. Archived notebooks are kept for provenance.",
    )
    (OUTPUT_DIR / "index.html").write_text(page, encoding="utf-8")


def create_nojekyll_file() -> None:
    (OUTPUT_DIR / ".nojekyll").write_text("", encoding="utf-8")


def main() -> None:
    clear_output_dir()

    markdown_files = sorted(
        path
        for path in ROOT.rglob("*.md")
        if not should_skip(path) and path != ROOT / "README.md"
    )
    if not markdown_files:
        raise RuntimeError("No Markdown notes were found to render.")

    for markdown_file in markdown_files:
        print(f"Rendering {markdown_file.relative_to(ROOT)}")
        render_markdown_file(markdown_file)

    copy_static_files()
    build_homepage()
    create_nojekyll_file()

    print(f"Built {len(markdown_files)} Markdown notes into {OUTPUT_DIR}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        command = " ".join(html.escape(part) for part in exc.cmd)
        raise SystemExit(f"Build failed while running: {command}") from exc
