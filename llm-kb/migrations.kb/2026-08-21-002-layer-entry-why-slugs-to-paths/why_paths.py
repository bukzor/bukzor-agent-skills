#!/usr/bin/env python3
"""Classify and rewrite `why:` motivation edges in design-tower layer entries.

Guarantees, per the canonical
`skill://llm-design-kb/jsonschema/layer-entry.jsonschema.yaml`: every `why:`
item is a file-relative path ending in `.md` that resolves to an existing
file.

`validate` is read-only and prints one tab-separated record per finding,
`VERDICT<TAB>file<TAB>item<TAB>detail`; it exits 1 when any finding is not
`OK`. `migrate` rewrites exactly the `RESOLVED` findings in place and is a
byte-identical no-op on a tree it has already converted -- a rewritten item
ends in `.md`, so it is never a slug again.

A slug is rewritten only when exactly one entry in its own tower bears that
stem. Ambiguous and unresolvable slugs are reported, never guessed: a wrong
path is worse than a reported one.
"""

from __future__ import annotations

import os
import re
import sys
from collections.abc import Iterator, Mapping, Sequence
from pathlib import Path

import yaml

# Copies, not additional towers: a worktree or replication checkout mirrors a
# tree that is migrated at its real path, and rewriting both doubles the diff
# for no gain. `trash/` is scratch by house convention.
PRUNE_NAMES = frozenset(
    {".git", ".venv", ".cache", ".direnv", "node_modules", "trash", "worktrees"}
)
PRUNE_SUFFIXES = ("--replication-run",)

NUMBERED_LAYER = re.compile(r"^0\d\d-.*\.kb$")
FRONTMATTER = re.compile(r"\A---\n(.*?\n)---\n", re.DOTALL)


def is_pruned(name: str) -> bool:
    return name in PRUNE_NAMES or name.endswith(PRUNE_SUFFIXES)


def is_tower(directory: Path) -> bool:
    """A design tower: a layer collection, by name or by numbered layers.

    Named `design`/`design.kb`/`<topic>.design.kb`, or holding numbered
    `0NN-*.kb/` layers -- which is what catches towers under a project-specific
    name such as `design-next.kb`.
    """
    name = directory.name
    if name in ("design", "design.kb") or name.endswith(".design.kb"):
        return True
    else:
        return any(
            NUMBERED_LAYER.match(child.name)
            for child in directory.iterdir()
            if child.is_dir()
        )


def find_towers(roots: Sequence[Path]) -> list[Path]:
    towers: list[Path] = []
    for root in roots:
        for dirpath, dirnames, _ in os.walk(root):
            dirnames[:] = sorted(d for d in dirnames if not is_pruned(d))
            directory = Path(dirpath)
            if directory != root and is_tower(directory):
                towers.append(directory)
                dirnames.clear()
    return sorted(towers)


def entry_files(tower: Path) -> list[Path]:
    """Every candidate entry in the tower: its `.md` files, minus the
    maintenance guides, which carry no frontmatter."""
    return sorted(
        path
        for path in tower.rglob("*.md")
        if path.name != "CLAUDE.md" and not any(is_pruned(p) for p in path.parts)
    )


def stem_keys(path: Path) -> Iterator[str]:
    """The names a slug could have used for this entry: its stem, and -- for a
    tower root such as `010-mission.md` -- the stem without its layer number,
    which is how every observed slug names it."""
    yield path.stem
    unnumbered = re.sub(r"^0\d\d-", "", path.stem)
    if unnumbered != path.stem:
        yield unnumbered


def stem_index(files: Sequence[Path]) -> Mapping[str, Sequence[Path]]:
    index: dict[str, list[Path]] = {}
    for path in files:
        for key in stem_keys(path):
            index.setdefault(key, []).append(path)
    return index


def project_root(tower: Path) -> Path:
    """The repository containing the tower -- the scope across which a
    sibling tower's entries are addressable."""
    for directory in tower.parents:
        if (directory / ".git").exists():
            return directory
    else:
        return tower


def why_items(text: str) -> Sequence[str]:
    match = FRONTMATTER.match(text)
    if match is None:
        return ()
    else:
        front = yaml.safe_load(match.group(1))
        if not isinstance(front, dict) or "why" not in front:
            return ()
        else:
            why = front["why"]
            assert isinstance(why, list), (type(why), why)
            assert all(isinstance(item, str) for item in why), why
            return tuple(why)


def bearers_of(
    entry: Path, item: str, scopes: Sequence[Mapping[str, Sequence[Path]]]
) -> Sequence[Path]:
    """Entries a slug could name, from the narrowest scope that knows it.

    Narrowest-first is what keeps a project-wide index from manufacturing
    ambiguity for a slug its own tower already answers unambiguously. The
    entry itself is never a candidate: a `why:` self-loop is meaningless, so
    a same-named entry one layer up is the only reading.
    """
    for index in scopes:
        bearers = [path for path in index.get(item, ()) if path != entry]
        if bearers:
            return bearers
    else:
        return ()


def classify(
    entry: Path,
    item: str,
    tower: Path,
    scopes: Sequence[Mapping[str, Sequence[Path]]],
):
    """Verdict and detail for one `why:` item; detail is the replacement text
    for any verdict `migrate` acts on.

    OK -- a file-relative path that resolves.
    RESOLVED -- a slug, or a tower-root-relative path, with one reading.
    AMBIGUOUS / UNRESOLVABLE / DANGLING -- reported, never guessed.
    """
    if item.endswith(".md"):
        if (entry.parent / item).is_file():
            return ("OK", item)
        elif (tower / item).is_file():
            return ("RESOLVED", os.path.relpath(tower / item, entry.parent))
        else:
            return ("DANGLING", item)
    else:
        bearers = bearers_of(entry, item, scopes)
        if len(bearers) == 1:
            return ("RESOLVED", os.path.relpath(bearers[0], entry.parent))
        elif bearers:
            return ("AMBIGUOUS", " ".join(str(b) for b in bearers))
        else:
            return ("UNRESOLVABLE", item)


def findings(roots: Sequence[Path]) -> Iterator[tuple[str, Path, str, str]]:
    towers = {tower: entry_files(tower) for tower in find_towers(roots)}
    projects: dict[Path, list[Path]] = {}
    for tower, files in towers.items():
        projects.setdefault(project_root(tower), []).extend(files)
    indexes = {scope: stem_index(files) for scope, files in projects.items()}
    for tower, files in towers.items():
        scopes = (stem_index(files), indexes[project_root(tower)])
        for entry in files:
            for item in why_items(entry.read_text()):
                verdict, detail = classify(entry, item, tower, scopes)
                yield verdict, entry, item, detail


def rewrite(text: str, replacements: Mapping[str, str]) -> str:
    """The document with each named `why:` item replaced by its path.

    Line-surgical rather than a YAML round-trip: reserializing would reflow
    every other field of every frontmatter it touches.
    """
    match = FRONTMATTER.match(text)
    assert match is not None, text[:200]
    lines = match.group(1).split("\n")
    in_why = False
    for i, line in enumerate(lines):
        if not line.startswith((" ", "-", "\t")):
            in_why = line.startswith("why:")
            assert not (in_why and line.strip() != "why:"), line
        elif in_why:
            stripped = line.strip()
            assert stripped.startswith("- "), line
            item = stripped[2:].strip()
            if item in replacements:
                lines[i] = line.replace(item, replacements[item], 1)
    return text.replace(match.group(1), "\n".join(lines), 1)


def write_migrated(entry: Path, replacements: Mapping[str, str]) -> None:
    entry.write_text(rewrite(entry.read_text(), replacements))


def proc_validate(roots: Sequence[Path]) -> int:
    worst = 0
    for verdict, entry, item, detail in findings(roots):
        if verdict != "OK":
            worst = 1
            print(f"{verdict}\t{entry}\t{item}\t{detail}")
    return worst


def proc_migrate(roots: Sequence[Path]) -> int:
    pending: dict[Path, dict[str, str]] = {}
    for verdict, entry, item, detail in findings(roots):
        if verdict == "RESOLVED":
            pending.setdefault(entry, {})[item] = detail
    for entry, replacements in sorted(pending.items()):
        write_migrated(entry, replacements)
        print(f"REWROTE\t{entry}\t{len(replacements)}")
    return 0


def main() -> int:
    command, *args = sys.argv[1:]
    roots = [Path(a).resolve() for a in args] or [
        Path.home() / "repo",
        Path.home() / "claude",
    ]
    match command:
        case "validate":
            return proc_validate(roots)
        case "migrate":
            return proc_migrate(roots)
        case _:
            raise AssertionError(command)


if __name__ == "__main__":
    sys.exit(main())
