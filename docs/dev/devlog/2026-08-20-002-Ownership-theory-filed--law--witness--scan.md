# Devlog: 2026-08-20 — Ownership theory filed: law, witness, scan

## Focus

File the vocabulary-licensing theory ("ownership") that the
formalize/deformalize session produced in chat, as
`llm-claims/design.claims.kb/ownership.{md,kb/}` -- 29 claims, a
runnable witness (`ownership.py`), a corpus scan
(`llm-claims-kb/bin/llm-claims-kb-ownership`), and the doc edits the
theory demands. Commissioned by the user: "do not edit others' trash.
what you may do is make a durable witness that's git-added. please
update kb."

## Decisions

### One flat theory, priors notation + purpose

**Rationale:** the words each part needs (label, theory, ontology,
stipulation, scan, check from `notation`; ledger, claim, reader, cost
from `purpose`) are needed across all parts -- a split into
sub-theories buys nothing. The container `DESIGN` licenses
skill/design/agent/user by containment.
**Alternatives considered:** five sub-theories mirroring the in-chat
ledger's clusters; rejected as arrows without payoff.

### User rulings filed this session (all dated 2026-08-20)

- **THREE_MOVES** (tentative by its own marking): reach = interior ∪
  ancestors ∪ importers' interiors. The ancestor move dissolves the
  parent-silent anomaly; EXPOSITION? and DIRECT_ONLY? are the named
  reopeners.
- **SYNTH_WHY_SMELL**: a synthesis citing bunches of its own children
  in `why:` is broken -- containment already carries the relation.
- **WHY_IS_FUSED**: support and vocabulary share `why:` deliberately;
  a lens disagreement is a factoring smell, not a field defect.
- **CHECK_OWNERSHIP**: single ownership is always checked -- "either
  mechanistically, in python, or agentically, in documented
  procedures." Mechanical = the new scan; agentic = the confinement
  audit.

### Retraction cascade

- **OWNABLE_IS_RESIDUAL** retracted (user correction): conflated
  repair triage with vocabulary governance; remainder filed as
  SHOULD_OWN?.
- **YIELD** retracted: `ownership.py nonmonotone` exhibits a move
  that discharges one finding and mints another, so the cull-first
  ranking fell; no replacement ranking claimed.
- **DOC_MISSES_IMPORT** and ARITY's "no shipped lint" clause would
  have been falsified by this very session's shipping; refiled as
  **ADMIT_PRICED** (the priced-admit commitment) and ARITY restated
  as "the data holds a relation where the law needs a function," with
  counts as dated data.

### Label renames (collision-forced, pre-flight against fleet labels)

The in-chat ledger used labels the fleet already holds or prefixes:

- REFERENCE → **DEFECT** (REFERENCE exists)
- NAME → **TWO_SORTS** (prefix of NAME_GRAMMAR, NAME_LOCUS)
- REACH_IS_THREE_MOVES → **THREE_MOVES** (existing REACH is a prefix)
- FORCE → **EXCLUSION_FORCE** (FORCE exists)

Folds: LABEL_ANSWERS_AT_HOME → DANGLING's body; NOT_IDENTICAL →
TWO_SORTS' body; RANK_STIPULATIONS → YIELD's retraction body.

### Witness and scan split

`ownership.py` (stdlib, pyright-clean) is the law on fixtures --
eight subcommands, one per `verify:` line. TDD retrofit: mutation-red
observed for the ancestor move (reach loses the root) and
outermost-wins (owner returns the inner stipulator); both restored.
`llm-claims-kb-ownership` reads the real fleet: sibling doubles fail
(exit 1), nested pairs inert (OUTERMOST_WINS), foreign pairs legal
(per-ledger namespaces), `--idle` is an adjudication queue and never
an error.

## Conventions Established

- The theory's own prose was scanned for word-sort trespasses against
  its unlicensed siblings (stance, good-smells): every hit is a word
  double-stipulated by a licensed prior too (cost, notation, reader,
  entry, ontology via purpose/notation; design via the container) --
  the adjudication-zone cases, not clean trespasses.
- Figures refreshed post-filing, since filing changes them: doubles
  13 sibling / 6 inside / 61 foreign (was 57); imports 4 idle of 52
  (was 50); 326 stipulations (an earlier probe said 338 -- the strata
  restructure landed in between); label citations 92 = 91 self + 1
  direct + 0 transitive-only (was 63/62/1/0).

## Open Questions

- SHOULD_OWN? -- what decides a word wants a stipulation; force
  cannot rank the unowned.
- EXPOSITION? -- if synthesis prose should avoid coinages, the
  ancestor move loses its motivating case and THREE_MOVES reopens.
- DIRECT_ONLY? -- transitive-import licensing carries zero measured
  traffic; eliminating it is assessed but not ruled.
- ANSWERABLE_IS_LOCAL? -- cousins/nephews are unlicensed and
  unanswerable: a violation no one may prosecute.
- Not touched, awaiting the user's word: the 13 sibling-double and 4
  idle-import fleet adjudications, the transitivity cut in
  mentions/`llm-claims-kb/SKILL.md`, `llm-claims/SKILL.md:88`'s norm
  sentence, CONFINE's wording.

## References

- `llm-claims/design.claims.kb/ownership.md` and `ownership.kb/` --
  the theory; `ownership.py` -- the witness.
- `llm-claims-kb/bin/llm-claims-kb-ownership` -- the scan;
  `llm-claims-kb/SKILL.md` § bin/llm-claims-kb-ownership.
- Bundled drafts: the working tree carried a prior session's
  uncommitted four-way confinement menu in
  `llm-claims-kb/SKILL.kb/self-audit.kb/confinement.md` and
  `llm-claims/SKILL.md`; this session's admit bullet lands on top of
  it, and the commits carry both.
- devlog 2026-08-20-001 (strata) -- the concurrent session whose
  restructure moved the corpus counts mid-measurement.
