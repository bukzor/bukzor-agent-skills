#!/usr/bin/env python3
"""Tests for validate_frontmatter.py"""

import pytest

from llmd import frontmatter_validate as fv

# TODO: Add unit tests for:
# - Union types: type: [string, null] should accept both str and NoneType
# - type_map coverage: all JSON Schema types map correctly to Python types
# - Schema discovery: x.jsonschema.yaml validates x.d/*.md


@pytest.fixture(autouse=True)
def _clear_skill_retrieval_cache():
    fv._retrieve_skill.cache_clear()


def _write_shared_schema(skills_home):
    skill_dir = skills_home / "common-skill"
    skill_dir.mkdir()
    (skill_dir / "shared.jsonschema.yaml").write_text(
        "definitions:\n"
        "  why:\n"
        "    type: array\n"
        "    items: {type: string}\n"
    )


class DescribeSkillRefResolution:
    def it_resolves_a_ref_to_a_skill_owned_schema(self, tmp_path, monkeypatch):
        monkeypatch.setattr(fv, "SKILLS_HOME", tmp_path)
        _write_shared_schema(tmp_path)
        schema = {
            "type": "object",
            "properties": {
                "why": {"$ref": "skill://common-skill/shared.jsonschema.yaml#/definitions/why"},
            },
        }

        errors = fv.validate_against_schema({"why": ["parent-a"]}, schema)

        assert errors == []

    def it_surfaces_a_type_error_through_the_ref(self, tmp_path, monkeypatch):
        monkeypatch.setattr(fv, "SKILLS_HOME", tmp_path)
        _write_shared_schema(tmp_path)
        schema = {
            "type": "object",
            "properties": {
                "why": {"$ref": "skill://common-skill/shared.jsonschema.yaml#/definitions/why"},
            },
        }

        errors = fv.validate_against_schema({"why": "not-a-list"}, schema)

        assert errors, "expected the ref target's type constraint to produce an error"
