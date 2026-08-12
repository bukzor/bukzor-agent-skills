Now make it run. Write the smallest executable model of your account: one module per level, one test per law -- each test the smallest instance that would fail if the law were false -- plus one test that the modules' import graph respects your own ordering of levels.

Put it outside this repo, or in a fresh subdirectory you create; don't list trash/ -- it's inside the blind. Boring, obvious code; the point is the tests.

A law you can't check in a ~50-line test isn't thereby wrong, but say why not -- "not mechanically checkable, because X" is part of the account.

Then review the pair, claim by claim: does the witness show what the account asserts? Adjudicate every mismatch out loud, one of two ways -- the account was wrong (update it, saying what changed) or the code is wrong (fix it, saying why). No silent repair in either direction; the mismatches are the findings.
