---
why:
  - ../020-goals.kb/designed-for-deletion.md
---

# Classes Detach Cleanly

Nothing below a class names the class: the spec and the engine are
written, and stay correct, without knowing any specific class exists.
A class is adopted by copying its package alone and retired by
`git rm -r` on that package — either direction leaves the core (spec
+ engine) unchanged and every other class unaffected.

Checkable:
- grep the engine source for class names — zero hits.
- `git rm -r <class-package>` — the core (`kb validate`, `kb doctor`,
  every other class's own checks) stays green.
- `kb new <deleted-class>` — fails cleanly (an unknown-class lookup
  miss, not a crash) once the package is gone.
