---
label: STUB_IS_SCHEMA
standing: agent
why:
  - every-collection-with-frontmatter-gets-a-schema.md
---

# A `$ref` Stub Is a Schema

"Has no schema" means no sibling `X.jsonschema.yaml` exists. It does
not mean the file present is shorter than the one a sweep would have
written. A two-line `$ref` stub is the *preferred* form, per
`references/schema-reuse.md`, so a sweep acting on
CANONICAL_PER_COLLECTION writes only where the sibling file is absent
and stops at every file it finds.

The distinction is not hypothetical. CANONICAL_PER_COLLECTION was
committed 2026-08-22 13:54 with the note that a mechanical agent could
do the work; the blast's files are stamped 14:03, nine minutes later.
Read as "make every collection have a schema", it overwrote 254
hand-written canonicals, stubs among them. The residue is still on
disk: `~/repo/github.com/bukzor/dotfiles` carries nine modified schema
files and two untracked ones, every diff replacing a committed
`$ref: skill://...` line with a hand-rolled full copy.

So the rule needs one more clause than it reads with, and the clause is
the whole difference between a sweep that closes gaps and a sweep that
un-does the `$ref` rollout:

- **absent sibling** -- write the schema, stub it onto a canonical if
  one is published;
- **present sibling, any length** -- leave it, and report it only if
  it fails to resolve.

The declined alternative is to fix this in the sweeping agent's brief
rather than in the ledger. It loses because the brief is written fresh
each time and the claim is what the next agent reads: a rule whose safe
reading lives only in the prompt of one run is a rule that gets
re-misread on the next.
