# skill.kb -- maintenance guide

The skill's runtime kbs (`SKILL_KB`, in the fleet ledger's `authorship.kb/`),
for an agent with a claims.kb in front of it. Only what is ledger-specific:
anything a plain `.kb` also needs is `Skill(llm-kb)`'s, cited, never copied.

## What belongs here

- `quality-passes.kb/` -- one way a claims.kb rots per file: what the pass
  improves, how to walk or scan, what a finding means, the repair. A pass
  names no occasion. `quality-passes.md` is its index.
- `must-read.kb/` -- the occasions: each file names one in its path and
  points at the passes or procedure due then, restating neither. A lens
  `Skill(llm-claims)`'s own bank carries is pointed at, not copied. Format
  is `Skill(llm-must-read-kb)`; `SKILL.md`'s `IMPERATIVE` block installs it.
- `procedures.kb/` -- multi-step methods, today the tiered sweep
  `run-quality-passes.md`, which runs `Skill(llm-kb)`'s sweep first.

## What does NOT belong here

- Why a rule is so -> the fleet ledger, `docs/dev/claims.kb/`.
- Notation a reader must decode in place -> `SKILL.md`.
