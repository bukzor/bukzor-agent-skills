"""Witnesses for the background order theory in its own vocabulary:
operators on bare frozensets, no upper-strata imports."""

from collections.abc import Callable

from engine_tower.fixpoint import iterate

type Edges = frozenset[tuple[str, str]]


def op(roots: frozenset[str], edges: Edges) -> Callable[[frozenset[str]], frozenset[str]]:
    # F(X) = roots ∪ post(X): monotone but not inflationary, so
    # downward iteration is possible and the overshoot is visible
    def f(x: frozenset[str]) -> frozenset[str]:
        return roots | frozenset(dst for src, dst in edges if src in x)

    return f


def test_iteration_from_bottom_computes_the_least_fixpoint():  # KNASTER
    f = op(frozenset({"w"}), frozenset({("w", "a"), ("a", "b")}))
    lfp = iterate(f, frozenset())
    assert lfp == {"w", "a", "b"}
    assert f(lfp) == lfp


def test_warm_start_is_sound_upward():  # WARM_START
    roots = frozenset({"w"})
    old = iterate(op(roots, frozenset({("w", "a")})), frozenset())
    grown = op(roots, frozenset({("w", "a"), ("a", "b")}))
    assert iterate(grown, old) == iterate(grown, frozenset())


def test_downward_revision_overshoots():  # OVERSHOOT
    ring: Edges = frozenset({("a", "b"), ("b", "a")})
    old = iterate(op(frozenset({"a"}), ring), frozenset())  # a root feeds the ring
    assert old == {"a", "b"}
    revised = op(frozenset(), ring)  # retract the root
    assert iterate(revised, old) == {"a", "b"}  # descent keeps the ring
    assert iterate(revised, frozenset()) == frozenset()  # the true lfp is empty
