---
managed-by: Skill(llm-subtask)
status: done
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
`docs/dev/claims.kb/strata.claims.kb/standing.kb/`, REIFY in
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

- [x] Effective-evidence fold (EXPLICIT): acts ordered by occasion;
      an act leaves the effective set only when an admitted act
      targets it; same-issuer self-annulment admitted by every
      stance; no recency resolution. Property tests: clashing
      uncited same-issuer acts both stand and compute to the
      contested interval; a citing act strikes exactly its named
      targets. Done 2026-08-17: `Act`/`effective()`/`contest()` in
      `standing.py` (clashes are mutual attacks between acts, read
      through the existing `grounded` interval -- the same contested
      interval whether the clashing assessors are two or one).
- [x] Moot color (sense-collapse): presupposition edges propagate
      defeat as `moot`, a value outside the truth order that absorbs
      content-acts. Property test: a moot claim cannot also be
      content-defeated (MOOT's "never both" as a theorem, not a
      constraint). Done: `moot()`/`color()`; absorption happens
      before the truth-order pass, so the exclusion is derived, and
      `test_moot_absorbs_content_acts` checks it exhaustively over
      512 small records.
- [x] Desugar a real `.claims.kb/` (start:
      `llm-claims/design.claims.kb/`) into acts per REIFY --
      `standing:`/`verdict:`/`authority:` as one act, `verify:` as a
      checker act -- and run the full stack over it; computed
      standing must reproduce every file's written fields
      (DEGENERATE: stored equals computed below the tripwires).
      Done: `tests/test_data_representation.py`, 52 files;
      `bare`/`open` desugar to no act (they name no judge) and pass
      through as claim states.
- [x] Add `verify:` lines to ACT, FORCE, EXPLICIT, ONE_WAY, REIFY
      pointing at the new tests; re-run
      `llm-claims-kb-graph` and commit. All five run green verbatim;
      `llm.kb-validate` 87 files 0 errors.

## Open Questions

- COMPREHEND (chat ledger, 2026-08-17): may an act contravene by
  description ("all my prior acts on X") rather than enumeration?
  Algebra needs only evaluation-time resolvability; syntax is KEY's
  department. Build enumeration first; leave a seam.
- Where the desugaring code lives long-term (incubator vs
  `llm-claims-kb/bin/`) -- incubator until it proves out.

## Success Criteria

- [x] All four laws witnessed by tests over a real ledger, not a
      synthetic instance. (The composed stack -- fold, interval,
      sense-collapse -- runs over all 52 claims of
      `llm-claims/design.claims.kb`; that ledger exercises no
      contravention, clash, or presupposition failure, so those
      branches are additionally witnessed on smallest synthetic
      instances, matching the suite's house style.)
- [x] The five act-algebra claims carry passing `verify:` lines.
- [x] The "never both defeated and dissolved" exclusion holds as a
      derived property with no schema constraint asserting it.

## Residue (2026-08-17)

- The sense-collapse tests are cited by no `verify:` -- no strata
  claim states the law; the candidate carrier is WITHDRAWN's
  `dissolved` word (`llm-claims/design.claims.kb/notation.kb/a-verdict-names-what-the-judge-ruled.md`).
  User's call whether to file one.
- `llm-claims-kb-graph` flags a pre-existing fleet citation cycle
  (since b7b89c0): `discourse-graph-is-the-continuous-presentation`
  <-> `the-discourse-graph-never-evaluates`. Needs a direction
  ruling; not this task's to cut.
- `standing.py` is ~275 lines; the module layout is pinned by
  `test_the_modules_are_exactly_the_theories`, so any split means
  splitting the standing *theory* in the user-ruled ledger first.

## Notes

GRAIN (`llm-claims/design.claims.kb/notation.kb/how-should-judge-verdict-standing-be-represented-long-term.md`)
stays open on KEY/CUT/CACHE; this work informs CACHE directly and
should not preempt KEY or CUT -- those close by ruling, on their
tripwires.
