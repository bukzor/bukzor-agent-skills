---
why:
  - ../../../design-next.kb/030-requirements.kb/action-triggers-enforced-deterministically.md
  - condition-vocabulary.md
---

# Interpretation, Not Compilation

Trigger files are runtime data, read at fire time. Per consumer
runtime there is one static **interpreter shim** per interception
point, installed once. When the runtime's interception fires, the
shim scans the reachable banks, matches the live action against each
trigger's condition (elaborated frontmatter where present, filename
grammar otherwise), and delivers any matched body — as injected
context, or as the deny reason for hard gates.

Properties this buys:

- **No per-trigger artifacts.** Authoring a trigger is writing one
  file; no build step, nothing to regenerate.
- **Staleness is structurally impossible.** There is no compiled
  copy to drift from its source; the only static artifact is the
  shim, whose content is independent of the bank's contents.
- **Zero-system floor.** A consumer with no shims at all retains the
  full floor semantics (`floor.md`) with no code anywhere.
- **Non-lockstep enhancement.** Each runtime's shims bind whichever
  condition kinds that runtime can detect; consumers never need to
  match each other's support level, because bindings are local and
  the floor is universal.

Observability is a **coverage report**, not a staleness check: which
action-shaped triggers are mechanically bound on this system versus
floor-only. Prior art for the shape: git's hook scripts and the
`pre-commit` framework — a generic hook installed once, configuration
consulted at run time.

**Why not compile trigger files into adapter wiring:** a compiled
artifact re-introduces, in generated form, the staleness class v1
suffered in prose form, and demands per-trigger regeneration
machinery whose whole job the fire-time read does for free.
