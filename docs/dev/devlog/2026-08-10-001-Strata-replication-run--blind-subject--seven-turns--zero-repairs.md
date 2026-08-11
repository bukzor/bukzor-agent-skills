# Devlog: 2026-08-10 — Strata replication run: blind subject, seven turns, zero repairs

## Focus

First execution of `docs/dev/strata.replication.md`: a blind
re-derivation of `strata.claims.kb/` by a fresh frontier-tier agent,
operated turn-by-turn from `strata.replication.kb/` with every paste
sent verbatim. Turns 010–070 all landed on their success criteria on
the first send; the 020 repair paste was never needed. The eighth
turn was sent into a broken ledger and is void — see below. The run
therefore stands at seven stages, each one commit in
`strata.replication.run.kb/` on branch `strata-replication-run`.

## The setup

The subject ran in a dedicated worktree (sibling directory
`bukzor-agent-skills--replication-run`) because the live tree carried
the `.ledger`→`.claims` rename staged but uncommitted: worktree at
HEAD, working diff applied, sealed with a bland `wip` commit so a bare
`git status` shows clean instead of listing answer paths. Operator
additions to the pastes totaled one sentence (the working directory);
everything else was the turn files as written.

The run committed nothing while it ran — the defect that later made
its middle unrewindable. The per-stage history was reconstructed
afterward from the subject's transcript (`extract-stages.py`), and the
next run commits as it goes.

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
- 040 witness: hit — `stratified-model/`, 23/23 (operator re-ran
  them), with three account-was-wrong rulings out loud (rings repair
  by rewiring, not supplementing; warrant-mix restricted to the sound
  fragment; sweep completeness demoted to discipline) and two rulings
  against the source (retraction unrepresentable in the file schema;
  stored discourse standing unfalsifiable absent an evaluator).
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

Subject cost: ~813k subagent tokens, ~3.9h wall.

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

## The eighth turn, and why it is not filed

080 (the critique) went out against a checkout whose
`strata.claims.kb/jsonschema/claim.jsonschema.yaml` was left dangling
by the `.ledger`→`.claims` rename — every per-theory `$ref` dead, the
ledger's own typing judgment unevaluable. A critique turn spends its
depth on whatever is broken, so that is what it bought.

The answer is void and is not recorded here: with the rot repaired
the turn wants asking again, and an audit written against a repaired
ledger must not be seeded with the one written against a broken one.
Re-asking the same subject is not a rewind — its first answer stays
in its context, and it will spend the new turn revising the old.
080 therefore waits on a subject restored to the pre-080 state; the
environment for it is tagged `run/pre-080`.

## The verdict on the headline question, seven stages in

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
- **The seams: unsettled.** Whether the blind run patrols better
  where the ledger declares but doesn't check is exactly what 080
  buys, and 080 has not yet run clean. What 070 produced on its own
  is six filable claims, below.
- **Procedurally: the turn files work.** The original run needed
  mid-course corrections; the front-loaded turns needed zero repairs
  across seven sends. The study is repeatable as written — with one
  addition the next run needs: repair the ledger's mechanical rot
  before the critique turn, and commit each stage as it lands.

## Awaiting adjudication (the run's deliverable so far)

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

## Open Questions

- 080, re-asked from `run/pre-080` of a subject restored to its
  pre-080 state — blocked on the rewind procedure
  (`strata.replication.md`, "Rewinding a run").
- 090 (the open-vetoes walkthrough) after it: its reply is rulings,
  which only the owner can give.
- Adjudication of 070's six claims — owner's court, then they land
  as diffs per `Skill(llm-claims-kb)`.
- Disposal: the branch and worktree once anything worth promoting is
  harvested — the subject's ROUNDTRIP test is named as a direct port
  into `engine_tower/view.py`. `strata.replication.run.kb/` merges to
  main when the run is finished.
- Where agreements-by-different-routes should be recorded as `why:`
  evidence, per the study doc — a sweep over the convergent claims.

## References

- `docs/dev/strata.replication.md` and `strata.replication.kb/` —
  the procedure; blind-list sharpening landed this session.
- `strata.replication.run.kb/` on branch `strata-replication-run` —
  the stages, one commit each, based at the frozen environment.
- Operator session `a299f67e-8eda-4c26-832e-94a02102b60a`; the
  subject's own transcript is
  `<projects>/a299f67e-…/subagents/agent-ad6558e4768ab4666.jsonl`,
  cited line-by-line from the stage files.
- `docs/dev/devlog/2026-08-09-*.md`, `2026-08-10-000-*.md` — the
  original arc this run replicates and audits.
