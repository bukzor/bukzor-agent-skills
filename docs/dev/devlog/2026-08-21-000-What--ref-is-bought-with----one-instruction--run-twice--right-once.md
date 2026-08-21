# Devlog: 2026-08-21 — What `$ref` is bought with

## Focus

One instruction — *use `$ref` for DRYness* — applied twice in one
session, wrongly the first time. The wrong pass and its revert are the
useful part; the right pass found a schema fork that had been drifting
since 2026-08-17.

## The data was right and the schema was the bug

`strata.replication.run.kb`'s sixteen `sent:`/`replied:` timestamps were
failing a `type: string` schema. The first fix quoted all sixteen. The
user's correction — *"that smells wrong; see the custom `date` and
`instant` types"* — was right twice over: the llmd dialect exists exactly
so a YAML-native timestamp needs no quoting, and the schema declared a
*stock* dialect, under which `date` and `instant` are unknown types.
Quoting the data to satisfy a schema that couldn't express the type is
the fix pointing the wrong way.

The corroboration was already on disk: `extract-stages.py:155` writes the
value unquoted, so the quoting would have been undone by the next
extraction.

One layer up, the same defect: `last-updated` in the canonical claim
schema was `type: string` plus `pattern: "^\\d{4}-\\d{2}-\\d{2}$"` — a
regex re-implementing a type the dialect already had — which is why eight
values across four skills were quoted.

## The wrong pass: `$ref` for a word you can spell

Reading "use `$ref` for DRYness" as a general instruction produced
`llm-kb/jsonschema/{date,instant}.jsonschema.yaml`: one-line units, six
consumers rewritten to `$ref` them. It validated, and every probe passed.

It was still wrong, and the giveaway was in its own justification. The
stated benefit was removing the dialect declaration from consumers — but
a schema that declares *no* `$schema` already means the llmd dialect, so
that declaration was never forced and deleting it needed no indirection.
What was left was cost: `type: date` says what it is where you read it,
while a `skill://` URL to a one-line file says go look.

`llm-kb/references/schema-reuse.md` now states the floor, because its
absence is what made the misreading available: the cost `$ref` buys off
is **hand-synced duplication — N copies that have to agree and don't** —
not repetition as such.

## The right pass: the copy that actually existed

The instruction's real referent was N drifting copies. Content-hashing
every schema in the repo found them already fixed — the 2026-07-07
copies-to-stubs migration — except two symlinks and one fork.

The symlinks (`docs/dev/{strata,design}.claims.kb/jsonschema/`) resolved
correctly but through the filesystem rather than the schema layer, so
they said nothing to a reader of the file. They are stubs now, like their
three siblings.

The fork was the find. `docs/dev/design.claims.kb/principles.jsonschema.yaml`
declared itself in its own description — *"Fork of
llm-claims-kb/jsonschema/claim.jsonschema.yaml … extended with one field:
`force`"* — and had since drifted three ways: a stale `ontology:`
description from before the ownership work rewrote it, the `last-updated`
defect, and a stock dialect that could not have expressed the fix.

It forked because the canonical had no extension point. It has one now —
the `$defs.base` + `$anchor: base` split that
`llm-subtask/jsonschema/todo.jsonschema.yaml` has carried all along, with
the closure stated once at the root. The fork is 30 lines instead of 130,
and the three drifts are gone because there is nothing left to drift.

No schema copy remains in the repo.

## A red count that isn't

Probing the fix surfaced something the 2026-07-09 date migration had
noted and scoped out, still true: a top-level `$CATEGORY.md` summary file
is **counted but not schema-checked**. Lookup for a collection resolves
`X.kb/` → `X.jsonschema.yaml`; the `X.md` beside it matches nothing.
Quoting `last-updated` in `llm-kb/complete-example/decorations.md` still
reads `20 files, 0 errors`.

What changed is the stakes. Every ledger's entry point — `X.claims.md`,
carrying `last-updated:` and the poset — is exactly such a file. Six of
the eight values unquoted today live in files nothing checks; they are
right by consistency, not by enforcement. Filed.

## What the verification had to be

Seven probes, each restored after. The ones that mattered were not the
ones testing what had just been edited: an unknown key must still be
rejected through the canonical's new root closure
(`additionalProperties` → `unevaluatedProperties`), `force` must *not*
leak into ordinary claims, and a naive timestamp — not merely a quoted
one — must fail `instant`. A chain that silently resolved to an empty
schema would have passed every probe aimed at the field being changed.
