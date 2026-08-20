from itertools import product

import pytest

from engine_tower.fixpoint import iterate
from engine_tower.history import state
from engine_tower.record import Schema
from engine_tower.reference import edges
from engine_tower.standing import (
    DESCRIBED,
    STIPULATED,
    Act,
    Color,
    Evidence,
    Standing,
    certified,
    cite,
    collapse,
    color,
    contest,
    effective,
    grounded,
    phi,
    standing,
    status_leq,
    status_sup,
)


def admits_all(act: Act) -> bool:
    return True


def standing_leq(x: Standing, y: Standing) -> bool:
    return all(status_leq(x[e], y[e]) for e in x)


def test_the_fibered_top_has_no_join():  # STATUS
    assert status_leq(DESCRIBED, certified("a"))
    assert not status_leq(certified("a"), certified("b"))
    with pytest.raises(AssertionError):
        status_sup(certified("a"), certified("b"))


def test_two_checkers_certifying_one_entry_crash_the_operator():  # COMPLETION
    entries = frozenset({"a"})
    ev = frozenset({Evidence("a", certified("c1")), Evidence("a", certified("c2"))})
    with pytest.raises(AssertionError):
        phi(ev, entries)({"a": DESCRIBED})


MISSION = Schema("mission.v1", frozenset({"schema", "text"}))
CLAIM = Schema("claim.v1", frozenset({"schema", "text", "why"}), frozenset({"why"}))
SCHEMAS = {s.name: s for s in (MISSION, CLAIM)}
WARRANTED = {
    "m": {"schema": "mission.v1", "text": "the mission"},
    "g": {"schema": "claim.v1", "text": "a goal", "why": "m"},
}


def test_premises_are_read_off_the_reference_structure():  # OPERATOR
    """OPERATOR raises an entry as far as the evidence citing it
    "through the reference structure" supports.  Premises are
    therefore not a second edge set to be kept in sync by hand: they
    are the entry's out-edges in the quiver."""
    rows = frozenset({Evidence("m", STIPULATED), Evidence("g", STIPULATED)})
    cited = cite(rows, edges(WARRANTED, SCHEMAS))
    assert cited == {
        Evidence("m", STIPULATED),
        Evidence("g", STIPULATED, frozenset({"m"})),  # the same edge, once
    }
    assert standing(cited, frozenset(WARRANTED)) == {"m": STIPULATED, "g": STIPULATED}


def test_an_unwarranted_reference_still_gates_ascent():  # OPERATOR, THRESHOLD
    # drop the mission's own evidence: g's premise falls below
    # THRESHOLD, so citing it no longer lifts g
    cited = cite(frozenset({Evidence("g", STIPULATED)}), edges(WARRANTED, SCHEMAS))
    assert standing(cited, frozenset(WARRANTED))["g"] == DESCRIBED


def test_phi_is_monotone_on_an_instance():  # OPERATOR
    entries = frozenset({"a", "b"})
    ev = frozenset({Evidence("b", STIPULATED, frozenset({"a"}))})
    step = phi(ev, entries)
    lo: Standing = {"a": DESCRIBED, "b": DESCRIBED}
    hi: Standing = {"a": STIPULATED, "b": DESCRIBED}
    assert standing_leq(lo, hi)
    assert standing_leq(step(lo), step(hi))


def test_warm_start_from_old_fixpoint_matches_cold():  # WARM_START, ASYMMETRY
    """Adding evidence: Phi' >= Phi, the old lfp is a pre-fixed point
    of Phi', so upward iteration from it is sound and lands exactly on
    lfp Phi'.  Appends are cheap; the append-only store is a theorem."""
    entries = frozenset({"a", "b"})
    ev1 = frozenset({Evidence("a", STIPULATED)})
    old = standing(ev1, entries)
    ev2 = ev1 | {Evidence("b", STIPULATED, frozenset({"a"}))}
    warm = iterate(phi(ev2, entries), old)  # resume from the old fixpoint
    cold = standing(ev2, entries)  # recompute from bottom
    assert warm == cold


def test_retraction_gap_keeps_the_ring():  # OVERSHOOT, COMPUTED, ASYMMETRY
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
    assert old["a"] == old["b"] == STIPULATED

    retracted = frozenset(ev for ev in ring if ev.entry != "w")
    revised = iterate(phi(retracted, entries), old)  # descend from old state
    fresh = standing(retracted, entries)  # lfp from bottom
    assert revised["a"] == revised["b"] == STIPULATED  # ring holds itself up
    assert fresh["a"] == fresh["b"] == DESCRIBED  # the true lfp reopens it


def test_grounded_decides_a_reinstatement_chain():  # APPROX, DEFEAT
    nodes = frozenset({"a", "b", "c"})
    # c defeats b, b defeats a => c stands, a reinstated
    lo, up = grounded(nodes, frozenset({("c", "b"), ("b", "a")}))
    assert lo == up == {"a", "c"}


def test_grounded_leaves_an_even_cycle_undecided():  # APPROX, DEFEAT
    duo = frozenset({"a", "b"})
    mutual = frozenset({("a", "b"), ("b", "a")})
    lo, up = grounded(duo, mutual)
    assert (lo, up) == (frozenset(), duo)


def test_a_ruling_collapses_the_gap():  # DEFEAT
    duo = frozenset({"a", "b"})
    mutual = frozenset({("a", "b"), ("b", "a")})
    lo, up = grounded(duo, mutual, rulings={"a": True})
    assert lo == up == {"a"}


def test_a_citing_act_strikes_exactly_its_named_targets():  # EXPLICIT
    a1 = Act("u", "p", "accepted", 0)
    a2 = Act("u", "q", "accepted", 1)
    fix = Act("v", "p", "rejected", 2, strikes=frozenset({a1.address}))
    assert effective(frozenset({a1, a2, fix}), admits_all) == {a2, fix}


def test_clashing_uncited_acts_both_stand():  # EXPLICIT -- no recency resolution
    yes = Act("u", "p", "accepted", 0)
    no = Act("u", "p", "rejected", 1)  # same issuer, later, citing nothing
    assert effective(frozenset({yes, no}), admits_all) == {yes, no}


def test_a_clash_computes_to_the_contested_interval():  # EXPLICIT, DEFEAT
    # the same interval whether the clashing assessors are two or one
    for second in ("u", "v"):
        yes = Act("u", "p", "accepted", 0)
        no = Act(second, "p", "rejected", 1)
        eff = effective(frozenset({yes, no}), admits_all)
        assert contest(eff, frozenset({"p"})) == (frozenset(), frozenset({"p"}))


def test_litigation_is_one_move():  # EXPLICIT
    yes = Act("u", "p", "accepted", 0)
    no = Act("v", "p", "rejected", 1)
    resolve = Act("w", "p", "accepted", 2, strikes=frozenset({no.address}))
    eff = effective(frozenset({yes, no, resolve}), admits_all)
    assert contest(eff, frozenset({"p"})) == (frozenset({"p"}), frozenset({"p"}))


def test_self_annulment_is_admitted_by_every_stance():  # EXPLICIT
    ruling = Act("v", "p", "accepted", 0)
    annul = Act("v", "p", "retracted", 1, strikes=frozenset({ruling.address}))

    def admits_no_strikes(act: Act) -> bool:
        return not act.strikes

    assert ruling not in effective(frozenset({ruling, annul}), admits_no_strikes)


def test_force_is_computed_per_stance():  # FORCE
    ruling = Act("u", "p", "accepted", 0)
    strike = Act("v", "p", "rejected", 1, strikes=frozenset({ruling.address}))
    record = frozenset({ruling, strike})
    assert ruling not in effective(record, admits_all)

    def distrusts_v(act: Act) -> bool:
        return act.assessor != "v"

    assert ruling in effective(record, distrusts_v)


def test_act_on_act_reference_is_well_founded():  # ACT
    early = Act("u", "p", "accepted", 0)
    same_moment = Act("v", "p", "rejected", 0, strikes=frozenset({early.address}))
    with pytest.raises(AssertionError):
        effective(frozenset({early, same_moment}), admits_all)


def test_a_claim_survives_restatement_an_act_does_not():  # ONE_WAY, ACT
    # restating a claim edits the same row: the history folds to one entry
    restated = state(
        (("p", {"text": "first wording"}), ("p", {"text": "second wording"}))
    )
    assert len(restated) == 1
    # the "same" judgment issued twice is two acts: indexical, unrepeatable
    twice = {Act("u", "p", "accepted", 0), Act("u", "p", "accepted", 1)}
    assert len({act.address for act in twice}) == 2


def test_collapse_climbs_the_presupposition_chain():  # SENSE
    # q defeated; p presupposes q; r presupposes p: the collapse chains
    presupposes = frozenset({("p", "q"), ("r", "p")})
    assert collapse(presupposes, frozenset({"q"})) == {"p", "r"}


def test_a_presupposition_cycle_is_rejected():  # DESCEND
    """Were the cycle admitted, defeating either end would moot both,
    and the acts that seeded the collapse would land on a claim that
    absorbs them -- a defeat that erases its own evidence."""
    cycle = frozenset({("p", "q"), ("q", "p")})
    with pytest.raises(AssertionError, match=r"presuppose themselves: \['p', 'q'\]"):
        collapse(cycle, frozenset({"q"}))


def test_a_disputed_presupposition_leaves_sense_contested():  # SENSE
    # q is clashed, not defeated -- "there is a king of france" is in
    # dispute.  p's subject is in doubt, not gone: p is not moot, and
    # neither is it plainly `in`, which is what a point-valued answer
    # was forced to say.  The two coordinates carry both facts.
    claims = frozenset({"p", "q"})
    presupposes = frozenset({("p", "q")})
    record = frozenset(
        {
            Act("u", "q", "accepted", 0),
            Act("v", "q", "rejected", 1),
            Act("u", "p", "accepted", 2),
        }
    )
    assert color(claims, presupposes, record, admits_all) == {
        "q": Color("in", "contested"),
        "p": Color("contested", "in"),
    }


def test_a_moot_claim_is_never_also_content_defeated():  # ABSORB, SENSE
    claims = frozenset({"p", "q"})
    presupposes = frozenset({("p", "q")})
    record = frozenset(
        {
            Act("u", "q", "rejected", 0),  # kills the presupposition
            Act("u", "p", "rejected", 1),  # a content-defeat that must be absorbed
        }
    )
    assert color(claims, presupposes, record, admits_all) == {
        "q": Color("in", "out"),
        "p": Color("out", None),
    }


def test_a_color_has_no_content_where_it_has_no_sense():  # SENSE, ABSORB
    """The exclusion is structural, not a precedence rule: there is no
    value of the pair that is both moot and content-defeated."""
    with pytest.raises(AssertionError, match="content is absent exactly"):
        Color("out", "out")
    with pytest.raises(AssertionError, match="content is absent exactly"):
        Color("contested", None)


def test_moot_absorbs_content_acts():  # ABSORB -- exhaustive over small records
    """A moot claim sits outside the truth order: any content-act on
    it has no force, so adding one changes no claim's color."""
    claims = frozenset({"p", "q"})
    pool = [
        Act(assessor, target, verdict, occasion)
        for occasion, (assessor, target, verdict) in enumerate(
            product("uv", "pq", ("accepted", "rejected"))
        )
    ]
    for presupposes in (frozenset(), frozenset({("p", "q")})):
        for bits in range(2 ** len(pool)):
            record = frozenset(act for i, act in enumerate(pool) if bits >> i & 1)
            before = color(claims, presupposes, record, admits_all)
            for target in claims:
                if not before[target].moot:
                    continue
                for verdict in ("accepted", "rejected"):
                    extra = Act("w", target, verdict, len(pool))
                    after = color(claims, presupposes, record | {extra}, admits_all)
                    assert after == before, (record, extra, before, after)
