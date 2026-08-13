---
why:
  - counter-tech-revenue-bias
trigger: When visible-debt counters alone stop being enough — i.e., operator is still missing time-sensitive customer signals despite the dashboard.
---

# Perishables via External Polling

Revenue and customer signals from external sources (email, Stripe,
Linear, calendar) are polled by Lambda jobs and surfaced as
**interrupts** to the picker — they preempt the active list rather
than waiting for the next session-start.

The cash-floor bucket gets a separate channel that *blocks*
deep-work picks when breached.

Cloud-required (only AWS can poll inbox/APIs while the laptop is
off and reach the operator via push). First cloud spend; expected
to be single-digit dollars/month.

Deferred because: the visible-debt counter on the revenue vital is
expected to handle ~80% of the bias problem without external
polling. Add this when the remaining 20% has identifiable cost.
