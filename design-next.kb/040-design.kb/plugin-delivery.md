---
why:
  - ../030-requirements.kb/degrade-gracefully.md
  - ../030-requirements.kb/action-triggers-enforced-deterministically.md
---

# Layer 3, Claude Code Adapter: Plugin Delivery

The layer-3 contract (`delivery-contract.md`) is runtime-agnostic;
this entry is its **Claude Code adapter**, not a universal
prescription. Under Claude Code the system ships as **one plugin**:
hooks (`hooks.json`), thin skills, path-scoped rules, slash commands,
and the engine under `bin/`. The plugin manifest is the single place
where activation is wired; installing the plugin is the whole setup
story, replacing v1's symlink farm plus per-project `setup:`
frontmatter blocks that each consumer had to copy-paste.

Division of native primitives by job:

- **Hooks** — enforcement and lifecycle (see `hook-wiring.md`).
- **Skills** — procedural teaching (see `thin-skills.md`).
- **Rules** (`paths:`-scoped) — short passive conventions that should
  be present while touching matching files (e.g. why-chain rules
  active under `**/*.kb/**`).
- **Commands** — operator-invoked verbs (`/checkin`, `/session-end`).

**Why not per-class plugins:** the classes share the spec and engine;
separate plugins would reintroduce version skew between them — the
exact v1 disease.
