"""fixpoint -- shared order-theoretic background.  [KNASTER]"""

from collections.abc import Callable


def iterate[T](f: Callable[[T], T], start: T) -> T:
    """Kleene iteration to a fixpoint.  From bottom this computes the
    least fixpoint; from a post-fixed point it descends only to the
    greatest fixpoint below the start.  Same loop, asymmetric meaning.
    [WARM_START, OVERSHOOT]"""
    x = start
    while (x2 := f(x)) != x:
        x = x2
    return x
