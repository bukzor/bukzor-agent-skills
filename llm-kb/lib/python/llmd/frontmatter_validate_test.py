#!/usr/bin/env python3
"""Tests for validate_frontmatter.py"""

from pathlib import Path

import pytest

from . import frontmatter_validate as fv
from .types import JsonObj

# TODO: Add unit tests for:
# - Union types: type: [string, null] should accept both str and NoneType
# - type_map coverage: all JSON Schema types map correctly to Python types
# - Schema discovery: x.jsonschema.yaml validates x.d/*.md


@pytest.fixture(autouse=True)
def clear_schema_retrieval_cache():
    fv.clear_schema_cache()


def _write_shared_schema(skills_home: Path):
    skill_dir = skills_home / "common-skill"
    _ = skill_dir.mkdir()
    _ = (skill_dir / "shared.jsonschema.yaml").write_text("""\
definitions:
  why:
    type: array
    items: {type: string}
""")


class DescribeSkillRefResolution:
    def it_resolves_a_ref_to_a_skill_owned_schema(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(fv, "SKILLS_HOME", tmp_path)
        _write_shared_schema(tmp_path)
        schema: JsonObj = {
            "type": "object",
            "properties": {
                "why": {"$ref": "skill://common-skill/shared.jsonschema.yaml#/definitions/why"},
            },
        }

        errors = fv.validate_against_schema({"why": ["parent-a"]}, schema)

        assert errors == []

    def it_surfaces_a_type_error_through_the_ref(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(fv, "SKILLS_HOME", tmp_path)
        _write_shared_schema(tmp_path)
        schema: JsonObj = {
            "type": "object",
            "properties": {
                "why": {"$ref": "skill://common-skill/shared.jsonschema.yaml#/definitions/why"},
            },
        }

        errors = fv.validate_against_schema({"why": "not-a-list"}, schema)

        assert errors, "expected the ref target's type constraint to produce an error"


class DescribeFileRelativeRefResolution:
    def it_resolves_a_whole_file_ref_to_a_sibling_schema(self, tmp_path: Path):
        _ = (tmp_path / "why.jsonschema.yaml").write_text("""\
type: array
items: {type: string}
""")
        schema_path = tmp_path / "goals.jsonschema.yaml"
        _ = schema_path.write_text("""\
type: object
properties:
  why:
    $ref: why.jsonschema.yaml
""")

        schema = fv.load_schema(schema_path)
        assert schema is not None
        errors = fv.validate_against_schema({"why": ["parent-a"]}, schema)

        assert errors == []

    def it_resolves_a_fragment_ref_to_a_sibling_schema(self, tmp_path: Path):
        _ = (tmp_path / "animals.jsonschema.yaml").write_text("""\
definitions:
  mammal:
    type: object
    properties:
      legs: {const: 4}
      fur: {const: true}
  bird:
    type: object
    properties:
      legs: {const: 2}
      feathers: {const: true}
""")
        schema_path = tmp_path / "petting-zoo.jsonschema.yaml"
        _ = schema_path.write_text("""\
type: object
properties:
  goat:
    $ref: animals.jsonschema.yaml#/definitions/mammal
  chicken:
    $ref: animals.jsonschema.yaml#/definitions/bird
""")

        schema = fv.load_schema(schema_path)
        assert schema is not None
        errors = fv.validate_against_schema(
            {"goat": {"legs": 4, "fur": True}, "chicken": {"legs": 2, "feathers": True}},
            schema,
        )

        assert errors == []
