---
managed-by: Skill(llm-subtask)
status: not-started
related-effort: ~/.claude/skills/llm-kb/.claude/todo.kb/2026-08-21-000-ref-rollout-beyond-todo-ideas.kb/2026-08-21-002-skill-granularity-is-the-addressing-unit.md
cost-benefit-sweh:
  timebox:
    "@value": 0.5
    rationale: |
      Reading one CLAUDE.md and deciding where each paragraph belongs.
      If it runs past 30 minutes the answer is "leave it alone" -- the
      split is only worth doing if it is obvious once looked at.
    confidence: unsure
  benefit-2w:
    "@value": 0.2
    rationale: |
      Nothing is broken. The payoff is that a second sessions log (a
      second host, another machine) would inherit the convention instead
      of copying it. No such consumer exists yet.
    confidence: confident
  cost-of-delay-2w:
    "@value": 0.1
    rationale: |
      The text is stable and lives next to its one consumer. Delay costs
      nothing until a second consumer appears, at which point the split
      becomes obvious and cheap to do correctly.
    confidence: confident
---

# Where does the sessions convention live: `llm-sessions`, or a bukzor specialization?

The 2026-08-21 cluster-6 work moved `sessions.jsonschema.yaml` into a new
`llm-sessions` skill so it could be `skill://`-addressed. The *schema*
moved; the *convention* did not. `~/.claude/sessions.kb/CLAUDE.md` still
holds the naming rules, what earns an entry, and how host sub-collections
are organized. Some of that is specific to one log; some is reusable.

## The question

Three shapes, in increasing cost:

1. **Leave it.** The convention lives next to its only consumer. The skill
   ships the schema and points at the log as the worked example -- which
   is what it does today.
2. **Move the reusable part up** into `llm-sessions/SKILL.md`, leaving
   `sessions.kb/CLAUDE.md` as log-specific residue.
3. **Split the skill**: generic `llm-sessions` plus a `bukzor-sessions`
   specialization that extends it.

## The framing that makes this non-obvious

This repo is `bukzor-agent-skills` -- llm-agent skills, by bukzor, for
bukzor. Reusability outside that domain is a *design smell in the good
sense*: it usually indicates the abstraction found a real seam. But it is
secondary, non-essential, and sometimes actively counterproductive --
generalizing past the one real consumer buys indirection with no user.

So shape 3 is not automatically better than shape 1. The test is not "is
this generic?" but "does a second consumer exist, or is one clearly
coming?" Today: no. That argues for 1 or 2 and against 3.

A related precedent worth checking before deciding: the `llm-claims` /
`llm-claims-kb` and `llm-kb` / `llm-must-read-kb` splits are both
*artifact-type* splits, not generic/specific splits. If no existing skill
pair splits along a generic/specialization axis, shape 3 would be
inventing a new kind of seam -- which needs a better reason than symmetry.

## Out of scope

Not blocking anything. The schema is addressable and everything
validates; this is about where prose lives.
