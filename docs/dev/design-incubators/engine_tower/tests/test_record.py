from engine_tower.history import Payload
from engine_tower.record import Migration, Schema, validates

CLAIM_V1 = Schema("claim.v1", frozenset({"schema", "text", "why"}))
CLAIM_V2 = Schema("claim.v2", frozenset({"schema", "text", "because"}))


def test_validation_is_a_typing_judgment():  # TYPING
    p: Payload = {"schema": "claim.v1", "text": "cycles are unproven", "why": "k7"}
    assert validates(p, CLAIM_V1)
    assert not validates({"schema": "claim.v1"}, CLAIM_V1)


def test_rename_migration_lands_in_the_target_fiber():  # MIGRATE
    def rename_why(p: Payload) -> Payload:
        q = {**p, "because": p["why"], "schema": "claim.v2"}
        del q["why"]
        return q

    m = Migration(CLAIM_V1, CLAIM_V2, rename_why)
    p: Payload = {"schema": "claim.v1", "text": "cycles are unproven", "why": "k7"}
    assert validates(p, m.source), p
    assert validates(m.push(p), m.target), m.push(p)
