# Schema Design

JSON Schema Draft 07 in YAML for frontmatter validation.

## Multiple Patterns in One Directory

Use `oneOf` when files can have different valid frontmatter structures:

```yaml
oneOf:
  - required: [provider, models]      # Pattern 1: Cloud providers
    properties:
      provider: {type: string}
      models: {type: array}

  - required: [category, privacy]     # Pattern 2: Local models
    properties:
      category: {const: "Local Model Support"}
      privacy: {type: string}
```

## Useful Constraints

```yaml
license:
  enum: [MIT, Apache-2.0, Proprietary]  # Prevent typos

repository:
  format: uri  # Validate URLs

date:
  type: date  # YAML parses ISO dates (2024-03-10) as date objects

additionalProperties: false  # Strict validation recommended
```

`type: date` (and `type: instant`, tz-aware datetime) are llmd dialect
extensions, not stock JSON Schema. A schema using them must either declare
`$schema: "skill://llm-kb/jsonschema/dialect.jsonschema.yaml"` or declare no
`$schema` at all (absent means the llmd dialect). Under a stock dialect
declaration these types are unknown, and validation reports the schema bug.

## Reuse Across Files

Sharing a definition (or a whole schema) across multiple `.jsonschema.yaml`
files is a separate concern from single-file design -- see
`references/schema-reuse.md` for the `$ref` patterns.

## Evolution

- Add optional fields: Safe
- Add required fields: Must update all existing files
- Change enums: May break files

Start minimal, expand as useful fields emerge.
