# Devlog: 2026-07-07 -- canonical schemas out of skeleton; $ref propagation downstream

## Focus

Polish the $ref work (todo.kb 2026-02-09-000): the canonical todo/ideas
schemas lived inside `llm-subtask/skeleton/.claude/`, so every project
initialized from the skeleton got a full-copy *snapshot* that drifts.
Moved them to a new `llm-subtask/jsonschema/` (skill-root directory for
published, $ref-able schemas); the skeleton now ships the same one-line
`skill://` stub as every other consumer, so new projects are live-linked
from day one. All 8 in-repo stubs re-pointed; repo-root `.claude/`
gained its missing todo stub (immediately surfacing two
`managed-by`-less entries, backfilled).

## Decisions

### Keep the `jsonschema/` folder (vs skill-root placement)

Debated as possible YAGNI/clutter for two files. Kept: the URI
`skill://<skill>/jsonschema/<file>` is a self-describing published-schema
address and a discovery surface (`ls ~/.claude/skills/*/jsonschema/`);
root placement would false-trigger the `$CATEGORY.jsonschema.yaml`-
next-to-`$CATEGORY.kb/` adjacency convention. Follow-on noted: sweep
llm-discourse-graph and llm-design-kb `schemas/` dirs to `jsonschema/`
for name uniformity.

### Propagation policy: $ref-presence, not byte-equality

First pass archived the strict-schema-propagation migration as
superseded; user overruled -- downstream must keep receiving canonical
improvements. Renamed it `schema-propagation-from-canonical`
(status back to verified, `kind: recurring`, depends-on the new
`2026-07-07-000-schema-copies-to-ref-stubs` one-shot conversion) with a
relaxed invariant: consumers must *carry the canonical $ref*; extension
on top is allowed; mindful omission is not (illegible as intent -- a
different contract renames its category instead).

### $ref semantics verified: conjunction, not override

Scratch experiment (trash/, not committed; results recorded in the
propagation migration entry) against the real validator: `$ref` + sibling keywords conjoins (Draft 2020-12) -- narrow
yes, loosen never, and *extension is blocked today* by the canonical's
`additionalProperties: false`. Verified recipe for the first real
extension: canonical drops `additionalProperties: false`; consumers
close themselves with `unevaluatedProperties: false` (sees across $ref).

### yaml-language-server modeline on every schema file

`# yaml-language-server: $schema=https://json-schema.org/draft-07/schema`
as line 1 of canonicals and stubs: editor-side completion/validation for
the schema files themselves. Orthogonal to the `$schema:` dialect
keyword (briefly deleted in error, restored) and can't resolve
`skill://`. Documented in `references/schema-reuse.md`.

## Migration rollout

- `2026-07-07-000-schema-copies-to-ref-stubs` (one-shot, complete):
  SNAPSHOT/STALE-REF/DIVERGED classifier keyed on historical canonical
  blob hashes; stubbed template.python-project's stale copy;
  ideation.physical-musings's hand-rolled schema left (DIVERGED, real
  intent).
- `schema-propagation-from-canonical` (recurring): rewritten
  validate.sh (MISSING/NO-REF) + migrate.sh stubbed 19 MISSING schema
  files across 12 downstream `.claude/` dirs -- those kbs are validated
  for the first time.

## Verification

- pytest (llm-kb): 4 passed. `llm.kb-validate .`: 140 files, 0 errors.
- Both migrations' validate.sh: clean but for the one documented NO-REF
  judgment (ideation.physical-musings).
- Downstream spot-checks: litellm clean; ~15 files of pre-existing
  frontmatter nonconformance now *visible* -- deliberately not fixed
  (scope), captured in
  `.claude/todo.kb/2026-07-07-000-Downstream-todo-ideas-frontmatter-conformance-sweep.md`.

## Follow-up

- `schemas/` -> `jsonschema/` rename in llm-discourse-graph +
  llm-design-kb (todo.kb 2026-02-09-000 checkbox).
- Downstream frontmatter conformance sweep (dedicated todo above).
- `complete-example/` still doesn't demonstrate schema reuse
  (todo.kb 2026-02-09-000, unchanged).
