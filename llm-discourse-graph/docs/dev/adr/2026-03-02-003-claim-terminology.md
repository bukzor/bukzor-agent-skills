---
status: accepted
date: 2026-03-02
---

# "Claim" terminology over "Assertion"

## Context

Initially renamed "Claim" to "Assertion" to de-emphasize debate connotations
and make the format feel general-purpose. Surveyed the broader knowledge
representation landscape.

## Decision

Use "Claim." It is the standard term across:
- Toulmin argumentation model
- Joel Chan's discourse graphs
- Clark et al. micropublications (2014)
- Schema.org (`schema.org/Claim`)

"Claim" in scientific usage is neutral — "the paper claims that X" carries
no adversarial connotation. "Assertion" is more generic but less precise:
in logic, an assertion is something you assert as true, while a claim is
something you put forward as possibly true. "Claim" better captures
epistemic uncertainty.

## Alternatives considered

**Assertion:** More neutral-sounding but not a term of art. Loses precision
about epistemic status.

**Statement:** Argdown's term. Too generic — a statement could be anything.

**Proposition:** Too academic.

## Consequences

- Aligns with established vocabulary across multiple fields
- Readers familiar with discourse graphs, Toulmin, or micropublications
  recognize the term immediately
- "Reasoning" (not "Argument") retained for the inference type to
  de-emphasize adversarial connotation where it matters more
