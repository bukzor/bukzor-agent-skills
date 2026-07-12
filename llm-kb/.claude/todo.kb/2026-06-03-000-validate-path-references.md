---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-02-09-000-schema-reuse-with-ref.md
cost-benefit-sweh:
  timebox:
    '@value': 1.5
    rationale: bounded -- schema annotation/format plus enforcement wiring, with a working prototype to generalize from rather than design from scratch
    confidence: tentative
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

**Follow-on:** `2026-07-09-000-body-markdown-path-link-checker.md`
covers prose links; blocked on this file's deliverable landing first.

**Prototype exists (2026-07-09):**
`../../2026-06-03-000-validate-path-references.prototype/validate_links.py`
(+ sibling `README.md`) -- built ad hoc during the Abby's Craft
`design.kb/` breakdown, colocated by date-slug but kept outside
`todo.kb/` since it's code, not a markdown planning doc. Already does
file-relative existence checks for both frontmatter link fields
(`why`, `depends`, `source`, `sources`, `candidate-resolutions`,
`conclusion`, `premises`, `resolved`) and backtick-wrapped body links
-- i.e. a rough cut of this file's deliverable *and* the follow-on's,
but as a standalone script duplicating `extract_frontmatter`, not a
jsonschema type/format and not wired into `bin/llm.kb-validate`. Its
README has a 3-step integration plan (docs mention → fold into
`frontmatter_validate.py` → handle forward-reference false positives).
This changes the deliverable from "design from scratch" to
"integrate/generalize this script."

## Deliverable

**Custom jsonschema type for frontmatter** -- a way to denote "path
that must exist, resolved file-relative" (also `~` and `skill://`
forms). Probationary name: `path` (final naming TBD). Schema
annotation (e.g. a shared definition or `format:`) + enforcement in
`lib/python/llmd/frontmatter_validate.py` / `bin/llm.kb-validate`.

## Open Questions

- Resolution bases: file-relative vs `~` vs repo-root vs
  `skill://` -- one annotation or several?
