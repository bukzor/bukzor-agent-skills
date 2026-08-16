---
label: OPEN_ENOUGH
standing: user
why:
  - the-sigil-signs-the-judge.md
  - a-claim-avoids-negation.md
---

# An Open Question Needs No New Mark

Undone work enters the ledger as an ordinary claim signed `?`, its text
naming what an answer would settle. `?` already says no one has judged
it; a second mark for "and this one is also unbuilt, not just
undecided" would carry no information `?` doesn't already carry, and
scheduling the work is `Skill(llm-subtask)`'s job, not the ledger's.

This was checked directly against `llm-discourse-graph`'s `TODO!`, which
does need its own mark there — but that system tracks belief separately
from disputes, so its questions and its todos are different node types
to begin with. Here they are the same thing at different states, and one
mark already covers both.
