---
label: GRAMMAR
standing: agent
why:
  - ../design.claims.md
  - ../../../llm-kb/claims.kb/design.claims.kb/a-plain-directory-is-a-key-prefix.md
ontology:
  - set
  - juncture
  - point juncture
  - stub
  - namespace directory
stale-when: a bank is consumed by something other than a listing of its paths -- then the path is no longer the trigger phrase and the reserved names lose their force
---

# Grammar -- what a well-formed bank looks like on disk

Coins: a **set** is a directory of shape `{before,after,when,while}/`,
each optional; a **juncture** is one of those four reserved names; the
first three are **point junctures** and hold trigger files; a **stub**
is a `while/X/` line in a listing whose contents are not yet listed; a
**namespace directory** is any other directory, a key prefix per
llm-kb's rule and nothing more.

The path is the trigger phrase: `while/making-code-changes/before/
writing-python-code.md` reads "while making code changes, before
writing python code".
