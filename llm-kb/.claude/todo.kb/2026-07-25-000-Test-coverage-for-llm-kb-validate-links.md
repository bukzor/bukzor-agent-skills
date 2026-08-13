---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-06-03-000-validate-path-references.md
cost-benefit-sweh:
  timebox:
    "@value": 1
    rationale: mirrors an existing test file's conventions (fixtures, pytest-describe naming); no design work, just coverage
    confidence: unsure
  benefit-2w:
    "@value": 0.3
    rationale: script gained --strict/--lax modes and a whitespace heuristic on 2026-07-23 with zero test coverage; a future edit could silently break either mode
    confidence: unsure
---

# Test coverage for llm.kb-validate-links

**Priority:** low
**Complexity:** small
**Context:** `bin/llm.kb-validate-links` (promoted from a `*.prototype/`
script 2026-07-23, see `docs/dev/devlog/2026-07-23-000-promote-validate-links-prototype-to-bin.md`)
has no automated tests. Its sibling `lib/python/llmd/frontmatter_validate.py`
has `frontmatter_validate_test.py` (pytest-describe style, `tmp_path`
fixtures) -- this file should follow the same shape.

## Problem Statement

`_is_path_shaped()`, `frontmatter_links()`, `body_links()`, and
`broken_links()` have no test coverage. The whitespace disqualifier and
`--strict`/`--lax` split were added and verified only by ad hoc runs
against the live `llm-kb` tree during that session, not by a
repeatable test suite. A future edit (e.g. touching the regex or the
heuristic) has no safety net.

## Proposed Solution

New `bin/llm.kb-validate-links_test.py` (or move the script's logic
into `lib/python/llmd/` first -- see the blocked-on integration effort
-- and test there instead, avoiding testing a `bin/`-resident script
directly). Cover:

- `_is_path_shaped`: strict accepts a dot-slash- or dot-dot-slash-
  prefixed string, rejects the same string bare (no prefix); lax
  additionally accepts `x/`, `x.kb/y`, `x.md`; whitespace disqualifies
  in both modes regardless of prefix.
- `frontmatter_links`: only `LINK_FIELDS` keys are read; list and
  scalar field values both yield; non-string values are skipped.
- `body_links`: backtick spans are filtered by `_is_path_shaped`;
  non-backtick prose is ignored.
- `broken_links`: `/`-suffixed candidates resolve as directories
  (`.is_dir()`), everything else as files (`.is_file()`).
- Regression cases for the two bugs found 2026-07-23: a command
  example with a trailing placeholder in one backtick span (e.g.
  `` `../foo <path>` ``) must not false-positive; a same-directory
  reference needs its `./` prefix, not a bare name.

## Implementation Steps

- [ ] Decide: test the `bin/` script directly (import via
      `importlib`/subprocess) or fold its logic into `lib/python/llmd/`
      first and test that module -- the latter also progresses the
      blocked integration effort in one pass.
- [ ] Write fixtures mirroring `frontmatter_validate_test.py`'s
      `tmp_path`-based style.
- [ ] Cover the four function-level cases above plus the two
      regression cases.
- [ ] Wire into whatever runs `frontmatter_validate_test.py` today
      (`uv run pytest`) so both suites run together.

## Open Questions

- Does this script's promotion out of scratch status also warrant
  moving its logic into `lib/python/llmd/` now, ahead of the full
  `bin/llm.kb-validate` integration tracked in
  `./2026-06-03-000-validate-path-references.md`? Doing so here would
  let this task and that one share the same test-writing effort.

## Success Criteria

- [ ] `uv run pytest` covers `_is_path_shaped`, `frontmatter_links`,
      `body_links`, and `broken_links` including both modes
- [ ] Both 2026-07-23 regression cases (command-example false positive,
      missing-prefix same-dir reference) are encoded as test cases

## Notes

Surfaced during the 2026-07-23 session-end claim-ledger flush as an
open, undischarged claim (script has real behavior with zero tests).
