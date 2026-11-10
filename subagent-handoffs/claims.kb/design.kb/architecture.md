---
label: ARCHITECTURE
standing: user
why:
  - requirements.md
ontology:
  - home
  - open handoff file
  - done handoff file
authority:
  address: "97605ccb"
  words: "agreed: update the subagent-handoffs skill with this proposal"
  about: one home per fact, tense, per-unit commits, amendment by dependents
---

# Architecture

Every fact lives in one home, and a handoff file's status sets its
tense: open files state current truth, done files are frozen records.
Each party commits its own writes.

- **home**: the one place a fact is written; every other file links to
  it.
- **open handoff file**: a unit not yet handed back. Its file states
  the current truth.
- **done handoff file**: a unit handed back. Its file is a frozen
  record.

Each claim in `architecture.kb/` is one property of that shape; the
options it declined are filed beside the claims that beat them.

> [!@bukzor] 97605ccb
>
> in the large, it sounds like your proposal amounts to "DRY, using
> /llm-kb and friends". [...] if so, agreed
