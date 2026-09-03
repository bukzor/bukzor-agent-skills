---
label: MIGRATION
standing: agent
why:
  - ../design.md
  - stratification.md
ontology:
  - legacy tower
  - route
non-claim-tokens:
  - RFC
stale-when: a numbered tower that fails to validate against the retained layer-entry schema -- the promise that old records keep working would have quietly lapsed
---

# migration -- what happens to what already exists

The reform is executed in place and nothing is rewritten on a
schedule. The skill's name and path do not move, which is what makes
the routing work: an agent meeting a numbered tower loads
`llm-design-kb`, because that is what the tower is, so whatever it
needs to read next has to be reachable from there.

This mirrors the fleet's ruling for its first extension
(`../../../../../docs/dev/claims.kb/design.claims.kb/extension.kb/migration-plan.md`),
which had already priced every part of the question.
