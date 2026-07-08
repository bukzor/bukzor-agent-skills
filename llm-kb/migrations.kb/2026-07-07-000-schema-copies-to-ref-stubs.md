---
status: complete
scope: |
  Every `.claude/todo.jsonschema.yaml` and `.claude/ideas.jsonschema.yaml`
  across the user's tree (~/repo, plus any project with a `.claude/`).
  Each must be the canonical one-line stub:

      # yaml-language-server: $schema=https://json-schema.org/draft-07/schema
      $ref: "skill://llm-subtask/jsonschema/<category>.jsonschema.yaml"

  The canonical schemas themselves live at `llm-subtask/jsonschema/` --
  the only full copies allowed anywhere. Excluded: files that diverged
  from canonical on purpose (a project with genuinely different todo
  frontmatter keeps its own schema; it just isn't a *copy* anymore).
related-todo: ~/.claude/skills/llm-kb/.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md
why: |
  The strict-propagation migration kept N byte-identical copies of the
  todo/ideas schemas in sync by hand -- every field addition cost N edits
  and a drift check. With `$ref` resolution in the validator (skill://
  and file-relative, landed 2026-07-05), copies can be one-line stubs
  onto a single canonical file: edit once, validated everywhere.

  The canonical files also moved out of `skeleton/.claude/` to
  `llm-subtask/jsonschema/`: skeleton contents get *copied* into new
  projects, so a full schema in the skeleton mints a fresh drifting
  snapshot on every init. The skeleton now ships the stub itself --
  projects initialized from it are live-linked from day one.
---

# Schema copies to $ref stubs

## Transformation

For each in-scope file that is an unmodified snapshot of some historical
canonical schema: replace its content with the one-line stub (plus
yaml-language-server modeline). Files that match no historical canonical
blob have local intent -- report, don't rewrite; the user judges.

`validate.sh` (read-only) classifies each in-scope file:

- `SNAPSHOT` -- byte-identical to a historical canonical version; safe
  to stub mechanically
- `STALE-REF` -- a stub pointing at the pre-move path
  (`skill://llm-subtask/skeleton/.claude/...`); safe to repoint
- `DIVERGED` -- matches no historical canonical blob; human judgment

`migrate.sh` rewrites `SNAPSHOT` and `STALE-REF` files to the current
stub; leaves `DIVERGED` untouched. Idempotent: conforming stubs match a
historical blob check trivially and rewriting them is a byte-identical
no-op.

## Applied so far

- 2026-07-07: whole skills repo -- canonical schemas moved to
  `llm-subtask/jsonschema/`, skeleton + all 8 skill-local/repo-root
  copies now stubs, `llm.kb-validate .` clean (138 files, 0 errors).
- 2026-07-07: full ~/repo sweep -- `template.python-project` held a
  stale pre-status-vocabulary snapshot (cosmetically re-wrapped, hence
  DIVERGED not SNAPSHOT); judged intent-free and stubbed, its todo.kb
  validates clean through the stub (left uncommitted there for review).
  Sole residual: `ideation.physical-musings/.claude/todo.jsonschema.yaml`,
  a genuinely local 12-line schema -- excluded by scope (diverged on
  purpose), stays as-is.

This migration is the one-shot *conversion* (copies become stubs). The
recurring guard -- every authoring project must carry the `$ref`,
including projects with no schema file at all (MISSING) -- is
`2026-05-15-000-schema-propagation-from-canonical.md`, which this
entry's stub shape now feeds.

## Follow-on (out of scope here)

Directory-name uniformity: llm-discourse-graph and llm-design-kb export
schemas from `schemas/`; the convention this migration establishes is
`jsonschema/` at the skill root (matches the `.jsonschema.yaml` suffix
and `references/schema-reuse.md`'s prescribed placement). Sweeping those
two skills to `jsonschema/` is a separate rename, tracked in the
related todo.
