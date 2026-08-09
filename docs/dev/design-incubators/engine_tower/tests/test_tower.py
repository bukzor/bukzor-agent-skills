"""The tower applied to its own code: module imports respect the
theory poset of ../../../strata.ledger.md.  [STRATA]"""

import ast
from pathlib import Path

SRC = Path(__file__).parent.parent / "src" / "engine_tower"

# the poset, mirrored from the ledger's theory table; a module may
# import only from the downward closure of its declared priors
PRIORS: dict[str, frozenset[str]] = {
    "fixpoint": frozenset(),
    "history": frozenset(),
    "view": frozenset({"history"}),
    "record": frozenset({"history"}),
    "reference": frozenset({"record", "fixpoint"}),
    "standing": frozenset({"reference", "view", "fixpoint"}),
    "genre": frozenset({"standing"}),
    "protocol": frozenset({"history", "view"}),
}


def closure(theory: str) -> frozenset[str]:
    out: set[str] = set()
    frontier = set(PRIORS[theory])
    while frontier:
        t = frontier.pop()
        if t not in out:
            out.add(t)
            frontier |= PRIORS[t]
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


def test_imports_respect_the_poset():  # STRATA
    for module in PRIORS:
        illegal = internal_imports(module) - closure(module)
        assert not illegal, (module, illegal)
