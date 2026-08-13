---
why:
  - counter-tech-revenue-bias
  - enable-accountable-deep-work
status: proposal
blocked-on: discussion
trigger: When cash flows are reliably tracked in any system the picker can ingest.
---

# Runway as Master State Variable

Financial runway (months of cash on hand) acts as a master state
variable that auto-tunes per-vital thresholds and exploration
budget allocation:

- Runway > 18 months → exploration encouraged; deep-work budgets large
- Runway 6–18 months → balanced; perishables prioritized
- Runway < 6 months → exploration constrained; cash-generating work dominates

The system changes its own posture as runway changes. The operator
shouldn't have to remember to be more conservative as cash shrinks
— the picker bias does it.

Deferred because: requires reliable runway data from somewhere. No
useful behavior without that input. Graduates when the operator has
runway tracked anywhere mechanical (spreadsheet, banking API,
accounting tool).

## Open questions

The architectural pattern (runway as master state) is settled. The
specifics are not:

- The bracket values (>18mo, 6-18mo, <6mo) are stated as the design,
  not as examples. They're plausible but un-calibrated; real
  cutoffs likely depend on the operator's circumstances (industry,
  dependents, savings appetite, etc.).
- Mechanism: does runway re-tune *tier-2 thresholds* (changing what
  counts as in-debt), or only the *exploration ceiling* (capping
  rabbit-hole budget), or both?
- Override semantics: when runway is short, does it *block*
  exploration entirely, or just reduce the budget? Hard cutoff vs.
  soft penalty.
- Hysteresis: should the brackets have hysteresis to avoid flapping
  when runway hovers near a boundary?
- Source-of-truth: which financial source supplies runway, and what
  happens when sources disagree (e.g., bank balance vs. accounting
  tool)?
