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

- [ ] Wave 1, mechanical: apply
      `llm-kb/migrations.kb/2026-11-25-001-skill-kb-quality-passes-and-reference-kb.md`,
      with its `migrate.sh` and `validate.sh`.
  - [ ] [000-apply-skill-kb-layout-migration](2026-11-25-000-Quality-passes-for-claim-ledgers.kb/2026-11-25-000-apply-skill-kb-layout-migration.md)
- [ ] Wave 2, `llm-claims-kb`: `skill.kb/must-read.kb/` entries for the
      `OCCASION_LADDER` occasions, each pointing at its passes; a tiered sweep,
      `skill.kb/procedures.kb/run-quality-passes.md`, that runs `llm-kb`'s
      sweep first and cites it; `quality-passes.md` as the index.
      Runs beside wave 3.
  - [ ] [001-llm-claims-kb-occasions-sweep-and-index](2026-11-25-000-Quality-passes-for-claim-ledgers.kb/2026-11-25-001-llm-claims-kb-occasions-sweep-and-index.md)
- [ ] Wave 3: write `skill.kb/quality-passes.kb/smoothing.md` (`SMOOTHING`).
      Each node is walked against: its rung's question (`llm-design-kb`'s
      each-rung lens), its `why:` (`REACH`, `corollaries`), its siblings
      (`one-home`), the rulings it quotes (`ruling-fidelity`), and
      confinement. Run the scans from the project root: inside the ledger,
      `llm-claims-kb-ownership --trespass` reports "0 stipulations", which
      59b55f01 mistook for a broken tool and replaced with a hand check that
      missed 6 trespasses.
  - [ ] [002-smoothing-pass](2026-11-25-000-Quality-passes-for-claim-ledgers.kb/2026-11-25-002-smoothing-pass.md)
- [ ] Wave 4: the same layout in `llm-design-kb` (its folded passes, a sweep
      that runs `llm-claims-kb`'s first) and in `llm-claims` for chat ledgers.
- [ ] Wave 5: deliver `FROM_NOW_ON` -- `SKILL.md` of `llm-claims-kb` names the
      sweep before a batch of claims is committed and smoothing at
      consolidation; drop the fleet claims' `todo:` as each lands.
      Consolidation is a project's occasion, not a skill's: give
      `llm-claims-kb` a `must-read.kb/when/` entry for a consolidation
      session, and have each project's consolidation policy name smoothing
      by link (my-own-shadertoy: `technical-policy.kb/consolidation-sessions.md`).
- [ ] Wave 6, receipt: run the sweep and smoothing on
      `my-own-shadertoy/docs/dev/claims.kb/`; record what they found.
      The run is blind: its brief links neither this plan nor 59b55f01's
      findings, and the coordinator checks it against Success Criteria.

## Open Questions

- [ ] A scan for `REACH` (every claim reaches the mission): a lint in
      `llm-claims-kb-graph`, or a pass only?
- [ ] Does each `stale-when:` get evaluated by the periodic sweep, and how?

## Success Criteria

- [ ] `migrations.kb/2026-11-25-001-...` is `verified`.
- [ ] Editing a ledger in a fresh session fires the passes without being told.
- [ ] The receipt run finds the 6 trespasses 59b55f01 left in my-own-shadertoy
      (`llm-claims-kb-ownership --trespass` from its root, 2026-11-25), and no
      fault 59b55f01 had fixed by hand.
