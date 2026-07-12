---
why:
  - procedures-are-tools
  - degrade-gracefully
---

# Thin Skills

Exactly three teaching skills, each `paths:`-gated for deterministic
activation with description matching kept as fallback:

- **kb** (paths: `**/*.kb/**`) — recognize the collection shape in
  any starting form; call the engine for mechanics. Teaches judgment
  the engine can't make: what's homogeneous, what deserves a schema,
  when a summary file pays.
- **epistemic** (paths: `**/design*.kb/**`, discourse dirs) — the
  why-chain and claim-graph judgment: which of the two node genres
  (design vs. discourse) a new entry belongs in, layer/type placement
  within it, cross-linking between the two, when to elaborate vs roll
  up.
- **attention** — task-tier selection, session-note judgment,
  check-in verbs; the operator-facing surface of the task genre.

Each stays near ~300 words of *recognition* content — the
`claude-realignment` skill is the v1 proof that a tight, single-job
skill needs no accretion. Everything mechanical the skills once
narrated is an engine call; everything enforceable is a hook. That is
the structural fix for v1's SKILL.md bloat: the container stops being
the only place anything can live.

The base SKILL.md fields (name, description, body) are the actual
portable layer — the agentskills.io open standard, adopted across
~26 vendors. Claude Code's `paths:`-gated activation is a proprietary
enhancement; its fallback, description-only matching, is
simultaneously the within-CC degradation path (`degrade-gracefully.md`)
and the cross-runtime floor every other adapter gets by default.
