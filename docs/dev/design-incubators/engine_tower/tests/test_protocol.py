from collections.abc import Mapping
from dataclasses import dataclass

from engine_tower.history import History, state
from engine_tower.protocol import Trigger, fire
from engine_tower.record import Schema
from engine_tower.reference import edges, referentially_closed
from engine_tower.standing import DESCRIBED, STIPULATED, Evidence, cite, standing

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

HISTORY: History = (
    ("m", {"schema": "mission.v1", "text": "the mission"}),
    ("g", {"schema": "claim.v1", "text": "a goal", "why": "m"}),
)
# the g -> m edge is written once, in the record; the evidence rows
# read their premises off the quiver [OPERATOR]
GRANTS = frozenset({Evidence("m", STIPULATED), Evidence("g", STIPULATED)})

HEALTHY = Situation(
    history=HISTORY,
    schemas=SCHEMAS,
    entries=frozenset({"m", "g"}),
    evidence=cite(GRANTS, edges(state(HISTORY), SCHEMAS)),
)


def test_a_healthy_situation_fires_nothing():  # MONITOR
    assert fire(BANK, HEALTHY) == frozenset()


def test_guards_from_two_strata_fire_off_one_situation():  # MONITOR
    # drop the mission record and its warrant; g still cites m, so
    # the dangling edge is also g's unmet premise
    history = HISTORY[1:]
    broken = Situation(
        history=history,
        schemas=SCHEMAS,
        entries=HEALTHY.entries,
        evidence=cite(
            frozenset({Evidence("g", STIPULATED)}), edges(state(history), SCHEMAS)
        ),
    )
    assert fire(BANK, broken) == {"dangling-reference", "open-claim"}
