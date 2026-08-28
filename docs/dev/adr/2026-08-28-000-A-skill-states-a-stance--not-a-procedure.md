# A skill states a stance, not a procedure

**Date:** 2026-08-28
**Status:** Accepted

## Context

`meta-reasoning`'s `Skill(judge-work)` was rebuilt twice in one
sitting, and each rebuild found a different way for a skill to be
overfit to the session that produced it.

The first version was a memoir with checks embedded: a framing
paragraph about the sitting that derived it, and a mandated reading
order into that sitting's record. Loading it cost ~5,900 words — 940
of its own and 4,936 of prescribed reading — before any judgment
could start. Its stated reason for refusing to carry its own content
was that "a summary is cached state," which misapplies the rule it
was citing: that rule governs *current state*, and a check does not
rot. "Is the ranking key a filter?" stays askable forever.

The second version cut that to 700 words and opened with an
instruction: *"open the thing that computes its rank and read that."*
That instruction had produced the sitting's central finding, so it
looked like the distilled lesson. It presumes a computer of ranks
exists. It did in that repository. In most settings nothing computes
the rank — and an agent following the instruction finds nothing,
shrugs, and misses that *nothing computing it* is the finding.

The generalisation failure is not fixable by a better instruction.
Any procedure encodes the setting its author was standing in.

## Decision

A skill's body states the **stance** an agent must hold, not the
procedure it must run. Three parts carry it:

- a **standing** — what the agent is accountable for, and what it may
  not inherit that accountability from;
- what the agent must be **able to say** before acting, as a
  precondition rather than a checklist;
- a **precedence** for when those pull against each other.

An agent holding a stance regenerates the right procedure in settings
the author never saw, including the settings where the expected
artifact is missing and its absence is the answer.

Situational content is not thereby banned. It is what makes a check
runnable, and deleting it for portability's sake produces advice
nobody can execute. It is instead **collected under one named
heading** that a port rewrites rather than drops — in `judge-work`,
"How the checks cash out here", holding the field name, the command,
and what counts as scarce in that repository.

## Alternatives Considered

### Option A — mandate reading the derivation instead of restating it
- **Pros:** no risk of the skill's summary drifting from its source.
- **Cons:** charges every invoker the derivation's full price at
  invocation frequency, to avoid a drift that checks cannot suffer
  (`price-text-by-load-frequency.md`). Measured at 88% of the load
  budget.

### Option B — prescribe the procedure that worked
- **Pros:** concrete, immediately actionable, demonstrably effective
  in the founding case.
- **Cons:** silently assumes the founding setting. The owner's
  ruling: *"presuming such a thing exists is not valid. Instead,
  arrange things (role setting, priorities, success criteria) such
  that agent will naturally do this on its own."*

### Option C — strip situational content entirely, for portability
- **Pros:** one artifact, portable by construction.
- **Cons:** the checks stop being runnable. The owner's ruling:
  *"minimization should be read as 'as small as possible, but no
  smaller'. Some things are inherently situational and should not be
  (attempted to) optimize away. For those bits, best you can do is
  make them easy and efficient to find, choose."*

## Consequences

**Positive:**
- A skill survives transplant: the stance holds, and the named
  section is the diff.
- Absence becomes legible. A stance-holding agent treats a missing
  artifact as a result; a procedure-following one treats it as a
  dead end.

**Negative:**
- A stance is longer than the instruction it replaces —
  `judge-work` went 700 → 1029 words — and the cost is paid at
  invocation frequency. Justified only where the skill is loaded
  into varied settings.
- Stances are harder to test than procedures. Whether one produces
  the intended behaviour is only observable in a setting the author
  did not construct.

**Neutral:**
- The acceptance test used here — replay the founding session with
  the artifact in hand — found two defects, both at the trigger and
  the entry, none in the checks. It cannot validate generalisation:
  replaying a session against rules extracted from it is one route,
  not two.

## Related

- Depends on: `docs/dev/claims.kb/design.claims.kb/authorship.kb/stance-over-procedure.md`,
  `.../situational-bindings-are-named-not-removed.md`
- Related to: `2026-08-27-000-Skill-load-triggers-live-in-the-description--not-in-project-frontmatter.md`
  (the trigger defect found here amends its calibration problem),
  `2026-08-09-000-Skills-cite-no-instances--instances-cite-the-skill.md`
  (a project-local skill may cite its own registers; promoting one to
  the fleet turns those citations into instance references and they
  must move inside the skill directory or go)
- Narrative address: `meta-reasoning` session `7c314aa6`, commits
  `de2bcc1` through `74fe941`, and
  `meta-reasoning/docs/dev/devlog/2026-08-28-000-judge-work-rebuilt--the-method-kept--the-memoir-routed-to-its-address.md`
