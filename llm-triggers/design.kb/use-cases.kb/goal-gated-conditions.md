---
status: proposal
---

# Goal-Gated Conditions

A delivery that exists to *start* a behavior has to reach the agent
that has not started it. A bank entry chaining to a worked
side-by-side is the case in hand: whoever is about to redesign
something needs the example, and whoever is already writing one has
stopped needing it. The two populations are disjoint, and the
condition has to select the first.

Today: the phrasing that comes most naturally to an author names the
behavior the payload exists to produce — `when: writing the
side-by-side` — which selects the second population exactly. The
entry is well-formed and it fires, so nothing looks wrong; it just
fires after its own purpose is moot, and stays silent at the juncture
it was written for. The author gets no signal, because a trigger that
fires resembles a trigger that works.

Satisficed when: authoring guidance
(`../040-design.kb/trigger-desc.md`) rejects a condition that names
its payload's intended effect, the way the evaluability rule already
rejects the payload-gated shape (`payload-gated-conditions.md`).
