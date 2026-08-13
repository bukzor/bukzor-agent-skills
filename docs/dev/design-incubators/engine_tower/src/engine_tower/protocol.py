"""protocol -- trigger banks as monitor automata.

A bank is one syntactic object: guarded rules over situation
predicates drawn from any lower stratum.  Its semantics is the
synchronized product with the agent's process; the enforcement
ladder (attention -> tooling -> typechecker) varies which machine
computes that product, not the bank.  The bank is generic in the
situation type: concrete situations bundle whatever lower-strata
state their guards need.  [MONITOR, GRADE]
"""

from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Trigger[S]:
    name: str
    guard: Callable[[S], bool]


def fire[S](bank: tuple[Trigger[S], ...], situation: S) -> frozenset[str]:
    """One transition of the synchronized product: the guards that
    hold now.  `fire` is the attention-grade interpreter; compiling
    the same bank into a linter or a type system changes the machine,
    not the bank.  [MONITOR, GRADE]"""
    return frozenset(t.name for t in bank if t.guard(situation))
