---
why:
  - visible-debt
  - tier-1-before-tier-2
---

# Burn Rate

Leading-indicator alerts that project a vital's trajectory toward
threshold breach **before** the breach occurs.

Example: "body vital projected to breach the sleep SLO in 3 days at
current pace."

Direct import from SRE. SLO breach alerts are lagging; burn-rate
alerts are leading. Both have value; leading-indicator alerts
generally beat lagging ones because they enable preemptive action.

Computed cheaply from the day-log + journal entries: current
consumption rate against remaining error budget. No new
infrastructure required.

Burn-rate alerts are tier-2 features — they require tier-1 data
(check-ins) and tier-2 configuration (error budgets). Layer them on
only after both are in place.
