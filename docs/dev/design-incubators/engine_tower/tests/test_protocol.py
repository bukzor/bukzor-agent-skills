from collections.abc import Mapping
from dataclasses import dataclass

from engine_tower.history import History, state
from engine_tower.protocol import Trigger, fire
from engine_tower.record import Schema
from engine_tower.reference import referentially_closed
from engine_tower.standing import DESCRIBED, STIPULATED, Evidence, standing

MISSION = Schema("mission.v1", frozenset({"schema", "text"}))
CLAIM = Schema("claim.v1", frozenset({"schema", "text", "why"}), frozenset({"why"}))
SCHEMAS = {s.name: s for s in (MISSION, CLAIM)}


@dataclass(frozen=True)
class Situation:
    history: History
    schemas: Mapping[str, Schema]
    entries: frozenset[str]
    evidence: frozenset[Evidence]


def dangling_reference(sit: Situation) -> bool:  # a reference-stratum predicate
    return not referentially_closed(state(sit.history), sit.schemas)


def open_claim(sit: Situation) -> bool:  # a standing-stratum predicate
    st = standing(sit.evidence, sit.entries)
    return any(st[e] == DESCRIBED for e in sit.entries)


BANK = (
    Trigger("dangling-reference", dangling_reference),
    Trigger("open-claim", open_claim),
)

HEALTHY = Situation(
    history=(
        ("m", {"schema": "mission.v1", "text": "the mission"}),
        ("g", {"schema": "claim.v1", "text": "a goal", "why": "m"}),
    ),
    schemas=SCHEMAS,
    entries=frozenset({"m", "g"}),
    evidence=frozenset(
        {Evidence("m", STIPULATED), Evidence("g", STIPULATED, frozenset({"m"}))}
    ),
)


def test_a_healthy_situation_fires_nothing():  # MONITOR
    assert fire(BANK, HEALTHY) == frozenset()


def test_guards_from_two_strata_fire_off_one_situation():  # MONITOR
    # drop the mission record and its warrant
    broken = Situation(
        history=HEALTHY.history[1:],
        schemas=SCHEMAS,
        entries=HEALTHY.entries,
        evidence=frozenset({Evidence("g", STIPULATED, frozenset({"m"}))}),
    )
    assert fire(BANK, broken) == {"dangling-reference", "open-claim"}
