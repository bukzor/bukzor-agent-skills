---
label: STALE_WHEN
standing: user
why:
  - ../purpose.kb/find-and-resolve-inconsistencies.md
  - ../purpose.kb/evaluate-a-change-by-what-it-breaks.md
---

# Every Claim Carries Its Staleness Condition

Every claim records the condition under which it stops holding -- its
**stale when**. One condition serves three uses:

- evaluated against today's data, it finds inconsistencies (CONSIST);
- evaluated against a proposed change, it predicts breakage (DISCUSS,
  and eventually AUTOCHECK);
- read by a later agent, it says which claims a change obliges them to
  re-check.

The earlier design split this into two notions -- a counterexample
already sitting in the data, and a future edit that would invalidate the
claim -- and the split was wrong: the difference is *when* the condition
gets evaluated, and the condition itself is one thing. Unifying them is
what makes PINS pay, because a change re-opens the claims whose
condition it touches and leaves the rest settled.

The name points at the use rather than the event. "What would break it"
describes a moment; "stale when" tells a reader to come back and
re-check, which is the action the field exists to trigger. It is also
already the suite's word: `Skill(llm-claims-kb)` spells `stale-when:` on
every theory header.
