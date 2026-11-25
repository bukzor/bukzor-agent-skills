---
managed-by: Skill(llm-subtask)
status: not-started
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
- [ ] Wave 2, `llm-claims-kb`: `skill.kb/must-read.kb/` entries for the
      `OCCASION_LADDER` occasions, each pointing at its passes; a tiered sweep,
      `skill.kb/procedures.kb/run-quality-passes.md`, that runs `llm-kb`'s
      sweep first and cites it; `quality-passes.md` as the index.
- [ ] Wave 3: write `skill.kb/quality-passes.kb/smoothing.md` (`SMOOTHING`).
- [ ] Wave 4: the same layout in `llm-design-kb` (its folded passes, a sweep
      that runs `llm-claims-kb`'s first) and in `llm-claims` for chat ledgers.
- [ ] Wave 5: deliver `FROM_NOW_ON` -- `SKILL.md` of `llm-claims-kb` names the
      sweep before a batch of claims is committed and smoothing at
      consolidation; drop the fleet claims' `todo:` as each lands.
- [ ] Wave 6, receipt: run the sweep and smoothing on
      `my-own-shadertoy/docs/dev/claims.kb/`; record what they found.

## Open Questions

- [ ] A scan for `REACH` (every claim reaches the mission): a lint in
      `llm-claims-kb-graph`, or a pass only?
- [ ] Does each `stale-when:` get evaluated by the periodic sweep, and how?

## Success Criteria

- [ ] `migrations.kb/2026-11-25-001-...` is `verified`.
- [ ] Editing a ledger in a fresh session fires the passes without being told.
- [ ] The receipt run finds no fault in my-own-shadertoy that 59b55f01 had
      fixed by hand, and any it finds are new.
