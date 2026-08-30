---
label: CHAIN
standing: user
why:
  - a-rung-is-a-theory.md
---

# Priors Are a DAG, Not a Ladder

A claim's `why:` names whatever claims it would be revisited over,
whatever rung they sit on. The mission-goals-requirements-architecture
ladder is the common shape of that graph, never a rule about it, so a
design claim citing a goal directly is an ordinary long edge rather
than an error to lint.

This dissolves both escape hatches the incumbent format needed. It
permitted same-rung `why:` "when the motivating concept naturally
lives at the same layer", and it exempted auxiliary collections
(`use-cases.kb/`, `background.kb/`) from the numbered chain
altogether. Under a DAG neither is an exception: a same-rung arrow is
an arrow, and an auxiliary theory is a theory whose priors are not
rung-shaped.

The declined alternative is the strict ladder with a lint on
rung-skipping, which the 2026-08-06 plan had proposed as "the
interpolation rule" -- mint the mediating requirement and route
through it. It loses because the rule cannot distinguish a missing
requirement from a claim that genuinely rests on a goal, and a lint
that fires on both teaches its reader to silence it.
