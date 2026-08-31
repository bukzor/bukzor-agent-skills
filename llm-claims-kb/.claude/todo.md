---
managed-by: Skill(llm-subtask)
---

- [x] Ledger auto-discovery misses the scoped-bare form ruled below.
      `mentions.py:43` and `ownership.py:70` both walk
      `rglob("*.claims.kb")`, which cannot match a directory named
      plainly `claims.kb` — so `llm-claims-kb-mentions` and
      `llm-claims-kb-ownership` report clean on a ledger they never
      opened. Found against `prototype.llm-postbox`, whose ledger is
      `docs/dev/claims.kb/`: `--census` said "0 trespasses over 0
      stipulations" while six theories with ontologies sat on disk, and
      a hand-run scan then turned up five real trespasses. `graph` and
      `flatten` are unaffected (explicit path argument). Fix in the
      shared adapter, not per-tool: discovery should accept a directory
      named exactly `claims.kb` as well as `*.claims.kb`. Until then a
      silent pass on these two tools means nothing.
- [ ] Awaiting the owner: do skeleton ledgers belong in the fleet?
      57e1ca7's discovery matches by name, so
      `llm-design-kb/skeleton/docs/dev/claims.kb` (template content)
      now enters every sweep — its labels become fleet facts to
      `llm-claims-kb-mentions` and its theories count in the census.
      Default under silence: skeletons stay in. If ruled out, the
      repair is one more exclusion in `ledger.ledger_roots`, which
      already skips `.claude` and `trash/`
- [ ] `llm-claims-kb-flatten` drops list blocks from claim bodies —
      a first paragraph ending in a colon renders as a dangling
      fragment and the bullets vanish (e.g. a struck claim's quoted
      vetoes). Claim-body guidance mandates bulleted enumerations,
      so the fix is in flatten: render list items as continuation
      lines or inline.
- [x] Record the scoped-bare-`claims.kb` naming convention in SKILL.md
      ("Layout" and "What this is not"): when a ledger lives in a
      subject's sub-scope (e.g. `sources.kb/X.kb/claims.md` +
      `claims.kb/`), the collection takes its bare category name — the
      scope supplies the subject; `<name>.claims.kb` remains the form
      where a subject token is needed. Both claims skills already rule
      shape-over-name, so this is a naming addendum, not a semantics
      change. Ruled by the user 2026-08-24; rationale in
      `~/claude/meta-reasoning/docs/dev/devlog/2026-08-24-000-kb-nesting-conventions-ruled----breakdowns-live-under-their-source.md`;
      first worked instance is that repo's
      `sources.kb/design-discussion-transcript.kb/claims.kb/`.
  - [x] Record the slot ruling with it: the `X.md` beside a ledger's
        `X.kb/` is both the roll-up and the defining claim — one file,
        claim frontmatter over roll-up prose. llm-kb's validator and
        `references/frontmatter-outside-a-collection.md` already state
        it; this SKILL.md half-says it ("its entry point, carrying the
        poset") and should say it outright.
