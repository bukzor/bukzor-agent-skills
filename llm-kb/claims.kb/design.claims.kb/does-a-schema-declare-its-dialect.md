---
label: DIALECT_DECLARED
standing: open
---

# Does a Schema Declare Its Dialect?

144 of 309 schema files in the corpus declare no `$schema` at all.
The rest declare one, and `llm-kb/jsonschema/dialect.jsonschema.yaml`
exists as the house dialect for those that do.

Two readings, and nobody has ruled between them. Either the
declaration is load-bearing -- a schema without one is validated under
whatever default the reader's library picks, which is drift waiting to
happen -- or the house dialect is the only one this corpus has ever
used, the default is already right, and 144 files are correctly silent.

The user's current lean, unratified: "I think the current thinking is
we don't want one? not sure."

Resolving this decides whether the 144 are a backlog or a non-event.
