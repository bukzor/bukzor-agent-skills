---
origin:
  - "6b0cdfea:552"
blind: true
---

# 040 -- The executable witness

The honesty pass, and the turn the original run only found by
accident: the account got sharply better when it had to run (the
comparison with an executable model surfaced a missing premise and an
import-graph hole). Expensive; skip only if the session is short. A
miss looks like tests that restate definitions instead of checking
laws.

````
Now make it run. Write the smallest executable model of your account: one module per level, one test per law -- each test the smallest instance that would fail if the law were false -- plus one test that the modules' import graph respects your own ordering of levels.

Put it outside this repo, or in a fresh subdirectory you create; don't list trash/ -- it's inside the blind. Boring, obvious code; the point is the tests.

A law you can't check in a ~50-line test isn't thereby wrong, but say why not -- "not mechanically checkable, because X" is part of the account. Report what running it broke. What a witness breaks, fix in the account, not in the test.
````
