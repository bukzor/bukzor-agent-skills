# Schema Reuse with `$ref`

## Default: one reusable unit per file, whole-file `$ref`

When a schema fragment is shared across files, give it its own file and
`$ref` the whole thing -- no `definitions:` wrapper, no `#/...` fragment:

```yaml
# why.jsonschema.yaml
description: Links to parent items in abstraction stack
type: array
items: {type: string}
```

```yaml
# goals.jsonschema.yaml
type: object
properties:
  why:
    $ref: "why.jsonschema.yaml"
  title:
    type: string
```

Prefer this over co-locating several reusable pieces as named entries under
one shared `definitions:` file. Whole-file `$ref` means adding a new shared
definition is a new file, not an edit to a file other consumers also
depend on -- fewer merge conflicts when multiple agents touch schemas
concurrently, and a `git log` on the file is the history of that one
definition, not an interleaving of unrelated ones.

This also covers reusing a whole category schema, not just one field --
e.g. a project whose `todo.jsonschema.yaml` is *entirely* someone else's
canonical schema is a one-line stub:

```yaml
$ref: "skill://llm-subtask/jsonschema/todo.jsonschema.yaml"
```

Real examples: `llm-kb/.claude/todo.jsonschema.yaml`,
`llm-collab/.claude/todo.jsonschema.yaml`,
`llm-subtask/.claude/ideas.jsonschema.yaml` -- all one-line stubs pointing at
`llm-subtask/jsonschema/{todo,ideas}.jsonschema.yaml`, the canonical
source. Editing the canonical file changes validation everywhere in one
place; no propagation, no drift.

Canonical schemas live in a `jsonschema/` directory at the *skill root*,
never inside a `skeleton/` -- skeleton contents get copied into projects, and
a copied full schema is a snapshot that drifts. The skeleton holds the same
one-line stub, so a project initialized from it is live-linked to the
canonical schema from day one.

## Two ways to point at the file

### File-relative (same project)

`$ref: "why.jsonschema.yaml"`, resolved relative to the `$ref`-ing file's
own location -- `../jsonschema/why.jsonschema.yaml` and
`./why.jsonschema.yaml` both work the same way. This is RFC 3986
relative-reference resolution against the schema's base URI.

`frontmatter_validate.py`'s `load_schema()` makes this possible: it injects
a `file://<absolute path>` `$id` into every loaded schema that doesn't
already declare one. Without a base URI, a bare relative string like
`why.jsonschema.yaml` has nothing to resolve against and raises
`Unresolvable`. `_retrieve_schema()` then serves the resolved `file://...`
URI straight off disk.

Use this for reuse *within* a project.

**Directory placement:** put shared files in a `jsonschema/` subdirectory at
the level encompassing all their consumers -- not next to any one of them,
which would misleadingly imply that consumer owns it. Name each file for
what it defines, not for its role (`why.jsonschema.yaml`, not
`common.jsonschema.yaml` -- "common" says nothing about content, same
failure mode as `misc`):

```
docs/dev/
├── jsonschema/
│   └── why.jsonschema.yaml           # shared `why:` definition
├── design/
│   ├── 020-goals.jsonschema.yaml     # $ref: ../jsonschema/why.jsonschema.yaml
│   └── 030-requirements.jsonschema.yaml
└── technical-policy.jsonschema.yaml  # $ref: jsonschema/why.jsonschema.yaml
```

This is the prescribed placement, not a description of existing usage --
file-relative `$ref` only started resolving with this session's fix, so no
project has grown into this shape yet. Follow it from the first schema
split rather than waiting for one to accumulate organically.

### `skill://` (across skills)

`$ref: "skill://llm-subtask/why.jsonschema.yaml"` -- authority is the skill
name, path is the file within that skill's root. Resolved in-memory via
`~/.claude/skills/<skill>/<path>` (a symlink farm onto this repo, so it also
transparently resolves same-repo cross-skill refs). No network fetch either
way. See the ADR (`llm-kb/docs/dev/adr/2026-05-18-000-skill-uri-scheme.md`) for
the scheme's full rationale.

Use this when the shared definition is owned by a *different* skill.

## Fragments: only for reusing one entry out of a topically-cohesive file

Sometimes several definitions genuinely belong in one file because the file
*is* the topic, not a junk drawer -- an `animals.jsonschema.yaml` holding
`mammal` and `bird` as animal classes, say:

```yaml
# animals.jsonschema.yaml
$defs:
  mammal:
    type: object
    properties:
      legs: {const: 4}
      fur: {const: true}
  bird:
    type: object
    properties:
      legs: {const: 2}
      feathers: {const: true}
```

A petting-zoo schema wants specific animals, not the taxonomy file itself,
so it points at one entry each:

```yaml
# petting-zoo.jsonschema.yaml
type: object
properties:
  goat:
    $ref: "animals.jsonschema.yaml#/$defs/mammal"
  chicken:
    $ref: "animals.jsonschema.yaml#/$defs/bird"
```

The `#/$defs/<name>` fragment is a standard JSON Pointer; `referencing`
(the library `frontmatter_validate.py` uses) resolves it natively, no custom
code needed.

The test to apply before reaching for this over one-file-per-definition:
would splitting `mammal` and `bird` into their own files lose something?
Here, yes -- they're two entries in one real taxonomy, not two unrelated
things sharing a file of convenience. If you can't articulate what the
grouping *is* beyond "things schemas share," it's the junk-drawer pattern
in disguise -- split it instead (see "Default" above).

A real (less kindergarten) instance of the same shape: `sweh-value` lives
in `llm-subtask/jsonschema/todo.jsonschema.yaml`'s `$defs:` -- an entry in
one cohesive "todo/idea task metadata" schema, addressable as
`$ref: "skill://llm-subtask/jsonschema/todo.jsonschema.yaml#/$defs/sweh-value"`.

## Extending a canonical schema: strict root, open `#base`

A canonical schema publishes *two* entry points from one file, with zero
duplication -- the strict root is built from the open base by conjunction:

```yaml
# canonical.jsonschema.yaml
$schema: https://json-schema.org/draft/2020-12/schema
$defs:
  base:
    $anchor: base
    type: object
    properties: { ... }        # all the content, no closure
    required: [ ... ]
$ref: "#/$defs/base"
unevaluatedProperties: false   # the strictness, stated once
```

Consumers choose an entry point, and the choice is legible in their
`$ref`:

```yaml
# exact conformance (the default; the usual one-line stub)
$ref: "canonical.jsonschema.yaml"
```

```yaml
# extension: base + local fields, closed locally
$ref: "canonical.jsonschema.yaml#base"
properties:
  project-field: {type: string}
unevaluatedProperties: false
```

Why this shape works (all verified by experiment against the real
validator, 2026-07-08; recorded in
`llm-kb/migrations.kb/2026-05-15-000-schema-propagation-from-canonical.md`):

- Under Draft 2020-12, `$ref` + sibling keywords is *conjunction* -- an
  extender can add fields or narrow constraints, never loosen. (Under
  draft-07, siblings of `$ref` are silently *ignored* -- the strict root
  would be dead text. This convention requires the 2020-12 dialect.)
- `additionalProperties: false` can't see through `$ref`, so it would
  reject even the canonical's own fields when used beside one;
  `unevaluatedProperties: false` sees across `$ref`, which is what lets
  both the strict root and extenders close over inherited fields.
- The strict entry point is closed *in the canonical*, not in each stub --
  a stub can't forget its closure, and plain stubs stay one `$ref` line.
- `#base` is a Draft 2020-12 `$anchor`; the JSON-Pointer form
  `#/$defs/base` resolves identically. Both work file-relative and
  through `skill://`.

Canonical instances: `llm-subtask/jsonschema/{todo,ideas}.jsonschema.yaml`.

## yaml-language-server compatibility

Partial, not full. A generic YAML/JSON-Schema tool (yaml-language-server,
IDE plugins) resolves plain file-relative `$ref`s out of the box -- it
already treats a schema file's own location as the implicit base URI, the
same behavior our `$id` injection gives `frontmatter_validate.py`.

`skill://` is a custom scheme that only `frontmatter_validate.py`'s
`_retrieve_schema()` understands. A generic tool sees an unresolvable URI
and either errors or silently gives up on validating through that `$ref` --
there is no editor-side resolver for it today. Prefer file-relative `$ref`
when editor-time validation matters more than avoiding a project-local copy;
use `skill://` (or the stub-file pattern) when eliminating duplication
matters more.

What *does* work everywhere is the yaml-language-server modeline, first
line of any `*.jsonschema.yaml` (canonical or stub):

```yaml
# yaml-language-server: $schema=https://json-schema.org/draft/2020-12/schema
```

Declare the meta-schema matching the keywords the file uses: canonicals
and extenders use 2020-12 keywords (`$anchor`, `unevaluatedProperties`),
so they declare 2020-12; a plain one-line stub uses only `$ref`, identical
in every dialect, so it keeps draft-07 -- which currently gets better
editor support.

It declares the schema *of the file itself* -- the JSON-Schema meta-schema --
so editing schema files gets keyword completion and validation. This is
orthogonal to the `$schema:` keyword inside the document (which declares the
dialect to validators) and to `$ref` resolution: the modeline can't make an
editor follow `skill://`.

## Circular `$ref`

Two schema files that `$ref` each other (a genuine cycle in the schema
graph) validate correctly, with no special handling. `referencing` resolves
`$ref` lazily, per validated instance node, rather than eagerly flattening
the schema graph -- a cycle among schema *files* is harmless as long as the
*instance data* is finite, which JSON/YAML instance data always is. Verified
directly against `frontmatter_validate.py`'s real validation path; see the
"Circular-ref finding" entry in
`llm-kb/.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md`.
