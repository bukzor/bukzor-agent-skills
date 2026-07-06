"""
Validate frontmatter in markdown files against JSON schemas.

Prevents errors by catching schema violations early.

Run via `bin/llm.kb-validate` (`python -m llmd.frontmatter_validate` under
the hood) -- not directly -- so this module always has a real parent
package and its own relative imports below just work.
"""

import argparse
import functools
import sys
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import cast, override

import yaml
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012, Schema, SchemaRegistry

from ._jsonschema_adapter import iter_schema_errors
from .types import JsonObj, JsonValue

SKILL_URI_SCHEME = 'skill://'
FILE_URI_SCHEME = 'file://'
SKILLS_HOME = Path.home() / '.claude' / 'skills'


def _resource_from_path(schema_path: Path) -> Resource[Schema]:
    contents = cast(Schema, yaml.safe_load(schema_path.read_text()))
    return Resource.from_contents(contents, default_specification=DRAFT202012)


@functools.lru_cache(maxsize=None)
def _retrieve_schema(uri: str) -> Resource[Schema]:
    """Resolve a schema `$ref` URI to a Resource.

    In-memory, filesystem-backed: no network fetch.

    - `skill://<skill>/<path>` resolves via `~/.claude/skills/<skill>/`,
      which is a symlink farm onto this repo, so this also transparently
      resolves same-repo cross-skill refs.
    - `file://<path>` is what a file-relative `$ref` resolves to, since
      `load_schema` gives every loaded schema a `file://` `$id` as a base.
    """
    if uri.startswith(SKILL_URI_SCHEME):
        skill, _, rel_path = uri[len(SKILL_URI_SCHEME):].partition('/')
        return _resource_from_path(SKILLS_HOME / skill / rel_path)
    elif uri.startswith(FILE_URI_SCHEME):
        return _resource_from_path(Path(uri[len(FILE_URI_SCHEME):]))
    else:
        raise ValueError(f"Unsupported $ref scheme (expected {SKILL_URI_SCHEME} or {FILE_URI_SCHEME}...): {uri}")


def clear_schema_cache() -> None:
    """Clear cached schema-retrieval results. Tests need this for isolation between fixtures."""
    _retrieve_schema.cache_clear()


_REGISTRY: SchemaRegistry = Registry(retrieve=_retrieve_schema)

SUFFIX = '.kb'
HIVE_PARTITION_MARKER = '='


@dataclass(frozen=True)
class ValidationResult:
    """One validation result."""
    depth: int
    kind: str  # 'dir', 'file'
    text: str
    errors: tuple[str, ...] = ()

    def __bool__(self) -> bool:
        return not self.errors

    @override
    def __str__(self) -> str:
        indent = "    " * self.depth
        match self.kind:
            case 'dir':
                return f"  {indent}{self.text}/"
            case 'file':
                icon = "✅" if self else "❌"
                lines = [f"{icon}{indent}{self.text}"]
                for error in self.errors:
                    lines.append(f"    {indent}{error}")
                return "\n".join(lines)
            case _:
                raise AssertionError(self.kind)


def validate_one_file(md_file: Path, schema_override: Path | None, depth: int) -> Iterator[ValidationResult]:
    """Validate one file, yielding output. Skips non-data files."""
    # CLAUDE.md is a maintenance guide; dotfiles (e.g. .template.md) are
    # meta-data conventions and not part of the .kb/ data corpus.
    if md_file.name == 'CLAUDE.md' or md_file.name.startswith('.'):
        return
    errors = validate_file(md_file, schema_override)
    yield ValidationResult(depth, 'file', md_file.name, errors=tuple(errors))


def without_children(paths: Iterable[Path]) -> Iterator[Path]:
    """Yield paths, skipping any that are children of already-yielded paths."""
    seen: set[Path] = set()
    for p in sorted(paths):
        if any(parent in seen for parent in p.parents):
            continue
        else:
            yield p
            seen.add(p)


def is_kb_dir(path: Path) -> bool:
    """Check if directory is a .kb/ or hive partition."""
    return path.is_dir() and (path.name.endswith(SUFFIX) or HIVE_PARTITION_MARKER in path.name)


def kb_subdirs(path: Path) -> list[Path]:
    """Get .kb/ and hive partition subdirectories."""
    return [d for d in sorted(path.iterdir()) if is_kb_dir(d)]


def validate_paths(paths: Iterator[Path], schema_override: Path | None = None, depth: int = 0) -> Iterator[ValidationResult]:
    """Recursively validate paths, yielding ValidationResult objects."""
    for path in paths:
        p = Path(path)

        if is_kb_dir(p):
            yield ValidationResult(depth, 'dir', p.name)

            for md_file in sorted(p.glob('*.md')):
                yield from validate_one_file(md_file, schema_override, depth + 1)

            yield from validate_paths(iter(kb_subdirs(p)), schema_override, depth + 1)

        elif p.is_dir():
            yield from validate_paths(without_children(p.glob(f'**/*{SUFFIX}')), schema_override, depth)

        elif p.is_file():
            yield from validate_one_file(p, schema_override, depth)


def extract_frontmatter(md_file: Path) -> str | None:
    """Extract YAML frontmatter from markdown file."""
    content = md_file.read_text()

    if not content.startswith('---\n'):
        return None

    # Find closing ---
    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return None

    return parts[1]


def load_schema(schema_file: Path) -> JsonObj | None:
    """Load JSON schema from YAML file.

    Injects a `file://` `$id` (the schema's own absolute path) when the
    schema doesn't declare one, giving file-relative `$ref`s a base URI
    to resolve against.
    """
    try:
        with open(schema_file) as f:
            schema = cast(JsonObj | None, yaml.safe_load(f))
    except Exception as e:
        print(f"Error loading schema: {e}", file=sys.stderr)
        return None
    if schema is not None and '$id' not in schema:
        schema['$id'] = Path(schema_file).resolve().as_uri()
    return schema


def validate_against_schema(data: JsonValue, schema: JsonObj) -> list[str]:
    """Validate frontmatter against a JSON Schema (Draft 2020-12).

    Delegates to the `jsonschema` reference implementation so every
    keyword in the spec is honored — pattern, minLength, minItems,
    nested properties, items, additionalProperties, oneOf/anyOf/allOf,
    if/then/else, $ref, and anything added in future drafts.
    """
    return iter_schema_errors(schema, data, _REGISTRY)


def validate_file(md_file: Path, schema_override: Path | None = None) -> list[str]:
    """Validate a single markdown file. Returns list of errors."""
    if not md_file.exists():
        return ["File not found"]

    frontmatter_yaml = extract_frontmatter(md_file)
    if frontmatter_yaml is None:
        return []

    try:
        data = cast(JsonValue, yaml.safe_load(frontmatter_yaml))
    except yaml.YAMLError as e:
        return [f"Invalid YAML: {e}"]

    # Auto-detect schema if not provided
    schema_file = schema_override
    if not schema_file:
        parent = md_file.parent.name
        if parent.endswith(SUFFIX):
            category = parent.removesuffix(SUFFIX)
            schema_file = md_file.parent.parent / f"{category}.jsonschema.yaml"
        else:
            return []  # Can't validate without schema

    schema_path = Path(schema_file)
    if not schema_path.exists():
        return [f"No schema found: {schema_file}"]

    schema = load_schema(schema_path)
    if schema is None:
        return ["Failed to load schema"]

    return validate_against_schema(data, schema)


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Validate markdown frontmatter against JSON schema'
    )
    _ = parser.add_argument('paths', nargs='*', default=['.'], help=f'Markdown files, {SUFFIX}/ directories, or directories containing {SUFFIX}/ subdirectories (default: .)')
    _ = parser.add_argument('--schema', help='Schema file (auto-detected if not provided)')

    args = parser.parse_args()
    paths = cast(list[str], args.paths)
    schema_arg = cast(str | None, args.schema)

    file_count = 0
    error_count = 0
    for result in validate_paths((Path(p) for p in paths), Path(schema_arg) if schema_arg else None):
        print(result)
        if result.kind == 'file':
            file_count += 1
            if not result:
                error_count += 1

    icon = "✅" if error_count == 0 else "❌"
    print(f"{icon} {file_count} files, {error_count} errors")

    sys.exit(0 if error_count == 0 else 2)


if __name__ == '__main__':
    main()
