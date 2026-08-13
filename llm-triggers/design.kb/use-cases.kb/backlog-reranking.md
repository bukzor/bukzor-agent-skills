# Below-the-Fold Reranking

The working set's total order is hand-maintained, and tangent work
keeps changing what's synergistic: a task far down the stack may
turn cheap or urgent because of what just landed. How much recurring
effort re-evaluation deserves, and how often, is a per-operator
budget — not a system constant.

Today: reordering happens when the operator notices; v1's wsjf-rank
pass is hand-run.

Satisficed when: an instance can record a recurring "re-rank pass
due" condition at its own cadence, and the surfaced body can carry
the instance's effort bound ("spend at most X") — the system
schedules the attention; the recorded values say how much.
