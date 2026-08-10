# Devlog: 2026-08-10 — Review passes: RESTRICT lemma, courts-are-sigils, skill polish

## Focus

Four passes — quality, coherence, factorization, mathematical
underpinnings — over the session corpus: `review-open-questions`,
`llm-claim-ledger`'s theory machinery, the authorship theory, and
`strata.ledger.kb/`. Mechanical ground truth first (kb-validate,
ledger-graph, engine-tower suite): all green before and after.

## Decisions

### RESTRICT: the lemma genre and tower share

**Rationale:** FREE_CONSERVE's one-two punch and SEAM's
freeze-the-floor both leaned on the same unstated order theory: on a
product lattice, a monotone operator whose first coordinate ignores
the rest has `pi1(lfp Phi) = lfp(phi1)`. Filed as
`fixpoint.kb/triangular-operators-restrict.md` (bare — settled
mathematics, standard behind stratified fixpoint semantics), per the
ruled split trigger: more than one theory leaning on a subsection
breaks it out as their shared prior. Payoff: confinement =
triangularity, so conservativity is a projection identity holding in
both directions at once — monotonicity's real job is only lfp
existence — and the lemma transfers to interval lattices, so
confined defeat evidence conserves too, which the ledger had not
claimed. OBLIGATION sharpened: the order-theoretic half stands bare;
the assistant owes the syntactic half (confined monotone rules
induce a triangular operator) plus glue. (Commit `aaaaa65`.)
**Alternatives considered:** leaving the lemma implicit in each
citing claim — rejected by the split trigger itself.

### The courts became an order

**Rationale:** the skill's law still said "There are two" after the
owner's zero-one-many ruling; the law never needed the numeral,
since "cheapest competent" presupposes an order. Now: courts ordered
by cost — record, check, witness, dearest of all the owner. Also
fixed a dangling antecedent ("Expect most of the batch to settle
here" sat in the owner's-residue paragraph while meaning the cheap
courts). (Commit `bfc9966`; also `5ce167e`, "a new theory, not a
second", in llm-claim-ledger.)

### COURTS filed in fleet.kb, not a skill's design ledger

**Rationale:** the un-persisted clarity of the session was the
correspondence: the review skill's courts and the ledger's sigils
are one verdict taxonomy — the assessor law and the status order —
at two enforcement grades (record = cite a standing `!`; check =
bare/certified; witness = `+`; owner = `!`; question = `?`; the
species rule is the `+`/`?` distinction). The authorship rules
forbid either skill citing the other, and
`llm-claim-ledger/design.ledger.kb/notation.kb` admits no proper
nouns, so the correspondence lives in the quarantine theory,
`strata.ledger.kb/fleet.kb/` (CONTINUUM is the precedent); fleet's
ontology widened to "the skills of this repo". (Commit `51f82bf`.)
**Alternatives considered:** llm-claim-ledger's design ledger — the
operator's first instinct; rejected on vocabulary (QUARANTINE), not
on topic.

## Conventions Established

- A skill and a notation that present the same structure get a
  fleet-correspondence claim as their alignment record, since
  authorship rules keep the artifacts themselves uncoupled.

## Open Questions

- A third recurrence of one shape — cheapest-competent-court (the
  skill), enforcement grades (GRADE), the status order's commitment
  force — reads as "a cost-ordered chain of computers; minimal
  placement; escalation changes grade, never meaning" (FLOOR, the
  wrong-court voidance, instance-witnesses-move-no-standing). One
  instance short of a tower claim, by the zero-one-many discipline.
- Prose nits awaiting veto: FREE_CONSERVE says "row" (record's word
  is "instance"); "node" appears in standing/genre defeaters but no
  ontology admits it; MIGRATE's "mechanical once the morphism is
  stated" is fully true only for renames; claim-ledger core's "the
  two laws" vs SATISFACTION's better "two halves of one law".
- Witness test for RESTRICT — filed in `.claude/todo.md`.

## References

- Commits: `bfc9966`, `5ce167e`, `aaaaa65`, `51f82bf`
- `docs/dev/strata.ledger.kb/fixpoint.kb/triangular-operators-restrict.md`
- `docs/dev/strata.ledger.kb/fleet.kb/the-courts-are-the-sigils.md`
- `docs/dev/devlog/2026-08-09-*.md` — the prior arc this continues
