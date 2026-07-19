---
why:
  - ../030-requirements.kb/action-triggers-enforced-deterministically.md
  - ../030-requirements.kb/judgment-triggers-remain-scannable.md
---

# Class: Trigger

Conditional directives, partitioned by whether the condition is
machine-detectable:

- **Action-shaped** ("before git commit", "before editing schemas"):
  enforced by *interpretation* — a per-runtime shim, installed once,
  reads the trigger file at fire time and delivers its body as
  injected context (or as the deny payload, for hard gates). Nothing
  is generated per-trigger, so enforcement cannot go stale; what a
  runtime reports instead is *coverage* — which triggers it binds
  mechanically versus leaves to the floor.
- **Judgment-shaped** ("when evaluating a contested position", "when
  wanting to comply but cannot"): stay a filename-indexed
  `must-read` bank, scanned during planning — v1's genuinely novel
  invention, retained at exactly the scope deterministic detection
  can't reach.

This dissolves v1's central tension: the same authoring format serves
both, but enforcement strength follows detectability instead of
hoping prose emphasis covers everything.

The subsystem's specifics — condition vocabulary and its admission
test, bank format, the interpreter contract, the wake-condition
grammar — live in `../../llm-triggers/design.kb/`, per
`delivery-boundary.md`.
