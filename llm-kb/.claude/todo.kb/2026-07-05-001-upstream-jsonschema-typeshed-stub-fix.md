---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-02-09-000-schema-reuse-with-ref.md
cost-benefit-sweh:
  timebox:
    "@value": 1.0
    rationale: |
      Small, scoped PR against an existing stub file (or a jsonschema
      py.typed rollout, whichever the upstream maintainers prefer) --
      not a design problem, just needs upstream's contribution process.
    confidence: unsure
  benefit-2w:
    "@value": 0.1
    rationale: |
      Zero benefit to us directly -- we've already worked around this
      locally with `typings/jsonschema/` (see the 2026-07-05 devlog).
      Benefit accrues to the wider community once merged; low urgency.
    confidence: unsure
  cost-of-delay-2w:
    "@value": 0.0
    rationale: |
      No cost of delay -- our local workaround is permanent and doesn't
      depend on upstream merging anything. This is a courtesy contribution,
      not a blocker removal.
    confidence: confident
---

# Upstream PR: fix the flawed jsonschema typeshed stub

**Priority:** Low
**Complexity:** Small
**Context:** Surfaced while making `llm-kb/lib/python/llmd/frontmatter_validate.py`
pyright-clean (2026-07-05 devlog:
`docs/dev/devlog/2026-07-05-001-pyright-clean-frontmatter-validate.md`).

## Problem Statement

`jsonschema` (the installed package, 4.26.0) ships no `py.typed` marker.
`basedpyright`/`pyright` fall back to a *bundled* third-party stub for it
(typeshed's `jsonschema` stub package) rather than reading the real
installed source -- and that bundled stub doesn't match the real 4.26 API:

- References a `_JsonParameter` type on `Validator.iter_errors`'s
  `instance` parameter that doesn't exist anywhere in the real installed
  package, and is stricter than the real API (real `iter_errors` takes
  `instance: Any`, no such restriction).
- `TypeChecker.redefine_many`, `Draft202012Validator.TYPE_CHECKER`, and
  `jsonschema.validators.extend` all resolve to `Any`/partially-`Unknown`
  under the bundled stub even though `jsonschema`'s real source has real
  (if incomplete) annotations for most of this surface -- `extend()`
  itself is the one genuinely unannotated function in the real source.

We worked around this locally with a small project-level
`typings/jsonschema/` stub package (repo root) that takes precedence over
the bundled one -- see `_jsonschema_adapter.py` and the referenced devlog
for the full story. That workaround is sufficient and permanent for this
repo; this todo is about closing the gap upstream so other projects don't
hit the same thing.

## Proposed Solution

1. Confirm which typeshed/pyright bundles the stale `jsonschema` stub
   (likely typeshed's `stubs/jsonschema/`) and whether it's still
   maintained there, or whether `jsonschema` upstream has since added
   (or should add) its own `py.typed` marker -- the real source is
   *mostly* annotated already (`create()`, `TypeChecker.redefine_many`,
   `protocols.Validator` are fully typed; `extend()` is the one gap).
2. If targeting typeshed: PR removing/updating the stale
   `_JsonParameter`-based `iter_errors` signature to match the real API,
   and fixing whatever caused `TYPE_CHECKER`/`redefine_many` to resolve
   as `Any` under the bundled stub despite real annotations existing.
3. If targeting `jsonschema` upstream directly: PR adding type annotations
   to `jsonschema.validators.extend` (the one real gap) and a `py.typed`
   marker, which would make the whole typeshed stub package obsolete for
   this library and let real source annotations win instead.
4. Reference our local `typings/jsonschema/*.pyi` files as a working
   draft of what accurate stubs look like for the surface we exercise --
   not comprehensive, but a correctness baseline for review.

## Open Questions

- Typeshed PR vs. upstream `py.typed` PR -- which is more likely to be
  accepted? Upstream `py.typed` is the better long-term fix but a bigger
  ask (commits the library to a typing contract); typeshed stub fix is
  smaller/faster but leaves the underlying staleness-prone bundled-stub
  pattern in place for the next drift.
- Does jsonschema upstream already have an open issue/discussion about
  `py.typed` adoption? Check before duplicating effort.

## Success Criteria

- [ ] Confirmed root cause location (typeshed bundled stub vs. jsonschema
      upstream) with a minimal reproduction independent of this repo.
- [ ] PR opened (typeshed and/or jsonschema, per the above).
- [ ] PR references this repo's `typings/jsonschema/` stubs as a
      correctness reference, not copy-pasted verbatim (they're scoped to
      our usage, not comprehensive).
