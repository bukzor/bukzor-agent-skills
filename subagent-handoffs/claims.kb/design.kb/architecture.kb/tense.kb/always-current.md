---
label: ALWAYS_CURRENT
standing: user
verdict: superseded
why:
  - ../../requirements.kb/tense-known.md
---

# Every handoff file always states the current truth

Every handoff file, open or done, states the current truth, and is
amended in place whenever that truth changes.

Superseded by FROZEN_WHEN_DONE (`frozen-when-done.md`). False once a
unit is done: nobody revisits a finished unit's file, so a later
unit's change leaves it stating what used to be true. In practice, a
done report kept the old spelling of a field after a later unit
renamed it everywhere else.
