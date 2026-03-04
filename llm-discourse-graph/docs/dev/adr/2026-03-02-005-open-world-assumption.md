---
status: accepted
date: 2026-03-02
---

# Open world assumption

## Context

Standard KGs differ on whether absence of a statement implies falsehood.
Closed World Assumption (CWA): what is not stated is false. Open World
Assumption (OWA): what is not stated is unknown. Wikidata explicitly uses
OWA — knowledge graphs are inherently incomplete.

## Decision

This format adopts the open world assumption. Absence of a claim does not
mean it is false. Absence of a question does not mean the topic is settled.
The graph is always incomplete.

## Consequences

- No node can be inferred from the absence of a node
- "We don't know" is a valid and common state
- Completeness cannot be assumed at any scope
- This aligns with the format's purpose: modeling knowledge-in-formation,
  not settled encyclopedic facts
