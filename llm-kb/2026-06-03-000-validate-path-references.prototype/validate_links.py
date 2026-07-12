"""
Check that path-valued frontmatter fields and inline body links in .kb/
markdown files resolve to real files on disk.

Born out of the Abby's Craft design.kb breakdown (2026-07-09): sanity-checking
~150 hand-written why:/depends:/candidate-resolutions:/... cross-references
across 83 files. `bin/llm.kb-validate` (llmd.frontmatter_validate) checks that
frontmatter conforms to its JSON schema, but a schema only constrains e.g. a
why: field to be "an array of strings" -- it has no way to know those strings
are supposed to be paths that resolve. A typo'd why: link currently passes
schema validation silently and just becomes a broken chain, discoverable only
by a human clicking through.

Scratch/prototype, run standalone (only depends on PyYAML) -- not wired into
bin/llm.kb-validate yet. See README.md in this directory for the integration
recommendation.

Usage:
    python3 validate_links.py [paths...]   # default: .
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterator
from itertools import chain
from pathlib import Path

import yaml

# Frontmatter fields (across llm-kb, llm-design-kb, llm-discourse-graph
# schemas) whose values are file-relative paths to other .kb/ nodes.
LINK_FIELDS = (
    'why', 'depends', 'source', 'sources',
    'candidate-resolutions', 'conclusion', 'premises', 'resolved',
)

# Backtick-wrapped file-relative markdown links in body prose, e.g. `../foo.md`.
BODY_LINK_RE = re.compile(r'`(\.\.?/[^`]+\.md)`')


def extract_frontmatter(md_file: Path) -> str | None:
    """Extract raw YAML frontmatter text, or None if the file has none.

    Duplicated from llmd.frontmatter_validate rather than imported, since
    this lives outside the package while it's still scratch -- fold into
    that module (reusing its extract_frontmatter) on integration.
    """
    content = md_file.read_text()
    if not content.startswith('---\n'):
        return None
    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return None
    return parts[1]


def frontmatter_links(md_file: Path) -> Iterator[tuple[str, str]]:
    """Yield (field, path) for every path-shaped value in known link fields."""
    raw = extract_frontmatter(md_file)
    if raw is None:
        return
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError:
        return  # frontmatter_validate.py already reports YAML errors
    if not isinstance(data, dict):
        return
    for field_name in LINK_FIELDS:
        value = data.get(field_name)
        if value is None:
            continue
        values = value if isinstance(value, list) else [value]
        for v in values:
            if isinstance(v, str) and v.startswith(('./', '../')):
                yield field_name, v


def body_links(md_file: Path) -> Iterator[tuple[str, str]]:
    """Yield ('body', path) for every backtick-wrapped relative .md link in prose."""
    for match in BODY_LINK_RE.finditer(md_file.read_text()):
        yield 'body', match.group(1)


def broken_links(md_file: Path) -> list[str]:
    """Return one error string per link that doesn't resolve to a real file."""
    errors = []
    for field_name, link in chain(frontmatter_links(md_file), body_links(md_file)):
        target = (md_file.parent / link).resolve()
        if not target.is_file():
            errors.append(f"{field_name}: {link} -> {target} (missing)")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    _ = parser.add_argument('paths', nargs='*', default=['.'], help='.md files or directories to scan recursively (default: .)')
    args = parser.parse_args()
    paths = [Path(p) for p in args.paths]

    files: list[Path] = []
    for p in paths:
        files.extend([p] if p.is_file() else sorted(p.glob('**/*.md')))

    file_count = 0
    error_count = 0
    for md_file in files:
        file_count += 1
        errors = broken_links(md_file)
        if errors:
            error_count += 1
            print(f"❌ {md_file}")
            for e in errors:
                print(f"    {e}")

    icon = "✅" if error_count == 0 else "❌"
    print(f"{icon} {file_count} files, {error_count} with broken links")
    sys.exit(0 if error_count == 0 else 2)


if __name__ == '__main__':
    main()
