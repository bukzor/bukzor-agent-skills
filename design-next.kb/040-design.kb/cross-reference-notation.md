---
why:
  - degrade-gracefully
---

# Cross-Reference Notation

Three notations, resolved at two different layers — and two
independent questions that must not be evaluated as one:

- **Within a tree**: plain file-relative paths (`../claims.kb/x.md`),
  per the v1 discourse-graph ADR. Resolved by any file reader, no
  tooling required.
- **Across skills, path-bearing** (`skill://llm-kb/foo.jsonschema.yaml`
  in a jsonschema `$ref`/`$id`): resolved inside the kb engine
  (Layer 1) — its validator interprets `skill://<name>/<path>`
  relative to wherever skill roots live on the current runtime, the
  same way it already resolves file-relative paths. Resolution is
  engine code, not runtime support, so this is not a Layer-3
  coupling: it needs no platform support, only the engine, which is
  portable by construction. Kept as the single source of truth for
  schema reuse — the alternative (vendoring schema copies into every
  project) is exactly the duplication `single-source-improvement.md`
  exists to prevent.
- **Across skills, load-directive** (`skill://llm-subtask` meaning
  "load this skill", replacing bare `Skill(<name>)`): genuinely
  runtime-coupled — "load a skill" is a Claude-Code-shaped concept
  other runtimes may not share — and stays a Layer-3/adapter concern,
  expressed in prose (the skill name) with the load mechanism left to
  whatever adapter is active.

**Evaluate these two uses independently.** Whether `skill://` resolves
(always — it's engine code) and whether a *load* directive is portable
(no — it's adapter-shaped) are different questions with different
answers. Collapsing them into one "keep or retire skill://" question
is the failure mode to guard against whenever this notation comes up
for reconsideration.
