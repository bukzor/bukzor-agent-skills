---
turn: 040-witness.md
sent: 2026-08-10T20:55:01.591Z
replied: 2026-08-10T21:05:45.940Z
model: claude-fable-5
effort: high
transcript: agent-ad6558e4768ab4666.jsonl:143
uuid: f34e7c89-bc59-4ff7-96bd-9504765fcab2
---

# 040 -- The executable witness -- what came back

The subject's reply, verbatim. The turn that asked for it is
`../strata.replication.kb/040-witness.md`; the operator's
verdict on it is this file's commit message.

---

23/23 pass on first run — which is itself suspicious, so the honest review below includes what the *construction* broke, not just what the runner printed. Three of the passes only exist because writing the code falsified my account as previously stated; those are the findings.

## Artifact

`/home/bukzor/repo/github.com/bukzor/bukzor-agent-skills--replication-run/stratified-model/` — fresh subdirectory, nothing under `trash/` touched or listed.

- `l0.py` → `l1.py` → `l2_claims.py`, `l2_discourse.py`, `l2_task.py` → `l3.py` (one module per level; L2 is one level with three class modules — the plurality is the level's content, and the import test treats them as one rank)
- `test_l0.py` … `test_l3.py`, `test_imports.py`, `run_tests.py` — 23 tests, zero dependencies, `python3 run_tests.py`

Jargon table (source term → code object): ls-is-the-index → `Directory.ls`/`Node.index`; dated slug → `l1.dated_slug`; synthesis/elaboration pair → `l1.Node`; promote/flush section–retraction → `l1.promote`/`l1.flush` (`l2_task.task_promote` is the class refinement); schema conjunction → `l2_claims.valid_claim`; standing enum → `Claim.standing`; legal stop → `is_base`; provenness-as-inductive-predicate → `sound` (lfp); warrant mix → `warrant_mix`; retraction sweep → `sweep`; theory/ontology/priors → `Theory`/`vocabulary`; confinement → `confined`; placement → `placement`; internal index → `theory_is_live`; last-wins union → `apply_utterances`; discourse polarity → `Deduction.kind`; certification transport/span → `l3.transport_prose`/`transport_stored`/`cross_sweep`.

## Review, claim by claim

**Account was wrong — updated (3):**

1. **"A ring stands only on what enters it from outside" — I had misread my own gloss, and the code caught it.** My conjecture sketch said: add an outside user-signed premise to a ring member and both become sound. Under the lfp with conjunctive `why:`, that is false — `CD <- AB EX` stays unsound because the circular premise still blocks. The test (`test_ring_is_unproven_and_outside_support_must_rewire_not_add`) now witnesses both halves: adding does nothing; only *replacing* the circular edge proves the ring. Account updated: outside support must rewire, not supplement. This also surfaces a missing premise in the source itself: `why:` has no disjunction — one claim, one derivation — so if the ledger ever wants alternative derivations, LEAST_FIX must be restated over an AND-OR graph, and nothing in the corpus says so.

2. **Warrant-mix was incoherently specified.** The account said "lfp of union: the set of open/agent leaves in the support closure, over all claims." Two failures under execution: (a) the union-lattice lfp assigns a base-free ring the *empty* mix — zero debt for an unproven circle, absurd; (b) a sound claim can never rest on an open leaf (an open premise makes its conclusion unsound), so "open/agent leaves of a warranted claim" was contradictory as written. Account updated: warrant-mix = agent leaves, defined only on the sound fragment (`warrant_mix` returns `{}` for the ring — tested); open-leaf debt belongs to a distinct computed view ("what blocks this open claim"), which neither the model nor the source ships.

3. **Sweep completeness is not mechanically checkable, and the account now says so at the right strength.** The law was "sweep is complete iff arrows over-approximate real dependence." Writing the test forced the admission: *real dependence is stored nowhere* — the model had to smuggle it in as test-side oracle data (`SLY`, certified "assuming E" with no arrow). In vivo the oracle is the author's head; a single missing arrow is silent, unswept, and unlintable — graph-health's component count catches only gross arrow poverty. Reclassified from law to discipline-with-a-tripwire; the test witnesses the escape, not the completeness.

**Code wrong, or forced choices flagged rather than smoothed (3):**

4. **`retracted` as a fifth standing value contradicts the source schema's four-value enum.** The model needed *some* representation and the corpus offers four incompatible mechanisms (chat strikethrough, filename suffix, contrary verdict, standing change). I chose the standing value and marked it in the module docstring. Adjudication lands against the *source*: the file-ledger schema cannot represent retraction at all — the model made an existing gap undeniable rather than introducing one.

5. **The discourse evaluator is invented.** The class stores `status` and `likelihood` and ships no evaluation engine, so my non-monotonicity witness holds only conditionally: under any evaluator where contradiction lowers standing. That the witness *required inventing the engine* is the sharper finding: stored standing with no evaluator is unfalsifiable by the class's own machinery. Both discourse tests are marked as defect-witnesses — a future fix should break them.

6. **`l2_discourse` imports nothing, so the import test cannot compute its level** — it is declared in the `LEVELS` map. Not repaired, because it is faithful: tower placement is by act, exactly as adjudicated at stratification time.

**Candor notes, no mismatch (2):**

7. The conjunction cut-out test is true by construction — in the model as in reality (2020-12 conjunction semantics). It guards regression; it cannot fail today.

8. Conservativity got *sharpened*, not contradicted: the test proves it only for pure addition, and running it made plain that conservativity is not a theorem of ledger mechanics — last-wins would happily let a later theory overwrite a prior label. It holds because extensions only add; anything else is repair, legally located in the prior's own fiber (the llm-stet demotion episode is the data's instance).

**Not mechanically checkable, because (4):** ARROWS' permanent informality — a negative claim; any checker would constitute the semantics it denies. Floor-meaning invariance for prose engines — meaning is an act of reading; there is no formal semantics on either side to compare. Transport law (i), meaning-preservation of spans — cross-vocabulary interpretation is a judgment, hence properly a signed act, not a computation. Sense-shifted word reuse — string-level confinement (what the model and `grep` both check) cannot see senses; the diamond test shows the symptom (two minimal placements), not the cause.

**Net for the account:** the tower survived contact — every level's laws ran, the definability spine (index := ls, chronology := lex sort, carrier parsed from L1, standing computed not stored, span repair reusing the existing sweep) is now executable — and the three places it bent are exactly where the code was worth writing: conjunctive-`why:` rings, warrant-mix's domain, and sweep completeness demoted to discipline.
