---
label: STANCE
standing: agent
authority: >-
  docs/dev/adr/2026-08-28-000-A-skill-states-a-stance--not-a-procedure.md
why:
    - skill-md-addresses-invokers.md
    - price-text-by-load-frequency.md
---

# Stance over procedure

A skill body states the stance an agent must hold, not the procedure
it must run: a procedure encodes the setting its author stood in, and
fails silently in every other one — most damagingly where the
artifact it names is absent, which a stance would have read as the
finding.

Three parts carry a stance, and a body missing any of them has
written a checklist:

- the **standing** — what the agent is accountable for, and what it
  may not inherit that accountability from;
- what it must be **able to say** before acting, as a precondition on
  acting rather than a list to work through;
- the **precedence** among those, for when they conflict.

The declined alternative is the concrete instruction that worked in
the founding case. It reads as the distilled lesson precisely because
it did the work once; that is the tell, not the warrant. An
instruction earns its place only where the artifact it names is
guaranteed present, which inside one repository is common and across
settings almost never.

Longer than the instruction it replaces, and paid at invocation
frequency — so this trades against `price-text-by-load-frequency.md`
and wins only where the skill meets settings its author did not build.
