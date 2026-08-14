# Devlog: 2026-08-13 — Answering the audit, and the record that was sitting in the subject's tree

## Focus

The replication run's 080 turn — the adversarial audit of
`strata.claims.kb/` — had landed and been graded. This session filed
its findings as diffs, then set up a re-run of 080 against the repaired
ledger. The re-run never went out: the operator called a halt, lost in
the churn. That halt is a finding too, and is recorded at the bottom.

## The audit's top three were already fixed, by someone else, first

080 was sent 2026-08-12 09:14 against a worktree frozen at 2026-08-10.
The 2026-08-11 migration (448e8a1, "A theory is a claim") was 18 hours
old and invisible to it. Its single highest-value recommendation,
verbatim — *"promote the theory definitions to signed claims … give
strata.claims.md its frontmatter as the ledger's defining claim, reduce
the CLAUDE.md headers and the entry-point table to views of those
files"* — is that migration, reached independently, by a different
route, with no contact between the two sessions.

Two accounts agreeing by different routes is the whole point of running
a replication. This is the strongest instance the run has produced, and
it arrived by accident, from a subject auditing stale state.

## What the remaining eleven bought

`52e6c55` (engine, 27 → 32 tests) and `befce32` (ledger):

- **MERGE, filed `open`.** WORD called a store "a word in the free
  monoid of updates — a DAG of transactions where branching is allowed".
  A word is linear; the gloss contradicted the claim it glossed. FOLD is
  defined on words, no claim said what a merge folds to, and the engine
  witnessed linear histories only. Gloss struck, gap filed, witness
  added that *exhibits* the gap rather than closing it: two
  linearizations of one branch pair fold to different states. `grep
  '^standing: open'` now returns two — a theorem owed, a law missing.
- **The poset got a computer.** `test_tower.py` mirrored the theory
  poset by hand, its own comment admitting "mirrored BY HAND … update
  both together". By RETENTION's own criterion — a property survives iff
  it is a law with a computer — the poset was the least-protected thing
  in the system. It now reads each theory's priors out of the twelve
  `<theory>.md` `why:` lines; the hand copy is deleted, not checked. The
  derived restriction reproduced the old table exactly.
- **OPERATOR's parenthesis became true.** "Raising each entry as far as
  the evidence citing it *(through the reference structure)* supports"
  was unrealized: `Evidence.premises` was a bare key set no quiver
  touched, and `test_protocol.py` hand-wrote the same `g→m` edge into
  both carriers. `cite()` reads premises off the quiver; the test writes
  the edge once.
- **Four standings made honest.** SATISFACTION stood `bare` on a
  misidentification — conservativity is not the satisfaction condition,
  it is a further property that can fail in an institution — so it now
  *instantiates the preconditions*, signs `agent`, and the filename
  follows the verb. ASYMMETRY keeps `bare` by dropping an architectural
  rider its priors do not cover. COMPUTED cites COMPLETION, which
  nothing cited, and names the completion its own least fixpoint needs
  to exist. TAINT names DRed and says why support counts alone cannot
  tell grounded support from a loop.
- **Confinement enforced on the enforcers.** FRESH_COST lost CAP and the
  distribution vocabulary no ontology admits and rests its arithmetic on
  SCALE, cited; FOLD says stores, not replicas; REGROUND says view, not
  theory; `quotient` moved to `fixpoint`, where the mathematics is.
- **question.md states its view function and obeys it**; the two
  `defeated-by` lines that were unfalsifiable in practice gained
  thresholds. (Both keys have since been renamed `stale-when:` by
  another session — see `2026-08-13-000-*`.)

One of the audit's own claims did not survive checking: its lead
evidence, "the skill's own graph tool crashes on the ledger at file
one", is a usage error — the tool takes the collection directory, and
given one it reports 55 nodes, 100 edges, one component, acyclic. The
corroboration was withdrawn in the stage commit; the defeats it was
offered for stand on frontmatter evidence that does hold.

## The leak found while rewinding

Re-running 080 needs three rewinds (see `2026-08-11-000-*`). Rebuilding
the environment surfaced a fourth problem, which the first run had and
nobody noticed: **`strata.replication.run.kb/` was committed on the
branch checked out in the subject's own worktree.** The subject's prior
answers, and the operator's verdicts on them in the commit messages,
sat in the tree the subject reads. Harmless while a run only moves
forward; fatal the moment a turn is re-asked — the rewind undone by a
`cat`.

So the record moved to `main` (e6e87f6) and the environment became a
throwaway branch: **a root commit**, message `wip`, built from `main`
with `devlog/`, `adr/`, all of `strata.replication*` and `.claude/todo*`
deleted. `git log` in that worktree prints one line. The first run's
seal was a `wip` commit on top of real history, which left every
operator commit message readable.

Merging `main` into an old environment branch was tried first and
abandoned: the original seal had captured a half-finished rename, so the
merge produced rename/delete conflicts for a tree nobody wanted to keep.
An environment is a checkpoint, not a line of work — rebuild it.

`strata.replication.md` now says all of this.

## A paste is a whole file now

Turn files kept their send-ready text inside a fence, under frontmatter
(`blind: true`) and an operator note saying what a miss looks like.
Sending meant hand-selecting the inside of a fence with the run's own
design one line above the selection. Each paste is now
`instructions.d/<turn>.md`, extracted byte for byte and verified by diff
against HEAD; the turn file keeps what is the operator's, and a pointer.
Select all, send.

## The halt

The operator's word, at the end: *"I'm so very lost. so much as changed
and i cant tell what's better versus broken. i'm tempted to reset
everything to two days ago."*

Worth recording precisely, because the diagnosis is not "the work was
wrong". Twenty commits landed in this repo in two days; four were this
session's. Peer sessions did the rest — the theory migration, the
`defeated-by:` → `stale-when:` rename across every claim, `FLEET_MAP` →
`ATLAS`, six commits of validator refactoring, three of which landed
while this session was mid-report. Every check was green throughout and
is green now (32/32 engine tests, zero flatten lints, 68 files 0 errors)
— which is exactly the problem: green checks say nothing about whether a
person can still find their way around.

Parallel agents on one tree buy throughput and spend orientation. The
spend is invisible in the commit log, and no lint reports it.

The run is parked, not cancelled: nothing expires, the cut transcript
and the sealed branch keep, and 080 can be re-sent against whatever the
ledger looks like whenever the operator says. Reverting any of this
session's four commits is one `git revert` each, offered and not yet
answered.

## Open Questions

- Keep or revert this session's four commits. Two of them edit
  `user`-signed claims (WORD's gloss, one word in REGROUND) — corrections
  that changed no ruling, but that an agent should not make unilaterally.
- What rate of change a single operator can actually track, and what the
  swarm owes them: a digest, a slower cadence, a lock on shared files.
  This session's answer was a report, and the report was itself part of
  the flood.
- `env-2026-08-13` is not private: peers commit onto it (186e256,
  31f0b70). The seal erodes with every one.

## References

- `2026-08-11-000-*` — the three rewinds and why re-asking is not one.
- `2026-08-13-000-*` — the `stale-when:` rename, another session.
- `docs/dev/strata.replication.md` — the environment and the rewind, as
  procedure. `strata.replication.run.kb/CLAUDE.md` — why the record is
  not the environment.
- `strata.replication.run.kb/080-defeats.md` — the audit, verbatim.
- Cut subject session `d7f2e549-1e8e-4981-99aa-780f9868341b`.
