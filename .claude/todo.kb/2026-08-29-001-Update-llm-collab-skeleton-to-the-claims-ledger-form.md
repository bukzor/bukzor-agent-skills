---
managed-by: Skill(llm-subtask)
status: open
---

# Update llm-collab's skeleton to the claims-ledger form

**Priority:** Medium
**Complexity:** Low
**Context:** COHORT, ruled 2026-08-29. `llm-collab/skeleton/` ships the
superseded design-tower pattern to every project that bootstraps from
it, so each new consumer starts on the format the llm-design-kb reform
just replaced.

## What is wrong

- `skeleton/docs/dev/design/` — the pre-ledger tower layout. The
  replacement is `skeleton/docs/dev/claims.kb/`, which
  `llm-design-kb/skeleton/` now ships; llm-collab should reference or
  mirror it rather than grow a third copy.
- `skeleton/docs/dev/technical-policy.jsonschema.yaml` — a **copy** of
  a schema, not a `$ref` to one. Its canonical home is now
  `skill://llm-claims-kb/jsonschema/policy.jsonschema.yaml`. This is
  the same drift that had `docs/dev/claims.kb/design.claims.kb/principles.jsonschema.yaml`
  claiming to import `force` while duplicating its whole `oneOf`
  (fixed 2026-08-29).

## Open question the fix has to answer

Whether llm-collab's skeleton should *contain* a design record at all,
or point at `/llm-design-kb` for it. Two skeletons that both bootstrap
design documentation is the parallel-home anti-pattern; the likely
answer is that llm-collab keeps ADR/devlog/README scaffolding, which is
genuinely its own, and delegates the design record.
