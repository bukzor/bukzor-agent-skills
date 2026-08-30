# TODO

- [ ] First sweep consumer: the bukzor-llc gutters (user-approved
      2026-08-30, prepended to that repo's work plan).
      private.bukzor-llc's beam-search gutters are wake-shaped and map
      onto three existing use-cases: `deadline-escalation.md` (G2, a
      dated fuse), `obligation-age-flag.md` (G1, weekly expansion),
      `stale-session-retirement.md` (play-charter fuses in
      sessions.kb). Building the SessionStart sweep shim against them
      settles the design's four open questions: recurrence notation
      (`trigger-desc.md`), where evaluation state lives, emission/nag
      semantics (`sweep.md`), and exact hook junctures
      (`claude-code-adapter.md`). Shape agreed with the operator:
      conditions stay in-place as frontmatter wake descs; a
      per-consumer `.claude/triggers.yaml` carries only adapter-grade
      delivery config (stores to walk, emission budget); the llc todo
      item carries the instance-side edit list
