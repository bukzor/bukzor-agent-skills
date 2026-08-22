---
label: FORMAT_SWEEP
standing: user
authority: "user, 2026-08-22: 'We need to do a design sweep to 1. unify (or decide not to) our improvements in the llm-stet design work with llm-claims-kb format/practices 2. adjust llm-claims-kb (if any) 3. adjust users of llm-claims-kb to conform (if needed)'"
---

# Unify the Format With the stet Design Work

The notation has been developed in two places at once. This skill and
`Skill(llm-claims-kb)` carry the shipped form; the stet design work in
`~/claude/meta-reasoning/claims.kb/plans.kb/` carries a later one, built
while reasoning about the same problems and never folded back.

The sweep runs in three phases, in order:

1. Enumerate what the stet work does differently, and rule on each --
   adopt, decline, or find them already equivalent. Silence is not a
   verdict; an aspect lost without one is a regression.
2. Change `Skill(llm-claims-kb)` and this skill to match what was
   adopted.
3. Bring the ledgers that use them into conformance.

Known differences to rule on, not an exhaustive list: `acts:` against
`standing:` (see ACTS_ADOPTED), `presupposes:` as a field this notation
has no counterpart for, and the four-classes fold that reads currency
off position rather than storing it.

One repair belongs to phase 2 and is already known: `SKILL.md`'s
"Statuses and retraction" still frames the strike as retraction-only,
which the 2026-08-21 widening -- the strike marks out-of-force, and the
word says why -- left behind.
