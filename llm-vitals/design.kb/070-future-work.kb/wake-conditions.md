---
why:
  - reduce-dropped-tasks
status: proposal
blocked-on: discussion
trigger: After the MVP picker is sticky (~2 weeks of consistent use).
---

# Wake Conditions on Fallow Items

Items moved out of active consideration carry a `wake:` field stating
what would bring them back: an event ("when rs- prefix lands"),
calendar ("Q3 review"), threshold ("when income > X"), or reflection
("re-read on quarterly sweep").

Quarterly sweep walks the fallow list and asks "did the trigger
fire?" Promotes mechanically.

Inverts the blocker question: if many fallow items wake on event X,
then X has high *blocker-leverage* — a derived prioritization signal
for active work.

Deferred because: works best alongside an active picker that's
already in habitual use. Adding it before the picker is sticky would
create a parking lot with no review discipline.

## Open questions

This entry is `proposal`-status because it presupposes a design that
doesn't exist yet — the fallow-state model for *items* (Active /
Fallow / Closed with resolution metadata). That design is flagged in
the session entry as adjacent to vitals, not part of it; it has no
home yet (likely an extension of `llm-subtask` or a new skill).

Until the fallow-state design lands, this entry sketches a feature
without a substrate. Specific open questions:

- Do fallow items appear in the vitals picker when their wake
  conditions fire? Or only in their own list (separate surface)?
- Does a fallow item with a fired wake condition contribute to vital
  debt, or is it categorically separate from vital state?
- Wake-condition taxonomy (event / calendar / threshold / reflection)
  was brainstormed but not deliberated — are these the right four?
- Quarterly cadence for the fallow sweep was named but not
  defended against weekly, biannual, etc.
