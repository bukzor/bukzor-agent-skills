import pytest

from engine_tower.fixpoint import iterate
from engine_tower.standing import (
    DESCRIBED,
    STIPULATED,
    Evidence,
    Standing,
    certified,
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
