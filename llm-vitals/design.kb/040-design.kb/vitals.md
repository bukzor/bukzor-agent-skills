---
why:
  - multi-axis-surface
  - visible-debt
---

# Vitals

The central primitive. A **vital** is a category of activity the user
commits to maintaining at a minimum level over time. Examples:
`revenue`, `body`, `relationships`, `ops`.

## Concept

Each vital has:
- A **kind** (journal vs. task — see `vital-kinds.md`)
- A **tier 1 cadence** (max interval between check-ins)
- A **tier 2 threshold** (target on a metric, when defined) — see
  `two-tier-slo.md`
- A current **debt** (time since tier 1 was last met, or magnitude of
  tier 2 violation)
- A **status** (green / yellow / red) summarizing the above

## Why "vital"

The word does explanatory work for both audiences:

- **Medical**: vital signs (pulse, BP, respiration, temp) are the
  multi-dimensional "is the patient alive and healthy?" check.
- **SRE**: the "golden signals" (latency, traffic, errors, saturation)
  are explicitly the systems analog of vital signs.

Both communities independently converged on multi-axis health
monitoring with per-axis thresholds. "Vital" carries both
connotations: medical observability *and* technical SLO discipline.

Other names considered and rejected:

- **tracks** — generic, no semantic weight
- **slo** — opaque to non-SREs; loses the health intuition
- **pillars** — pop-self-help coded; loses technical resonance
- **commitments** — obligational rather than observational
- **signals** — strong SRE pedigree but loses the multi-axis health
  intuition for non-SREs

## Cardinality

Recommended: ~4 wellness vitals (`body`, `relationships`,
`restoration`, `meaning`), ~5 work vitals (`revenue`, `customer`,
`tech`, `maintenance`, `exploration`), and ~3 business vitals
(`ops`, `marketing`, `monitoring`) — added as needed.

Total ~12 vitals is the upper bound of what fits in working memory
when reviewing the dashboard. Fewer underspecifies the life surface;
more dilutes attention.
