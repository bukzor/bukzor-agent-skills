---
why:
  - visible-debt
  - counter-tech-revenue-bias
---

# Debt as Prioritization

The picker biases work selection by **current debt magnitude across
vitals**, not by static importance. The most-in-debt vital surfaces
first; ties broken by configured per-vital weight.

This is structurally an **SLO-violation-driven scheduler**: at any
moment, the system picks work that closes the largest current SLO
breach. The mechanism replaces single-axis ranking (which can't
represent multi-domain rotting) with multi-axis debt comparison.

Concrete consequence: if revenue debt is 12 days and tech debt is 0,
the picker proposes revenue work in slot 1 even if no individual
revenue task is "important" in isolation. The aggregate debt is the
signal.

Tie-breaking weights exist but are deliberately weak — the system
trusts measured debt over static rankings.
