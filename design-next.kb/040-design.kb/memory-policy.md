---
why:
  - ../030-requirements.kb/authorship-boundary.md
  - ../030-requirements.kb/filesystem-as-database.md
---

# Memory Policy

Claude Code's native auto-memory (Claude-authored `MEMORY.md` per
project, auto-loaded, size-capped) is admitted with a boundary:

- **Auto-memory holds observations**: orientation shortcuts, learned
  project quirks, "where things are" — content that is cheap to
  regenerate and safe to be wrong.
- **kbs hold knowledge**: decisions, claims, designs, tasks —
  deliberate, schema-validated, operator-reviewable content.

The failure mode this forbids: MEMORY.md becoming a shadow kb —
unvalidated, unversioned, Claude-authored knowledge that agents trust
because it auto-loads. A doctor check flags auto-memory content that
has grown kb-shaped (dated entries, decision language, task lists)
for promotion into the real system or deletion.

MEMORY.md also fails `filesystem-as-database` in a way plain kbs
don't: it lives in Claude Code's own state directory
(`~/.claude/projects/<project-hash>/memory/`), not the repo — not
git-tracked, not diffable pre-commit, not transferable to another
machine or collaborator the way a `.kb/` file is. This is a second,
independent reason to cap its authority even for content that passes
the observations bar.
