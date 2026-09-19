# procedures.kb -- shared methods

Methods invoked by a trigger -- in `../must-read.kb/` or in a
consumer's own bank -- when the situation calls for them. Procedure
files name no callers; callers name the procedure.

## What belongs here

- A method whose trigger lives outside this skill's bank: an
  occasion that arises without intent (a peer message arriving)
  binds at a scope installed every session, and only the method is
  the skill's to ship.
- A method referenced by 2+ triggers.

## What does NOT belong here

- A method with one in-skill trigger -> inline it in that entry.
