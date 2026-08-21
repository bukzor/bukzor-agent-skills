"""The act algebra's derived results, checked by quantification.

`tests/test_standing.py` witnesses each ruled claim on the smallest
instance that exhibits it.  What is checked here is derived rather
than ruled -- absorption [ABSORB], one-pass sufficiency [LOCAL],
assessor invariance [BLIND], litigation [EXPLICIT] -- and a derived
result is a claim about every record, so the smallest instance is
the wrong witness for it.  Generated records carry what the minimal
ones cannot: strikes, three claims, a presupposition chain, and all
four verdict words.
"""

from collections.abc import Mapping
from dataclasses import dataclass, replace

from hypothesis import find, given, settings
from hypothesis.strategies import (
    composite,
    data,
    fixed_dictionaries,
    frozensets,
    integers,
    sampled_from,
    tuples,
)

from engine_tower.reference import Edge
from engine_tower.standing import (
    FALSE,
    TRUE,
    UNKNOWN,
    Act,
    Disposition,
    Stance,
    Tri,
    affirms,
    collapse,
    contest,
    disposition,
    effective,
    frames,
)

ASSESSORS = ("u", "v", "w")
ORDER = ("p", "q", "r")  # presupposition runs down it
EDGE_CLAIMS = {
    f"{src}-needs-{dst}": (src, dst) for i, src in enumerate(ORDER) for dst in ORDER[:i]
}
CLAIMS = frozenset(ORDER) | frozenset(EDGE_CLAIMS)
TARGETS = tuple(sorted(CLAIMS))  # an act may land on an edge-claim [EDGE]
VERDICTS = ("accepted", "certified", "rejected", "retracted")

# derandomized, and with no example database: a failure must reproduce
# from this file alone, from whatever directory the suite was run
PROPERTY = settings(derandomize=True, database=None, deadline=None, max_examples=200)


def admits_all(act: Act) -> bool:
    return True


@composite
def records(draw) -> frozenset[Act]:
    """A record of up to five acts, each free to strike any earlier
    one.  One act per occasion keeps addresses distinct and `strikes`
    well-founded by construction; the only configuration that loses is
    simultaneity, which can strike nothing and so folds like acts on
    distinct occasions anyway."""
    acts: list[Act] = []
    for occasion in range(draw(integers(0, 5))):
        earlier = sorted(act.address for act in acts)
        acts.append(
            Act(
                draw(sampled_from(ASSESSORS)),
                draw(sampled_from(TARGETS)),
                draw(sampled_from(VERDICTS)),
                occasion,
                draw(frozensets(sampled_from(earlier))) if earlier else frozenset(),
            )
        )
    return frozenset(acts)


@composite
def presuppositions(draw) -> Mapping[str, Edge]:
    """The edge-claims on offer: a frame graph running down the claim
    order, hence acyclic -- the tower's own discipline [STRATA], and
    the engine's precondition [DESCEND].  Drawing a cycle would sample
    outside the domain, where the properties below say nothing and
    `collapse` raises.

    Which of these a reader is holding is not decided here.  These are
    claims, and the record settles them like any other [EDGE]."""
    offered = draw(frozensets(sampled_from(sorted(EDGE_CLAIMS))))
    return {name: EDGE_CLAIMS[name] for name in sorted(offered)}


@dataclass(frozen=True)
class Trusting:
    """A reader's stance: the assessors this reader credits.  Named
    rather than a lambda so that a falsifying example prints a stance
    the reader can reconstruct."""

    assessors: frozenset[str]

    def __call__(self, act: Act) -> bool:
        return act.assessor in self.assessors


@composite
def stances(draw) -> Trusting:
    return Trusting(draw(frozensets(sampled_from(ASSESSORS), min_size=1)))


def test_the_generator_reaches_every_disposition():
    """The properties below are conditioned on disposition -- a
    collapsed claim, a defeated one.  A generator that stopped reaching
    one would leave them quiet rather than red, so it fails here
    instead.  Both coordinates are swept: a disputed subject is as much
    a case to reach as a defeated one, and nothing else here would
    notice if the generator never drew it."""
    for field in ("live", "upheld"):
        for wanted in Tri:
            find(
                tuples(presuppositions(), records()),
                lambda case, field=field, wanted=wanted: any(
                    getattr(c, field) is wanted
                    for c in disposition(CLAIMS, *case, admits_all).values()
                ),
                settings=PROPERTY,
            )
    # and the case the liveness bounds turn on: an edge-claim in
    # dispute, which must reach the upper collapse and not the lower
    # [EDGE]
    find(
        tuples(presuppositions(), records()),
        lambda case: any(
            disposition(CLAIMS, *case, admits_all)[name].upheld is UNKNOWN
            for name in case[0]
        ),
        settings=PROPERTY,
    )


@PROPERTY
@given(records(), presuppositions(), stances(), sampled_from(VERDICTS), data())
def test_a_collapsed_claim_absorbs_verdicts_in_any_record(
    record, edge_claims, admits, verdict, choose
):  # ABSORB
    """A collapsed claim sits outside the truth order, so a verdict on
    it has nothing to move: adding one leaves every claim's disposition
    where it was, however the record already struck."""
    # an assessor this reader credits -- an act they discount would
    # pass the property by having no force at all
    assessor = choose.draw(sampled_from(sorted(admits.assessors)))
    before = disposition(CLAIMS, edge_claims, record, admits)
    for target in sorted(CLAIMS):
        if not before[target].collapsed:
            continue
        extra = Act(assessor, target, verdict, len(record))
        after = disposition(CLAIMS, edge_claims, record | {extra}, admits)
        assert after == before, f"+{extra.address} {verdict}: {before} -> {after}"


def disposition_by_iteration(
    claims: frozenset[str],
    edge_claims: Mapping[str, Edge],
    record: frozenset[Act],
    admits: Stance,
) -> Mapping[str, Disposition]:
    """The collapse cycle run to a fixpoint: contest, collapse the
    subjects that defeat took out, contest again over what is left,
    and repeat while the collapsed set grows.  The other bound is read
    the same way at the end, off the settled pass.  `disposition` takes
    one pass for both, and that the two agree is the property below."""
    eff = effective(record, admits)
    surely: frozenset[str] = frozenset()
    while True:
        live = claims - surely
        lower, upper = contest(frozenset(a for a in eff if a.target in live), live)
        grown = surely | collapse(frames(edge_claims, lower), (live - upper) | surely)
        if grown != surely:
            surely = grown
            continue
        possibly = collapse(frames(edge_claims, upper), (live - lower) | surely)
        return {
            c: (
                Disposition(FALSE, UNKNOWN)
                if c in surely
                else Disposition(
                    UNKNOWN if c in possibly else TRUE,
                    TRUE if c in lower else UNKNOWN if c in upper else FALSE,
                )
            )
            for c in claims
        }


@PROPERTY
@given(records(), presuppositions(), stances())
def test_one_collapse_pass_reaches_the_fixpoint(record, edge_claims, admits):  # LOCAL
    """Acts on a collapsed claim attack only that claim and each other,
    so dropping them moves no surviving claim's interval: a second
    round has no further collapse to find."""
    one_pass = disposition(CLAIMS, edge_claims, record, admits)
    to_fixpoint = disposition_by_iteration(CLAIMS, edge_claims, record, admits)
    assert one_pass == to_fixpoint, f"one pass {one_pass}, iterated {to_fixpoint}"


def renamed(record: frozenset[Act], naming: Mapping[str, str]) -> frozenset[Act]:
    """Every act's assessor through `naming`, with `strikes` following
    the addresses they name."""
    moved = {
        act.address: replace(act, assessor=naming[act.assessor]).address
        for act in record
    }
    return frozenset(
        replace(
            act,
            assessor=naming[act.assessor],
            strikes=frozenset(moved[address] for address in act.strikes),
        )
        for act in record
    )


@PROPERTY
@given(
    records(),
    presuppositions(),
    fixed_dictionaries({a: sampled_from(ASSESSORS) for a in ASSESSORS}),
)
def test_assessor_identity_carries_no_force_of_its_own(  # BLIND
    record, edge_claims, naming
):
    """To a reader who admits everything, who judged is not a fact the
    algebra can see: rename the assessors -- three into one, or one
    into three -- and every claim keeps its disposition.  A clash
    computes to the contested interval whether the clashing assessors
    are two or one; so with everything else."""
    before = disposition(CLAIMS, edge_claims, record, admits_all)
    after = disposition(CLAIMS, edge_claims, renamed(record, naming), admits_all)
    assert after == before, f"{naming}: {before} -> {after}"


@PROPERTY
@given(records(), presuppositions(), sampled_from(TARGETS))
def test_litigation_is_one_move_in_any_record(record, edge_claims, target):  # EXPLICIT
    """Litigation is one move, from any record whatever: an act
    affirming the claim and striking every effective act against it
    leaves the claim un-attacked.  It settles `upheld` and nothing
    else -- the subject is other claims' business, so the move that
    wins the point leaves a disputed subject exactly as disputed, and
    where the subject is gone there is nothing to win at all."""
    before = disposition(CLAIMS, edge_claims, record, admits_all)
    against = frozenset(
        act.address
        for act in effective(record, admits_all)
        if act.target == target and not affirms(act)
    )
    move = Act("x", target, "accepted", len(record), strikes=against)
    after = disposition(CLAIMS, edge_claims, record | {move}, admits_all)
    won = (
        before[target]
        if before[target].collapsed
        else Disposition(before[target].live, TRUE)
    )
    assert after[target] == won, (
        f"+{move.address} accepted striking {sorted(against)}: "
        f"{target} {before[target]} -> {after[target]}, wanted {won}"
    )
