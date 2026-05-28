# ADR: `agent-skill://` URI scheme for cross-skill references

## Status

Accepted 2026-05-18. Scope broadened 2026-05-27 (see Decision).

## Context

Skills reference each other two ways: as a dependency to load
(`requires:`/`depends:` frontmatter, prose mentions) and -- once schema
reuse lands -- as a path to a skill-owned file (jsonschema `$ref`/`$id`).
Both need a stable, resolvable notation.

Two pressures forced the question:

- Schema duplication: six byte-identical `*.jsonschema.yaml` copies
  hand-propagate every field change. Collapsing them to one source of
  truth needs a `$ref` that points at a skill-owned file -- which needs
  a URI grammar.
- Notation sprawl: skill references were written `Skill(<name>)`, a
  bespoke notation with no resolver and no normative referent.

## Decision

Use the URI scheme:

    agent-skill://<skill-name>/<path-within-skill>

- scheme: `agent-skill`
- authority (netloc): the skill name, kebab-case (e.g. `llm-kb`)
- path: the path within the skill root; empty when referring to the
  skill itself

Examples:

    agent-skill://llm-subtask                       # the skill (load directive)
    agent-skill://llm-subtask/sweh.jsonschema.yaml  # a skill-owned file ($ref/$id)

**Resolution contract.** A resolver maps authority + path to a
skill-owned file: `~/.claude/skills/<authority>/<path>`. For jsonschema,
an in-memory index by declared `$id` is the preferred mechanism, with the
filesystem path as fallback. No remote (`http`) resolution is needed for
the primary use case.

**Scope, 2026-05-18 (initial):** URIs only where path resolution matters;
`Skill(<name>)` stays in human-facing fields.

**Scope, 2026-05-27 (broadened -- supersedes the above):** the scheme is
the single notation for all cross-skill references. The no-path form
`agent-skill://<name>` replaces `Skill(<name>)` everywhere, including
load-directive frontmatter. Replacing the existing `Skill(<name>)`
occurrences is a transformation tracked as a migration (see References).

## Why this scheme

Anchors to Anthropic's Agent Skills open standard (released 2025-12-18;
spec at agentskills.io; repo github.com/agentskills/agentskills; adopted
by Microsoft VS Code/GitHub, OpenAI ChatGPT/Codex, Cursor, Goose,
OpenCode). The `agent-skill` qualifier disambiguates from other meanings
of "skill" (Alexa Skills, Semantic Kernel skills) and gives the scheme a
stable normative referent.

Authority position for the skill name is correct, not merely workable.
RFC 3986 defines authority as the naming authority that governs the
namespace -- the role a skill plays over its files. And authority + an
absolute path makes RFC 3986 relative-reference resolution behave
intuitively for `$ref`: a `$ref: y.yaml` beside
`$id: agent-skill://llm-kb/a/x.yaml` resolves to
`agent-skill://llm-kb/a/y.yaml`.

## Consequences

**Positive:**

- One resolvable notation for both load-directives and file refs.
- Enables `$ref` to a single schema source of truth, killing the
  six-copy duplication.
- Stable normative referent (the Agent Skills standard).

**Negative:**

- The no-path load-directive form must be taught: agents and every
  SKILL.md `setup:` block must treat `agent-skill://<name>` as the load
  directive that `Skill(<name>)` was, or skill-loading silently stops
  triggering.
- A custom resolver is required; off-the-shelf jsonschema tooling does
  not resolve `agent-skill://` without it.

## Alternatives Considered

- Retain `Skill(<name>)` for references, URIs only for files: the
  2026-05-18 position; rejected 2026-05-27 in favor of one unified
  notation.
- Opaque/URN form `agent-skill:<name>/...` (no `//`): rejected -- with no
  authority, RFC 3986 relative-`$ref` resolution does not behave
  intuitively, and the clean skill->path hierarchy is exactly what
  authority position expresses.
- Remote `http(s)` `$ref`: unnecessary; skills resolve locally in-memory.

## References

- Transformation (the notation sweep): `agent-skill://llm-kb/migrations.kb/2026-05-27-000-skill-notation-to-agent-skill-uri.md`
- `$ref` implementation work: `agent-skill://llm-kb/.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md`
