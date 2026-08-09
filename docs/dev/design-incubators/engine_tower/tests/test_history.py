from engine_tower.history import History, state

H1: History = (("m", {"text": "mission v1"}),)
H2: History = (("m", {"text": "mission v2"}), ("g", {"text": "goal"}))


def test_state_is_a_monoid_action():  # FOLD
    assert state(H1 + H2) == {**state(H1), **state(H2)}


def test_any_prefix_is_queryable():  # WORD
    h = H1 + H2
    assert state(h[:1]) == {"m": {"text": "mission v1"}}
    assert state(h)["m"] == {"text": "mission v2"}
