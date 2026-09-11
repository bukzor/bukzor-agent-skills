"""Rank a ledger's claims by how weakly they rest on the owner's word.

A claim's effective standing is the fold over its `why:` graph, read the
way `Skill(llm-claims)` reads a derivation: the owner's word and a
certified check are ground, and the fold stops there; a bare claim that
only follows from its premises is transparent; anything else the fold
meets -- an agent's signature, an open question, a struck claim, a bare
claim resting on nothing, a citation naming no file -- is a judge whose
ruling everything above it waits on. A claim is as weak as the weakest
judge it meets, however many owner rulings it also cites.

The weight of that weakness is what depends on the claim: a leaf nobody
cites can be wrong for free, a root with twenty dependents cannot. Output
is one JSON record per claim on stdout, weakest first: the judges
themselves, then claims weak through an ancestor, then the grounded, each
most-depended-on first. A quoted chat address in a body is not a ground --
the ledger is meant to stand without its source -- so only `why:`,
`standing:`, `verdict:` and `verify:` are read; a citation into another
ledger is followed and the claim read there.
"""

import argparse
import json
import os
import sys
from collections.abc import Mapping
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import cast

from .ledger import Claim, Ledger, cited_claim, read_ledger

# Whose word the fold can meet, weakest first. The last two are ground.
JUDGES = ("dangling", "struck", "hidden", "open", "agent", "certified", "user")
GROUND = frozenset({"certified", "user"})

# The fold can reach a file that is no claim (a schema, a todo) or no file
# at all. Only the latter is a judge -- rot -- so a non-claim is left out of
# the universe and the fold looks straight past it.
Universe = Mapping[Path, Claim | None]


@dataclass(frozen=True)
class Grounding:
    id: str
    label: str
    standing: str
    theory: str
    todo: bool
    verdict: str | None
    effective: str  # the weakest judge the fold meets; one of JUDGES
    is_judge: bool  # its dependents wait on a ruling on this claim itself
    weakest: tuple[str, ...]  # nearest judges beneath it; a ruling on each grounds it
    rests_on_it: int  # transitive dependents within the ledger
    user_grounds: tuple[str, ...]  # labels of the user-standing claims reached
    priors: int
    foreign: int  # priors whose file lies outside the ledger
    dangling: int  # priors naming no file at all

    @property
    def grounded(self) -> bool:
        return self.effective in GROUND


@dataclass(frozen=True)
class Fold:
    """What the fold found beneath one node, the node itself included."""

    judges: frozenset[Path]  # the nearest non-ground judges; the node, if it is one
    ground: frozenset[Path]  # the ground the fold stopped at, through transparent claims only
    users: frozenset[Path]  # every user-standing claim anywhere beneath


EMPTY = Fold(frozenset(), frozenset(), frozenset())


def judge(claim: Claim | None) -> str | None:
    """Whose word a claim itself supplies, or None where it is transparent:
    bare, unchecked, and resting on premises that must speak for it."""
    if claim is None:
        return "dangling"
    elif claim.verdict is not None:
        return "struck"
    elif claim.standing in ("user", "agent", "open"):
        return claim.standing
    elif claim.verify is not None:
        return "certified"
    elif claim.why:
        return None
    else:
        return "hidden"


def fold(path: Path, universe: Universe, memo: dict[Path, Fold], active: frozenset[Path]) -> Fold:
    """The fold at one node. A cycle proves nothing, so re-entering an active
    node contributes nothing; a bare claim whose premises all fold to nothing
    is its own hidden judge."""
    if path in memo:
        return memo[path]
    elif path in active:
        return EMPTY
    elif path not in universe:
        return EMPTY
    claim = universe[path]
    own = judge(claim)
    beneath = [
        fold(cited.path.resolve(), universe, memo, active | {path})
        for cited in (claim.why if claim is not None else ())
    ]
    users = frozenset().union(*(found.users for found in beneath))
    if own == "user":
        result = Fold(frozenset(), frozenset({path}), users | {path})
    elif own == "certified":
        result = Fold(frozenset(), frozenset({path}), users)
    elif own is None:
        judges = frozenset().union(*(found.judges for found in beneath))
        ground = frozenset().union(*(found.ground for found in beneath))
        if judges or ground:
            result = Fold(judges, ground, users)
        else:
            result = Fold(frozenset({path}), frozenset(), users)
    else:
        result = Fold(frozenset({path}), frozenset(), users)
    memo[path] = result
    return result


def load_reachable(ledger: Ledger) -> Universe:
    """Every claim the fold can reach: the ledger's own, and each foreign
    claim cited transitively, read from its file. None where a citation
    names no file."""
    found: dict[Path, Claim | None] = {claim.path.resolve(): claim for claim in ledger.claims}
    seen = set(found)
    frontier = [cited.path.resolve() for claim in ledger.claims for cited in claim.why]
    while frontier:
        path = frontier.pop()
        if path in seen:
            continue
        seen.add(path)
        if not path.exists():
            found[path] = None
            continue
        claim = cited_claim(ledger.origin, path)
        if claim is not None:
            found[path] = claim
            frontier.extend(cited.path.resolve() for cited in claim.why)
    return found


def in_ledger_priors(ledger: Ledger) -> Mapping[str, tuple[str, ...]]:
    """Each claim's priors that resolve inside this ledger, by id."""
    known = {claim.id for claim in ledger.claims}
    return {
        claim.id: tuple(cited.id for cited in claim.why if cited.id in known)
        for claim in ledger.claims
    }


def dependents(priors: Mapping[str, tuple[str, ...]]) -> Mapping[str, frozenset[str]]:
    """Transitive dependents of each claim: everything whose chain passes through it."""
    found: dict[str, set[str]] = {claim: set() for claim in priors}
    for claim in priors:
        for ancestor in ancestors(claim, priors):
            found[ancestor].add(claim)
    return {claim: frozenset(deps) for claim, deps in found.items()}


def ancestors(claim: str, priors: Mapping[str, tuple[str, ...]]) -> frozenset[str]:
    seen: set[str] = set()
    frontier = [claim]
    while frontier:
        for prior in priors[frontier.pop()]:
            if prior not in seen:
                seen.add(prior)
                frontier.append(prior)
    return frozenset(seen)


def grounding(ledger: Ledger, universe: Universe) -> tuple[Grounding, ...]:
    rests = dependents(in_ledger_priors(ledger))
    memo: dict[Path, Fold] = {}
    rows = tuple(
        grounding_of(claim, len(rests[claim.id]), ledger, universe, memo)
        for claim in ledger.claims
    )
    return tuple(
        sorted(
            rows,
            key=lambda row: (
                row.grounded,
                not row.is_judge,
                -row.rests_on_it,
                JUDGES.index(row.effective),
                row.id,
            ),
        )
    )


def name_of(path: Path, universe: Universe, origin: Path) -> str:
    """A judge's label, or for a citation naming no file, the path it named."""
    claim = universe[path]
    return claim.label if claim is not None else os.path.relpath(path, origin.resolve())


def grounding_of(
    claim: Claim, rests: int, ledger: Ledger, universe: Universe, memo: dict[Path, Fold]
) -> Grounding:
    here = claim.path.resolve()
    found = fold(here, universe, memo, frozenset())
    beneath = found.judges - {here}
    stops = found.judges or found.ground
    effective = min((judge(universe[p]) or "hidden" for p in stops), key=JUDGES.index)
    known = {cited.id for cited in claim.why} & {other.id for other in ledger.claims}
    outside = [cited for cited in claim.why if cited.id not in known]
    return Grounding(
        id=claim.id,
        label=claim.label,
        standing=claim.standing,
        theory=claim.scope,
        todo=claim.todo,
        verdict=claim.verdict,
        effective=effective,
        is_judge=here in found.judges,
        weakest=tuple(sorted(name_of(p, universe, ledger.origin) for p in beneath)),
        rests_on_it=rests,
        user_grounds=tuple(sorted(name_of(p, universe, ledger.origin) for p in found.users)),
        priors=len(claim.why),
        foreign=sum(1 for cited in outside if cited.path.exists()),
        dangling=sum(1 for cited in outside if not cited.path.exists()),
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    _ = parser.add_argument("ledger", type=Path, help="a `*.claims.kb/` directory")
    args = parser.parse_args()
    root = cast(Path, args.ledger)

    ledger = read_ledger(root)
    for row in grounding(ledger, load_reachable(ledger)):
        json.dump(asdict(row), sys.stdout)
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
