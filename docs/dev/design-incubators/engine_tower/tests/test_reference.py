from engine_tower.history import State
from engine_tower.record import Schema
from engine_tower.reference import (
    COUNT,
    PROVENANCE,
    cone,
    edges,
    path_weight,
    reachable,
    referentially_closed,
)

MISSION = Schema("mission.v1", frozenset({"schema", "text"}))
CLAIM = Schema(
    "claim.v1", frozenset({"schema", "text", "why"}), frozenset({"why", "basis"})
)
SCHEMAS = {s.name: s for s in (MISSION, CLAIM)}
RECORDS: State = {
    "m": {"schema": "mission.v1", "text": "the mission"},
    "g": {"schema": "claim.v1", "text": "a goal", "why": "m"},
    "r1": {"schema": "claim.v1", "text": "a req", "why": "g", "basis": "m"},
}
EDGES = edges(RECORDS, SCHEMAS)


def test_ref_fields_present_a_quiver():  # QUIVER
    assert referentially_closed(RECORDS, SCHEMAS)
    assert EDGES == {("g", "m"), ("r1", "g"), ("r1", "m")}


def test_reachability_is_a_least_fixpoint():  # REACH
    assert reachable(EDGES, frozenset({"r1"})) == {"r1", "g", "m"}
    # every entry reachable from the mission-cone: the design-tower condition
    assert cone(EDGES, "m") == {"m", "g", "r1"}


def test_semiring_weights_count_support_chains():  # WEIGHT
    assert path_weight(EDGES, "r1", "m", COUNT, lambda _: 1) == 2


def test_provenance_semiring_returns_the_chains():  # WEIGHT
    chains = path_weight(EDGES, "r1", "m", PROVENANCE, lambda e: frozenset({(e,)}))
    assert chains == {
        (("r1", "g"), ("g", "m")),
        (("r1", "m"),),
    }
