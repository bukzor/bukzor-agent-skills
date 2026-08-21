# Decision (2026-08-21): a skill is the addressing unit -- one per artifact type

Cluster 6 asked where `~/.claude/sessions.jsonschema.yaml` should live. It
is a full canonical sitting outside any skill, so nothing can reach it
except a file-relative `$ref` from inside `~/.claude`; every consumer
elsewhere is stuck copying it.

First answer, wrong: put it in `llm-subtask/jsonschema/`, on the grounds
that a skill needs "agent behavior" and sessions had only documentation.

The user rejected the premise, correctly. In this architecture agent
behavior *is* documentation plus a load trigger -- there is no other
mechanism -- so "documentation, not behavior" reduces to "no trigger,"
which is false: `sessions.kb/` is exactly as good a trigger as
`*.claims.kb/`. Two further points settle it:

- The house pattern is already fine-grained. `llm-claims` /
  `llm-claims-kb` split notation from files; `llm-kb` /
  `llm-must-read-kb` split general from must-read. Merging would have cut
  against a convention with two precedents.
- The supporting argument pointed the other way. `sessions.kb` already
  `$ref`s `cost-benefit-sweh` across to llm-subtask (the 2026-08-13
  ruling), which proves sharing a definition never required merging the
  skills. It was evidence for separation read as evidence for merger.

llm-subtask's own `todo.jsonschema.yaml` already notes the strain of
being "generic task vocabulary for a skill named *subtask*". A session is
not a subtask -- it is a run with a uuid, timestamps, and a transcript.
Merging deepens a mismatch already recorded as a smell.

**The rule, stated positively:** `skill://` is the only cross-tree
addressing scheme, so a skill is the *addressing unit*. Hosting a
canonical is by itself sufficient reason for a skill to exist, and the
grain should follow artifact type. A skill that accumulates unrelated
canonicals for want of a better home is the failure mode to avoid.

Applied: new `llm-sessions` skill (SKILL.md + `jsonschema/`), symlinked
into `~/.claude/skills/`. `~/.claude/sessions.jsonschema.yaml` is a
one-line stub onto it; `sessions.kb/penguin.jsonschema.yaml` needed no
edit, since its `../sessions.jsonschema.yaml` now resolves through that
stub. The cross-skill `cost-benefit-sweh` ref went back to `skill://`
form, no longer being a sibling. Verified: `sessions.kb` 99 files, 0
errors; `llm-subtask` 4 files, 0 errors.
