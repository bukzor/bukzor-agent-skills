# Skills cite no instances; instances cite the skill

**Date:** 2026-08-09
**Status:** Accepted

## Context

The `formalize`/`deformalize` skills initially cited their worked
instances (`strata.ledger.kb/`, `design-incubators/engine_tower/`) as
exemplars. Two problems:

1. **Contamination.** A skill is loaded by whoever invokes it. When an
   instance is the answer to an exercise -- the strata blind study,
   any independent re-derivation -- a skill that names it hands the
   answer to exactly the agent who must not see it.
2. **Coupling.** The instance list is unbounded and churns; the skill
   would need editing every time an instance moves, dies, or a better
   one appears. `ls`/`grep` already find instances via their
   `depends:`/provenance references.

A first attempt kept the references and added the skills to the blind
study's do-not-open list -- managing the symptom per-instance instead
of removing the cause. A second attempt stated the no-instances rule
inside each SKILL.md -- but that addresses skill *writers*, while
SKILL.md is read by *invokers*; author-facing rules there are noise on
every invocation.

## Decision

The reference arrow points one way: **instances cite the skill**
(`depends:` frontmatter, provenance notes), **skills cite no
instances**. Author-facing conventions like this one live here in
`docs/dev/adr/`, not in SKILL.md bodies.

Sanctioned exception: material *inside* the skill's own directory
(schemas, skeletons, a `design.ledger.kb/` of the skill's own design)
is part of the skill, not an instance, and may be referenced freely.

## Alternatives Considered

### Keep exemplar references; enumerate them in each blind's do-not-open list
- **Pros:** exemplars aid comprehension at invocation time
- **Cons:** every new exercise must re-discover which skills leak; the
  coupling and churn problems remain

### State the rule inside each SKILL.md
- **Pros:** visible at the point of temptation
- **Cons:** wrong audience -- invokers pay the tokens, writers rarely
  reread the body they are editing

## Consequences

**Positive:** skills are safe to hand to any agent, including one
inside a blind; instance churn never touches skill text.

**Negative:** an invoking agent wanting a worked example must find one
itself (`grep -rl 'Skill(formalize)'` or a provenance scan) -- one
step less convenient than a curated pointer.

**Neutral:** existing `llm-*` skills already largely conform; the
`llm-claim-ledger-kb` -> `../llm-claim-ledger/design.ledger.kb/`
pointer is within-family and stands under the exception.

## Related

- Related to:
  `llm-collab/docs/dev/adr/2025-12-02-001-cross-skill-referencing-via-load-pattern.md`,
  `docs/dev/strata.replication.md` (the blind whose protection forced
  the issue)
