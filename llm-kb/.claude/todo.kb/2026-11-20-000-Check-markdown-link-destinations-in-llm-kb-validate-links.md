---
managed-by: Skill(llm-subtask)
status: done
related-effort: ./2026-07-09-000-body-markdown-path-link-checker.md
---

# Check markdown link destinations in llm.kb-validate-links

**Priority:** medium. Reference-style links are the house style
(`~/.claude/must-read.kb/before/editing-documentation.md`), so the commonest
link form in the corpus is the one the checker cannot see.
**Complexity:** small
**Context:** `../../bin/llm.kb-validate-links`, `body_links()`

## Problem Statement

`body_links()` reads only backtick spans (`BACKTICK_SPAN_RE`). Markdown link
destinations go unchecked in both forms:

- inline, `[text](../path.md)`;
- reference definitions, `[label]: ../path.md`, including the form a formatter
  wraps onto the next line (`[label]:` then an indented `../path.md`).

The checker then reports a clean result that covers none of those links.
SKILL.md's "Checks frontmatter path fields and inline body links both" reads as
if markdown links were included.

## Current Situation

Field case, 2026-11-20: `my-own-shadertoy/.claude/must-read.kb/` had 16 entries,
each linking its ledger claim through reference definitions. The checker said
"0 links in 16 files, 0 files with broken links". The links had to be resolved
by hand.

Witness, one file at `x.kb/item.md`:

```markdown
# x

See [GOOD] and [BAD], or [inline](../missing-inline.md), or `../missing-code.md`.

[GOOD]: ./item.md
[BAD]:
  ../missing-ref.md
```

Today it reports only `../missing-code.md`. It should also report
`../missing-inline.md` and `../missing-ref.md`, and pass `./item.md`.

## Proposed Solution

Nominate markdown link destinations alongside backtick spans, through the same
`_is_path_shaped()` gate and `broken_links()` resolution, so `--strict` and
`--lax` keep their meaning. Skip URLs (`scheme:`) and pure `#anchor`
destinations; strip a trailing `#anchor` before resolving.

## Implementation Steps

- [x] Extract destinations of inline links and reference definitions, wrapped
      definitions included
- [x] Encode the witness above as a test (`lib/python/llmd/validate_links_test.py`;
      the rest of `./2026-07-25-000-Test-coverage-for-llm-kb-validate-links.md`
      can reuse its `_check()` helper)
- [x] Correct SKILL.md's description of what the checker reads

## Open Questions

- ~~Regex or a CommonMark parser (`markdown-it-py`)?~~ Ruled 2026-11-20: the
  parser, as the community-standard choice; landed as an inline script
  dependency plus a root `pyproject.toml` dependency so pyright resolves it.
  Rationale: a regex misreads a prose line
  that happens to start `[LABEL]: text`, which formatters do produce when they
  rewrap a paragraph. CommonMark rejects it as a definition because a
  definition's destination must end the line or precede a title. A parser also
  skips links inside code blocks for free.

## Success Criteria

- [x] The witness reports exactly `../missing-inline.md` and `../missing-ref.md`
      (plus the pre-existing `../missing-code.md`)
- [x] Running it over `my-own-shadertoy/.claude/must-read.kb/` counts its
      reference links, all resolving: 19 links in 15 files, 0 broken

## Notes

Separable from `./2026-07-09-000-body-markdown-path-link-checker.md`, and not
blocked by it: that entry's open question is which prose spans count as
references at all. A markdown link destination is a reference by syntax, so
none of that judgment applies.
