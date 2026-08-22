---
label: MODELINE_SELECTS
standing: user
why:
  - a-roll-up-may-be-data-and-todo-md-is.md
authority: "user, 2026-08-22: 'there already exists a load-bearing mechanism for this: the # yaml-language-server comments ... a good smell: this path doesn't incur chicken-and-egg schema changes'"
---

# A File May Name Its Own Schema

Schema binding is positional: `X.kb/entry.md` is governed by
`X.jsonschema.yaml` beside the directory, and a file outside any
collection is governed by nothing. That default is right and stays.
Beside it goes an explicit opt-in: a file may name its schema, and
then it is data whatever its position says.

The mechanism already exists and already runs -- the modeline every
schema file in this corpus already carries:

```yaml
# yaml-language-server: $schema=https://json-schema.org/draft/2020-12/schema
```

A *modeline* is a comment on the first line that a tool reads as
configuration rather than as content -- vim's `# vim: set ...`, and
here the YAML language server's `$schema` pragma, which is what makes
an editor complete and check these files today.

The declined alternative was a `$schema:` key in the frontmatter
itself. It is chicken-and-egg: the key selecting the schema must
itself validate against that schema, so every schema in the corpus
grows a property whose only job is to permit its own selector. The
modeline is outside the document, so it costs no schema change
anywhere.
