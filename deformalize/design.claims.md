---
label: DESIGN
standing: agent
ontology:
  - skill
  - design
  - claim
  - theory
  - glossary
  - agent
  - user
stale-when: a design filed here that is not `/deformalize`'s -- a second skill's commitments in this ledger
last-updated: 2026-08-15
---

# The design, as a ledger

`design.claims.kb/` records what `/deformalize` commits to. `SKILL.md`
is the manual; this is the reasoning behind the manual, and the place to
argue with it.

## Theories

```
purpose ──► reader
```

| Theory | Holds | Stale when |
|---|---|---|
| `purpose` | why `/deformalize` exists, and the job it does at the seam with `/formalize` | a run whose output is judged for taste rather than for what it breaks |
| `reader` | who reads the deformalized account, and how the vocabulary crosses from formal to plain | an account read only by agents already fluent in the formal vocabulary |

`purpose` is the prior: `reader`'s claims about the glossary need the
job (DEFORM_JOB) already on the table before they can argue for a shape.

Several claims here rest on claims of `../formalize/design.claims.kb/`
-- the seam runs one way, `/formalize` handing off to `/deformalize`, and
the `why:` arrows point the same direction the handoff does.

## Standing

```bash
grep -rl 'standing: open' design.claims.kb/   # nobody has stood behind it
grep -rl 'standing: agent' design.claims.kb/  # agent-signed, veto invited
```

Every claim here was ruled on directly or moved in with its ruling
intact (2026-08-15, migrated from `../formalize/design.claims.kb/`
where it was misfiled). Only the two theory headers stand `agent`.
