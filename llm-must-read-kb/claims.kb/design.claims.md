---
label: MUST_READ_DESIGN
standing: agent
why:
  - ../../llm-kb/claims.kb/design.claims.md
ontology:
  - trigger bank
  - directive
  - host context
non-claim-tokens:
  - ANY
  - CLAUDE
  - SKILL
stale-when: a consumer delivers a directive by a route that never reads a filename -- then the listing is no longer the index, and every claim below that treats the listing as the semantics is re-derived
last-updated: 2026-09-22
---

# must-read.kb's design, as a ledger

What a trigger bank commits to beyond `Skill(llm-kb)`: the shape of a
bank, what its paths mean, when a directive is installed and when it
fires, who does the installing, and which occasions earn a set of their
own. One claim per file, label and standing in frontmatter
(`Skill(llm-claims-kb)`). Argue with a claim by editing its file.

Division of labor: `../SKILL.md` states the settled pattern for a
consumer; this ledger holds what is committed-but-contestable, what is
open, and what was dissolved -- so the next agent does not re-conjecture
it. A commitment that reached `SKILL.md` and nobody disputes needs no
claim here.

## Layer 0

A trigger bank is a tree of trigger sets indexed by occasions; a set is
installed when its occasion begins, every member's occasion entails its
set's, and "installed before fired" then rests on exactly one premise --
noticing the occasion begin -- dischargeable per occasion by a puller.
Three laws carry it: `firing.kb/a-member-entails-its-set.md`,
`firing.kb/a-set-is-installed-when-its-occasion-begins.md`,
`firing.kb/a-trigger-cannot-gate-what-fires-it.md`. The theorem is
`firing.kb/every-firing-trigger-is-installed.md`.

## Theories, in prior order

- `grammar` -- what a well-formed bank looks like on disk; imports
  llm-kb's plain-directory rule.
- `occasions` -- the preorder the bank is indexed by.
- `firing` -- what paths mean: install, fire, and the laws between.
- `delivery` -- how a listing reaches an agent, and what wording and
  compaction do to it.
- `pullers` -- who notices an occasion begin, and the gradient from
  judgment to mechanism.
- `policy` -- which occasions earn a set, and where things live.
- `instance` -- the proper nouns: today's bank, thrown away first.

Decided and no longer askable (the tombstones sit beside the claims
that dissolved them, `grep -rl 'verdict:'`): occasion-first path order;
`while` as the word; one listing command; the top set is the bank; stubs
shown.

Provenance: session `ba648ef5` (2026-09-18/19, formalized 09-19) and
three sibling sessions' cross-reads, recorded in
`~/.claude/sessions.kb/penguin.kb/must-read-sharding.md`.

## Scans

```bash
grep -rH '^standing:' llm-must-read-kb/claims.kb/design.claims.kb/
grep -rl 'verdict:' llm-must-read-kb/claims.kb/design.claims.kb/
llm-claims-kb/bin/llm-claims-kb-graph llm-must-read-kb/claims.kb/design.claims.kb
```
