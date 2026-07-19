---
why:
  - ../030-requirements.kb/coupling-is-adapter-only.md
---

# Delivery Boundary

Delivery and trigger enforcement — however a directive's body reaches
the model's context, however an action gets gated — is the trigger
subsystem's surface, owned by `llm-triggers` (its `design.kb/` holds
the specifics). The subsystem is part of this suite: it depends on
`Skill(llm-kb)` and cites the spec one-way; no freestanding trigger
standard exists, because no triggers-without-kb consumer does. Its
detail nonetheless sits below this tower's grain — this tower states
the boundary, llm-triggers designs what's inside it.

The boundary: condition vocabulary and bank format are
subsystem-side and runtime-neutral; interpreter shims — the only
code that names a runtime's interception points — are adapter-side.
A class package may carry delivery-facing content without the spec or
the engine ever naming a runtime; the engine stays adapter-blind by
the same discovery contract that keeps it class-blind
(`kb-engine.md`).
