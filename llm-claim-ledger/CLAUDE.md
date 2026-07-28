--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-subtask)
    - Skill(llm-discourse-graph)
---

# llm-claim-ledger

`design.kb/` here is **not** the layered `Skill(llm-design-kb)` collection
it is elsewhere in this repo — no `010-mission.kb/`, no `why:` chain. It
is a claim ledger governed by this skill itself: one theory per
collection, one claim per file, `label:` and `standing:` in frontmatter.
`design.md` is the entry point.

`SKILL.md` and `SKILL.kb/` are the manual, and carry no claims.
