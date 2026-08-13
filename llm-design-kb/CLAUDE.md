--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-kb)
---

# llm-design-kb Skill

See `SKILL.md` for the design.kb layering pattern this skill defines.
This file gives maintenance guidance for agents working **on** the
skill itself (not consumers writing a project's own design.kb).

## Collections

- `principles.kb/` — reusable design-authorship rules, distinct from
  any one project's own goals/requirements
- `references/` — deep-dive guidance (`how-to-document-design-knowledge.md`)
- `jsonschema/` — shared schema fragments (`technical-policy.jsonschema.yaml`)
