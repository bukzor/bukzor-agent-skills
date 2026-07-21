---
why:
  - ../020-goals.kb/session-continuity.md
  - ../020-goals.kb/write-economy.md
  - ../020-goals.kb/mechanism-over-exhortation.md
status: proposal
---

# Wake Conditions Are Noticed

Every recorded wake condition — a task's deferral, a future-work
`trigger:`, a delete-when clause, a recurring review — is evaluated
at named junctures, and a condition that has become true surfaces
without anyone deciding to go look: mechanically where the condition
is decidable, as an enumerated listing for cheap judgment where it
is not. Surfacing claims attention only; disposition stays with the
agent or operator.

This is the staleness half of the mission's attention job, and the
property that keeps deferral trustworthy: work is deferred instead
of hoarded in the working set only while waking is guaranteed
(`../040-design.kb/class-task.md`). "Read the layer periodically" is
the exhortation this replaces.

The requirement binds existence, not frequency: junctures must be
named and evaluation complete, while every cadence and threshold is
instance data — the core and classes ship no policy values.

Checkable: for any decidable condition true at a juncture, that
juncture surfaced it — a sleeping fired trigger is an audit failure,
not a shrug; judgment conditions appear in the juncture's enumerated
listing; and a grep of core and classes for hardcoded cadence or
threshold values comes back empty.

The evaluating mechanism is the trigger subsystem's sweep
(`../../llm-triggers/design.kb/040-design.kb/sweep.md`), per
`../040-design.kb/delivery-boundary.md`; the needs it must satisfice
are inventoried in `../../llm-triggers/design.kb/use-cases.kb/`.
