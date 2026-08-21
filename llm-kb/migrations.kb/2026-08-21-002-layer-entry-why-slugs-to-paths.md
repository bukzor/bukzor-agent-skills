---
status: in-progress
kind: one-shot
scope: |
  Every design.kb layer collection in the user's tree -- 15 towers
  carrying 574 `why:` refs, under 4 invented schema names and 3 reference
  systems (file-relative paths, bare slugs, tower-root-relative paths).
  Two coupled changes, in this order:

  1. Instance data: every `why:` item becomes a file-relative path ending
     in `.md`. Slug-style items are rewritten (har-browse 63 refs,
     llm-vitals 61, chatfs 39, fuser-vfs 33, mitmproxy 21, chatfs-cli 16),
     as are tower-root-relative ones (sttt-engine 35, template-py 3).
     Empty `why:` lists are left alone -- `[]` is the field's default and
     is legal.

     One rider, in the chatfs tower only: its shared 040 schema typed
     `last-updated` as a `format: date` string, so the three entries
     carrying that field are unquoted to match the house `type: date`.
     Without it the tower cannot bind the canonical and stay green --
     one entry already wrote its date unquoted and was failing.
  2. Schemas: each tower's per-layer schema becomes a stub onto
     `skill://llm-design-kb/jsonschema/layer-entry.jsonschema.yaml`, or --
     for a motivated layer or one with project-local fields -- a 3-line
     `#base` extender.

  Excluded: tower roots (`010-mission`) and auxiliary collections
  (`use-cases.kb/`, `background.kb/`, ...). They are not layer entries and
  do not bind this schema.

  Excluded: the decision-lifecycle trio (`status` / `blocked-on` /
  `superseded-by`), three hand-synced copies deliberately left out of the
  layer-entry canonical because `status` alone is four incompatible enums
  under one name. Its own canonical is an open question.
depends-on:
  - 2026-08-21-000-schema-copies-to-ref-stubs-all-categories.md
related-todo: ~/.claude/skills/llm-kb/.claude/todo.kb/2026-08-21-000-ref-rollout-beyond-todo-ideas.md
why: |
  Separate from 2026-08-21-000 because the ordering is intrinsic: this is
  the one cluster whose copies do not already conform, so stubbing before
  the data edit would simply turn 12 towers red. It also rewrites *instance
  data*, which no other entry in this arc does.

  The slug-vs-path split is the substantive finding. Twelve independent
  restatements of "a layer entry has upward motivation edges" produced four
  reference systems, and the survey's own reading of har-browse was wrong
  (slugs, not paths). Paths survive entry promotion to sub-kbs and resolve
  mechanically for link checking; slugs do neither. `pattern: '\.md$'`
  accepts every observed path reference and rejects every observed slug,
  so the classifier is exact rather than heuristic.

  Ratified 2026-08-21 with one amendment: the canonical's proposed
  `minItems: 1` on `why` was struck. An empty list is the field's default,
  and a schema that rejects its own default is incoherent. Cardinality was
  the wrong check anyway -- the one worth having is filesystem existence of
  each referenced path, which a future dedicated path type will enforce.
---

# Layer-entry `why:` slugs to paths

## Transformation

Phase 1, data. For each layer entry with a `why:` list, rewrite any item
that does not end in `.md` as the file-relative path to the entry it
names. The mapping is mechanical where slugs are unique within the tower;
report ambiguous slugs rather than guessing.

Phase 2, schemas. Replace each tower's per-layer schema with the smallest
of the three forms documented in the canonical's own description: exact
root `$ref`, `#base` + `required: [why]` for a motivated layer, or `#base`
+ local properties + `unevaluatedProperties: false` for an extension.

Idempotent: phase 1 is a no-op once every item ends in `.md`; phase 2
rewrites to a fixed target.

## Validation

`validate.sh` should report, per tower: items not ending in `.md`, and
`why:` targets that do not resolve to an existing file. The second check is
new capability -- no schema could express it, which is part of why the
drift went unnoticed, and it is the eventual home of a dedicated path type
with enforced filesystem existence.

## Applied so far

Phase 1, data, complete: 268 of 271 non-conforming refs rewritten across
175 files in 8 towers (har-browse 63, llm-vitals 61, chatfs 39, sttt-engine
35, fuser-vfs 33, mitmproxy 21, chatfs-cli 16, template-py 3). The other
7 towers already conformed. Idempotency demonstrated, not asserted: a
second `migrate.sh` run produced no output and left every file
byte-identical.

Phase 2, schemas, complete: every layer-binding schema in all 13 towers
whose layer entries carry frontmatter now consumes the canonical. Exact
root `$ref`: none -- no layer wanted the plain shape. `#base` +
`required: [why]`: mitmproxy 020/040 and its 040 sub-kb, claude-empty
020/040, har-browse 020-070, chatfs 020/030/070, meta-dd
goals/deliverables/non-goals. `#base` +
local properties: chatfs 040 (`background`/`source`/`last-updated`),
har-browse 070 sub-kb, design-next 020/030/040/070 and llm-vitals
020-070 and llm-triggers 040 (lifecycle trio), summer 020-060 and
template-py 020 (`tags`), physical-musings 020/030
(`status`/`ratified`/`cluster`). Extender: meta-fs2's local layer-entry
file, which re-anchors `base` onto the canonical's and adds `aliases`.
Three now-unreferenced local `why` units deleted (meta-fs2, design-next,
har-browse), along with mitmproxy's whole local `why-linked-entry` schema;
meta-dd's `why` unit became a `#why` stub instead, since its tower root
still binds it.

Not touched, by exclusion: tower roots (`010-mission*`), auxiliary
collections (`use-cases.kb/`, `discovered-constraints.kb/`, ...), summer's
010 and 070 (070 deliberately carries no `why:`), and the lifecycle trio,
whose `superseded-by` stays slug-shaped in llm-vitals. git-partial's
`integration-patterns.kb/` stays schemaless too: an auxiliary collection
keyed on `constraints:`, not a layer.

sttt-engine and fuser-vfs had no schemas at all, and their 020-060 entries
were failing validation for want of one. Every such entry carries `why:`,
so each layer gained the same `#base` + `required: [why]` binding as every
other motivated layer -- 10 new files, 43 errors cleared.

Residual, needing a decision rather than a script: three refs naming the
slug `canonical-conversation-graph`, which exists at both
`030-requirements.kb/` and `040-design.kb/` of
`prototype.chatfs/docs/dev/design.kb`. Left as slugs and visible as
validator errors, in
`docs/dev/design.kb/040-design.kb/rotate-90-degrees-layout.md` and
`packages/chatfs-cli/design.kb/040-design.kb/{chat-as-directory,no-partial-synthesis}.md`.
