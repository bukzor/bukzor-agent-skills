---
why:
  - ../030-requirements.kb/procedures-are-tools.md
  - ../030-requirements.kb/validators-outlive-migrations.md
  - ../030-requirements.kb/classes-detach-cleanly.md
---

# The kb Engine

One CLI, `kb`, implementing the spec as a **class-blind interpreter**:
its source names no class, only the spec's shapes (collection, entry,
dated record, linked node) plus a discovery contract for finding
whatever classes happen to be installed.

- `kb new <class> --title …` — class-aware generators (one slug
  implementation, one template mechanism; absorbs v1's eight
  `bin/` scripts).
- `kb init` — stand up a project's directories (absorbs the v1
  skeletons).
- `kb validate [path]` — schema + structural validation.
- `kb promote <path>` — flat file or ad hoc directory → canonical
  collection (absorbs the prose promotion procedure an agent
  demonstrably couldn't follow).
- `kb doctor` — the permanent battery of recurring convention
  validators; every migration adds one.
- `kb query …` — frontmatter-aware listing/filtering to the extent
  `ls`/`grep` need help (kept minimal; see future-work).

## Discovery contract

`kb new`, `kb validate`, and `kb doctor` all need to know which
classes exist and what each requires, without the engine's own source
ever spelling out a class name. The engine finds class packages at
runtime by directory convention — a class package is a directory at a
fixed relative layout (schema file, conventions page, templates) the
engine walks and reads as data — never by an import or a hardcoded
name. The schema it validates against, the template it fills, the
check it registers with `kb doctor`: all loaded from the package,
none compiled into the CLI.

This is what makes `git rm -r <class-package>` drop that class from
every `kb` surface simultaneously
(`../030-requirements.kb/classes-detach-cleanly.md`), and what makes
`kb new <gone-class>` fail on an ordinary lookup miss rather than a
crash once the package is gone.

> [!TODO]
> Sought: whether declarative checks loaded as data are expressive
> enough for the full `kb doctor` battery and for `kb new`'s
> class-aware generation, or whether some checks need code the
> engine can't safely load from a class package at runtime. Flagged
> for the adversarial review pass, not resolved here — if the
> ceiling is real, the discovery contract needs an escape hatch
> (e.g. a narrow, sandboxed check-script convention) without
> reopening engine→class source coupling.

The engine is where shared improvement concentrates: a slug fix, a
naming change, a new audit lands once. Agents are taught to
*recognize* situations and call the engine — never to execute
mechanical steps from prose.

The CLI is the portable interface by construction — any shell-capable
agent or human drives it with zero adapter work. Exposing the same
verbs over MCP (`../070-future-work.kb/mcp-server-adapter.md`)
extends that to any MCP-speaking client without per-runtime rewrites.
