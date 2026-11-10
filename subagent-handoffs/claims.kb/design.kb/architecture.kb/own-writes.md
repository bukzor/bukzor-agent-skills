---
label: OWN_WRITES
standing: agent
why:
  - commits.md
  - ../requirements.kb/disk-record.md
---

# Each party commits its own writes

The coordinator commits what it writes -- each brief before launch,
each amendment before the "reread" message -- and each agent commits
its unit. So the history shows what an agent was asked, as asked,
beside what it did, and no party's commit carries another's edits.

This extends COMMITS (`commits.md`) to the coordinator's side: without it, a brief amended in place would land in the agent's
commit, under the agent's authorship.
