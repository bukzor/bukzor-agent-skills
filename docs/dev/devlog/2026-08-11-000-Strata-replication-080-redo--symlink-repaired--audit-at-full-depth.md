# Devlog: 2026-08-11 — Strata replication 080 redo: symlink repaired, audit at full depth

## Focus

The first 080 audit led with the dangling schema symlink and spent its
depth on record-layer rot. The rot was mechanical rename fallout —
main had already fixed it; the subject's worktree froze the moment
before the fix. Repaired the worktree symlink (`8685b51` on
`replication-run`), re-issued 080 verbatim to the same subject with a
two-sentence preface (discard the prior audit; re-derive from scratch;
don't re-litigate the fix), and got the audit the turn was designed to
buy. **This entry's defeat list supersedes the eleven in
`2026-08-10-001`** as the adjudication input.

## What the now-live tooling reports

With the `$ref` chain repaired the subject could run what the dead
chain had blocked, and the ledger's record layer came back clean at
tooling grade: schema sweep over all 55 claims — zero findings; all
21 distinct `verify:` commands pass, none selecting zero tests; graph
55 nodes / 100 edges, one component, acyclic, no rings. The discipline
the claims describe is the discipline the files practice — evidence
the distracted audit structurally could not produce.

## Reversals (subject's own, against its discarded reply)

- ASYMMETRY mis-standing complaint withdrawn: the "removal of
  Evidence rows" line lives in an engine docstring, not the claim; the
  gap survives as a *missing* claim, not a wrong standing.
- GRADE/DERIVATIVE "definitions wearing signatures" largely
  withdrawn: the bodies carry substantive theses; the signatures work.
- question.md finding changed character: the table IS stamped, so
  plain staleness would be lawful DEBT — the surviving defect is
  drift-at-birth (below), which is sharper.
- "history's ontology admits unused words" reversed into defeat 1:
  WORD's body does use "branch"/"transaction", and that is worse.

## The eleven defeats (superseding list)

1. `history.kb/the-store-is-the-history.md` — WORD asserts two
   non-isomorphic carriers in one sentence (free monoid; DAG with
   branching); FOLD and every "recompute from the word" are defined
   only on the ordered carrier; no claim folds or merges a branch.
2. `standing.kb/evidence-induces-a-monotone-operator.md` + WORD — the
   retracting act is named nowhere: in an append-only store removal
   must itself be an appended act; corpus shows four ad-hoc forms; an
   open claim OBLIGATION should have as a sibling, filed nowhere.
3. `standing.kb/the-status-order-is-not-a-complete-lattice.md` — the
   completion repair is decided-but-unbuilt, its vocabulary admitted
   by no ontology, its only verify certifying the crash: acceptance
   debt wearing a settled claim's face.
4. `view.kb/always-fresh-is-impossible.md` — the super-linear
   arithmetic rests on SCALE's regime premise, absent from `why:`;
   `bare`'s license is "follows from its premises."
5. `genre.kb/together-they-are-the-satisfaction-condition.md` — the
   ledger has theory inclusions, not signature morphisms; "the
   defining axiom of an institution" claims absent apparatus.
6. `fleet.kb/CLAUDE.md` — defeater "any named system changing" is
   true on every commit; the theory's own authors route around it
   twice rather than restating it — a defeater its theory disbelieves.
7. `strata.claims.kb/question.md` — EXTENSION and SEMANTICS rows
   disagree with their files' `why:` since the birth commit: the
   evidence-diff-since-stamp protocol returns empty while the table
   is wrong — DEBT's one named sin, inside the theory defining it.
8. `llm-claims-kb` schema vs 17 claim files — "a certified claim's
   standing is bare" is contradicted by 17 of 25 verify-bearing
   claims standing `agent`/`user`; practice is the defensible side,
   convicting the schema prose of lacking the concept of a verify's
   *scope*. (New finding; the repaired chain made the census
   possible.)
9. `reference.kb/weights-generalize-provenance.md` — REACH's preorder
   admits cycles; WEIGHT's path sum diverges on one; the DAG
   hypothesis lives only in an engine docstring.
10. `fixpoint.kb/triangular-operators-restrict.md` — the ledger's
    most-leaned-on lemma is the only fixpoint claim with no
    `verify:`; the keystone sits at attention grade.
11. `fleet.kb/the-courts-are-the-sigils.md` — "where the alignment is
    kept," and nothing watches it: no trigger on either taxonomy
    changing; a load-bearing invariant at attention grade in the
    throwaway theory. (New.)

Withdrawn from the old list: the symlink (repaired), old ASYMMETRY
(#3) and GRADE/DERIVATIVE (#10) per the reversals above.

## Lenses, condensed

- Alignment: the embodied goal is the user's; flagged for the user —
  purpose.kb's three regime axioms quietly re-price the whole tower
  (FRESH_COST, CONSERVE, STANCE, FLOOR lean on them) while being the
  least-examined claims in the ledger.
- Effectiveness: high; residual gaps are all one species — *declared
  but unpatrolled* (RESTRICT unbound, COURTS unwatched, the table
  underived, and every check run this turn exists only as ad-hoc
  session commands).
- Simplicity, pressed: the twelve-theory count survives — every
  attempted merge kills a load-bearing distinction; the accretion is
  intra-file and enumerable (question.md's Decomposed-by column:
  delete or derive; COURTS's concordance; WEIGHT's unused path-sets).
  "The ledger claims to be the simplification" survives the press.

## Bottom line (strengthened, both halves)

Theirs on what the structures are — reinforced, because the
machine-checked half came back clean. The subject's at the seams the
tower declares but does not patrol — every surviving defeat sits on
one, and the division has now survived two independent passes.

Single highest-value change, upgraded from the first audit's: a
`ledger-check` bank running the four checks done ad hoc this turn
(schema sweep, all `verify:` lines, graph acyclicity, table-vs-`why:`
diff), named in a `verify:` on AUDIT, with question.md's table derived
rather than authored. The symlink rot was an instance; this closes
the class. Runner-up content diff: resolve WORD's two-carrier
sentence and file the retraction act as OBLIGATION's open sibling.

## Open Questions

- Adjudication of the eleven (owner's court), then diffs per
  `Skill(llm-claims-kb)`. 070's six filable claims stand unchanged.
- 090 still unsent; subject resumable in place.
- Worktree/branch disposal unchanged from `2026-08-10-001`.

## References

- `2026-08-10-001-*.md` — the run this entry amends; its defeat list
  is superseded, everything else stands.
- Worktree commit `8685b51` — the repair.
- Subject reply: this session's task notifications (operator session
  `a299f67e`); redo cost ~149k tokens, ~6.5min.
