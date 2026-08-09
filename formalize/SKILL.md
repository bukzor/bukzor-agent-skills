---
name: formalize
description: "Slash-command: /formalize <paths> -- distill the ideas at paths into a claim ledger of named theories. Agent MUST load on /formalize, or when asked to find the mathematical structure in a body of informal work."
---

# /formalize \<paths\>

Take the ideas represented at the paths and produce their formal
account: a well-factored set of theories-of-claims, filed per
`Skill(llm-claim-ledger-kb)`. The dual command is `/deformalize`; a
formalization is not done until the two have met (see Verification).

## Why, before how

The account is a retention device, not an ornament: its owner will
have "good ideas" that restructure the system, and the properties
worth keeping must survive restructurings nobody re-verifies by hand.
A structure earns its place by what it lets us keep. Judge every step
below by that.

## The bar

Naming a structure -- a category, a lattice, a monad -- is worth
nothing on its own. An identification carries: the carrier, the
operations, the laws they satisfy, one smallest instance drawn from
the data, and the observation that would kill it. If the laws fail on
the data, "there is no structure here" is a result; say it plainly. A
citation is not an exhibit.

## Procedure

1. **Survey** the paths wide before framing anything. Schemas and
   data carry the actual ontology; prose carries only the motivation.
   Report the recurring shapes, the tensions, and the places that
   itch before theorizing. Delegate the breadth if that is cheaper.
2. **Conjecture** freely: several candidate structures (five is a
   floor), cheap sketches only, each meeting the bar above. At least
   one should feel like a reach -- a list of safe picks is hiding the
   good conjecture. Then kill your own weak ones and say what killed
   each; survivors get worked in full.
3. **Stratify.** The subject usually has layers, and a claim true of
   the most generic layer may miss richer structure above it -- or be
   false there. Say what makes a level a level, what relation orders
   them, and which claims survive at which level; genericity and
   structure trade against each other, so locate every claim on that
   trade. Where one level's structure is definable from the level
   below, say so -- that is load-bearing.
4. **Boil down** to a one-page picture. State what you
   compartmentalized away and what each abstraction costs; a
   simplification that drops a real obligation is a bug.
5. **Crystallize the questions** the work was bought to settle --
   each stated twice, as experienced and as well-posed (often
   different questions; the difference is a finding) -- then which
   claims settle each, and what residue stays open.
6. **File it** per `Skill(llm-claim-ledger-kb)`: one claim per file,
   theories named (never numbered), each collection's `CLAUDE.md`
   carrying `prior:`/`ontology:`/`defeated by:`. Auxiliary and
   sub-theories are encouraged wherever one lets a citing theory
   argue in one sentence. The questions from step 5 are themselves a
   theory. The entry-point `.md` carries the poset and the picture.

## Verification

Hand the result to `/deformalize` -- ideally a fresh session, so the
code cannot inherit the prose's blind spots -- and adjudicate every
mismatch it reports. Claims a witness exercises get `verify:` lines;
what stays unwitnessed is the ledger's stated proof debt, not a
secret.
