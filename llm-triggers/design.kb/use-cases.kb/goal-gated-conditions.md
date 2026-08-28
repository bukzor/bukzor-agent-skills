---
status: proposal
---

# Goal-Gated Conditions

A condition is goal-gated when it names the behavior its payload exists
to prompt. The trigger then fires only for agents already doing the
thing — exactly the population that no longer needs the delivery — and
stays silent at the juncture where the behavior is owed but not yet
begun.

Deployed instance, caught by the owner within hours (dotfiles d4a11f4,
reverted a19d712): the redesign bank entry chains to a worked
side-by-side, and the chain was narrowed to `when: writing the
side-by-side`. The read's purpose is to prompt side-by-side writing;
gating on that behavior inverted cause and effect. The ruling: "I want
the trigger to *prompt* writing a side-by-side at appropriate
junctures."

The repair is to state the condition over the situation that makes the
behavior owed — usually the carrier's own condition, so the entry goes
bare and inherits it. A narrower juncture inside a conditional carrier
is legitimate only when the target serves a genuine sub-situation of
the carrier's, never when it serves the whole condition.

Satisficed when: authoring guidance
(`../040-design.kb/trigger-desc.md`) rejects a condition that names its
payload's intended effect, the way the evaluability rule already
rejects the payload-gated shape (`payload-gated-conditions.md`).
