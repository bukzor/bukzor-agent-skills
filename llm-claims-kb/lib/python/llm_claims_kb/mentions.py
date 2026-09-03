"""Report a claim whose prose names a label its theory never imported.

Labels are how claims cite each other in prose -- `(ASSESSOR)`, `WITHDRAWN+`
-- and a mention is a citation the reader is expected to resolve. It resolves
if the label is in this ledger, which a flattened paste carries whole, or in a
theory this one imports: a defining claim's `why:`, transitively. Otherwise
the reader meets a name with nothing behind it.

The test is exact, and deliberately has no threshold to tune. A token is
reported only when it is a real label *somewhere in the fleet* and
unreachable *here* -- an all-caps word nobody has made a label is not this
tool's business, and a label that already resolves needs no import added.

Two things are not citations, and neither is reported. A backticked name is a
literal quoted from elsewhere -- another system's label, a field, a filename
-- which is how a ledger cites a prototype it does not depend on. And naming
a sibling skill as a whole reaches into nothing, so it needs no import; only
reaching past the boundary for a label inside does.

Every ledger in the tree is read regardless of which are checked: whether a
token is a label at all is a fact about the fleet, not about one ledger.
"""

import argparse
import re
import sys
from collections.abc import Iterable, Mapping, Sequence
from pathlib import Path

from .ledger import Claim, Ledger, Theory, ledger_roots, read_ledger

# A label as prose wears it: sigils trail it, a verdict strikes it, and
# `grep LABEL` has to keep finding it under both. Two characters at least
# (LABEL_MIN), mirroring the schema's `(?=..)`: a lone capital is the
# sentence-initial `A` and the first-person `I`, not a citation.
MENTION = re.compile(
    r"(?<![A-Za-z0-9_])((?=[A-Z][A-Z0-9_])[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*)(?![a-z0-9_])"
)


def theory_index(ledgers: Iterable[Ledger]) -> Mapping[Path, Theory]:
    """Theories keyed by their defining claim's real path -- the one handle a
    citation from another ledger resolves through, ids being ledger-local."""
    return {
        theory.defining.path.resolve(): theory
        for ledger in ledgers
        for theory in ledger.theories
        if theory.defining
    }


def labels_in(theory: Theory) -> frozenset[str]:
    """What this theory answers to: its own label and its claims'."""
    return frozenset(
        {claim.label for claim in theory.claims}
        | ({theory.defining.label} if theory.defining else set())
    )


def reachable(
    theory: Theory,
    ledger: Ledger,
    index: Mapping[Path, Theory],
    seen: frozenset[str] = frozenset(),
) -> frozenset[str]:
    """Every label a claim in this theory may name without explaining itself.

    Its own ledger's labels, because a flattened ledger is one paste and the
    reader has them all in hand; then, transitively, whatever its imports
    reach -- an import that did not carry the imported theory's own imports
    would leave the reader one hop short of the same missing name.
    """
    if theory.name in seen:
        return frozenset()
    else:
        found = frozenset(label for one in ledger.theories for label in labels_in(one))
        for cited in theory.priors:
            imported = index.get(cited.path.resolve())
            if imported:
                found |= labels_in(imported)
                found |= reachable(imported, ledger, index, seen | {theory.name})
        return found


def prose(body: str) -> str:
    """The claim's text with code spans and blocks struck out.

    A backticked name is a literal quoted from somewhere else, and quoting a
    name is not citing a claim. The ledgers already write it this way: strata
    says FREE_CONSERVE of its own claim and `CLAIMS_ONLY` of the prototype's.
    """
    return re.sub(r"```.*?```|`[^`]*`", " ", body, flags=re.DOTALL)


def mentioned(claim: Claim) -> frozenset[str]:
    """Labels this claim's prose names, its own excepted -- a claim stating
    its own label is titling itself, not citing anything."""
    return frozenset(MENTION.findall(prose(claim.path.read_text()))) - {claim.label}


def homes(ledgers: Iterable[Ledger]) -> Mapping[str, tuple[str, ...]]:
    """Every label in the fleet, and where it is defined -- what turns a
    finding into an instruction: import this, or stop reaching for it."""
    found: dict[str, set[str]] = {}
    for ledger in ledgers:
        for theory in ledger.theories:
            for label in labels_in(theory):
                found.setdefault(label, set()).add(f"{ledger.root}:{theory.label}")
    return {label: tuple(sorted(where)) for label, where in found.items()}


def unimported(
    ledger: Ledger, fleet: Mapping[str, tuple[str, ...]], index: Mapping[Path, Theory]
) -> tuple[str, ...]:
    """One line per mention this ledger cannot resolve.

    A theory's defining claim is read with the rest of them: it is the file
    that states the theory, so it is where the cross-theory citations
    concentrate, and it resolves against the same imports -- its own `why:`.
    """
    return tuple(
        f"{claim.path}: {claim.label} names {label},"
        f" defined in {'/'.join(fleet[label])}"
        for theory in ledger.theories
        for known in [reachable(theory, ledger, index)]
        for claim in (*filter(None, [theory.defining]), *theory.claims)
        for label in sorted(mentioned(claim) - known)
        if label in fleet
    )


def named(roots: Sequence[Path]) -> tuple[Path, ...]:
    """The roots given on the command line, each of which must exist -- a typo
    that silently checked nothing would report a clean fleet."""
    for root in roots:
        assert root.is_dir(), f"{root}: not a ledger"
    return tuple(roots)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root", nargs="*", type=Path, help="ledgers to check; default all"
    )
    args = parser.parse_args(argv)

    ledgers = tuple(read_ledger(root) for root in ledger_roots())
    index, fleet = theory_index(ledgers), homes(ledgers)
    wanted = {root.resolve() for root in named(args.root)}
    checked = [
        ledger for ledger in ledgers if not wanted or ledger.root.resolve() in wanted
    ]

    findings = [line for ledger in checked for line in unimported(ledger, fleet, index)]
    for line in findings:
        print(line)
    print(f"{len(findings)} unimported mentions", file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
