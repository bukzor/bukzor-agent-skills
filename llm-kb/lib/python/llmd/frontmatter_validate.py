"""
Validate frontmatter in markdown files against JSON schemas.

Prevents errors by catching schema violations early.

Run via `bin/llm.kb-validate` (`python -m llmd.frontmatter_validate` under
the hood) -- not directly -- so this module always has a real parent
package and its own relative imports below just work.
"""

import argparse
import functools
import subprocess
import sys
import urllib.parse
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import cast, override

import yaml
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012, Schema, SchemaRegistry, UnknownDialect, specification_with

from ._jsonschema_adapter import DIALECT_URI, iter_schema_errors
from .types import JsonObj, JsonValue

SKILL_URI_SCHEME = 'skill://'
FILE_URI_SCHEME = 'file://'
SKILLS_HOME = Path.home() / '.claude' / 'skills'

# urljoin only resolves a relative $ref against schemes it knows are
# hierarchical. Without this, a file-relative $ref inside a schema fetched
# via skill:// (e.g. `todo.jsonschema.yaml`) doesn't join onto the skill://
# base -- it passes through unchanged and fails to resolve.
urllib.parse.uses_relative.append('skill')
urllib.parse.uses_netloc.append('skill')


def _resource_from_path(schema_path: Path) -> Resource[Schema]:
    contents = cast(Schema, yaml.safe_load(schema_path.read_text()))
    dialect = contents.get('$schema') if isinstance(contents, dict) else None
    if dialect == DIALECT_URI:
        # The referencing library can't know custom dialect URIs, so the llmd
        # dialect's 2020-12 referencing semantics are stated explicitly.
        # (Validator selection is separate: _jsonschema_adapter registers the
        # dialect so evolve() picks the llmd validator on $ref crossings.)
        return DRAFT202012.create_resource(contents)
    if isinstance(dialect, str):
        # Explicit lookup rather than from_contents(): its detect() silently
        # falls back to the default on an unknown dialect, and a dialect
        # nobody implements should be a loud schema bug, not a guess.
        try:
            specification = specification_with(dialect)
        except UnknownDialect as e:
            raise ValueError(f"{schema_path}: unknown $schema dialect {dialect!r}; expected {DIALECT_URI} or a standard JSON Schema dialect") from e
        return specification.create_resource(contents)
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
# The same finding as its sibling below, at a coarser resolution: there, the
# schema is named and absent; here, no name was reached. Which places the
# lookup reaches is the reference's subject and changes over time -- an error
# that recited the current reach would teach it as the rule.
NO_SCHEMA_FOUND = (
    "No schema found for this frontmatter."
    " Resolutions: skill://llm-kb/references/frontmatter-outside-a-collection.md"
)
# git's wording for the absence of a repository, stable since forever. Should
# it ever change, the tests below fail rather than users.
NO_REPOSITORY = 'not a git repository'


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
    # Skipped because their location is forced, not because their frontmatter
    # is uninteresting: a maintenance guide governs the collection it sits in,
    # and a dotfile (e.g. .template.md) states the collection's conventions, so
    # both must live inside a `.kb/` without being members of it. A file merely
    # outside every collection fails that test and gets the ordinary verdict.
    if md_file.name == 'CLAUDE.md' or md_file.name.startswith('.'):
        return
    errors = validate_file(md_file, schema_override)
    yield ValidationResult(depth, 'file', md_file.name, errors=tuple(errors))


def glob_prune(paths: Iterable[Path]) -> Iterator[Path]:
    """Drop what lies under a path already yielded, as find(1) `-prune`.

    A `**` glob finds nested collections at every depth; the walk descends
    into those itself, so passing them along again validates them twice.
    Unlike `-prune` this cannot stop the descent -- the glob has already
    paid for it -- it only declines to pass the results on.
    """
    seen: set[Path] = set()
    for p in sorted(paths):
        if any(parent in seen for parent in p.parents):
            continue
        else:
            yield p
            seen.add(p)


def ignored_by_git(path: Path) -> bool:
    """Whether git ignores `path`, asked of the repository that holds it.

    Each path is asked where it lives, so a submodule answers for its own
    contents -- ask the superproject and it refuses outright, "Pathspec ...
    is in submodule". `check-ignore` performs git's own repository
    discovery, which is why nothing here goes looking for a `.git`.

    Any refusal but that one raises, with git's diagnosis already on the
    terminal: a filter that quietly stops filtering quietly changes which
    files get validated.
    """
    # Absolute both sides: git reads a relative pathspec against `-C`, not
    # the caller's cwd.
    path = path.resolve()
    command = ('git', '-C', str(path if path.is_dir() else path.parent), 'check-ignore', '-q', str(path))
    completed = subprocess.run(command, stderr=subprocess.PIPE, text=True)

    if completed.returncode > 1 and NO_REPOSITORY in completed.stderr:
        return False  # the one refusal that is an answer: no repository, nothing ignored
    else:
        _ = sys.stderr.write(completed.stderr)  # git's complaints are the user's

    # -q leaves the answer in the exit code alone.
    match completed.returncode:
        case 0:
            return True
        case 1:
            return False
        case code:
            raise subprocess.CalledProcessError(code, command)


def corpus(root: Path, found: Iterable[Path]) -> Iterator[Path]:
    """Those of `found` that count as corpus: what git ignores is scratch.

    A `.kb/` under `trash/` or `node_modules/` is somebody's scratch, and its
    schema rot padding the error count teaches the reader to skip the count.
    Only what the walk discovered can be dropped this way -- `root` was named
    on the command line, so if it is itself ignored, asking was asking and
    everything under it is validated.
    """
    if ignored_by_git(root):
        return iter(found)
    else:
        return (path for path in found if not ignored_by_git(path))


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

            yield from validate_paths(corpus(p, kb_subdirs(p)), schema_override, depth + 1)

        elif p.is_dir():
            yield from validate_paths(corpus(p, glob_prune(p.glob(f'**/*{SUFFIX}'))), schema_override, depth)

        elif p.is_file():
            yield from validate_one_file(p, schema_override, depth)

        else:
            # Named on the command line and neither collection, directory, nor
            # file -- a mistyped path. Reported rather than passed over: having
            # validated nothing must never read as having found nothing wrong.
            yield ValidationResult(depth, 'file', p.name, errors=('File not found',))


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


def schema_for(md_file: Path) -> Path | None:
    """The schema a file's location puts it under, or None if none does.

    A file in `X.kb/` is governed by `X.jsonschema.yaml` beside that
    directory. A hive partition (`year=2026/`) subdivides a collection
    without renaming it, so the walk up passes through any number of them
    to reach the `.kb/` they partition.
    """
    directory = md_file.parent
    while HIVE_PARTITION_MARKER in directory.name:
        directory = directory.parent

    if directory.name.endswith(SUFFIX):
        category = directory.name.removesuffix(SUFFIX)
        return directory.parent / f"{category}.jsonschema.yaml"
    else:
        return None


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

    schema_file = schema_override or schema_for(md_file)
    if schema_file is None:
        return [NO_SCHEMA_FOUND]

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
