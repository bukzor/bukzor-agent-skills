# A theory is a claim; containment is indentation

**Date:** 2026-08-11
**Status:** Accepted
**Amended:** 2026-08-13 -- the header this ADR calls `defeated-by:` is
now `stale-when:`, narrowed to the observable condition; see
`devlog/2026-08-13-000-stale-when-replaces-defeated-by--a-header-cannot-predict-an-outcome.md`.
The word `defeater` below reads as "staleness condition", and the
`FLEET_MAP` whose collision Consequences names is now `ATLAS`.

## Context

`Skill(llm-claims)` has said since its first draft that a theory needs
no node type of its own (claim `THEORY_NODE+`): it opens with a
defining claim whose text fixes the ontology and the defeater and
whose arrows name the priors, so extension and contest are ordinary
governance on that claim. The file form did not follow. In
`Skill(llm-claims-kb)` a theory was a *header*: a `<theory>.md`
synthesis file whose frontmatter carried only `last-updated:`, with
the ontology, the priors, and the defeater written as bullets at the
top of the collection's `CLAUDE.md`. Consequences:

- A theory had no `standing:` and so no sigil. The one thing the
  notation insists on -- every claim sound, open, or retracted, signed
  by whoever judged it -- was unavailable for the claims that govern
  the vocabulary of every other claim.
- The ontology lived in a maintenance guide, where no tool looked, in
  prose no schema typed.
- The nesting was hard-coded two deep: ledger, theory, claims. A
  theory inside a theory had no spelling, and the ledger's own root
  (`design.claims.md`) was a fourth kind of file again.
- `bin/llm-claims-kb-flatten` had to invent a header line for the chat
  form, and could not say who signed it.

## Decision

One rule, at every depth: **`X.md` beside `X.kb/` is the claim that
defines the theory `X.kb/` holds.** It is a claim like any other --
`label:`, `standing:`, `why:` -- plus three fields only a defining
claim carries: `ontology:` (the words it stipulates), `defeated-by:`
(what would retire the theory whole), and `last-updated:` where its
body also carries a roll-up view. An `X.md` with no `X.kb/` beside it
is an ordinary claim; nothing else distinguishes the two.

The rule recurses upward and downward without a special case. A
ledger's own `design.claims.md` defines `design.claims.kb/` by the
same rule, so the ledger is simply its outermost theory; a theory
inside a theory is spelled the way everything else is.

The defining claim is not *required*, and its absence has exactly one
meaning: `X.kb/` with no `X.md` is an **open theory**. It stipulates
nothing, so its claims answer to the ontologies above it, and it
renders and is cited `LABEL?` -- the notation's own way of saying
nobody has signed. What it never means is a folder: a collection whose
claims need no words of their own belongs in its parent. Requiring the
claim up front would price a new theory at a signature nobody is ready
to make; letting it stand open prices the debt where the ledger
already prices debt, and the first claim inside it that needs a word
of its own is the bill.

Priors ride on `why:`. On a defining claim, what the claim rests on
*is* the list of theories whose words it also admits, so priors need
no field of their own.

The chat rendering is **one nested list**: indentation is containment,
`<-` stays support. A claim reads in every word stipulated above it,
which is the whole of theory membership -- no membership field, no
grouping header, no fixed depth. `Skill(llm-claims)`'s recommended
markdown format follows suit, with the flat list as the all-defaults
case.

Content moved, not copied: each collection's `CLAUDE.md` gives up its
lede and its header bullets and keeps only the maintenance guide (what
belongs here, what does not); the theory's own words live once, in the
defining claim.

## Alternatives Considered

### A `theory:` membership field on every claim
- **Pros:** membership is explicit, greppable per claim, and survives
  reflowing
- **Cons:** pays a token on every line to say what one two-space
  indent says once, and still cannot express a theory inside a theory
  without inventing a second field for the parent

### A separate theory schema alongside the claim schema
- **Pros:** the theory-only fields are required where they belong and
  rejected where they don't
- **Cons:** the claim schema is `additionalProperties: false`, and in
  draft-07 a `$ref` ignores its siblings, so a per-collection schema
  cannot extend it -- the three fields go on the shared schema as
  optional, and the flatten lints the case a schema would have caught
  (a defining claim that stipulates no ontology)

### Keep the header form, add `standing:` to it
- **Pros:** the smallest possible diff
- **Cons:** leaves a second node type in a notation whose own claim
  says there is one, and leaves the two-level nesting and the fourth
  kind of root file exactly as they were

## Consequences

**Positive:** a theory is signed, contested, retracted, and rendered
by the machinery that already existed for claims; the reader tool lost
its root special case; the flatten gained lints a header form could
not support; nesting is unbounded.

**Negative:** every ledger in the repo was migrated at once
(`llm-claims/design.claims.kb/`, `docs/dev/design.claims.kb/`,
`docs/dev/strata.claims.kb/`), and theory labels now share one
namespace with claim labels -- `FLEET` (the theory) prefixes
`FLEET_MAP` (a claim inside it), which `grep FLEET` cannot tell apart.
The strata root was renamed `ENGINE` for the same reason. Every
migrated theory stands `agent`; they were unsigned before, so this is
newly visible debt rather than new debt.

**Neutral:** each ledger's `<name>.claims.jsonschema.yaml` now
`$ref`s its own `claim.jsonschema.yaml` instead of typing a synthesis
file, so the root defining claim validates like the rest -- except at
the very top, where `llm-kb`'s validator only reaches files inside a
`.kb/`; the ledger root's frontmatter is checked by the reader's own
asserts and lints instead.

## Related

- `llm-claims/design.claims.kb/notation.kb/a-theory-is-defined-by-a-claim.md`
  (`THEORY_NODE+`) -- the claim this ADR finally implements
- `llm-claims/design.claims.kb/notation.kb/containment-is-indentation.md`
  (`NESTING+`) -- the claim recording the rendering half
- `2026-08-10-000-Adopt-the-claims-kb-suffix--rename-the-ledger-skills.md`
  -- the rename this builds on
