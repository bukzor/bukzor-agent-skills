---
why:
  - ../010-mission.md
trigger: A store designed under the one-operator assumption is about to be shared with a second person, or a second operator's agent starts reading or writing an instance — sweep for operator-private content and settle identity/authority conventions before the share, not after.
---

# Multi-Operator

The mission stipulates one operator; multi-operator is expected
eventually if the system succeeds, and deliberately unbuilt until
then (operator, 2026-07-19). Ratified as a two-way door on the
design plane: scope is filesystem position, so a second operator is
more instances, not a redesign; ratification generalizes from "the
operator" to named approvers without touching the marker grammar;
author identity rides on git until an `author:` field earns schema
space; and per-operator orderings are already the shape of "a
working set is present where an ordering has a consumer"
(`../040-design.kb/class-task.md`) — collections are one-file-per-item
and multi-writer-friendly, the single-writer syntheses per-instance
already.

The one irreversibility is on the data plane, hence the trigger
above: one-operator habits place personal content freely (sessions
pointing into project stores, private context in working sets), and
a shared repo's git history cannot unshare it. The door that can
close is not the design — it is what got committed before the first
share.
