"""The tower applied to its own code: module imports respect the
theory poset, and the poset is READ FROM the ledger rather than
mirrored -- the ledger's `why:` lines are the only copy.  [STRATA]"""

import ast
from pathlib import Path

SRC = Path(__file__).parent.parent / "src" / "engine_tower"
LEDGER = Path(__file__).parents[3] / "strata.claims.kb"
assert LEDGER.is_dir(), LEDGER  # no ledger, no poset: fail, never skip

# theories with no computational content, so no module: regime
# requirements (purpose), proper nouns (fleet), past-tense provenance
# (question), and the capstone -- `tower` lives as this test file
NON_CODE = frozenset({"purpose", "fleet", "question", "tower"})


def names(text: str) -> set[str]:
    """The theory names in one `why:` payload -- block item or inline
    list, both of which the ledger writes."""
    return {
        part.strip().strip("[],'\"").removeprefix("- ").removesuffix(".md")
        for part in text.split(",")
        if part.strip(" []")
    }


def priors(theory: str) -> frozenset[str]:
    """The theory's declared priors: the `why:` of its defining claim,
    as bare theory names.  A root theory has no `why:`."""
    lines = (LEDGER / f"{theory}.md").read_text().splitlines()
    assert lines[0] == "---", (theory, lines[0])
    out: set[str] = set()
    in_why = False
    for line in lines[1 : lines.index("---", 1)]:
        if in_why and line.startswith(" "):
            out |= names(line)
        else:
            in_why = line.startswith("why:")
            if in_why:
                out |= names(line.removeprefix("why:"))
    return frozenset(out)


THEORIES = frozenset(p.stem for p in LEDGER.glob("*.md")) - {"CLAUDE"}
ALL_PRIORS = {t: priors(t) for t in THEORIES}
# a module may import only from the downward closure of its declared
# priors, restricted to the code-bearing theories -- edges into
# non-code theories drop out of the induced subgraph
CODE = THEORIES - NON_CODE
PRIORS = {t: p & CODE for t, p in ALL_PRIORS.items() if t in CODE}


def closure(theory: str, graph: dict[str, frozenset[str]] = PRIORS) -> frozenset[str]:
    out: set[str] = set()
    frontier = set(graph[theory])
    while frontier:
        t = frontier.pop()
        if t not in out:
            out.add(t)
            frontier |= graph[t]
    return frozenset(out)


def internal_imports(module: str) -> frozenset[str]:
    tree = ast.parse((SRC / f"{module}.py").read_text())
    found: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module:
                parts = node.module.split(".")
                if parts[0] == "engine_tower":
                    found.add(parts[1])
                elif node.level:  # from .sibling import name
                    found.add(parts[0])
            elif node.level:  # from . import sibling
                found.update(alias.name for alias in node.names)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                parts = alias.name.split(".")
                if parts[0] == "engine_tower":
                    found.add(parts[1])
    return frozenset(found)


def test_the_modules_are_exactly_the_theories():
    on_disk = {p.stem for p in SRC.glob("*.py")} - {"__init__"}
    assert on_disk == set(PRIORS)


def test_the_declared_priors_are_a_poset():  # STRATA
    # `why:` names a strictly lower theory, so the whole ledger graph
    # -- not just its code-bearing part -- must be acyclic
    for theory in ALL_PRIORS:
        assert theory not in closure(theory, ALL_PRIORS), theory


def test_imports_respect_the_poset():  # STRATA
    for module in PRIORS:
        illegal = internal_imports(module) - closure(module)
        assert not illegal, (module, illegal)
