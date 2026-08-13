# Self-audit: schema potential

## Goal

Items carrying structured data have a `$CATEGORY.jsonschema.yaml`;
the data lives in frontmatter, not in prose.

## Procedure

For each `.kb/` you touched with 2+ items, scan for the same kind of
fact appearing across items: inline labels (`Status: accepted`),
repeated section headings (`## Owner`), or free-prose statements
covering the same fact in different words.

If 3+ items carry the same kind of fact, schema-promote on sight.

## Recovery

Design a schema (`references/schema-design.md`). Lift the in-prose
fields into frontmatter. Run `bin/llm.kb-validate`.

## Related

- `collection-homogeneity.md` -- items not sharing a type-of-thing
  won't share structure; fix homogeneity first.
