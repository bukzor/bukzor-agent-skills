---
why:
  - action-triggers-enforced-deterministically
  - judgment-triggers-remain-scannable
---

# Genre: Trigger

Conditional directives, partitioned by whether the condition is
machine-detectable:

- **Action-shaped** ("before git commit", "before editing schemas"):
  authored as trigger files, *compiled* into whichever adapter
  implements `delivery-contract.md`'s enforcement verbs — hooks,
  under the Claude Code adapter. The file body becomes the injected
  context (or the deny payload, for hard gates). The file remains the
  source of truth; the adapter is its enforcement. `kb doctor`
  verifies the compilation is current.
- **Judgment-shaped** ("when evaluating a contested position", "when
  wanting to comply but cannot"): stay a filename-indexed
  `must-read` bank, scanned during planning — v1's genuinely novel
  invention, retained at exactly the scope hooks can't express.

This dissolves v1's central tension: the same authoring format serves
both, but enforcement strength follows detectability instead of
hoping prose emphasis covers everything.
