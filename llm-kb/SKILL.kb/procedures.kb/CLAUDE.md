# procedures.kb -- shared multi-step methods

Procedures invoked by `../must-read/` triggers or by hand when the
situation calls for them. Multi-step methods that change state.

## What belongs here

- Multi-step methods invoked on demand.
- Procedures referenced by 2+ must-read triggers (or 1 trigger plus
  other procedures invoking it as a recovery step).

## What does NOT belong here

- Proactive quality checks (one question + one recovery)
  -> `../self-audit.kb/`.
- Procedures specific to maintaining the llm-kb skill itself
  -> `../../docs/dev/procedures.kb/`. That's the skill-internal kb;
  this is the consumer-facing one.
- Single-use methods that fire from one trigger and aren't likely to
  spread -- inline them in the must-read file instead.

## Directionality

Procedure files name no callers. References go one way: callers (the
must-read files, or other procedures invoking a peer as a recovery
step) name the procedure; the procedure never names its callers.
Caller-lists go stale silently as new callers appear and would couple
the procedure to its current users.
