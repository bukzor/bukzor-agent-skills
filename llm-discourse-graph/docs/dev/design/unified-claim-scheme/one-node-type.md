# One Node Type: Claim

## Decision

Collapse five collection types (questions, claims, deductions, sources,
definitions) into one: claim. Variation comes from attributes, not types.

## Discussion

The discourse graph had five typed collections with separate schemas.
In practice during the vim config decomposition session:

- **Deductions** added ceremony without value. Every deduction was
  straightforward — the body text of the conclusion claim could carry
  the reasoning. Replaced by `why[]` on claims.
- **Definitions** are stipulative claims — truth = 1 by construction,
  only utility varies. No structural distinction needed.
- **Questions** are incomplete claims with unknown referents. This matches
  erotetic logic (Hamblin, Hintikka, Groenendijk & Stokhof): a question
  is the set of its possible complete answers, or equivalently a
  proposition with an unfilled variable. Distinguishable by the presence
  of `candidate-resolutions` or `resolved` fields.
- **Sources** are provenance metadata, not nodes in the graph. They
  became attributes on claims (`sources:` field) rather than a separate
  collection. Externalized via `$ref` for DRY when multiple claims
  share a source.

Node "type" is emergent from attributes and graph position:

| Has source? | Has why[]? | High normativity? | Emergent type |
|---|---|---|---|
| yes | no | no | Observation |
| maybe | yes (certainty=1) | no | Deduction |
| maybe | yes (certainty<1) | no | Inference |
| no | no | yes | Stipulation/Definition |
| n/a | n/a | n/a, has unknowns | Question |

## What We Lose

- **First-class deductions** that can be independently contested ("your
  premises are fine but your reasoning is flawed"). Mitigation: meta-claims
  about the justification. Flagged as a watch item.
- **Typed directories** scannable via `ls sources.kb/`. Mitigation: node
  type derivable from frontmatter queries.
- **Kind: contradiction** on deductions. Mitigation: positive-only design;
  watch for friction.
