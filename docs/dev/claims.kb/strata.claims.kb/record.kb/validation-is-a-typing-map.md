---
label: TYPING
standing: agent
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_record.py::test_validation_is_a_typing_judgment
---

# Validation Is a Typing Map

An instance is a keyed family of records; a schema is a record type.
Validation is not a scan for errors but the exhibition of a typing
map from the instance into the schema -- it either exists or it
doesn't, and the witness is reusable by every later computation that
wants to trust the fields.
