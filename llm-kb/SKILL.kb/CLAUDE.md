# SKILL.kb -- maintenance guide

This directory holds the skill's runtime directives for consumers. The
SKILL.md `IMPERATIVE` block at the project root tells consumers to
`ls -RF SKILL.kb/must-read/` on skill load.

Maintainer's job: keep the must-read triggers, audits, and procedures
organized so an agent reaching this directory at runtime finds the right
file fast.

## What belongs here

- `must-read/` -- trigger-bound directives, partitioned by when they fire.
- `procedures.kb/` -- multi-step methods invoked when the situation
  calls for them.
- `self-audit.kb/` -- proactive quality checks. One question, one
  recovery, per file.

## What does NOT belong here

- The skill's tutorial content -> `SKILL.md`.
- Internal references loaded only for special cases -> `references/`.
- Methodology applied to maintaining the skill itself -> `docs/dev/`.

## Subdirectory conventions

### must-read/

Mirrors the personal `~/.claude/must-read.d/` convention.

- `before/<situation>.md` -- read **and** complete prescribed actions
  before the named action. Hard precondition.
- `after/<situation>.md` -- read at completion of the named action.
- `when/<situation>.md` -- read when the situational match fires
  mid-task.

Filenames are situation slugs naming what triggers the read. Each file
states the trigger and points at one or more procedures or audits for
the method.

### procedures.kb/ vs self-audit.kb/

The split:

- An **audit** is something to run proactively, with the explicit goal
  of catching problems before they harden. One question, one recovery.
- A **procedure** is everything else -- a multi-step method invoked
  when the situation calls for it.

When adding a new file, ask: would an agent run this proactively to
catch problems, or only when the work itself calls for it?
Proactive -> audit; on-demand -> procedure.
