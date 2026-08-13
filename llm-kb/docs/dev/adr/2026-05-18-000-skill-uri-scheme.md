# ADR: `skill://` URI scheme for cross-skill references

## Status

Accepted 2026-05-18. Scope broadened 2026-05-27. Renamed `agent-skill://`
-> `skill://` 2026-07-05 (see Decision).

## Context

Skills reference each other two ways: as a dependency to load
(`requires:`/`depends:` frontmatter, prose mentions) and -- once schema
reuse lands -- as a path to a skill-owned file (jsonschema `$ref`/`$id`).
Both need a stable, resolvable notation.

Two pressures forced the question:

- Schema duplication: byte-identical `*.jsonschema.yaml` copies
  hand-propagate every field change. Collapsing them to one source of
  truth needs a `$ref` that points at a skill-owned file -- which needs
  a URI grammar.
- Notation sprawl: skill references were written `Skill(<name>)`, a
  bespoke notation with no resolver and no normative referent.

## Decision

Use the URI scheme:

    skill://<skill-name>/<path-within-skill>

- scheme: `skill`
- authority (netloc): the skill name, kebab-case (e.g. `llm-kb`)
- path: the path within the skill root; empty when referring to the
  skill itself

Examples:

    skill://llm-subtask                       # the skill (load directive)
    skill://llm-subtask/sweh.jsonschema.yaml  # a skill-owned file ($ref/$id)

**Resolution contract.** A resolver maps authority + path to a
skill-owned file: `~/.claude/skills/<authority>/<path>`. For jsonschema,
an in-memory index by declared `$id` is the preferred mechanism, with the
filesystem path as fallback. No remote (`http`) resolution is needed for
the primary use case.

**Scope, 2026-05-18 (initial):** URIs only where path resolution matters;
`Skill(<name>)` stays in human-facing fields.

**Scope, 2026-05-27 (broadened -- supersedes the above):** the scheme is
the single notation for all cross-skill references. The no-path form
`agent-skill://<name>` (at the time) replaces `Skill(<name>)` everywhere,
including load-directive frontmatter. Replacing the existing
`Skill(<name>)` occurrences is a transformation tracked as a migration
(see References).

**Rename, 2026-07-05 (supersedes the `agent-skill` scheme name):**
dropped the `agent-` prefix -- `agent-skill://` -> `skill://`. See "Why
this scheme" for what changed.

## Why this scheme

Anchors to Anthropic's Agent Skills open standard (released 2025-12-18;
spec at agentskills.io; repo github.com/agentskills/agentskills; adopted
by Microsoft VS Code/GitHub, OpenAI ChatGPT/Codex, Cursor, Goose,
OpenCode).

The scheme name was originally `agent-skill://`, reasoning that the
qualifier would disambiguate from other meanings of "skill" (Alexa
Skills, Semantic Kernel skills). That reasoning was superseded 2026-07-05
on discovering that a bare `skill://` scheme already exists for this
exact concept: the Model Context Protocol's Skills Extension (SEP-2640)
defines `skill://<skill-path>/<file-path>` to address Agent Skill
resources over MCP, with live adoption (FastMCP's Skills Provider,
skillsovermcp.com, Microsoft Agent Framework, Kiro CLI) and an open
Claude Code feature request (anthropics/claude-code#38253) to speak it
natively.

That scheme's grammar is, independently, the same one this ADR already
adopted: authority is the first path segment (the skill/locator name),
carries no host semantics ("clients MUST NOT resolve it as a network
host"), and the spec explicitly rejects the empty-authority triple-slash
form ("avoids the awkward triple-slash (`skill:///`) form while staying
honest about what the segment means") in favor of the same two-slash,
populated-authority shape used here. Since our resolution model (skill
name as authority, resolved to `~/.claude/skills/<name>/`, path within)
already matches that grammar for the path-bearing form, adopting the same
scheme name is alignment with a real, converging standard rather than a
collision with one -- a compliant MCP server rooted at the same directory
tree would resolve our `$ref` URIs to identical file content. Keeping the
`agent-` prefix to disambiguate from a standard that already agrees with
us would add a token for no protective benefit.

**Two use cases under one grammar.** SEP-2640 covers only resource-fetch:
its profile requires an explicit file-path (`SKILL.md` must be spelled
out; no default-to-entry-file shorthand), and it has no concept of a
dependency/load directive at all. This scheme carries two distinct uses:

1. Path-bearing (`skill://llm-subtask/sweh.jsonschema.yaml`) -- a
   resource reference, directly the SEP-2640 use case, byte-identical to
   what a compliant MCP server would serve from the same root.
2. Zero-path (`skill://llm-subtask`) -- a load directive, "depend on this
   skill," the one-to-one replacement for `Skill(<name>)`.

SEP-2640 doesn't bless the zero-path form -- its own profile always
requires a path, for its own (narrower) resource-fetch purpose -- but it
doesn't forbid it either, since dependency declaration isn't something it
addresses at all. The zero-path form is its own natural reading under the
general URI semantics both schemes share: an authority with an empty path
conventionally denotes the resource named by that authority itself (the
skill), the same way `scheme://authority` with no path is ordinarily read
as "the entity at that authority" across many schemes. We extend the
shared grammar to this second use case on that basis, not on SEP-2640's
authority.

Authority position for the skill name is correct, not merely workable.
RFC 3986 defines authority as the naming authority that governs the
namespace -- the role a skill plays over its files. And authority + an
absolute path makes RFC 3986 relative-reference resolution behave
intuitively for `$ref`: a `$ref: y.yaml` beside
`$id: skill://llm-kb/a/x.yaml` resolves to `skill://llm-kb/a/y.yaml`.

## Consequences

**Positive:**

- One resolvable notation for both load-directives and file refs.
- Enables `$ref` to a single schema source of truth, killing
  copy-paste schema duplication.
- Stable normative referent (the Agent Skills standard), and incidental
  alignment with MCP's `skill://` resource scheme (SEP-2640) should this
  repo, or Claude Code itself, ever serve skills over MCP.

**Negative:**

- The no-path load-directive form must be taught: agents and every
  SKILL.md `setup:` block must treat `skill://<name>` as the load
  directive that `Skill(<name>)` was, or skill-loading silently stops
  triggering.
- A custom resolver is required; off-the-shelf jsonschema tooling does
  not resolve `skill://` without it.

## Alternatives Considered

- Retain `Skill(<name>)` for references, URIs only for files: the
  2026-05-18 position; rejected 2026-05-27 in favor of one unified
  notation.
- Opaque/URN form `agent-skill:<name>/...` (no `//`): rejected -- with no
  authority, RFC 3986 relative-`$ref` resolution does not behave
  intuitively, and the clean skill->path hierarchy is exactly what
  authority position expresses.
- `agent-skill://` prefix to disambiguate from other "skill" namespaces:
  the 2026-05-18 scheme name; rejected 2026-07-05 on discovering MCP's
  SEP-2640 `skill://` scheme already occupies -- and agrees with -- this
  exact namespace and grammar. Disambiguating from a standard that
  already matches ours has no benefit and costs a token on every use.
- Remote `http(s)` `$ref`: unnecessary; skills resolve locally in-memory.

## References

- Transformation (the notation sweep): `skill://llm-kb/migrations.kb/2026-05-27-000-skill-notation-to-skill-uri.md`
- `$ref` implementation work: `skill://llm-kb/.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md`
- MCP Skills Extension SEP-2640 (`skill://` grammar):
  github.com/modelcontextprotocol/experimental-ext-skills, `docs/skill-uri-scheme.md`
