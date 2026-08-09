"""view -- derived values and the commuting triangle.  [TRIANGLE]"""

from collections.abc import Callable

from engine_tower.history import History, State, state


def lawful[A](cached: A, view: Callable[[State], A], history: History) -> bool:
    """A materialized view is lawful iff the triangle commutes -- the
    stored answer equals the view of the replayed state.  Cache drift
    is exactly the failure of this equation.  [TRIANGLE]"""
    return cached == view(state(history))
