# INCIDENT -- Investigation kb

<!-- Replace: one paragraph. What failed, on what system, over what
window, and how it ended (recovered on its own / rebooted / still
broken). A resuming agent reads this first and nothing else is allowed
to assume it was there. -->

Collections, one per information type:

- `timeline.kb/` -- dated events of the incident; `timeline.md` synthesizes
- `evidence.kb/` -- raw captures; append-only, never rewritten
- `findings.kb/` -- conclusions distilled from evidence, status-tracked
- `root-cause.kb/` -- candidate explanations; `root-cause.md` is the decision point
- `environment.kb/` -- static machine context (topology, resources, monitoring)
- `remediations.kb/` -- prevention/recovery measures and adoption status
- `reports.kb/` -- outbound upstream contributions and posting status
- `todo.kb/` -- next actions, Skill(llm-subtask) conventions

Maintenance:

- New evidence lands as a new dated file in `evidence.kb/`; then update the
  `status`/`evidence` of affected findings and root-cause candidates --
  never edit a capture to match a conclusion.
- When the root cause closes, rewrite `root-cause.md` to state the answer;
  keep `root-cause.kb/` as the record of why alternatives lost.
- Update `last-updated` in `README.md`/`timeline.md` when their content changes.
