---
why:
  - ../030-requirements.kb/coupling-is-adapter-only.md
---

# Delivery Boundary

Delivery and trigger enforcement — however a directive's body reaches
the model's context, however an action gets gated, however teaching
content activates — is not a kb-core concern. It is a peer concern to
the spec/engine/class core, designed and packaged on its own
timeline: the trigger subsystem, `status: proposal`, pending the T4
session (see `.claude/todo.md`).

What kb core commits to until T4 lands: a class package — most
visibly the trigger class (`class-trigger.md`) — may carry
delivery-facing content (compiled hook payloads, rule files, whatever
a given runtime needs) without the spec or the engine ever naming
that runtime. The engine stays adapter-blind by the same discovery
contract that keeps it class-blind (`kb-engine.md`); which adapter is
active, and how a class's delivery-facing content compiles for it, is
entirely the trigger subsystem's design surface, not this tower's.

**Superseded content.** This entry replaces the prior
`delivery-contract.md` (a three-verb inject/gate/activate
formalization) and `plugin-delivery.md` / `hook-wiring.md` (the
Claude Code adapter's native-primitive division and standing hook
list). None of that content is lost — it's recoverable from git
history — but it is deliberately not carried forward here: formalizing
a verb contract or a hook-event mapping from kb core, before the
trigger-subsystem session exists to own that surface, would be
exactly the boundary-jumping this tower is trying to stop doing. It's
raw material for T4 to start from, not content this tower should keep
maintaining in parallel.
