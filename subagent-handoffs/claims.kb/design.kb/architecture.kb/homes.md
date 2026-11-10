---
label: HOMES
standing: user
why:
  - ../requirements.kb/one-copy.md
  - homes.kb/one-home.md
authority:
  address: "97605ccb"
  words: "agreed: update the subagent-handoffs skill with this proposal"
  about: one home per fact
---

# Where each fact lives

Every fact has one home, and every other file links to it. A handoff
file holds only what has no other home: what its unit was asked, how
far it got, what it chose, and what it still doubts.

The homes:

- design: the project's design docs, or the plan where there are none;
- an interface: the artifact that defines it -- code, schema, file
  format;
- a finding: the doc it belongs in, written by the unit that found it;
- a rule every agent follows: the handoff collection's `CLAUDE.md`;
- a change, line by line: git.

Where a finding has no permanent home, the report is its home, and
nothing copies it. The answers weighed are in `homes.kb/`.
