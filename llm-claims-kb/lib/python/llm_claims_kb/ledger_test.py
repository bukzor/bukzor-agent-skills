from pathlib import Path

from .ledger import ledger_roots

GRAPH_SCHEMA = """\
type: object
additionalProperties: false
properties:
  sources: {type: array, items: {type: string}}
"""
LEDGER_SCHEMA = '$ref: "skill://llm-claims-kb/jsonschema/claim.jsonschema.yaml"\n'


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


class DescribeLedgerRoots:
    """A `claims.kb/` is a ledger by what its schema requires, not by its name:
    a discourse graph's `claims.kb/` and a ledger's are told apart by whether
    the schema beside the directory requires `label:` and `standing:`."""

    def it_keeps_a_collection_whose_schema_requires_label_and_standing(self, tmp_path: Path):
        write(tmp_path / "ledger" / "x.claims.jsonschema.yaml", LEDGER_SCHEMA)
        (tmp_path / "ledger" / "x.claims.kb").mkdir()

        assert ledger_roots(tmp_path) == (tmp_path / "ledger" / "x.claims.kb",)

    def it_skips_a_collection_whose_schema_requires_neither(self, tmp_path: Path):
        write(tmp_path / "graph" / "claims.jsonschema.yaml", GRAPH_SCHEMA)
        write(tmp_path / "graph" / "claims.kb" / "a-claim.md", "---\nsources: []\n---\n\nA claim.\n")

        assert ledger_roots(tmp_path) == ()

    def it_skips_a_collection_with_no_schema(self, tmp_path: Path):
        write(tmp_path / "bare" / "claims.kb" / "a-claim.md", "A claim with no frontmatter.\n")

        assert ledger_roots(tmp_path) == ()
