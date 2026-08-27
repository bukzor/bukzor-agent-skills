---
label: STATUS_ENUM
standing: agent
---

# `status:` Is a Spelling, Not a Concept

There is no `status` canonical to write, and there never will be. The
corpus carries at least seven incompatible vocabularies under the one
name, so the shared spelling marks a collision rather than a concept;
each vocabulary earns a canonical named for what it governs, or none
at all.

The vocabularies, no two of them convertible:

- a todo item: `open|deferred|blocked|not-started|done|abandoned|duplicate|template`
- a migration: `tentative|planning|started|in-progress|complete|verified|archival`
- a design entry's decision lifecycle: `idea|proposal|accepted|rejected|superseded`
- a discourse-graph node: a truth-valued word
- a curriculum's 060 entries: `not-started|done`
- har-browse's 070 sub-kb: `frontier-optimal|dominated`
- ideation.physical-musings: `active|deferred|superseded`
- loose files: `active`, `exploring`, `complete`, from no vocabulary at all

Two independent surveys produced that list -- this claim's original
four and the layer-entry recommendation's four -- and they overlap in
one entry. Neither author suspected the other's. A name eight authors
reached for independently, meaning eight things, is a word carrying no
information.

What follows is not "four names and no canonical at all." A vocabulary
whose copies have provably drifted still earns extraction; it just does
not earn the name `status`. The decision-lifecycle trio is the first
such case and the argument is written out in
`.claude/todo.kb/2026-08-23-005-Fleet-rulings-that-gate-the-schema-lanes.kb/2026-08-23-000-decision-lifecycle-trio-canonical-recommendation.md`:
four declaration sites, one traceable copy lineage, already forked on
`superseded-by`'s type, and zero data edits to converge them today.

The declined alternative is the other half of this claim's original
question -- one concept with four dialects, canonicalized once and
pointed at from each schema. It loses on the enum contents, which no
widening reconciles: a migration's `verified` and a design entry's
`rejected` are not two dialects of one lifecycle, and a schema admitting
both admits nonsense in every tree that binds it.
