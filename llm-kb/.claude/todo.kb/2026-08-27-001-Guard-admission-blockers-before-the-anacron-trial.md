---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-08-21-000-ref-rollout-beyond-todo-ideas.md
cost-benefit-sweh:
  timebox:
    "@value": 2.0
    rationale: |
      Three defects and a triage pass. The 1191-finding baseline is the
      unbounded one and is explicitly a sampling job, not a sweep: past 2h
      the answer is "this guard needs a narrower question", which is
      itself the finding.
    confidence: unsure
  benefit-2w:
    "@value": 1.5
    rationale: |
      Nine of ten current findings are one guard bug. Fixing it turns the
      report from noise into signal, which is the precondition for the
      anacron trial being worth running at all.
    confidence: confident
  cost-of-delay-2w:
    "@value": 1.0
    rationale: |
      The trial starts producing daily reports whether or not this lands.
      A report that is nine-tenths false on day one is how a scheduled
      guard gets ignored permanently.
    confidence: confident
---

# Guard Admission Blockers Before the Anacron Trial

**Priority:** high -- gates `2026-08-27-000`'s schedule step
**Complexity:** medium
**Context:** ruling 4's admission rule, `2026-08-23-005-*.kb/2026-08-23-003-*.md`

## Problem Statement

The owner adopted the daily anacron schedule as a trial. Its admission
rule: a `kind: recurring` guard joins the schedule only when its baseline
is zero or near-zero. Neither guard qualifies today. Scheduling anyway
teaches the owner that scheduled guard reports are noise, after which both
guards are dead -- and a dead guard lies exactly as `kind: recurring`
promises it will not.

## Current Situation

Measured 2026-08-27, after the unreverted 2026-08-22 working-tree damage
in the `dotfiles` clone was reverted: the schema guard reports **10**
(down from 17).

| finding | count | what it is |
| --- | --- | --- |
| `NO-REF <tree>/claims.jsonschema.yaml` | 9 | a guard defect |
| `MISSING llm-claims-kb/.claude/ideas.jsonschema.yaml` | 1 | a real gap |

The nine are one bug wearing nine hats. Category `claims` has two rival
canonicals: `llm-discourse-graph/jsonschema/claims` (enrolled) and
`llm-claims-kb/jsonschema/claim` (singular, so the table derived by
globbing `<skill>/jsonschema/` never maps `claims` to it). Every correct
stub onto the singular canonical is reported as drift.

The bullet guard (`2026-05-26-003-bullet-must-be-bracketed`) reports
**1191**. Its own entry says it produces candidates for human triage and
refuses to mechanize the judgment, which is honest and also why it cannot
be scheduled as-is.

## Implementation Steps

- [ ] Rule the `claims`/`claim` rivalry: one canonical for the category,
      an alias in the derived table, or two categories that are genuinely
      different objects. Whichever it is, the derivation must express it --
      re-introducing a hand-maintained table is the failure the glob
      replaced.
- [ ] Close `MISSING llm-claims-kb/.claude/ideas.jsonschema.yaml`.
- [ ] Triage the bullet guard's 1191 baseline: sample, classify, and
      decide what the guard should actually ask. Do not sweep 1191 files.
- [ ] Fix the `ERROR(1)` crash. An unreadable directory anywhere under the
      roots makes `find` exit 1; `report="$(collections ... | xargs ...)"`
      inherits it under `pipefail`; `errexit` fires the `ERR` trap. The
      guard then prints nothing and exits 1 -- indistinguishable at a
      glance from "found findings", the worst failure shape a recurring
      guard has. Reproduced at root `~` (42 permission-denied lines from
      container overlay dirs); latent at the current roots.
- [ ] Prune the stale `dotfiles` clone at `~/repo/github.com/bukzor/dotfiles`
      the way `*--replication-run` clones are pruned, or prefer the live
      tree. Note while there: the `-name .git` prune misses
      `~/.local/state/git-localhost-store` git dirs, which are not named
      `.git`.

## Success Criteria

- [ ] Schema guard baseline is 0, or every survivor carries a written
      ruling in its own `$comment`
- [ ] The bullet guard has either a near-zero baseline or a narrower
      question, and the decision is written down
