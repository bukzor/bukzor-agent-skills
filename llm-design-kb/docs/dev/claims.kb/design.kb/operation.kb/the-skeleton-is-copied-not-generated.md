---
label: SKEL
standing: user
authority: "@bukzor 2026-08-29: 'a skeleton/ that consumers can copy wholesale to bootstrap. This removes a bunch of toil around the schema and such' -- prior art named: llm-collab/skeleton/"
why:
  - ../operation.md
  - ../stratification.kb/the-rung-set-is-seeded-not-legislated.md
---

# The Skeleton Is Copied, Not Generated

`skeleton/docs/dev/claims.kb/` is copied wholesale into a project to
bootstrap its record. There is no init script: `cp -r` is the whole
operation, which is where `llm-collab`'s skeleton ADR was already
heading when it reduced its generators to a copy.

It ships **schemas and empty collections, not just claims**. A
consumer who has to `mkdir` a collection and hand-write a
`.jsonschema.yaml` that they will need in over nine cases out of ten
is being charged toil the skill could have paid once. Each empty
collection therefore holds a `.keepme` that explains itself and asks
to be deleted -- deleting a file being cheaper than creating one, and
the collection being load-bearing anyway: a rung `.md` with no `.kb/`
beside it reads as an ordinary claim rather than a theory.

The rung claims ship `standing: open`, because they *are* the
questions -- "what problem are we solving?" -- and answering them is
the consumer's first act. This supersedes an earlier proposal that
they ship `standing: agent` as copied stipulations; a skeleton asserts
nothing about a project it has never seen.

Schemas enter by `skill://` reference rather than by copy. That is an
ergonomics default, not a correctness rule: a consumer with reason to
copy or extend the schema may, and pays the drift themselves.
