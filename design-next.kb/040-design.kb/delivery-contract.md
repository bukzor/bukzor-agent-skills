---
why:
  - ../030-requirements.kb/coupling-is-layer-3-only.md
---

# Delivery Contract

Layer 3 is a runtime-agnostic **contract**, not the Claude Code
plugin described in `plugin-delivery.md` — that entry is one
**adapter** implementing it. The contract is three verbs:

1. **Inject context on trigger** — deliver a directive's body into
   the model's context when a matched condition fires.
2. **Gate or deny an action** — block or require confirmation before
   a matched action proceeds.
3. **Activate teaching content conditionally** — load a skill's body
   when its scope (paths, description, explicit invocation) matches.

Any sufficiently capable agent harness can implement these three verbs
around its own tool-execution loop, whether or not it calls the result
"hooks":

- **Claude Code adapter**: hooks implement verbs 1–2
  (`hook-wiring.md`); paths-gated skills and rules implement verb 3
  (`thin-skills.md`).
- **Raw Anthropic-API tool-use loop**: a middleware function wrapping
  the tool-call dispatch implements verbs 1–2 directly; verb 3 is
  whatever the caller's own prompt-assembly step does with the skill
  files (trivial — they're just markdown to concatenate on a matched
  condition).
- **Other harnesses** (OpenCode, LangGraph-style frameworks, etc.):
  their own callback/middleware layer implements 1–2 if present;
  absent that, verb 3's floor — unconditional or description-matched
  inclusion — still works everywhere, since it requires no special
  runtime support at all.
- **MCP**: orthogonal to this contract (it exposes *verbs the engine
  provides*, not trigger delivery), but the most standards-aligned way
  to make the engine itself reachable from any adapter — see
  `../070-future-work.kb/mcp-server-adapter.md`.

Classes and requirements name only the verbs (per
`../030-requirements.kb/coupling-is-layer-3-only.md`); adapters name
the mechanism. A second
adapter is added by implementing these three verbs for a new runtime,
never by rewriting layers 0–2.
