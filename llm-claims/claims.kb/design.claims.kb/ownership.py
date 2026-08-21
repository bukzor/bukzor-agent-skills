#!/usr/bin/env python3
"""Runnable law for the ownership theory (ownership.md).

Each subcommand witnesses one claim on a minimal fixture fleet; run
with no argument to run them all. The corpus-facing scan is
llm-claims-kb/bin/llm-claims-kb-ownership; this file is the law the
claims cite, small enough to read against them.
"""

from __future__ import annotations

import sys
from collections.abc import Callable
from dataclasses import dataclass, replace

Path = tuple[str, ...]


@dataclass(frozen=True)
class Theory:
    """One position in a fleet: what it coins, says, defines, and cites."""

    path: Path
    ontology: frozenset[str] = frozenset()
    says: frozenset[str] = frozenset()
    labels: frozenset[str] = frozenset()
    mentions: frozenset[str] = frozenset()
    imports: tuple[Path, ...] = ()


Fleet = frozenset[Theory]


class Contention(Exception):
    """Two owners for one word: an error charged to both stipulations."""


def at(fleet: Fleet, path: Path) -> Theory:
    """The theory at a path."""
    found = [t for t in fleet if t.path == path]
    assert len(found) == 1, (path, found)
    return found[0]


def is_prefix(shorter: Path, longer: Path) -> bool:
    """Containment, read off the paths."""
    return longer[: len(shorter)] == shorter


def ledger_of(t: Theory) -> str:
    """SORT_REACH: the namespace is per-ledger; the root names the ledger."""
    return t.path[0]


def interior(fleet: Fleet, owner_t: Theory) -> Fleet:
    """CONTAINMENT_ADMITS: containment admits downward without an arrow."""
    return frozenset(t for t in fleet if is_prefix(owner_t.path, t.path))


def ancestors_of(fleet: Fleet, t: Theory) -> Fleet:
    """The ancestor move: a synthesis may say its parts' words (REACH)."""
    return frozenset(a for a in fleet if is_prefix(a.path, t.path) and a.path != t.path)


def imported_closure(fleet: Fleet, t: Theory) -> Fleet:
    """Every theory the taker imports, the chain included."""
    seen: set[Theory] = set()
    frontier = [t]
    while frontier:
        for p in frontier.pop().imports:
            taker = at(fleet, p)
            if taker not in seen:
                seen.add(taker)
                frontier.append(taker)
    return frozenset(seen)


def importers(fleet: Fleet, owner_t: Theory) -> Fleet:
    """Whoever reaches the owner by import, through a chain or directly.

    An import carries its own imports onward, because a theory has to be
    able to read what it rests on, and a prior's claims are written in
    the prior's priors' words: reach truncated at one hop leaves a taker
    unable to read its own premises. One law, two sorts -- the label sort
    has always resolved this way, and the sorts differ in the shape of
    the finding, never in the law.
    """
    return frozenset(t for t in fleet if owner_t in imported_closure(fleet, t))


def ledger(fleet: Fleet, owner_t: Theory) -> Fleet:
    """SORT_REACH: the namespace the owner governs, and the only one."""
    return frozenset(t for t in fleet if ledger_of(t) == ledger_of(owner_t))


def answerable(fleet: Fleet, owner_t: Theory) -> Fleet:
    """LOCAL: standing runs to the owner's siblings and no further."""
    return frozenset(
        t
        for t in ledger(fleet, owner_t)
        if t.path[:-1] == owner_t.path[:-1] and t.path != owner_t.path
    )


def reach(fleet: Fleet, owner_t: Theory) -> Fleet:
    """REACH: the ledger less the siblings, who enter by importing."""
    return ledger(fleet, owner_t) - (
        answerable(fleet, owner_t) - importers(fleet, owner_t)
    )


def stipulators(fleet: Fleet, word: str) -> Fleet:
    """Every theory whose ontology lists the word."""
    return frozenset(t for t in fleet if word in t.ontology)


def owner(fleet: Fleet, word: str, namespace: str) -> Theory | None:
    """OUTERMOST_WINS on nesting; CONTENTION raises, one ledger at a time."""
    claimants = frozenset(
        t for t in stipulators(fleet, word) if ledger_of(t) == namespace
    )
    outermost = frozenset(
        t
        for t in claimants
        if not any(is_prefix(o.path, t.path) and o.path != t.path for o in claimants)
    )
    if not outermost:
        return None
    elif len(outermost) > 1:
        raise Contention(word, sorted(t.path for t in outermost))
    else:
        (winner,) = outermost
        return winner


def licensed(fleet: Fleet, word: str, site: Theory) -> bool:
    """DEFAULT: an unowned word is free; owned, license is reach (LICENSE)."""
    who = owner(fleet, word, ledger_of(site))
    if who is None:
        return True
    else:
        return site in reach(fleet, who)


def word_findings(fleet: Fleet) -> frozenset[tuple[Path, Path, str]]:
    """TRESPASS: a non-importing sibling of the owner, saying the word."""
    return frozenset(
        (who.path, site.path, word)
        for site in fleet
        for word in site.says
        if (who := owner(fleet, word, ledger_of(site))) is not None
        and not licensed(fleet, word, site)
    )


def force(fleet: Fleet, word: str) -> int:
    """EXCLUSION_FORCE: findings generated -- a property of the neighbours."""
    return len([f for f in word_findings(fleet) if f[2] == word])


def resolves(fleet: Fleet, label: str, site: Theory) -> bool:
    """A label resolves at home or through an import."""
    home = frozenset(t for t in fleet if ledger_of(t) == ledger_of(site))
    return any(label in t.labels for t in home | imported_closure(fleet, site))


def label_findings(fleet: Fleet) -> frozenset[tuple[Path, str]]:
    """DANGLING: charged to the mentioning site; no prosecutor is needed."""
    return frozenset(
        (site.path, label)
        for site in fleet
        for label in site.mentions
        if not resolves(fleet, label, site)
    )


def cull(fleet: Fleet, owner_path: Path, word: str) -> Fleet:
    """FOUR_POSITIONS, the owner's side: the word was no coinage."""
    t = at(fleet, owner_path)
    return (fleet - {t}) | {replace(t, ontology=t.ontology - {word})}


def move(fleet: Fleet, site_path: Path, into: Path) -> Fleet:
    """FOUR_POSITIONS, the speaker's position: refile inside the owner."""
    t = at(fleet, site_path)
    return (fleet - {t}) | {replace(t, path=into + (t.path[-1],))}


def admit(fleet: Fleet, site_path: Path, owner_path: Path) -> Fleet:
    """FOUR_POSITIONS, the license: import the owner (priced: ADMIT_PRICED)."""
    t = at(fleet, site_path)
    return (fleet - {t}) | {replace(t, imports=t.imports + (owner_path,))}


def uniquify(fleet: Fleet, site_path: Path, word: str, fresh: str) -> Fleet:
    """FOUR_POSITIONS, the word itself: the two meanings differ."""
    t = at(fleet, site_path)
    return (fleet - {t}) | {replace(t, says=(t.says - {word}) | {fresh})}


def witness_default() -> str:
    """DEFAULT: an unowned word is free; an unowned label dangles."""
    fleet = frozenset(
        {
            Theory(
                path=("L", "s"),
                says=frozenset({"tide"}),
                mentions=frozenset({"GHOST"}),
            )
        }
    )
    assert word_findings(fleet) == frozenset(), word_findings(fleet)
    dangles = label_findings(fleet)
    assert dangles == frozenset({(("L", "s"), "GHOST")}), dangles
    return (
        "the unowned word is free; the undefined label dangles, charged to its holder"
    )


def witness_dangling() -> str:
    """DANGLING: confessed by its holder, and resolved by an import."""
    fleet = frozenset(
        {
            Theory(path=("A", "t"), labels=frozenset({"KNOWN"})),
            Theory(path=("B", "u"), mentions=frozenset({"KNOWN"})),
        }
    )
    dangles = label_findings(fleet)
    assert dangles == frozenset({(("B", "u"), "KNOWN")}), dangles
    repaired = label_findings(admit(fleet, ("B", "u"), ("A", "t")))
    assert repaired == frozenset(), repaired
    return "a foreign label dangles at its mention site; an import resolves it"


def witness_owner() -> str:
    """OUTERMOST_WINS on nesting; CONTENTION on doubles; per-ledger throughout."""
    nested = frozenset(
        {
            Theory(path=("L", "o"), ontology=frozenset({"w"})),
            Theory(path=("L", "o", "i"), ontology=frozenset({"w"})),
        }
    )
    who = owner(nested, "w", "L")
    assert who is not None and who.path == ("L", "o"), who
    foreign = frozenset(
        {
            Theory(path=("L", "a"), ontology=frozenset({"w"})),
            Theory(path=("M", "b"), ontology=frozenset({"w"})),
        }
    )
    theirs = owner(foreign, "w", "M")
    assert theirs is not None and theirs.path == ("M", "b"), theirs
    siblings = frozenset(
        {
            Theory(path=("L", "a"), ontology=frozenset({"w"})),
            Theory(path=("L", "b"), ontology=frozenset({"w"})),
        }
    )
    try:
        owner(siblings, "w", "L")
    except Contention:
        return "the outer owns; each ledger answers for itself; a double contends"
    raise AssertionError(("sibling double resolved, should have raised", siblings))


def witness_reach() -> str:
    """REACH: the ledger less the owner's siblings, who enter by importing."""
    o = Theory(path=("L", "o"), ontology=frozenset({"w"}))
    inside = Theory(path=("L", "o", "i"))
    root = Theory(path=("L",))
    taker = Theory(path=("L", "m"), imports=(("L", "o"),))
    sibling = Theory(path=("L", "s"))
    nephew = Theory(path=("L", "s", "n"))
    fleet = frozenset({o, inside, root, taker, sibling, nephew})
    r = reach(fleet, o)
    assert {inside, root, taker, nephew} <= r, sorted(t.path for t in r)
    assert sibling not in r, sibling
    return "only the bare sibling is barred; importing lets it back in"


def witness_moves() -> str:
    """The three old moves survive the collapse: each is merely not a sibling."""
    o = Theory(path=("L", "o"), ontology=frozenset({"w"}))
    fleet = frozenset(
        {
            o,
            Theory(path=("L", "o", "i")),
            Theory(path=("L",)),
            Theory(path=("L", "m"), imports=(("L", "o"),)),
            Theory(path=("L", "m", "n")),
        }
    )
    moves = interior(fleet, o) | ancestors_of(fleet, o)
    for taker in importers(fleet, o):
        moves |= interior(fleet, taker)
    assert moves <= reach(fleet, o), sorted(t.path for t in moves - reach(fleet, o))
    return "interior, ancestors, importers' interiors: all inside the one exclusion"


def witness_trespass() -> str:
    """TRESPASS: the sibling speaks and is charged; nephew and stranger are free."""
    fleet = frozenset(
        {
            Theory(path=("L", "o"), ontology=frozenset({"w"})),
            Theory(path=("L", "s"), says=frozenset({"w"})),
            Theory(path=("L", "s", "n"), says=frozenset({"w"})),
            Theory(path=("M", "f"), says=frozenset({"w"})),
        }
    )
    found = word_findings(fleet)
    assert found == frozenset({(("L", "o"), ("L", "s"), "w")}), found
    return "the sibling alone; the nephew is licensed, the foreign site ungoverned"


def witness_force() -> str:
    """SCREENING: the docket is force > 0; the unowned never appear on it."""
    fleet = frozenset(
        {
            Theory(path=("L", "o"), ontology=frozenset({"w"})),
            Theory(path=("L", "s"), says=frozenset({"w", "haze"})),
            Theory(path=("L", "t"), says=frozenset({"haze"})),
            Theory(path=("L", "q"), ontology=frozenset({"quiet"})),
        }
    )
    docket = {word for (_, _, word) in word_findings(fleet)}
    assert docket == {"w"}, docket
    assert force(fleet, "w") == 1, force(fleet, "w")
    assert force(fleet, "haze") == 0, force(fleet, "haze")
    assert force(fleet, "quiet") == 0, force(fleet, "quiet")
    return "the docket holds w alone; the shared unowned word and the idle coinage score zero"


def witness_repairs() -> str:
    """FOUR_POSITIONS: each repair singly discharges the fixture's finding."""
    fleet = frozenset(
        {
            Theory(path=("L", "o"), ontology=frozenset({"w"})),
            Theory(path=("L", "s"), says=frozenset({"w"})),
        }
    )
    assert len(word_findings(fleet)) == 1, word_findings(fleet)
    repaired = [
        cull(fleet, ("L", "o"), "w"),
        move(fleet, ("L", "s"), ("L", "o")),
        admit(fleet, ("L", "s"), ("L", "o")),
        uniquify(fleet, ("L", "s"), "w", "w2"),
    ]
    for after in repaired:
        assert word_findings(after) == frozenset(), word_findings(after)
    return "cull, move, admit, uniquify: each alone clears the docket"


def witness_nonmonotone() -> str:
    """YIELD's retraction: a repair discharges one finding and mints another.

    The move that clears w carries the site into the interior of a theory whose
    own child owns v, making the site that child's sibling for the first time.
    """
    fleet = frozenset(
        {
            Theory(path=("L", "o"), ontology=frozenset({"w"})),
            Theory(path=("L", "o", "c"), ontology=frozenset({"v"})),
            Theory(path=("L", "s"), says=frozenset({"w", "v"})),
        }
    )
    before = word_findings(fleet)
    assert before == frozenset({(("L", "o"), ("L", "s"), "w")}), before
    after = word_findings(move(fleet, ("L", "s"), ("L", "o")))
    expected = frozenset({(("L", "o", "c"), ("L", "o", "s"), "v")})
    assert after == expected, after
    return "the move clears the w finding and mints a v finding: not monotone"


WITNESSES: dict[str, Callable[[], str]] = {
    "default": witness_default,
    "dangling": witness_dangling,
    "owner": witness_owner,
    "reach": witness_reach,
    "moves": witness_moves,
    "trespass": witness_trespass,
    "force": witness_force,
    "repairs": witness_repairs,
    "nonmonotone": witness_nonmonotone,
}


def main(argv: list[str]) -> int:
    """Run the named witnesses, or all of them."""
    names = argv[1:] if len(argv) > 1 else sorted(WITNESSES)
    for name in names:
        assert name in WITNESSES, (name, sorted(WITNESSES))
        print(f"{name}: {WITNESSES[name]()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
