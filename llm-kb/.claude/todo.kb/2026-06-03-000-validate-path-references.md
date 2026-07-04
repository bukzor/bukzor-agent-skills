---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-02-09-000-schema-reuse-with-ref.md
cost-benefit-sweh:
  timebox:
    '@value': 3
    rationale: deliverable 1 (frontmatter path format + validator) is bounded; deliverable 2 (prose checker) is a design problem — stop and reassess there
    confidence: unsure
  benefit-2w:
    '@value': 0.5
    rationale: path rot is slow but real (live example in the file); saves future dead-ref confusion across all kbs
    confidence: unsure
  cost-of-delay-2w:
    '@value': 0.1
    rationale: rot accumulates slowly
    confidence: unsure
---

# Validate path references in kb files

**Context:** kb files are full of path references -- frontmatter
(`requires:`, `required-reading:`, `related-effort:`) and body prose
("see `references/schema-design.md`"). Nothing checks they resolve, so
they rot silently. Live example: `todo.kb/2026-02-09-000`'s
`required-reading` points at `~/.claude/skills/llm.kb/...` -- the
skill was renamed `llm-kb`.

## Deliverables

1. **Custom jsonschema type for frontmatter** -- a way to denote
   "path that must exist, resolved file-relative" (also `~` and
   `agent-skill://` forms). Schema annotation (e.g. a shared
   definition or `format:`) + enforcement in
   `lib/python/llmd/frontmatter_validate.py` / `bin/llm.kb-validate`.
2. **Body-markdown checker** -- find path-like references in prose
   and verify they resolve. Significantly harder: what counts as a
   reference (code spans, links, bare mentions)? False-positive
   management is the core design problem.

## Open Questions

- Resolution bases: file-relative vs `~` vs repo-root vs
  `agent-skill://` -- one annotation or several?
- Deliverable 2: lint-with-allowlist, or only check delimited forms
  (markdown links, code spans that look like paths)?
