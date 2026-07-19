---
managed-by: Skill(llm-subtask)
---

# Extend claude-open-tasks-list to the decision grammars

**Priority:** Medium
**Complexity:** Medium
**Context:** Child of the green-light gate in `.claude/todo.md`.
Marker semantics: `design-next.kb/CLAUDE.md` § Open-Item Markers.
Operator pre-cleared throwaway risk 2026-07-19: this is deliberately
an early, disposable slice of the v2 engine's doctor/query surface
(`design-next.kb/040-design.kb/kb-engine.md`).

## Problem Statement

The v2 delta's open items span four grammars, distinguished by what
unblocks them. `~/bin/claude-open-tasks-list` sweeps only the labor
grammar (`- [<char>]` checkboxes, brief/Task-file existence). The
decision grammars — `status: proposal` (awaits operator),
`> [!QUESTION]` (awaits evidence/decision), 070 `trigger:` (awaits a
stated condition) — enumerate only via ad-hoc grep; the gate's
"Ratify" child in `.claude/todo.md` embeds that grep inline. The
green-light precondition ("no proposals or open questions left on
the critical path") is uncheckable by mechanism.

## Current Situation

- Tool: `~/bin/claude-open-tasks-list`, Python, roots `~/repo` +
  `~/.claude`, worktree dedup by effective mtime, closed status
  vocabulary (`SKIP_STATUSES`), "existence is signal" for
  `todo.kb/`/`todo.d/`/`CLAUDE.*Task*.md`.
- Downstream consumers key off current output: `task-list.md`,
  `wsjf-rank`. Decision items are not labor — they must not pollute
  those consumers' default view.
- Instances today: 7 `status: proposal` entries and 4 `[!QUESTION]`
  blocks (all in `design-next.kb/`, but match by pattern, not path —
  other kbs may adopt the markers), `trigger:` in
  `070-future-work.kb/*` frontmatter.

## Proposed Solution

Add a decision-grammar sweep behind a flag or separate output
section, default output unchanged. Per-grammar display grain:

- `status: proposal` → file path + H1 title
- `[!QUESTION]` → path:line + the marker's one-line title
- `trigger:` → path + the condition text (a wake condition to
  re-evaluate, not work to schedule)

Reuse the existing dedup machinery. Prefer a declarative
pattern-table over per-grammar code paths — this doubles as cheap
evidence for kb-engine.md's open `[!QUESTION]` on whether
declarative checks are expressive enough for `kb doctor`.

## Implementation Steps

- [ ] Read the full tool source; pick flag vs section (smallest
      diff that keeps default output byte-identical)
- [ ] Implement the three patterns + display grains
- [ ] Verify: counts match the inline grep from todo.md's Ratify
      child; default output unchanged for existing consumers
- [ ] Replace the inline grep in `.claude/todo.md`'s Ratify child
      with the new invocation
- [ ] Note the declarative-vs-code outcome on kb-engine.md's
      `[!QUESTION]` if it produced evidence either way

## Open Questions

- Should `trigger:` items appear at all by default, or only under a
  wider flag? They wake on conditions, not attention.

## Success Criteria

- [ ] One command enumerates every green-light blocker (labor +
      decision) across both planes
- [ ] `task-list.md` / `wsjf-rank` pipelines unaffected
- [ ] The inline grep in todo.md is gone (tool cited instead)

## Notes

Read-back moments this serves: design-session start ("what awaits
ratification?") and the green-light gate check
(`070-future-work.kb/v1-migration-bridge.md`'s trigger).
