---
label: PLACE
standing: user
authority: "@bukzor 2026-08-29: 'the standard placement for a repo (or a repo-subpath-ed project) is docs/dev/claims.kb/design -- rationale: it gives plenty of room for multiple claim-kbs under docs/dev scope'; and, on the child name, 'the second claims is redundant'"
why:
  - ../migration.md
---

# The Record Lives Under docs/dev

The normative default home is `docs/dev/claims.kb/design.md` beside
`docs/dev/claims.kb/design.kb/`. The `claims.kb/` container is what
gives a project room for the several ledgers it accumulates, and the
child takes a bare subject token because the container already
supplied the word "claims" -- `claims.kb/design.claims.kb/` repeats
it.

That third naming case is now in
`skill://llm-claims-kb/SKILL.md`'s Layout section, where the other two
already were.

A skill or subproject that keeps its own record roots the same path at
its own subpath, which is what this record does. Ledgers already at
`<skill>/claims.kb/` do not move: multiple ledgers per scope is the
reason the `docs/dev/claims.kb/` convention exists, so a scope holding
exactly one is not misplaced by it.
