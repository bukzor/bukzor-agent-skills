# Hacking on llm-discourse-graph

## Project Structure

```
SKILL.md                    — The skill (what agents load)
schemas/                    — JSON Schema (draft-07) for each collection type
docs/dev/adr/               — Architecture decision records
docs/dev/devlog/            — Session-level development history
docs/dev/design/            — Living design documentation
docs/dev/technical-policy.kb/ — Cross-cutting normative guidance
```

## Adding a New Collection Type

1. Create `schemas/$NAME.jsonschema.yaml` following existing schemas
2. Add the collection to the table in `SKILL.md`
3. Write an ADR documenting the rationale
4. Update this file and `CLAUDE.md` if the change affects development workflow

## Modifying a Schema

- `additionalProperties: false` is intentional — it catches accidental fields
- Probability fields (`likelihood`) use 0-1 scale, default 1.0
- All cross-reference fields are `type: string` paths, not URIs

## Design Decisions

See [docs/dev/adr/](docs/dev/adr/) for architecture decision records.
