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
- [ ] `--candidates` needs a background corpus that does not depend on
      cwd. Run in a single-ledger repo it offers function words as
      coinages: in `prototype.llm-postbox` the top 11 included `may`
      (12 uses), `with` (21) and `until` (11). Run in this repo — 13
      ledgers — not one function word appears among 23 candidates,
      which are all real terms (`projection`, `fixpoint`, `stipulator`,
      `modeline`, `phi`).
  - [ ] So the measure is sound and the corpus is the defect. The
        `candidates` docstring already names the intended defense —
        "a word the other ledgers say as freely is English, however
        hard this one leans on it" — but `abroad` is computed from
        `sayers(theories)`, and `theories` is `fleet()`, which is
        `ledger_roots()` walking from cwd. A project repo holding one
        ledger has no other ledgers to be measured against, so every
        common English word looks concentrated. No blacklist is
        needed; the frequency signal just has nothing to read.
  - [ ] Options, cheapest first: (a) fold a known fleet root into the
        walk for `abroad`/ambient counting only, never for findings —
        namespaces stay per-ledger (SORT_REACH), so a foreign ledger
        must not be able to generate one; (b) ship a generated
        ambient-frequency table in the skill, refreshed by a
        maintenance command, so the signal survives where no fleet is
        checked out; (c) scale `floor`/`ceiling` by fleet size, which
        only relocates the arbitrary constant and is the weakest.
  - [ ] Separately, and independent of fleet size: a token that is
        already part of a multi-word stipulation is offered as if
        unowned. TOPOLOGY owns `single reader`, and the same scan
        proposed owning `single` (8 uses) for the ledger root.
        Candidate tokens should be checked against the components of
        existing ontology entries, not just against whole entries.
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
