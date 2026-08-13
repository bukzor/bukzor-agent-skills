"""genre -- confinement, conservativity, the satisfaction condition.

Entries live in a home vocabulary (confinement, the syntactic half);
standing restricts along theory inclusion unchanged (conservativity,
the semantic half).  Because standing fixed one node sort and one
rule format, a genre extension can only add Evidence rows about its
own entries -- conservativity holds by construction; give genres
their own node sorts and it becomes a per-genre proof obligation.
[CONFINE, CONSERVE, SATISFACTION, FREE_CONSERVE]
"""

from engine_tower.standing import Evidence, Standing


def restrict(x: Standing, entries: frozenset[str]) -> Standing:
    """The reduct M'|_W: forget the extension's entries.  [CONSERVE]"""
    return {e: s for e, s in x.items() if e in entries}


def confined(extension: frozenset[Evidence], own_entries: frozenset[str]) -> bool:
    """The syntactic half, as a predicate: extension evidence
    concludes only on the genre's own entries.  Premises may cite
    anything.  [CONFINE]"""
    return all(ev.entry in own_entries for ev in extension)
