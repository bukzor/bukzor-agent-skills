--- # workaround: anthropics/claude-code#13003
depends:
    - skills/llm-collab
---

# llm-discourse-graph — Development Guide

## Quick Reference

**Adding a collection type:** Requires a new schema in `schemas/`, updates to SKILL.md, and an ADR. → See [HACKING.md](HACKING.md)

**Understanding the five collections:** Questions, claims, deductions, sources, definitions. → See [SKILL.md](SKILL.md)

**Design decisions:** → See [docs/dev/adr/](docs/dev/adr/)

## Architecture Overview

A Claude Code skill defining a file-per-node epistemic knowledge graph format.
No runtime code — the deliverable is documentation (SKILL.md) and schemas
(`schemas/*.jsonschema.yaml`) that teach agents how to create and maintain
discourse graphs. Built on the `llm.kb` nesting convention.

## Key Files

- `SKILL.md` — The skill itself; loaded when agents use discourse graphs
- `schemas/*.jsonschema.yaml` — Five JSON Schemas governing frontmatter
- `docs/dev/adr/` — Design decisions (collection types, scoping, terminology)

## Conventions

- Schemas use `additionalProperties: false` — strict field governance
- `likelihood` fields use 0-1 scale, default 1.0 (certain until told otherwise)
- Cross-references are collection-relative paths with lexical scoping

## Testing

No automated tests yet. Validate schemas with any JSON Schema draft-07 tool.
