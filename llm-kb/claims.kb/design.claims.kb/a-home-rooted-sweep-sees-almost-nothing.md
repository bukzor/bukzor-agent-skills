---
label: HOME_ROOT_EMPTY
standing: bare
verify: "llm.kb-validate ~ | tail -1   # 230 files, against 551 in bukzor-agent-skills alone"
---

# A Home-Rooted Sweep Sees Almost Nothing

`llm.kb-validate ~` reports 230 files. One repository under it,
bukzor-agent-skills, reports 551 by itself.

The cause is not a bug and needs no fix. The walk drops what git
ignores, and both container directories ignore their whole contents on
purpose:

```
~/repo/.gitignore:2:*/
~/claude/.gitignore:3:*/
```

Every project under them is an independent repository, correctly
invisible to the one above. So a `~` root is not a wide net -- it is a
net with no bottom.

Anything phrased as "run the sweep from `~`" is therefore a no-op, and
a guard that claims homedir coverage by naming `~` covers nothing.
