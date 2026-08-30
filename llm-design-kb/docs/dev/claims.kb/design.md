---
label: DESIGN_KB
standing: agent
ontology:
  - rung
  - record
  - tower
  - stratification
stale-when: a design record in the wild that keeps rungs but abandons claim standing -- the reform's premise was that the two compose, and an instance proving otherwise voids it
---

# llm-design-kb's own design, as a ledger

What this skill commits to, kept in the form it recommends. The
reform of 2026-08-29 is its founding content: llm-design-kb stopped
defining a document format of its own and became a **stratification
discipline over `Skill(llm-claims)`** -- it contributes the rungs and
the rule that a statement sits on the rung whose question it answers,
and takes notation, standing, arrows, and persistence from its basis.

The finding the reform rests on, from the 2026-08-06 comparison of two
decompositions of one design conversation: **a design tower is a claim
ledger with standing erased.** `why:` was already the ledger's `<-`;
layers were already theories with priors; `070-future-work.kb/` was
already the `?` claims; "why not X" was already the struck claim. What
the tower could not record is who decided each entry -- so it read as
ratified whether a person had ruled it or an agent had guessed.

## Theories

Each is the claim file beside its collection, so `ls` is the index.

- `stratification` -- what the rungs are and how they relate
- `operation` -- the three beats, and what each is accountable for
- `migration` -- what happens to towers and formats already in the wild

## Scans

```bash
grep -rH '^standing:' docs/dev/claims.kb/design.kb/
llm-claims-kb-flatten docs/dev/claims.kb/design.kb
```
