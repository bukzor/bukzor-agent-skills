---
name: persist-clarity
description: "Agent MUST load on /persist-clarity, when a session is ending that produced more understanding than diffs, when the user asks to wrap up without losing the clarity/context/understanding, or before /clear or a handoff following significant litigation, debugging, or design work."
---

# /persist-clarity [scope]

A session ends with two products: its **decisions** (diffs, conclusions,
rulings — usually persisted) and its **clarity** — the understanding
that produced them, which evaporates at the context boundary. Clarity
is not storable: fluency, the state where every trade-off is ready to
hand, dies with the context no matter what you write. What you can do
is persist its four residues and a re-entry path that restores it. This
skill is that operation.

## The four residues

1. **Results** — conclusions *with their standing*: who ruled each one,
   what's still open, what would reopen it. A summary of conclusions is
   not this; a summary strips exactly the standing. Work with what disk
   already holds: verify, and/or amend, reword, sharpen — mint as a
   last resort.
2. **Reversals** — why the losing alternatives lost. The most valuable
   residue and the first one lost: without it, the next session
   re-proposes the dead idea and re-pays the whole litigation. Record
   each kill *beside the winner* — its ground, its revisit condition,
   the owner's veto quoted verbatim. The shape for this is a decision
   point (`skill://llm-kb#decision-points`): `$ITEM.md` states the
   resolution and why, `$ITEM.kb/` holds one file per candidate —
   chosen and declined alike.
3. **Lenses** — the ways-of-seeing that generated the decisions. Find
   them by looking for the moments the work *turned*: the question that
   made a hard choice easy; the razor you applied more than once; the
   distinction the user drew that you didn't have at session start; the
   false fork someone dissolved. One lens per entry, phrased as a
   reusable rule, citing the session's own artifact as its worked
   instance.
4. **The narrative address** — a pointer to where the full story can be
   re-mined: session id, transcript, PR, register entry, incident doc.
   A pointer, never a copy.

The same four appear in any situation:

| residue | a design session | a debugging session |
|---|---|---|
| results | the chosen architecture, and who ruled it | the root cause, and how the fix was verified |
| reversals | the rejected store, with its ground | the eliminated hypotheses, with the evidence that killed each |
| lenses | the razor that did most of the choosing | "check the X before blaming the Y" |
| address | ledger commits, register entry | incident doc, session id |

## The re-entry path

Fluency is restorable, not storable — so the last artifact is a
**reading order for a cold agent**: what to load, in what sequence,
placed where that agent will look first (the roll-up, the README, the
CLAUDE.md). Include the warning that the struck and declined records
are load-bearing, not debris; a cold reader skips them by instinct and
then re-litigates them by accident.

## Open threads

Clarity about what is *not* done rots fastest of all. Every open thread
gets a discharge route now, in the project's task system: the task, its
trigger if it's dormant, and where its context lives. An open without a
route is a decision you've silently delegated to amnesia.

## Procedure

1. **Inventory the turns** — settled, killed, reframed, left open —
   from the whole session, not the recent tail. The early turns are the
   ones you've already half-forgotten; that's the signal they need
   persisting.
2. **Run the cold-reader test** on each: could an agent with no memory
   of this session reconstruct it from disk? Persist only what fails —
   re-persisting what's already on disk buries the new under the known.
3. **File each residue into its home.** Decision record (claims
   ledger, ADR, design doc) for results and reversals; the project's
   methodology home (playbook, HACKING) for lenses; the task system
   for discharge routes. Prefer the homes that exist; where a residue
   has none, mint the smallest one that holds it — a single file
   beats a structure, and either beats evaporation. What's banned is
   only the *parallel* home: a second place for something that
   already has a place.
4. **Write the re-entry path last** — it indexes everything the
   previous steps filed.
5. **Verify as the cold agent**: follow your own re-entry path reading
   only what's on disk; anywhere you reach for something missing, that
   is the gap. Then commit — uncommitted clarity is one crash from
   gone.

## Homes, by ecosystem

- Claims-ledger projects (`Skill(llm-claims-kb)`): results are claims
  with standing; reversals are struck claims (`verdict:` with the
  ground and the acceptance quoted in `authority:`); the roll-up
  carries the re-entry section. `Skill(llm-claims)`'s session-ending
  rule already obliges the serialization — this skill adds residues 2–4.
- Session-register projects (`Skill(llm-sessions)`, discussion
  registers): the register entry is the narrative address — a pointer
  plus the name, not a second copy.
- Plain projects: ADRs hold results, and their "options considered"
  section holds reversals; README or HACKING holds lenses; the tracker
  holds discharge routes.

## Anti-patterns

- **The conclusions-summary.** Strips standing and omits reversals —
  it preserves what you decided while discarding why anyone should
  still believe it.
- **The narrative dump.** A transcript-shaped copy nobody will reload;
  the address beats it at a thousandth the size.
- **Parallel structure.** A second home for a residue that already
  has one; the two drift, and the reader trusts the wrong one.
- **Persisting the journey as the state.** Render the final framing;
  the journey lives in the reversals and at the address.
- **Polishing the persisted.** Anything already on disk can be
  sharpened later, by anyone; the residues only you currently hold —
  reversals and lenses — evaporate now, and only you can save them.
  Spend the wrap-up there first.
