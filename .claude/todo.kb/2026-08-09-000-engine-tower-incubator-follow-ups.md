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
the tooling itself — plus a handful of operator rulings the
mechanization surfaced (see Open Questions).

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

## Open Questions

Operator rulings still live after the 2026-08-09 act review + purpose
restructure (32b1a76), which settled the rest of that day's
wiggle-room: COMPLETION's repair is ruled (antichain completion, the
assessor law made structural), certified-grants dissolved into
ASSESSOR/STANCE, and CONFINE's content is fixed by OBLIGATION's
executable statement plus DEFINED_SORTS.

- [ ] OBLIGATION's toolchain: green-light Lean 4 procurement (elan) or
      name another proof-grade home ("whichever proof assistant the
      fleet procures"). Cross-referenced from
      `~/.claude/sessions.kb/penguin/2026-08-09-status-lattice-cross-reference.md`.
- [ ] uv.lock floats: the repo .gitignore excludes it, so the suite's
      environment drifts (last run: Python 3.14.0rc2, pytest 9). Pin
      per-incubator or accept the float.
- [ ] Offered, unclaimed: mechanize COMPLETION's now-ruled repair
      (assessor-indexed verdict maps make Phi total; the crash test
      becomes a witness of the un-completed order); mutation-testing
      pass over the 27-test suite; pilot computed standing on a real
      `.kb`.

## Success Criteria

- [ ] One repo-root command typechecks the incubator with 0 errors.
- [ ] TWICE `verify:` shape decided and recorded.
- [ ] Each Open Question ruled and implemented, or explicitly dropped
      here with a reason.
