---
label: DESIGN
standing: agent
stale-when: a design filed here that is not `/formalize`'s -- a second skill's commitments in this ledger
last-updated: 2026-08-18
---

# The design, as a ledger

`design.claims.kb/` records what `/formalize` commits to, in the same
notation a `/formalize` run produces: one claim per file, carrying its
label and its standing. `SKILL.md` is the manual; this is the reasoning
behind the manual, and the place to argue with it.

Read `purpose.kb/` when the question is whether the skill still aims at
the right thing. Read `run.kb/` to change a step of the procedure.
`setting.kb/` is the one to throw away first: it holds the proper nouns.

## Theories

Claims are grouped by the vocabulary they need. Each collection is a
**theory**, defined by the claim file beside it -- `run.md` defines
`run.kb/` -- which stipulates the ontology, names the priors in its
`why:`, and states the staleness condition. A claim may use only the
words its theory and its priors admit (`Skill(llm-claims)` § Theories).
This file stipulates nothing: it has no siblings to exclude, so a word
listed here would bind no one.

```
purpose ──► identification ──► run ──► setting
```

| Theory | Holds | Stale when |
|---|---|---|
| `purpose` | what the skill is, what a basis pins down, the six uses it is bought for | a run whose payoff is a use outside the six |
| `identification` | what an identification must carry to count as one | an identification worth keeping that names no operations and states no laws |
| `run` | how a run proceeds, and what it spends | a run performed by a program rather than by an agent reading the material |
| `setting` | where the output lives, whose designs it serves, what `/deformalize` takes over | a second operator, or a home other than the in-chat ledger |

The chain runs one way and the direction is the point: a use is stated
before the bar that serves it, and a step of the procedure cites the use
it pays for. `run` is the theory `SKILL.md` is downstream of -- a change
there is a change to the manual.

Who reads the deformalized account, and in what words, is
`/deformalize`'s own theory (`../deformalize/design.claims.kb/reader.md`)
-- `/formalize` only hands the account off, per
`setting.kb/plain-english-belongs-to-deformalize.md`. It was misfiled
here through 2026-08-15 and moved once a real ledger existed for
`/deformalize` to hold it.

## Standing

```bash
grep -rl 'standing: open' design.claims.kb/   # nobody has stood behind it
grep -rl 'standing: agent' design.claims.kb/  # agent-signed, veto invited
```

No claim stands `open`. `STOP` (`run.kb/what-the-stopping-rule-is.md`)
was retracted 2026-08-16 -- it presupposed `/formalize` needed its own
stopping mechanism distinct from the interactive session running it, and
the owner's answer dissolved that presupposition rather than settling
it. The `agent` set is the four theory headers plus two claims of
`run.kb/` -- each a judgment made on the owner's behalf that the owner
may never have read.
