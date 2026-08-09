from engine_tower.history import History, State
from engine_tower.view import lawful

HISTORY: History = (("m", {"text": "mission"}), ("g", {"text": "goal"}))


def keys_view(s: State) -> frozenset[str]:
    return frozenset(s)


def test_fresh_cache_is_lawful():  # TRIANGLE
    assert lawful(frozenset({"m", "g"}), keys_view, HISTORY)


def test_stale_cache_fails_the_triangle():  # TRIANGLE
    assert not lawful(frozenset({"m"}), keys_view, HISTORY)
