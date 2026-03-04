# Devlog: 2026-03-04 — Lane-mixing resolution and question/answer generalization

## Focus

Resolve the blocking question from CLAUDE.task.2.md: whether the unified
claim scheme can coherently serve all five target use cases (discussion
decomposition, design knowledge, live debate, knowledge base, sub-agent
fact-finding) without becoming useless for any of them.

## Decisions

### Lane-mixing: resolved — unification is coherent

**Rationale:** The five use cases are restrictions of a general
question→answer pattern, not conflicting requirements. Differences are in
which question types dominate and how rigorous validity values are. No use
case requires fields or mechanisms the others don't have. Per-party validity
handles the multi-voice/single-voice spectrum. Source attribution handles
provenance/temporal reconstruction.

**Objections tested (Jr/Sr adversarial review):**
- [Jr-1: zero-utility] Baseline is plaintext/llm.kb. Scheme adds validity, per-party, sources, why[]. Incremental cost, clear benefit. Defeated.
- [Jr-2: lcd-not-unification] JSON counterexample: minimal types, maximal generality, transformative. Defeated.
- [Jr-3: erotetic-unvalidated] Non-sequitur: lack of prior tooling ≠ impractical. Severable from scheme. Defeated.
- [Jr-4: no-practical-test] Argument FOR proceeding, not against. Defeated.
- [Jr-5: premature-contradiction-resolution] `mkdir` promotion is non-destructive. Defeated.
- [Jr-6: question-answer-unfalsifiable] Definitional framing is the point, like "every URL is a resource" in REST. Defeated.
- [Jr-7: experiment-validity-mapping] Truth = assessor's best estimate; methodology out of scope. Dissolved.

### Parentage generalized: why/how → question/answer

**Rationale:** The original why/how framing was the most common case (design
work) mistaken for the general principle. Evidence: Alice/Bob disagreement
has "what should?" parent; forensic analysis has "why?" parent; categorization
has "what Xs exist?" parent. All question→answer, only the last is
specifically why/how.

**Key formulation:** "Within this framework, parent/child relationships
SHALL be considered question/answer relationships."

### Contradiction resolved without `contradicts[]`

**Rationale:** Competing claims are siblings under a shared question-parent.
To contest a claim: `mkdir $(basename $claim .md).kb/` — promotes claim to
question with competing children. Non-destructive, no graph rearrangement.
Per-party validity expresses who endorses which position.

### Truth defined as assessor's credence

**Rationale:** Framework stores the result of assessment, not the methodology.
Sidesteps Bayesian/frequentist debate by placing it outside scope. Statistical
methods inform truth values but don't mechanically determine them.

## Conventions Established

- Directory names SHOULD spell out the question for disambiguation
  (e.g. `why-did-server-crash.kb/`). Rationale: self-documenting names
  repay verbosity in LLM-collaborative workflows where only names are
  visible (ls -RF, cross-session handoff, smaller models).
- `$NOUN.kb/` MAY be used as shorthand when the question type is obvious
  (implies "What $NOUNs exist?").
- Design tower = restriction of general scheme where all questions are "how?"
- Labeled objections ([Jr-N: short-name]) for structured debate tracking.

## Open Questions

- `why[]` conjunctive vs disjunctive (carried forward)
- Contesting reasoning vs conclusions (carried forward)
- Inline/short format tier (carried forward)
- Fate of `depends` alongside `why[]` (carried forward)
- Fixed layer vocabulary survival as naming convention (carried forward)

## References

- Living spec: `docs/dev/design/unified-claim-scheme.md`
- Component docs: `docs/dev/design/unified-claim-scheme/`
- Prior session: `docs/dev/devlog/2026-03-03-002-unified-claim-scheme-design.md`
- Session logs: sv-f0a0 (design), sv-bcb1 (why/how insight)
- Conversation conducted in scratch.vim-work/docs/sources/ working directory
