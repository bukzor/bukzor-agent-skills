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
- `why:` frontmatter items are file-relative paths ending in `.md`
  (`../020-goals.kb/reduce-dropped-tasks.md`), per
  `skill://llm-design-kb/jsonschema/layer-entry.jsonschema.yaml`.
