---
status: planning
scope: |
  Every textual `Skill(<name>)` reference in the user's tree, rewritten to
  the no-path agent-skill URI `agent-skill://<name>`. Two trees:

  - bukzor-agent-skills repo: ~79 files (~115 occurrences as of
    2026-05-27). Both frontmatter directives (`requires:`, `depends:`,
    `managed-by:`) and prose mentions.
  - ~/.claude convention files: ~25 files -- slash commands
    (session-start, session-end), todo.kb/, ideas.kb/, sessions.kb/,
    must-read.kb/, user-preferences.kb/, CLAUDE.md, CLAUDE.*Task*.md.

  Includes the `setup:` blocks in each SKILL.md, which instruct downstream
  projects to declare `depends: - Skill(<name>)`. These must change in
  lockstep with the convention that interprets the directive, so the
  load-directive keeps triggering skill loads (see "Load-directive
  consequence" below).

  Excludes literal Skill-tool call examples written as `Skill("<name>")`
  (tool-invocation syntax quoting a string argument, not the bare
  reference notation) -- flag those case-by-case.
why: |
  The `agent-skill://` URI scheme, its rationale, and its scope evolution
  are recorded in the ADR
  `agent-skill://llm-kb/docs/adr/2026-05-18-000-agent-skill-uri-scheme.md`.
  The scheme replaces the bespoke `Skill(<name>)` notation with a
  resolvable URI anchored to Anthropic's Agent Skills standard.

  This migration is the transformation that implements the 2026-05-27
  broadened scope: rewrite every existing `Skill(<name>)` occurrence to
  the no-path form `agent-skill://<name>`. The path-bearing `$ref` form
  (skill-owned files in jsonschema) is separate work, tracked in
  related-todo.
related-todo: ~/.claude/skills/llm-kb/.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md
related-session: ~/.claude/sessions.kb/apply-migrations-kb-backlog.md
---

# Replace `Skill(<name>)` notation with `agent-skill://<name>` URIs

## The notation

The scheme -- grammar, rationale, resolution contract, scope evolution --
is defined in the ADR
`agent-skill://llm-kb/docs/adr/2026-05-18-000-agent-skill-uri-scheme.md`.

This migration handles only the **no-path** form, which denotes the skill
itself and is the one-to-one replacement for `Skill(<name>)`:

    Skill(llm-kb)        ->  agent-skill://llm-kb
    Skill(llm-subtask)   ->  agent-skill://llm-subtask

## What gets replaced

The bare reference notation wherever it appears:

- Frontmatter directives: `requires:`, `depends:`, `managed-by:`.
- Prose mentions in CLAUDE.md, SKILL.md, kb entries, slash commands.
- The `setup:` blocks in each SKILL.md that tell downstream projects how
  to declare the dependency.

## What should NOT be replaced

- Literal Skill-tool call examples written as `Skill("<name>")` (quoted
  string argument) -- these illustrate a tool invocation, not the
  reference notation. Flag case-by-case rather than blanket-rewriting.
- Anything inside captured/immutable history (session logs under
  `*/.claude/projects/`, pre-rendered output).

## Load-directive consequence (load-bearing)

Because the no-path form replaces a *load-directive* (see the ADR's
Consequences), the sweep is not purely textual. Two things must change
together with it, or skill-loading silently stops:

1. The interpretation convention -- whatever teaches agents that a
   dependency directive means "load it" (the must-read `before/lazy-loading/`
   entries, this skill's pattern docs, the user's CLAUDE.md shorthand) must
   state that the no-path `agent-skill://<name>` form is the load directive,
   equivalent to the old `Skill(<name>)`.
2. Each SKILL.md `setup:` block -- it currently emits
   `depends: - Skill(<name>)` as the copy-paste downstream projects use.
   It must emit `depends: - agent-skill://<name>` so new projects adopt the
   URI form rather than re-seeding the old notation.

If the bulk sweep runs before these convention updates land, swept
frontmatter could fail to trigger loads and new projects would keep
copying the old form. Apply the convention/setup updates first (or in the
same pass).

## Algorithm (validate-first)

A `validate.sh` greps for `Skill\([a-z0-9_-]+\)` across the repo and the
~/.claude convention roots, excluding `*/node_modules/`, `*/.git/`,
`*/.claude/projects/`, and `*/trash/`; emits `<path>:<line>:<content>`.

The transform is mechanically simple --
`Skill\(([a-z0-9_-]+)\)` -> `agent-skill://\1` -- and a guarded
`migrate.sh` is feasible, but the `Skill("<name>")` exclusion needs
per-context judgment, so a semi-automated workflow (validate, review,
rewrite where every hit is the bare form) is the safe default. When those
scripts are written, they must follow the user's shell guidelines (no
`2>/dev/null`, no `grep` for control flow, no per-process redirects) --
see the cleanup task in the apply-migrations session.

## Idempotency

`agent-skill://<name>` does not match `Skill\(...\)`, so re-running the
transform on already-converted text is a no-op.

## A recurring validator is appropriate

`Skill(<name>)` is muscle memory -- agents (and training priors) will keep
emitting it after the one-shot sweep. A `validate.sh` kept as a recurring
drift-detector (like the bare-`-`-bullet migration) would surface
regressions. This entry classifies as one-shot for the sweep; promoting
the validator to `recurring` is a reasonable follow-on once the bulk
replacement is done.

## Relationship to the `$ref` work

The path-bearing form (`agent-skill://llm-kb/foo.jsonschema.yaml` in
jsonschema `$ref`/`$id`, plus the validator's in-memory `$id` index and
filesystem fallback) is designed and tracked in related-todo
(`schema-reuse-with-ref.md`). That work is independent of this notation
sweep; they share only the URI grammar.

## Status: planning

Decision recorded, scope mapped, no scripts written and no files swept.
Advances to `started` on the first applied subset.
