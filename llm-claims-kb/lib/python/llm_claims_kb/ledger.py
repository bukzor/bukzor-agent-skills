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
point outside the ledger or nowhere at all. Reporting those is each tool's
business, not the reader's -- `foreign()`, `dangling()`, `Theory.defining` and
the `None`s are what it hands them to report with.
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
class Prior:
    """One `why:` entry: the claim id it names, and the file it named it by.

    Both, because a citation that lands outside this ledger has no id here to
    look up, and only the path can then say whether it is a reference or rot.
    """

    id: str
    path: Path


@dataclass(frozen=True)
class Claim:
    id: str  # path under the ledger's parent, unsuffixed -- ledger-wide identity
    scope: str  # the id of the theory it is confined to
    stem: str
    label: str
    standing: str
    verdict: str | None  # what was ruled, where the ruling went against the claim
    why: tuple[Prior, ...]  # what it rests on, in citation order
    verify: str | None  # the CHECK of `-- certified(CHECK)`
    authority: str | None  # the act that settled the standing
    ontology: tuple[str, ...]  # the words stipulated -- defining claims only
    stale_when: str | None  # what voids the theory's stamp -- defining claims only
    path: Path  # the claim file, so a drawn node is a way in
    gist: str  # opening paragraph: the claim itself

    @property
    def url(self) -> str:
        return self.path.resolve().as_uri()

    @property
    def cited_as(self) -> str:
        """Label and the sigil signing its judge, struck through where the
        judgment went against the claim.

        A struck label is the chat form's own mark for a verdict, and it names
        no word: which of them applies is in the claim's prose, and `grep
        LABEL` finds a struck line like any other. The strike has to reach the
        reference site, because that is where a lone sigil reads backwards --
        `!` on a rejected claim says the user signed it, when what they signed
        was its rejection.
        """
        said = f"{self.label}{SIGIL[self.standing]}"
        return f"~~{said}~~" if self.verdict else said


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
    def cited_as(self) -> str:
        """What claims cite it as: its defining claim's citation, or the
        fallback label under an open sigil until that claim is written."""
        return self.defining.cited_as if self.defining else f"{self.label}?"

    @property
    def priors(self) -> tuple[Prior, ...]:
        return self.defining.why if self.defining else ()

    @property
    def ontology(self) -> tuple[str, ...]:
        return self.defining.ontology if self.defining else ()

    @property
    def stale_when(self) -> str | None:
        return self.defining.stale_when if self.defining else None


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


def prior(origin: Path, source: Path, entry: str) -> Prior:
    """One `why:` entry resolved -- entries are file-relative, so they join to
    the directory of the claim doing the citing."""
    target = source.parent / entry
    return Prior(claim_id(origin, target), target)


def split_frontmatter(text: str) -> tuple[Mapping[str, object], str] | None:
    """The frontmatter mapping and the body that follows it, or None where the
    file opens with no frontmatter at all -- a `why:` may point at a schema or
    a todo, and a reader following one has to be able to come back empty."""
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        return None
    loaded = cast(Mapping[str, object], yaml.safe_load(match.group(1)))
    assert isinstance(loaded, dict), loaded
    return loaded, text[match.end() :]


def first_paragraph(body: str) -> str:
    """The claim itself: the paragraph after the title, whitespace collapsed."""
    blocks = (block.strip() for block in body.split("\n\n"))
    paragraphs = (block for block in blocks if block and not block.startswith("#"))
    return " ".join(next(paragraphs, "").split())


def read_claim(origin: Path, path: Path) -> Claim:
    split = split_frontmatter(path.read_text())
    assert split is not None, f"{path}: no frontmatter, so this file is no claim"
    front, body = split
    assert "label" in front, f"{path}: no `label:`, so this file is no claim"
    label, standing, why = front["label"], front["standing"], front.get("why", [])
    verdict, verify = front.get("verdict"), front.get("verify")
    authority = front.get("authority")
    ontology, stale_when = front.get("ontology", []), front.get("stale-when")
    # Renamed 2026-08-13. Reading past the old key would drop the line silently.
    assert "defeated-by" not in front, f"{path}: `defeated-by:` is now `stale-when:`"
    assert isinstance(label, str), label
    assert isinstance(standing, str) and standing in SIGIL, standing
    assert verdict is None or isinstance(verdict, str), verdict
    assert isinstance(why, list), why
    assert verify is None or isinstance(verify, str), verify
    assert authority is None or isinstance(authority, str), authority
    assert isinstance(ontology, list), ontology
    assert stale_when is None or isinstance(stale_when, str), stale_when
    identity = claim_id(origin, path)
    return Claim(
        id=identity,
        scope=identity.rpartition("/")[0],
        stem=path.stem,
        label=label,
        standing=standing,
        verdict=verdict,
        why=tuple(prior(origin, path, str(entry)) for entry in cast(list[object], why)),
        verify=verify,
        authority=authority,
        ontology=tuple(str(word) for word in cast(list[object], ontology)),
        stale_when=stale_when,
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


def undefined(ledger: Ledger) -> tuple[Prior, ...]:
    """Every cited prior this ledger defines no claim for, one per id.

    A theory whose defining claim is unwritten is not one of them: the
    collection is there, so the theory is open rather than absent, and citing
    it is how that debt gets priced.
    """
    known = {claim.id for claim in ledger.claims} | {
        theory.name for theory in ledger.theories
    }
    found = {
        cited.id: cited
        for claim in ledger.claims
        for cited in claim.why
        if cited.id not in known
    }
    return tuple(found[key] for key in sorted(found))


def foreign(ledger: Ledger) -> tuple[str, ...]:
    """Cited ids whose file is on disk, outside this ledger.

    A real reference -- a tower's lower storeys keep ledgers of their own, and
    a claim that rests on ruled law elsewhere has to be able to say so.
    """
    return tuple(cited.id for cited in undefined(ledger) if cited.path.exists())


def cited_claim(origin: Path, path: Path) -> Claim | None:
    """The claim a citation names, or None where it names none: a `why:` may
    legally point at a schema, a todo, or nothing on disk at all."""
    if not path.is_file():
        return None
    split = split_frontmatter(path.read_text())
    if split is None or "label" not in split[0]:
        return None
    else:
        return read_claim(origin, path)


def imported(ledger: Ledger) -> Mapping[str, Claim]:
    """The claims cited from outside this ledger, read from their own files.

    A defining claim's `why:` is how one theory imports another -- the
    theories whose words it also admits -- so following a citation across the
    boundary honors that import rather than reaching past this reader's scope.
    Keyed by the citing ledger's ids, since that is what a `why:` here says.
    """
    found = {
        cited.id: cited_claim(ledger.origin, cited.path) for cited in undefined(ledger)
    }
    return {name: claim for name, claim in found.items() if claim is not None}


def dangling(ledger: Ledger) -> tuple[str, ...]:
    """Cited ids that name no file anywhere: the rot lint."""
    return tuple(cited.id for cited in undefined(ledger) if not cited.path.exists())
