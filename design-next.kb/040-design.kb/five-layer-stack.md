---
why:
  - spec-cited-never-restated
  - procedures-are-tools
---

# Five-Layer Stack

The system is five layers; each concern lives in exactly one.

| Layer | Holds | Form |
|---|---|---|
| 0 Spec | what the formats *are* | one RFC + JSON Schemas |
| 1 Engine | mechanical behavior | one CLI (`kb`) |
| 2 Genres | per-domain conventions | schema + ~1 page each |
| 3 Delivery | activation + enforcement | a contract + swappable adapter |
| 4 Instances | actual knowledge/work | data directories |

Layer 3 is a runtime-agnostic *contract* (`delivery-contract.md`),
not the Claude Code plugin (hooks, skills, rules, commands) described
under `plugin-delivery.md` — that plugin is the contract's first
adapter, not the only one the layer permits.

V1's unit was the vertical silo: each skill bundled its own spec
prose, scripts, procedures, teaching, and self-documentation — which
is why definitions drifted apart and improvements had to be re-landed
per skill. The stack inverts this: definitions live once in the spec,
behavior once in the engine, activation once in the plugin manifest.

Where v1 pieces land: `llm-kb` splits into layers 0–2; `llm-collab`
dissolves (devlog becomes a record genre, decisions become settled
questions per `decisions-are-settled-questions.md`, scripts become
engine commands, skeleton becomes `kb init`); `llm-design-kb` and
`llm-discourse-graph` become the design and discourse genres,
kept separate but sharing the spec's linked-node primitive
(`genre-epistemic.md`); `llm-must-read-kb` becomes the trigger genre;
`llm-subtask` becomes the task genre plus hook wiring; `llm-vitals`,
`sessions.kb`, and the personal must-read bank are instances;
`claude-realignment` and `llm-chat-librarian` remain standalone (a
judgment skill and a deferred engine feature, respectively).
