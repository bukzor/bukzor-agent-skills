# Procedure: reconcile-case-study

Take a raw case-study and produce distilled entries (failure-modes,
procedures, principles, concepts, glossary).

## Goal

Align provisional aliases to canonical names; ensure every named item
has a canonical entry with mitigations and cross-refs. Set
`status: reconciled` when done.

## When to use

- A case-study has no `status:` field (= raw) or a partial-state
  status that isn't `reconciled`.

## Inputs

- The raw case-study.
- Read/write access to `../failure-modes.kb/`, `../procedures.kb/`,
  `../principles.kb/`, `../concepts.kb/`, `../glossary.kb/`.

## Steps

1. **Alias reconciliation.** For each entry in the case-study's
   `failure-modes:` frontmatter:
   - **Matching entry** in `../failure-modes.kb/`: align case-study
     alias to the canonical name.
   - **Partial match**: revise either side. Prefer revising the
     canonical entry to encompass the new instance.
   - **No entry**: create one. Populate from the case-study --
     description, recognition prompt, corrective signals (verbatim
     quotes from the case-study), worked example, recovery path.

2. **Mitigation linking.** For each created or revised failure-mode
   entry:

   ```yaml
   ---
   aliases: [<primary-alias>]
   mitigated-by: [<path>]
   eliminated-by: []
   ---
   ```

   If a needed mitigation doesn't exist, create it. Procedure for
   multi-step methods; principle for aphorisms. Use
   `../../../SKILL.kb/procedures.kb/stub-missing-entry.md` for
   cascade-bounded stubbing.

3. **Concept and glossary stubs.** Any novel term mentioned without
   a definition: stub it per
   `../../../SKILL.kb/procedures.kb/stub-missing-entry.md`.

4. **Distilled procedures and principles.** If the case-study embeds
   a method or aphorism worth promoting, extract it to
   `../procedures.kb/` or `../principles.kb/`.

5. **Set status.** When all named items have canonical entries with
   mitigations and cross-refs:

   ```yaml
   ---
   status: reconciled
   ---
   ```

   If stopping mid-way, leave `status:` absent (= raw) and note
   blockers in the case-study itself. If this stopping point feels
   like a recurring shape, name it -- add a partial-state value to
   `../case-studies.jsonschema.yaml`.

## After completing

Run `../../../SKILL.kb/must-read/after/distilling-from-a-raw-source.md`
audits.

## What this prevents

- Failure modes named inconsistently across case-studies.
- Distilled content drifting from raw case-study sources.
- Concepts and terms used without definition.

## Related

- `post-mortem.md` -- the capture procedure that feeds this one.
- `../../../SKILL.kb/procedures.kb/stub-missing-entry.md` -- cascade
  bounding.
