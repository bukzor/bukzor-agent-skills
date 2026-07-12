---
last-updated: 2026-07-09
---

# validate-path-references prototype

Working scripts that aren't formally part of the skill yet -- candidate
for integration into `bin/`, `lib/python/llmd/`, or the procedure docs,
per `.claude/todo.kb/2026-06-03-000-validate-path-references.md` and
its follow-on `.claude/todo.kb/2026-07-09-000-Body-markdown-path-link-checker.md`.
Nothing here is wired up or tested against the package's own test
suite; treat as a proposal, not a shipped tool.

## `validate_links.py`

**What it does:** walks a directory tree of `.md` files and checks that
every path-shaped value in known cross-reference frontmatter fields (`why`,
`depends`, `source`, `sources`, `candidate-resolutions`, `conclusion`,
`premises`, `resolved` — the union across llm-kb, llm-design-kb, and
llm-discourse-graph schemas) resolves to a real file, relative to the
referencing file's directory. It also checks backtick-wrapped relative
markdown links in body prose (`` `../foo.md` ``) the same way.

**Why it exists:** `bin/llm.kb-validate` (`llmd.frontmatter_validate`)
checks that frontmatter *conforms to its JSON schema* — but a schema only
constrains `why:` to be "an array of strings." It has no way to know those
strings are supposed to be paths, so a typo'd `why:`/`depends:` link
currently passes validation silently and just becomes a broken chain,
discoverable only by a human clicking through every link. This is exactly
the kind of error `bin/llm.kb-validate` exists to catch mechanically instead.

**Provenance:** built ad hoc during the Abby's Craft `design.kb/` breakdown
(2026-07-09) to sanity-check ~150 hand-written cross-references across 83
files spanning a full mission→goals→requirements→design→components→
deliverables→future-work tower plus a discourse graph. Two bugs were
actually caught this way (a schema misplaced one directory too deep; a
`why:` link one `../` short) — cheap validation for what would otherwise be
silent rot the first time someone follows a stale link.

**Integration recommendation, in order of effort:**

1. **Cheapest, do first:** mention it from
   `references/creating-a-new-kb.md`'s "Pass 4: validation" step, which
   currently only says to run `bin/llm.kb-validate` — that pass's whole
   point is catching exactly this class of error, but the described tool
   doesn't yet.
2. **Real integration:** fold `frontmatter_links`/`body_links`/
   `broken_links` into `lib/python/llmd/frontmatter_validate.py` as a second
   check inside `validate_file()` (or a sibling `link_validate.py` module
   called from the same `main()`), so `bin/llm.kb-validate` reports both
   schema errors and broken links in one pass, one exit code. Would need:
   reusing that module's `extract_frontmatter` instead of the duplicate
   here, and deciding whether link-checking runs unconditionally or behind
   a flag (e.g. `--links`) since it's a different failure class than schema
   drift and some collections may have false positives — e.g. this script
   doesn't know about `skill://` URIs (see `frontmatter_validate.py`'s
   `SKILL_URI_SCHEME`), only relative-path links.
3. **Watch for false positives before flipping it on by default:** a link
   that's a deliberate forward-reference to a not-yet-created file (e.g. a
   `why:`/body link to a planned-but-unwritten deliverable) will report as
   broken even though it's intentional. The Abby's Craft tree has three of
   these (links to `ideas.md`, a file `project-bootstrap.md`'s own
   deliverable creates later). Either accept that as a real signal ("this
   file doesn't exist *yet*, go create it") or add a way to mark a link as
   a known-forward-reference.
