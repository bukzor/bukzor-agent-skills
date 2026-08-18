"""standing -- the status poset, the evidence operator, computed standing.

The status order L is not a chain: described ⊑ stipulated ⊑
obligated, then one incomparable top certified(c) per checker c (a
fibered top).  Global state is L^E pointwise.  Evidence induces a
monotone operator Phi; standing is DEFINED as its least fixpoint --
computed, never stored.  [STATUS, OPERATOR, COMPUTED]

Judgments enter the same base as acts -- bare claims of the record --
and which acts count is computed per stance by the contravention
fold, never asserted.  [ACT, FORCE, EXPLICIT]
"""

from collections.abc import Callable, Mapping
from dataclasses import dataclass

from engine_tower.fixpoint import iterate
from engine_tower.reference import Edge

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


def cite(evidence: frozenset[Evidence], quiver: frozenset[Edge]) -> frozenset[Evidence]:
    """Fill in each row's premises from the reference structure: an
    entry's warrant is what the entry cites.  The quiver is the only
    carrier of that edge -- writing premises by hand makes a second
    edge set nothing reconciles.  [OPERATOR]"""
    return frozenset(
        Evidence(
            ev.entry,
            ev.grants,
            frozenset(dst for src, dst in quiver if src == ev.entry),
        )
        for ev in evidence
    )


type Standing = Mapping[str, Status]  # a point of L^E
type Attack = tuple[
    str, str
]  # (attacker, target) -- defeat evidence, not a reference edge


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


@dataclass(frozen=True)
class Act:
    """One judgment: an assessor, a target, a verdict, an occasion --
    a historical proposition, so it enters the base as a bare claim
    [ACT].  `strikes` enumerates the addresses this act contravenes;
    enumeration only, resolvable at evaluation time (contravention by
    description is a syntax question, not answered here) [EXPLICIT]."""

    assessor: str
    target: str
    verdict: str
    occasion: int
    strikes: frozenset[str] = frozenset()

    @property
    def address(self) -> str:
        """Content-address: what the act already says -- assessor,
        target, occasion.  The verdict is content at the address, not
        part of it.  [REIFY]"""
        return f"{self.assessor}:{self.target}:{self.occasion}"


type Stance = Callable[[Act], bool]  # which acts a reader admits [STANCE]


def effective(record: frozenset[Act], admits: Stance) -> frozenset[Act]:
    """The contravention fold: the admitted acts, minus those an
    admitted act names.  Recency resolves nothing -- unstruck clashing
    acts both stand [EXPLICIT] -- and effectiveness is this
    computation per stance, never a mark on any act [FORCE].
    Same-issuer self-annulment is admitted by every stance: no reader
    may hold an assessor to a commitment the assessor withdrew."""
    by_address = {act.address: act for act in record}
    assert len(by_address) == len(record), by_address  # one act per address [REIFY]
    for act in record:
        for target in act.strikes:
            # act-on-act reference is well-founded: a target precedes
            # the act that cites it [ACT]
            assert by_address[target].occasion < act.occasion, (target, act)
    struck = frozenset(
        target
        for act in record
        for target in act.strikes
        if admits(act) or act.assessor == by_address[target].assessor
    )
    return frozenset(act for act in record if admits(act) and act.address not in struck)


def affirms(act: Act) -> bool:
    """A verdict's polarity toward its target: `accepted` and
    `certified` uphold, every other word takes standing away."""
    return act.verdict in ("accepted", "certified")


def contest(
    acts: frozenset[Act], claims: frozenset[str]
) -> tuple[frozenset[str], frozenset[str]]:
    """Read the truth-order interval off an effective set: acts of
    opposite polarity on one claim attack each other, a non-affirming
    act attacks its claim, and `grounded` does the rest.  A clash
    computes to the contested interval -- the same one whether the
    clashing assessors are two or one.  [EXPLICIT, DEFEAT]"""
    on = {c: frozenset(act for act in acts if act.target == c) for c in claims}
    nodes = claims | frozenset(act.address for c in claims for act in on[c])
    attacks = frozenset(
        {(act.address, c) for c in claims for act in on[c] if not affirms(act)}
        | {
            (a.address, b.address)
            for c in claims
            for a in on[c]
            for b in on[c]
            if affirms(a) != affirms(b)
        }
    )
    lower, upper = grounded(nodes, attacks)
    return lower & claims, upper & claims


def moot(presupposes: frozenset[Edge], defeated: frozenset[str]) -> frozenset[str]:
    """Sense-collapse: a claim whose presupposition is defeated, or
    itself moot, is moot -- a color outside the truth order, judging
    the framing rather than the content.  Ledger spelling:
    `verdict: dissolved`."""

    def step(m: frozenset[str]) -> frozenset[str]:
        return m | frozenset(
            src for src, dst in presupposes if dst in defeated or dst in m
        )

    return iterate(step, frozenset())


def color(
    claims: frozenset[str],
    presupposes: frozenset[Edge],
    record: frozenset[Act],
    admits: Stance,
) -> Mapping[str, str]:
    """The stack over one record: fold, interval, sense-collapse.

    Moot absorbs content-acts -- they are dropped before the
    truth-order pass -- so "moot and content-defeated" is impossible
    by derivation; nothing here or in any schema asserts it.  Moot
    seeds from surely-defeated only: a merely contested
    presupposition collapses nothing yet.

    The second pass cannot move a surviving claim's interval: attacks
    never cross claims, so a moot claim's acts leave as a whole
    island.  It stays for what it proves rather than what it
    computes -- without the drop, the exclusion above would rest on
    testing `mooted` first, which is the precedence rule the
    criterion forbids."""
    eff = effective(record, admits)
    _, upper = contest(eff, claims)
    mooted = moot(presupposes, claims - upper)
    live = claims - mooted
    lower, upper = contest(frozenset(act for act in eff if act.target in live), live)
    return {
        c: (
            "moot"
            if c in mooted
            else "in" if c in lower else "contested" if c in upper else "out"
        )
        for c in claims
    }
