"""Read a claim ledger kept as files -- the directory form of `Skill(llm-claims)`.

One theory per `*.kb/` collection, one claim per file, label and standing in
frontmatter (`jsonschema/claim.jsonschema.yaml`); the theory's own defining
claim is the `prior:`/`ontology:`/`defeated by:` header of its `CLAUDE.md`.
The `llm-claims-kb-*` tools all read a ledger through here, so the schema has one
parser and the tools disagree only about rendering.

Tolerant by design: a theory header may be absent or partial, and a `why:` may
point nowhere. Reporting those is each tool's business, not the reader's --
`dangling()` and the `None`s are what it hands them to report with.
"""

import os
import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import cast

import yaml

# The sigil each standing spells out.
SIGIL = {"bare": "", "open": "?", "agent": "+", "user": "!"}


@dataclass(frozen=True)
class Claim:
    id: str  # `<theory>/<stem>` -- ledger-wide identity
    theory: str
    stem: str
    label: str
    standing: str
    why: tuple[str, ...]  # claim ids, resolved from file-relative paths
    verify: str | None  # the CHECK of `-- certified(CHECK)`
    authority: str | None  # the act that settled the standing
    url: str  # the claim file, so a drawn node is a way in
    gist: str  # opening paragraph: the claim itself


@dataclass(frozen=True)
class Theory:
    name: str
    priors: tuple[str, ...]
    ontology: str | None  # the words it admits -- absent if unheadered
    defeater: str | None


@dataclass(frozen=True)
class Ledger:
    name: str
    theories: tuple[Theory, ...]
    claims: tuple[Claim, ...]


def claim_id(path: Path) -> str:
    """`<theory>/<stem>`, with `..` segments of a `why:` path collapsed."""
    clean = Path(os.path.normpath(path))
    return f"{clean.parent.name.removesuffix('.kb')}/{clean.stem}"


def split_frontmatter(text: str) -> tuple[Mapping[str, object], str]:
    """The frontmatter mapping, and the body that follows it."""
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    assert match is not None, text[:200]
    loaded = cast(Mapping[str, object], yaml.safe_load(match.group(1)))
    assert isinstance(loaded, dict), loaded
    return loaded, text[match.end() :]


def first_paragraph(body: str) -> str:
    """The claim itself: the paragraph after the title, whitespace collapsed."""
    blocks = (block.strip() for block in body.split("\n\n"))
    paragraphs = (block for block in blocks if block and not block.startswith("#"))
    return " ".join(next(paragraphs, "").split())


def header_bullet(text: str, key: str) -> str | None:
    """The `- ``key:`` ...` theory-header bullet, continuation lines joined."""
    match = re.search(
        rf"^- `{key}:`(.*?)(?=^- `|\n\n|\Z)", text, re.MULTILINE | re.DOTALL
    )
    return None if match is None else " ".join(match.group(1).split())


def strip_marks(value: str | None) -> str | None:
    """A header bullet's prose, without the dashes that introduced it."""
    return None if value is None else value.strip(" `-–—") or None


def parse_priors(value: str | None) -> tuple[str, ...]:
    """Theory names cited as priors; every spelling of "none" yields none.

    A `prior:` bullet may gloss its answer after a dash -- `none -- root
    theory` -- so the gloss is cut before the names are read; a theory name
    is one word, and everything after the first is prose.
    """
    stated = re.split(r"\s[-–—]{1,2}\s", strip_marks(value) or "")[0]
    names = (item.strip(" `").split(" ")[0] for item in stated.split(","))
    return tuple(name.removesuffix(".kb") for name in names if name and name != "none")


def read_claim(path: Path) -> Claim:
    front, body = split_frontmatter(path.read_text())
    label, standing, why = front["label"], front["standing"], front.get("why", [])
    verify, authority = front.get("verify"), front.get("authority")
    assert isinstance(label, str), label
    assert isinstance(standing, str) and standing in SIGIL, standing
    assert isinstance(why, list), why
    assert verify is None or isinstance(verify, str), verify
    assert authority is None or isinstance(authority, str), authority
    return Claim(
        id=claim_id(path),
        theory=path.parent.name.removesuffix(".kb"),
        stem=path.stem,
        label=label,
        standing=standing,
        why=tuple(
            claim_id(path.parent / str(entry)) for entry in cast(list[object], why)
        ),
        verify=verify,
        authority=authority,
        url=path.resolve().as_uri(),
        gist=first_paragraph(body),
    )


def read_theory(kb: Path) -> Theory:
    header = kb / "CLAUDE.md"
    text = header.read_text() if header.exists() else ""
    return Theory(
        name=kb.name.removesuffix(".kb"),
        priors=parse_priors(header_bullet(text, "prior")),
        ontology=strip_marks(header_bullet(text, "ontology")),
        defeater=strip_marks(header_bullet(text, "defeated by")),
    )


def read_ledger(root: Path) -> Ledger:
    theories: list[Theory] = []
    claims: list[Claim] = []
    for kb in sorted(root.glob("*.kb")):
        theories.append(read_theory(kb))
        claims.extend(
            read_claim(md) for md in sorted(kb.glob("*.md")) if md.name != "CLAUDE.md"
        )
    assert theories, root
    return Ledger(
        name=root.name.removesuffix(".claims.kb"),
        theories=tuple(theories),
        claims=tuple(claims),
    )


def dangling(ledger: Ledger) -> tuple[str, ...]:
    """Cited claim ids that no file defines."""
    known = {claim.id for claim in ledger.claims}
    cited = {prior for claim in ledger.claims for prior in claim.why}
    return tuple(sorted(cited - known))
