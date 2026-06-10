#!/usr/bin/env bash
# prepare-content.sh — Populate Hugo content/ for notebook-redirect site.
#
# Usage:  bash scripts/prepare-content.sh
#
#   - Copies README.md → content/_index.md (homepage).
#   - Generates redirect stub pages for every .ipynb notebook in active dirs.
#   - Copies any .md notes without a notebook counterpart (markdown-only).
#   - Adds lightweight _index.md stubs for every directory so Hugo section menus work.
#   - Rewrites .md / .ipynb → .html inside relative links so they resolve after Hugo builds.
#
set -euo pipefail
IFS=$'\n\t'

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CONTENT_DIR="$ROOT/content"
GITHUB_BASE="https://github.com/B67687/MathLearningNotes/blob/main"

# ——— config ——————————————————————————————————————————————————————————————
# Each pattern is evaluated against the path *relative to ROOT*.
# A trailing / ensures it only matches a directory prefix, not a file suffix.
EXCLUDE=(
	'.git/'
	'.github/'
	'.opencode/'
	'_site/'
	'archive/'
	'content/' # skip content/ itself (in case it has leftover files)
	'math-learning-notes-content/'
	'meta/'
	'themes/'
	'tools/'
	'.nojekyll'
	'.gitignore'
	'build_pages.py'
	'hugo.toml'
	'pages-requirements.txt'
	'requirements.txt'
)

# Section weights for top-level dirs (lower = earlier in sidebar).
declare -A WEIGHTS=(
	['algebra']=10
	['calculus']=20
	['discrete-mathematics']=30
	['fractals']=40
	['trigonometry']=50
	['translated-notebooks']=60
)
DEFAULT_WEIGHT=50

# ——— helpers —————————————————————————————————————————————————————————————
# Returns 0 (true) if the given relative path should be excluded.
should_exclude() {
	local rel="$1"
	for pat in "${EXCLUDE[@]}"; do
		if [[ "$rel" == "$pat"* ]] || [[ "$rel" == *"/$pat"* ]]; then
			return 0
		fi
	done
	return 1
}

snake_to_title() {
	local name="$1"
	# Strip leading digits for title generation but keep for sorting
	name="${name##[0-9]*}"
	[[ -z "$name" ]] && name="$1" # was only digits
	echo "$name" | sed -E 's/[-_]/ /g; s/(^| )([a-z])/\1\U\2/g'
}

# like snake_to_title but for ipynb filenames that may have spaces
filename_to_title() {
	local name="$1"
	# Strip .ipynb extension
	name="${name%.ipynb}"
	# Replace hyphens, underscores, and multiple spaces with single space
	echo "$name" | sed -E 's/[-_]+/ /g; s/  +/ /g; s/(^| )([a-z])/\1\U\2/g'
}

dir_weight() {
	echo "${WEIGHTS[$1]:-$DEFAULT_WEIGHT}"
}

# ——— step 1: prepare content/ ——————————————————————————————————————————
echo "=== Cleaning content/ ==="
rm -rf "$CONTENT_DIR"
mkdir -p "$CONTENT_DIR"

# ——— step 2: copy README.md as _index.md (homepage) ———————————————————
echo "=== Copying README.md → _index.md ==="
cp "$ROOT/README.md" "$CONTENT_DIR/_index.md"

# ——— step 3: generate redirect stubs for notebooks ————————————————————
echo "=== Generating redirect stub pages for notebooks ==="
STUB_COUNT=0
while IFS= read -r -d '' nb; do
	rel="${nb#$ROOT/}"

	if should_exclude "$rel"; then
		continue
	fi

	# Generate stub at content/<path-without-ipynb>.md
	stub_rel="${rel%.ipynb}.md"
	stub="$CONTENT_DIR/$stub_rel"
	mkdir -p "$(dirname "$stub")"

	# Extract a readable title from the filename
	basename="$(basename "$rel")"
	title="$(filename_to_title "$basename")"

	# Build the GitHub viewer URL
	github_url="$GITHUB_BASE/$rel"

	cat >"$stub" <<-STUB
		---
		title: "$title"
		layout: redirect
		redirect_url: "$github_url"
		---

	STUB
	STUB_COUNT=$((STUB_COUNT + 1))
done < <(find "$ROOT" -name '*.ipynb' -type f -print0)
echo "  Generated $STUB_COUNT redirect stubs."

# ——— step 4: copy markdown-only notes (no notebook counterpart) ————————
echo "=== Copying markdown-only notes ==="
MD_COUNT=0
while IFS= read -r -d '' md; do
	rel="${md#$ROOT/}"

	if should_exclude "$rel"; then
		continue
	fi

	# Skip README (already handled as _index.md)
	[[ "$rel" == "README.md" ]] && continue

	# Skip if a notebook with the same basename exists (already redirected)
	if [[ -f "$ROOT/${rel%.md}.ipynb" ]]; then
		continue
	fi

	dest="$CONTENT_DIR/$rel"
	mkdir -p "$(dirname "$dest")"
	cp "$md" "$dest"
	MD_COUNT=$((MD_COUNT + 1))
done < <(find "$ROOT" -name '*.md' -type f -print0)
echo "  Copied $MD_COUNT markdown-only note(s)."

# ——— step 5: add _index.md stubs ———————————————————————————————————————
echo "=== Adding _index.md stubs for section directories ==="

# Collect all dirs under content/ (excluding root which already has _index.md)
DIRS=()
while IFS= read -r -d '' dir; do
	rel="${dir#$CONTENT_DIR/}"
	[[ -z "$rel" ]] && continue
	DIRS+=("$dir")
done < <(find "$CONTENT_DIR" -type d -print0)

# Sort by depth descending so deepest dirs are processed first
IFS=$'\n' DIRS=($(for d in "${DIRS[@]}"; do echo "$d"; done | awk -F/ '{print NF, $0}' | sort -t' ' -k1,1rn -k2 | cut -d' ' -f2-))
unset IFS

for dir in "${DIRS[@]}"; do
	idx="$dir/_index.md"
	[[ -f "$idx" ]] && continue

	dirname="$(basename "$dir")"
	title="$(snake_to_title "$dirname")"
	weight="$(dir_weight "$dirname")"

	cat >"$idx" <<-INDX
		---
		title: "$title"
		weight: $weight
		---

	INDX
done

echo "  Added $(find "$CONTENT_DIR" -name '_index.md' -not -path "$CONTENT_DIR/_index.md" | wc -l) section stubs."

# ——— step 6: rewrite .md/.ipynb links → .html ————————————————————————
echo "=== Rewriting .md / .ipynb links → .html ==="

while IFS= read -r -d '' f; do
	sed -i \
		-E 's/(\]\()([^)]+)\.md(#?)/\1\2.html\3/g; s/(\]\()([^)]+)\.ipynb(#?)/\1\2.html\3/g' \
		"$f"
done < <(find "$CONTENT_DIR" -name '*.md' -type f -print0)

echo "  Done."

# ——— summary ——————————————————————————————————————————————————————
echo ""
echo "=== Content prepared ==="
echo "  Content root: $CONTENT_DIR"
echo "  Total files:  $(find "$CONTENT_DIR" -type f | wc -l)"
echo "  Stubs:        $(find "$CONTENT_DIR" -name '*.md' -not -name '_index.md' | wc -l)"
echo "  Sections:     $(find "$CONTENT_DIR" -name '_index.md' | wc -l)"
echo "  Homepage:     README.md → _index.md (redirect-based notebook viewer)"
