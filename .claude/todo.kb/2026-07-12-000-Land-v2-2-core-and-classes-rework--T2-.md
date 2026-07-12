---
managed-by: Skill(llm-subtask)
---

# Land v2.2 core-and-classes rework (T2)

**Priority:** Medium
**Complexity:** High
**Context:** 2026-07-12 session (sessions.kb/penguin/design-next-kb-v2-refinement.md);
supersedes the tower's five-layer framing. Baseline committed at 757b46b.

## Problem Statement

design-next.kb's 040 layer is built on v2.0's function-grouped stack,
which contradicts `020-goals.kb/designed-for-deletion.md` (domain
units, thin core). The v2.2 direction is settled; the reworked
entries are not yet written.

## Settled (2026-07-12, operator-confirmed)

- **Core-and-classes**: kb system = four kinds — spec (1), engine (1,
  class-blind), class (1/domain, the deletion/adoption unit), data
  (many). Class packages carry conventions page, schema, templates,
  triggers, checks — reaching core only as runtime data (discovery).
- **Invariant**: nothing below a class names the class. Checkable:
  grep engine source for class names → zero; `git rm -r <class>` →
  core green; `kb new <gone-class>` fails cleanly.
- **Layer numbers dropped entirely** (operator: "very opaque").
- **Delivery boundary**: delivery machinery (3 verbs, adapters,
  compilation) leaves kb core. Packaging of the trigger subsystem is
  `status: proposal` pending T4 (see todo.md).
- **Data flow**: class→spec required; class→class citation/composition
  only (never subclassing); class→engine verb-citation only with
  engine-absent degradation; engine→class and spec→anything disallowed.
- Genre→class rename confirmed earlier (2026-07-11); haiku sweep
  queued in todo.md, blocks the prose rework.

## 040 Blast Radius (fully classified 2026-07-12)

- **Rework, major**: five-layer-stack (→ core-and-classes: kinds
  table, dependency rules, v1-pieces mapping), kb-engine (class-blind
  interpreter, discovery contract), plugin-delivery + delivery-contract
  + hook-wiring (migrate to trigger-subsystem design, kb keeps only
  the boundary statement), thin-skills (folds into new
  class-package.md).
- **Rework, minor**: memory-policy (split runtime-neutral property
  from CC mechanism — already a defect under the old coupling rule's
  own grep check), cross-reference-notation (drop layer vocabulary;
  re-ground `skill://` roots in class packages).
- **Rename/rewording only**: genre-*.md → class-*.md (task pends T3;
  record pends residue test).
- **Survives**: decisions-are-settled-questions, kb-spec (stays
  trigger-ignorant per boundary).
- **Separately queued**: references-are-structured-data,
  kb-spec.kb/synthesis-file.
- **030 additions**: classes-detach-cleanly.md (why:
  designed-for-deletion — closes the goal's currently-empty why
  chain); rename coupling-is-layer-3-only → coupling-is-adapter-only.
- New: class-package.md defines the class kind ("an application of
  llm-kb"; composition/citation, never subclassing; prior art:
  application profile).

## Implementation Steps

- [ ] Haiku genre→class sweep (todo.md; mechanical, blocks the rest)
- [ ] Draft 030 additions + coupling rename
- [ ] Draft 040 reworks per classification above
- [ ] CLAUDE.md sweeps (design-next.kb/ + 040-design.kb/)
- [ ] Adversarial review of the drafts in a fresh context (subagent or
      separate session — reviewer gets the tower + drafts, never the
      drafting session's narrative), targeting the Open Questions below
- [ ] Land: apply review verdicts, commit, update this brief

## Open Questions — targets for the review pass

Three spots where this session's consensus formed fastest and
deserves a skeptic (advocate/skeptic/arbiter or a framing-free
session):

- Teaching collapse (class conventions page = SKILL.md = delivered
  teaching) — proposed unilaterally by the agent, never discussed.
- Engine-reads-classes-as-data feasibility for `kb new` and doctor
  checks — where the invariant could die on contact with mechanism;
  declarative-check expressiveness is unproven.
- Decision 3 unconfirmed: class-local code = consumer status (stable
  formats in, no engine hooks) — task-archeology stance generalized.

## Success Criteria

- [ ] Every 040 entry matches its classification; no entry outside
      adapter/trigger-subsystem scope names a runtime mechanism
- [ ] designed-for-deletion has a checkable 030 requirement and
      inbound why: references
- [ ] Drafts survive the adversarial pass on the three named spots

## Notes

Solutions floated in-session were proof-of-existence, not normative
(standing operator caveat). DRY-within-unit compile mechanism stays
open (yaml-to-four-surfaces = existence proof only).
