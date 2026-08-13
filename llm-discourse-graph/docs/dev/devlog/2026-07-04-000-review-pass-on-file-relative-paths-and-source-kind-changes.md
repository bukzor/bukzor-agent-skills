# Devlog: 2026-07-04 — Review pass on file-relative-paths and source-kind changes

## Focus

Review and refine the 2026-07-03 dogfooding changes (ADRs
`2026-07-03-000-file-relative-paths` and
`2026-07-03-001-user-assistant-source-kind`, plus schema/SKILL.md edits)
before considering them settled.

## Decisions

### Deductions gain a `sources` array

The 2026-07-03 diff was internally inconsistent: ADR-001 and the sources
schema description both said sources are "cited from many
claims/deductions", and the ADR's motivating need ("who asserted this")
explicitly included deductions -- but `deductions.jsonschema.yaml` had
no `sources` field, so a deduction couldn't cite anything.

**Rationale:** Deductions carry `status`/`likelihood` like claims and
are exactly where sycophancy shows up ("assistant asserted this
entailment"), so attribution parity is the coherent resolution.
**Alternatives considered:** Narrow the ADR/schema prose to claims-only.
Rejected: it would leave the ADR's own stated need half-met.

### Superseded prose is fixed everywhere living, left alone in history

Lexical-scoping language survived the supersession in project CLAUDE.md,
SKILL.md's frontmatter-path example, and all three
`docs/dev/design/unified-claim-scheme*` docs (whose own CLAUDE.md
defines contradiction as staleness). All now point at the ADR instead of
duplicating mechanism -- the duplication is what went stale. Devlogs
keep their historical lexical-scoping mentions.

## Conventions Established

- ADR cross-references use explicit filenames, not bare ordinals
  ("ADR-000") -- ordinals became ambiguous once a second date-series
  (2026-07-03-000/-001) existed.
- ADR filenames must match their titles: renamed
  `2026-03-02-000-six-collection-types.md` to `...-five-...` (title and
  content said five; nothing referenced the filename).

## Open Questions

-

## References

- `docs/dev/adr/2026-07-03-000-file-relative-paths.md`
- `docs/dev/adr/2026-07-03-001-user-assistant-source-kind.md`
- `~/.claude/sessions.kb/physical-musings-goals-and-structure.md` -- the
  dogfooding session that produced the reviewed changes
