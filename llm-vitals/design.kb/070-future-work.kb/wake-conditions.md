---
why:
  - reduce-dropped-tasks
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
