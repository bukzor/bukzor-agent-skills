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
  # a calendar day; `instant` is the tz-aware-timestamp counterpart
  $ref: "skill://llm-kb/jsonschema/date.jsonschema.yaml"

additionalProperties: false  # Strict validation recommended
```

`date` and `instant` (a tz-aware datetime) are llmd dialect extensions, not
stock JSON Schema, so a schema writing `type: date` inline owes a
`$schema: "skill://llm-kb/jsonschema/dialect.jsonschema.yaml"` declaration --
under a stock dialect the type is unknown and validation reports the schema
bug. `$ref` the shared unit instead and the question does not arise: the
declaration lives once, in the unit, and a `$ref` crossing re-selects the
dialect from the resource it lands in.

## Reuse Across Files

Sharing a definition (or a whole schema) across multiple `.jsonschema.yaml`
files is a separate concern from single-file design -- see
`references/schema-reuse.md` for the `$ref` patterns.

## Evolution

- Add optional fields: Safe
- Add required fields: Must update all existing files
- Change enums: May break files

Start minimal, expand as useful fields emerge.
