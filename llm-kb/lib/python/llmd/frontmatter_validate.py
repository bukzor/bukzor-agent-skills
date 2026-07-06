#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "pyyaml",
#   "jsonschema",
# ]
# ///
"""
Validate frontmatter in markdown files against JSON schemas.

Prevents errors by catching schema violations early.
"""

import sys
import datetime
import functools
import yaml
from pathlib import Path
from dataclasses import dataclass
import argparse

from jsonschema import Draft202012Validator
from jsonschema.validators import extend
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012


def _is_date(_checker, instance):
    return isinstance(instance, datetime.date) and not isinstance(instance, datetime.datetime)


def _is_instant(_checker, instance):
    return isinstance(instance, datetime.datetime) and instance.tzinfo is not None


# YAML emits datetime.date and datetime.datetime natively; JSON Schema has no
# matching types. `date` accepts a calendar day; `instant` accepts a tz-aware
# point in time. Naive datetime is intentionally unaccepted — pick one.
_TYPE_CHECKER = Draft202012Validator.TYPE_CHECKER.redefine_many({
    "date": _is_date,
    "instant": _is_instant,
})

SKILL_URI_SCHEME = 'skill://'
SKILLS_HOME = Path.home() / '.claude' / 'skills'


@functools.lru_cache(maxsize=None)
def _retrieve_skill(uri):
    """Resolve `skill://<skill>/<path>` to a schema Resource.

    In-memory, filesystem-backed: no network fetch. `<skill>` resolves via
    `~/.claude/skills/<skill>/`, which is a symlink farm onto this repo, so
    this also transparently resolves same-repo cross-skill refs.
    """
    if not uri.startswith(SKILL_URI_SCHEME):
        raise ValueError(f"Unsupported $ref scheme (expected {SKILL_URI_SCHEME}...): {uri}")
    skill, _, rel_path = uri[len(SKILL_URI_SCHEME):].partition('/')
    schema_path = SKILLS_HOME / skill / rel_path
    contents = yaml.safe_load(schema_path.read_text())
    return Resource.from_contents(contents, default_specification=DRAFT202012)


_REGISTRY = Registry(retrieve=_retrieve_skill)

KbValidator = extend(Draft202012Validator, type_checker=_TYPE_CHECKER)

SUFFIX = '.kb'
HIVE_PARTITION_MARKER = '='


@dataclass(frozen=True)
class ValidationResult:
    """One validation result."""
    depth: int
    kind: str  # 'dir', 'file'
    text: str
    errors: tuple[str, ...] = ()

    def __bool__(self):
        return not self.errors

    def __str__(self):
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


def validate_one_file(md_file, schema_override, depth):
    """Validate one file, yielding output. Skips non-data files."""
    # CLAUDE.md is a maintenance guide; dotfiles (e.g. .template.md) are
    # meta-data conventions and not part of the .kb/ data corpus.
    if md_file.name == 'CLAUDE.md' or md_file.name.startswith('.'):
        return
    errors = validate_file(md_file, schema_override)
    yield ValidationResult(depth, 'file', md_file.name, errors=tuple(errors))


def without_children(paths):
    """Yield paths, skipping any that are children of already-yielded paths."""
    seen = set()
    for p in sorted(paths):
        if any(parent in seen for parent in p.parents):
            continue
        else:
            yield p
            seen.add(p)


def is_kb_dir(path):
    """Check if directory is a .kb/ or hive partition."""
    return path.is_dir() and (path.name.endswith(SUFFIX) or HIVE_PARTITION_MARKER in path.name)


def kb_subdirs(path):
    """Get .kb/ and hive partition subdirectories."""
    return [d for d in sorted(path.iterdir()) if is_kb_dir(d)]


def validate_paths(paths, schema_override=None, depth=0):
    """Recursively validate paths, yielding ValidationResult objects."""
    for path in paths:
        p = Path(path)

        if is_kb_dir(p):
            yield ValidationResult(depth, 'dir', p.name)

            for md_file in sorted(p.glob('*.md')):
                yield from validate_one_file(md_file, schema_override, depth + 1)

            yield from validate_paths(kb_subdirs(p), schema_override, depth + 1)

        elif p.is_dir():
            yield from validate_paths(without_children(p.glob(f'**/*{SUFFIX}')), schema_override, depth)

        elif p.is_file():
            yield from validate_one_file(p, schema_override, depth)


def extract_frontmatter(md_file):
    """Extract YAML frontmatter from markdown file."""
    content = md_file.read_text()

    if not content.startswith('---\n'):
        return None

    # Find closing ---
    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return None

    return parts[1]


def load_schema(schema_file):
    """Load JSON schema from YAML file."""
    try:
        with open(schema_file) as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading schema: {e}", file=sys.stderr)
        return None


def validate_against_schema(data, schema):
    """Validate frontmatter against a JSON Schema (Draft 2020-12).

    Delegates to the `jsonschema` reference implementation so every
    keyword in the spec is honored — pattern, minLength, minItems,
    nested properties, items, additionalProperties, oneOf/anyOf/allOf,
    if/then/else, $ref, and anything added in future drafts.
    """
    validator = KbValidator(schema, registry=_REGISTRY)
    errors = []
    for error in validator.iter_errors(data):
        path_parts = []
        for p in error.absolute_path:
            if isinstance(p, int):
                path_parts.append(f"[{p}]")
            else:
                path_parts.append(f".{p}" if path_parts else str(p))
        path = "".join(path_parts)
        prefix = f"{path}: " if path else ""
        errors.append(f"{prefix}{error.message}")
    return errors


def validate_file(md_file, schema_override=None):
    """Validate a single markdown file. Returns list of errors."""
    if not md_file.exists():
        return ["File not found"]

    frontmatter_yaml = extract_frontmatter(md_file)
    if frontmatter_yaml is None:
        return []

    try:
        data = yaml.safe_load(frontmatter_yaml)
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


def main():
    parser = argparse.ArgumentParser(
        description='Validate markdown frontmatter against JSON schema'
    )
    parser.add_argument('paths', nargs='*', default=['.'], help=f'Markdown files, {SUFFIX}/ directories, or directories containing {SUFFIX}/ subdirectories (default: .)')
    parser.add_argument('--schema', help='Schema file (auto-detected if not provided)')

    args = parser.parse_args()

    file_count = 0
    error_count = 0
    for result in validate_paths(args.paths, args.schema):
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
