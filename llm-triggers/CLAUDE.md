--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
depends:
    - Skill(llm-design-kb)
---

# llm-triggers

The kb suite's trigger subsystem: condition-triggered directive
delivery across agent runtimes. Design phase — `design.kb/` is the
content; no runtime machinery ships yet. Successor to
`llm-must-read-kb`, which still documents the working v1 banks.

## Collections

- `design.kb/` — layered design per `Skill(llm-design-kb)`
