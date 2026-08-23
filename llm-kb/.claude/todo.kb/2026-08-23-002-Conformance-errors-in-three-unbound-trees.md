---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-08-21-000-ref-rollout-beyond-todo-ideas.md
suggested-reading:
  - ~/.claude/skills/llm-kb/migrations.kb/2026-08-21-000-schema-copies-to-ref-stubs-all-categories.md
cost-benefit-sweh:
  timebox:
    "@value": 3.0
    rationale: |
      Three trees, ~50 errors, all frontmatter-vs-schema disagreements
      that want a ruling per error class rather than per file. Past 3h
      the remainder is whichever class turned out to need a canonical
      edit, which is lane -005's business, not this one's.
    confidence: unsure
  benefit-2w:
    "@value": 1.0
    rationale: |
      These trees currently report ~50 errors, so their validator output
      is unreadable and nobody runs it. Zeroing them restores drift
      detection in three places.
    confidence: confident
  cost-of-delay-2w:
    "@value": 0.25
    rationale: |
      Static. Nothing writes to these trees regularly; the errors have
      been standing for months.
    confidence: confident
---

# Conformance errors in three trees

**Priority:** Medium. **Complexity:** Small each, but three unrelated
diagnoses.
**Context:** residual of the 2026-08-21 `$ref` rollout. Each of these is
a collection that came under validation and turned out not to conform.
None was caused by the rollout; the rollout is what made them visible.

## Three independent findings

Each is a separate tree, a separate write-set, and a separate diagnosis.
They share nothing but their cause of discovery.

### 1. `prototype.chatfs` -- 9 errors, and an open question underneath

`status: exploring|active` and `kind: investigation` fall outside the
canonical's closed enums, and `resolved:` holds a date where the
canonical says string.

The fork is real and is **not** this lane's to settle: either the enums
want widening -- which edits a canonical and so belongs to lane -005 --
or the data is wrong and gets rewritten here. Diagnose, recommend, and
hand the enum question up. Do not paper over it by widening an enum
locally, which is how a rival schema gets minted by accident.

### 2. `~/claude/ai-coding-tools-facts.d` -- ~40 errors, one cause

One schema in that tree declares
`http://json-schema.org/draft-07/schema#` **with the trailing `#`**,
which the validator rejects as an unknown dialect, and every file under
it fails as a consequence. Expect the count to collapse to near zero on
one character.

Confirm that is the whole story before declaring victory: the
`scratch.vim-work` precedent is that a schema which never resolved hides
a second, independent defect behind it. Whatever survives the fix is
real drift and wants a ruling per class.

### 3. `ideation.epistemics` -- 1 error at `background.kb/prior-art`

Left standing after that repo's 2026-08-21 pass and never diagnosed.
Note that this repo holds two *deliberate* rival schemas -- it exists in
part to remove the canonical's `status` requirement -- so check whether
this error is a third instance of that intent before treating it as
drift.

## Implementation Steps

- [ ] `ai-coding-tools-facts.d`: fix the dialect URI; re-run; triage what
      survives
- [ ] `ideation.epistemics`: diagnose the one error; rule drift or intent
- [ ] `prototype.chatfs`: classify all 9; fix the data errors; write the
      enum question up for lane -005

## Delegation

- **Sole writer of:** one tree per agent -- `~/repo/github.com/bukzor/prototype.chatfs`,
  `~/claude/ai-coding-tools-facts.d`, `~/repo/github.com/bukzor/ideation.epistemics`.
  Three-way fan-out is safe; the write-sets are disjoint.
- **Never write** a `*.jsonschema.yaml` under `*/jsonschema/` in any
  skill. Canonicals are out of scope for this lane in every direction:
  no edit, no widening, no new file. A finding that seems to require one
  is a finding to report, not to act on.
- **Never delete or rewrite** a schema file that already exists. Fix
  frontmatter; if a schema itself is wrong, say so and stop.
- **Verify with:** `llm.kb-validate <tree>` -- report the before and
  after counts, not just "fixed".

## Success Criteria

- [ ] Each tree's error count is 0, or every survivor has a written
      ruling naming it intentional
