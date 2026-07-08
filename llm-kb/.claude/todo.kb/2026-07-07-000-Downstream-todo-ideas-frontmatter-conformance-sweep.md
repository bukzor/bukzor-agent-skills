---
managed-by: Skill(llm-subtask)
status: open
related-effort: ~/.claude/skills/llm-kb/migrations.kb/2026-05-15-000-schema-propagation-from-canonical.md
cost-benefit-sweh:
  timebox:
    "@value": 2.0
    rationale: |
      ~15 failing files across 5 projects, mostly mechanical (add
      managed-by, quote @value, rename/drop stray fields). Some need
      judgment (unknown fields may deserve canonical-schema extension
      instead of deletion). ~8 min/file average.
    confidence: tentative
  benefit-2w:
    "@value": 0.5
    rationale: |
      Downstream projects get trustworthy write-time validation; the
      real benefit accrues per future editing session in those repos,
      thin within 2 weeks.
    confidence: tentative
---

# Downstream todo/ideas frontmatter conformance sweep

**Priority:** Low
**Complexity:** Low
**Context:** Fallout from the schema-propagation migration
(`migrations.kb/2026-05-15-000-schema-propagation-from-canonical.md`).
On 2026-07-07 its `migrate.sh` stubbed 19 missing
`.claude/{todo,ideas}.jsonschema.yaml` files across downstream
projects. Validation now runs there for the first time, and some
existing frontmatter fails against the canonical schema.

## Problem Statement

Newly-validated downstream todo.kb/ideas.kb frontmatter predates the
canonical schema's current shape. Deliberately NOT fixed during the
migration to keep its scope contained; captured here instead.

## Findings (2026-07-07 sweep, per `llm.kb-validate <project>/.claude`)

Clean: litellm, bukzor.garden (root), super-tictactoe, sttt-engine,
private.bukzor-llc, scratch.vim-work, template.python-project.

Failing, by flavor:

- Invalid YAML -- unquoted `@value:` key (needs `"@value":`):
  - [ ] prototype.chatfs `todo.kb/2026-05-16-000-buck2-migration.md`
  - [ ] har-browse `ideas.kb/2026-05-12-000-har-browse-streaming-witness...md`
- Missing `managed-by` and/or stray `anthropic-skill-ownership`
  (predates the ownership-marker migration):
  - [ ] private.evan-family `todo.kb/2026-04-17-{000,001}-*.md`
  - [ ] chatfs-mockup-chatgpt `todo.kb/2026-05-11-{000,001}, 2026-06-20-000`
- Unknown fields (`depends-on`, `depends`, `parent`,
  `supersedes-question-from`) -- decide per field: rename to a canonical
  field, drop, or extend the canonical schema (see the extension recipe
  in the migration entry):
  - [ ] prototype.chatfs `todo.kb/2026-01-02-002, 2026-05-16-{000,001}`
- `cost-benefit-sweh` rejected by the canonical *ideas* schema --
  investigate: likely the flat pre-time-period-nesting shape:
  - [ ] ideation.physical-musings `ideas.kb/2026-07-03-000-*.md`
- [ ] har-browse `todo.kb/2026-04-24-000-har-browse-streaming-refactor.md`
      (error truncated in sweep output; re-run to see it)

Also NOT covered here: kb validation errors *outside* `.claude/` in
those repos (e.g. prototype.chatfs has ~150 across its own doc kbs) --
pre-existing, unrelated to the stub rollout.

## Success Criteria

- [ ] `llm.kb-validate <project>/.claude` clean for every project
      stubbed by the 2026-07-07 rollout
- [ ] Any field worth keeping is a deliberate schema extension, not an
      unvalidated stray
