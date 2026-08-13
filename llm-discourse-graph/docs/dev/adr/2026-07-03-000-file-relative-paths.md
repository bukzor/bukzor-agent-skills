---
status: accepted
date: 2026-07-03
supersedes: 2026-03-02-001-lexical-scoping-for-paths.md
---

# File-relative paths (supersedes lexical scoping)

## Context

The lexical-scoping ADR (2026-03-02-001) decided on ancestor-walking
path resolution, explicitly noting
"Tooling must implement ancestor-walking resolution" as a consequence.
No such tool was ever built. The only real enforcement is `llm-kb`'s
cross-references self-audit, which checks that a written relative path
resolves via ordinary filesystem semantics from the referencing file --
i.e. it already assumes file-relative paths, not ancestor-walking.
Real usage (`ideation.physical-musings`, 2026-07-03) confirmed this:
every cross-reference written was `../collection.kb/item.md`-style, and
validated correctly under plain relative-path resolution.

## Decision

Cross-references are ordinary file-relative paths. No resolution layer
walks ancestor scopes; a path means exactly what `cd $(dirname
$referencing_file) && test -e $path` would find.

## Consequences

- Hoisting is no longer non-breaking: moving a file requires updating
  every path that points to it and every path it itself contains. This
  is the cost lexical scoping was explicitly trying to avoid, now accepted.
- Shadowing (a local file silently overriding an ancestor of the same
  name) is no longer a real mechanism -- there was never tooling that
  implemented it, so nothing actually relied on it.
- No new tooling is required beyond what `llm-kb`'s existing
  cross-references audit already does.
- Placement (which scope a node lives at) is still a real judgment
  call -- it's just not backed by an automatic resolution mechanism.
