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

## Defaults

A schema describes the data a consumer receives, not the text an author
types. `default:` states what an absent key means to that consumer. The
fleet validator does not materialize defaults, so nothing in-house will
catch a default the schema itself rejects -- coherence is on the author.
The test is mechanical: substitute the default for the absent key and
re-validate in your head. A schema must accept the materialized form of
its own default, because a consumer that fills defaults and round-trips
the object would otherwise emit a document the schema rejects.

```yaml
todo:
  const: true    # authors only ever type `todo: true`...
  default: false # ...but the materialized form fails validation
```

fails the test -- it models the author's keystrokes, not the consumer's
data. So does `minItems: 1` with `default: []`. Correct:

```yaml
todo:
  type: boolean
  default: false
```

A default naming one branch of a `oneOf` or `enum` passes -- the
materialized form is a branch -- and is the house pattern for graded
fields (`force: default: should` in
`llm-claims-kb/jsonschema/policy.jsonschema.yaml`).

Choose the default so that *absent* means what every existing file
already means, and the new field costs no migration: `verdict:` and
`todo:` in `llm-claims-kb/jsonschema/claim.jsonschema.yaml` shipped into
a populated corpus without touching a file.

## Reuse Across Files

Sharing a definition (or a whole schema) across multiple `.jsonschema.yaml`
files is a separate concern from single-file design -- see
`references/schema-reuse.md` for the `$ref` patterns.

## Evolution

- Add optional fields: Safe -- free of migration when the default makes
  absent mean what existing files already mean (see Defaults)
- Add required fields: Must update all existing files
- Change enums: May break files

Start minimal, expand as useful fields emerge.
