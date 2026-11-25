---
managed-by: Skill(llm-subtask)
status: open
blocked-by:
  - 2026-11-25-000-apply-skill-kb-layout-migration.md
required-reading:
  - CLAUDE.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/quality-passes-run-at-occasions.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/each-skill-keeps-passes-occasions-and-a-sweep.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/quality-pass-occasions-form-a-ladder.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/every-ledger-is-swept-and-smoothed.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/descriptions-are-triggers.md
  - ../../../CLAUDE.md
  - ../../../llm-kb/skill.kb/quality-passes.md
  - ../../../llm-kb/skill.kb/procedures.kb/run-quality-passes.md
  - ../../../llm-kb/skill.kb/must-read.kb/
  - ../../../llm-claims-kb/SKILL.md
  - ../../../llm-claims-kb/skill.kb/quality-passes.kb/
---

# `llm-claims-kb`: pass occasions, the sweep, and the index

**Parent:** <https:../2026-11-25-000-Quality-passes-for-claim-ledgers.md> (wave
2)

## Problem Statement

`llm-claims-kb` has quality passes but nothing runs them. Give it what
`llm-kb` already has (`LAYOUT`), so that an agent editing a ledger in a fresh
session reaches the passes without being told:

- `skill.kb/must-read.kb/` entries for the `OCCASION_LADDER` occasions that
  belong to this skill -- while writing a claim, after an edit, before a
  commit -- each pointing at the passes due then. Leave out consolidation: it
  is a project's occasion, and wave 5 gives it an entry. Leave out
  `stale-when:` too: how it is evaluated is an open question in the plan.
  A while-writing lens that `Skill(llm-claims)`'s own bank already carries
  stays there: point at it, don't restate it.
- `skill.kb/procedures.kb/run-quality-passes.md`, a tiered sweep modelled on
  `llm-kb`'s. It runs `llm-kb`'s sweep first and cites it, then this skill's
  passes and scans (`llm-claims-kb-graph`, `-mentions`, `-ownership
  --trespass`, schema validation). Run the scans from the project root:
  inside a ledger, `--trespass` reports "0 stipulations", which a past session
  mistook for a broken tool. Smoothing is periodic, not a per-commit tier.
- `skill.kb/quality-passes.md`, the index, as `llm-kb`'s is. It lists
  `quality-passes.kb/smoothing.md`, which sibling unit 002 is writing now; the
  link may dangle until it lands.
- `SKILL.md`: the bootstrap that installs the bank (`llm-kb`'s `IMPERATIVE`
  block is the precedent), and the "before committing a batch of claims"
  sentence pointed at the sweep (`FROM_NOW_ON`'s first half). Its smoothing
  half is wave 5's. The `description:` is a trigger (`descriptions-are-triggers.md`):
  change it only if an occasion now needs it, and say why in Decisions.
- `skill.kb/CLAUDE.md`: what each collection under it holds.

Drop the `todo:` from `LAYOUT` only if `llm-claims-kb` was the last skill it
waited on. It wasn't: `llm-design-kb` and `llm-claims` are wave 4.

**Scope (only these files):** `llm-claims-kb/SKILL.md`,
`llm-claims-kb/skill.kb/CLAUDE.md`, `llm-claims-kb/skill.kb/quality-passes.md`,
`llm-claims-kb/skill.kb/must-read.kb/**`,
`llm-claims-kb/skill.kb/procedures.kb/**`. Not
`llm-claims-kb/skill.kb/quality-passes.kb/` (unit 002's).

## Steps

## Decisions

## Open Questions

## Final report
