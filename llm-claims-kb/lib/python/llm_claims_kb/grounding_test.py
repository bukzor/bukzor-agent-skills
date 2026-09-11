from collections.abc import Mapping
from pathlib import Path

from .grounding import Grounding, grounding, load_reachable
from .ledger import read_ledger


def write_claim(
    path: Path, label: str, standing: str, why: tuple[str, ...] = (), extra: str = ""
) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    cites = "".join(f"  - {entry}\n" for entry in why)
    front = f"label: {label}\nstanding: {standing}\n{extra}"
    front += f"why:\n{cites}" if cites else ""
    path.write_text(f"---\n{front}---\n\n# {label}\n\nThe claim.\n")
    return path


def rows(root: Path) -> Mapping[str, Grounding]:
    ledger = read_ledger(root)
    return {row.label: row for row in grounding(ledger, load_reachable(ledger))}


def order(root: Path) -> tuple[str, ...]:
    ledger = read_ledger(root)
    return tuple(row.label for row in grounding(ledger, load_reachable(ledger)))


class DescribeEffectiveStanding:
    """The fold over `why:`: ground stops it, a bare derivation passes it
    through, and any other judge it meets is what the claim waits on."""

    def it_stops_at_the_owners_word(self, tmp_path: Path):
        kb = tmp_path / "x.claims.kb"
        write_claim(kb / "a.md", "AA", "agent")
        write_claim(kb / "u.md", "UU", "user", why=("a.md",))

        assert rows(kb)["UU"].effective == "user"
        assert rows(kb)["UU"].weakest == ()
        assert not rows(kb)["UU"].is_judge

    def it_stops_at_a_certified_check(self, tmp_path: Path):
        kb = tmp_path / "x.claims.kb"
        write_claim(kb / "a.md", "AA", "agent")
        write_claim(kb / "c.md", "CC", "bare", why=("a.md",), extra="verify: check.py\n")

        assert rows(kb)["CC"].effective == "certified"

    def it_grounds_a_bare_derivation_resting_only_on_the_owners_word(self, tmp_path: Path):
        kb = tmp_path / "x.claims.kb"
        write_claim(kb / "u.md", "UU", "user")
        write_claim(kb / "d.md", "DD", "bare", why=("u.md",))

        assert rows(kb)["DD"].effective == "user"
        assert rows(kb)["DD"].weakest == ()
        assert not rows(kb)["DD"].is_judge

    def it_is_as_weak_as_the_weakest_judge_it_meets(self, tmp_path: Path):
        kb = tmp_path / "x.claims.kb"
        write_claim(kb / "u.md", "UU", "user")
        write_claim(kb / "a.md", "AA", "agent", why=("u.md",))
        write_claim(kb / "d.md", "DD", "bare", why=("u.md", "a.md"))

        assert rows(kb)["DD"].effective == "agent"
        assert rows(kb)["DD"].weakest == ("AA",)
        assert not rows(kb)["DD"].is_judge
        assert rows(kb)["DD"].user_grounds == ("UU",)

    def it_makes_an_agent_claim_its_own_judge(self, tmp_path: Path):
        kb = tmp_path / "x.claims.kb"
        write_claim(kb / "u.md", "UU", "user")
        write_claim(kb / "a.md", "AA", "agent", why=("u.md",))

        assert rows(kb)["AA"].effective == "agent"
        assert rows(kb)["AA"].is_judge
        assert rows(kb)["AA"].weakest == ()

    def it_calls_a_bare_claim_resting_on_nothing_hidden(self, tmp_path: Path):
        kb = tmp_path / "x.claims.kb"
        write_claim(kb / "h.md", "HH", "bare")

        assert rows(kb)["HH"].effective == "hidden"
        assert rows(kb)["HH"].is_judge

    def it_does_not_count_a_struck_claim_as_ground(self, tmp_path: Path):
        kb = tmp_path / "x.claims.kb"
        write_claim(kb / "s.md", "SS", "user", extra="verdict: rejected\n")
        write_claim(kb / "d.md", "DD", "bare", why=("s.md",))

        assert rows(kb)["DD"].effective == "struck"
        assert rows(kb)["DD"].weakest == ("SS",)

    def it_reports_a_citation_naming_no_file_as_dangling(self, tmp_path: Path):
        kb = tmp_path / "x.claims.kb"
        write_claim(kb / "d.md", "DD", "bare", why=("gone.md",))

        assert rows(kb)["DD"].effective == "dangling"
        assert rows(kb)["DD"].weakest == ("x.claims.kb/gone.md",)
        assert rows(kb)["DD"].dangling == 1

    def it_follows_a_citation_into_another_ledger(self, tmp_path: Path):
        write_claim(tmp_path / "y.claims.kb" / "f.md", "FF", "agent")
        kb = tmp_path / "x.claims.kb"
        write_claim(kb / "d.md", "DD", "bare", why=("../y.claims.kb/f.md",))

        assert rows(kb)["DD"].effective == "agent"
        assert rows(kb)["DD"].weakest == ("FF",)
        assert rows(kb)["DD"].foreign == 1

    def it_survives_a_cycle(self, tmp_path: Path):
        kb = tmp_path / "x.claims.kb"
        write_claim(kb / "a.md", "AA", "bare", why=("b.md",))
        write_claim(kb / "b.md", "BB", "bare", why=("a.md",))

        assert rows(kb)["AA"].effective == "hidden"


class DescribeOrder:
    def it_puts_judges_first_by_what_rests_on_them_then_the_grounded(self, tmp_path: Path):
        kb = tmp_path / "x.claims.kb"
        write_claim(kb / "u.md", "UU", "user")
        write_claim(kb / "a.md", "AA", "agent")
        write_claim(kb / "b.md", "BB", "agent", why=("a.md",))
        write_claim(kb / "d.md", "DD", "bare", why=("b.md",))
        write_claim(kb / "e.md", "EE", "bare", why=("d.md",))

        assert order(kb) == ("AA", "BB", "DD", "EE", "UU")
