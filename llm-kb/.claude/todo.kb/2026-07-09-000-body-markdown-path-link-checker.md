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

## Existing script

`../../bin/llm.kb-validate-links`'s `body_links()` scans every
backtick-wrapped span and gates each with a shared `_is_path_shaped()`
heuristic (2026-07-23), now offering two modes:

- `--strict` (default): only `./`/`../`-prefixed spans count -- the
  original delimited-forms-only behavior.
- `--lax`: also nominates spans that end with `/`, contain `.kb/`, or
  end with `.md`, even unprefixed -- more recall, more false positives.

Still does not attempt bare-mention (non-code-span) references or
`[text](link)` markdown link syntax.

## Open Questions

- ~~Lint-with-allowlist, or only check delimited forms?~~ Resolved
  2026-07-23 via the `--strict`/`--lax` split above -- both exist now,
  selectable per invocation rather than a single fixed choice.
- Forward-reference false positives: a link to a planned-but-not-yet-
  created file (e.g. a deliverable a later step creates) reports as
  broken even though it's intentional. Accept as real signal ("go
  create it"), or add a way to mark a known-forward-reference? Live
  example: `docs/dev/CLAUDE.md`'s "Planned but not yet seeded"
  collections (`glossary.kb/`, `principles.kb/`, `failure-modes.kb/`
  mentions) currently fail `--strict` -- 6 files, confirmed 2026-07-23.
- New false-positive class found 2026-07-23: ellipsis-truncated
  illustrative paths in prose, e.g. `` `../jsonschema/...` `` in
  `.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.kb/2026-07-07-001-complete-example-refactor-yaml-lsp-verification.md`
  -- legitimate prose, not a bug, but `--strict` flags it (starts with
  `../`). Not fixed; same "is this a real reference" ambiguity as the
  forward-reference question above.
- What counts as a reference at all -- code spans, `[text](link)`
  markdown links, bare mentions in prose? `--lax`'s shape heuristics
  are a partial answer for code spans; markdown-link-syntax and bare
  mentions are still unaddressed.

## Success Criteria

- [ ] Body path-like references in `.kb/` markdown are checked for
      existence, file-relative to the referencing file
- [ ] False-positive rate on forward-references is addressed (accepted
      as signal, or explicitly suppressible)
