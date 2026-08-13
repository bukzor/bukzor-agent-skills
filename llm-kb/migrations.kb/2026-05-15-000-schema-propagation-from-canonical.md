---
status: verified
kind: recurring
depends-on:
  - 2026-07-07-000-schema-copies-to-ref-stubs.md
scope: |
  Every project that authors `.claude/todo.kb/` or `.claude/ideas.kb/`
  must carry a `.claude/<category>.jsonschema.yaml` whose content
  includes `$ref: skill://llm-subtask/jsonschema/<category>.jsonschema.yaml`.

  Extension *on top of* the `$ref` is allowed (conjunction: consumers
  may add fields or narrow constraints, never loosen -- see "Policy
  updated 2026-07-07"). Mindful omission of the `$ref` is not allowed:
  omission is indistinguishable from drift. A project whose tasks
  genuinely follow a different contract should name its category
  something other than todo/ideas, which takes it out of scope honestly.

  As of 2026-07-07 no extensions exist, so in practice every in-scope
  file is the byte-identical one-line stub.
originating-commits:
  - 6a2c361   # 2026-05-15: llm-{kb,subtask,collab}: centralize idea/todo schemas on llm-subtask skeleton
  - "7612398" # 2026-05-21: llm-{subtask,collab,kb}/.claude: propagate strict schema (byte-identical to skeleton)
  - 3bea19d   # 2026-05-21: todo.kb/schema-reuse-with-ref: drift surface — six byte-identical copies
why: |
  The todo and ideas frontmatter schemas serve as write-time
  validators across every skill's `.claude/` directory. They MUST be
  identical: agents commit-by-commit propagate field additions
  (cost-of-delay-2w, confidence) and any drift produces silently
  different validation behavior across the skill tree.

  Source-of-truth: `llm-subtask/skeleton/.claude/`. Copies elsewhere
  must be byte-identical until the schema-reuse-with-ref migration
  ($ref-based de-duplication, separate scope) lands.

  Originating commits propagated the schemas to llm-subtask, llm-kb,
  llm-collab. Completed 2026-05-27: the remaining authoring copies were
  propagated and the todo schema gained an optional `closeout:` field.
related-todo: ~/.claude/skills/llm-kb/.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md
verified-by: |
  2026-07-07 validate.sh sweep of ~/repo after the migrate.sh rollout:
  clean except the one documented judgment-pending NO-REF finding
  (ideation.physical-musings).
---

# Schema propagation from the llm-subtask canonical

(Named "strict schema propagation from skeleton" until 2026-07-07:
the invariant was byte-identical copies of the then-canonical
`skeleton/.claude/` schemas. See "Policy updated 2026-07-07".)

## Drift verified 2026-05-26

`diff` from `llm-subtask/skeleton/.claude/{todo,ideas}.jsonschema.yaml`
against each skill's `.claude/`:

**Missing schema files (snapshot; resolved 2026-05-27):**

- `llm-collab/.claude/ideas.jsonschema.yaml` -- propagated
- `llm-must-read-kb/.claude/todo.jsonschema.yaml` -- propagated
- `llm-must-read-kb/.claude/ideas.jsonschema.yaml` -- false positive:
  llm-must-read-kb authors no ideas (no `ideas.kb`/`ideas.md`), so the
  omission is legitimate. `validate.sh` now gates MISSING on the skill
  actually authoring the category.
- `llm-subtask/.claude/todo.jsonschema.yaml` (the skill that owns the
  schema!) -- propagated

**Byte-divergent schema files:** none currently detected in present
copies (good — propagation was correct where applied).

## Algorithm

`validate.sh` finds every `.claude/{todo,ideas}.kb/` under the search
roots (default `~/repo`) and checks the adjacent
`<category>.jsonschema.yaml`. Reports:

- `MISSING <path>` — the project authors the category but has no
  schema file
- `NO-REF  <path>` — schema file exists but doesn't `$ref` the
  canonical

(Until 2026-07-07 the check was a byte-diff against the skeleton
copies, reporting `MISSING`/`DIFFER`.)

`migrate.sh` writes the canonical stub for each MISSING entry.
NO-REF entries are NOT auto-resolved — a full copy is handled by the
2026-07-07 conversion migration, and anything else is genuine
divergence for the user to judge.

## Idempotency

- `validate.sh` is read-only.
- `migrate.sh` only creates files that don't exist; once present,
  re-running is a no-op.

## Sibling concern: the schema-reuse-with-ref migration

The current "all copies must be byte-identical" pattern is the
near-term remediation. The long-term fix is `$ref`-based schema
reuse so the skeleton becomes the single load-bearing definition and
copies become one-line pointers. That's tracked separately at
`~/.claude/skills/llm-kb/.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md`
(currently WSJF #1 by exec_score) and would supersede this migration
when it lands.

## Completion 2026-05-27

`migrate.sh` propagated the three genuinely-missing copies; the fourth
MISSING was a validator false positive (gated out, above). The todo
schema gained an optional `closeout:` string -- propagated byte-equal
to all four authoring copies. `validate.sh` now reports clean (no
MISSING, no DIFFER), so the byte-equality invariant holds tree-wide.

Note: the invariant is drift-prone (any future edit to one copy
reopens it). Treat `validate.sh` as a recurring check until the
schema-reuse-with-ref migration collapses the copies to `$ref`
pointers.

## Policy updated 2026-07-07

The anticipated `$ref` collapse happened: canonical schemas moved to
`llm-subtask/jsonschema/` and every copy (including the skeleton's) is
now a one-line `$ref` stub (see
`2026-07-07-000-schema-copies-to-ref-stubs.md`, the one-shot
conversion). This migration lives on as the recurring propagation
guard, with the invariant relaxed from byte-equality to
`$ref`-presence:

- **The `$ref` must appear.** Content improvements then propagate
  automatically -- editing the canonical file changes validation
  everywhere. The recurring pass exists to catch consumers that lost
  the `$ref` (fresh copies, hand-rolled replacements, projects that
  never got the stub).
- **Extension on top is allowed.** Semantics verified by scratch
  experiment against the real validator, 2026-07-07: under Draft
  2020-12, `$ref` + sibling keywords is *conjunction*, not override --
  consumers can add fields or narrow constraints, never loosen.
  Implemented 2026-07-08 as the two-entry-point convention: each
  canonical publishes a strict root (`$ref: "#/$defs/base"` +
  `unevaluatedProperties: false` -- what the unchanged one-line stubs
  get) and an open `#base` anchor. An extender is
  `$ref: "skill://llm-subtask/jsonschema/<category>.jsonschema.yaml#base"`
  plus its own `properties:` and `unevaluatedProperties: false` --
  purely local, no canonical edit, no coordination. Verified 2026-07-08
  end-to-end through llm.kb-validate: strict stub still rejects unknown
  fields; extender accepts its declared field, rejects junk, still
  can't loosen; both `#base` ($anchor) and `#/$defs/base` (pointer)
  resolve file-relative and through `skill://`. Required the 2020-12
  dialect bump in the canonicals (under draft-07, `$ref` siblings are
  ignored -- the strict root would be dead text).
- **Omission is not allowed.** A consumer that wants "almost the
  canonical contract" extends/narrows on top of the `$ref`, keeping
  the delta explicit; one that wants a different contract renames its
  category.

Known open finding: `ideation.physical-musings/.claude/todo.jsonschema.yaml`
is a hand-rolled local schema (NO-REF). Under this policy it should
either become `$ref` + narrowing, or rename its category.

## Applied 2026-07-07: tree-wide MISSING rollout

First run of the new-form pass: `migrate.sh` stubbed 19 MISSING schema
files across 12 downstream `.claude/` dirs (litellm, bukzor.garden ×3,
prototype.chatfs ×3, private.* ×2, scratch.vim-work,
template.python-project, ideation.physical-musings's ideas). Those
projects' todo/ideas frontmatter is validated for the first time;
nonconformant data found there is deliberately out of this migration's
scope, captured in
`llm-kb/.claude/todo.kb/2026-07-07-000-Downstream-todo-ideas-frontmatter-conformance-sweep.md`.
