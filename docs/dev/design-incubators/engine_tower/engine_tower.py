"""The engine tower S0-S5, reified as runnable Python.

Reading order IS the tower: each section uses only names defined above
it, and truncating the file at any section banner leaves a working
program.  That is the stratification claim made literal -- every stratum
is a conservative extension of the ones below, and the lower strata
never mention the upper ones.

Each demo_* function is one theorem from the design discussion; its
asserts are the checked proof obligations, on the smallest instance
that exhibits the phenomenon.  Run:  python engine_tower.py
"""

import operator
from collections.abc import Callable, Mapping
from dataclasses import dataclass

# ===================================================================
# S0 -- History.  The update alphabet U; a history is a word in the
# free monoid U*.  State is a map K -> Payload under override (last
# writer wins); `state` is the unique monoid action extending it.
# Nothing here knows content.
# ===================================================================

type Payload = Mapping[str, str]
type Update = tuple[str, Payload]  # (key, payload)
type History = tuple[Update, ...]
type State = Mapping[str, Payload]


def state(history: History) -> State:
    """The action map U* -> S: fold override over the word.

    "Prior states queryable" is free: store the word, fold any prefix.
    """
    return {key: payload for key, payload in history}


def lawful[A](cached: A, view: Callable[[State], A], history: History) -> bool:
    """PROJECTION: a materialized view is lawful iff the triangle
    commutes -- the stored answer equals the view of the replayed
    state.  Cache drift is exactly the failure of this equation."""
    return cached == view(state(history))


def demo_s0() -> str:
    h1: History = (("m", {"text": "mission v1"}),)
    h2: History = (("m", {"text": "mission v2"}), ("g", {"text": "goal"}))
    # state is a monoid homomorphism: fold of concatenation == override of folds
    assert state(h1 + h2) == {**state(h1), **state(h2)}

    def keys_view(s: State) -> frozenset[str]:
        return frozenset(s)

    assert lawful(frozenset({"m", "g"}), keys_view, h1 + h2)
    assert not lawful(frozenset({"m"}), keys_view, h1 + h2)  # stale cache
    return "state() is a fold; stale cache detected by the commuting triangle"


# ===================================================================
# S1 -- Records.  Schemas + migrations form a category; instances sit
# fibered over it.  Validation is a typing judgment I |= Sigma; a
# migration acts on instances as the pushforward (opcartesian lift).
# ===================================================================


@dataclass(frozen=True)
class Schema:
    name: str
    fields: frozenset[str]  # required field names
    ref_fields: frozenset[str] = frozenset()  # values are keys (S2 reads these)


def validates(payload: Payload, schema: Schema) -> bool:
    """The typing judgment  payload |= schema."""
    return schema.fields <= payload.keys()


@dataclass(frozen=True)
class Migration:
    """An arrow Sigma -> Sigma' with its action on instances.

    The opcartesian-lift law, in checkable form: push must carry
    payloads validating against source to payloads validating against
    target.  A rename is an isomorphism (push has an inverse)."""

    source: Schema
    target: Schema
    push: Callable[[Payload], Payload]


def demo_s1() -> str:
    claim_v1 = Schema("claim.v1", frozenset({"schema", "text", "why"}))
    claim_v2 = Schema("claim.v2", frozenset({"schema", "text", "because"}))

    def rename_why(p: Payload) -> Payload:
        q = {**p, "because": p["why"], "schema": "claim.v2"}
        del q["why"]
        return q

    m = Migration(claim_v1, claim_v2, rename_why)
    p: Payload = {"schema": "claim.v1", "text": "cycles are unproven", "why": "k7"}
    assert validates(p, m.source), p
    assert validates(m.push(p), m.target), m.push(p)  # lift lands in the target fiber
    return "rename migration carries the v1 fiber into the v2 fiber"


# ===================================================================
# S2 -- References.  Ref-valued fields present a quiver on keys.
# Referential integrity is the pullback condition (edges land on
# existing keys).  Reachability is a least fixpoint; cones are up-sets;
# valuing edges in a semiring turns reachability into counting or
# provenance.  Taint is the same lfp shape.
# ===================================================================

type Edge = tuple[str, str]  # (src_key, dst_key)


def edges(s: State, schemas: Mapping[str, Schema]) -> frozenset[Edge]:
    """The quiver Q(I) presented by the instance's ref-valued fields."""
    return frozenset(
        (key, payload[field])
        for key, payload in s.items()
        for field in schemas[payload["schema"]].ref_fields
        if field in payload
    )


def referentially_closed(s: State, schemas: Mapping[str, Schema]) -> bool:
    """The pullback condition: every edge lands on an existing key."""
    return all(dst in s for _, dst in edges(s, schemas))


def reachable(es: frozenset[Edge], roots: frozenset[str]) -> frozenset[str]:
    """lfp X. roots ∪ post(X) -- the reachability preorder, pointwise."""
    x: frozenset[str] = frozenset()
    while True:
        x2 = roots | frozenset(dst for src, dst in es if src in x) | x
        if x2 == x:
            return x
        x = x2


def cone(es: frozenset[Edge], key: str) -> frozenset[str]:
    """The invalidation cone ↑key: everything that reaches key --
    reachability in the reversed quiver.  Taint has this exact type."""
    return reachable(frozenset((dst, src) for src, dst in es), frozenset({key}))


@dataclass(frozen=True)
class Semiring[T]:
    zero: T
    one: T
    plus: Callable[[T, T], T]
    times: Callable[[T, T], T]


COUNT = Semiring(0, 1, operator.add, operator.mul)  # support counts

type Paths = frozenset[tuple[Edge, ...]]


def _concat_paths(a: Paths, b: Paths) -> Paths:
    return frozenset(p + q for p in a for q in b)


PROVENANCE: Semiring[Paths] = Semiring(
    frozenset(), frozenset({()}), operator.or_, _concat_paths
)


def path_weight[T](
    es: frozenset[Edge], src: str, dst: str, sr: Semiring[T], w: Callable[[Edge], T]
) -> T:
    """Sum over all src->dst paths of the product of edge weights.
    COUNT gives how many independent support chains exist; PROVENANCE
    gives the chains themselves.  Assumes the quiver is a DAG."""
    if src == dst:
        return sr.one
    acc = sr.zero
    for edge in es:
        if edge[0] == src:
            acc = sr.plus(acc, sr.times(w(edge), path_weight(es, edge[1], dst, sr, w)))
    return acc


def demo_s2() -> str:
    mission = Schema("mission.v1", frozenset({"schema", "text"}))
    claim = Schema(
        "claim.v1", frozenset({"schema", "text", "why"}), frozenset({"why", "basis"})
    )
    schemas = {s.name: s for s in (mission, claim)}
    records: State = {
        "m": {"schema": "mission.v1", "text": "the mission"},
        "g": {"schema": "claim.v1", "text": "a goal", "why": "m"},
        "r1": {"schema": "claim.v1", "text": "a req", "why": "g", "basis": "m"},
    }
    assert referentially_closed(records, schemas)
    es = edges(records, schemas)
    assert es == {("g", "m"), ("r1", "g"), ("r1", "m")}, es
    # every entry reachable from mission-cone: the design-tower condition
    assert cone(es, "m") == {"m", "g", "r1"}
    n_chains = path_weight(es, "r1", "m", COUNT, lambda _: 1)
    assert n_chains == 2, n_chains
    chains = path_weight(es, "r1", "m", PROVENANCE, lambda e: frozenset({(e,)}))
    routes = sorted(",".join(f"{s}->{d}" for s, d in p) for p in chains)
    return f"cone(m) is everything; r1 supports m by {n_chains} chains: {routes}"


# ===================================================================
# S3 -- Standing.  The status order L is not a chain: described ⊑
# stipulated ⊑ obligated, then one incomparable top certified(c) per
# checker c (a fibered top).  Global state is L^E pointwise.  Evidence
# induces a monotone operator Phi; standing is DEFINED as lfp Phi
# (Knaster-Tarski) -- computed, never stored.
# ===================================================================

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
    fibered; asking for one is a modeling error, so it raises."""
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
    removal or addition of Evidence rows -- a change of operator, not a
    step of one.  CLAIMS_ONLY / GENERIC_BASE live here: `entry` is the
    single node sort, so this rule format is fixed once and for all."""

    entry: str
    grants: Status
    premises: frozenset[str] = frozenset()


THRESHOLD = STIPULATED  # premises must stand at least here to support ascent

type Standing = Mapping[str, Status]  # a point of L^E


def phi(
    evidence: frozenset[Evidence], entries: frozenset[str]
) -> Callable[[Standing], Standing]:
    """The evidence-induced operator Phi: L^E -> L^E.  Monotone because
    every generator is ascent-only."""

    def step(x: Standing) -> Standing:
        out = {e: DESCRIBED for e in entries}
        for ev in evidence:
            if all(status_leq(THRESHOLD, x[p]) for p in ev.premises):
                out[ev.entry] = status_sup(out[ev.entry], ev.grants)
        return out

    return step


def iterate[T](f: Callable[[T], T], start: T) -> T:
    """Kleene iteration to a fixpoint.  From bottom this computes lfp;
    from a post-fixed point it descends to the greatest fixpoint below
    the start.  Same loop, asymmetric meaning -- that asymmetry is the
    whole economics of S3."""
    x = start
    while (x2 := f(x)) != x:
        x = x2
    return x


def standing(evidence: frozenset[Evidence], entries: frozenset[str]) -> Standing:
    """standing := lfp Phi  (LEAST_FIX).  Defined, not stored: a ring of
    mutual support gets nothing from itself, only from outside."""
    return iterate(phi(evidence, entries), {e: DESCRIBED for e in entries})


def demo_s3_warm_start() -> str:
    """Adding evidence: Phi' >= Phi, the old lfp is a pre-fixed point of
    Phi', so upward iteration from it is sound and lands exactly on
    lfp Phi'.  Appends are cheap; the append-only store is a theorem."""
    entries = frozenset({"a", "b"})
    ev1 = frozenset({Evidence("a", STIPULATED)})
    old = standing(ev1, entries)
    ev2 = ev1 | {Evidence("b", STIPULATED, frozenset({"a"}))}
    warm = iterate(phi(ev2, entries), old)  # resume from the old fixpoint
    cold = standing(ev2, entries)  # recompute from bottom
    assert warm == cold, (warm, cold)
    return f"warm-start from old fixpoint == cold lfp: {warm}"


def demo_s3_retraction_gap() -> str:
    """Removing evidence: the old lfp is only a post-fixed point of
    Phi'; descending from it stops at the greatest fixpoint below it,
    generally strictly above lfp Phi'.  The visible face of the gap is
    the circular warrant: a ring of mutual support survives the
    retraction of the external warrant that once justified it."""
    entries = frozenset({"a", "b", "w"})
    ring = frozenset(
        {
            Evidence("a", STIPULATED, frozenset({"b"})),
            Evidence("b", STIPULATED, frozenset({"a"})),
            Evidence("a", STIPULATED, frozenset({"w"})),
            Evidence("w", STIPULATED),  # the external warrant
        }
    )
    old = standing(ring, entries)
    assert old["a"] == old["b"] == STIPULATED, old

    retracted = frozenset(ev for ev in ring if ev.entry != "w")
    revised = iterate(phi(retracted, entries), old)  # descend from old state
    fresh = standing(retracted, entries)  # lfp from bottom
    assert revised["a"] == revised["b"] == STIPULATED, revised  # ring holds itself up
    assert fresh["a"] == fresh["b"] == DESCRIBED, fresh  # LEAST_FIX reopens it
    return f"revision keeps the ring ({revised['a']!r}); true lfp reopens it ({fresh['a']!r})"


def grounded(
    nodes: frozenset[str],
    attacks: frozenset[Edge],  # (attacker, target)
    rulings: Mapping[str, bool] | None = None,
) -> tuple[frozenset[str], frozenset[str]]:
    """Defeat breaks Phi's monotonicity; the repair runs the
    approximating operator on the precision-ordered square L^2 -- one
    (surely-in, possibly-in) interval per entry.  For Boolean L with
    attack evidence, the well-founded fixpoint computed here IS Dung's
    grounded semantics.

    Returns (lower, upper): surely standing, not yet ruled out.  The
    gap between them is the undecided region -- UNFORCED: the ledger
    stores the operator, and a "semantics" is a query-time choice of
    fixpoint of its approximation.  A user ruling (!) pins one
    coordinate and shrinks that choice."""
    rulings = rulings or {}
    attackers = {n: frozenset(a for a, t in attacks if t == n) for n in nodes}

    def pin(s: frozenset[str]) -> frozenset[str]:
        s |= frozenset(n for n, v in rulings.items() if v)
        return s - frozenset(n for n, v in rulings.items() if not v)

    lower, upper = pin(frozenset()), pin(nodes)
    while True:
        new_lower = pin(frozenset(n for n in nodes if attackers[n].isdisjoint(upper)))
        new_upper = pin(frozenset(n for n in nodes if attackers[n].isdisjoint(lower)))
        if (new_lower, new_upper) == (lower, upper):
            return lower, upper
        lower, upper = new_lower, new_upper


def demo_s3_grounded() -> str:
    nodes = frozenset({"a", "b", "c"})
    # reinstatement chain: c defeats b, b defeats a => c stands, a reinstated
    lo, up = grounded(nodes, frozenset({("c", "b"), ("b", "a")}))
    assert lo == up == {"a", "c"}, (lo, up)

    # even cycle: mutual defeat -- grounded leaves both undecided
    duo = frozenset({"a", "b"})
    mutual = frozenset({("a", "b"), ("b", "a")})
    lo2, up2 = grounded(duo, mutual)
    assert (lo2, up2) == (frozenset(), duo), (lo2, up2)

    # a user ruling pins one coordinate; the rest re-decides around it
    lo3, up3 = grounded(duo, mutual, rulings={"a": True})
    assert lo3 == up3 == {"a"}, (lo3, up3)
    return "chain decides fully; even cycle undecided; a ruling collapses the gap"


# ===================================================================
# S4 -- Theories / genres.  Vocabulary lattice P(V); entries live in a
# home vocabulary (confinement, the syntactic half); standing is a
# presheaf on the theory poset (conservativity, the semantic half).
# Because S3 fixed one node sort and one rule format, a genre extension
# can only add Evidence rows about its own entries -- conservativity
# holds by construction.  Give genres their own node sorts and this
# becomes a per-genre proof obligation.
# ===================================================================


def restrict(x: Standing, entries: frozenset[str]) -> Standing:
    """The reduct M'|_W: forget the extension's entries."""
    return {e: s for e, s in x.items() if e in entries}


def demo_s4_conservativity() -> str:
    core_entries = frozenset({"m", "g"})
    core_ev = frozenset(
        {Evidence("m", STIPULATED), Evidence("g", STIPULATED, frozenset({"m"}))}
    )
    core = standing(core_ev, core_entries)

    # confined genre extension: concludes only on its own entries, citing
    # core entries as premises freely
    ext_entries = core_entries | {"r1"}
    ext_ev = core_ev | {Evidence("r1", OBLIGATED, frozenset({"g"}))}
    ext = standing(ext_ev, ext_entries)
    # the satisfaction condition: old standing unchanged under extension
    assert restrict(ext, core_entries) == core, (ext, core)

    # break confinement: the extension concludes on a core entry
    rogue_ev = core_ev | {Evidence("g", certified("rogue-check"))}
    rogue = standing(rogue_ev, ext_entries)
    assert restrict(rogue, core_entries) != core, rogue
    return f"confined extension conserves core standing; rogue one moves g to {rogue['g']!r}"


# ===================================================================
# S5 -- Protocol / triggers.  A trigger bank is a monitor automaton:
# guarded rules over situation predicates drawn from ANY lower
# stratum.  Its semantics is the synchronized product with the agent's
# process; the enforcement ladder (attention -> tooling -> typechecker)
# varies WHICH machine computes that product -- the bank itself is one
# syntactic object, and adapters are the interpretations out of it.
# ===================================================================


@dataclass(frozen=True)
class Situation:
    history: History
    schemas: Mapping[str, Schema]
    entries: frozenset[str]
    evidence: frozenset[Evidence]


@dataclass(frozen=True)
class Trigger:
    name: str
    guard: Callable[[Situation], bool]


def fire(bank: tuple[Trigger, ...], sit: Situation) -> frozenset[str]:
    """One transition of the synchronized product: the guards that hold
    now.  `fire` is the attention-grade interpreter; compiling the same
    bank into a linter or a type system changes the machine, not the
    bank."""
    return frozenset(t.name for t in bank if t.guard(sit))


def _dangling_reference(sit: Situation) -> bool:  # an S2 predicate
    return not referentially_closed(state(sit.history), sit.schemas)


def _open_claim(sit: Situation) -> bool:  # an S3 predicate
    st = standing(sit.evidence, sit.entries)
    return any(st[e] == DESCRIBED for e in sit.entries)


BANK = (
    Trigger("dangling-reference", _dangling_reference),
    Trigger("open-claim", _open_claim),
)


def demo_s5() -> str:
    mission = Schema("mission.v1", frozenset({"schema", "text"}))
    claim = Schema("claim.v1", frozenset({"schema", "text", "why"}), frozenset({"why"}))
    schemas = {s.name: s for s in (mission, claim)}
    entries = frozenset({"m", "g"})
    healthy = Situation(
        history=(
            ("m", {"schema": "mission.v1", "text": "the mission"}),
            ("g", {"schema": "claim.v1", "text": "a goal", "why": "m"}),
        ),
        schemas=schemas,
        entries=entries,
        evidence=frozenset(
            {Evidence("m", STIPULATED), Evidence("g", STIPULATED, frozenset({"m"}))}
        ),
    )
    assert fire(BANK, healthy) == frozenset(), fire(BANK, healthy)

    # drop the mission record and its warrant: guards from two different
    # strata fire off the one situation
    broken = Situation(
        history=healthy.history[1:],
        schemas=schemas,
        entries=entries,
        evidence=frozenset({Evidence("g", STIPULATED, frozenset({"m"}))}),
    )
    fired = fire(BANK, broken)
    assert fired == {"dangling-reference", "open-claim"}, fired
    return f"healthy situation fires nothing; broken one fires {sorted(fired)}"


# ===================================================================


def main():
    demos = [
        ("S0 history ", demo_s0),
        ("S1 records ", demo_s1),
        ("S2 refs    ", demo_s2),
        ("S3 append  ", demo_s3_warm_start),
        ("S3 retract ", demo_s3_retraction_gap),
        ("S3 defeat  ", demo_s3_grounded),
        ("S4 genres  ", demo_s4_conservativity),
        ("S5 triggers", demo_s5),
    ]
    for label, demo in demos:
        print(f"{label} | {demo()}")


if __name__ == "__main__":
    main()
