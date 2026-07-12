---
why:
  - spec-cited-never-restated
---

# Genre: Design & Discourse

Two genres, kept deliberately separate, sharing one Layer-0 primitive
(`kb-spec.md`'s "linked node"): one file per node, typed frontmatter
edges, elaboration via sibling `.kb/`, roll-up to the parent on
resolution.

- **Design** (v1 `llm-design-kb`) — held/desired content: mission,
  goals, requirements, design, linked by `why:` chains. (This tower
  is an instance.)
- **Discourse** (v1 `llm-discourse-graph`) — truth-apt content:
  questions, claims, deductions, sources, definitions, linked by
  `premises`/`conclusion`/`candidate-resolutions`.

**Kept separate.** The two edge vocabularies encode different kinds
of content — held/desired vs. truth-apt — and merging them into one
vocabulary would blur that distinction inside the schema itself, not
just in prose. Sharing only the mechanical shape (node, edge,
elaboration, roll-up) captures everything genuinely common without
forcing the two content kinds into one.

**Cross-linkable by construction.** Both are plain node files in a
project's directory tree, so a discourse claim and a design
requirement cross-reference each other today with the ordinary
notation (`cross-reference-notation.md`) — no schema merge required
for that. The common case in practice is using both at once in one
project: place them as sibling scopes and link across freely; each
keeps its own schema, validator, and edge semantics.
