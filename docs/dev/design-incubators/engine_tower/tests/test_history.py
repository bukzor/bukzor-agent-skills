from engine_tower.history import History, state

H1: History = (("m", {"text": "mission v1"}),)
H2: History = (("m", {"text": "mission v2"}), ("g", {"text": "goal"}))


def test_state_is_a_monoid_action():  # FOLD
    assert state(H1 + H2) == {**state(H1), **state(H2)}


def test_a_branch_has_no_canonical_fold():  # MERGE
    """WORD keeps a word and FOLD is defined on one, so a store that
    branches is outside both.  Two branches off a common prefix that
    write the same key admit two linearizations, and they fold to
    different states -- the merge's state is not determined by the
    branches.  Some further law (a merge update, a payload algebra
    that commutes, a total order every branch respects) has to supply
    the missing choice."""
    prefix: History = (("m", {"text": "mission v1"}),)
    left: History = (("m", {"text": "left"}),)
    right: History = (("m", {"text": "right"}),)
    assert state(prefix + left + right) != state(prefix + right + left)


def test_any_prefix_is_queryable():  # WORD
    h = H1 + H2
    assert state(h[:1]) == {"m": {"text": "mission v1"}}
    assert state(h)["m"] == {"text": "mission v2"}
