---
managed-by: Skill(llm-subtask)
status: not-started
cost-benefit-sweh:
  timebox:
    "@value": 3.0
    rationale: |
      The registration mechanism is small; the cost is deciding the
      check protocol once, because every later check inherits it.
      Past three hours the thing to do is ship one plug-in and let the
      second check argue with the first.
    confidence: tentative
  benefit-2w:
    "@value": 4.0
    rationale: |
      Every kb that grows a check today writes its own runner and its
      own summary line, and each one is a place a check can go quiet
      unnoticed. Two repos have already built one by hand.
    confidence: tentative
---

# Let specialized checks plug in under `llm.kb-validate`

**Context:** `llm.kb-validate` (`llmd.frontmatter_validate:main`) checks
frontmatter against JSON Schema and nothing else. Every other check
lives beside it as a separate command a caller has to know about:
`bin/llm.kb-validate-links` (not even on `$PATH`),
`llm-claims-kb-graph`, `llm-claims-kb-mentions`,
`llm-claims-kb-ownership`, and per-repo checkers like
`meta-reasoning/lib/archeology/verify-quotes.py`.

## Problem Statement

There is no address for "check this kb". There is an address for each
check, and a caller who does not know the list gets a green tick from
the subset they happened to run.

That is not hypothetical. `meta-reasoning` wrote `repo-health.sh` on
2026-08-28 purely to hold five such commands in one place, and writing
it turned up two checks that had been passing by looking away —
including `llm.kb-validate-links`, whose findings nobody had missed
because nobody was running it. A per-repo shell script is the workaround
for the missing mechanism, and it does not travel.

`llm-claims-kb`'s checkers are the strongest case: a claims ledger *is*
a `.kb/`, its integrity checks are `.kb/` checks, and there is no reason
`llm.kb-validate` should not run them when it meets one.

## Proposed Solution

Python entry points, which both packages already have the machinery for
(`[project.scripts]` in `llm-kb` and `llm-claims-kb`):

```toml
[project.entry-points."llm.kb.checks"]
links = "llmd.link_validate:check"
claims-graph = "llm_claims_kb.graph:check"
```

`llm.kb-validate` discovers the group, runs every registered check over
the paths it was given, and aggregates. A check is a callable taking
paths and returning findings; the runner owns the summary line and the
exit code.

Two properties are not optional, both learned the hard way:

- **Every check reports what it examined, not just its verdict.** A
  check that can pass by finding nothing is not a check.
- **A check that cannot apply says so.** Silently skipping the files it
  does not understand is precisely how the whitelist bug in
  `llm.kb-validate-links` survived — it reported `✅ N files` while
  reading a fraction of what it named.

## Open Questions

- **Where does the protocol live?** `llm-kb` is the natural host — it
  owns the `.kb/` concept and the `llm.kb-validate` name. Registering
  costs no dependency: `llm-claims-kb` declares `pyyaml` and nothing
  else, and an entry point is package metadata, so it can advertise a
  check without importing `llm-kb` at all — only the host imports the
  callables it finds. What is left to settle is whether the protocol
  stays duck-typed, or gets written down as a shared type, which is
  the only version that costs anyone a dependency.
- **Opt-in or automatic?** Running every installed check on every
  invocation is the point, but a slow check (graph rendering) should
  not be in the default path. A `--check=` selector plus a `default:
  false` flag in registration is the obvious shape.
- **What about non-Python checks?** `verify-quotes.py` is repo-local
  and will stay that way; a repo-local `pyproject.toml` entry point is
  a fine answer, but confirm the discovery works from a workspace
  member and not only from an installed distribution.

## Success Criteria

- [ ] `llm.kb-validate <path>` runs schema, link, and claims-integrity
      checks in one invocation, and prints one line per check naming
      what it examined.
- [ ] `meta-reasoning/repo-health.sh` shrinks to the checks that are
      genuinely repo-local, with the rest arriving through the plug-in
      group.
- [ ] A newly installed skill's checks run without any caller
      learning its command name.
