---
name: llm-triggers
description: "Trigger subsystem for the kb suite (design phase): condition vocabulary, trigger banks, per-runtime interpreters. Successor to llm-must-read-kb. Agent MUST load when authoring or repairing a trigger -- a (condition, directive) pair -- in any bank, or when deciding whether a directive needs a condition of its own."
---

# llm-triggers

Design-phase stub. The subsystem's content is `design.kb/`; nothing
here is runtime machinery yet. Until the v2 build, working trigger
banks remain governed by `Skill(llm-must-read-kb)`.

## Tools

`llm-triggers/bin/llm-triggers-lint [PATH]` -- run by path. Checks frontmatter
triggers under PATH (default `.`), skipping what `.gitignore` excludes. Run it
after editing any trigger; exit 0 clean, 2 on error.

Errors: a bare directive in an unconditional carrier; any `requires:` or
`depends:` -- `triggers:` is the only field. Warnings: a `triggers:` entry with
no `read:`; a `read:` that does not resolve.
