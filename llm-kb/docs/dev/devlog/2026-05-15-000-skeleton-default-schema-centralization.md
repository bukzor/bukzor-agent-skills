# Devlog: 2026-05-15 — skeleton-default schema centralization

## Focus

Continue the methodology kb work from the May 13 seed. Drive the
validator to clean across all three skills; centralize idea/todo
schemas on the llm-subtask skeleton; complete the SKILL.kb audit
infrastructure pass.

## Decisions

### SKELETON-DEFAULT as the schema-distribution model

**Rationale:** `llm-subtask/skeleton/.claude/` holds the canonical
`ideas.jsonschema.yaml` and `todo.jsonschema.yaml`. Consuming skills
(llm-kb, llm-collab, llm-subtask itself) carry verbatim copies in
their own `.claude/` directories. The skeleton is the source-of-truth;
copies are the install operation.

**Alternatives considered:**
- `$ref` from each copy to the skeleton — clean but unimplemented in
  `frontmatter_validate.py`. Tracked as
  `.claude/todo.kb/2026-02-09-000-schema-reuse-with-ref.md`.
- Symlinks — rejected per existing convention ("No symlinks for
  trigger files," `2026-05-13-000` devlog). `$ref` paths and relative
  YAML refs would resolve from the symlink's apparent location, not
  the target's.
- Leave schemas at skill roots (`llm-collab/idea.jsonschema.yaml`) —
  rejected because the validator's `parent.parent /
  $CATEGORY.jsonschema.yaml` lookup can't find a schema at the wrong
  directory level. `.kb/` schemas must sit adjacent to their `.kb/`.

### post-mortem.md to SKILL.kb/procedures.kb/

**Rationale:** The capture procedure is generic — every consumer
running this skill could use it. `docs/dev/` is the
maintainer-internal methodology kb; `SKILL.kb/` is the consumer-facing
runtime. Relocating clarifies the audience boundary.

**Alternatives considered:** Leave it in `docs/dev/` and reference
across the boundary. Rejected because reaching across the maintainer
boundary for a runtime trigger smelled wrong.

### Sessions.kb `session: { uuid, started, ended }` shape

**Rationale:** Nesting the lifecycle markers under a `session:` key
groups identity + lifecycle into one namespace, separates them from
per-entry editorial metadata (`cwd`, `color`, `focus`), and lets the
schema enforce required + load-bearing-null in one place.

**Alternatives considered:** Top-level `session-uuid`, `session-started`,
`session-ended`. Rejected for awkward grouping; doesn't compose. The
old top-level `session-uuid` was migrated to nested `session.uuid`.

### Validator skips dotfiles

**Rationale:** A `.template.md` (shell-substitution skeleton) lives in
`~/.claude/sessions.kb/`. Pathlib's `*.md` glob matches dotfiles.
Skipping anything starting with `.` follows the shell convention for
"hidden / not data."

**Alternatives considered:**
- Move template out of the `.kb/` — possible, but the placement is
  intentional (the substituted output goes back to the same dir).
- Add `additionalProperties: true` or relax types — rejected; would
  weaken validation everywhere.

## Conventions Established

- **SKELETON-DEFAULT:** template-canonical files live at
  `llm-subtask/skeleton/`; projects vendor copies into their own
  `.claude/`. Drift until `$ref` lands.
- **Anti-enumeration in schemas:** parent `description:` fields should
  not summarize their children's attributes. The properties block
  carries that already; doubling it in description is the same smell
  as a CLAUDE.md that lists current contents.
- **Validator recovery line:** when a known `.kb/` is missing a
  schema, copy from `llm-subtask/skeleton/.claude/`. Documented in
  `SKILL.md`.
- **Dotfile convention in `.kb/`:** `.template.md` and other meta
  files use a leading dot; the validator skips them.

## Open Questions

- Should `reconcile-case-study.md` also move to `SKILL.kb/procedures.kb/`?
  (Tracked in `llm-kb/.claude/todo.md`.) The capture/distill pair are
  symmetrically generic.
- Naming question for `post-mortem.md` (capture-incident? learn-from-failure?)
  deferred until a second case-study clarifies the modes.

## Next Session

The originating distillation work is unblocked but not done. See
`.claude/todo.kb/2026-05-15-000-reconcile-seed-case-study-may-13-har-browse-rust-port.md`.
Run from a fresh context per the post-mortem / reconcile split.

## References

- `~/.claude/sessions.kb/skeleton-default.md` — the session-index entry.
- `docs/dev/devlog/2026-05-13-000-skill-kb-and-methodology-seed.md` —
  the prior session whose follow-ups this session executed.
- `~/.claude/sessions.kb/yaml-date-jsonschema.md` — parallel session
  that bootstrapped the validator's `date`/`instant` types.
