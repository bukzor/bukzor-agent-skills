---
label: REENTRY
standing: agent
why:
  - the-top-set-is-installed-by-the-host.md
  - ../delivery.kb/reinstalling-the-top-set-restores-every-stub.md
authority: "offered by the shell-loader peer session, ~/.claude/sessions.kb/penguin.kb/shell-config-intent-first-loader.kb/2026-09-19-001-sibling-review.md (2026-09-19): re-run the loader at every entry; idempotent legs"
---

# Installing Is Idempotent per Context Window

The top set's installer occasion is entry into a context window --
session start and every post-compaction resume alike -- and installing
is idempotent (a listing that is already in context is re-listed at the
cost of its lines and nothing else). So re-running the installer on
every entry needs no state and closes the compaction question for the
top set. The shell loader's practice is the same rule in a different
substrate.

Stale when: an install stops being idempotent -- a listing that mutates
state, or one whose repetition an agent reads as a new instruction.
