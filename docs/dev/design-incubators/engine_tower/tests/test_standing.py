from itertools import product

import pytest

from engine_tower.fixpoint import iterate
from engine_tower.history import state
from engine_tower.record import Schema
from engine_tower.reference import edges
from engine_tower.standing import (
    DESCRIBED,
    FALSE,
    OBLIGATED,
    STIPULATED,
    TRUE,
    UNKNOWN,
    Act,
    Disposition,
    Evidence,
    Standing,
    certified,
    cite,
    collapse,
    contest,
    disposition,
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


def test_the_status_chain_orders_by_commitment():  # STATUS
    """The claim names four rungs in a particular order, so the check
    runs the whole chain rather than one pair of it: each rung strictly
    below the next, and no rung below its predecessor."""
    chain = (DESCRIBED, STIPULATED, OBLIGATED, certified("a"))
    for lower, higher in zip(chain, chain[1:]):
        assert status_leq(lower, higher), (lower, higher)
        assert not status_leq(higher, lower), (higher, lower)


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


def test_a_second_row_grants_where_the_first_is_dead():  # REWIRE
    """Within a row support is conjunctive -- the test above is one
    failed premise killing a grant.  Across rows it is disjunctive: a
    second row on the same entry grants on its own.  That is why
    repair is rewiring: a stronger grant filed into the dead row is
    spend without effect, however far it is raised."""
    entries = frozenset({"g", "m", "n"})
    dead = Evidence("g", STIPULATED, frozenset({"m"}))  # m is never warranted
    live = Evidence("g", STIPULATED, frozenset({"n"}))
    warrants_n = Evidence("n", STIPULATED)
    assert standing(frozenset({dead, warrants_n}), entries)["g"] == DESCRIBED
    assert standing(frozenset({dead, live, warrants_n}), entries)["g"] == STIPULATED
    louder = Evidence("g", OBLIGATED, frozenset({"m"}))
    assert standing(frozenset({dead, louder, warrants_n}), entries)["g"] == DESCRIBED


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


def test_collapse_climbs_the_presupposition_chain():  # SPLIT
    # q defeated; p presupposes q; r presupposes p: the collapse chains
    presupposes = frozenset({("p", "q"), ("r", "p")})
    assert collapse(presupposes, frozenset({"q"})) == {"p", "r"}


def test_a_presupposition_cycle_is_rejected():  # DESCEND
    """Were the cycle admitted, defeating either end would collapse
    both, and the acts that seeded the collapse would land on a claim
    that absorbs them -- a defeat that erases its own evidence."""
    cycle = frozenset({("p", "q"), ("q", "p")})
    with pytest.raises(AssertionError, match=r"presuppose themselves: \['p', 'q'\]"):
        collapse(cycle, frozenset({"q"}))


CLAIMS = frozenset({"p", "q", "p-needs-q"})
NEEDS = {"p-needs-q": ("p", "q")}  # the edge, as a claim of the base [EDGE]


def test_a_disputed_presupposition_leaves_live_unknown():  # SPLIT
    # q is clashed, not defeated -- "there is a king of france" is in
    # dispute.  p's subject is in doubt, not gone: p has not collapsed,
    # and neither is it plainly live, which is what a point-valued
    # answer was forced to say.  The two coordinates carry both facts.
    record = frozenset(
        {
            Act("u", "q", "accepted", 0),
            Act("v", "q", "rejected", 1),
            Act("u", "p", "accepted", 2),
        }
    )
    assert disposition(CLAIMS, NEEDS, record, admits_all) == {
        "q": Disposition(TRUE, UNKNOWN),
        "p": Disposition(UNKNOWN, TRUE),
        "p-needs-q": Disposition(TRUE, TRUE),  # unopposed, so the reader holds it
    }


def test_a_collapsed_claim_is_never_also_defeated():  # ABSORB, SPLIT
    record = frozenset(
        {
            Act("u", "q", "rejected", 0),  # kills the presupposition
            Act("u", "p", "rejected", 1),  # a defeat that must be absorbed
        }
    )
    assert disposition(CLAIMS, NEEDS, record, admits_all) == {
        "q": Disposition(TRUE, FALSE),
        "p": Disposition(FALSE, UNKNOWN),
        "p-needs-q": Disposition(TRUE, TRUE),
    }


def test_a_defeated_edge_claim_collapses_nothing():  # EDGE
    """q is refuted, but the claim that p needs q is refuted too: the
    reader is not holding that edge, so it collapses nothing.  An edge
    handed in beside the record could not be answered this way."""
    record = frozenset(
        {
            Act("u", "q", "rejected", 0),
            Act("u", "p-needs-q", "rejected", 1),
        }
    )
    assert disposition(CLAIMS, NEEDS, record, admits_all) == {
        "q": Disposition(TRUE, FALSE),
        "p": Disposition(TRUE, TRUE),
        "p-needs-q": Disposition(TRUE, FALSE),
    }


def test_a_disputed_edge_claim_cannot_collapse_surely():  # EDGE, SPLIT
    """q is surely defeated and the edge is merely in dispute, so the
    edge reaches the upper bound and not the lower: p's liveness is
    unknown, the same answer a surely-held edge to a disputed q gives.
    A contested edge that collapsed outright would let a claim be
    erased on a frame nobody had established."""
    record = frozenset(
        {
            Act("u", "q", "rejected", 0),
            Act("u", "p-needs-q", "accepted", 1),
            Act("v", "p-needs-q", "rejected", 2),
        }
    )
    assert disposition(CLAIMS, NEEDS, record, admits_all) == {
        "q": Disposition(TRUE, FALSE),
        "p": Disposition(UNKNOWN, TRUE),
        "p-needs-q": Disposition(TRUE, UNKNOWN),
    }


def test_two_readers_hold_different_frames():  # EDGE, STANCE
    """The frame graph is reader-relative, because it is read out of
    the record and the record is read under a stance.  One reader
    credits the assessor who struck the edge and one does not; they
    disagree about whether p is live at all, from the same record."""
    record = frozenset(
        {
            Act("u", "q", "rejected", 0),
            Act("u", "p-needs-q", "accepted", 1),
            Act("v", "p-needs-q", "rejected", 2),
        }
    )

    def trusts_only_u(act: Act) -> bool:
        return act.assessor == "u"

    assert disposition(CLAIMS, NEEDS, record, trusts_only_u)["p"] == Disposition(
        FALSE, UNKNOWN
    )
    assert disposition(CLAIMS, NEEDS, record, admits_all)["p"] == Disposition(
        UNKNOWN, TRUE
    )


def test_an_edge_claim_is_a_claim_of_the_base():  # EDGE, ACT
    """Both halves of that: an edge over a claim the base does not
    hold is rejected, and so is a presupposition over an edge-claim --
    the stratification that keeps the two levels from recursing."""
    with pytest.raises(AssertionError, match="edge-claims outside the base"):
        disposition(frozenset({"p", "q"}), NEEDS, frozenset(), admits_all)
    with pytest.raises(AssertionError, match="presupposition over edge-claims"):
        disposition(
            CLAIMS | {"r", "r-needs-the-edge"},
            NEEDS | {"r-needs-the-edge": ("r", "p-needs-q")},
            frozenset(),
            admits_all,
        )


def test_a_collapsed_claim_answers_no_truth_question():  # SPLIT, ABSORB
    """The exclusion is structural, not a precedence rule: no value of
    the pair is both collapsed and settled on the merits, either way."""
    with pytest.raises(AssertionError, match="no truth question"):
        Disposition(FALSE, FALSE)
    with pytest.raises(AssertionError, match="no truth question"):
        Disposition(FALSE, TRUE)


def test_a_collapsed_claim_absorbs_verdicts():  # ABSORB -- exhaustive, small records
    """A collapsed claim sits outside the truth order: any verdict on
    it has no force, so adding one moves no claim's disposition."""
    pool = [
        Act(assessor, target, verdict, occasion)
        for occasion, (assessor, target, verdict) in enumerate(
            product("uv", "pq", ("accepted", "rejected"))
        )
    ]
    for edge_claims in ({}, NEEDS):
        for bits in range(2 ** len(pool)):
            record = frozenset(act for i, act in enumerate(pool) if bits >> i & 1)
            before = disposition(CLAIMS, edge_claims, record, admits_all)
            for target in CLAIMS:
                if not before[target].collapsed:
                    continue
                for verdict in ("accepted", "rejected"):
                    extra = Act("w", target, verdict, len(pool))
                    after = disposition(
                        CLAIMS, edge_claims, record | {extra}, admits_all
                    )
                    assert after == before, (record, extra, before, after)
