---
why:
  - ../030-requirements.kb/spec-cited-never-restated.md
  - ../030-requirements.kb/procedures-are-tools.md
  - ../030-requirements.kb/classes-detach-cleanly.md
status: proposal
---

# Core and Classes

The system is a thin core plus detachable class packages: four kinds
of thing, each concern living in exactly one.

| Kind | Count | Holds | Form |
|---|---|---|---|
| spec | 1 | what the formats *are* | one RFC + JSON Schemas (`kb-spec.md`) |
| engine | 1 | mechanical behavior, class-blind | one CLI, `kb` (`kb-engine.md`) |
| class | 1 per domain | conventions page, schema, templates, triggers, checks | a package (`class-package.md`) |
| data | many | actual knowledge/work | instance directories |

Spec plus engine is the core. The class is the deletion/adoption
unit: a domain's package is dropped with `git rm -r` and adopted by
copying it alone, per
`../030-requirements.kb/classes-detach-cleanly.md`.

Dependency rules:

- **class → spec**: required — a class is an application of the spec.
- **class → class**: citation and composition only, never
  subclassing (`class-package.md`).
- **class → engine**: verb citation only ("run `kb doctor`"), with a
  stated degradation when the engine is absent.
- **engine → class**: disallowed as a source dependency — the engine
  discovers class packages only as runtime data (directory
  convention / manifest), per `kb-engine.md`'s discovery contract; it
  never imports or hardcodes a class name.
- **spec → anything**: disallowed — the spec cites nothing
  downstream.

Delivery and trigger machinery sit outside all four kinds, on the
adapter side of `delivery-boundary.md`.

V1's unit was the vertical silo: each skill bundled its own spec
prose, scripts, procedures, teaching, and self-documentation — which
is why definitions drifted apart and improvements had to be re-landed
per skill. Core-and-classes inverts this: definitions live once in
the spec, behavior once in the engine, a domain's conventions once in
its package.

Where v1 pieces land: `llm-kb` splits into the spec and the engine;
`llm-collab` dissolves (devlog does not survive as a record class
sub-type — the residue test found its content already better-homed
elsewhere, see `class-record.md` — decisions become settled questions
per `decisions-are-settled-questions.md`, scripts become engine
commands, skeleton becomes `kb init`); `llm-design-kb` and
`llm-discourse-graph` become the design and discourse classes, kept
separate but sharing
the spec's linked-node primitive (`class-epistemic.md`);
`llm-must-read-kb` becomes the trigger class; `llm-subtask` becomes
the task class, its enforcement wiring moving to the adapter side of
`delivery-boundary.md`; `llm-vitals`, `sessions.kb`, and the personal
must-read bank are data; `claude-realignment` and
`llm-chat-librarian` remain standalone (a judgment skill and a
deferred engine feature, respectively).
