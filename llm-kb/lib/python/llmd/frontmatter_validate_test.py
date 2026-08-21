#!/usr/bin/env python3
"""Tests for validate_frontmatter.py"""

import datetime
import subprocess
from pathlib import Path

import pytest

from . import frontmatter_validate as fv
from ._jsonschema_adapter import DIALECT_URI
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


def _init_repo(root: Path):
    _ = subprocess.run(("git", "init", "-q", str(root)), check=True)
    _ = (root / ".gitignore").write_text("trash/\n")


def _commit_all(repo: Path):
    _ = subprocess.run(("git", "-C", str(repo), "add", "-A"), check=True)
    _ = subprocess.run(
        ("git", "-C", str(repo), "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "fixture"),
        check=True,
    )


def _write_kb(collection: Path):
    _ = collection.mkdir(parents=True)
    _ = (collection / "entry.md").write_text("---\nlabel: X\n---\n\n# Entry\n")


def _collections(results: list[fv.ValidationResult]) -> list[str]:
    return [result.text for result in results if result.kind == "dir"]


class DescribeGitignoredDiscovery:
    def it_skips_a_kb_the_walk_found_under_an_ignored_directory(self, tmp_path: Path):
        _init_repo(tmp_path)
        _write_kb(tmp_path / "live.kb")
        _write_kb(tmp_path / "trash" / "scratch.kb")

        results = list(fv.validate_paths(iter([tmp_path])))

        assert _collections(results) == ["live.kb"]

    def it_validates_an_ignored_collection_named_on_the_command_line(self, tmp_path: Path):
        _init_repo(tmp_path)
        _write_kb(tmp_path / "trash" / "scratch.kb")

        results = list(fv.validate_paths(iter([tmp_path / "trash"])))

        assert _collections(results) == ["scratch.kb"]

    def it_validates_everything_outside_a_repository(self, tmp_path: Path):
        _write_kb(tmp_path / "live.kb")
        _write_kb(tmp_path / "trash" / "scratch.kb")

        results = list(fv.validate_paths(iter([tmp_path])))

        assert sorted(_collections(results)) == ["live.kb", "scratch.kb"]

    def it_asks_a_submodule_about_its_own_contents(self, tmp_path: Path):
        # The superproject refuses the question outright -- "Pathspec ... is
        # in submodule" -- so each path must be asked where it lives. The
        # submodule's own .gitignore is what governs inside it.
        _init_repo(tmp_path)
        _init_repo(tmp_path / "mod")
        _write_kb(tmp_path / "mod" / "live.kb")
        _write_kb(tmp_path / "mod" / "trash" / "scratch.kb")
        _commit_all(tmp_path / "mod")
        _ = subprocess.run(
            ("git", "-C", str(tmp_path), "-c", "advice.addEmbeddedRepo=false", "add", "mod"),
            check=True,
        )

        results = list(fv.validate_paths(iter([tmp_path])))

        assert _collections(results) == ["live.kb"]

    def it_raises_when_git_cannot_answer(self, tmp_path: Path):
        # A `.git` git refuses to read: the filter cannot know what is
        # scratch, and must not silently decide that nothing is.
        _ = (tmp_path / ".git").write_text("not a gitfile\n")
        _write_kb(tmp_path / "live.kb")

        with pytest.raises(subprocess.CalledProcessError):
            _ = list(fv.validate_paths(iter([tmp_path])))


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

    def it_keeps_extension_types_when_the_ref_target_declares_the_llmd_dialect(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(fv, "SKILLS_HOME", tmp_path)
        skill_dir = tmp_path / "common-skill"
        _ = skill_dir.mkdir()
        _ = (skill_dir / "dated.jsonschema.yaml").write_text(f"""\
$schema: "{DIALECT_URI}"
type: object
properties:
  last-updated: {{type: date}}
""")
        schema: JsonObj = {"$ref": "skill://common-skill/dated.jsonschema.yaml"}

        errors = fv.validate_against_schema({"last-updated": datetime.date(2026, 3, 10)}, schema)

        assert errors == []

    def it_reports_a_schema_bug_when_extension_types_hide_under_a_stock_dialect(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        # `type: date` is not draft-07; evolve() honestly hands the ref
        # target to the stock draft-07 validator, and the resulting
        # UnknownType must surface as a legible error, not a crash.
        monkeypatch.setattr(fv, "SKILLS_HOME", tmp_path)
        skill_dir = tmp_path / "common-skill"
        _ = skill_dir.mkdir()
        _ = (skill_dir / "dated.jsonschema.yaml").write_text("""\
$schema: "http://json-schema.org/draft-07/schema#"
type: object
properties:
  last-updated: {type: date}
""")
        schema: JsonObj = {"$ref": "skill://common-skill/dated.jsonschema.yaml"}

        errors = fv.validate_against_schema({"last-updated": datetime.date(2026, 3, 10)}, schema)

        assert len(errors) == 1
        assert "'date'" in errors[0]
        assert DIALECT_URI in errors[0]

    def it_rejects_an_unknown_dialect_legibly(self):
        schema: JsonObj = {"$schema": "urn:no-such-dialect", "type": "object"}

        errors = fv.validate_against_schema({}, schema)

        assert len(errors) == 1
        assert "urn:no-such-dialect" in errors[0]
        assert DIALECT_URI in errors[0]

    def it_resolves_a_file_relative_ref_inside_a_skill_owned_stub(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(fv, "SKILLS_HOME", tmp_path)
        skill_dir = tmp_path / "common-skill"
        _ = skill_dir.mkdir()
        _ = (skill_dir / "todo.jsonschema.yaml").write_text("""\
type: array
items: {type: string}
""")
        _ = (skill_dir / "stub.jsonschema.yaml").write_text("$ref: todo.jsonschema.yaml\n")
        schema: JsonObj = {
            "type": "object",
            "properties": {
                "todo": {"$ref": "skill://common-skill/stub.jsonschema.yaml"},
            },
        }

        errors = fv.validate_against_schema({"todo": ["a", "b"]}, schema)

        assert errors == []


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


class DescribeSchemaDiscovery:
    def it_errors_on_frontmatter_no_schema_can_reach(self, tmp_path: Path):
        loose = tmp_path / "loose.md"
        _ = loose.write_text("---\nlabel: X\n---\n\n# Loose\n")

        errors = fv.validate_file(loose)

        assert len(errors) == 1, errors
        assert "frontmatter-outside-a-collection" in errors[0], errors[0]

    def it_passes_a_file_that_has_no_frontmatter_at_all(self, tmp_path: Path):
        loose = tmp_path / "loose.md"
        _ = loose.write_text("# Loose\n")

        assert fv.validate_file(loose) == []

    def it_reaches_through_a_hive_partition_to_the_collection_schema(self, tmp_path: Path):
        # A partition subdivides a collection without renaming it, so the
        # schema is still the collection's.
        _ = (tmp_path / "logs.jsonschema.yaml").write_text("""\
type: object
required: [label]
properties:
  label: {type: string}
additionalProperties: false
""")
        partition = tmp_path / "logs.kb" / "year=2026"
        partition.mkdir(parents=True)
        entry = partition / "entry.md"
        _ = entry.write_text("---\nbogus: X\n---\n\n# Entry\n")

        errors = fv.validate_file(entry)

        assert [error for error in errors if "bogus" in error], errors

    def it_reports_a_skill_manifest_like_any_other_loose_file(self, tmp_path: Path):
        # Whose keys these are and whether to report on the file are separate
        # questions. llm-kb defines no schema for SKILL.md, and still says so.
        manifest = tmp_path / "SKILL.md"
        _ = manifest.write_text("---\nname: x\ndescription: y\n---\n\n# X\n")

        results = list(fv.validate_one_file(manifest, None, 0))

        assert [result.errors for result in results] == [(fv.NO_SCHEMA_GOVERNS,)], results

    def it_skips_a_maintenance_guide_wherever_it_sits(self, tmp_path: Path):
        # CLAUDE.md is forced to live inside the collection it governs, so
        # reporting it would report a file that cannot be a member.
        collection = tmp_path / "notes.kb"
        collection.mkdir()
        guide = collection / "CLAUDE.md"
        _ = guide.write_text("---\nanything: goes\n---\n\n# Notes\n")

        assert list(fv.validate_one_file(guide, None, 0)) == []
