---
status: accepted
date: 2026-03-02
---

# Deduction polarity and status

## Context

The deductions schema modeled only entailment: premises entail a conclusion.
This left three gaps:

1. **No contradiction edges.** "Claim A opposes Claim B" required either an
   unstated convention or a `supports`/`opposes` field on claims — but the
   design already committed to mediating all inter-claim relations through
   deductions (ADR-000).
2. **No undercut edges.** "This evidence undermines that inference" (attacking
   the deduction itself, not its conclusion) had no structural representation.
3. **No status on deductions.** Claims have `status: asserted | contested |
   retracted`, but deductions had only `likelihood`. A disputed inference
   could not be marked as contested.

## Decision

Add two fields to the deductions schema:

**`kind`** — `entailment` (default) or `contradiction`. Determines polarity:

- `entailment`: premises support the conclusion being true
- `contradiction`: premises support the conclusion being false

**`status`** — same enum as claims: `asserted | contested | retracted`.

The `conclusion` field can point to either a claim or another deduction. This
covers all three argumentation relations with one mechanism:

| Relation | kind | conclusion points to |
|---|---|---|
| Support | `entailment` | `claims.kb/x.md` |
| Opposition | `contradiction` | `claims.kb/x.md` |
| Undercut | `contradiction` | `deductions.kb/d.md` |

## Alternatives considered

**`supports`/`opposes` fields on claims:** Would make inter-claim relations
direct rather than mediated through deductions. Rejected because it breaks
the existing principle that deductions are the sole mechanism for connecting
claims. Adding polarity to deductions achieves the same expressiveness without
a second relation mechanism.

**Separate `counterargument` collection type:** Adds a collection for what is
structurally identical to a deduction with opposite polarity. Unnecessary.

**Three-valued kind (entailment/contradiction/undercut):** Undercut is just
contradiction where the conclusion happens to be a deduction. No need for a
third value — the target type already disambiguates.

## Consequences

- All three argumentation relations (support, oppose, undercut) are now
  first-class without new collection types
- Deductions can target other deductions, enabling meta-argumentation
- `kind` defaults to `entailment` — existing deductions remain valid
- `status` on deductions enables marking disputed inferences
