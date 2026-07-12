---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-06-03-000-validate-path-references.md
cost-benefit-sweh:
  timebox:
    "@value": 2
    rationale: split off deliverable 2 of the related-effort file; the design problem (what counts as a reference, false-positive management) is the bulk of the cost
    confidence: unsure
  benefit-2w:
    "@value": 0.3
    rationale: closes the remaining gap after deliverable 1 -- frontmatter links validated but prose links still rot silently
    confidence: unsure
---

# Body-markdown path-link checker

**Blocked on:** `2026-06-03-000-validate-path-references.md` (frontmatter
path type + validator) landing first -- reuses its resolution
semantics (file-relative, `~`, `skill://`) and its
"exists on disk" check, applied to prose instead of YAML values.

## Problem Statement

kb body prose is full of path-like references ("see
`references/schema-design.md`") that nothing checks. Once frontmatter
`path`-typed fields are validated (the related-effort file), body
prose is the remaining rot surface.

## Prototype

`../../2026-06-03-000-validate-path-references.prototype/validate_links.py`'s
`body_links()` already does a rough cut: regex `` `(\.\.?/[^`]+\.md)` ``
over backtick-wrapped relative markdown links, resolved file-relative
and checked with `.is_file()`. Covers the easy case (delimited,
explicit relative paths); does not attempt bare-mention or
non-code-span references.

## Open Questions

- Lint-with-allowlist, or only check delimited forms (markdown links,
  code spans that look like paths)? Prototype currently does the
  latter only.
- Forward-reference false positives: a link to a planned-but-not-yet-
  created file (e.g. a deliverable a later step creates) reports as
  broken even though it's intentional. Accept as real signal ("go
  create it"), or add a way to mark a known-forward-reference?
- What counts as a reference at all -- code spans, `[text](link)`
  markdown links, bare mentions in prose?

## Success Criteria

- [ ] Body path-like references in `.kb/` markdown are checked for
      existence, file-relative to the referencing file
- [ ] False-positive rate on forward-references is addressed (accepted
      as signal, or explicitly suppressible)
