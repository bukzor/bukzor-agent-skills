# Decisions (2026-05-18)

## URI scheme for cross-skill references: `skill://`

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

## Architecture: stub-`$ref` first, data-side `$schema` later

Two architectures considered for eliminating per-project schema duplication:

- **A. Data-side `$schema`** — every todo.md frontmatter declares its schema
  directly; per-project `.claude/<X>.jsonschema.yaml` files deleted entirely.
  Maximum DRY, requires data-file migration and validator dispatch on `$schema`.
- **B. Stub `$ref`** — each project keeps a 1-line `.claude/<X>.jsonschema.yaml`
  that $refs the skill-owned source of truth. Editor tools (yaml-language-server)
  discover it via existing globs; existing data files unchanged.

**Decision: B first.** Strict improvement, no data-file migration, leverages
existing tooling. A is a nice-to-have layer that doesn't preclude B.

## Validator changes implied

- On startup, walk `~/.claude/skills/*/` for `*.jsonschema.yaml`; load and index
  by their declared `$id`.
- When resolving `$ref` with scheme `skill://`, do in-memory lookup by
  `$id`. No network fetch.
- Fallback if `$id` not found in index: filesystem path derived from authority
  + path (`~/.claude/skills/<authority>/<path>`).

## Open question reclassification

The original "remote `$ref` (http URLs)?" question is answered by
`skill://`: http resolution is no longer needed for the primary use
case — skills resolve in-memory. Remote `$ref` becomes a separate
future question, not a blocker.

## Drift-surface update (same day)

Schema gained two optional fields today (`cost-of-delay-2w` on `cost-benefit-sweh`,
and `confidence` on `sweh-value`). Each schema file grew from ~90 lines to ~140.
Six copies × ~50 added lines = the dup tax visibly worsened. This is itself an
urgency signal for re-rating this todo with the new `cost-of-delay-2w` field.
