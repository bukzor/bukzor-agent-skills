import pytest

from engine_tower.fixpoint import iterate
from engine_tower.record import Schema
from engine_tower.reference import edges
from engine_tower.standing import (
    DESCRIBED,
    STIPULATED,
    Evidence,
    Standing,
    certified,
    cite,
    grounded,
    phi,
    standing,
    status_leq,
    status_sup,
)


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
