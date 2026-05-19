---
managed-by: Skill(llm-subtask)
required-reading:
  - ~/.claude/skills/llm.kb/references/schema-design.md
  - ~/.claude/skills/llm.kb/lib/python/llmd/frontmatter_validate.py
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
  benefit-2w:
    "@value": 1.0
    rationale: |
      Reduces schema duplication across kbs (esp. shared `why[]` field).
      Adoption is gradual; expect ~1h saved through reduced copy-paste
      and clearer cross-kb relationships.
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

- [ ] Add `$ref` resolution to `frontmatter_validate.py`
  - Resolve file-relative paths
  - Support `#/definitions/...` fragment syntax
  - Cache loaded schemas to avoid re-parsing
- [ ] Add tests for `$ref` resolution
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
- [ ] Validator resolves file-relative `$ref`
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

### URI scheme for cross-skill references: `agent-skill://`

For `$ref` and any other path-resolving cross-skill reference, use:

    agent-skill://<skill-name>/<path-within-skill>

Examples:

    $id:  agent-skill://llm-subtask/sweh.jsonschema.yaml
    $ref: agent-skill://llm-subtask/sweh.jsonschema.yaml

Rationale: anchors to Anthropic's **Agent Skills** open standard (released
2025-12-18, spec at agentskills.io, repo at github.com/agentskills/agentskills;
adopted by Microsoft VS Code/GitHub, OpenAI ChatGPT/Codex, Cursor, Goose,
OpenCode). The "agent-skill" qualifier disambiguates from other meanings of
"skill" (Alexa Skills, Semantic Kernel skills, etc.) and gives the URI scheme
a stable normative referent.

`Skill(<name>)` notation in human-facing fields like `managed-by:` stays as-is;
URIs only apply where path resolution matters.

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
- When resolving `$ref` with scheme `agent-skill://`, do in-memory lookup by
  `$id`. No network fetch.
- Fallback if `$id` not found in index: filesystem path derived from authority
  + path (`~/.claude/skills/<authority>/<path>`).

### Open question reclassification

The existing "Open Questions" section asked about remote `$ref` (http URLs)
support. With `agent-skill://`, http resolution is no longer needed for the
primary use case — skills resolve in-memory. Remote `$ref` becomes a separate
future question, not a blocker.

### Drift-surface update (today, 2026-05-18)

Schema gained two optional fields today (`cost-of-delay-2w` on `cost-benefit-sweh`,
and `confidence` on `sweh-value`). Each schema file grew from ~90 lines to ~140.
Six copies × ~50 added lines = the dup tax visibly worsened. This is itself an
urgency signal for re-rating this todo with the new `cost-of-delay-2w` field.
