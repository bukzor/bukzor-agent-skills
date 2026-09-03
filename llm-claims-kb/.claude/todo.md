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
- [x] Awaiting the owner: do skeleton ledgers belong in the fleet?
      57e1ca7's discovery matches by name, so
      `llm-design-kb/skeleton/docs/dev/claims.kb` (template content)
      now enters every sweep — its labels become fleet facts to
      `llm-claims-kb-mentions` and its theories count in the census.
      Default under silence: skeletons stay in. If ruled out, the
      repair is one more exclusion in `ledger.ledger_roots`, which
      already skips `.claude` and `trash/`
      Ruled 2026-09-01: "Skeleton is a valid albeit empty ledger, and
      should continue to be" — skeletons stay discovered. The
      label-pollution worry dissolves under NON_CLAIM_TOKENS
      (llm-claims notation.kb): the fleet stops gating mentions and
      becomes at most a "defined in X" hint
- [x] Build the mention-gate reform once its open policies rule —
      policies in llm-claims `design.claims.kb/notation.kb/`:
  - [x] Mirror LABEL_MIN's two-character floor in `MENTION`
        (`mentions.py`); the schema pattern now enforces it at write
        time. Done 2026-09-01 — the mention form carries the schema's
        `(?=..)` as `(?=[A-Z][A-Z0-9_])`, since a bare lookahead
        constrains the string ahead, not the match. No finding
        changed: single capitals were already filtered out by the
        fleet lookup, so the floor stays invisible until the gate
        inverts
  - [x] Close the census blindspot: `unimported()` iterates
        `theory.claims` only, so defining-claim prose is never
        checked. Fixed 2026-09-01 — the scan reads the defining claim
        with the rest, resolving it against the theory's own `why:`.
        Findings went 1 → 5, and all four new ones come from defining
        claims (`strata.claims.md`, and GRAIN, which defines a
        sub-theory of notation)
  - [x] Settle BACKTICK_SCOPE before touching the code-span strip.
        Ruled 2026-09-03: a backtick exempts nothing, in both scans.
        The owner returned it as a fact, not a choice -- "this was
        decided by measurement already" -- since NON_CLAIM_TOKENS had
        already priced a list entry at one line once, which makes the
        comparison a computation. The claim is rewritten to its answer
        (`a-backtick-does-not-exempt-a-token.md`, `standing: user`)
  - [x] Invert the gate per NON_CLAIM_TOKENS/NON_CLAIM_FIELD: report
        any unreachable label-shaped token unless listed in the
        scope's `non-claim-tokens:`; reachability wins; demote the
        fleet lookup to the "defined in X" hint. Built 2026-09-03 --
        the field is on the schema and in `ledger.py`, a claim reads
        its own theory's list and its containers' (the interior
        NON_CLAIM_FIELD scopes it to), and the fleet lookup now only
        decorates a finding
  - [x] Drop the code-span strip in `speech()` too (ownership), per
        the same ruling. Done 2026-09-03; the fleet went 7 → 8
        trespasses, the new one the predicted false positive
        (`principles.kb/` read as the word *principle*). It has no
        list to go on -- `non-claim-tokens:` is label-shaped tokens,
        and the trespass scan is a queue with four repairs, not an
        error list -- so it sits in the queue like the other seven
- [x] Five citations survived the seeded `non-claim-tokens:` lists —
      real fleet labels named by theories that import nothing reaching
      them, which is the finding the inverted gate exists to surface.
      Imported 2026-09-03 at the owner's word ("go ahead and add the
      necessary why's", minimality to be reviewed separately): EXTEND
      takes llm-design-kb's MIGRATION, ENGINE takes llm-claims'
      NOTATION, and GRAIN takes DATA_REPRESENTATION, CONSTITUTION and
      SCALAR. The scan reports zero findings fleet-wide
- [ ] Repairing a mention on a *defining* claim always buys an idle
      import. Two of the five above landed in the idle queue at once
      (GRAIN -> DATA_REPRESENTATION, GRAIN -> SCALAR), and the cause is
      structural, not a judgment about those imports:
      `support_witnessed` excludes the taker's own defining claim,
      since its citation *is* the import under adjudication — but a
      defining claim is exactly where cross-theory citations
      concentrate, so the sentence that motivated the import can never
      witness it. Either the support lens should read a defining
      claim's prose citations (which the mentions scan now computes
      exactly), or IDLE_UNDECIDABLE should say outright that this
      shape is expected. Idle entries are never errors, so this is a
      queue-noise question, not a correctness one
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
