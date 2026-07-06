---
managed-by: Skill(llm-subtask)
required-reading:
  - ~/.claude/skills/llm-kb/references/schema-design.md
  - ~/.claude/skills/llm-kb/lib/python/llmd/frontmatter_validate.py
suggested-reading:
  - https://json-schema.org/understanding-json-schema/structuring.html
related-effort: ~/.claude/skills/llm-collab/.claude/todo.kb/2026-02-09-000-design-kb-pattern-for-living-design-docs.md
cost-benefit-sweh:
  timebox:
    "@value": 1.0
    rationale: |
      Pattern definition + a couple working examples. Beyond 1h you're
      designing tooling; spike on real adoption first to learn what's
      actually needed.
    confidence: unsure
  benefit-2w:
    "@value": 1.0
    rationale: |
      Reduces schema duplication across kbs (esp. shared `why[]` field).
      Adoption is gradual; expect ~1h saved through reduced copy-paste
      and clearer cross-kb relationships.
    confidence: unsure
  cost-of-delay-2w:
    "@value": 1.5
    rationale: |
      Six copies of the SWEH schema (per `sweh-schema-source.md` in
      homedir-archeology `reference.kb/`) hand-propagate every field
      change. The 2026-05-18 expansion (`cost-of-delay-2w` +
      `confidence`) added ~50 lines × 6 files = ~300 lines of new
      duplicate text — the dup tax visibly worsened.

      During the active backlog re-rate sweep, expect 2-4 schema edits
      over 2 weeks. Each propagation costs ~0.2 SWEh of mechanical
      copying plus drift-risk when a copy is missed. 1.5 SWEh budgets
      ~3 events × 0.3 SWEh plus a forgotten-file tax.
    confidence: unsure
---

# Schema Reuse with $ref

**Priority:** Medium
**Complexity:** Medium
**Context:** Emerged from design.kb pattern work; needed for shared `why[]` field across abstraction levels

## Problem Statement

llm.kb lacks support for reusable schema definitions. Projects with multiple `.kb/` directories that share common fields (e.g., `why[]` for traceability) must duplicate schema definitions. This causes:
1. Inconsistency risk when updating shared fields
2. Verbose schemas
3. No single source of truth for cross-cutting frontmatter

## Current Situation

- `references/schema-design.md` covers `oneOf`, constraints, evolution -- no `$ref`
- `frontmatter_validate.py` does basic validation, doesn't resolve `$ref`
- `complete-example/` shows duplication (status+budget in both decorations and food schemas)
- No documented pattern for shared schema directory

## Proposed Solution

### Directory Pattern

Place shared schemas at a level encompassing all usages:

```
docs/dev/
├── jsonschema/
│   └── common.yaml           # Shared definitions
├── design/
│   ├── 020-goals.jsonschema.yaml    # $ref: ../jsonschema/common.yaml
│   └── 030-requirements.jsonschema.yaml
└── technical-policy.jsonschema.yaml  # $ref: jsonschema/common.yaml
```

### Schema Structure

```yaml
# jsonschema/common.yaml
$schema: "http://json-schema.org/draft-07/schema#"
definitions:
  why:
    description: Links to parent items in abstraction stack
    type: array
    items:
      type: string
```

```yaml
# design/020-goals.jsonschema.yaml
$schema: "http://json-schema.org/draft-07/schema#"
type: object
properties:
  why:
    $ref: "../jsonschema/common.yaml#/definitions/why"
```

### Tool Compatibility

Design for yaml-language-server compatibility:
- File-relative `$ref` paths
- Standard Draft-07 `$schema`
- Inline directive support: `# yaml-language-server: $schema=...`

## Implementation Steps

### Documentation

- [ ] Add `references/schema-reuse.md` covering:
  - `$ref` syntax and file-relative paths
  - `definitions` block for reusable fragments
  - Directory placement pattern (`jsonschema/` at encompassing level)
  - yaml-language-server compatibility
- [ ] Update `references/schema-design.md` to reference new doc
- [ ] Add cross-reference in SKILL.md references section

### Validator Enhancement

- [x] Add `$ref` resolution to `frontmatter_validate.py`
  - [x] Resolve file-relative paths
  - [x] Support `#/definitions/...` fragment syntax (via `referencing`'s
        default `Registry` behavior, no custom code needed)
  - [x] Cache loaded schemas to avoid re-parsing (`lru_cache` on
        `_retrieve_schema`)
- [x] Add tests for `$ref` resolution
- [ ] Handle circular reference detection (or document as unsupported)

### Example Update

- [ ] Refactor `complete-example/` to demonstrate schema reuse
  - Extract shared `status`+`budget` to common schema
  - Update food and decorations schemas to use `$ref`

## Open Questions

- Should validator support remote `$ref` (http URLs) or only file-relative?
- How to handle `$ref` in `oneOf` blocks?
- Should we support `allOf` for schema composition?

## Success Criteria

- [ ] `references/schema-reuse.md` exists and is comprehensive
- [x] Validator resolves file-relative `$ref`
- [ ] `complete-example/` demonstrates the pattern
- [ ] yaml-language-server works with the pattern (manual verification)

## Drift surface (2026-05-15)

The SKELETON-DEFAULT pattern (canonical schema in
`llm-subtask/skeleton/.claude/`, hand-copied to each consuming skill's
`.claude/`) now has three live copies of `ideas.jsonschema.yaml` and two
of `todo.jsonschema.yaml`. Drift risk is real until `$ref` lands.
Affected paths:

- `llm-subtask/skeleton/.claude/ideas.jsonschema.yaml` (canonical)
- `llm-subtask/skeleton/.claude/todo.jsonschema.yaml` (canonical)
- `llm-kb/.claude/ideas.jsonschema.yaml` (copy)
- `llm-subtask/.claude/ideas.jsonschema.yaml` (copy)
- `llm-collab/.claude/todo.jsonschema.yaml` (copy)

Resolution path: implement `$ref` resolution, then convert each copy to a
single-line `$ref` pointer.

## Decisions (2026-05-18)

### URI scheme for cross-skill references: `skill://`

The scheme grammar, rationale, resolution contract, and scope evolution
are recorded in the ADR
`skill://llm-kb/docs/adr/2026-05-18-000-skill-uri-scheme.md`.

The `$ref`/`$id` work below uses the path-bearing form
`skill://<skill-name>/<path-within-skill>`, e.g.
`$ref: skill://llm-subtask/sweh.jsonschema.yaml`.

(The 2026-05-18 stance that `Skill(<name>)` stays in human-facing fields
was broadened 2026-05-27 -- all skill references now use the URI, swept by
`skill://llm-kb/migrations.kb/2026-05-27-000-skill-notation-to-skill-uri.md`.
Renamed 2026-07-05 from `agent-skill://` to `skill://` -- see the ADR.)

### Architecture: stub-`$ref` first, data-side `$schema` later

Two architectures considered for eliminating per-project schema duplication:

- **A. Data-side `$schema`** — every todo.md frontmatter declares its schema
  directly; per-project `.claude/<X>.jsonschema.yaml` files deleted entirely.
  Maximum DRY, requires data-file migration and validator dispatch on `$schema`.
- **B. Stub `$ref`** — each project keeps a 1-line `.claude/<X>.jsonschema.yaml`
  that $refs the skill-owned source of truth. Editor tools (yaml-language-server)
  discover it via existing globs; existing data files unchanged.

**Decision: B first.** Strict improvement, no data-file migration, leverages
existing tooling. A is a nice-to-have layer that doesn't preclude B.

### Validator changes implied

- On startup, walk `~/.claude/skills/*/` for `*.jsonschema.yaml`; load and index
  by their declared `$id`.
- When resolving `$ref` with scheme `skill://`, do in-memory lookup by
  `$id`. No network fetch.
- Fallback if `$id` not found in index: filesystem path derived from authority
  + path (`~/.claude/skills/<authority>/<path>`).

### Open question reclassification

The existing "Open Questions" section asked about remote `$ref` (http URLs)
support. With `skill://`, http resolution is no longer needed for the
primary use case — skills resolve in-memory. Remote `$ref` becomes a separate
future question, not a blocker.

### Drift-surface update (today, 2026-05-18)

Schema gained two optional fields today (`cost-of-delay-2w` on `cost-benefit-sweh`,
and `confidence` on `sweh-value`). Each schema file grew from ~90 lines to ~140.
Six copies × ~50 added lines = the dup tax visibly worsened. This is itself an
urgency signal for re-rating this todo with the new `cost-of-delay-2w` field.

### Drift-surface update (2026-05-21)

Six schema files are now **byte-identical** (md5 `91c4d226…`): skeleton's
`todo.jsonschema.yaml` and `ideas.jsonschema.yaml`, plus the four downstream
copies (`llm-subtask/.claude/ideas`, `llm-kb/.claude/{todo,ideas}`,
`llm-collab/.claude/todo`). Previously there were two hash families
(skeleton-with-`managed-by`-const vs skill-local-without); the
strict-`managed-by`-propagation session collapsed both into one. Each file is
now ~200 lines (added `status`, `required-reading`, `suggested-reading`,
`related-effort` and flipped `additionalProperties: false`).

Implication for `$ref` work: any further field addition now requires **six
hand-edits** instead of the prior two-shape surgery. Drift pressure is
strictly worse per change. The mitigation is unchanged — implement
stub-`$ref` resolution (decision B above) and collapse the five downstream
copies into one-line pointers at `llm-subtask/skeleton/.claude/`.

Inventory diverges from the 2026-05-15 list: that section enumerated five
paths, omitting `llm-kb/.claude/todo.jsonschema.yaml` (which has lived in
the repo since `6a2c361`, the original centralization commit). The actual
count was six all along; today's session updated all six in lockstep.

## Progress (2026-07-05)

Wired the `skill://` resolver (`_retrieve_skill`/`_REGISTRY`, drafted in an
earlier uncommitted pass) into `KbValidator` by passing `registry=_REGISTRY`
in `validate_against_schema`. Proven red-green with a new pytest suite
(`frontmatter_validate_test.py`, `DescribeSkillRefResolution`) — first
observed `referencing.exceptions.Unresolvable` before the wiring, then green
after. `llm-kb/pyproject.toml` + `uv.lock` added so the skill has its own
pytest-capable venv (none existed before).

Converted all seven downstream stub copies to real one-line `$ref`s at the
skeleton (skeleton files themselves untouched, still canonical):

- `todo.jsonschema.yaml`: llm-kb, llm-collab, llm-subtask, llm-must-read-kb
- `ideas.jsonschema.yaml`: llm-kb, llm-collab, llm-subtask

Each conversion verified against real `.claude/{todo,ideas}.kb/` data
(0 errors) before moving to the next, and against a deliberately-broken
frontmatter file (confirmed the stub still rejects bad data, not just
passing everything silently).

Still open: file-relative `$ref` (only `skill://` resolves today; a bare
`../foo.yaml` or `./foo.yaml#/definitions/x` next to a schema is untested),
circular-ref handling, `references/schema-reuse.md`, `complete-example/`
refactor.

### File-relative `$ref`: confirmed gap, fix identified (2026-07-05)

Reproduced the failure directly: a schema with
`$ref: "../jsonschema/common.yaml#/definitions/why"`, loaded and validated
via the real `validate_against_schema`, raises

    _WrappedReferencingError: Unresolvable: ../jsonschema/common.yaml#/definitions/why

**Fragment resolution (`#/definitions/...`) itself is free** — `referencing`
does RFC 3986 relative-URI resolution (`urljoin` against a base) and
JSON-Pointer fragments natively, confirmed with a synthetic `file://`
example outside the validator. The gap is that our validator never gives a
loaded schema a base URI to resolve *against*:

1. `load_schema()` just `yaml.safe_load`s the path — no `$id`, so
   `self._base_uri == ''`. `urljoin('', '../jsonschema/common.yaml')`
   yields the same bare relative string, which nothing knows how to fetch.
2. `_retrieve_skill()` only handles `skill://` URIs (raises `ValueError`
   otherwise) — even with a base URI, a resolved `file://...` URI wouldn't
   be retrievable.

**Fix, two small additions, same TDD pattern as the `skill://` work:**

- In `load_schema()` (or just before validating), inject
  `$id: <absolute file:// URI of the schema's own path>` when the loaded
  dict doesn't already declare one — gives relative refs a base to resolve
  against.
- Extend the retrieve callback to also handle `file://` URIs (read straight
  off disk), since a resolved relative ref comes back as an absolute
  `file://...` URI via `urljoin`. Likely cleanest as one retrieve function
  dispatching on URI scheme (`skill://` vs `file://`) rather than two
  separate registries.

Not yet implemented — reproduction and root-cause only. Next session should
red-green this the same way: write the failing file-relative test above,
add the `$id`-injection + `file://` retrieval, confirm green.

## Progress (2026-07-05, continued)

Implemented per the plan above: `load_schema()` now injects a `file://`
`$id` (the schema's own absolute path) when one isn't already declared;
`_retrieve_skill()` was renamed `_retrieve_schema()` and dispatches on URI
scheme (`skill://` vs `file://`) rather than only handling `skill://`.
Red-green confirmed — the file-relative test
(`DescribeFileRelativeRefResolution`) failed with exactly the predicted
`Unresolvable: common.yaml#/definitions/why` error before the fix, passed
after. Full suite (3 tests) green; `bin/llm.kb-validate .` against the
real repo still reports 0 errors across all 65 files (no regression).

Still open: circular-ref handling, `references/schema-reuse.md`,
`complete-example/` refactor. Those three are independent of each other —
any can go next.
