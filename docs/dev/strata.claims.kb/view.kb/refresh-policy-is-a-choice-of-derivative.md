---
label: DERIVATIVE
standing: agent
why:
  - a-cache-is-lawful-iff-the-triangle-commutes.md
---

# Refresh Policy Is a Choice of Derivative

A view refreshes incrementally exactly when it has a derivative: a
map taking (current value, incoming update) to the new value, agreeing
with recomputation. Every view has the trivial derivative -- discard
and recompute -- so a refresh policy is a per-view choice: a real
derivative where one exists and is worth its bookkeeping, the trivial
one plus a staleness budget elsewhere.

There is no third option; "we'll keep it roughly up to date" is the
trivial derivative with an unstated budget.
