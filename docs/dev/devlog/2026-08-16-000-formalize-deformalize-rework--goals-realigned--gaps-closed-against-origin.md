# Devlog: 2026-08-16 -- `/formalize`/`/deformalize` realigned, then checked against their own origin

## Focus

An `/align` pass on `/formalize` (primary) and `/deformalize`
(secondary), negotiated into a claim ledger for each skill for the
first time. Then, separately: traced both skills back to the sessions
that produced them (`Skill(claude-code-archeology)`) and checked
whether the shipped skills actually cover the corrections and moves
that produced good results there. Five gaps found; all five closed.

## The realignment

`READER` was drafted inside `/formalize`'s ledger, then corrected and
moved wholesale to a new `deformalize/design.claims.kb/` once that
ledger existed to hold it -- the user's call ("you were meant to form
such a theory about /deformalize"), not a symmetric split. `/formalize`
stays formal; `/deformalize` owns the glossary and plain-English
successor theories and is now ledger-first, with plain-old-Python
demoted to an optional third rung (`DEFORM_ORDER`).

`stale-when:` absorbed what had been drafted as two notions
(a counterexample already in the data, a future change that would
break the claim) into one condition, evaluated at different moments
-- the same unification move `Skill(llm-claims)` itself made for
`defeated-by:` on 2026-08-13.

A real tooling gap surfaced wiring the seam: `llm-claims-kb`'s `why:`
resolution has no cross-ledger case -- `claim_id()` computes every id
relative to the *citing* ledger's own parent, so a path climbing into a
sibling skill's `.claims.kb/` reports dangling even though it resolves
on disk. Worked around with prose-only backtick citations (non-normative
by the notation's own rule); recorded in the root `.claude/todo.md`,
not fixed.

`llm-claims` itself gained a fourth core policy ("every render is a
patch") and a `## Commentary` section (`//` sub-bullets, no sigil, don't
travel with the claim) -- both surfaced by the negotiation, not planned
going in. The core block change means the claude.ai-preferences copy is
now stale (tracked, unfixed, `USER:` item).

## The coverage check

Traced `/deformalize` to its origin turn (session `a0c6820b`,
2026-08-09 ~20:00): proposed as a generalization of a comparison that
had *just happened* in the same session -- an independently-produced
Python reification of a formal ledger caught a real bug (the status
order wasn't actually a complete lattice, so Knaster–Tarski didn't
license what the ledger claimed) that self-review had missed. Chased
one level further back to the session that produced the identification
bar itself (`6b0cdfea`, 2026-08-09 ~14:38-19:33, three eras across two
compactions): five corrections, not the four a later session's summary
claimed, verified against the transcript directly rather than trusting
that summary (per the archeology skill's own caution -- a session's
account of itself is a lossy secondary source).

Checked the shipped skills against that transcript. Five gaps, all
closed this session:

1. **Questions weren't filed as their own theory.** The pre-negotiation
   draft had this ("the questions from step 5 are themselves a theory",
   echoing the origin session's [35]); dropped in the rewrite. Restored
   -- `QUESTIONS` claim + `formalize/SKILL.md` step 7.
2. **The review step didn't distinguish blind from self-review.** The
   origin move was blind (a sibling session's independent reification);
   today's review step was symmetric. One line added.
3. **No path past Python.** The retention question that started the
   whole thread ("does agda have an edge over lean... or dark-horse
   formal systems") asked about the ceiling of the ladder;
   `/deformalize` stops one rung short of it. Recorded as `PROOF_RUNG`,
   unbuilt, in the ledger only -- not in `SKILL.md`, per the ruling that
   a rung named in the manual before it exists is a promise the skill
   can't keep.
4. **No independent-verification procedure.** The highest-value move in
   either origin session (comparing two independently-produced accounts,
   not self-checking one) had no representation in either skill. Built
   as `formalize/SKILL.kb/must-read.kb/when/independent-verification-is-wanted.md`
   -- auxiliary, not the default path, same shape as `deformalize`'s code
   escalation -- plus `PEER_CHECK` in the ledger.
5. **No distillation above the ledger.** The origin session's actual
   "boil down" deliverable was a one-sentence Layer 0 plus a small
   number of named laws, sitting at the parent node of what it
   summarized -- a different, coarser compression than the poset+table
   `Skill(llm-claims-kb)`'s entry-point convention already provides.
   `ONEPAGE` (a size *budget*) was rejected earlier this same session for
   good reason and stays rejected; `DISTILL` is narrower and doesn't
   revive it. Added to `formalize/SKILL.md` step 8.

Two of the five (4 and 5) were flagged, then built without being asked
a second time -- both were additive, reversible, and already fully
specified by evidence already in hand; treating them as needing a
check-in was miscalibrated caution, called out directly and corrected
in the same turn.

## Verification

- `llm.kb-validate formalize/ deformalize/ llm-claims/`: 0 errors
  throughout, checked after every batch of edits.
- `llm-claims-kb-flatten` on both new ledgers: clean, no dangling `why:`
  (after the cross-ledger workaround above).
- `llm-claims-kb-graph`: both ledgers acyclic.

## Left open

- `STOP?` (`formalize/design.claims.kb/run.kb/what-the-stopping-rule-is.md`)
  -- the stopping-rule/check-in question, parked at the user's word.
- `DECIDED_UNBUILT?` (`llm-claims/design.claims.kb/notation.kb/`) -- how
  a ledger marks a claim that's decided but not yet built; the
  `AUTOCHECK! todo: ...` shape on the table is explicitly a strawman,
  not a decision.
- The cross-ledger `why:` tooling gap (above), root `.claude/todo.md`.
- `USER:` re-paste `llm-claims/SKILL.md`'s core block into claude.ai
  preferences -- now includes policy 4.

## Commits

`626d109`, `daaae2b`, `66d7c1d`, `1965487`, `d0ced89`, `f97eceb` -- all
pushed to `origin/main`.
