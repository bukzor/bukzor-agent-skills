---
why:
  - interpretation-not-compilation.md
  - ../../../design-next.kb/030-requirements.kb/coupling-is-adapter-only.md
status: proposal
---

# Claude Code Adapter

Everything here is Claude-Code-specific by design — the adapter is
the one place runtime nouns belong (coupling-is-adapter-only). It is
a set of interpreter shims (`interpretation-not-compilation.md`)
wired once in hook configuration with broad matchers; hook payloads
are never generated per-trigger.

Condition-kind bindings:

- **command pattern** → PreToolUse / PostToolUse on the shell tool;
  the shim matches the live command string and emits the body as
  injected context, or as the deny reason for hard gates.
- **path pattern** → PreToolUse / PostToolUse on file-writing tools,
  matching the touched path.
- **lifecycle point** → SessionStart (orientation delivery) and
  Stop / SessionEnd (capture nudges).

The floor's wiring is prose: the host CLAUDE.md's Required Reading
stanza naming the bank — v1's mechanism, unchanged.

Operator verbs: a skill is itself a top-level `/<skill>` command, and
that is the only per-directory grant — nested `commands/` dirs inside
a skill do not resolve, top-level or namespaced (verified
empirically). Multiple verbs therefore ship as sibling skills, or as
a plugin (`/<plugin>:<name>` namespace) — making the plugin the only
single-install bundle for shims, verbs, and teaching together.

> [!QUESTION] which hook events, exactly?
> The event names above are today's; bindings settle when the first
> shim is built, and belong to this entry alone when they do.
