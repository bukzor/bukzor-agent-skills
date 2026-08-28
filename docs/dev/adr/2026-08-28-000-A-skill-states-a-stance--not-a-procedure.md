# A skill states a stance, not a procedure

**Date:** 2026-08-28
**Status:** Accepted

## Context

`Skill(judge-work)` in the meta-reasoning repo was rewritten twice in one
sitting. The first rewrite cut it from 940 words plus 4,936 words of
mandated reading down to 700 words mandating none — and the owner
rejected the result. The defect was its opening instruction: *"open the
thing that computes its rank and read that."*

That instruction presumes a rank-computing mechanism exists. One did, in
that repo. Where none exists, an agent follows the instruction, finds
nothing, and moves on — having missed that *nothing computing the rank*
is the finding, and usually the larger one.

The owner's framing: generality and efficiency are competing goals, and
"minimize" means as small as possible **but no smaller**. Content that is
inherently situational must not be optimized away. The most an author can
do with it is make it easy to find and to choose.

Two neighbouring ADRs already hold ground here and neither reaches the
body's own form: 2026-08-09-000 keeps instances out of skills and
author-facing rules out of `SKILL.md`; 2026-08-27-000 makes the
`description:` the authoritative trigger surface.

## Decision

**1. The body states a stance, not steps.** A skill establishes the
agent's accountability, the things it must be able to say before acting,
and the precedence among those when they conflict. A step presumes the
setting that makes it possible; a stance yields the step wherever the
setting supports one, and yields the *absence* as a finding where it does
not.

**2. Situational bindings stay, below a marked seam.** They are what makes
a check runnable — deleting them for portability produces a file that
generalizes because it no longer does anything. The seam is named in the
body, and says outright that a port rewrites that section rather than
dropping it. Everything above the seam is setting-independent.

**3. A detection instruction states what an empty result means.** A check
whose null case is unstated reads as noise to precisely the agent who
most needs it: the one arriving before the mechanism exists.

**4. A skill's cost is the transitive closure of what it mandates
reading**, not its own length. Mandated derivation is the usual inflator.
Route the story to an address, marked read-on-contest, so the cost is
paid only when a check is challenged.

The incident behind (4) generalizes on its own: `judge-work` refused to
state its own content because a rule it carried forbade caching state
that can go stale. That rule governed *current state*, and a check does
not rot. **A content rule does not automatically govern the rules.**

## Alternatives Considered

### Keep prescriptive steps, add a conditional per setting
- **Pros:** concrete; an agent knows exactly what to run
- **Cons:** the branch set is unbounded, the author must anticipate
  settings they have never seen, and every conditional is a new place to
  be wrong. This is what the rejected draft was already becoming.

### Delete situational content for portability
- **Pros:** maximally general; one file runs anywhere
- **Cons:** a check nobody can run is not a check. Directly contrary to
  the owner's "no smaller" ruling.

### Split general body and local bindings into two files
- **Pros:** cleanest separation; a port copies one file and writes the other
- **Cons:** two loads for a section that is a dozen lines. Rejected on
  cost. Revisit when a skill's bindings outgrow a section — that is the
  tripwire.

## Testing

The acceptance test for a skill is to **replay the episode that created
it, with the skill in hand**: does the `description:` fire on that
episode's opening message, and do the checks produce the finding without
the human who originally supplied it?

`judge-work` failed both. Its description named ranking and "what next"
but not "the owner doubts the worklist is worth doing" — the exact
message that created it. Its rooting check would have matched every item
at that date, since the field it looks for did not yet exist anywhere,
which a cold agent reads as a mistyped query rather than as a result.
This is the cheap detector for the miscalibrated descriptions counted in
2026-08-27-000.

**The test's limit, which is structural:** replaying a session against
rules extracted from that same session is one route, not two. It can show
the skill compresses that episode. It cannot show the skill generalizes,
because every rule in it was fitted to those events. Generalization is
tested only by a different episode, in a different setting.
