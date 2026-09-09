# Before Writing or Changing a Schema File

You're about to create or edit a `*.jsonschema.yaml` -- a new
collection's schema, a field added to an existing one, or a copy you
found and want to de-duplicate.

**Read `references/schema-reuse.md` first.** Add
`references/schema-design.md` when the question is what one file should
say rather than how files share.

The belief that most often goes stale in the wild: every published
canonical exposes an open `#base` beside its strict root, so a consumer
with extra fields extends -- `$ref: "<canonical>#base"`, its own
`properties:`, `unevaluatedProperties: false` -- and never copies. A
copy whose prose explains why extension was impossible is evidence
about the base as of the copy's date, not a ruling; open the base and
look for `$anchor: base` before believing it. The one binding form is a
root `$comment:` opening with `NO-REF`.
