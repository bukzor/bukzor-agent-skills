---
why:
  - ../030-requirements.kb/procedures-are-tools.md
  - ../030-requirements.kb/degrade-gracefully.md
  - ../030-requirements.kb/classes-detach-cleanly.md
status: proposal
---

# Class Package

A class is an application of the spec (`kb-spec.md`) to one domain —
prior art: the metadata-standards notion of an *application profile*,
a domain-specific customization of a base schema that extends it
without forking it (`kb-spec.md`'s closing line: "a meta-schema
validates class schemas so classes extend the spec without forking
it"). Concretely, a class package bundles:

- **schema** — the class's `jsonschema.yaml`, validating its entries'
  frontmatter.
- **templates** — what `kb new <class>` fills in.
- **conventions page** — the judgment content an agent needs that the
  engine can't make mechanical: what's homogeneous, what deserves a
  schema, when to elaborate vs. roll up, domain-specific placement
  calls. Kept near the size discipline that made
  `claude-realignment` work as a v1 proof: tight, single-job,
  recognition-only content.
- **triggers** — this domain's instances of the trigger class,
  delivered per whatever the active adapter needs
  (`delivery-boundary.md`).
- **checks** — this domain's `kb doctor` validators.

**Composition and citation, never subclassing.** A class package may
cite another class's entries (a task references the design entry it
motivated). Composition — one class package built from another
class's primitives — is allowed in principle but has no confirmed
example yet: the shape that looked like one, the dated-record format
several classes reuse, turns out to be a **spec** primitive each
class gets independently via its own required class→spec edge
(`dated-records-are-primitive.md`), not something borrowed from a
sibling class. Flagging for the operator: composition may be a
thinner allowance than citation, or the right example just hasn't
surfaced yet. Either way, no class package ever inherits or extends
another class's schema — each class extends only the spec, never a
sibling class. That's the mechanism that keeps
`classes-detach-cleanly.md` true: removing one class package can
never strand another that quietly subclassed it.

> [!QUESTION] is the conventions page itself the delivered teaching?
> Whether a class's conventions page *is* the delivered teaching
> artifact (e.g. a Claude Code SKILL.md body, verbatim) or compiles
> to one through a separate step. Treating them as identical was
> proposed unilaterally in an earlier session; settles on testing
> against a second adapter.

> [!QUESTION] does class-local code have plain consumer status?
> Whether class-local code — templates aside, e.g. a check script —
> is a plain consumer: stable formats in, no engine hooks.
> Generalizes the task-archeology stance (T2 brief, decision 3).
> This entry asserts it neither way; settles on operator
> ratification whenever the question next matters.

> [!QUESTION] does teaching consolidate cross-class, or stay per-package?
> The prior thin-skills content (now folded into this entry) asserted
> exactly three teaching skills (kb / epistemic / attention) cutting
> across class boundaries, rather than one conventions page per class
> package (the mapping this entry describes above). That enumeration
> was agent-proposed and untested — the operator didn't recognize
> "attention skill" from a plain read of the committed baseline.
> Settles at build time; defer instance-naming rather than deciding
> here.
