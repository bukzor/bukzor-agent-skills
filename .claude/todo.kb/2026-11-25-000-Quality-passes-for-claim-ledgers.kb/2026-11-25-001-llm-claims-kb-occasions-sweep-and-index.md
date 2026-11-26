---
managed-by: Skill(llm-subtask)
status: done
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

- [x] `skill.kb/must-read.kb/`: while-writing, after-edit, before-commit entries
- [x] `skill.kb/procedures.kb/run-quality-passes.md`, the tiered sweep
- [x] `skill.kb/quality-passes.md`, the index
- [x] `SKILL.md`: bootstrap block; the before-commit sentence names the sweep
- [x] `skill.kb/CLAUDE.md`: what each collection holds
- [x] validate, commit

## Decisions

- `description:` unchanged. Every new occasion is reached after the skill
  has loaded, and the description already fires on maintaining a ledger
  directory; no occasion needs a new trigger word.
- While-writing entry is `before/writing-a-claim-file.md`: it points at
  `Skill(llm-claims)`'s `before/writing-a-claim.md` for the body and adds
  only the frontmatter passes (corollaries, standing-honesty,
  ruling-fidelity).
- After-edit is lighter than the sweep (graph-health, ruling-fidelity,
  confinement on what was touched); before-commit is the full sweep. The
  ladder distinguishes the two rungs, so the entries do.
- Schema validation is not a separate row: `llm-kb`'s Tier 1
  `llm.kb-validate` is that check; the sweep says so instead of running it
  twice.
- Tier 1 `llm-claims-kb-ownership` blocks only on a contention the edit
  introduced: the scan is fleet-wide, and one pre-existing contention
  (outside any edit) would otherwise block every commit.
- New standing text is marked `[!DRAFT] agent-authored 2026-11-25`.

## Open Questions

- [ ] `bin/llm-claims-kb-graph docs/dev/claims.kb` (a bare container
      ledger) fails: `graph claims.kb has missing "pos" information`. On
      `docs/dev/claims.kb/design.claims.kb` it works. Tool bug, out of
      scope; the sweep's Tier 1 row will hit it on bare-container ledgers.

## Final report

`llm.kb-validate llm-claims-kb`: 13 files, 0 errors.
`llm.kb-validate-links llm-claims-kb`: 28 links, 0 broken
(`quality-passes.kb/smoothing.md` had landed, so nothing dangles).
No deviations from the brief beyond the Decisions above.

- Occasions: `llm-claims-kb/skill.kb/must-read.kb/{before/writing-a-claim-file,after/editing-a-claims-kb,before/committing-a-batch-of-claims}.md`
- Sweep: `llm-claims-kb/skill.kb/procedures.kb/run-quality-passes.md`
- Index: `llm-claims-kb/skill.kb/quality-passes.md`
- Bootstrap and before-commit sentence: `llm-claims-kb/SKILL.md`
