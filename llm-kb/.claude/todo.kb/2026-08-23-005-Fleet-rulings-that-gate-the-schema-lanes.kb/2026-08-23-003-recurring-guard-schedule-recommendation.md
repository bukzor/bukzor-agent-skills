# Recommendation (2026-08-23): the schema guard gets a daily anacron run that *files* a report; nothing blocks, and the bullet guard is not admitted until its baseline is clean

Two questions hide inside "do the recurring guards get a schedule?" --
*when does it run* and *where does the finding land*. The first is
already solved by machinery on this machine. The second produced the
six weeks of silence, and a timer alone does not fix it:
`logrotate-cron` writes to `~/.local/state/cron/*.log`, which nobody
reads.

## The guards, enumerated

Two `kind: recurring` migrations exist fleet-wide. `migrations.kb/` is a
singleton -- the only one under `~/repo`, `~/claude`, `~/.claude` is
`llm-kb/migrations.kb` (plus its replication clone, which is pruned by
construction). So "fleet policy" governs exactly two scripts today.

| guard | writes? | roots | runtime (warm) | findings today |
| --- | --- | --- | --- | --- |
| `2026-05-15-000-schema-propagation-from-canonical/validate.sh` | no | `~/repo ~/claude ~/.claude` | 11.3s, 11.5s, 11.8s, 13.3s | 15 stdout, 8 ruled-on-stderr |
| `2026-05-26-003-bullet-must-be-bracketed/validate.sh` | no | `claude-open-tasks-list` | 9.2s | **1191** |

Scoped to a single repo the schema guard costs 1.6s (this repo, 26
collections) and 0.7s (`~/claude/meta-reasoning`, 6). That number matters
only for the declined alternative below.

The 1191 is the ruling's second half. That guard is honest -- its own
entry says it reports candidates for human triage and refuses to
mechanize the judgment -- but a scheduled report of 1191 lines is not a
signal, it is a wall. Putting both guards on one schedule buries the
15-line one inside the 1191-line one.

## Today's 15 findings are not 15 drift events

The parent brief's evidence does not survive re-derivation intact.

| finding class | count | what it actually is |
| --- | --- | --- |
| `claims.jsonschema.yaml` stubbing `skill://llm-claims-kb/jsonschema/claim.jsonschema.yaml` | 8 | correct stubs. Category `claims` has two rival canonicals: `llm-discourse-graph/jsonschema/claims` (enrolled) and `llm-claims-kb/jsonschema/claim` (singular, so the derived table never maps `claims` to it). A guard defect, not drift |
| `dotfiles` schemas replaced by full copies | 7 | uncommitted working-tree edits in `~/repo/github.com/bukzor/dotfiles` (`git status` shows nine `M` plus two untracked), all stamped 2026-08-22 14:03 -- the schema blast, whose revert never reached this clone. `git diff` shows a committed `$ref` stub overwritten by a hand-rolled full copy. No commit to blame because it was never committed |

And the brief's "six weeks of ordinary drift" reads ten independent
lapses into what the migration entry itself records as six-of-ten being
**one** un-fetched clone of `dotfiles` on `orphan-recovery`. One stale
checkout, counted ten times, is weaker evidence for a schedule than the
brief implies. The schedule is still right -- but on the argument below,
not that one.

Re-measured 2026-08-27, four days on: **17** findings, then **10** once the
seven uncommitted dotfiles edits were reverted. The two new ones are a fresh
`claims.jsonschema.yaml` (the table defect again) and a genuine
`MISSING llm-claims-kb/.claude/ideas.jsonschema.yaml`. Half a finding a day,
arriving in repos nobody was auditing, is the rate a daily timer is priced
against -- and it is the first drift measurement this migration has taken
twice.

## Which trigger correlates with the drift

161 in-scope collections live in 27 distinct git roots. This repo holds
26 of them -- 16%. A pre-commit hook in `llm-kb` fires on changes to the
canonical, which is the one event that *cannot* produce a `$ref` finding:
editing a canonical propagates automatically, by design. It is
anti-correlated with the drift.

Nothing else is correlated either. Drift arrives when an agent creates a
`*.kb/` in any of 27 repos, hand-rolls a schema, or -- as today --
overwrites a stub and never commits. Only 5 of those 27 roots carry a
`.pre-commit-config.yaml` at all. The one variable covering all 27
uniformly is elapsed time, and the fleet's activity rate makes it a fair
proxy: 129 session transcripts in the last week, 42 in the last 36
hours.

## The machinery already exists

`~/.config/anacron/anacrontab` is tracked in dotfiles, runs two daily
jobs today, and is kicked `@reboot` and `@hourly` from
`~/.config/cron/crontab`, whose own comment reads "Prefer anacron for
periodic jobs (daily, weekly) -- it handles missed runs." On a Crostini
VM that is off more than it is on, "handles missed runs" is the whole
argument against a systemd timer or a raw cron line. There are zero
systemd user timers.

So: one anacrontab row, period 1, in the shape of the two already there.
11 seconds a day.

## What it does with a finding: file, never block

Never block, on direct local evidence: `~/.claude/settings.json` carries
a `"//hooks-disabled"` key holding two `PreToolUse` hooks the owner
already turned off wholesale. A guard that blocks joins them.

Filing needs an arrival mechanism, or this recommendation is the status
quo with extra steps. The cheapest one that touches no new machinery:
the job writes its report to a fixed path, and `/session-start` reads
that path the way it already reads `.claude/todo.md`. That splits cost
from attention correctly -- the 11 seconds run overnight, and the finding
appears in front of an agent who can repair it, at the cost of `cat` on a
15-line file. A `SessionStart` hook already exists in `settings.json`
(`binpatch.py`), so the mechanism is proven; but 42 session starts in 36
hours times 11 seconds is the wrong place to *run* the guard.

## Admission rule (the general policy the ruling should state)

A `kind: recurring` guard joins the schedule only when its baseline is
zero or near-zero. The schema guard qualifies after the `claims`/`claim`
table defect is fixed and the 7 uncommitted dotfiles edits are resolved.
The bullet guard, at 1191, does not, and putting it on the schedule
anyway would teach the owner that scheduled guard reports are noise --
after which both guards are dead, and the dead one lies exactly as the
brief says. Its baseline needs a triage pass first; that is a todo item,
not a schedule.

## Declined: a pre-commit hook in each consumer repo

The steelman rests on a measured number. Scoped to one repo the guard
costs 0.7--1.6s, comfortably inside a pre-commit budget; a hook fires at
the instant drift is introduced, names the author, and solves "reports to
nobody" completely, because the report is a blocked commit in front of
the person who caused it. Time-based checking is the worse detector by
that standard: it finds drift a day late, in a repo the owner may not be
working in.

It loses on distribution, not on merit. Nothing installs or updates a
hook across 27 roots; 22 have no pre-commit config to add it to; the
guard would be vendored into each, which is this migration's own
propagation problem applied recursively. And today's failure is
uncommitted -- seven modified files no pre-commit hook has seen or will
see until someone commits them.

The narrower variant -- a pre-commit hook in `llm-kb` only -- is declined
outright: it fires on the 16% of the surface that is anti-correlated with
the finding.

Also declined: running the guard *inside* `/session-end` or
`/session-start`. It puts an 11-second fleet scan on the interactive
path 30-plus times a day to detect something that changes on a scale of
days, and a step in a prose command file is skippable in a way an
anacrontab row is not.

## Verdict

**Adopt, as a trial** (user, 2026-08-27: "i'm less certain.. willing to
try it").

The schema guard gets one `period 1` anacrontab row; it files a report to
a fixed path and blocks nothing; session start reads that path. The
bullet guard is not admitted until its 1191-line baseline has had a
triage pass.

The trial needs a stopping condition, or it becomes the six weeks of
silence with more moving parts -- agent's call, recorded here, veto by
editing this file. **Pull it if a nonempty report survives two
consecutive weeks of session starts unrepaired.** That is the same
failure this ruling diagnosed, and the second time it would be
self-inflicted. Two supporting facts already in hand: the guard's
admission rule wants the `claims`/`claim` table defect fixed first, or
nine of ten findings on day one are the guard's own bug; and the drift
rate is now measured twice, at half a finding a day.
