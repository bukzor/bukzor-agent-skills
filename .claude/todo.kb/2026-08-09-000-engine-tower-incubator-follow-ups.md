---
managed-by: Skill(llm-subtask)
status: active
---

# Engine-tower incubator follow-ups

**Priority:** low — quality-of-tooling, nothing blocks on it
**Complexity:** small (each item < 1 hour)
**Context:** `docs/dev/design-incubators/engine_tower/`, reviewed
2026-08-09 (see devlog
`2026-08-09-000-Engine-tower-review--FREE-CONSERVE-premise--poset-check-hole.md`).

## Problem Statement

The incubator's witnesses run at tooling grade, but two gaps remain in
the tooling itself.

## Implementation Steps

- [ ] Typecheck wiring for the incubator. Pyright reports 0 errors
      from the project root but 25 spurious `engine_tower` import
      errors from the repo root, so there is no one command a repo-root
      agent can run as a gate. Add the wiring (e.g. a repo-root-safe
      invocation: `uv --directory docs/dev/design-incubators/engine_tower run pyright`,
      wired wherever this repo keeps check commands). COMPLETION's own
      moral is grade escalation: a law binds only through whoever
      computes it.
- [ ] Decide the TWICE verify: shape — operator call. The other agent
      deliberately kept a single poset test with the hand-mirrored
      PRIORS table ("update both together" comment). Alternative: pair
      witness `pytest tests/test_genre.py tests/test_tower.py`, one
      occurrence per file. Pick one and note the rationale in the
      ledger claim; either answer closes this.

## Success Criteria

- [ ] One repo-root command typechecks the incubator with 0 errors.
- [ ] TWICE `verify:` shape decided and recorded.
