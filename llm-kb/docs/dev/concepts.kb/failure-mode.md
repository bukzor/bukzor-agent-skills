# Concept: failure-mode

A recurring way agent work goes wrong, named with a short alias for in-context
recognition.

## Shape

- Short alias (kebab-case, memorable): `container-thinking`,
  `action-bias`, `empty-directory-paralysis`.
- Description: what the failure is.
- Symptom / recognition prompt: how the agent can recognize the mode in
  its own behavior mid-task.
- Corrective signals: phrases users say when this mode is happening
  (verbatim or paraphrased -- useful for pattern-matching against fresh
  user feedback).
- Worked example: a concrete instance from a case-study.
- Recovery: what to do when recognition fires.

## Frontmatter

```yaml
---
aliases:
  - <primary-alias>
mitigated-by:
  - ../procedures.kb/<proc>.md
  - ../principles.kb/<principle>.md
eliminated-by: []
---
```

- `aliases:` -- short names this mode is known by.
- `mitigated-by:` -- procedures or principles that reduce likelihood or impact.
- `eliminated-by:` -- procedures or principles that prevent the mode entirely.
  Rare; most modes are mitigated, not eliminated.

## See also

- `../procedures.kb/reconcile-case-study.md` -- the procedure that produces failure-mode entries.
- `case-study.md` -- where failure-mode aliases are first perceived (provisional)
  before reconciliation to canonical form.

TODO: expand with examples once `failure-modes.kb/` is populated.
