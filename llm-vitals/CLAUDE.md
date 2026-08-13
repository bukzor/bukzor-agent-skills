--- # workaround: anthropics/claude-code#13003
requires:
    - Skill(llm-kb)
depends:
    - Skill(llm-design-kb)
---

# llm-vitals

A multi-axis attention-allocation system across personal, wellness,
and business domains, modeled on SRE observability with two-tier
accountability. See `design.kb/010-mission.md` for the mission
statement.

## Collections

- `design.kb/` — layered design documentation (mission, goals,
  requirements, architectural design, deferred ideas). The skill is
  not yet implemented; this directory is currently design-only.

## Conventions

- `.kb/` ↔ `.md` follow growth pressure: stay flat until items need
  per-entry detail.
- `why:` frontmatter slugs reference file stems (`reduce-dropped-tasks`)
  with order prefixes stripped (`010-mission` → `mission`), per the
  `llm-design-kb` skill's example pattern.
