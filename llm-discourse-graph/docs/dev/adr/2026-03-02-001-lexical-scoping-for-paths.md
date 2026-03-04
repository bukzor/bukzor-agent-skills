---
status: accepted
date: 2026-03-02
---

# Lexical scoping for path resolution

## Context

Nodes cross-reference each other via paths in YAML frontmatter. When content
is shared across scopes, it gets hoisted to a common ancestor. Need a
referencing scheme that doesn't break when files move between scopes.

## Decision

Path resolution walks up ancestor scopes, like `node_modules` resolution or
shell `$PATH` lookup. A reference to `claims.kb/conways-law.md` checks:

1. `./claims.kb/conways-law.md` (current scope)
2. `../claims.kb/conways-law.md` (parent scope)
3. Up to project root

## Alternatives considered

**Explicit relative paths** (`../../claims.kb/x.md`): Precise but brittle.
Every hoist requires updating all references. Verbose.

**Symlinks:** Leave file in original location, symlink from new scope. Git
handles symlinks inconsistently. Hides true dependency structure. Breaks
when targets move.

**Global IDs / URIs:** Indirection layer. Requires a registry. Overkill for
a filesystem-based format.

## Consequences

- Hoisting is non-breaking — all existing references still resolve
- Shadowing works — local file overrides ancestor with same name
- Paths stay short — always `collection.kb/item.md`
- Moving content *down* (narrowing scope) can break references from
  sibling scopes — this is correct behavior (removed from their visibility)
- Tooling must implement ancestor-walking resolution
