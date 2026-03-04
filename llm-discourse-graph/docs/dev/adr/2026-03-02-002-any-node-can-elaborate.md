---
status: accepted
date: 2026-03-02
---

# Any node can elaborate into a sub-scope

## Context

Need hierarchy for scoping discussions. Initially assumed only questions
create sub-scopes (following IBIS, where hierarchy is always through Issues).

## Decision

Any node type can be elaborated. `$ITEM.md` is elaborated by `$ITEM.kb/`
as a sibling in the same collection directory. The parent node IS the roll-up.

```
claims.kb/
  conways-law.md                <- the claim
  conways-law.kb/               <- elaboration
    deductions.kb/
```

Convention, not configuration — no `scope` frontmatter field needed. The
filesystem encodes the relationship via stem match.

## Alternatives considered

**Only questions create scopes:** Forces artificial reframing. "Conway's Law
holds" becomes "Is Conway's Law true?" — which is a valid question but not
what someone meant when they said "let's dig into this claim." The
question-only constraint added a rule without adding value.

**Explicit `scope` field in frontmatter:** Configuration over convention.
Redundant with the filesystem structure and creates a field to keep in sync.

**`.debate.kb/` suffix to distinguish from plain `.kb/`:** Unnecessary.
The contents of the elaboration directory are self-evident — if it has
`claims.kb/` and `deductions.kb/` inside, it's an elaboration. No
disambiguator needed.

## Consequences

- Hierarchy is general, not question-specific
- `ls` shows the association (stem match)
- Project root is itself an implicit scope (same shape as any elaboration)
- The recursion is uniform across all node types
