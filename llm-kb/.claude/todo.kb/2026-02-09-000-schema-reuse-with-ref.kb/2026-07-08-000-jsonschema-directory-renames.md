# Progress (2026-07-08): `schemas/` -> `jsonschema/` renames

Swept the two remaining skills that published schemas from a `schemas/`
directory -- llm-discourse-graph (5 files) and llm-design-kb (1 file) --
to `jsonschema/`, completing directory-name uniformity for
skill-published schemas.

"jsonschema" chosen over "schema" deliberately (entrenchment explicitly
discounted): exact match with the `.jsonschema.yaml` suffix makes one
greppable token across files, dirs, and `skill://` URIs; names the
specific technology where "schema(s)" is overloaded; mass noun, so no
singular/plural drift. "schema/" would keep the suffix stutter anyway
and split the vocabulary.

Also added the yaml-language-server modeline to all six moved schemas.
One live consumer repointed (in its own repo, uncommitted there):
prototype.chatfs `docs/dev/technical-policy.jsonschema.yaml`, which
validates clean through the new path.
