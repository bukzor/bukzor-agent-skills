# After Editing a claims.kb

> [!DRAFT] agent-authored 2026-11-25, vetoable

You just added, changed, renamed, or removed claim files. Before the next
edit builds on these, pass over what you touched:

- a file added, renamed, or removed, or a `why:` changed -- run
  `bin/llm-claims-kb-graph` on the ledger and read it: [graph-health].
- a claim's body or `authority:` quotes a ruling -- [ruling-fidelity].
- an `ontology:` written, or a claim moved between theories --
  [confinement], against `llm-claims-kb-ownership --trespass` run from the
  project root.

The full sweep waits for the commit:
`../before/committing-a-batch-of-claims.md`.

[graph-health]: ../../quality-passes.kb/graph-health.md
[ruling-fidelity]: ../../quality-passes.kb/ruling-fidelity.md
[confinement]: ../../quality-passes.kb/confinement.md
