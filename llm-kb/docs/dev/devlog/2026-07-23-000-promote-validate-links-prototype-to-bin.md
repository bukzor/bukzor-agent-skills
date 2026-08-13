# Devlog: 2026-07-23 -- promote validate_links prototype to bin/

## Focus

`2026-06-03-000-validate-path-references.prototype/validate_links.py`
had been sitting unwired since 2026-07-09 (see the prototype's own
README and `.claude/todo.kb/2026-07-09-000-body-markdown-path-link-checker.md`).
Its own "cheapest, do first" integration step -- mention it from
`references/creating-a-new-kb.md`'s validation pass -- hadn't happened,
so agents kept hand-rolling one-off regex link-checkers from scratch
every time a kb's cross-references needed auditing, repeating the same
false-positive mistakes (e.g. over-broad backtick-path regexes matching
CLI examples) each session. Observed directly: an agent transcript
doing exactly this against an unrelated repo's `design.kb/`.

## Decisions

### Move the script to `bin/`, not just document the prototype path

Instructions (self-audits, references) should not point at a
`*.prototype/` directory colocated with `todo.kb/` -- that location
signals "scratch, not load-bearing," which undersells a script that's
now a documented, referenced part of the workflow. `git mv`'d
`validate_links.py` to `bin/llm.kb-validate-links`, alongside the
existing `bin/llm.kb-validate`.

### Shebang + chmod, not `python3 script.py` in docs

Matches this repo's existing convention for standalone scripts with
third-party deps (see `docs/dev/devlog/2025-12-10-000-*.kb/*-analysis.py`):
`#!/usr/bin/env -S uv run --script` + PEP 723 inline metadata
(`dependencies = ["pyyaml"]`) + `chmod +x`. Callers invoke it directly
(`bin/llm.kb-validate-links <path>`) instead of needing to know or type
an interpreter.

### Wired into two instruction points

- `references/creating-a-new-kb.md` Pass 4 (validation) -- now mentions
  the link checker alongside `bin/llm.kb-validate` until it's folded in
  proper.
- `SKILL.kb/self-audit.kb/cross-references.md` -- Procedure now runs the
  script first, then hand-scans only for what it doesn't cover (bare
  relative paths without a `./`/`../` prefix, markdown `[text](path)`
  links, frontmatter fields outside its tracked list).

### `--strict`/`--lax` modes, strict as default

User request, after seeing the same gap from a second angle (a JIT
script in an unrelated session hand-rolling a `.kb/`-directory-ref
checker this script didn't cover): make the path-nomination heuristic
configurable rather than fixed.

- `--strict` (default): only `./`/`../`-prefixed strings count as
  paths -- unambiguous, and also generalized to check *any* extension
  (not just `.md`), so dot-slash-prefixed directory references are
  now caught too, not only file references.
- `--lax`: additionally nominates strings that end with `/`, contain
  `.kb/`, or end with `.md`, even unprefixed -- more recall, more
  false positives.

Default is `--strict`: this script runs as a Tier-1 blocking self-audit
on every touched file (`SKILL.kb/procedures.kb/run-self-audits.md`); a
noisy default there means triaging false positives on every commit,
which is the same wasted-iteration problem this whole change exists to
remove, just moved into a committed tool. `--lax` fits a deliberate,
supervised sweep instead (e.g. the kind of full-kb audit that birthed
the original prototype).

### Whitespace disqualifies a candidate, in both modes

Generalizing strict mode's suffix acceptance (any extension, not just
`.md`) introduced a real false positive: a command example embedding a
placeholder in one backtick span (`` `../../bin/llm.kb-validate-links <path>` ``,
written in this session's own doc edits) starts with `../` and was
being treated as one literal path including the trailing `<path>`
text. Real paths never contain whitespace in this repo's kebab-case
convention, so `_is_path_shaped()` now rejects any candidate
containing whitespace before checking prefix/shape -- a general fix,
not a doc patch.

### Two real pre-existing broken links found and fixed

Running `--strict` over the whole `llm-kb` tree (not just the files
touched above) surfaced real breakage predating this session:
`SKILL.kb/self-audit.md` referenced `must-read/` -- a same-directory
sibling -- as `../must-read/` (one level too far up) in one spot and as
a bare `must-read/before/...md` (no prefix at all) in another. Fixed
both to `./must-read/...`. (First pass mistakenly dropped the prefix
entirely instead of correcting it to `./` -- caught and fixed in
review: this repo's convention is that a real reference is always
`./`- or `../`-prefixed, never bare.)

## Verification

- `bin/llm.kb-validate-links SKILL.kb references` -- 0 broken links
  after fixing the doc edits' own illustrative example paths (a
  dot-slash-prefixed example path in backticks tripped the very regex
  being documented -- reworded to avoid that pattern in prose).
- Confirmed the shebang resolves PyYAML via `uv run --script` standalone.
- `bin/llm.kb-validate-links --strict .` over the whole `llm-kb` tree:
  138 files, down to 6 known/accepted failures (see Follow-up) after
  the `self-audit.md` fixes above.
- `bin/llm.kb-validate .` (schema validator) and `uv run pytest`: both
  still pass, confirming no regression in the sibling validator this
  script doesn't touch.

## Follow-up

- Full integration (fold into `frontmatter_validate.py` so
  `bin/llm.kb-validate` reports schema errors and broken links in one
  pass) is still open -- see
  `.claude/todo.kb/2026-06-03-000-validate-path-references.md` and its
  follow-on.
- 6 files still fail `--strict`: forward references to collections
  `docs/dev/CLAUDE.md` marks "planned but not yet seeded"
  (`glossary.kb/`, `principles.kb/`, `failure-modes.kb/`). Real signal,
  not a bug -- the forward-reference open question in
  `.claude/todo.kb/2026-07-09-000-body-markdown-path-link-checker.md`
  is exactly this, still unresolved.
- One new false-positive class found: an ellipsis-truncated
  illustrative path (`` `../jsonschema/...` ``) in an unrelated
  `todo.kb/` file reads as a literal path to `--strict`. Logged in the
  same Open Questions section rather than fixed.
- No test coverage for this script's new modes/heuristic -- see
  `.claude/todo.kb/2026-07-25-000-Test-coverage-for-llm-kb-validate-links.md`.
