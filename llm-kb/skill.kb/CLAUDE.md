# skill.kb -- maintenance guide

This directory holds the skill's runtime directives for consumers. The
SKILL.md `IMPERATIVE` block at the project root tells consumers to
`ls -RF skill.kb/must-read.kb/` on skill load.

Maintainer's job: keep the must-read triggers, quality passes, and procedures
organized so an agent reaching this directory at runtime finds the right
file fast.

## What belongs here

- `must-read.kb/` -- trigger-bound directives, partitioned by when they fire.
- `procedures.kb/` -- multi-step methods invoked when the situation
  calls for them.
- `quality-passes.kb/` -- proactive quality checks. One question, one
  recovery, per file.
- `reference.kb/` -- docs a consumer loads on demand: patterns, guides,
  worked examples.

## What does NOT belong here

- The skill's tutorial content -> `SKILL.md`.
- Methodology applied to maintaining the skill itself -> `docs/dev/`.

## Subdirectory conventions

### must-read.kb/

The skill-scope trigger bank. Format, juncture semantics, and naming are
`Skill(llm-must-read-kb)`; don't restate them here. Local rule only: each
file states its trigger and points at one or more procedures or quality passes
for the method.

### procedures.kb/ vs quality-passes.kb/

The split:

- A **quality pass** is something to run proactively, with the explicit goal
  of catching problems before they harden. One question, one recovery.
- A **procedure** is everything else -- a multi-step method invoked
  when the situation calls for it.

When adding a new file, ask: would an agent run this proactively to
catch problems, or only when the work itself calls for it?
Proactive -> quality pass; on-demand -> procedure.
