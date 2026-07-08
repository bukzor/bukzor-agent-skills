---
managed-by: Skill(llm-subtask)
required-reading:
  - ~/.claude/skills/llm-kb/references/schema-design.md
  - ~/.claude/skills/llm-kb/lib/python/llmd/frontmatter_validate.py
suggested-reading:
  - https://json-schema.org/understanding-json-schema/structuring.html
related-effort: ~/.claude/skills/llm-collab/.claude/todo.kb/2026-02-09-000-design-kb-pattern-for-living-design-docs.md
cost-benefit-sweh:
  timebox:
    "@value": 1.0
    rationale: |
      Pattern definition + a couple working examples. Beyond 1h you're
      designing tooling; spike on real adoption first to learn what's
      actually needed.
    confidence: unsure
  benefit-2w:
    "@value": 1.0
    rationale: |
      Reduces schema duplication across kbs (esp. shared `why[]` field).
      Adoption is gradual; expect ~1h saved through reduced copy-paste
      and clearer cross-kb relationships.
    confidence: unsure
  cost-of-delay-2w:
    "@value": 1.5
    rationale: |
      Six copies of the SWEH schema (per `sweh-schema-source.md` in
      homedir-archeology `reference.kb/`) hand-propagate every field
      change. The 2026-05-18 expansion (`cost-of-delay-2w` +
      `confidence`) added ~50 lines × 6 files = ~300 lines of new
      duplicate text — the dup tax visibly worsened.

      During the active backlog re-rate sweep, expect 2-4 schema edits
      over 2 weeks. Each propagation costs ~0.2 SWEh of mechanical
      copying plus drift-risk when a copy is missed. 1.5 SWEh budgets
      ~3 events × 0.3 SWEh plus a forgotten-file tax.
    confidence: unsure
---

# Schema Reuse with $ref

**Priority:** Medium
**Complexity:** Medium
**Context:** Emerged from design.kb pattern work; needed for shared `why[]` field across abstraction levels

## Problem Statement

llm.kb lacked support for reusable schema definitions. Projects with
multiple `.kb/` directories sharing common fields had to duplicate schema
definitions — inconsistency risk on every shared-field update, verbose
schemas, no single source of truth. By 2026-05-21 the todo/ideas schemas
had six hand-synced byte-identical copies, each field addition costing
six edits.

## State (as of 2026-07-08): effectively complete

The full arc is history in `2026-02-09-000-schema-reuse-with-ref.kb/`
(chronological; one entry per session's progress, decision, or finding).
Where things landed:

- **Resolution:** the validator resolves `$ref` via `skill://` (in-memory,
  through the `~/.claude/skills/` symlink farm), `file://`-based relative
  paths, and JSON-Pointer/`$anchor` fragments; circular refs verified a
  non-issue (lazy resolution).
- **Canonical placement:** `llm-subtask/jsonschema/{todo,ideas}.jsonschema.yaml`
  (skill-root `jsonschema/`, never `skeleton/` — copies drift; all skills
  publishing schemas now use a `jsonschema/` dir). Every consumer,
  skeleton included, is a one-line stub.
- **Extension:** two-entry-point convention — strict document root for
  stubs, open `#base` anchor for extenders; canonicals on the 2020-12
  dialect.
- **Documentation:** `references/schema-reuse.md` is the durable pattern
  guide; `complete-example/` demonstrates file-relative reuse.
- **Enforcement:** `migrations.kb/2026-07-07-000-schema-copies-to-ref-stubs.md`
  (one-shot conversion) + `2026-05-15-000-schema-propagation-from-canonical.md`
  (recurring $ref-presence guard, tree-wide).

## Success Criteria

- [x] `references/schema-reuse.md` exists and is comprehensive
- [x] Validator resolves file-relative `$ref`
- [x] `complete-example/` demonstrates the pattern
- [x] yaml-language-server works with the pattern (verified via
      generic-resolver proxy; a real-editor check remains optional)

## Residual open items (tracked elsewhere)

- Downstream data conformance:
  `2026-07-07-000-Downstream-todo-ideas-frontmatter-conformance-sweep.md`
- `ideation.physical-musings` NO-REF judgment: propagation migration entry
- `$ref` in `oneOf` blocks: unexplored; no use case has arisen
