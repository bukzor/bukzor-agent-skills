---
last-updated: "2026-08-10"
---

# The design, as a ledger

`design.claims.kb/` records what this skill commits to, in the notation the
skill teaches: one claim per file, carrying its label and its standing.
`SKILL.md` and `SKILL.kb/` are the manual; this is the reasoning behind
the manual, and the place to argue with it.

Read `notation.kb/` to understand or change a design decision. Read
`stance.kb/` and `purpose.kb/` when the question is whether the design
is still aimed at the right thing.

## Theories

Claims are grouped by the vocabulary they need, not the topic they
touch. Each collection is a **theory**: a fixed ontology, a declared
prior whose ontology it also admits, and a stated defeater. A claim may
use only the words its theory admits (`Skill(llm-claims)` § Theories).

```
stance ──► purpose ──► good-smells ──► notation
```

| Theory | Holds | Defeated by |
|---|---|---|
| `stance` | what terminates a regress; what a distinction earns | a stopping point that is a truth rather than an act |
| `purpose` | the invariant, the cost it must beat, the rung it occupies | a competitor that is a better notation rather than none |
| `good-smells` | criteria any claim notation can be judged against | a ledger written and read by tools |
| `notation` | the decisions this notation actually made | an inference relation cheap enough to check at entry |

The chain runs one way and the direction is the point: a criterion is
stated before the design it judges, and a decision cites its criterion
rather than restating it. `notation` is the theory most likely to be
wrong, and the only one `SKILL.kb/` is downstream of — a change there is
a change to the manual.

`good-smells.kb/` is the only one large enough to want a roll-up of its
own; that is `good-smells.md`. The rest fit in `ls`.

## Standing

```bash
grep -rl 'standing: open' design.claims.kb/   # nobody has stood behind it
grep -rl 'standing: agent' design.claims.kb/  # agent-signed, veto invited
```

Most of `good-smells.kb/` is `open`: extracted from a single design
conversation, and only partially exercised by the one second instance
so far (prototype.llm-stet, 2026-08-08). The `agent` set is the one
worth a periodic scan, since each entry is a judgment made on the
user's behalf that the user may never have read.
