---
managed-by: Skill(llm-subtask)
status: pending
---

# Lean Port of the Engine Tower

**Priority:** Gated -- do not schedule until a trigger below fires;
until then this file exists to make the fork visible, not to nag.
**Complexity:** High -- session estimate (2026-08-18): ~six focused
sessions, with real stall risk concentrated in one proof.
**Context:** Ruled in the "f11n code" session, 2026-08-18: if the
engine is ever formalized, the proof-assistant code *is* the engine
-- one artifact, no shadow implementation, no correspondence proof.
That ruling turns "add proofs" into "move the engine", which is what
this brief specifies.

## Problem Statement

The act algebra's laws are ruled and witnessed
(`docs/dev/design-incubators/engine_tower/`), but the results that
carry the most weight are the *derived* ones -- the moot/defeated
exclusion, one-pass sufficiency of `color()`, the clash-interval
equivalences -- and their evidence is an informal argument plus
exhaustive checks over a small, strike-free domain. If the engine
becomes load-bearing across real ledgers, that evidence tier is too
low for what `certified` wants to mean.

## Current Situation

- Python incubator, 60 tests green; ten act-algebra claims carry
  passing `verify:` lines (ACT, FORCE, EXPLICIT, ONE_WAY, REIFY,
  DESCEND, and the derived SENSE, ABSORB, LOCAL, BLIND).
- SENSE was re-ruled 2026-08-20: standing is a *pair* -- sense and
  content, each on the same interval -- so a disputed presupposition
  now reads `contested` at the sense coordinate instead of vanishing.
  DESCEND was filed beside it, rejecting presupposition cycles. The
  postpone condition below therefore holds on its own terms: the act
  algebra moved this week, and the sense half of it is a week old.
- Every real ledger run so far is degenerate: no strikes, no
  clashes, no presupposition failures. Those branches are witnessed
  only on smallest synthetic instances.
- The cheaper confidence rung is taken (2026-08-18):
  `tests/test_derived_theorems.py` quantifies four derived results
  over generated strike-bearing records. That is evidence about small
  records -- three claims, five acts, four verdict words -- not proof
  about all of them, so it lowers the odds of a bug escaping without
  answering what this task answers. The four statements are now filed
  as claims that run those checks (ABSORB, LOCAL, BLIND standing
  `bare`, plus SENSE for the collapse rule they lean on), and the
  bound is recorded as debt at them and in `strata.claims.md`
  (Verify) -- so the general-form requirement below now has named
  claims to discharge rather than a devlog to re-read.
- The standing theory is still re-rulable: KEY, CUT open; GRAIN
  closes on their tripwires
  (`llm-claims/design.claims.kb/notation.kb/how-should-judge-verdict-standing-be-represented-long-term.md`).

## Triggers -- schedule this task when any fires

- [ ] An algebra bug escapes the test suite in a real ledger run.
      Overrides every postpone-state below; wrong answers outrank
      unsettled rulings.
- [ ] A real ledger starts exercising the non-degenerate branches --
      first live strike, clash, or moot claim -- *and* the standing
      theory's open rulings (KEY, CUT) have closed.
- [ ] The incubator graduates (the desugaring or the engine is about
      to leave for real tooling). The port is the graduation fork
      itself: decide the implementation language *at* that exit, not
      after Python tooling has accreted callers.

## Postpone -- keep waiting while any holds (bug-escape excepted)

- The act-algebra laws are still moving: KEY or CUT open, or any
  ruled claim of the standing theory re-litigated within the last
  few sessions. Proofs are brittle against re-rulings; formalizing a
  moving design buys churn, not confidence.
- Every real ledger remains degenerate. Until something strikes or
  dissolves in production, the minimal witnesses carry the actual
  load.

## Requirements

What must be true of the result. How is the implementer's, except
where a prior ruling already binds it.

- One artifact (ruled): the proof-assistant source is the engine.
  No maintained second implementation of the algebra, no
  correspondence obligation. Any surviving Python copy is explicitly
  non-normative.
- No witness regression at any point: every ledger claim whose
  `verify:` cites the incubator keeps a witness at least as strong
  through every intermediate commit; the pytest suite retires only
  claim-by-claim, as each successor witness lands.
- `verify:` lines stay agent-runnable from the repo root, green,
  with runtime an agent will actually pay per-claim.
- The derived theorems are stated in full generality and
  machine-checked: moot absorption / the never-both exclusion,
  one-pass sufficiency of the color computation, clash-interval
  equivalence (one vs two assessors), litigation-is-one-move. Where
  a bounded or finite-domain check stands in for a general proof,
  the bound is recorded as explicit debt at the claim it weakens.
- The tower discipline survives with teeth: modules-are-theories and
  priors-only imports remain *enforced*, and the ledger stays the
  only home of the poset (or the brief that lands the port says
  precisely what replaced that guarantee and why it is as strong).
- The degenerate real-ledger reproduction still holds against the
  live ledger, not a snapshot: fields desugared per REIFY, computed
  standing reproducing every written field. Where the file-reading
  boundary sits is unconstrained; that it reads the real ledger is
  not.

## Open Questions

- Lean 4 vs Agda. Session recommendation on record (devlog
  2026-08-18, unratified): Lean 4 -- mathlib's order theory,
  compiled executables first-class, agent fluency. Decide at
  trigger time; the requirements above are neutral.
- What kernel-checked witnesses do to the ledger's standing
  vocabulary: is a checked theorem a stronger `certified`, or the
  same word earned honestly? Possibly a claim of its own.
- Whether the pytest incubator survives as non-normative
  illustration or retires fully once the last witness migrates.

## Success Criteria

- [ ] Every engine-cited claim's `verify:` resolves to a
      machine-checked witness and runs green from the repo root.
- [ ] The four derived theorems are checked in generality, or their
      bounds stand recorded as debt at the claims they weaken.
- [ ] The real-ledger reproduction check passes against the live
      ledger.
- [ ] `git log` shows no intermediate commit at which any claim's
      witness was weaker than before the port began.
- [ ] One artifact: no normative Python implementation of the
      algebra remains.

## Notes

Prior analysis: the "f11n code" session (2026-08-18) weighed
hypothesis property-testing vs formalization -- hypothesis rated the
right interim rung (an afternoon, targets the strike-bearing domain
gap in `test_moot_absorbs_content_acts`), formalization rated
high-leverage only as the graduation move. The one-artifact ruling
and the six-session estimate are from that conversation.

The rung was taken the same day, so this task inherits its four
statements rather than inventing them: moot absorbs content-acts,
one collapse pass reaches the fixpoint, assessor identity carries no
force of its own, one act settles any claim whose frame stands
(`tests/test_derived_theorems.py`). Writing them turned up one
result the informal argument had not stated: the second contest in
`color()` is redundant for the value -- dropping a moot claim's acts
removes whole components, so no surviving claim's interval can move
-- and is load-bearing only for the derivation, which is why it
stays.
