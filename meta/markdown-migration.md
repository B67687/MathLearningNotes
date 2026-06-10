# Markdown Migration

> **Status: SUPERSEDED (2025-06-10)**
>
> This strategy has been reversed. Notebooks (`.ipynb`) are now the canonical format
> again. See the [Notebook Restoration](#notebook-restoration-2025-06-10) section below.

The long-term source format should be Markdown.

The reason is simple: Markdown is easier to read, diff, copy, search, review, preserve, and publish than Jupyter notebooks.

Jupyter notebooks are still useful for code, simulation, widgets, and generated outputs. But most explanations in this repository are mainly mathematical writing. Those should live as Markdown first.

## Tool Decision

Use Markdown as the durable source.

Use Jupytext or MyST Markdown when notebook execution is still needed.

Use MarkItDown only for importing outside material such as PDFs, DOCX files, slides, spreadsheets, or other document formats. It is not the main notebook migration tool.

## Why Not MarkItDown For The Main Notebook Migration

MarkItDown is useful, but it is designed as a general converter for many document types.

For Jupyter notebooks, the more natural tool family is Jupytext and MyST Markdown because they understand notebook structure and can keep Markdown connected to executable notebooks.

The migration strategy is:

```text
ipynb -> markdown source
ipynb -> archive/notebooks for provenance
markdown source -> polished canonical note over time
optional markdown source -> executable notebook later when needed
```

## Current Local Converter

This repository includes a no-dependency exporter:

```bash
python3 tools/export_notebooks_to_markdown.py
```

It writes temporary Markdown exports into:

```text
markdown-notes/
```

To export only one notebook:

```bash
python3 tools/export_notebooks_to_markdown.py discrete-mathematics/combinatorics/pascals-triangle.ipynb
```

The exporter adds provenance front matter so converted notes remain linked to the original notebook.

After promotion, Markdown files live beside the old notebook paths and notebooks live under:

```text
archive/notebooks/
```

The active topic folders should be edited as Markdown first.

Archived notebooks are for provenance, recovery, and inspecting original outputs.

## Provenance Policy

Existing notebooks are treated as original human-authored notes by `B67687` unless a file explicitly says otherwise.

New generated or derived notes should say so in front matter.

Use:

```yaml
original_human_author: B67687
```

for original human notes.

Use:

```yaml
derived_from: path/to/source.ipynb
generated_by: GPT-5
review_status: needs-human-review
```

for generated or heavily rewritten notes.

## Migration Passes

First pass: create Markdown mirrors without changing original notebooks. Completed.

Second pass: promote Markdown into the active topic folders and archive notebooks. Completed.

Third pass: choose one topic folder and polish the Markdown files into canonical explanations. In progress.

Fourth pass: mark polished Markdown files as canonical and treat notebooks as archived provenance.

Fifth pass: keep the website build rendering Markdown explanations as first-class pages. Completed.

## Notebook Restoration (2025-06-10)

The markdown-canonical strategy has been **reversed** because KaTeX/Hugo rendering
could not handle some LaTeX features (e.g. `\textcolor`) that work perfectly in
Jupyter notebooks with MathJax.

### What Changed

- All 129 notebooks were moved back from `archive/notebooks/` to their original
  active directories (e.g. `discrete-mathematics/combinatorics/binomial-expansion.ipynb`).
- All 129 derived Markdown files were moved from the active directories to
  `archive/markdown/` for historical reference.
- 5 notes that were originally written as Markdown (no notebook original) remain
  as Markdown in the active directories. These are marked with a † symbol in the README.
- The Hugo website now generates redirect stub pages that point each note to its
  GitHub notebook viewer URL (which renders notebooks with full MathJax support).
- A custom `redirect` layout handles the redirect rendering.

### Current File Layout

```
Active directories (canonical):
├── *.ipynb         — 129 Jupyter notebooks (primary format)
├── *.md            — 5 markdown-only notes (no notebook original)

Archive:
├── archive/markdown/   — 129 derived Markdown files (historical)
└── archive/notebooks/  — (empty directory, preserved for reference)
```

### Site Behavior

Each notebook's page on the Hugo site now auto-redirects to the GitHub viewer
URL for that notebook. Markdown-only notes are rendered directly by the Hextra
theme as before. The homepage (from README.md) links to all notes.
