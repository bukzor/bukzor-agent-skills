---
label: GUARD_SCHEDULE
standing: open
why:
  - what-roots-does-a-guard-run-over.md
---

# Do Guards Run on a Schedule?

Two migrations declare `kind: recurring`, which
`migrations.kb/CLAUDE.md` defines as "never one-shot-finishes;
`validate.sh` runs forever to flag drift":

- `2026-05-15-000-schema-propagation-from-canonical.md` (verified)
- `2026-05-26-003-bullet-must-be-bracketed.md` (complete)

Neither has anything that runs it. "Runs forever" is a status they
carry, not a thing that happens -- both were last executed by hand, by
an agent who happened to read the entry.

A guard is only a guard if something fires it. The open question is
what: a commit hook (fires often, on one repo, and blocks the commit),
a timer (fires on all repos, and reports to nobody), or a session-start
check (fires when an agent is present to act on it, which is the only
time a finding can be repaired).
