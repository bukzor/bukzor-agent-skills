---
managed-by: Skill(llm-subtask)
status: done
blocked-by:
  - 2026-11-25-001-llm-claims-kb-occasions-sweep-and-index.md
required-reading:
  - CLAUDE.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/quality-passes-run-at-occasions.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/each-skill-keeps-passes-occasions-and-a-sweep.md
  - ../../../docs/dev/claims.kb/design.claims.kb/authorship.kb/quality-pass-occasions-form-a-ladder.md
  - ../../../llm-design-kb/SKILL.md
  - ../../../llm-design-kb/skill.kb/
  - ../../../llm-claims-kb/skill.kb/quality-passes.md
  - ../../../llm-claims-kb/skill.kb/procedures.kb/run-quality-passes.md
  - ../../../llm-claims-kb/skill.kb/must-read.kb/
  - 2026-11-25-001-llm-claims-kb-occasions-sweep-and-index.md
---

# `llm-design-kb`: its folded passes, the sweep, and the index

**Parent:** <https:../2026-11-25-000-Quality-passes-for-claim-ledgers.md> (wave
4)

## Problem Statement

Wave 1 renamed `llm-design-kb/skill.kb/principles.kb/` to `quality-passes.kb/`
and changed nothing else. Finish the job under `LAYOUT`, the way unit 001 did
it for `llm-claims-kb`. Its handoff file is required reading for its
Decisions, and its files are the precedent.

- Each of the six entries becomes a quality pass (`PASS_AT_OCCASION`): what it
  improves, how to walk the work, what a finding means, how it is repaired. It
  names no occasion; the bank does. Recast by cutting and reshaping, not by
  adding. An entry that is not a pass at all (a decision heuristic with no work
  to walk) belongs elsewhere: say where in Open Questions and leave it in
  place.
- `quality-passes.kb/CLAUDE.md`: say what a pass is here.
- `skill.kb/procedures.kb/run-quality-passes.md`: a tiered sweep that runs
  `llm-claims-kb`'s sweep first and cites it, then this skill's passes.
- `skill.kb/quality-passes.md`, the index.
- `skill.kb/must-read.kb/`: the existing
  `when/deciding-what-a-design-claim-should-say.md` keeps pointing at the
  passes due while writing. Add the ladder's other occasions that this skill
  owns, mirroring unit 001's set. Leave out consolidation and `stale-when:`:
  wave 5 and the plan's open questions own those.
- `SKILL.md`: mentions of the passes and of the sweep.

Not here: a `REACH` pass or scan. That awaits a ruling (the plan's Open
Questions).

**Scope (only these files):** `llm-design-kb/SKILL.md`,
`llm-design-kb/skill.kb/**`.

## Steps

- [x] Recast the six entries as passes, or name the non-passes' home
- [x] `quality-passes.kb/CLAUDE.md`: what a pass is here
- [x] `procedures.kb/run-quality-passes.md`, the tiered sweep
- [x] `skill.kb/quality-passes.md`, the index
- [x] `must-read.kb/`: while-writing entry updated; after-edit, before-commit added
- [x] `SKILL.md`: passes and sweep named
- [x] validate, commit

## Decisions

- **Three passes, three decision lenses.** `each-rung-...`,
  `state-properties-...`, `regression-proof-...` walk the record and were
  reshaped (rule, walk, finding, repair). `evaluate-uses-independently`,
  `shared-shape-separate-semantics`, `test-the-residue-not-the-bundle` judge a
  decision, not a record: left in place, unchanged (Open Questions).
- **Filenames kept.** They are not quality nouns, but out-of-scope readers
  cite them (`llm-claims-kb/.../smoothing.md` `[EACH_RUNG]`,
  `design-next.kb/040-design.kb/class-record.md`).
- `regression-proof`: dropped its pointer to an "Alternatives Considered"
  rule this skill no longer has; added that a `verdict:` and its ground are
  not narrative, so the pass does not strip declined options.
- **Sweep has no Tier 1 or 3 of its own.** Every blocking scan
  (graph, mentions, ownership) and confinement is `llm-claims-kb`'s; restating
  them would be a second copy.
- **Triggers mirror 001:** `after/editing-a-design-record.md` (points at
  `llm-claims-kb`'s after-edit entry first), `before/committing-design-claims.md`
  (stands in for `llm-claims-kb`'s before-commit, since the sweep runs it).
  The while-writing entry splits passes from decision lenses and points at
  `llm-claims-kb`'s `before/writing-a-claim-file.md`.
- `SKILL.md`: Maintenance's graph and confinement bullets cut to one bullet
  naming the sweep (their content lives in `llm-claims-kb`'s sweep and
  `confinement.md`); Persist ends "after the sweep"; the confinement paragraph
  names the pass by path. `description:` unchanged, as in 001.

## Open Questions

- [ ] Home of the three decision lenses: `llm-design-kb/skill.kb/reference.kb/`
      (`REFERENCE_KB`: loaded on demand by the skill's users), still reached
      from the while-writing trigger. Not the fleet ledger's `principles.kb/`:
      that governs this fleet, these serve consumers' records.
- [ ] `llm-design-kb/CLAUDE.md` (out of scope) is stale: it lists
      `skill.kb/must-read.kb/when/` only, calls the passes "lenses" with one
      indexing trigger, and omits `procedures.kb/` and `quality-passes.md`.
- [ ] Its Dogfooding rule asks a new rule to be stated as a claim in
      `llm-design-kb/docs/dev/claims.kb/` (out of scope); the sweep and
      triggers have no claim there yet.

## Final report

Checks on `llm-design-kb`: `llm.kb-validate` 41 files 0 errors;
`llm.kb-validate-links` 44 links 0 broken; `llm-triggers-lint` 0 errors.
No deviation from scope.

- Passes: `llm-design-kb/skill.kb/quality-passes.kb/` (+ `CLAUDE.md`)
- Sweep: `llm-design-kb/skill.kb/procedures.kb/run-quality-passes.md`
- Index: `llm-design-kb/skill.kb/quality-passes.md`
- Occasions: `llm-design-kb/skill.kb/must-read.kb/{when/deciding-what-a-design-claim-should-say,after/editing-a-design-record,before/committing-design-claims}.md`
- `llm-design-kb/SKILL.md`
