---
last-updated: "2026-08-09"
---

# The strata, as a ledger

The formal model of this repo's skill ecosystem: the engine is not one
thing but a tower of strata, each a small mathematical structure
derived over the fixpoints of the one below. `strata.ledger.kb/` holds
the model as a claim ledger (`Skill(llm-claim-ledger-kb)`): one claim
per file, label and standing in frontmatter, one theory per collection.

Read `tower.kb/` for the punchline, `fleet.kb/` for where the v1
skills and prior prototypes sit in it. Argue with a claim by editing
its file; the git diff is the strikethrough.

## The picture

The whole tower, quotiented to one sentence and three laws.

**Authority belongs to acts; everything else is a projection; a
change is judged by what it forces to re-project.**

The invariant (`history`): an act is attributed and appended, never
edited. Everything derived from acts obeys three laws:

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

Claims are grouped by the vocabulary they need (`Skill(llm-claim-ledger)`,
`SKILL.kb/theories.md`). Two are auxiliary -- `fixpoint` holds shared
background mathematics so that `reference` and `standing` can argue in
one sentence each, and `view` holds the derived-value machinery that
`standing` and `protocol` both lean on.

The spine, with auxiliaries feeding in:

```
history ──► record ──► reference ──► standing ──► genre ──► tower ──► fleet
    │                      ▲             ▲  ▲                 ▲
    └──► view ─────────────┼─────────────┼──┘                 │
    │        └──► protocol ┼─────────────┼────────────────────┘
fixpoint ──────────────────┴─────────────┘
```

| Theory | Priors | Holds | Defeated by |
|---|---|---|---|
| `fixpoint` | -- | background order theory: lfp, warm-start, overshoot, approximation | a misstatement of settled mathematics |
| `history` | -- | the store as a word of updates; state as its fold | a substrate that forgets its past |
| `view` | history | derived values, the commuting triangle, staleness as debt | a reader that can afford to recompute every read |
| `record` | history | schemas, typing, migration as transport | a fleet that abandons frontmatter typing |
| `reference` | record, fixpoint | quivers, reachability, cones, weights | references a machine cannot enumerate |
| `standing` | reference, view, fixpoint | the status poset, the evidence operator, computed standing | a second node sort in the base |
| `genre` | standing | confinement, conservativity, the satisfaction condition | a genre that must re-legislate a prior to exist |
| `protocol` | history, view | trigger banks as monitors; enforcement grades | a runtime that enforces every rule natively |
| `tower` | genre, protocol | the strata as their own theory poset; self-application | a lower engine needing a higher vocabulary |
| `fleet` | tower | proper nouns: where v1 skills and prototypes sit | any named system changing |

`fleet` is the throwaway theory. Theorems stand `bare` (`fixpoint`,
plus `REACH`); `OBLIGATION` stands `open`; everything else is signed
`+` pending rulings.

## Scans

```bash
grep -rH '^standing:' docs/dev/strata.ledger.kb/*.kb/       # the ledger at a glance
grep -rH '^standing: open' docs/dev/strata.ledger.kb/*.kb/  # what wants an answer
grep -rA4 '^why:' docs/dev/strata.ledger.kb/*.kb/*.md       # the warrant graph
```

## Provenance

Distilled 2026-08-09 from a formalization conversation over this repo,
`ideation.epistemics`, `prototype.personal-reasoning-management`, and
`prototype.llm-stet`; correspondences with those systems live in
`fleet.kb/`, not restated elsewhere.
