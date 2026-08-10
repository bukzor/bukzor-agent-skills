# Adopt the .claims.kb suffix; rename the ledger skills

**Date:** 2026-08-10
**Status:** Accepted

## Context

The file form of a claim ledger predates `Skill(llm-kb)`'s `.kb`
convention (ADR `2025-12-11-001`) and was never brought under it:
`llm-claim-ledger`/`llm-claim-ledger-kb` name the skill pair, and
every collection under them -- `strata.ledger.kb/`, `design.ledger.kb/`
in three places -- carries a bare `.ledger.kb` suffix that says
nothing about the containing skill.

Meanwhile `Skill(llm-discourse-graph)` claimed the word "claims" for
its own bare `claims.kb/` node-type collection. `Skill(llm-claim-ledger-kb)`'s
"What this is not" section leaned on "ledger" vs. "claims" as the
distinguishing word between the two instruments -- a distinction that
was already thin (both keep claims in files) and that any future
rename toward `.kb`-family consistency would erase outright.

## Decision

Normalize every claim-ledger artifact onto a `.claims.kb` suffix:

- `llm-claim-ledger` -> `llm-claims`, `llm-claim-ledger-kb` ->
  `llm-claims-kb`. The skill pair renames together -- the X/X-kb
  pairing (the notation and its file form) forces both sides at once,
  the same as `llm-kb`'s own name forces `.kb`.
- Every `*.ledger.kb/`, `*.ledger.md`, `*.ledger.jsonschema.yaml` in
  this repo becomes `*.claims.kb/`, `*.claims.md`,
  `*.claims.jsonschema.yaml`: `docs/dev/strata.ledger.kb/`,
  `docs/dev/design.ledger.kb/`, `llm-claim-ledger/design.ledger.kb/`.
- `llm-claims-kb/bin/llm.ledger-graph` and `llm.ledger-dot` become
  `llm.claims-graph` and `llm.claims-dot`.

The symmetry sought: `llm-kb : .kb :: llm-claims-kb : .claims.kb`.

Accepted cost: the ledger form now shares the bare word "claims.kb"
with `llm-discourse-graph`'s node-type collection. Mitigated two ways
-- the ledger form never appears bare, always carrying a stem prefix
(`strata.claims.kb`, `design.claims.kb`, never plain `claims.kb`), and
`llm-claims-kb/SKILL.md`'s "What this is not" now disambiguates by
shape instead of by word: sibling node-type collections
(`questions.kb/`, `sources.kb/`, ...) mean the discourse graph;
frontmatter `standing:` and theory headers mean a ledger.

The concept name "claim ledger" is untouched in prose everywhere --
this rename moves artifact names (skills, directories, files, tools)
only, never the vocabulary a claim ledger is written and read in.

## Alternatives Considered

### Keep `.ledger.kb`, rename only the skill pair
- **Pros:** smaller diff, no collision with `llm-discourse-graph`
- **Cons:** leaves the skill's own collections off the `.kb` convention
  its sibling skill established two months earlier; the inconsistency
  this ADR exists to close would just move down one level

### Invent a third word (neither "ledger" nor "claims")
- **Pros:** no collision, ever
- **Cons:** a new word is a new thing to learn for no structural gain;
  "claims" is already the correct word for what the files hold, and
  the collision is cheap to resolve by shape

## Consequences

**Positive:** one suffix convention (`.kb` and its typed variants)
across every skill-managed directory in the repo; the ledger skill
pair's own name stops being the odd one out.

**Negative:** the collision with `llm-discourse-graph`'s `claims.kb/`
is now real, not hypothetical -- an agent meeting a bare `claims.kb/`
must read its shape, not just its name, to know which instrument it
is.

**Neutral:** historical records (`docs/dev/devlog/`, `docs/dev/adr/`)
keep the old names as provenance; only live files were swept. Sister
repos (`prototype.personal-reasoning-management`'s `design.ledger.kb/`,
`corpus/ledger.kb/`) still carry the old suffix -- a separate pass, not
done here.

## Related

- `2025-12-11-001--unify-directory-naming-to-kb-suffix.md` -- the `.kb`
  convention this rename brings the ledger skills under
- `2026-08-09-000-Skills-cite-no-instances--instances-cite-the-skill.md`
  -- names the pre-rename paths as history
- Commits `03f6254` (renames + reference sweep), `879de9a`
  (`llm-claims-kb/SKILL.md` rewrite, `SKILL.kb/self-audit.kb/`), `00721a9`
  (completed the rename pair's old-path deletions)
