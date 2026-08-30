---
label: POLICY
standing: user
authority: "@bukzor 2026-08-29: 'technical policy fits neatly at claims.kb/technical-policy.kb/. We provide a jsonschema/policy.jsonschema.yaml for it. Which has a $defs.force in case anyone wants to borrow just that bit.'"
why:
  - ../migration.md
  - ../operation.kb/the-skeleton-is-copied-not-generated.md
---

# Technical Policy Becomes a Theory

Cross-cutting normative rules live at `claims.kb/technical-policy.kb/`
-- a theory beside the design record rather than inside it, preserving
the sibling relationship the incumbent layout already had.

Its `force:` field (`must` / `should` / `may`, RFC 2119) moves to
`skill://llm-claims-kb/jsonschema/policy.jsonschema.yaml`, which is
the claim schema plus that one field, with a `#force` anchor for
consumers who want only the grading. The field is why policy needs a
schema of its own at all: a policy is an imperative, and grading how
hard it binds is meaningless on a descriptive claim.

The canonical definition had to move because it was already being
copied. `docs/dev/claims.kb/design.claims.kb/principles.jsonschema.yaml`
described itself as importing `force` from this skill and in fact
duplicated the whole `oneOf` -- a schema drifting from its stated
source, in the fleet's own constitution. This skill's
`technical-policy.jsonschema.yaml` stays in place for legacy towers.
