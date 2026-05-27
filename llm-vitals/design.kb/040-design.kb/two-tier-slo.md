---
why:
  - tier-1-before-tier-2
  - cadence-bound-checkins
---

# Two-Tier SLO

Each vital has two independent thresholds. Tier 1 must be healthy
before tier 2 is meaningful.

## Tier 1: Check-In Cadence (observability)

The maximum acceptable interval between check-ins for this vital.
Binary and mechanical:

- For journal-kind vitals: when was the last journal entry?
- For task-kind vitals: when did `day-log.jsonl` last mention this
  vital?

Tier 1 corresponds to a **liveness probe** in SRE / Kubernetes
terminology: is the signal arriving at all? If tier 1 is breached, the
priority isn't "your metric is bad," it's "you don't know your metric."

## Tier 2: Metric Threshold (SLO)

A target on a measurable signal *within* reported data. Examples:

- `body`: `sleep_avg_hours >= 7`
- `revenue`: `hours_per_week >= 10`
- `exploration`: `hours_per_day <= 4` (a maximum, not a minimum)

Tier 2 is enforceable only when tier 1 is healthy — you cannot threshold
a metric you haven't observed.

Tier-2 thresholds are softened by error budgets and tracked with
burn-rate alerts; see `error-budget.md` and `burn-rate.md`.

## Ordering Discipline

Always evaluate tier 1 before tier 2. Mixing them produces alarm
fatigue: if you haven't journaled in 11 days, "your sleep average
is 5.5h" is a stale claim, not actionable. Liveness first, SLO
second.
