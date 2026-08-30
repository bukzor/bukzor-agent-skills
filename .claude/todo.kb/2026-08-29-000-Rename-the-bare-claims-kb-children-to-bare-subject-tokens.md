---
managed-by: Skill(llm-subtask)
status: open
---

# Rename the bare claims.kb children to bare subject tokens

**Priority:** Medium
**Complexity:** Medium (mechanical, but wide)
**Context:** PLACE/NEST, ruled by @bukzor 2026-08-29 during the
llm-design-kb reform: "the second `claims` is redundant". A child of a
bare `claims.kb/` takes a bare subject token, because the container
already supplies the word. Now stated in `llm-claims-kb/SKILL.md`'s
Layout section as the third naming case, and followed by the two
ledgers minted since; the six that predate it still carry the old
form.

## Scope

Six ledgers, each `<scope>/claims.kb/design.claims.kb/` ->
`<scope>/claims.kb/design.kb/`, with `.md` and `.jsonschema.yaml`
renamed to match:

- `docs/dev/claims.kb/design.claims.kb/` (and `strata.claims.kb/`)
- `deformalize/claims.kb/design.claims.kb/`
- `formalize/claims.kb/design.claims.kb/`
- `llm-claims/claims.kb/design.claims.kb/`
- `llm-kb/claims.kb/design.claims.kb/`

Roughly 243 reference lines across ~120 files. Internal `why:` arrows
are file-relative and survive the directory rename untouched; what
breaks is prose references, `skill://` paths, and the two-hop
`$ref` chains.

## Rules

- **Historical records keep the old name as provenance** — devlogs and
  ADRs are not swept (`Skill(llm-claims-kb)`'s Renames rule).
- One commit per ledger, `git mv` with both paths staged.
- After each: `llm.kb-validate`, `llm.kb-validate-links`,
  `llm-claims-kb-graph`, `llm-claims-kb-mentions`.
- Check `llm-claims-kb/lib/python/llm_claims_kb/{ledger,ownership}.py`
  and the `engine_tower` incubator for hardcoded ledger names before
  starting — both name these paths.

## Why not now

Deliberately not bundled into the reform that ruled it: a 120-file
mechanical rename would have buried the reform's diff, and single-topic
commits are the repo's convention. Nothing depends on it — the old
names are legal and only cosmetically redundant.
