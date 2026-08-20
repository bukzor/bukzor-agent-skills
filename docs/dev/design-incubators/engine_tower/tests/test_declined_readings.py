"""Why presupposition is not a connective [SENSE].

SENSE declines two truth-functional readings of "the king of france
is bald": the conjunctive one, which makes the claim plain `out` when
there is no king, and the conditional one, which makes it plain `in`.
The argument that neither can carry a presupposition rests on facts
about intuitionistic propositional logic, and citing a fact is not
checking it -- so this checks them, by brute force over every preorder
on <=3 worlds and every monotone valuation of two atoms.

Semantics: w |= p iff p in V(w); w |= A->B iff every v >= w with
v |= A has v |= B; w |= bot never.  ~A := A -> bot.  A formula is
valid iff it holds at every world of every model; a countermodel
refutes it.  Two controls -- excluded middle and double negation
elimination -- fail here and would pass under a classical checker,
which is what makes the other five results mean anything.

Nothing here imports the engine.  It is a witness for a claim the
engine's shape rests on, not for the engine.
"""

from dataclasses import dataclass
from itertools import product
from typing import Mapping

import pytest

type Formula = tuple
type Upsets = Mapping[int, frozenset[int]]
type Valuation = Mapping[int, frozenset[str]]

BOT: Formula = ("bot",)
A: Formula = ("atom", "A")
B: Formula = ("atom", "B")


def imp(x: Formula, y: Formula) -> Formula:
    return ("imp", x, y)


def neg(x: Formula) -> Formula:
    return imp(x, BOT)


def conj(x: Formula, y: Formula) -> Formula:
    return ("and", x, y)


def disj(x: Formula, y: Formula) -> Formula:
    return ("or", x, y)


def show(f: Formula) -> str:
    kind = f[0]
    if kind == "bot":
        return "F"
    elif kind == "atom":
        return f[1]
    elif kind == "imp":
        return f"~{show(f[1])}" if f[2] == BOT else f"({show(f[1])} -> {show(f[2])})"
    elif kind == "and":
        return f"({show(f[1])} & {show(f[2])})"
    elif kind == "or":
        return f"({show(f[1])} | {show(f[2])})"
    else:
        raise AssertionError(f"unknown connective: {kind}")


def holds(f: Formula, world: int, up: Upsets, val: Valuation) -> bool:
    """`f` at `world`, where `up[w]` is the worlds >= w and `val[w]`
    the atoms true at w."""
    kind = f[0]
    if kind == "bot":
        return False
    elif kind == "atom":
        return f[1] in val[world]
    elif kind == "and":
        return holds(f[1], world, up, val) and holds(f[2], world, up, val)
    elif kind == "or":
        return holds(f[1], world, up, val) or holds(f[2], world, up, val)
    elif kind == "imp":
        return all(
            holds(f[2], v, up, val) for v in up[world] if holds(f[1], v, up, val)
        )
    else:
        raise AssertionError(f"unknown connective: {kind}")


def preorders(n: int):
    """Every reflexive transitive relation on `n` worlds, as up-sets."""
    worlds = range(n)
    pairs = [(i, j) for i in worlds for j in worlds if i != j]
    for bits in product((False, True), repeat=len(pairs)):
        rel = {(i, i) for i in worlds} | {p for p, b in zip(pairs, bits) if b}
        transitive = all((i, k) in rel for (i, j) in rel for (j2, k) in rel if j == j2)
        if transitive:
            yield {i: frozenset(j for j in worlds if (i, j) in rel) for i in worlds}


def valuations(up: Upsets, atoms: tuple[str, ...]):
    """Monotone valuations: an atom true at w stays true above w."""
    worlds = sorted(up)
    upsets = [
        frozenset(s)
        for bits in product((False, True), repeat=len(worlds))
        for s in [{w for w, b in zip(worlds, bits) if b}]
        if all(up[w] <= frozenset(s) for w in s)
    ]
    for choice in product(upsets, repeat=len(atoms)):
        yield {w: frozenset(a for a, s in zip(atoms, choice) if w in s) for w in worlds}


def countermodel(f: Formula, size: int = 3):
    """A model and world refuting `f`, or None if none exists at this
    size.  A miss is not a proof of validity -- three worlds is enough
    for every case below, and no more is claimed."""
    for up in preorders(size):
        for val in valuations(up, ("A", "B")):
            for w in sorted(up):
                if not holds(f, w, up, val):
                    return up, val, w
    return None


@dataclass(frozen=True)
class Reading:
    name: str
    formula: Formula
    valid: bool
    why: str


CASES = (
    Reading(
        "ex-falso",
        imp(BOT, B),
        True,
        "a refuted presupposition makes the conditional reading vacuous, "
        "constructively too -- so rejecting excluded middle does not save it",
    ),
    Reading(
        "conditional-reading-says-bald",
        imp(neg(A), imp(A, B)),
        True,
        "no king => (king -> bald) holds: the conditional reading reports "
        "the claim upheld exactly where it has nothing to talk about",
    ),
    Reading(
        "the-classical-step",
        imp(imp(A, B), disj(neg(A), B)),
        False,
        "(A->B) == (~A|B) is the step that makes the conditional reading "
        "look like a disjunction; it is not available here",
    ),
    Reading(
        "de-morgan",
        imp(neg(conj(A, B)), disj(neg(A), neg(B))),
        False,
        "refuting the conjunctive reading does not locate the failure: "
        "'not (king and bald)' does not say which one failed",
    ),
    Reading(
        "both-polarities-refuted",
        imp(neg(A), conj(neg(conj(A, B)), neg(conj(A, neg(B))))),
        True,
        "no king => 'is bald' and 'is not bald' are both refuted, "
        "consistently -- the polarity-invariance a presupposition has "
        "and an attack does not",
    ),
    Reading(
        "control-excluded-middle",
        disj(A, neg(A)),
        False,
        "control: a classical checker would call this valid",
    ),
    Reading(
        "control-double-negation",
        imp(neg(neg(A)), A),
        False,
        "control: a classical checker would call this valid",
    ),
)


@pytest.mark.parametrize("case", CASES, ids=lambda c: c.name)
def test_a_truth_functional_reading_cannot_carry_presupposition(case):  # SENSE
    found = countermodel(case.formula)
    if (found is None) != case.valid:
        witness = "no countermodel at 3 worlds"
        if found is not None:
            up, val, w = found
            order = ", ".join(f"{k}<={sorted(v)}" for k, v in sorted(up.items()))
            true_at = ", ".join(
                f"{k}:{sorted(v) or '-'}" for k, v in sorted(val.items())
            )
            witness = f"refuted at world {w}: [{order}] [{true_at}]"
        raise AssertionError(
            f"{show(case.formula)} wanted "
            f"{'valid' if case.valid else 'refuted'}, got {witness}\n"
            f"  {case.why}"
        )
