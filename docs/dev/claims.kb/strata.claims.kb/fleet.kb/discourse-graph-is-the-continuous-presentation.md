---
label: CONTINUUM
standing: agent
why:
  - ../standing.kb/verdicts-are-assessor-indexed.md
  - ../standing.kb/status-is-a-poset-with-a-fibered-top.md
---

# Discourse-Graph Is the Continuous Presentation

`llm-discourse-graph`'s unified claim scheme
(`docs/dev/design/unified-claim-scheme/validity-axes.md`,
`.../per-party-validity.md`) is the standing stratum at continuous
resolution: its validity axes (truth, certainty, utility) are the
un-quotiented commitment space whose four-point quotient is the
status order, and its per-party validity map -- assessor-keyed
entries over an `$all` consensus, RFC 7396 merge-patch to override --
is the assessor law verbatim, designed 2026-03, months before the
mechanized operator crashed on the missing join. Design, not shipped:
the live schema (`jsonschema/claims.jsonschema.yaml`) carries neither
the party map nor the axes, only a flat `status` enum and a scalar
`likelihood`. The two systems are one structure at two resolutions,
not a division of labor; porting between them is choosing a quotient,
not translating a theory.
