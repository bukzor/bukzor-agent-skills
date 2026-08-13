---
status: deferred
date: 2026-03-02
---

# Similarity groups for equivalent claims

## Context

In a collaborative graph maintained by multiple humans and LLMs, the same
idea will be expressed differently by different contributors. Clark et al.
(micropublications, 2014) formalize this as "Similarity Groups" with a
representative "Holotype" claim. Without a mechanism for equivalence, the
graph fragments through invisible duplication.

## Decision

Claims have optional `similars` and `holotype` frontmatter fields:

```yaml
similars:
  - claims.kb/rapamycin-inhibits-mtor-harrison.md
holotype: claims.kb/rapamycin-inhibits-mtor.md
```

`similars` lists other claims expressing the same idea in different words.
`holotype` points to the canonical representative of the group.

## Alternatives considered

**No equivalence mechanism:** Rely on humans/LLMs noticing duplication.
Fails at scale in collaborative graphs.

**Merge duplicates aggressively:** Loses provenance — different sources
expressing the same idea differently IS information worth preserving.

**Alias field on a single file:** Doesn't preserve the distinct source
formulations as separate nodes.

## Consequences

- Duplication is visible and managed, not hidden
- Different formulations preserved with their attribution
- Holotype provides a canonical reference point for queries
- Additional maintenance burden: keeping similarity groups current
