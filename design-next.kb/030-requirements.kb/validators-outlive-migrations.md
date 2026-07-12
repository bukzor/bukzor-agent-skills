---
why:
  - mechanism-over-exhortation
  - single-source-improvement
---

# Validators Outlive Migrations

Every convention change ships a recurring validator, not a one-shot
sweep. The validator joins a permanent battery (`kb doctor`) that
runs on demand and on every enforced trigger, so conventions cannot silently regress
— muscle memory and training priors will keep re-emitting old forms
long after a sweep.

Checkable: for each entry in the migration log, a corresponding
doctor check exists and passes. V1's half-landed renames (`.d/`
references surviving the `.kb/` rename inside the renaming skill's
own index files) are the motivating counter-example.
