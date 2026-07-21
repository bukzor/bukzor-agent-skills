---
why:
  - ../010-mission.md
  - ../../../design-next.kb/030-requirements.kb/wake-conditions-are-noticed.md
  - ../../../design-next.kb/030-requirements.kb/degrade-gracefully.md
  - task-deferral.md
status: proposal
---

# The Sweep

The subsystem's third delivery mechanism, completing the set:
interception shims deliver action-shaped triggers, the floor scan
delivers judgment-shaped ones, and the sweep delivers wake-shaped
conditions (`trigger-desc.md`) — conditions anchored to time and
state rather than to a live action, which no interception point ever
sees.

Properties, stated as requirements on any implementation; the
mechanics below them are deliberately TBD:

- **Nothing recorded is skipped.** A sweep evaluates every wake
  condition in its scope: decidable descs mechanically, judgment
  descs enumerated for a cheap judgment pass — surfaced as a
  listing, like the floor, never silently dropped.
- **Surface, never dispose.** Emissions claim attention (a surfaced
  line, an escalation, a report); acting on a fired condition —
  completing, retiring, deleting — remains the agent's or operator's
  move. This authority ceiling holds even when the condition's body
  names the disposition (`../use-cases.kb/delete-when.md`).
- **Bounded emission.** What a sweep injects at any one juncture
  fits a small fixed budget; overflow degrades to a count plus a
  pointer, never a dump.
- **Interpretation, not compilation.** Conditions are read from
  their files at sweep time (`interpretation-not-compilation.md`);
  the sweep keeps no state beyond what evaluability requires
  (`trigger-desc.md`'s open evaluation-state question).
- **Zero-sweep floor.** Wake descs are ordinary frontmatter; a
  consumer with no sweep machinery still meets them at every
  planning-time read of their store, so missing tooling degrades
  wake delivery to noticing-at-read -- never to invisibility
  (`../../../design-next.kb/030-requirements.kb/degrade-gracefully.md`).
- **No policy values.** Every cadence, threshold, and budget the
  sweep honors is instance data, authored where the need lives
  (`../../../design-next.kb/030-requirements.kb/wake-conditions-are-noticed.md`).
  "Policy" is not a separate concept: whatever claims attention is a
  trigger instance -- per-instance condition parameters plus a
  directive body, usually judgment-shaped; the residue (emission
  budget values, channel wiring) is per-consumer delivery
  configuration, adapter-grade like hook bindings.
  `../use-cases.kb/` holds the motivating inventory.

> [!QUESTION] which junctures run the sweep?
> Lifecycle points (session start/end) are the obvious bindings and
> an engine verb the obvious on-demand form; whether doctor hosts
> it, shims invoke it, or both, settles when the first sweep is
> built. Ecosystem-side, the requirement demands only that named
> junctures exist and evaluation be complete
> (`../../../design-next.kb/030-requirements.kb/wake-conditions-are-noticed.md`).

> [!QUESTION] emission channels and nag semantics
> What a surfaced wake looks like — context line, report file,
> escalating insistence — is unratified, as are the per-cell
> contracts it actuates (`task-deferral.md`); both settle with the
> same first implementation.
