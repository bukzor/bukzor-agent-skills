"""Tests for bin/llm.kb-validate-links, run as the user runs it: a subprocess."""

import subprocess
from pathlib import Path

SCRIPT = Path(__file__).parents[3] / "bin" / "llm.kb-validate-links"

WITNESS = """\
# x

See [GOOD] and [BAD], or [inline](../missing-inline.md), or `../missing-code.md`.

[GOOD]: ./item.md
[BAD]:
  ../missing-ref.md
"""


def _check(tmp_path: Path, body: str, *flags: str):
    kb = tmp_path / "x.kb"
    _ = kb.mkdir()
    _ = (kb / "item.md").write_text(body)
    return subprocess.run(
        (str(SCRIPT), *flags, str(kb)),
        capture_output=True,
        text=True,
    )


def _broken(stdout: str) -> list[str]:
    """The link text of each reported error line."""
    return [
        line.split(": ", 1)[1].split(" -> ")[0]
        for line in stdout.splitlines()
        if line.startswith("    ")
    ]


class DescribeMarkdownLinkDestinations:
    def it_reports_exactly_the_broken_links_of_the_witness(self, tmp_path: Path):
        result = _check(tmp_path, WITNESS)
        assert result.returncode == 2, result.stdout
        assert sorted(_broken(result.stdout)) == [
            "../missing-code.md",
            "../missing-inline.md",
            "../missing-ref.md",
        ]

    def it_counts_every_nominated_link(self, tmp_path: Path):
        result = _check(tmp_path, WITNESS)
        assert "4 links in 1 files" in result.stdout, result.stdout

    def it_skips_urls_and_pure_anchors(self, tmp_path: Path):
        body = "[a](https://example.com/x.md) [b](#top) [c](mailto:a@b.c)\n"
        result = _check(tmp_path, body, "--lax")
        assert result.returncode == 0, result.stdout
        assert "0 links" in result.stdout, result.stdout

    def it_strips_a_trailing_anchor_before_resolving(self, tmp_path: Path):
        result = _check(tmp_path, "[a](./item.md#section) [b](../gone.md#x)\n")
        assert _broken(result.stdout) == ["../gone.md"], result.stdout

    def it_ignores_links_inside_code_blocks(self, tmp_path: Path):
        body = "```\n[a](../in-fence.md)\n```\n"
        result = _check(tmp_path, body)
        assert result.returncode == 0, result.stdout

    def it_does_not_read_a_rewrapped_prose_line_as_a_definition(self, tmp_path: Path):
        body = "A sentence that ends\n[LABEL]: and goes on in prose.\n"
        result = _check(tmp_path, body)
        assert result.returncode == 0, result.stdout
        assert "0 links" in result.stdout, result.stdout

    def it_gates_destinations_through_the_strict_shape_rule(self, tmp_path: Path):
        result = _check(tmp_path, "[a](bare-name.md)\n")
        assert "0 links" in result.stdout, result.stdout

    def it_nominates_bare_destinations_under_lax(self, tmp_path: Path):
        result = _check(tmp_path, "[a](bare-name.md)\n", "--lax")
        assert _broken(result.stdout) == ["bare-name.md"], result.stdout
