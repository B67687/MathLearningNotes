from __future__ import annotations

import html
import os
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("PAGES_OUTPUT_DIR", ROOT / "_site"))
EXCLUDED_PARTS = {
    ".git",
    ".github",
    ".ipynb_checkpoints",
    "__pycache__",
    "_site",
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


def should_skip(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def handle_remove_readonly(func, path, excinfo) -> None:
    os.chmod(path, stat.S_IWRITE)
    func(path)


def clear_output_dir() -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR, onexc=handle_remove_readonly)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def run_nbconvert(notebook_path: Path) -> Path:
    relative_path = notebook_path.relative_to(ROOT)
    destination = OUTPUT_DIR / relative_path.with_suffix(".html")
    destination.parent.mkdir(parents=True, exist_ok=True)

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
        str(notebook_path),
    ]
    subprocess.run(command, check=True)
    rewrite_html_links(destination)
    return destination


def rewrite_notebook_links(text: str) -> str:
    return re.sub(r"(?P<prefix>[\(/\"'=])(?P<target>[^\"')>]+?)\.ipynb(?P<suffix>[\"')>#?])", r"\g<prefix>\g<target>.html\g<suffix>", text)


def rewrite_html_links(html_path: Path) -> None:
    content = html_path.read_text(encoding="utf-8")
    updated = rewrite_notebook_links(content)
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


def build_homepage() -> None:
    readme_path = ROOT / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8")
    readme_text = rewrite_notebook_links(readme_text)
    body = render_markdown(readme_text)

    page = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>MathLearningNotes</title>
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
        background: #ffffff;
        border: 1px solid #d0d7de;
        border-radius: 12px;
        padding: 32px;
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
        Notebook links on this site open rendered HTML pages generated from the repository's <code>.ipynb</code> files.
      </div>
      <article class="markdown-body">
        {body}
      </article>
    </main>
  </body>
</html>
"""
    (OUTPUT_DIR / "index.html").write_text(page, encoding="utf-8")


def create_nojekyll_file() -> None:
    (OUTPUT_DIR / ".nojekyll").write_text("", encoding="utf-8")


def main() -> None:
    clear_output_dir()

    notebooks = sorted(
        path for path in ROOT.rglob("*.ipynb") if not should_skip(path)
    )
    if not notebooks:
        raise RuntimeError("No notebooks were found to convert.")

    for notebook in notebooks:
        print(f"Converting {notebook.relative_to(ROOT)}")
        run_nbconvert(notebook)

    copy_static_files()
    build_homepage()
    create_nojekyll_file()

    print(f"Built {len(notebooks)} notebooks into {OUTPUT_DIR}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        command = " ".join(html.escape(part) for part in exc.cmd)
        raise SystemExit(f"Build failed while running: {command}") from exc
