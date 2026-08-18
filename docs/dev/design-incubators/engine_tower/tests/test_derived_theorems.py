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
    Act,
    Stance,
    affirms,
    color,
    contest,
    effective,
    moot,
)

ASSESSORS = ("u", "v", "w")
ORDER = ("p", "q", "r")  # presupposition runs down it
CLAIMS = frozenset(ORDER)
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
                draw(sampled_from(ORDER)),
                draw(sampled_from(VERDICTS)),
                occasion,
                draw(frozensets(sampled_from(earlier))) if earlier else frozenset(),
            )
        )
    return frozenset(acts)


@composite
def presuppositions(draw) -> frozenset[Edge]:
    """A frame graph running down the claim order, hence acyclic --
    the tower's own discipline [STRATA].  A cycle would make a claim's
    frame turn on its own defeat, which is a different subject."""
    downward = [(src, dst) for i, src in enumerate(ORDER) for dst in ORDER[:i]]
    return draw(frozensets(sampled_from(downward)))


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


def test_the_generator_reaches_every_color():
    """The properties below are conditioned on color -- a moot claim,
    a defeated one.  A generator that stopped reaching one would leave
    them quiet rather than red, so it fails here instead."""
    for wanted in ("moot", "in", "contested", "out"):
        find(
            tuples(presuppositions(), records()),
            lambda case, wanted=wanted: wanted
            in color(CLAIMS, *case, admits_all).values(),
            settings=PROPERTY,
        )


@PROPERTY
@given(records(), presuppositions(), stances(), sampled_from(VERDICTS), data())
def test_moot_absorbs_content_acts_in_any_record(
    record, presupposes, admits, verdict, choose
):  # ABSORB
    """A moot claim sits outside the truth order, so a content-act on
    it has nothing to move: adding one leaves every claim's color
    where it was, however the record already struck."""
    # an assessor this reader credits -- an act they discount would
    # pass the property by having no force at all
    assessor = choose.draw(sampled_from(sorted(admits.assessors)))
    before = color(CLAIMS, presupposes, record, admits)
    for target in sorted(CLAIMS):
        if before[target] != "moot":
            continue
        extra = Act(assessor, target, verdict, len(record))
        after = color(CLAIMS, presupposes, record | {extra}, admits)
        assert after == before, f"+{extra.address} {verdict}: {before} -> {after}"


def color_by_iteration(
    claims: frozenset[str],
    presupposes: frozenset[Edge],
    record: frozenset[Act],
    admits: Stance,
) -> Mapping[str, str]:
    """The collapse cycle run to a fixpoint: contest, collapse the
    frames that defeat took out, contest again over what is left, and
    repeat while the moot set grows.  `color` takes one pass, and that
    the two agree is the property below."""
    eff = effective(record, admits)
    mooted: frozenset[str] = frozenset()
    while True:
        live = claims - mooted
        lower, upper = contest(frozenset(a for a in eff if a.target in live), live)
        grown = mooted | moot(presupposes, (live - upper) | mooted)
        if grown != mooted:
            mooted = grown
            continue
        return {
            c: (
                "moot"
                if c in mooted
                else "in" if c in lower else "contested" if c in upper else "out"
            )
            for c in claims
        }


@PROPERTY
@given(records(), presuppositions(), stances())
def test_one_collapse_pass_reaches_the_fixpoint(record, presupposes, admits):  # LOCAL
    """Acts on a moot claim attack only that claim and each other, so
    dropping them moves no surviving claim's interval: a second round
    has no further collapse to find."""
    one_pass = color(CLAIMS, presupposes, record, admits)
    to_fixpoint = color_by_iteration(CLAIMS, presupposes, record, admits)
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
    record, presupposes, naming
):
    """To a reader who admits everything, who judged is not a fact the
    algebra can see: rename the assessors -- three into one, or one
    into three -- and every claim keeps its color.  A clash computes
    to the contested interval whether the clashing assessors are two
    or one; so with everything else."""
    before = color(CLAIMS, presupposes, record, admits_all)
    after = color(CLAIMS, presupposes, renamed(record, naming), admits_all)
    assert after == before, f"{naming}: {before} -> {after}"


@PROPERTY
@given(records(), presuppositions(), sampled_from(ORDER))
def test_litigation_is_one_move_in_any_record(record, presupposes, target):  # EXPLICIT
    """Litigation is one move, from any record whatever: an act
    affirming the claim and striking every effective act against it
    leaves the claim un-attacked.  Where the frame has collapsed there
    is nothing to win -- content cannot mend a moot claim."""
    before = color(CLAIMS, presupposes, record, admits_all)
    against = frozenset(
        act.address
        for act in effective(record, admits_all)
        if act.target == target and not affirms(act)
    )
    move = Act("x", target, "accepted", len(record), strikes=against)
    after = color(CLAIMS, presupposes, record | {move}, admits_all)
    assert after[target] == ("moot" if before[target] == "moot" else "in"), (
        f"+{move.address} accepted striking {sorted(against)}: "
        f"{target} {before[target]} -> {after[target]}"
    )
