---
why:
  - tier-1-before-tier-2
  - wellness-as-upstream
---

# Error Budget

Imported from SRE. Each vital's tier-2 threshold is paired with a
**budget of misses** per rolling window rather than expressed as an
absolute requirement.

Example: instead of "≥3 movement sessions every week" (which
guarantees failure feelings on a hard week), the threshold is "≥3
movement sessions/week with a budget of 1 miss per 4-week window."

Why this matters:

- **Humane**: a single bad week doesn't trigger an alert; reality
  includes bad weeks.
- **Accurate**: most real-life thresholds are stochastic, not
  deterministic.
- **Defendable**: when the budget is exhausted, the alert is honest
  ("you're now over budget"); the operator cannot dismiss it as
  noise.

The error budget is also what enables burn-rate alerting (see
`burn-rate.md`): leading indicators only make sense when there's a
budget to project consumption against.
