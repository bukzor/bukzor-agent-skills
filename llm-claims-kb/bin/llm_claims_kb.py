"""Read a claim ledger kept as files -- the directory form of `Skill(llm-claims)`.

One claim per file, label and standing in frontmatter
(`jsonschema/claim.jsonschema.yaml`). A theory is one of those claims and not
a second kind of thing: `<theory>.md` states the ontology in its body and its
`ontology:`, its `why:` names the priors, and the claims confined to it are
the sibling `<theory>.kb/`.

One rule holds at every depth -- a `.md` beside a `.kb/` of the same name
defines that theory, a `.md` alone is a claim -- so the shape nests without
limit, and the ledger itself is the outermost instance of it:
`<name>.claims.md` is the defining claim of `<name>.claims.kb/`.

The `llm-claims-kb-*` tools all read a ledger through here, so the schema has
one parser and the tools disagree only about rendering.

Tolerant by design: a theory may have no defining claim yet, and a `why:` may
point nowhere. Reporting those is each tool's business, not the reader's --
`dangling()`, `Theory.defining` and the `None`s are what it hands them to
report with.
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
    id: str  # path under the ledger's parent, unsuffixed -- ledger-wide identity
    scope: str  # the id of the theory it is confined to
    stem: str
    label: str
    standing: str
    why: tuple[str, ...]  # claim ids, resolved from file-relative paths
    verify: str | None  # the CHECK of `-- certified(CHECK)`
    authority: str | None  # the act that settled the standing
    ontology: tuple[str, ...]  # the words stipulated -- defining claims only
    defeater: str | None  # what would retire the theory -- defining claims only
    path: Path  # the claim file, so a drawn node is a way in
    gist: str  # opening paragraph: the claim itself

    @property
    def url(self) -> str:
        return self.path.resolve().as_uri()


@dataclass(frozen=True)
class Theory:
    name: str  # its defining claim's id: `design.claims/notation`
    path: Path  # the collection itself -- an id is not a path, only a handle
    defining: Claim | None  # absent until someone writes `<name>.md`
    claims: tuple[Claim, ...]  # confined to it; its sub-theories' are their own

    @property
    def stem(self) -> str:
        """The collection's own name, for a reader who has the tree in view."""
        return self.name.rpartition("/")[2]

    @property
    def container(self) -> str:
        """The theory this one sits inside; empty for the ledger's own theory.

        Containment admits: a nested theory reads in every word its container
        stipulates, which is why nesting needs no `why:` to say so.
        """
        return self.name.rpartition("/")[0]

    @property
    def label(self) -> str:
        """What claims cite it by -- the directory name, until it is defined."""
        fallback = re.sub(r"[^A-Z0-9]+", "_", self.stem.upper())
        return self.defining.label if self.defining else fallback

    @property
    def standing(self) -> str:
        """A theory's standing is its defining claim's; unwritten, no one has signed."""
        return self.defining.standing if self.defining else "open"

    @property
    def priors(self) -> tuple[str, ...]:
        return self.defining.why if self.defining else ()

    @property
    def ontology(self) -> tuple[str, ...]:
        return self.defining.ontology if self.defining else ()

    @property
    def defeater(self) -> str | None:
        return self.defining.defeater if self.defining else None


@dataclass(frozen=True)
class Ledger:
    name: str
    root: Path
    theories: tuple[Theory, ...]  # flattened: a nested theory stands beside its parent

    @property
    def origin(self) -> Path:
        """What claim ids are relative to -- the directory the ledger sits in."""
        return self.root.parent

    @property
    def claims(self) -> tuple[Claim, ...]:
        """Every claim file, each theory's defining claim among them."""
        return tuple(
            claim
            for theory in self.theories
            for claim in (*filter(None, [theory.defining]), *theory.claims)
        )


def claim_id(origin: Path, path: Path) -> str:
    """A claim's identity: its path under the ledger's parent, suffixes cut.

    The origin is the parent and not the ledger root because the ledger's own
    defining claim sits beside the root -- `design.claims.md` names the theory
    `design.claims`, whose claims are `design.claims/notation` and below.

    `why:` paths are file-relative and get here already joined to the citing
    file's directory, `..` segments and all. One that climbs out of the ledger
    keeps its path as its id, so it dangles visibly rather than colliding.
    """
    relative = Path(os.path.relpath(os.path.normpath(path), os.path.normpath(origin)))
    directories = [part.removesuffix(".kb") for part in relative.parts[:-1]]
    return "/".join([*directories, relative.stem])


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


def read_claim(origin: Path, path: Path) -> Claim:
    front, body = split_frontmatter(path.read_text())
    assert "label" in front, f"{path}: no `label:`, so this file is no claim"
    label, standing, why = front["label"], front["standing"], front.get("why", [])
    verify, authority = front.get("verify"), front.get("authority")
    ontology, defeater = front.get("ontology", []), front.get("defeated-by")
    assert isinstance(label, str), label
    assert isinstance(standing, str) and standing in SIGIL, standing
    assert isinstance(why, list), why
    assert verify is None or isinstance(verify, str), verify
    assert authority is None or isinstance(authority, str), authority
    assert isinstance(ontology, list), ontology
    assert defeater is None or isinstance(defeater, str), defeater
    identity = claim_id(origin, path)
    return Claim(
        id=identity,
        scope=identity.rpartition("/")[0],
        stem=path.stem,
        label=label,
        standing=standing,
        why=tuple(
            claim_id(origin, path.parent / str(entry))
            for entry in cast(list[object], why)
        ),
        verify=verify,
        authority=authority,
        ontology=tuple(str(word) for word in cast(list[object], ontology)),
        defeater=defeater,
        path=path,
        gist=first_paragraph(body),
    )


def defining_claim(collection: Path) -> Path:
    """Where a collection's defining claim lives: beside it, sharing its name."""
    return collection.parent / f"{collection.name.removesuffix('.kb')}.md"


def read_theory(origin: Path, collection: Path) -> Theory:
    """One theory: the claim that defines it, and the claims confined to it.

    A `.md` that defines a nested theory is that theory's, not this one's --
    a defining claim lives at the scope its ontology governs, one level up
    from the claims it admits words for.
    """
    defining = defining_claim(collection)
    confined = [
        md
        for md in sorted(collection.glob("*.md"))
        if md.name != "CLAUDE.md" and not (collection / f"{md.stem}.kb").is_dir()
    ]
    return Theory(
        name=claim_id(origin, defining),
        path=collection,
        defining=read_claim(origin, defining) if defining.exists() else None,
        claims=tuple(read_claim(origin, md) for md in confined),
    )


def read_theories(origin: Path, collection: Path) -> tuple[Theory, ...]:
    """Every theory inside a collection, and every theory inside those."""
    return tuple(
        theory
        for nested in sorted(collection.glob("*.kb"))
        for theory in (read_theory(origin, nested), *read_theories(origin, nested))
    )


def read_ledger(root: Path) -> Ledger:
    """The ledger, outermost theory first: it is one, and nests like the rest."""
    origin = root.parent
    return Ledger(
        name=root.name.removesuffix(".claims.kb"),
        root=root,
        theories=(read_theory(origin, root), *read_theories(origin, root)),
    )


def dangling(ledger: Ledger) -> tuple[str, ...]:
    """Cited claim ids that no file defines."""
    known = {claim.id for claim in ledger.claims}
    cited = {prior for claim in ledger.claims for prior in claim.why}
    return tuple(sorted(cited - known))
