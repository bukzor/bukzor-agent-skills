---
name: llm-sessions
description: "Session log kept as files. Agent MUST load when reading or maintaining a sessions.kb/ directory, or when asked to record, find, or reconcile claude-code sessions."
---

# LLM Sessions

A `sessions.kb/` collection tracks claude-code sessions -- in flight,
planned, or recently relevant -- so many parallel lines of work stay
findable. One entry per session or per host; entries carry the session
uuid (which is also the transcript name under `~/.claude/projects/`),
when it ran, and what it was for.

## Schema

`jsonschema/sessions.jsonschema.yaml` is the canonical. A collection binds
it positionally: `sessions.kb/*.md` validates against a sibling
`sessions.jsonschema.yaml`, which should be a one-line stub:

```yaml
# yaml-language-server: $schema=https://json-schema.org/draft-07/schema
$ref: "skill://llm-sessions/jsonschema/sessions.jsonschema.yaml"
```

Per-host sub-collections do the same, file-relative
(`$ref: "../sessions.jsonschema.yaml"`), so one edit to the canonical
reaches every host.

The schema declares the llm-kb dialect for its `instant`/`date` types, and
`$ref`s `cost-benefit-sweh` across to Skill(llm-subtask) rather than
restating it -- a session and a task rate their cost the same way.

## Worked example

`~/.claude/sessions.kb/` is the live collection; its `CLAUDE.md` is the
maintenance guide for that particular log (naming, what earns an entry,
how host sub-collections are organized).
