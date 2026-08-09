"""standing -- the status poset, the evidence operator, computed standing.

The status order L is not a chain: described ⊑ stipulated ⊑
obligated, then one incomparable top certified(c) per checker c (a
fibered top).  Global state is L^E pointwise.  Evidence induces a
monotone operator Phi; standing is DEFINED as its least fixpoint --
computed, never stored.  [STATUS, OPERATOR, COMPUTED]
"""

from collections.abc import Callable, Mapping
from dataclasses import dataclass

from engine_tower.fixpoint import iterate

_STATUS_NAMES = {0: "described", 1: "stipulated", 2: "obligated"}


@dataclass(frozen=True)
class Status:
    rank: int
    checker: str | None = None  # only at rank 3; distinct checkers incomparable

    def __repr__(self):
        if self.rank == 3:
            return f"certified({self.checker})"
        else:
            return _STATUS_NAMES[self.rank]


DESCRIBED = Status(0)
STIPULATED = Status(1)
OBLIGATED = Status(2)


def certified(checker: str) -> Status:
    return Status(3, checker)


def status_leq(a: Status, b: Status) -> bool:
    return a == b or a.rank < b.rank


def status_sup(a: Status, b: Status) -> Status:
    """Join.  Two distinct certified(c) have no join -- the top is
    fibered [STATUS], so L is not a lattice and this map is partial;
    it raises where the join is missing.  Phi inherits the
    partiality: two checkers certifying one entry crash it."""
    if status_leq(a, b):
        return b
    if status_leq(b, a):
        return a
    raise AssertionError((a, b))


@dataclass(frozen=True)
class Evidence:
    """One generator of Phi, the ascent rule format: if every premise
    stands at THRESHOLD or better, `entry` is granted `grants`.

    There is no descent rule.  Retraction and fiat enter only as
    removal or addition of Evidence rows -- a change of operator, not
    a step of one [ASYMMETRY].  `entry` is the single node sort, so
    this rule format is fixed once, below every genre
    [FREE_CONSERVE]."""

    entry: str
    grants: Status
    premises: frozenset[str] = frozenset()


THRESHOLD = STIPULATED  # premises must stand at least here to support ascent

type Standing = Mapping[str, Status]  # a point of L^E
type Attack = tuple[str, str]  # (attacker, target) -- defeat evidence, not a reference edge


def phi(
    evidence: frozenset[Evidence], entries: frozenset[str]
) -> Callable[[Standing], Standing]:
    """The evidence-induced operator Phi: L^E -> L^E.  Monotone because
    every generator is ascent-only.  [OPERATOR]"""

    def step(x: Standing) -> Standing:
        out = {e: DESCRIBED for e in entries}
        for ev in evidence:
            if all(status_leq(THRESHOLD, x[p]) for p in ev.premises):
                out[ev.entry] = status_sup(out[ev.entry], ev.grants)
        return out

    return step


def standing(evidence: frozenset[Evidence], entries: frozenset[str]) -> Standing:
    """standing := lfp Phi.  Defined, not stored: a ring of mutual
    support gets nothing from itself, only from outside.  [COMPUTED]"""
    return iterate(phi(evidence, entries), {e: DESCRIBED for e in entries})


def grounded(
    nodes: frozenset[str],
    attacks: frozenset[Attack],
    rulings: Mapping[str, bool] | None = None,
) -> tuple[frozenset[str], frozenset[str]]:
    """Defeat breaks Phi's monotonicity; the repair runs the
    approximating operator on the precision-ordered square L^2 -- one
    (surely-in, possibly-in) interval per entry [APPROX, DEFEAT].
    For Boolean L with attack evidence, the well-founded fixpoint
    computed here is argumentation's grounded semantics.

    Returns (lower, upper): surely standing, not yet ruled out.  The
    gap between them is the undecided region -- the ledger stores the
    operator, and a "semantics" is a query-time choice of fixpoint of
    its approximation.  A user ruling pins one coordinate and shrinks
    that choice."""
    rulings = rulings or {}
    attackers = {n: frozenset(a for a, t in attacks if t == n) for n in nodes}

    def pin(s: frozenset[str]) -> frozenset[str]:
        s |= frozenset(n for n, v in rulings.items() if v)
        return s - frozenset(n for n, v in rulings.items() if not v)

    def step(
        bounds: tuple[frozenset[str], frozenset[str]],
    ) -> tuple[frozenset[str], frozenset[str]]:
        lower, upper = bounds
        return (
            pin(frozenset(n for n in nodes if attackers[n].isdisjoint(upper))),
            pin(frozenset(n for n in nodes if attackers[n].isdisjoint(lower))),
        )

    return iterate(step, (pin(frozenset()), pin(nodes)))
