---
why:
  - ../030-requirements.kb/authorship-boundary.md
  - ../030-requirements.kb/filesystem-as-database.md
---

# Memory Policy

**Runtime-neutral property.** Any runtime's own auto-generated,
auto-loaded memory is admitted only as observations: orientation
shortcuts, learned quirks, "where things are" — content that is
cheap to regenerate and safe to be wrong. Deliberate knowledge —
decisions, claims, designs, tasks — lives only in a kb: schema-
validated, versioned, operator-reviewable content. The failure mode
this forbids: a runtime's auto-memory becoming a shadow kb —
unvalidated, unversioned, machine-authored knowledge that agents
trust because it auto-loads without a session asking for it.

**Claude Code mechanism.** Claude Code's implementation is
`MEMORY.md` per project: Claude-authored, auto-loaded, size-capped.
It also fails `filesystem-as-database` in a way plain kbs don't: it
lives in Claude Code's own state directory
(`~/.claude/projects/<project-hash>/memory/`), not the repo — not
git-tracked, not diffable pre-commit, not transferable to another
machine or collaborator the way a `.kb/` file is — a second,
independent reason to cap its authority even for content that passes
the observations bar. A `kb doctor` check flags `MEMORY.md` content
that has grown kb-shaped (dated entries, decision language, task
lists) for promotion into the real system or deletion. A different
runtime's adapter enforces the same observations/knowledge boundary
against whatever auto-memory mechanism it offers — or has none to
police, if it offers none.
