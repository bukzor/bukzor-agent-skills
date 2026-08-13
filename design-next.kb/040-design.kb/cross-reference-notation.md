---
why:
  - ../030-requirements.kb/degrade-gracefully.md
status: proposal
---

# Cross-Reference Notation

Three notations, resolved by three different resolvers — and two
independent questions that must not be evaluated as one:

- **Within a tree**: plain file-relative paths (`../claims.kb/x.md`),
  per the v1 discourse-graph ADR. Resolved by any file reader, no
  tooling required.
- **Across class packages, path-bearing**
  (`skill://llm-kb/foo.jsonschema.yaml` in a jsonschema `$ref`/`$id`):
  resolved inside the kb engine — its validator interprets
  `skill://<class-package>/<path>` relative to wherever that class
  package's root lives on the current runtime, the same way it
  already resolves file-relative paths. Resolution is engine code,
  not adapter support, so this is not an adapter coupling: it needs
  no platform support, only the engine, which is portable by
  construction. Kept as the single source of truth for schema
  reuse — the alternative (vendoring schema copies into every
  project) is exactly the duplication
  `../020-goals.kb/single-source-improvement.md` exists to prevent.
- **Across class packages, load-directive** (`skill://llm-subtask`
  meaning "load this class package's teaching", replacing bare
  `Skill(<name>)`): genuinely runtime-coupled — "load a skill" is a
  Claude-Code-shaped concept other runtimes may not share — and stays
  an adapter concern, expressed in prose (the class package's name)
  with the load mechanism left to whatever adapter is active.

**Evaluate these two uses independently.** Whether `skill://` resolves
(always — it's engine code) and whether a *load* directive is portable
(no — it's adapter-shaped) are different questions with different
answers. Collapsing them into one "keep or retire skill://" question
is the failure mode to guard against whenever this notation comes up
for reconsideration.
