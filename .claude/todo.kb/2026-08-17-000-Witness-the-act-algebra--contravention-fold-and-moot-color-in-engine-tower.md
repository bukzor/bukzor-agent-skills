---
managed-by: Skill(llm-subtask)
status: open
---

# Witness the Act Algebra: Contravention Fold and Moot Color in engine_tower

**Priority:** Medium -- nothing blocks on it, but it is the only thing
standing between the ruled act algebra and `certified`, and it
discharges CACHE's acceptance debt (SUGAR licenses the scalar field
"in exactly the degree that the map exists to desugar into"; today
that degree is design-only).
**Complexity:** Medium -- a few hundred lines by estimate, on top of a
tested codebase (`docs/dev/design-incubators/engine_tower/`).
**Context:** The act algebra was user-ruled 2026-08-17 (commit
b7b89c0): ACT, FORCE, EXPLICIT, ONE_WAY in
`docs/dev/strata.claims.kb/standing.kb/`, REIFY in
`.../data-representation.kb/`. Two of its four laws (support
fixpoint, defeat/interval calculus) already run in engine_tower with
a pytest witness suite; the other two exist only as prose.

## Problem Statement

The algebra's claims carry no `verify:` lines because nothing
executes them. WITNESS closes that: mechanize the two unwitnessed
laws and run the whole stack over a real `.claims.kb/`, so the
claims graduate from user-ruled to certified and the fields-to-acts
desugaring stops being promissory.

## Current Situation

- engine_tower witnesses OPERATOR, COMPUTED, COMPLETION, DEFEAT,
  ASYMMETRY (`tests/test_standing.py`), wired to no real ledger.
- EXPLICIT (contravention fold) and sense-collapse (the moot color
  behind `verdict: dissolved`) have no executable form.
- Related, pre-existing: `.claude/todo.kb/2026-08-09-000-engine-tower-incubator-follow-ups.md`
  (tooling gaps), `.claude/todo.kb/2026-08-16-000-Reconcile-llm-claims-kb-s-standing-scheme-with-PRMS-s-stmt-proof-and-STANCE-s-assessor-relativity.md`
  (the reconciliation this ruling advanced).

## Proposed Solution

Extend engine_tower with the two missing laws, then feed it a real
ledger through the degenerate-case desugaring (REIFY: fields are the
one-act sugar).

## Implementation Steps

- [ ] Effective-evidence fold (EXPLICIT): acts ordered by occasion;
      an act leaves the effective set only when an admitted act
      targets it; same-issuer self-annulment admitted by every
      stance; no recency resolution. Property tests: clashing
      uncited same-issuer acts both stand and compute to the
      contested interval; a citing act strikes exactly its named
      targets.
- [ ] Moot color (sense-collapse): presupposition edges propagate
      defeat as `moot`, a value outside the truth order that absorbs
      content-acts. Property test: a moot claim cannot also be
      content-defeated (MOOT's "never both" as a theorem, not a
      constraint).
- [ ] Desugar a real `.claims.kb/` (start:
      `llm-claims/design.claims.kb/`) into acts per REIFY --
      `standing:`/`verdict:`/`authority:` as one act, `verify:` as a
      checker act -- and run the full stack over it; computed
      standing must reproduce every file's written fields
      (DEGENERATE: stored equals computed below the tripwires).
- [ ] Add `verify:` lines to ACT, FORCE, EXPLICIT, ONE_WAY, REIFY
      pointing at the new tests; re-run
      `llm-claims-kb-graph` and commit.

## Open Questions

- COMPREHEND (chat ledger, 2026-08-17): may an act contravene by
  description ("all my prior acts on X") rather than enumeration?
  Algebra needs only evaluation-time resolvability; syntax is KEY's
  department. Build enumeration first; leave a seam.
- Where the desugaring code lives long-term (incubator vs
  `llm-claims-kb/bin/`) -- incubator until it proves out.

## Success Criteria

- [ ] All four laws witnessed by tests over a real ledger, not a
      synthetic instance.
- [ ] The five act-algebra claims carry passing `verify:` lines.
- [ ] The "never both defeated and dissolved" exclusion holds as a
      derived property with no schema constraint asserting it.

## Notes

GRAIN (`llm-claims/design.claims.kb/notation.kb/how-should-judge-verdict-standing-be-represented-long-term.md`)
stays open on KEY/CUT/CACHE; this work informs CACHE directly and
should not preempt KEY or CUT -- those close by ruling, on their
tripwires.
