#!/usr/bin/env python3
"""
Convert Obsidian vault markdown to Hugo-compatible content.

Run from the .hugo/ directory or as: python3 .hugo/convert.py

What it does:
  1. Copies .md files from the repo root into .hugo/content/ with slugified filenames
  2. Renames index.md → _index.md (Hugo branch bundles)
  3. Maps INTRODUCTION.md → root _index.md (homepage)
  4. Rewrites [[wikilinks]] to standard markdown links
  5. Adds trailing double spaces for CommonMark line breaks

Skips: README.md, LICENCE*.md, and anything under .hugo/, .git/, .obsidian/, .docs/, .trash/
"""

import os
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = Path(__file__).resolve().parent / "content"

SKIP_DIRS = {".hugo", ".git", ".docs", ".obsidian", ".trash"}


def should_skip_file(filename: str) -> bool:
    """Skip README and all LICENCE variants."""
    return filename == "README.md" or filename.startswith("LICENCE")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(name: str) -> str:
    """Convert a filename or directory name to a URL-friendly slug."""
    s = name.replace(".md", "")
    s = s.replace("&", "and")
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"[^a-z0-9\-]", "", s.lower())
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def extract_title(content: str) -> str | None:
    """Extract title from YAML (---) or TOML (+++) frontmatter."""
    # YAML
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if m:
        t = re.search(r"^title:\s*['\"]?(.+?)['\"]?\s*$", m.group(1), re.MULTILINE)
        if t:
            return t.group(1)

    # TOML
    m = re.match(r"^\+\+\+\s*\n(.*?)\n\+\+\+", content, re.DOTALL)
    if m:
        t = re.search(r"^title\s*=\s*['\"](.+?)['\"]", m.group(1), re.MULTILINE)
        if t:
            return t.group(1)

    return None


def slugify_path(rel_root: Path) -> Path:
    """Slugify every component of a relative directory path."""
    if rel_root == Path("."):
        return Path(".")
    return Path(*[slugify(p) for p in rel_root.parts])


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

def build_file_list(repo_root: Path) -> list[tuple[Path, Path]]:
    """
    Walk the repo and return (source_path, dest_path) pairs.
    dest_path is relative to CONTENT_DIR.
    """
    files = []

    for root, dirs, filenames in os.walk(repo_root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        rel_root = Path(root).relative_to(repo_root)

        for f in sorted(filenames):
            if not f.endswith(".md") or should_skip_file(f):
                continue

            src = Path(root) / f
            slugged_dir = slugify_path(rel_root)

            # INTRODUCTION.md → root homepage
            if f == "INTRODUCTION.md" and rel_root == Path("."):
                dest = Path("_index.md")

            # File matching its parent directory → Hugo _index.md
            # e.g. monsters/Monsters.md → monsters/_index.md
            elif rel_root != Path(".") and slugify(f) == slugify(rel_root.name):
                dest = slugged_dir / "_index.md"

            # Regular page
            else:
                slug = slugify(f) + ".md"
                if slugged_dir == Path("."):
                    dest = Path(slug)
                else:
                    dest = slugged_dir / slug

            files.append((src, dest))

    return files


# ---------------------------------------------------------------------------
# Page lookup (for wikilink resolution)
# ---------------------------------------------------------------------------

def build_lookup(file_list: list[tuple[Path, Path]]) -> dict[str, str]:
    """
    Build a mapping of page name → Hugo URL path.

    Keys:
      - Regular files: filename without .md  (e.g. "Wildbond")
      - Directory-matching files (→ _index.md): filename without .md + frontmatter title
      - INTRODUCTION.md: "INTRODUCTION" + frontmatter title if present
    """
    lookup: dict[str, str] = {}

    for src, dest in file_list:
        # Compute Hugo URL from dest path
        if dest.name == "_index.md":
            # Branch bundle: URL is the directory
            if dest.parent == Path("."):
                url = "/"
            else:
                url = "/" + "/".join(dest.parent.parts) + "/"
        else:
            # Leaf page: URL includes the slug
            if dest.parent == Path("."):
                url = "/" + dest.stem + "/"
            else:
                url = "/" + "/".join(dest.parent.parts) + "/" + dest.stem + "/"

        filename = src.name

        if filename == "INTRODUCTION.md":
            lookup["INTRODUCTION"] = url
            content = src.read_text(encoding="utf-8")
            title = extract_title(content)
            if title:
                lookup[title] = url

        elif dest.name == "_index.md":
            # Directory-matching file (e.g. monsters/Monsters.md)
            # Key by filename so [[Monsters]] resolves
            page_name = filename.replace(".md", "")
            lookup[page_name] = url
            # Also key by frontmatter title if different
            content = src.read_text(encoding="utf-8")
            title = extract_title(content)
            if title and title != page_name:
                lookup[title] = url

        else:
            page_name = filename.replace(".md", "")
            lookup[page_name] = url

    return lookup


def get_page_name(src: Path) -> str:
    """Determine the page's own name (for self-reference detection)."""
    if src.name == "INTRODUCTION.md":
        return "INTRODUCTION"
    return src.stem


# ---------------------------------------------------------------------------
# Wikilink conversion
# ---------------------------------------------------------------------------

def resolve_wikilink(
    match: re.Match, lookup: dict[str, str], current_page: str
) -> str:
    """Convert one [[wikilink]] match to a standard markdown link."""
    inner = match.group(1)

    # Strip vault path prefix  (e.g. "sigil-of-uchma/Content/")
    inner = re.sub(r"^sigil-of-uchma/(?:[^/]+/)*", "", inner)

    page = inner
    section = None
    alias = None

    # Split alias
    if "|" in page:
        page, alias = page.split("|", 1)

    # Split section anchor
    if "#" in page:
        page, section = page.split("#", 1)

    page = page.strip()
    section = section.strip() if section else None
    section_slug = slugify(section) if section else None

    # Self-reference (empty page or same page)
    if not page or page == current_page:
        display = alias or section or page or ""
        anchor = f"#{section_slug}" if section_slug else ""
        return f"[{display}]({anchor})"

    url = lookup.get(page)
    if url is None:
        print(f"  WARNING: unresolved link [[{inner}]] (page '{page}' not in lookup)")
        return f"[{alias or page}](#)"

    display = alias or section or page
    anchor = f"#{section_slug}" if section_slug else ""
    return f"[{display}]({url}{anchor})"


def rewrite_wikilinks(
    content: str, lookup: dict[str, str], current_page: str
) -> str:
    """Replace all [[wikilinks]] in content with markdown links."""
    return re.sub(
        r"\[\[([^\]]+)\]\]",
        lambda m: resolve_wikilink(m, lookup, current_page),
        content,
    )


# ---------------------------------------------------------------------------
# Line break conversion
# ---------------------------------------------------------------------------

def add_line_breaks(content: str) -> str:
    """
    Add trailing double spaces so CommonMark renders line breaks.

    Obsidian (strict line breaks OFF) treats every newline as a <br>.
    CommonMark treats single newlines as spaces within a paragraph.
    Two trailing spaces force a <br> in CommonMark.

    Skips: frontmatter, fenced code blocks, HTML blocks, headings,
    table rows, and lines that already end with double spaces or \\.
    """
    lines = content.split("\n")
    result: list[str] = []

    in_frontmatter = False
    fm_fence: str | None = None
    in_code_block = False
    in_html_block = False
    html_tag: str | None = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        # --- Frontmatter (--- or +++) ---
        if i == 0 and stripped in ("---", "+++"):
            in_frontmatter = True
            fm_fence = stripped
            result.append(line)
            continue
        if in_frontmatter:
            if stripped == fm_fence:
                in_frontmatter = False
            result.append(line)
            continue

        # --- Fenced code blocks ---
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            result.append(line)
            continue
        if in_code_block:
            result.append(line)
            continue

        # --- HTML block-level elements ---
        if not in_html_block:
            html_match = re.match(
                r"<(table|div|details|section|aside|figure|pre)\b",
                stripped,
                re.IGNORECASE,
            )
            if html_match:
                in_html_block = True
                html_tag = html_match.group(1).lower()
                result.append(line)
                continue
        if in_html_block:
            if re.search(rf"</{html_tag}\s*>", stripped, re.IGNORECASE):
                in_html_block = False
                html_tag = None
            result.append(line)
            continue

        # --- Decide whether to add trailing spaces ---
        has_next = i + 1 < len(lines)
        next_non_empty = has_next and lines[i + 1].strip() != ""

        needs_break = (
            stripped != ""
            and next_non_empty
            and not stripped.startswith("#")   # headings
            and not stripped.startswith("|")   # table rows
            and not line.endswith("  ")        # already has break
            and not line.endswith("\\")        # backslash break
        )

        result.append(line + "  " if needs_break else line)

    return "\n".join(result)



# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"Repo root:  {REPO_ROOT}")
    print(f"Output dir: {CONTENT_DIR}")

    # Clean previous output
    if CONTENT_DIR.exists():
        shutil.rmtree(CONTENT_DIR)
    CONTENT_DIR.mkdir(parents=True)

    # Discover files and build lookup
    file_list = build_file_list(REPO_ROOT)
    lookup = build_lookup(file_list)

    print(f"\nFound {len(file_list)} source files")
    print(f"Page lookup ({len(lookup)} entries):")
    for name, url in sorted(lookup.items()):
        print(f"  {name}  →  {url}")

    # Process each file
    print("\nConverting:")
    for src, dest in file_list:
        dest_path = CONTENT_DIR / dest
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        content = src.read_text(encoding="utf-8")
        current_page = get_page_name(src)

        content = rewrite_wikilinks(content, lookup, current_page)
        content = add_line_breaks(content)

        dest_path.write_text(content, encoding="utf-8")
        print(f"  {src.relative_to(REPO_ROOT)}  →  {dest}")

    print("\nDone.")


if __name__ == "__main__":
    main()
