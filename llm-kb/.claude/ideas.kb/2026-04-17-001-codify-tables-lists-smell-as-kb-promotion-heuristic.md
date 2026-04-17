---
anthropic-skill-ownership: llm-subtask
---

# Codify tables/lists smell as .kb promotion heuristic

During a session (2026-04-17), the user had to repeatedly correct the
agent for putting lists of homogeneous items in single .md files. The
rule: a list of same-type things in one file is a smell — promote to
a .kb/ directory with one file per item.

This heuristic is central to the pattern but absent from the skill doc.
The existing test-results project CLAUDE.md says "if you find yourself
writing a list, split into multiple files" — but the skill itself
doesn't codify this, and doesn't connect it to the .kb/ promotion.

Should be added to the "Collections" section and possibly called out
as a "Smell" pattern.
