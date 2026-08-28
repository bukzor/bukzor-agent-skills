# Payload-Gated Conditions

A condition is payload-gated when deciding it requires the very
material it guards. `depends:` — "read when relevant" — is the
deployed instance: it asks an agent to judge a skill's relevance
before reading the skill that would establish what the skill covers.
The decider's only pre-read evidence is whatever the payload
advertises about itself from outside.

Today: the field looks like a judgment condition but supplies no
judgment at decision time, so it resolves by proxy — the skill's own
one-line description, which is doing the real work unacknowledged —
or by habit. Neither resolution is recorded, and both are invisible
to the author who wrote the field expecting it to fire.

Satisficed when: the evaluability rule
(`../040-design.kb/trigger-desc.md`) rejects this shape at authoring
time, being neither cheap to evaluate nor honestly judgment-only.
The repairs are to restate the condition over what the decider can
observe — the action about to be taken — or to drop the field and
let the payload advertise its own trigger, which is the mechanism
already carrying the load.
