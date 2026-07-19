# Trigger subsystem: condition vocabulary and interpretation model (T4)

**Date:** 2026-07-19
**Status:** Accepted

## Context

`design-next.kb/040-design.kb/delivery-boundary.md` had stood as
`status: proposal` since T2, deliberately incomplete: v1's
`hook-wiring.md` / `plugin-delivery.md` / `delivery-contract.md`
were deleted rather than carried forward, on the grounds that
formalizing a verb contract or hook-event mapping from kb core,
before a dedicated session existed to own that surface, would be the
exact boundary-jumping the tower exists to stop. `.claude/todo.md`
named the session T4 and listed four open surfaces: condition
vocabulary, compilation model for action-shaped triggers (risk:
hooks-in-disguise), bank format, and a packaging verdict (peer
standard vs. in-suite package, gated on a real
triggers-without-kb consumer).

One empirical input was inherited from the retired
`integrate-sessions-kb-into-llm-subtask` taskfile: whether
skill-bundled `commands/` subdirectories resolve as top-level
`/<name>` commands, bearing on the adapter-side packaging story.

## Decision

Recorded forward-facing in `llm-triggers/design.kb/040-design.kb/`
(new skill, seeded this session) plus updates to
`design-next.kb/040-design.kb/class-trigger.md` and
`delivery-boundary.md`. Per axis:

1. **Packaging** — in-suite, not peer. Triggers depend on
   `Skill(llm-kb)` outright; a triggers-without-kb consumer is not a
   deferred case, it's a non-concept, so no revisit trigger is
   recorded. `llm-triggers/` is the trigger class's successor to
   `llm-must-read-kb`, holding subsystem specifics at a grain finer
   than design-next.kb's — mirroring `llm-vitals/design.kb/` as a
   sibling-skill design tower, not a peer standard.
2. **Condition vocabulary** — three neutral kinds seed it: command
   pattern, path pattern, lifecycle point. Membership test (the
   hooks-in-disguise guard): a condition kind is admitted only if an
   agent with no enforcement mechanism could still notice the
   situation itself during planning — "about to run `git commit`"
   passes, "PreToolUse fired with matcher X" fails. Every
   action-shaped trigger in the v1 personal bank and the superseded
   standing-hook list is expressible in the three kinds.
3. **Compilation model — rejected in favor of interpretation.** No
   compile step: one static interpreter shim per interception point,
   installed once per runtime, reads trigger files at fire time and
   matches the live action against each condition. Consequence:
   staleness is structurally impossible (no generated artifact to
   drift from source), and `class-trigger.md`'s old "`kb doctor`
   verifies the compilation is current" is replaced by a coverage
   report (bound vs. floor-only), which cannot go stale by
   construction.
4. **The floor** — a filename-indexed bank, scanned at plan time,
   requiring zero runtime support — is not a fallback but the base
   semantics every trigger carries on every consumer; mechanical
   binding strengthens delivery of that same meaning, never replaces
   it. This is what makes per-consumer support level non-lockstep:
   bindings are local upgrades, and an unbound trigger is still
   fully enforced at the floor, never "broken."
5. **Bank format** — one authoring format for both partitions of
   `class-trigger.md` (action-shaped and judgment-shaped); only
   enforcement strength varies by detectability. V1's juncture
   convention (`before/`/`after/`/`when/`) carries forward
   unchanged.
6. **Task↔trigger boundary** (T3's inherited open item) — resolved
   as a shared wake-condition value grammar (`trigger-desc.md`):
   juncture (`at`/`before`/`when`/`after`) × self-disambiguating
   type (date/instant/`file:`/prose), serving task deferral
   (`task-deferral.md`) and `070-future-work.kb`'s existing
   `trigger:` field as one primitive, cited by both rather than
   restated.
7. **Empirical input** — tested directly (scratch skill at
   `~/.claude/skills/t4-test-skill/` with a `commands/` subdir,
   probed via `claude -p`, then removed): skill-bundled `commands/`
   directories do **not** resolve, neither as `/<name>` nor
   `/<skill>:<name>`. The skill itself is the top-level `/<skill>`
   command (commands and skills merged). Only plugins bundle
   multiple verbs, namespaced `/<plugin>:<name>`. Recorded in
   `llm-triggers/design.kb/040-design.kb/claude-code-adapter.md`;
   strengthens rather than contradicts the superseded
   `plugin-delivery.md`'s one-plugin conclusion, now raw material
   for the adapter entry rather than restated tower content.

## Journey

Opened as a Cucumber-BDD analogy (condition text vs. per-system
glue) — explicitly not a proposal to use the `cucumber` library,
just the human-writable/machine-bound split. The floor concept is
this session's real generalization of that analogy: unlike Cucumber,
where an unbound step is broken, an unbound trigger here is fully
meaningful at the floor, which is what buys graceful, non-lockstep
per-consumer elaboration.

The compilation-vs-interpretation question was raised by the
operator directly, declining to presuppose implementation: "let's
stay schematic for the moment, focus on inherencies not
incidentals." The resulting split — inherent: trigger files at
thought-speed, plus some per-system adapting code; incidental:
whether that code is a compiler — led to interpretation once the
question was posed as "is a no-compile design feasible," not
assumed answered by v1's language ("compiled into whichever
adapter").

Recording home was a live correction mid-session: the assistant's
first framing collapsed "no separate packaging standard" (axis 1)
into "no separate recording home," concluding T4's results should
land directly in `design-next.kb`. Operator counter: the two
questions are independent, and design-next's own grain is too
coarse for seed-vocabulary and schema-level detail — `llm-triggers/`
with its own `design.kb/` is the better fit, cross-cited rather than
inlined. Adopted; `design-next.kb` was pared back to properties plus
citations once the split was accepted.

The trigger-desc schema (strawman by the operator) was flagged by
the assistant, on presentation, as likely due for a redesign: the
juncture × type matrix expresses more than deferral (dependency
wakes via `after: file:`, deadlines via `before:` + time), which the
operator's "how to defer" framing hadn't separately named. Recorded
as `status: proposal` with per-cell semantics open, rather than
either forcing false precision or discarding the useful strawman.

## Alternatives Considered

- **Compile trigger files into generated adapter wiring** (v1's own
  framing, and this session's opening assumption) — rejected: a
  compiled artifact re-introduces, in generated form, the exact
  staleness class v1 suffered in prose form, and demands per-trigger
  regeneration machinery that a fire-time read makes unnecessary.
- **Peer standard packaging** (todo.md's original framing) —
  rejected outright, no live consideration needed: the gating
  consumer (a real triggers-without-kb use case) doesn't exist and
  triggers are declared dependent on `llm-kb` by design, so the gate
  can never fire.
- **Recording T4's results directly in `design-next.kb`** — proposed
  by the assistant, rejected by the operator; see Journey. Superseded
  same session by the `llm-triggers/design.kb/` split.
- **A second grammar for task deferral** distinct from future-work's
  `trigger:` field — implicitly rejected: both are one wake-condition
  primitive (`trigger-desc.md`) with per-class field-name framing,
  per `shared-shape-separate-semantics`.

## Consequences

**Positive:**

- `class-trigger.md` and `delivery-boundary.md` now state properties
  only (interpretation, floor-always-on, adapter-only coupling) and
  no longer carry a `status: proposal` / "pending T4" placeholder —
  the v2 build's T4 blocker is cleared.
- The trigger class has a named, seeded successor skill
  (`llm-triggers/`) rather than an unstarted placeholder.
- The task↔trigger boundary (T3's open inheritance) is resolved with
  a concrete, if `proposal`-status, mechanism.

**Negative:**

- `llm-triggers/design.kb/` carries several `status: proposal`
  entries and `[!QUESTION]` blocks of its own (field names for the
  `on:` elaboration block, per-cell sweep semantics for
  `trigger-desc.md`, exact hook-event bindings) — real design debt,
  not yet a landing blocker but due before the subsystem is built.
- `llm-must-read-kb` and `llm-triggers` are now two skills describing
  overlapping territory (the former the working v1 banks, the latter
  the v2 design) until the fold-in at build time; not yet a source of
  drift since neither's content restates the other's.

**Neutral:**

- The "Ratify (or reject) the tower's `status: proposal` entries"
  sweep (already queued in `.claude/todo.md`) now also covers
  `llm-triggers/design.kb/`'s new proposal-status entries.

## Related

- Related to: `llm-triggers/design.kb/` (the forward-facing
  recording); `design-next.kb/040-design.kb/class-trigger.md`,
  `delivery-boundary.md` (the ecosystem-level properties, now citing
  down); `docs/dev/adr/2026-07-19-000-Task-domain-dissolves-into-spec-primitives--T3-.md`
  (T3, whose task↔trigger boundary this ADR resolves)
