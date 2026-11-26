---
managed-by: Skill(llm-subtask)
status: open
---

# Quality passes for claim ledgers

**Priority:** high -- the passes run in the fresh session make every later
ledger edit cheaper.
**Complexity:** medium -- mostly mechanical moves, plus three new documents.
**Context:** my-own-shadertoy session 59b55f01 (2026-11-23..25). Its smoothing
passes and audits found faults nothing persisted would have caught. The rules
they produced are filed (fleet `ONE_HOME`, `DERIVED_RECORD`, `SCOPE_KEPT`;
`llm-design-kb` `REACH`); the layout to keep and run them is ruled in the
fleet ledger's `authorship.kb/` (`PASS_AT_OCCASION`, `PASS_NAME`, `LAYOUT`,
`SMOOTHING`, `SKILL_KB`, `REFERENCE_KB`, `OCCASION_LADDER`, `FROM_NOW_ON`).
Burn down with `/subagent-handoffs`.

## Problem Statement

Claim ledgers have quality passes (`llm-claims-kb/skill.kb/self-audit.kb/`)
but nothing runs them: no trigger, no sweep, no index. The smoothing walk that
found most of 59b55f01's faults is written nowhere. Pass-shaped content sits
under three names in three skills.

## Implementation Steps

- [x] Wave 1, mechanical: apply
      `llm-kb/migrations.kb/2026-11-25-001-skill-kb-quality-passes-and-reference-kb.md`,
      with its `migrate.sh` and `validate.sh`.
  - [x] [000-apply-skill-kb-layout-migration](2026-11-25-000-Quality-passes-for-claim-ledgers.kb/2026-11-25-000-apply-skill-kb-layout-migration.md)
- [x] Wave 2, `llm-claims-kb`: `skill.kb/must-read.kb/` entries for the
      `OCCASION_LADDER` occasions, each pointing at its passes; a tiered sweep,
      `skill.kb/procedures.kb/run-quality-passes.md`, that runs `llm-kb`'s
      sweep first and cites it; `quality-passes.md` as the index.
      Runs beside wave 3.
  - [x] [001-llm-claims-kb-occasions-sweep-and-index](2026-11-25-000-Quality-passes-for-claim-ledgers.kb/2026-11-25-001-llm-claims-kb-occasions-sweep-and-index.md)
- [x] Wave 3: write `skill.kb/quality-passes.kb/smoothing.md` (`SMOOTHING`).
      Each node is walked against: its rung's question (`llm-design-kb`'s
      each-rung lens), its `why:` (`REACH`, `corollaries`), its siblings
      (`one-home`), the rulings it quotes (`ruling-fidelity`), and
      confinement. Run the scans from the project root: inside the ledger,
      `llm-claims-kb-ownership --trespass` reports "0 stipulations", which
      59b55f01 mistook for a broken tool and replaced with a hand check that
      missed 6 trespasses.
  - [x] [002-smoothing-pass](2026-11-25-000-Quality-passes-for-claim-ledgers.kb/2026-11-25-002-smoothing-pass.md)
- [x] Wave 4: the same layout in `llm-design-kb` (its folded passes, a sweep
      that runs `llm-claims-kb`'s first) and in `llm-claims` for chat ledgers.
  - [x] [003-llm-design-kb-passes-and-sweep](2026-11-25-000-Quality-passes-for-claim-ledgers.kb/2026-11-25-003-llm-design-kb-passes-and-sweep.md)
  - [x] [004-llm-claims-chat-ledger-passes](2026-11-25-000-Quality-passes-for-claim-ledgers.kb/2026-11-25-004-llm-claims-chat-ledger-passes.md)
- [x] Wave 5: deliver `FROM_NOW_ON` -- `SKILL.md` of `llm-claims-kb` names the
      sweep before a batch of claims is committed and smoothing at
      consolidation; drop the fleet claims' `todo:` as each lands.
      Consolidation is a project's occasion, not a skill's: give
      `llm-claims-kb` a `must-read.kb/when/` entry for a consolidation
      session, and have each project's consolidation policy name smoothing
      by link (my-own-shadertoy: `technical-policy.kb/consolidation-sessions.md`).
      Done by the coordinator: the `SKILL.md` sweep sentence landed in wave 2;
      the occasion is `llm-claims-kb/skill.kb/must-read.kb/when/a-session-consolidates-a-ledger.md`,
      reached through the bank `SKILL.md` installs. Not done: the project link.
      `CONSOLIDATION` is `standing: user`, so the bullet waits for bukzor.
- [x] Wave 6, receipt: run the sweep and smoothing on
      `my-own-shadertoy/docs/dev/claims.kb/`; record what they found.
      The run is blind: its brief links neither this plan nor 59b55f01's
      findings, and the coordinator checks it against Success Criteria.
      Its brief asks for the consolidation, not for the passes, so it tests
      the second criterion too.
  - [x] [005-consolidate-my-own-shadertoy-ledger](2026-11-25-000-Quality-passes-for-claim-ledgers.kb/2026-11-25-005-consolidate-my-own-shadertoy-ledger.md)
- [x] Apply the receipt's repairs, here and now (bukzor, 2026-11-25): smooth
      my-own-shadertoy's ledger to a fixpoint.
  - [x] [006-apply-the-shadertoy-ledger-repairs](2026-11-25-000-Quality-passes-for-claim-ledgers.kb/2026-11-25-006-apply-the-shadertoy-ledger-repairs.md)

## Open Questions

- [ ] `llm-design-kb/CLAUDE.md` says a bank entry "is the payload, never a
      redirect"; unit 003's `after/editing-a-design-record.md` and
      `before/committing-design-claims.md` point at the sweep, as
      `Skill(llm-must-read-kb)`'s "Composition with procedures.kb/" allows,
      and so do `llm-kb`'s and `llm-claims-kb`'s. Which rule yields?
- [ ] Move notation-level passes from `llm-claims-kb` down to `llm-claims`,
      with `llm-claims-kb` citing them: `confinement.md` (`llm-claims`'
      `SKILL.md` Theories section already condenses it: two homes) and
      `ruling-fidelity.md`, reworded without file-form terms; then
      `standing-honesty.md` cites `llm-claims` for the shared rule. Proposed
      by unit 004 (its Open Questions); a follow-up unit once ruled.
- [ ] A scan for `REACH` (every claim reaches the mission): a lint in
      `llm-claims-kb-graph`, or a pass only?
- [ ] Does each `stale-when:` get evaluated by the periodic sweep, and how?

## Success Criteria

- [x] `migrations.kb/2026-11-25-001-...` is `verified`.
- [x] Editing a ledger in a fresh session fires the passes without being told.
      Receipt 005: `llm-claims-kb`'s description, then its bank's
      `when/a-session-consolidates-a-ledger.md`, then smoothing, then the sweep.
- [ ] The receipt run finds the 6 trespasses 59b55f01 left in my-own-shadertoy
      (`llm-claims-kb-ownership --trespass` from its root, 2026-11-25), and no
      fault 59b55f01 had fixed by hand.
      Partly met (coordinator's grading, 2026-11-25). The receipt ran the scan
      and saw all 6. It repaired 4 (findings 5c, 6, 7, 8), rightly dismissed
      `pass` in `requirements.kb` as the verb, and gave no disposition to
      `milestone` in `goals.kb/bite-sized-increments.md:9`. That one sits in
      `authority.words:`, bukzor's quote, so it has no repair; the gap was the
      missing dismissal (unit 006 supplied it). None of its
      findings re-raises a fault 59b55f01 fixed; each cites current text.
