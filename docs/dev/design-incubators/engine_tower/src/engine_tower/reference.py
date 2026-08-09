"""reference -- quivers, reachability, cones, weights.

Ref-valued fields present a quiver on keys.  Referential integrity is
the pullback condition (edges land on existing keys).  Reachability
is a least fixpoint; cones are up-sets; valuing edges in a semiring
turns reachability into counting or provenance.  Taint is the same
lfp shape.  [QUIVER, REACH, WEIGHT, TAINT]
"""

import operator
from collections.abc import Callable, Mapping
from dataclasses import dataclass

from engine_tower.fixpoint import iterate
from engine_tower.history import State
from engine_tower.record import Schema

type Edge = tuple[str, str]  # (src_key, dst_key)


def edges(s: State, schemas: Mapping[str, Schema]) -> frozenset[Edge]:
    """The quiver Q(I) presented by the instance's ref-valued fields.
    [QUIVER]"""
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
    """lfp X. roots ∪ post(X) -- the reachability preorder, pointwise.
    [REACH]"""

    def step(x: frozenset[str]) -> frozenset[str]:
        return roots | frozenset(dst for src, dst in es if src in x) | x

    return iterate(step, frozenset())


def cone(es: frozenset[Edge], key: str) -> frozenset[str]:
    """The invalidation cone ↑key: everything that reaches key --
    reachability in the reversed quiver.  Taint has this exact type.
    [TAINT]"""
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
    gives the chains themselves.  Assumes the quiver is a DAG.
    [WEIGHT]"""
    if src == dst:
        return sr.one
    acc = sr.zero
    for edge in es:
        if edge[0] == src:
            acc = sr.plus(acc, sr.times(w(edge), path_weight(es, edge[1], dst, sr, w)))
    return acc
