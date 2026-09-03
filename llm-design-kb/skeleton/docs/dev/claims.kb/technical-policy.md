---
label: POLICY
standing: open
why:
  - design.kb/requirements.md
non-claim-tokens:
  - RFC
---

# <project> -- technical policy

Cross-cutting normative rules -- means, not ends: conventions,
constraints, and style decisions that bind work across the whole
project rather than describing any one part of it. Each policy claim
carries `force:` (`must` / `should` / `may`, RFC 2119) and a `why:`
naming the goal or requirement it serves.

Kept separate from the rungs because a policy is an imperative, where
a rung claim is a description: "the parser must reject unknown fields"
binds future work, while "the parser rejects unknown fields" reports
present behavior. A project with no cross-cutting policy deletes this
file and its collection.
