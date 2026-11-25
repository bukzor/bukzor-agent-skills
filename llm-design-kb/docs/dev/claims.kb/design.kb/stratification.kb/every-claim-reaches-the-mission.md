---
label: REACH
standing: user
why:
  - priors-are-a-dag-not-a-ladder.md
  - a-rung-is-a-theory.md
authority:
  address: 59b55f01
  words:
    as long as requirements clearly serve goals (or some higher requirement, i
    suppose), that's fine.
  about: whether a requirement may rest on another requirement
---

# Every Claim Reaches the Mission

What the DAG keeps from the ladder is reach: every claim reaches the mission
through `why:`, directly or through other claims. So a requirement may rest on
another requirement, as long as the chain ends in a goal. A requirement whose
only prior is another requirement narrows that requirement's check; one that
says how the other is met answers architecture's question, and is misfiled.

The declined alternative is the ladder's adjacency rule, that each requirement
cite a goal. It forces a false arrow onto a sub-check -- one revisited when its
parent requirement collapses, not when the goal is reworded -- or pushes
check-level detail up into the goals.
