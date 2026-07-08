# Progress (2026-07-07): canonical schemas out of skeleton

The skeleton was the wrong home for canonical schemas: skeleton contents
get *copied* into new projects, minting a fresh drifting snapshot per
init. Moved `skeleton/.claude/{todo,ideas}.jsonschema.yaml` to
`llm-subtask/jsonschema/` (new skill-root directory for published,
`$ref`-able schemas); the skeleton now ships the same one-line
`skill://` stub as everyone else, so initialized projects are
live-linked from day one. All 8 in-repo stubs re-pointed at
`skill://llm-subtask/jsonschema/`; repo-root `.claude/` gained its
missing todo stub (which immediately surfaced two `managed-by`-less
entries -- backfilled).

Kept the `jsonschema/` folder over skill-root placement, deliberately:
it's a discovery surface (`ls ~/.claude/skills/*/jsonschema/` = every
published schema), avoids false `$CATEGORY.jsonschema.yaml`-next-to-data
adjacency semantics, and is where future single-unit extractions
(e.g. `sweh.jsonschema.yaml`) land.

yaml-language-server modeline
(`# yaml-language-server: $schema=https://json-schema.org/draft-07/schema`)
added as line 1 of every canonical schema and stub -- editor-side
completion/validation for the schema files themselves; documented in
`references/schema-reuse.md`.

Downstream sweep is now two migrations:
`llm-kb/migrations.kb/2026-07-07-000-schema-copies-to-ref-stubs.md`
(one-shot: copies become stubs) and the renamed
`2026-05-15-000-schema-propagation-from-canonical.md` (recurring guard,
policy relaxed from byte-equality to $ref-presence; extension allowed,
omission not). Swept ~/repo: `template.python-project`'s stale copy
stubbed; 19 MISSING schemas stubbed across 12 downstream projects;
`ideation.physical-musings`'s hand-rolled todo schema is the one open
NO-REF judgment. Data nonconformance surfaced by the new stubs:
`todo.kb/2026-07-07-000-Downstream-todo-ideas-frontmatter-conformance-sweep.md`.
