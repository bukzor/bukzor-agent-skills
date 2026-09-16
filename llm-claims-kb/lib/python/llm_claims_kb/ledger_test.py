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


CLAIM = "---\nlabel: {label}\nstanding: bare\n{why}---\n\n# {label}\n\nA claim.\n"


def claim(label: str, *why: str) -> str:
    arrows = "".join(f"  - {entry}\n" for entry in why)
    return CLAIM.format(label=label, why=f"why:\n{arrows}" if arrows else "")


class DescribeSlugDirectories:
    """A plain directory inside a collection is a prefix on its members' names:
    `<slug>/LABEL.md` is one claim, named for its label, and a `.kb/` under a
    slug is a theory of the collection above."""

    def ledger(self, tmp_path: Path) -> Path:
        root = tmp_path / "claims.kb"
        write(tmp_path / "claims.jsonschema.yaml", LEDGER_SCHEMA)
        write(tmp_path / "claims.md", "---\nlabel: ROOT\nstanding: bare\nontology: [x]\n---\n\n# Root\n")
        write(root / "what-no-move-may-raise" / "DEBT.jsonschema.yaml", LEDGER_SCHEMA)
        write(root / "what-no-move-may-raise" / "DEBT.md", claim("DEBT"))
        write(root / "what-no-move-may-raise" / "DEBT.kb" / "CLAUDE.md", "# guide\n")
        write(root / "what-no-move-may-raise" / "DEBT.kb" / "what-voids-repayment" / "UNREPAYABLE.md", claim("UNREPAYABLE"))
        write(root / "why-ledgers-rot" / "PROBLEM.md", claim("PROBLEM"))
        write(
            root / "why-ledgers-rot" / "PROBLEM.kb" / "the-wall" / "WALL.md",
            claim("WALL", "../../../what-no-move-may-raise/DEBT.kb/what-voids-repayment/UNREPAYABLE.md"),
        )
        return root

    def it_names_a_claim_by_slug_and_label(self, tmp_path: Path):
        from .ledger import read_ledger

        ledger = read_ledger(self.ledger(tmp_path))

        assert {claim.id: claim.label for claim in ledger.claims} == {
            "claims": "ROOT",
            "claims/what-no-move-may-raise/DEBT": "DEBT",
            "claims/what-no-move-may-raise/DEBT/what-voids-repayment/UNREPAYABLE": "UNREPAYABLE",
            "claims/why-ledgers-rot/PROBLEM": "PROBLEM",
            "claims/why-ledgers-rot/PROBLEM/the-wall/WALL": "WALL",
        }

    def it_scopes_a_claim_to_the_nearest_collection_through_the_slug(self, tmp_path: Path):
        from .ledger import read_ledger

        ledger = read_ledger(self.ledger(tmp_path))
        by_label = {claim.label: claim for claim in ledger.claims}

        assert by_label["UNREPAYABLE"].scope == "claims/what-no-move-may-raise/DEBT"
        assert by_label["DEBT"].scope == "claims"
        assert by_label["ROOT"].scope == ""
        assert {theory.name: theory.container for theory in ledger.theories} == {
            "claims": "",
            "claims/what-no-move-may-raise/DEBT": "claims",
            "claims/why-ledgers-rot/PROBLEM": "claims",
        }

    def it_resolves_a_why_through_slugs(self, tmp_path: Path):
        from .ledger import dangling, read_ledger

        ledger = read_ledger(self.ledger(tmp_path))

        assert dangling(ledger) == ()

    def it_refuses_a_file_under_a_slug_not_named_for_its_label(self, tmp_path: Path):
        import pytest

        from .ledger import read_ledger

        root = self.ledger(tmp_path)
        write(root / "why-ledgers-rot" / "PROBLEM.kb" / "misnamed" / "WRONG.md", claim("RIGHT"))

        with pytest.raises(AssertionError):
            read_ledger(root)

    def it_leaves_a_directory_git_ignores_unread(self, tmp_path: Path):
        import subprocess

        from .ledger import read_ledger

        root = self.ledger(tmp_path)
        subprocess.run(("git", "init", "-q", str(tmp_path)), check=True)
        write(tmp_path / ".gitignore", "trash/\n")
        write(root / "trash" / "SCRATCH.md", claim("SCRATCH"))

        assert "SCRATCH" not in {claim.label for claim in read_ledger(root).claims}
