---
why:
  - multi-axis-surface
---

# Vocabulary

Canonical terms used throughout the skill. Naming chosen for concept
↔ ontic match, drawing on medical, SRE, and EOS prior art.

| Term | Meaning |
|---|---|
| **vital** | A category of activity tracked for minimum maintenance (body, revenue, ops, ...). |
| **kind** | The reporting mechanism for a vital: `journal` or `task`. |
| **check-in** | A single reporting event (journal entry or day-log mention). |
| **tier 1** | Check-in cadence requirement (max interval). The observability layer. |
| **tier 2** | Metric threshold within reported data. The SLO layer. |
| **threshold** | General term for tier-2 target (may be minimum *or* maximum). |
| **minimum** | A floor-shaped threshold (e.g., ≥3 sessions/week). |
| **maximum** | A ceiling-shaped threshold (e.g., ≤4h exploration/day). |
| **error budget** | Allowed misses per rolling window before threshold alerts. |
| **debt** | Time since last met, or magnitude of current violation. |
| **status** | Green / yellow / red, summarizing tier 1 + tier 2 + burn rate. |
| **burn rate** | Leading-indicator projection of impending threshold breach. |

The word **vital** is load-bearing: it does conceptual work for both
medical audiences (vital signs) and SRE audiences (golden signals).
Both communities independently converged on multi-axis health
monitoring — the term lets us inherit both pieces of prior art.

Terms explicitly rejected: `track` (no semantic weight), `slo`
(opaque to non-SREs), `pillars` (pop self-help), `commitments`
(obligational rather than observational), `signals` (loses health
intuition for non-SREs).
