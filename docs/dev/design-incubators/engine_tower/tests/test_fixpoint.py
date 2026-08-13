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


type Pair = tuple[frozenset[str], frozenset[str]]


def phi1(x1: frozenset[str]) -> frozenset[str]:
    # the first coordinate reads only itself -- this is triangularity
    return frozenset({"a"}) | frozenset({"b"} if "a" in x1 else ())


def triangular(
    phi2: Callable[[Pair], frozenset[str]],
) -> Callable[[Pair], Pair]:
    # Phi(x1, x2) = (phi1(x1), phi2(x1, x2)): the second coordinate may
    # read both, the first may not read the second
    def f(x: Pair) -> Pair:
        return (phi1(x[0]), phi2(x))

    return f


def test_a_triangular_operator_restricts_to_its_first_coordinate():  # RESTRICT
    bottom: Pair = (frozenset(), frozenset())
    feeds = triangular(lambda x: frozenset({"x"} if "a" in x[0] else ()) | x[1])
    assert iterate(feeds, bottom)[0] == iterate(phi1, frozenset())
    # enlarging what the second coordinate contributes cannot move the
    # first: the restricted lfp is computable without the upper stratum
    flooded = triangular(lambda _: frozenset({"x", "y"}))
    assert iterate(flooded, bottom)[0] == iterate(feeds, bottom)[0]
    assert iterate(flooded, bottom)[1] != iterate(feeds, bottom)[1]


def test_downward_revision_overshoots():  # OVERSHOOT
    ring: Edges = frozenset({("a", "b"), ("b", "a")})
    old = iterate(op(frozenset({"a"}), ring), frozenset())  # a root feeds the ring
    assert old == {"a", "b"}
    revised = op(frozenset(), ring)  # retract the root
    assert iterate(revised, old) == {"a", "b"}  # descent keeps the ring
    assert iterate(revised, frozenset()) == frozenset()  # the true lfp is empty
