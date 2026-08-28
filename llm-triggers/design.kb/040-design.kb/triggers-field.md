---
why:
  - ../010-mission.md
  - bank-format.md
  - trigger-desc.md
  - floor.md
---

# The `triggers:` Field

One frontmatter field supplants `requires:` and `depends:`. An entry pairs a
juncture-keyed condition with what to read:

```yaml
triggers:
    - when: restructuring this ledger
      read: Skill(llm-claims-kb)
    - before: committing
      read:
          - ./commit.md
          - ./conventions.md
    - read: ./chain-target.md
```

**Junctures are `before:`, `when:`, `after:`** — the bank's own vocabulary
(`bank-format.md`), so a trigger reads the same whether its condition is
spelled as a directory name or a frontmatter key. Values are trigger-descs
(`trigger-desc.md`), which keeps `at:` available where a time-point applies.

**`read:` takes a scalar or a list.** One condition may deliver several
targets; a shared antecedent never forces near-duplicate entries.

**A bare entry inherits its carrier's condition.** No juncture means the
condition was discharged by whatever routed the reader in. This is what
`depends:` should have meant — that field instead asked the reader to judge
relevance using the material it gated, which is unevaluable
(`../use-cases.kb/payload-gated-conditions.md`).

Inheritance makes the carrier law mechanical rather than a judgment call. A
bare entry is well-formed only in a conditionally-reached carrier: a bank
entry, a `SKILL.md`, or a file that is some trigger's own `read:` target.
Everywhere else — chiefly a `CLAUDE.md`, which loads for every arrival — a
bare entry is an error (`../use-cases.kb/arrival-fired-directives.md`).
