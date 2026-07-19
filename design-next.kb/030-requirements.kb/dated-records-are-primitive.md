---
why:
  - ../020-goals.kb/session-continuity.md
  - ../020-goals.kb/single-source-improvement.md
---

# Dated Records Are Primitive

Temporal identity — `YYYY-MM-DD-NNN-title` naming, newest-wins
conflict resolution, append-mostly lifecycle — is defined once at
spec level, and every dated collection (tasks, incidents, migrations)
is an instance of it.

Checkable: one definition of the dated-record convention exists;
generators for every dated class share one implementation. V1
reinvented this six times (adr, devlog, todo.kb, ideas.kb,
migrations.kb, case-studies.kb) — devlog itself does not carry
forward into v2 (see `class-record.md`), but the duplication it
exemplified is still the motivating count.
