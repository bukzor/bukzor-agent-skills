--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-subtask)
    - Skill(llm-claims-kb)
    - Skill(llm-discourse-graph)
---

# llm-claims

`design.claims.kb/` here is **not** the layered `Skill(llm-design-kb)`
collection it is elsewhere in this repo — no `010-mission.kb/`, no `why:`
chain. It is a claim ledger in the file form, `Skill(llm-claims-kb)`:
one theory per collection, one claim per file, `label:` and `standing:`
in frontmatter. `design.claims.md` is the entry point.

`SKILL.md` and `skill.kb/` are the manual, and carry no claims.
