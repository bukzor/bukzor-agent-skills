---
why:
  - grow-incrementally
  - wellness-as-upstream
---

# Tier 1 Before Tier 2

When evaluating a vital's status, tier 1 (check-in cadence) must
always be checked before tier 2 (metric threshold). Tier 2 alerts are
meaningless when tier 1 is breached — a stale metric is not a metric.

This matches SRE practice: liveness probes are evaluated before
service-level objectives. If a service isn't responding, the alert is
"service down," not "service slow."

Implies: the picker surface prioritizes tier-1 breaches above tier-2
breaches, regardless of how dramatic the tier-2 number might be. Also
implies: tier-2 SLOs can be deferred for any given vital until tier 1
is reliably healthy, supporting incremental rollout.
