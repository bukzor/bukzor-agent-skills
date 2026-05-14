# Self-audit: CLAUDE.md enumeration

A `CLAUDE.md` is a maintenance guide, not a content directory. This audit
catches the failure mode where a CLAUDE.md drifts into enumerating
current contents (file lists, tool lists, PR lists), which then goes
stale silently the moment someone adds content without updating the
guide.

## Goal

Every section of the CLAUDE.md describes a **rule** (what belongs, what
doesn't, when to add) and none describes the **current state** (what's
currently there).

## Procedure

Re-read the CLAUDE.md. For each section, ask:

> Would `ls -RF` produce the same value as this section?

If yes, the section is enumerating. If no, the section is rule-shaped
and keeps.

## Recovery

Strip enumerating sections. Replace with rule-shaped sections if the
information is durable.

### Non-examples (drift -- strip these)

- "Tools available: Aider, Goose, Cursor, ..."
- "Files here: api.md, auth.md, deploy.md"
- "Active PRs: #123, #456, #789"

### Examples (durable -- keep these)

- "What belongs here: tool-comparison entries, one per tool."
- "What does NOT belong here: per-PR or per-incident notes."
- "When adding a new entry: include `last-evaluated` frontmatter."

## Frontmatter check (root CLAUDE.md only)

If the CLAUDE.md being audited is the root of a kb-using project, verify
the frontmatter declares `requires: Skill(llm-kb)`. Without it, agents
won't load this skill on entry and the kb pattern's invariants go
unenforced.
