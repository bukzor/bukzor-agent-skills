---
why:
  - ../030-requirements.kb/action-triggers-enforced-deterministically.md
  - ../030-requirements.kb/validators-outlive-migrations.md
---

# Hook Wiring

This is the Claude Code adapter's implementation of
`delivery-contract.md`'s inject/gate verbs. Everything below is
CC-specific by design; a different runtime's adapter implements the
same two verbs by its own mechanism.

The standing hooks, each replacing a v1 exhortation:

- **SessionStart** → orientation, mechanically: open session notes,
  stale vitals, top task lines injected as context (replaces "your
  FIRST action MUST be `ls …`" imperatives and the session-start
  script an agent had to remember to run).
- **PreToolUse** on matched commands (`if: "Bash(git commit *)"` and
  kin) → inject the relevant trigger body; deny outright when the
  gate is hard (e.g. committing kb files that fail `kb validate`).
- **Stop / SessionEnd** → capture nudge: uncommitted `[x]` marks,
  unwritten session log, stale design docs surfaced once, at the
  moment they're actionable.
- **PostToolUse** on kb writes → `kb validate` the touched
  collection, surfacing drift at edit time rather than review time.

Compiled from trigger-genre sources (see `genre-trigger.md`); hook
payloads are generated, never hand-maintained in JSON.
