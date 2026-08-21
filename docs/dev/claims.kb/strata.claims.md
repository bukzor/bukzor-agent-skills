---
label: ENGINE
standing: agent
ontology:
  - stratum
  - tower
  - regime
  - economics
  - extension
  - enforcement
stale-when: a lower engine needing a higher vocabulary
---

# The strata, as a ledger

The formal model of this repo's skill ecosystem: the engine is not one
thing but a tower of strata, each a small mathematical structure
derived over the fixpoints of the one below. `strata.claims.kb/` holds
the model as a claim ledger (`Skill(llm-claims-kb)`): one claim
per file, label and standing in frontmatter, one theory per collection.

Read `question.md` for what it was all bought to settle, `tower.kb/`
for the punchline, `fleet.kb/` for where the v1 skills and prior
prototypes sit in it. Argue with a claim by editing its file; the git
diff is the strikethrough.

## The picture

The whole tower, quotiented to one sentence and three laws.

**Authority belongs to acts; everything else is a projection; a
change is judged by what it forces to re-project.**

The invariant (`history`): an act is attributed and appended, never
edited. Everything derived from acts obeys four laws:

- **Regime** (`purpose`): the corpus outgrows any reader and entry
  stays near free; every law below is subject to that arithmetic.
- **Economics** (`view`, `standing`, `fixpoint`): a projection is
  fresh, maintained, or stale-with-a-stamp; the only sin is reading
  stale as fresh. `record` and `reference` are the legibility
  preconditions -- they make projections cheap enough to exist.
- **Extension** (`genre`, `tower`): new vocabulary never re-judges
  what stood below it.
- **Enforcement** (`protocol`): a law binds only through whoever
  computes it -- attention, tooling, or kernel.

So a "good idea" is new acts; its cost is the projections it forces
to recompute; a property survives it iff it is a law with a computer.
`fleet` is the worked examples.

This section is itself a projection of the ledger below, stamped
`last-updated` like any view -- argue with the claims, not with it.

## Theories

Claims are grouped by the vocabulary they need (`Skill(llm-claims)`,
§ Theories). Two are auxiliary -- `fixpoint` holds shared
background mathematics so that `reference` and `standing` can argue in
one sentence each, and `view` holds the derived-value machinery that
`standing` and `protocol` both lean on. A second root, `purpose`,
holds the operating regime -- the user's requirements about scale,
capture, and representational duty -- which `view`, `standing`,
`genre`, and `protocol` cite.

Two more sit above the spine as the serialization seam:
`data-structures` reads the inventory of generic carriers off the
central theories, and `data-representation` owes every carrier a
realization in every persistence target -- markdown document,
filesystem, datalog, program memory. The arrows point only down --
no central theory cites the pair -- so below the seam the ledger is
representation-free: `file`, `frontmatter`, `path` appearing in a
lower theory is a filing error, not a matter of style.

The spine, with auxiliaries feeding in:

```
history ──► record ──► reference ──► standing ──► genre ──► tower ──► fleet
    │                      ▲             ▲  ▲                 ▲         │
    └──► view ─────────────┼─────────────┼──┘                 │         ▼
    │        └──► protocol ┼─────────────┼────────────────────┘     question
fixpoint ──────────────────┴─────────────┘
purpose ───► view, standing, genre, protocol
history, record, reference, standing, view, protocol, genre
    └────────────────► data-structures ──► data-representation
```

That picture is hand-cut, and is the only hand copy left: the poset
itself is the `why:` lines of the fourteen `<theory>.md` files, and
`engine_tower/tests/test_tower.py` reads it from there to hold the
module import graph to it.

`fleet` is the throwaway theory; `question` is the historical one --
the design problems the ledger was bought to settle, with their open
residues, `question.md` the stamped synthesis. Theorems stand `bare`
(`fixpoint`, plus `REACH`, `FRESH_COST`, `TAINT`, `WEIGHT`, and the
act algebra's `ABSORB`, `LOCAL`, `BLIND`);
`OBLIGATION`, `MERGE`, and `RETRACTION` stand `open` -- a theorem
owed and two laws missing. The regime (`purpose`) and the claims the
user ruled in the 2026-08-09 act review stand `user`. Everything
else is signed `+`: the agent's judgment, veto invited, silence is
consent -- a resting state, not a queue awaiting signatures
(`Skill(llm-claims)`, PROVISIONAL).

## Verify

`verify:` commands run from the repo root; they exercise
`design-incubators/engine_tower/`, the tower as a uv project -- one
module per code-bearing theory, one test per witnessed claim, plus a
test that the module import graph respects the poset above. Most are
instance witnesses at tooling grade: they check the phenomenon on a
smallest instance, not the theorem, so they move no standing to
`bare` -- OBLIGATION names the proof-grade step.

The act algebra's derived results (`ABSORB`, `LOCAL`, `BLIND`) are
checked by quantification instead, over generated records bounded at
three claims, five acts, four verdict words, and acyclic
presupposition: more evidence, still not proof. They stand `bare` on
their derivation from the law of acts, and that bound is the debt a
proof would discharge.

## Scans

```bash
grep -rH '^standing:' docs/dev/strata.claims.kb/       # the ledger at a glance
grep -rH '^standing: open' docs/dev/strata.claims.kb/  # what wants an answer
grep -rA4 '^why:' docs/dev/strata.claims.kb/          # the warrant graph
```

## Provenance

A worked instance of `/formalize`, verified by `/deformalize` (the
incubator below); those skills postdate and were distilled from this
run. Distilled 2026-08-09 from a formalization conversation over this repo,
`ideation.epistemics`, `prototype.personal-reasoning-management`, and
`prototype.llm-stet`; correspondences with those systems live in
`fleet.kb/`, not restated elsewhere. Restructured the same day after
the user's act review: `purpose` root added, the assessor law filed,
theorem-shaped claims moved to `bare`, explicit rulings to `user`.
