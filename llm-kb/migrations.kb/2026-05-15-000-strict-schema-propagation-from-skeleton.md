---
status: verified
scope: |
  Every skill's `.claude/` directory should hold byte-identical copies
  of the `todo.jsonschema.yaml` and `ideas.jsonschema.yaml` files from
  the canonical source: `llm-subtask/skeleton/.claude/`. Skills that
  don't author todo/ideas (e.g. consumer-only skills) may legitimately
  omit, but presence implies byte-equality.
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
---

# Strict schema propagation from llm-subtask skeleton

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

`validate.sh` walks each skill under `bukzor-agent-skills/` and diffs
its `.claude/{todo,ideas}.jsonschema.yaml` against the canonical
skeleton copies. Reports:

- `MISSING <path>` — skeleton has the file; skill does not
- `DIFFER <path>` — both exist but bytes differ

`migrate.sh` for each MISSING entry: `cp` from the skeleton path
(idempotent — copying the same content twice is a no-op).
DIFFER entries are NOT auto-resolved — the divergence direction is
context-dependent (sometimes the skill is correct and the skeleton is
behind), so the user judges.

## Idempotency

- `validate.sh` is read-only.
- `migrate.sh` overwrites MISSING destinations from the skeleton.
  Once content matches, re-running is a byte-identical no-op.

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
