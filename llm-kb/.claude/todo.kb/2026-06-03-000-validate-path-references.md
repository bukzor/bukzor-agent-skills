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

**Script exists, promoted to `bin/` (2026-07-23):** `../../bin/llm.kb-validate-links`
-- built ad hoc during the Abby's Craft `design.kb/` breakdown
(2026-07-09), then moved out of a `*.prototype/` dir into `bin/` since
agents shouldn't be pointed at scratch-labeled paths from load-bearing
instructions (see `docs/dev/devlog/2026-07-23-000-promote-validate-links-prototype-to-bin.md`).
Already does file-relative existence checks for both frontmatter link
fields (`why`, `depends`, `source`, `sources`, `candidate-resolutions`,
`conclusion`, `premises`, `resolved`) and backtick-wrapped body links
-- i.e. a rough cut of this file's deliverable *and* the follow-on's,
but as a standalone script duplicating `extract_frontmatter`, not a
jsonschema type/format and not wired into `bin/llm.kb-validate`. Step 1
of the original 3-step integration plan (docs mention → fold into
`frontmatter_validate.py` → handle forward-reference false positives)
is done (`references/creating-a-new-kb.md`,
`skill.kb/self-audit.kb/cross-references.md` both point at it now).
This changes the remaining deliverable from "design from scratch" to
"integrate/generalize this script."

## Observed in the field

A full-repo run against `~/claude/meta-reasoning` (3071 files) found 5
hits: 3 real depth-off refs, 2 false positives. Both false-positive
classes are integration work this file owns.

**It does not filter by `.gitignore`.** One hit was inside a gitignored
`empty.bak/` holding vendored plugin files -- not corpus, and its rot
must not pad the error count. `llm.kb-validate` already gets this right
and SKILL.md states the rule for it ("What the walk *discovers* is
filtered by `.gitignore`"), asked per-repository so a submodule's own
ignores govern inside it. Folding the checker in should inherit that
walk rather than keep a second one.

**Forward references read as breaks.** `design-3.claim.kb/CLAUDE.md`
cites `../design-3.claim.md` in the same sentence that says it is
"written at review exit" -- the file is correctly absent until then.
This is the known step-3 false-positive problem with a concrete
specimen: the prose declares the reference deferred, so the signal
exists in the text, but nothing machine-readable carries it.

## Deliverable

**Custom jsonschema type for frontmatter** -- a way to denote "path
that must exist, resolved file-relative" (also `~` and `skill://`
forms). Probationary name: `path` (final naming TBD). Schema
annotation (e.g. a shared definition or `format:`) + enforcement in
`lib/python/llmd/frontmatter_validate.py` / `bin/llm.kb-validate`.

## Open Questions

- Resolution bases: file-relative vs `~` vs repo-root vs
  `skill://` -- one annotation or several?
