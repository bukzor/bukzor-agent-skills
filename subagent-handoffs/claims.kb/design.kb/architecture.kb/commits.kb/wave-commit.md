---
label: WAVE_COMMIT
standing: user
verdict: superseded
why:
  - ../../requirements.kb/unit-diff.md
---

# The coordinator commits at each wave boundary

The coordinator commits once per wave, after every unit in it has
reported.

Superseded by UNIT_COMMIT (`unit-commit.md`), itself superseded by
AGENT_COMMIT (`agent-commit.md`). A wave's commit holds every unit that ran in it, so no unit can be
reviewed or reverted alone. In practice wave commits ran to thousands
of lines, and work left uncommitted between waves needed a unit of
its own just to commit it.
