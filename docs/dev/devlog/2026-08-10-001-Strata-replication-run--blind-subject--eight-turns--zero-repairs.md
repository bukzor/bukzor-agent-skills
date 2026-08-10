# Devlog: 2026-08-10 — Strata replication run: blind subject, eight turns, zero repairs

## Focus

First execution of `docs/dev/strata.replication.md`: a blind
re-derivation of `strata.claims.kb/` by a fresh frontier-tier agent,
operated turn-by-turn from `strata.replication.kb/` with every paste
sent verbatim. Turns 010–080 all landed on their success criteria on
the first send; the 020 repair paste was never needed. The run ends,
by design, at the edge of user territory: 080's proposed defeats and
070's filable claims await adjudication, and 090 awaits the owner.

## The setup

The subject ran in a dedicated worktree (branch `replication-run`,
sibling directory `bukzor-agent-skills--replication-run`) because the
live tree carried the `.ledger`→`.claims` rename staged but
uncommitted: worktree at HEAD, working diff applied, sealed with a
bland `wip` commit so a bare `git status` shows clean instead of
listing answer paths. Operator additions to the pastes totaled one
sentence (the working directory); everything else was the turn files
as written.

## The run

- 010 survey: hit — shapes and tensions, no theory; one labeled
  contamination (below); subject self-widened the blind past the
  letter (skipped `design.claims.kb/` and the 2026-08-09 ADR unasked).
- 020 conjectures: hit — seven candidates over three quoted itches,
  three killed informatively (no cross-session merge order exists;
  the cost calculus compares but never composes), four worked in
  full. No name-dropping; repair unused.
- 030 strata: hit — levels as (vocabulary, artifacts, engine, laws)
  with cut-out/blind/conservative conditions; laws re-checked per
  level (its S1 false of discourse-graph, inexpressible at generic
  kb, under-describing the kernel rung); thesis "carrier below, laws
  at the level, values computed."
- 040 witness: hit — `stratified-model/` in the worktree, 23/23
  (operator re-ran them), with three account-was-wrong rulings out
  loud (rings repair by rewiring, not supplementing; warrant-mix
  restricted to the sound fragment; sweep completeness demoted to
  discipline) and two rulings against the source (retraction
  unrepresentable in the file schema; stored discourse standing
  unfalsifiable absent an evaluator).
- 050 freeze: hit — one-page picture with per-abstraction costs;
  in-chat ledger, nine named theories, ~40 claims, corpses kept
  struck-through.
- 060 questions and bets: hit — five questions each stated
  as-experienced and well-posed; the retention question split into
  design (validators carry most retention) vs procurement (Lean
  stays; Alloy as the counterexample inner loop; Agda's edge real
  but at the wrong margin); bets pre-registered, title-contaminated
  ones self-marked "(T)" and clean bets isolated.
- 070 reveal: hit, no deference — bets graded 7 called / 1 clean
  miss ("the answer will lack an executable model", bet while
  holding `/deformalize` — "I read it as a spec and should have read
  it as a fossil"); four rulings on what the structures are, three
  decided against itself on data evidence (fibered standing carrier;
  stamped-cache economics over its computed-never-stored maxim; the
  nine-theory carving), the fourth split productively (conjunctive
  rows: their carrier, its authoring law).
- 080 audit: hit — all 55 claims checked against the filing rule,
  graph tool run (acyclic, one component), eleven defeats proposed
  (below), simplicity pressed via three attempted theory-merges,
  each shown to destroy a load-bearing distinction.

Subject cost: ~813k subagent tokens, ~3.9h wall across the eight
turns.

## Contamination log

One leak, labeled immediately by the subject: an `ls` of
`docs/dev/devlog/` exposed entry titles — "engine tower",
"FREE-CONSERVE", "courts are sigils" (a near-verbatim claim
filename), including one from a 2026-08-10 title outside the
date-pinned ban. Consequence: 010's exclusion list was date-pinned
while the answer's vocabulary kept spreading into later-dated files.
Repaired this session: 010 now excludes `devlog/`, `adr/`, and
`design.claims.*` wholesale, bans listings of excluded directories,
and extends the git ban to "2026-08-09 or later". The subject's
(T)-marking of contaminated bets is the model response and is worth
keeping as an expectation.

## The verdict on the headline question

The question the study was built to answer: would a
`/formalize`-style prompted run produce a .kb of equal or better
quality than the hand-built `strata.claims.kb/`?

- **Equal on the skeleton, by an independent route.** The blind run
  converged on acts-as-authority, computed standing, the lfp core,
  confinement/conservativity, grade-bound laws, and the self-applied
  tower — FLOOR nearly verbatim, the import-poset test independently
  chosen as keystone. Convergence-by-different-routes is the
  strongest validation either account could get, and it is now
  evidence the agreeing claims' `why:` can cite.
- **Not better at the core.** By the subject's own adjudication the
  held ledger won three of four structural rulings, and its deepest
  content (COMPLETION, OVERSHOOT, FREE_CONSERVE-via-RESTRICT) traces
  to what the subject named "carrier fidelity under escalation" plus
  incident-driven discovery — depth the scripted prompts did not
  reproduce: the subject's simplifications deleted the bug's type
  before escalation could find the bug.
- **Better at the seams.** The blind run patrolled where the ledger
  declares but doesn't check: six filable claims, two live integrity
  holes the ledger's own authors missed, and an eleven-defeat audit.
  The composite of the two accounts is better than either.
- **Procedurally: the turn files work.** The original run needed
  mid-course corrections; the front-loaded turns needed zero repairs
  across eight sends. The study is repeatable as written.

## Awaiting adjudication (the run's deliverable)

080's proposed defeats, condensed one per line; full argument in the
session transcript.

1. `strata.claims.kb/jsonschema/claim.jsonschema.yaml` — symlink
   dangles since the rename; every per-theory `$ref` dead; the
   ledger's own typing judgment unevaluable, unswept.
2. WORD + ASYMMETRY jointly — the retracting act is unspecified:
   append-only store, removal-shaped retraction, no typed act; the
   corpus exhibits four ad-hoc forms. (= 070's RETRACTFORM, open.)
3. ASYMMETRY — `bare` over-covers: "retraction is a change of
   operator" is an unsigned modeling ruling.
4. `view.kb/always-fresh-is-impossible.md` — `bare` on a CAP cite
   whose hypotheses no claim asserts; real warrant is SCALE — a
   judgment in a theorem's clothes.
5. `standing.kb/the-status-order-is-not-a-complete-lattice.md` — the
   user-signed repair is implemented nowhere and uses words
   ("antichain", "downset") no ontology admits; an open claim hiding
   in a theorem's file.
6. `genre.kb/together-they-are-the-satisfaction-condition.md` —
   `bare` states as textbook what is an agent identification (the
   ledger has theory inclusions, not arbitrary signature morphisms).
7. `reference.kb/weights-generalize-provenance.md` — path sum
   diverges on a cyclic quiver; the DAG hypothesis lives only in an
   engine docstring.
8. `fleet.kb/CLAUDE.md` — defeater "any named system changing" is
   true on every commit: weather, not a kill condition.
9. `question.md` EXTENSION and SEMANTICS rows — drifted from the
   claim files' `why:` and unstamped: an unlawful cache inside the
   ledger that defines lawful caching.
10. GRADE and DERIVATIVE — definitions signed `agent`; the sigil is
    spent on nothing (ASSESSOR half-shares the defect).
11. `fixpoint.kb/triangular-operators-restrict.md` — grade defeat:
    the keystone lemma has no `verify:` while its dependents claim
    tooling grade (matches the standing todo for a RESTRICT witness).

070's six filable claims (proposed placements, all `+` except the
open one): RING → `standing.kb/` (conjunctive rows repair by
rewiring); ROUNDTRIP → `view.kb/` (promote/flush is a
section–retraction; classes refine the preserved invariant);
RETRACTFORM → `history.kb/` (open); NOEVAL → `fleet.kb/`
(discourse-graph caches without a view — TRIANGLE unstatable, one
grade below stale); CHRONO → `history.kb/` (substrate realizes order
lexicographically; zfill is contract); ORACLE → `reference.kb/` (the
quiver under-approximates dependence; prose spans are the live
instance). Two self-withdrawn: the NOMERGE sharpening and the
warrant-mix metric (WEIGHT subsumes it).

Subject's single highest-value change: bind the ledger's own record
layer to a computer — repoint the schema symlink, add a
validate-all-claims + graph-acyclicity check, name it in a `verify:`
so it is a law rather than a habit.

## Open Questions

- Adjudication of the eleven defeats and six claims — owner's court,
  then defeats land as diffs per `Skill(llm-claims-kb)`.
- 090 (the open-vetoes walkthrough) not yet sent: its reply is
  rulings, which only the owner can give. The subject is resumable
  in place for it after adjudication.
- Disposal: the worktree and branch `replication-run` (holding
  `stratified-model/`, 23/23) once anything worth promoting is
  harvested — the subject's ROUNDTRIP test is named as a direct port
  into `engine_tower/view.py`.
- Where agreements-by-different-routes should be recorded as `why:`
  evidence, per the study doc — a sweep over the convergent claims.

## References

- `docs/dev/strata.replication.md` and `strata.replication.kb/` —
  the procedure; blind-list sharpening landed this session.
- Operator session `a299f67e-8eda-4c26-832e-94a02102b60a` (this
  projects dir) — full subject replies live in its task
  notifications; the subject itself is a sidechain of it.
- Worktree: `../bukzor-agent-skills--replication-run`, branch
  `replication-run`, subject artifact `stratified-model/`.
- `docs/dev/devlog/2026-08-09-*.md`, `2026-08-10-000-*.md` — the
  original arc this run replicates and audits.
