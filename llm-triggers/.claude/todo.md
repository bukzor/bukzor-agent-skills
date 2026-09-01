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
- [ ] Candidate wake condition for the sweep (user-approved
      2026-08-31): the sycophancy check — "a sitting closed with zero
      substantive opposition on any invested position → run the
      Advocate/Skeptic/Arbiter protocol at next session-start."
      Judgment-only desc, obligation-age-flag-shaped. Known risk to
      design against: an automatic skeptic invites performed
      skepticism; the companion control is the grade-with-disconfirmer
      gate in the must-read bank, which demands a named disconfirmer
      rather than a posture
- [ ] `design.kb/use-cases.kb/` has no sibling schema, so
      `llm.kb-validate .` fails at the repo root: "No schema found:
      llm-triggers/design.kb/use-cases.jsonschema.yaml" — the repo's
      only validation error, 1 of 624 files. The collection landed in
      8cc06b7/99166b1 (2026-08-27..28) and its entries carry
      frontmatter, so CANONICAL_PER_COLLECTION says write the schema
      rather than strip the frontmatter. Noticed 2026-09-01 by a
      session working elsewhere; left for whoever owns the use-case
      inventory, since the right shape depends on where that design is
      heading
