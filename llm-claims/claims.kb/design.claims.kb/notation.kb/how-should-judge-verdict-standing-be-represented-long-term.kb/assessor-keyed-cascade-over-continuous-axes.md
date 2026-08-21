---
label: CASCADE
standing: agent
why:
  - a-fixpoint-over-an-assessor-indexed-evidence-operator.md
---

# Assessor-Keyed Cascade Over Continuous Axes

`llm-discourse-graph`'s unified-claim-scheme design
(`docs/dev/design/unified-claim-scheme/validity-axes.md`,
`.../per-party-validity.md`): a `$all`/per-party map, RFC 7396
merge-patch to override, where a value is three continuous axes
(truth/certainty/utility) rather than a discrete set. Answers both
gaps GRAIN names -- multiple assessors, and a verdict finer than a
fixed enum -- at bounded cost, since a dissenting party restates only
the axis it diverges on, not the whole verdict. Designed 2026-03,
never shipped: the live schema carries neither the map nor the axes,
only a flat `status` and a scalar `likelihood`. Keyed by "party" (a
discussion participant), one notch narrower than STRONGFORM's
judge-is-a-proof case.
