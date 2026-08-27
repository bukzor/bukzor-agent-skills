---
label: GUARD_SCHEDULE
standing: agent
why:
  - what-roots-does-a-guard-run-over.md
---

# A Guard Runs on a Timer and Arrives at Session Start

Two questions hide in "do guards run on a schedule": when does it run,
and where does the finding land. They get different answers, and
conflating them is what produced six weeks of silence -- the machine
already runs periodic jobs whose output nobody reads.

- **Fires on a timer**, not a commit hook. Drift arrives when an agent
  creates a collection in any of 27 git roots; only 5 carry a
  pre-commit config, and a hook in this repo fires on canonical edits,
  the one event that cannot produce a finding. Elapsed time is the only
  variable covering all 27.
- **Anacron, not cron or a systemd timer.** `~/.config/anacron/anacrontab`
  is tracked, already runs two daily jobs, and is kicked from
  `~/.config/cron/crontab`, whose own comment prefers it because it
  handles missed runs. This host is off more than it is on. One
  `period 1` row, 11 seconds a day.
- **Files, never blocks.** `~/.claude/settings.json` carries a
  `"//hooks-disabled"` key holding two `PreToolUse` hooks the owner
  already turned off wholesale; a blocking guard joins them.
- **Arrives at session start.** The job writes a fixed report path and
  the session-start step reads it, the way it already reads
  `.claude/todo.md`. A finding is only repairable while an agent is
  present, but 42 session starts in 36 hours is the wrong place to
  *run* an 11-second fleet scan.
- **Admitted only when its baseline is clean.** The schema guard
  reports ten, nine of them its own `claims`-vs-`claim` table defect;
  the bullet guard reports 1191. Scheduling the second
  teaches the owner that guard reports are noise, after which both are
  dead -- and a dead guard lies exactly as `kind: recurring` promises
  it will not.

The declined alternative is a pre-commit hook in each consumer repo,
and it is the better *detector*: scoped to one repo the guard costs
0.7--1.6s, it fires the instant drift is introduced, and it reports to
the person who caused it. It loses on distribution -- nothing installs
or updates a hook across 27 roots, 22 have no config to add it to, and
vendoring the guard into each is this migration's own propagation
problem applied recursively. Today's finding is also uncommitted, which
no hook would ever see.

Measurements and the full argument:
`.claude/todo.kb/2026-08-23-005-Fleet-rulings-that-gate-the-schema-lanes.kb/2026-08-23-003-recurring-guard-schedule-recommendation.md`.
