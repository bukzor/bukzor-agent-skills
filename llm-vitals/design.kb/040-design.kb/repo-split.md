---
why:
  - decoupled-data-location
  - unify-personal-and-enterprise
---

# Repo Split

Three-way separation between skill code, personal/wellness data, and
business data:

- **Skill** → `bukzor-agent-skills/llm-vitals/` (public, open-source)
- **Personal / wellness data** → `private.evan-family/vitals/`
  (private; matches the repo's "personal planning" scope)
- **Business data** → `private.bukzor-llc/vitals/` (private; matches
  the LLC repo's business scope)

The skill reads from multiple `vitals_root:` paths via configuration
(`~/.claude/llm-vitals.yaml`). Picker merges across roots.

Why split rather than mingle:

- Respects existing repo semantics (each private repo's described
  scope).
- Better blast radius if any one repo is compromised or shared.
- Wellness data and business data have different sensitivity and
  potential sharing audiences.

The split costs ~10 lines of merge logic in the picker and pays for
itself in correct semantic placement.
