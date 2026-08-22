---
label: PRAGMA_AGREES
standing: open
why:
  - does-a-schema-declare-its-dialect.md
  - a-file-may-name-its-own-schema.md
authority: "user, 2026-08-22: 'i've been wondering, shouldn't $schema and # yaml-language-server: pragma match?'"
---

# Should the Modeline and the $schema Key Agree?

A schema file can say its dialect twice: in the `# yaml-language-server`
modeline, which is what the editor reads, and in its own `$schema` key,
which is what a validating library reads. Nothing checks that the two
say the same thing, and in this corpus they routinely do not -- 318
files carry a draft-07 modeline while the canonical they `$ref` is
2020-12.

The same question as SELECTION_CONFLICT one level up: two declarations
of one fact, and no rule that they match. The likely answer is the same
answer, but it is not the same claim, because the two fields address
different readers -- an editor and a validator -- and it is arguable
that an editor pinned to an older draft is a deliberate accommodation
rather than drift.

Note that they cannot always agree: a schema *about* schemas legitimately
declares one dialect and is written in another.
