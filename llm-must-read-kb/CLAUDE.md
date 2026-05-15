--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-must-read-kb)
    - Skill(llm-collab)
    - Skill(llm-subtask)
---

# llm-must-read-kb Skill

See `SKILL.md` for documentation. This file gives maintenance guidance
for agents working **on** the skill (not consumers of it).

## Self-Application

This skill prescribes a directory shape and access pattern. It should
apply that same pattern to itself wherever it has trigger-bound
directives — e.g. any future `SKILL.kb/must-read.kb/` here governing
edits to trigger files or scope additions.

If you find yourself writing "always do X before editing trigger
files" prose in SKILL.md, that's a signal to add a
`SKILL.kb/must-read.kb/before/editing-a-trigger-file.md` instead.

## What changes warrant which artifact

- **ADR** (`docs/dev/adr/`): any change to user-observable contracts —
  juncture semantics (`before/`/`after/`/`when/`), filename slug rules,
  the "Required Reading" stanza wording, the directory name itself,
  what `setup:` instructs consumers to do.
- **Devlog** (`docs/dev/devlog/`): non-trivial sessions, especially
  ones that surfaced edge cases or rejected alternatives. Subsequent
  agents need to find the reasoning.
- **`.claude/todo.md`**: in-progress work on this skill.
- **`.claude/todo.kb/`**: deferred ideas, future work, blocked items
  (per `Skill(llm-subtask)`).
- **Inline in `SKILL.md`**: stable conventions consumers must follow.

## Relationship to `Skill(llm-kb)`

This skill **extends** llm-kb by prescribing an access pattern. Any
change here that conflicts with llm-kb's base contracts is a smell —
prefer to surface the question in llm-kb first (or jointly), then
specialize here. Examples:

- Promotion signals → llm-kb owns these; we inherit.
- Frontmatter directives (`requires:`/`depends:`) → llm-kb owns; we
  inherit and apply at the trigger-bank scope.
- Filename slug conventions → llm-kb owns the *general* rule; we
  prescribe the *juncture-verb composition* on top.

## Editing trigger files vs editing SKILL.md

The skill describes the **format** of trigger files. Concrete trigger
files (in consumer scopes) are content, not skill material. Don't bake
real-world rules from `~/.claude/must-read.kb/` into SKILL.md examples
— pick neutral example slugs that show the format without dragging in
specific policy.

## Verification

Changes to the skill should be tested by:

1. Reading the resulting `SKILL.md` cold and asking: would a consumer
   know how to stand up a new `must-read.kb/` from this alone?
2. Walking each example through the prescribed access pattern and
   confirming the agent's mental loop terminates on a clear action.
3. If `bin/` scripts get added later: their tests run before commit
   (mirrors `llm-collab/TESTING.md` convention).
