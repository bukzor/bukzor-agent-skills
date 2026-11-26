---
managed-by: Skill(llm-subtask)
status: open
blocked-by:
  - 2026-11-25-005-consolidate-my-own-shadertoy-ledger.md
required-reading:
  - CLAUDE.md
  - 2026-11-25-005-consolidate-my-own-shadertoy-ledger.md
  - ../../../llm-claims-kb/skill.kb/quality-passes.kb/smoothing.md
  - ../../../llm-claims-kb/skill.kb/quality-passes.kb/confinement.md
  - ../../../llm-claims-kb/skill.kb/quality-passes.kb/ruling-fidelity.md
  - ../../../llm-design-kb/skill.kb/quality-passes.kb/
---

# my-own-shadertoy: apply unit 005's repairs, then smooth to a fixpoint

**Parent:** <https:../2026-11-25-000-Quality-passes-for-claim-ledgers.md> (after
wave 6; the measurement is over, so the plan is open to you now)

## Problem Statement

Unit 005 reported 14 findings and edited nothing. Apply them in
my-own-shadertoy (`~/repo/github.com/bukzor.sandbox/sandbox-repo.kb/github.com/bukzor-sandbox/my-own-shadertoy`),
then finish the smoothing pass: walk the frontier until it is empty, and run
the sweep last. Read the confinement, ruling-fidelity and design-kb passes in
full this time; 005 applied them by name.

Decisions already made:

- **Finding 1:** restore the footers. Session 4025060d removed them in a WIP
  commit, and `BREADCRUMBS` is the owner's ruling, which outranks it.
- **Findings 2, 4-8, 11-13:** apply as 005 proposed, unless the full pass text
  changes your mind. Say so in Decisions.
- **Finding 3:** drop `todo:` and the spent tripwire sentence, and fix
  `after/a-milestone-lands.md`. You decide whether it moves to
  `technical-policy.kb/`.
- **Finding 9:** apply. `FIRST_INSTANCE` is `standing: user`, so the quote stays
  verbatim and the reworded body keeps every qualifier (ruling-fidelity).
- **The missed trespass:** `'milestone'` in `goals.kb/bite-sized-increments.md:9`
  (outside the quote) gets a repair like finding 6's.
- **Every scan finding gets a disposition**: repaired, dismissed with a reason,
  or put to the owner. Report them in a table.
- **Not here:** finding 10 (`NAMES_SHOW_STRUCTURE` is a ruling, and the
  coordinator will put it to bukzor), and finding 14 (`.claude/todo.md`, which
  a peer session edited today). The dev-process-design scaffold stays as it
  is.

Commit in my-own-shadertoy as you go, path-scoped, per its `CLAUDE.md`; don't
push. A peer session may commit there too: never stage a path you didn't
change.

**Scope (only these files):** in my-own-shadertoy, `docs/dev/claims.kb/**`
(except `dev-process-design.*`) and the `.claude/must-read.kb/` entries a repair
names; this handoff file.

## Steps

## Decisions

## Open Questions

## Final report
