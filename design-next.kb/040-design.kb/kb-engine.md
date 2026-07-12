---
why:
  - procedures-are-tools
  - validators-outlive-migrations
---

# Layer 1: The kb Engine

One CLI, `kb`, implementing the spec:

- `kb new <genre> --title …` — genre-aware generators (one slug
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

The engine is where shared improvement concentrates: a slug fix, a
naming change, a new audit lands once. Agents are taught to
*recognize* situations and call the engine — never to execute
mechanical steps from prose.

The CLI is the portable interface by construction — any shell-capable
agent or human drives it with zero adapter work. Exposing the same
verbs over MCP (`../070-future-work.kb/mcp-server-adapter.md`)
extends that to any MCP-speaking client without per-runtime rewrites.
