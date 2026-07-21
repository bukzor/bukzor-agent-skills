# Future-Work Triggers Fire

Every future-work entry defers an idea behind a `trigger:`
condition. The layer's standing contract — "read on periodic review,
or whenever a trigger condition may have fired" — is circular:
knowing a trigger fired requires the very read it is supposed to
prompt.

Today: nothing evaluates these conditions; a fired deferral waits
for an operator to reread the layer.

Satisficed when: decidable trigger-descs (dates, `file:` descs) are
evaluated mechanically at some named juncture, and prose descs are
enumerated there for a cheap judgment pass — a fired deferral
surfaces without anyone deciding to go look.
