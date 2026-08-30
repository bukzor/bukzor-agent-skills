# llm-design-kb Skill

See `SKILL.md` for the pattern this skill defines. This file is
maintenance guidance for agents working **on** the skill (not
consumers writing a project's own design record).

## Collections

- `skeleton/` — copied wholesale by consumers to bootstrap a record.
  Editing it changes what every future record starts as, so a change
  here is a design decision: file the claim in `docs/dev/claims.kb/`
  first.
- `skill.kb/must-read.kb/when/` — the trigger bank. Each filename
  names its own occasion; the file is the payload, never a redirect.
- `skill.kb/principles.kb/` — design-authorship lenses for consumers.
  Adding one means adding its occasion to the trigger that indexes them.
- `docs/dev/claims.kb/` — this skill's own design record, kept in the
  form it recommends.
- `jsonschema/` — retained for legacy numbered towers only
  (`layer-entry`, `technical-policy`). New records bind
  `skill://llm-claims-kb/jsonschema/`; see
  `docs/dev/claims.kb/design.kb/migration.kb/`.

## Dogfooding

The skill's own record is the first test of a change to the skill: if
a new rule cannot be stated as a claim in `docs/dev/claims.kb/`, it is
not ready to ship to consumers.
