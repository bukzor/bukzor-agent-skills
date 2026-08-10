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

### llm-claim-ledger's own ledger caught up with its manual

**Rationale:** the user observed the session's clarity concentrated on
llm-claim-ledger while the records landed elsewhere. Diagnosis: the
manual (`SKILL.md`, `SKILL.kb/`) was already current — rulings landed
there as they happened — but `design.ledger.kb/` lagged, and
notation.kb's charter says decisions live there, instructions in
SKILL.kb. Filed SPLIT (user; the 2026-08-09 split-trigger ruling,
previously manual-only, with the rejected count-trigger on record) and
PLACEMENT (agent; the cheapest-judge law proper-noun-free — the
generator behind the sigil aphorisms, and the ledger-side face of
what fleet.kb/COURTS aligns). Widened notation.kb's ontology with
words its standing claims already used (theory, ontology, prior,
defeater, veto) — the ENFORCEABLE failure mode caught in the
ENFORCEABLE claim's own collection. (Commit `0a79876`.)
Revised same day on the user's correction: the cost accounting ran
backward -- `!` records a judgment already sunk, so a correct `!`
only reduces cost and its duty is being honored, while every `+`
issues new debt against the user's next scan, warrant being the
question the writer signs. Standing raised to `user`; the mismatch
bills and the declined alternative remain agent prose. Also the
occasion for a claim-shape ruling request: quotable commitment first,
cases as parallel bullets, argument subordinated.
**Alternatives considered:** enriching SKILL.md with the reasoning —
rejected; the manual's audience pays for reasoning it doesn't need,
and the aphorisms already carry the operational content.

### Documentation-optimization doctrine persisted

**Rationale:** the PLACEMENT correction surfaced a general doctrine
worth keeping: text is priced by load frequency, and each tier has
its own objective — hot text (core blocks, descriptions) minimizes
recurring tokens, per-invocation text optimizes the invoker's next
action, cold text (design ledgers, ADRs, devlogs) optimizes for
extraction and veto-addressability, where brevity is the wrong
objective. Filed as `authorship.kb/TIERS` (agent, refining
LOAD_COST), with the claim-body shape as a "Claim bodies" directive
in llm-claim-ledger-kb's manual — decision in the ledger,
instruction in the manual, stated once each. (Commit `14310b8`.)
**Alternatives considered:** a good-smells claim for the shape —
deferred; one conversation old, let it survive a second application.

### llm-claim-ledger[-kb] renamed to llm-claims[-kb]; .claims.kb suffix adopted

**Rationale:** the ledger skill pair predated `Skill(llm-kb)`'s `.kb`
convention and was never brought under it — every `.ledger.kb`
collection named nothing about its containing skill. Renamed
`llm-claim-ledger` → `llm-claims`, `llm-claim-ledger-kb` →
`llm-claims-kb` (the X/X-kb pairing forces both), and every
`*.ledger.kb/`, `*.ledger.md`, `*.ledger.jsonschema.yaml` in the repo
to `.claims.kb`/`.claims.md`/`.claims.jsonschema.yaml`, plus the two
graph tools (`llm.ledger-graph` → `llm.claims-graph`,
`llm.ledger-dot` → `llm.claims-dot`). Sought symmetry:
`llm-kb : .kb :: llm-claims-kb : .claims.kb`. Accepted cost: the
ledger form now shares the bare word "claims.kb" with
`llm-discourse-graph`'s node-type collection; mitigated by the
ledger form never appearing bare (always stem-prefixed) and by
`llm-claims-kb/SKILL.md`'s "What this is not" disambiguating by
shape (sibling node-type collections vs. `standing:`-and-theory
frontmatter) rather than by word. The concept name "claim ledger"
stays in prose throughout — only artifact names moved. Historical
records (this devlog, other ADRs) keep the old names as provenance;
sister repos (`prototype.personal-reasoning-management`'s
`design.ledger.kb/`, `corpus/ledger.kb/`) are a separate pass, not
done here. Full ruling: `docs/dev/adr/2026-08-10-000-Adopt-the-claims-kb-suffix--rename-the-ledger-skills.md`.
(Commits `03f6254`, `879de9a`, `00721a9`.)

While in `llm-claims-kb/SKILL.md`: added `SKILL.kb/self-audit.kb/`,
four ledger-specific rot audits (standing honesty, graph health,
confinement, stamp freshness) that cite `Skill(llm-kb)`'s own
`.kb`-generic audits by reference rather than copying them, plus a
line stating a claims.kb inherits every `llm-kb` audit wholesale.
The tool docs for `bin/llm.claims-graph` were thinned to
purpose/usage/output, with the how-to-read-the-drawing prose moved
to `self-audit.kb/graph-health.md` where the audit-file genre wants
it, leaving one pointer line behind.
**Alternatives considered:** keeping `.ledger.kb` and renaming only
the skill pair — rejected, it would leave the skill's own
collections off the convention its sibling skill (`llm-kb`)
established two months earlier.

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
  stated" is fully true only for renames. (The fourth nit, "the two
  laws", fixed in `0a79876`.)
- Witness test for RESTRICT — filed in `.claude/todo.md`.

## References

- Commits: `bfc9966`, `5ce167e`, `aaaaa65`, `51f82bf`, `0a79876`,
  `03f6254`, `879de9a`, `00721a9`
- `docs/dev/strata.ledger.kb/fixpoint.kb/triangular-operators-restrict.md`
- `docs/dev/strata.ledger.kb/fleet.kb/the-courts-are-the-sigils.md`
- `llm-claim-ledger/design.ledger.kb/notation.kb/settle-at-the-cheapest-judge.md`
- `llm-claim-ledger/design.ledger.kb/notation.kb/a-theory-splits-on-cost-not-count.md`
- `docs/dev/devlog/2026-08-09-*.md` — the prior arc this continues
- `docs/dev/adr/2026-08-10-000-Adopt-the-claims-kb-suffix--rename-the-ledger-skills.md`
- `llm-claims-kb/SKILL.kb/self-audit.kb/`
