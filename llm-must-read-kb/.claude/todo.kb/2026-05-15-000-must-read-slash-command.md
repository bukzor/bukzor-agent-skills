---
managed-by: Skill(llm-subtask)
cost-benefit-sweh:
  timebox:
    "@value": 1.5
    rationale: |
      Parse free-text + infer scope + write trigger file via shared
      procedure (from .claude/todo.md). Beyond 1.5h, the parsing is
      getting clever; defer to manual creation.
  benefit-2w:
    "@value": 1.0
    rationale: |
      Ergonomic for trigger creation; estimate ~5 uses/week × ~5 min
      saved per use vs manual path = ~1h over 2 weeks. Blocked on
      create-new-trigger.md procedure landing first.
---

# /must-read slash command

`Skill(llm-must-read-kb)` codifies the trigger-bank pattern. The skill
governs the *what* (file shape, juncture, placement); a slash command
governs the *invocation* — parse free-text into a trigger file.

**Blocker:** `references/create-new-trigger.md` must exist first (see
`.claude/todo.md`). Both manual and command paths share that procedure
so they produce identical artifacts.

## Behavior

`/must-read <free text>` → write a trigger file via the canonical
procedure.

- Input: a sentence like "do X when Y, to prevent Z" from arguments,
  or from prior turn(s) when "above" appears.
- Output: a single new trigger file at the appropriate scope and
  juncture, populated from the SKILL.md template.

## Scope selection

Default: personal (`~/.claude/must-read.kb/`). Override flags map to
project (`$REPO/.claude/must-read.kb/`) or skill
(`$SKILL/SKILL.kb/must-read.kb/`) homes. Inside a skill dir, prompt
rather than infer — skill-level rules are sticky and should be
deliberate.

## Juncture selection

Map trigger phrasing to juncture:

| Phrasing | Juncture |
|---|---|
| "prevent X" / "before X" | `before/` |
| "when X"                 | `when/`   |
| "after X"                | `after/`  |
| Ambiguous                | ask       |

## Open questions

- Should the command also handle promotion when a trigger grows past
  ~50 lines (per SKILL.md "Composition with procedures.kb/")?
  Probably no for MVP — promotion is a maintenance act, not part of
  invocation.
- Default scope behavior when invoked from a project cwd: still
  personal, or infer project? Lean personal — that's where most
  cross-cutting rules belong.

## Success criteria

- `/must-read "agent should X when Y"` writes a single valid trigger
  file at the right scope and juncture.
- The new file fires its trigger on the next session.
- Manual creation (without the command) produces an identical-shape
  artifact, because both paths read `references/create-new-trigger.md`.
