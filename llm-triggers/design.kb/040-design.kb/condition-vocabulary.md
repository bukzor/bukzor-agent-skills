---
why:
  - ../../../design-next.kb/030-requirements.kb/action-triggers-enforced-deterministically.md
  - ../../../design-next.kb/030-requirements.kb/coupling-is-adapter-only.md
---

# Condition Vocabulary

The shared, runtime-neutral names for machine-detectable trigger
conditions. Three kinds seed it:

- **command pattern** — the agent is about to run (or just ran) a
  shell command matching a pattern: `git commit *`; `*`.
- **path pattern** — the agent is about to touch (or just touched) a
  file matching a glob: `**/*.kb/**` on write,
  `**/*.jsonschema.yaml` on edit.
- **lifecycle point** — a named moment every agent loop has
  regardless of runtime: session start, session end.

Every action-shaped trigger in the v1 personal bank and the v1
standing-hook list is expressible in these three kinds.
Judgment-shaped conditions (mental-state predicates) are deliberately
outside the vocabulary: they are floor-only by nature (`floor.md`).

## Admission test

A condition kind is admitted only if an agent with no enforcement
mechanism at all could still notice the situation itself during
planning. "About to run `git commit`" passes — every consumer down to
the floor can apply it. "PreToolUse fired with matcher X" fails — it
names one runtime's plumbing, not a noticeable situation, so it can
only ever be adapter glue (`claude-code-adapter.md`), never shared
vocabulary. This is the structural guard against the vocabulary
decaying into one runtime's hook events wearing neutral names.

## Elaboration carrier

A trigger file states its condition mechanically via optional
frontmatter — sketched as an `on:` block, e.g.
`on: {command: "git commit *"}`. A bare file with no such block is
floor-only. Elaboration is per-trigger and monotonic: adding it never
changes the floor meaning, only enables mechanical matching
(`interpretation-not-compilation.md`).

> [!QUESTION] field names for the elaboration block
> `on:` / `command:` / `path:` / `lifecycle:` are placeholders;
> settles when the first interpreter is built against them.
