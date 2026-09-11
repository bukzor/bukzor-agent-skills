"""Rank a ledger's claims by how weakly they rest on the owner's word.

A claim is grounded in the owner's judgment when some `why:` chain from it
reaches a `standing: user` claim. Everything else rests on an agent's
assertion, or on a file outside the ledger. The weight of that weakness is
what depends on the claim: a leaf nobody cites can be wrong for free, a root
with twenty dependents cannot.

Output is one JSON record per claim on stdout, weakest first: claims that
reach no user-standing ground, most-depended-on first; then the rest by
distance to the nearest one. A quoted chat address in a body is not a
ground -- the ledger is meant to stand without its source -- so only the
`why:` graph and `standing:` are read.
"""

import argparse
import json
import sys
from collections import deque
from collections.abc import Mapping
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import cast

from .ledger import Claim, Ledger, read_ledger


@dataclass(frozen=True)
class Grounding:
    id: str
    label: str
    standing: str
    theory: str
    todo: bool
    verdict: str | None
    rests_on_it: int  # transitive dependents within the ledger
    hops_to_user: int | None  # shortest `why:` path to a user-standing claim
    user_grounds: tuple[str, ...]  # labels of the user-standing claims reached
    priors: int
    foreign: int  # priors whose file lies outside the ledger
    dangling: int  # priors naming no file at all

    @property
    def unreached(self) -> bool:
        return self.hops_to_user is None


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


def hops(
    claim: str, priors: Mapping[str, tuple[str, ...]], ground: frozenset[str]
) -> int | None:
    """Shortest `why:` path from the claim to any ground; 0 if it is one."""
    seen = {claim}
    queue = deque([(claim, 0)])
    while queue:
        here, distance = queue.popleft()
        if here in ground:
            return distance
        for prior in priors[here]:
            if prior not in seen:
                seen.add(prior)
                queue.append((prior, distance + 1))
    return None


def grounding(ledger: Ledger) -> tuple[Grounding, ...]:
    by_id = {claim.id: claim for claim in ledger.claims}
    priors = in_ledger_priors(ledger)
    rests = dependents(priors)
    ground = frozenset(
        claim.id
        for claim in ledger.claims
        if claim.standing == "user" and claim.verdict is None
    )
    rows = tuple(
        grounding_of(claim, by_id, priors, rests, ground) for claim in ledger.claims
    )
    return tuple(
        sorted(
            rows,
            key=lambda row: (
                not row.unreached,
                -row.rests_on_it,
                row.hops_to_user or 0,
                row.id,
            ),
        )
    )


def grounding_of(
    claim: Claim,
    by_id: Mapping[str, Claim],
    priors: Mapping[str, tuple[str, ...]],
    rests: Mapping[str, frozenset[str]],
    ground: frozenset[str],
) -> Grounding:
    reached = ancestors(claim.id, priors) & ground
    if claim.id in ground:
        reached = reached | {claim.id}
    outside = [cited for cited in claim.why if cited.id not in by_id]
    return Grounding(
        id=claim.id,
        label=claim.label,
        standing=claim.standing,
        theory=claim.scope,
        todo=claim.todo,
        verdict=claim.verdict,
        rests_on_it=len(rests[claim.id]),
        hops_to_user=hops(claim.id, priors, ground),
        user_grounds=tuple(sorted(by_id[found].label for found in reached)),
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

    for row in grounding(read_ledger(root)):
        json.dump(asdict(row), sys.stdout)
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
