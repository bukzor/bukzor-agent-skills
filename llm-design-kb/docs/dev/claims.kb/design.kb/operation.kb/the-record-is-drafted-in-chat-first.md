---
label: BEATS
standing: agent
why:
  - ../operation.md
---

# The Record Is Drafted in Chat First

The design is rendered as a `Skill(llm-claims)` ledger in the
conversation before any file is written, reviewed rung by rung, and
only then persisted via `Skill(llm-claims-kb)`.

Reviewing per rung rather than per record is the incumbent's own rule
-- "pause after each layer to provide an opportunity for review and/or
correction" -- kept verbatim, because its warrant survives the reform
intact: a mission the user would have redirected is a record built on
sand, and the cost of finding out early is one message.

Review is a **veto point, not a gate**: silence persists every claim
at its honest sigil, an agent's inference landing at `agent` standing
where it stays vetoable forever. The alternative to persisting
unreviewed claims is not careful claims; it is evaporation, which
nobody gets to veto.

The maintenance passes are this skill's, not its basis's: the
descriptive-claim ground-truth check, the standing-on-entry rule, the
arrow trace, and the confinement grep are all about *design* records.
`Skill(llm-claims-kb)` keeps only the generic ledger self-audit.
