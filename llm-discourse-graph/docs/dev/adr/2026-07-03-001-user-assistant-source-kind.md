---
status: accepted
date: 2026-07-03
---

# `user`/`assistant` as source kinds

## Context

ADR-000 folded Evidence into Claims, reasoning that the epistemic
difference between observed and inferred claims is "captured by
optional `source` and `date-observed` fields on claims" -- but the
implemented `claims.jsonschema.yaml` only ever grew a plural `sources`
array (paths to `sources.kb/` provenance nodes for observational/
empirical claims); no field captured *who, in live discussion, asserted
a non-empirical claim* (a stipulation, a proposal, a user's own idea).
`ideation.physical-musings` (2026-07-03) needed exactly this to fight
its own core failure modes (backslide, sycophancy) and first reached
for a new parallel `source` (singular) field on claims/deductions --
which would have duplicated `sources` in both name and mechanism.

## Decision

No new field. Extend `sources.kb/`'s `kind` enum with `user` and
`assistant`, so a live-discussion participant is modeled the same way
as any other provenance reference: one reusable stub source node (e.g.
`sources.kb/user.md`, `kind: user`), cited from many claims via the
existing `sources: [...]` array. `testimony` remains distinct -- a
third party's *reported* statement, not a live co-author's own.

## Alternatives considered

**New `source` (singular) field on claims/deductions:** what ADR-000's
own rationale seemed to anticipate. Rejected on discovery: it would
duplicate `sources` in both name and mechanism for no added expressive
power -- `sources.kb` already exists precisely to hold reusable
provenance nodes cited from many claims.

## Consequences

- One source-kind vocabulary covers both empirical and non-empirical
  provenance; no schema growth on claims/deductions themselves.
- Projects wanting live-discussion provenance create small stub nodes
  (`sources.kb/user.md`, `sources.kb/assistant.md`) once, then cite
  them like any other source.
