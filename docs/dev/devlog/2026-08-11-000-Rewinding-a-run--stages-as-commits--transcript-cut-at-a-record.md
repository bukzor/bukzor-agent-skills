# Devlog: 2026-08-11 — Rewinding a run: stages as commits, transcript cut at a record

## Focus

The replication run's eighth turn (080, the critique) was answered
against a ledger whose schema symlink dangled, so the audit spent
itself on the rot. The first repair attempt was not a repair: the
symlink was fixed and the turn re-sent to the same subject, which
answered with a revision of its own discarded audit — its reply opened
with a section headed "Reversals from my discarded reply". Re-asking
is not rewinding. This session rewinds it properly.

## What "properly" turned out to require

Three separate rewinds, only one of which existed:

1. **The record.** Nothing was committed while the run ran, so the run
   had no middle to return to. Fixed by reconstructing the stages from
   the subject's transcript into `strata.replication.run.kb/`, one
   commit per stage on branch `strata-replication-run`, based at the
   sealed environment the subject was given. Author dates are the
   run's own clock. A checkout is now a point in the experiment.
2. **The environment.** The distraction — the dangling
   `strata.claims.kb/jsonschema/claim.jsonschema.yaml` — removed as
   its own commit, after stage 070 where it belongs in the timeline,
   tagged `run/pre-080`.
3. **The subject.** `/rewind` cuts only at your own prompts on the one
   chain resume loaded, and a subagent transcript is not offered at
   all: it lives in `projects/<slug>/<session>/subagents/` with every
   record marked `isSidechain`. Two flags closed the gap
   (`bukzor-tools` e022df8): `--at` cuts at a chosen record instead of
   tracing forward to the branch tip, and `--as-session CWD` strips the
   sidechain marks and re-homes the branch. The subject now exists as
   session `0476a1a8-b186-4988-8deb-83853c353acb` in the worktree,
   ending at its 070 reply, 15 records, resumable.

## Removed, not amended

Post-distraction artifacts are out of the tree, not annotated in
place: the redo's devlog, the superseding-defeat-list note it added to
the run's devlog, and the operator note it added to `080-defeats.md`.
The run devlog is rewritten to seven stages and says why the eighth is
absent; the audit findings themselves live only in the transcript,
cited by line. An audit written against a repaired ledger must not be
seeded with the one written against a broken one.

## Procedure changes

`strata.replication.md` gains two sections. **The environment**: run
the subject in a dedicated worktree and seal it with a bland `wip`
commit — a dirty `git status` lists the answer's own paths, so the
seal is what makes the blind survive a command the subject has every
reason to run — then repair mechanical rot before the run. **Rewinding
a run**: commit each stage as it lands; cut the transcript rather than
re-asking. `Skill(claude-code-archeology)` gains the same in general
form, plus the corrected fact about where subagent transcripts live.

One caveat recorded in both places: a promoted subagent session comes
back without its agent definition, so its model and effort must be
restored by hand.

## Open Questions

- 080 itself, from the promoted session (todo.md carries the recipe).
- Whether `strata.replication.run.kb/` merges to main when the run
  finishes, or stays on the run branch as the time machine. The blind
  list already covers it either way (`docs/dev/strata.*`).
- `claude-search`/`claude-inventory` still glob `projects/*/*.jsonl`
  and so cannot see subagent transcripts at all — the same gap
  `--as-session` works around one file at a time.

## References

- `2026-08-10-001-*seven-turns*.md` — the run, rewritten.
- Branch `strata-replication-run`, tag `run/pre-080`;
  `strata.replication.run.kb/CLAUDE.md` for the per-stage discipline.
- `bukzor-tools` e022df8 — `--at`, `--as-session`.
