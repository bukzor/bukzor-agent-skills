# Skill load triggers live in the description, not in project frontmatter

**Date:** 2026-08-27
**Status:** Accepted

## Context

The 2025-12-03 setup-depends ADR asked "when should an agent first load a
skill?" and answered: when the project declares a dependency. Every skill's
`setup:` stanza then told adopting projects to add `requires:`/`depends:` to
their `CLAUDE.md`.

The measured cost, on a read-only question against a claim ledger: two full
skill loads the session never used, and with the rest of the bootstrap,
roughly half the tool calls fell before the first line of the answer.

A fleet audit found 117 directive rows. 82 of them merely restated a trigger
the target skill already advertised — 53 correctly, 29 in a description that
was itself miscalibrated.

The root cause is structural. A directive is a **trigger** — a *(condition,
target)* pair — and project frontmatter carries only the target. A `CLAUDE.md`
loads for everyone entering the repo, whatever they came to do, so it
discharges no condition: the directive fires on arrival rather than on need.

## Decision

A skill's `description:` is the authoritative trigger surface.

- Descriptions are **intent-keyed** ("when creating a `.kb/` collection"), not
  location-keyed ("for `.kb/` directories"). Being in a directory is not a
  reason to load a skill; being about to change it is.
- The user-scope Required Reading protocol scans descriptions as triggers
  during planning, alongside `must-read.kb`.
- `setup:` stanzas no longer instruct projects to register the skill.
- A project directive survives only where its carrier was itself reached
  conditionally — a `must-read.kb/` entry, a `SKILL.md` — which discharges the
  condition already.

## Alternatives Considered

### Option A — move triggers into `~/.claude/must-read.kb/`
- **Pros:** bank scanning is already protocol-mandated; collapses two surfaces
  to one.
- **Cons:** the bank is operator-local, so a skill installed by anyone else
  would carry no triggers at all. Filed as
  `design-next.kb/070-future-work.kb/federated-trigger-banks.md`, to revive if
  banks ever federate.

### Option B — keep setup-depends, add a lint
- **Pros:** no rewrite; stops regeneration.
- **Cons:** retains a redundant surface and its per-project maintenance, with
  the condition still missing.

## Consequences

**Positive:**
- Triggers travel with the skill they belong to; no per-project registration.
- 82 redundant directives removed fleet-wide.
- Reading a collection no longer loads the skill that governs writing it.

**Negative:**
- Descriptions are not mechanically enforced; they rest on the planning-time
  scan. That is the floor semantics `Skill(llm-triggers)` defines, and hooks
  can strengthen it later without re-authoring.

**Neutral:**
- `requires:`/`depends:` remain valid in conditionally-reached carriers.
  `Skill(llm-triggers)`'s v1 is planned to supplant both with a single
  `triggers:` field.

## Related

- Supersedes: `2025-12-03-000-setup-depends-pattern-for-skill-self-registration.md`
- Related to: `llm-triggers/design.kb/use-cases.kb/arrival-fired-directives.md`,
  `llm-triggers/design.kb/use-cases.kb/payload-gated-conditions.md`
