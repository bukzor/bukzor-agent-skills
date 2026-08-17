"""The act algebra over a real ledger, llm-claims/design.claims.kb.

The ledger is REIFY's degenerate case: every judgment rides as
fields on the claim it judges -- `standing:`/`verdict:` the signing
assessor's one act, `verify:` a checker's -- nothing is reified,
nothing strikes.  The desugaring must be faithful (decode undoes
encode) and the stack's computed standing must reproduce every
file's written fields.  [REIFY, SUGAR]

The desugaring lives here, not in src/: the representation seam
inventories the code's carriers rather than adding any, and this
form is incubating until it proves out.
"""

from collections.abc import Mapping
from pathlib import Path

from engine_tower.standing import Act, color, effective

LEDGER = Path(__file__).parents[5] / "llm-claims" / "design.claims.kb"
assert LEDGER.is_dir(), LEDGER  # no ledger, no witness: fail, never skip

SIGNERS = ("agent", "user")  # the standings that name a judge
RESTING = ("bare", "open")  # the standings that do not


def admits_all(act: Act) -> bool:
    return True


def fields(path: Path) -> dict[str, str]:
    """The file's scalar frontmatter -- block-list values (`why:`)
    read as empty and are not sugar for any act."""
    lines = path.read_text().splitlines()
    assert lines[0] == "---", (path, lines[0])
    out: dict[str, str] = {}
    for line in lines[1 : lines.index("---", 1)]:
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "-")):
            out[key] = value.strip()
    return out


def read_ledger() -> Mapping[str, Mapping[str, str]]:
    return {
        str(path.relative_to(LEDGER)): fields(path)
        for path in sorted(LEDGER.rglob("*.md"))
        if path.name != "CLAUDE.md"
    }


def desugar(stored: Mapping[str, Mapping[str, str]]) -> frozenset[Act]:
    """Fields -> acts.  `bare` and `open` name no judge, so they
    desugar to no act: they are states of the claim, not judgments of
    it.  [REIFY]"""
    acts: set[Act] = set()
    for occasion, (claim, f) in enumerate(sorted(stored.items())):
        assert f["standing"] in SIGNERS + RESTING, (claim, f["standing"])
        if f["standing"] in SIGNERS:
            acts.add(Act(f["standing"], claim, f.get("verdict", "accepted"), occasion))
        if "verify" in f:
            acts.add(Act(f["verify"], claim, "certified", occasion))
    return frozenset(acts)


def resugar(eff: frozenset[Act], claim: str, resting: str) -> dict[str, str]:
    """Effective acts -> fields: the one-entry verdict map back to its
    scalar sugar.  A second act of either sort on one claim is a
    reify tripwire, past which the field form stops being licensed.
    [SUGAR, REIFY]"""
    mine = {act for act in eff if act.target == claim}
    signatures = [act for act in mine if act.assessor in SIGNERS]
    checkers = [act for act in mine if act.assessor not in SIGNERS]
    assert len(signatures) <= 1, signatures
    assert len(checkers) <= 1, checkers
    out: dict[str, str] = {}
    if signatures:
        [signature] = signatures
        out["standing"] = signature.assessor
        if signature.verdict != "accepted":
            out["verdict"] = signature.verdict
    else:
        out["standing"] = resting
    if checkers:
        [checker] = checkers
        out["verify"] = checker.assessor
    return out


def test_the_fields_are_the_one_act_sugar():  # REIFY, SUGAR
    stored = read_ledger()
    acts = desugar(stored)
    # the run is only a witness if the ledger exercises every branch
    standings = {f["standing"] for f in stored.values()}
    assert standings & set(SIGNERS) and standings & set(RESTING), standings
    assert any("verdict" in f for f in stored.values())
    assert any("verify" in f for f in stored.values())

    eff = effective(acts, admits_all)
    assert eff == acts  # nothing strikes: the whole record is effective
    for claim, f in stored.items():
        sugared = {k: v for k, v in f.items() if k in ("standing", "verdict", "verify")}
        assert resugar(eff, claim, f["standing"]) == sugared, claim


def test_computed_standing_reproduces_the_written_fields():  # REIFY, DEFEAT
    """Below the tripwires -- one signer per claim, no contravention,
    no dispute -- the interval collapses everywhere: a written
    verdict computes to out, everything else to in, and no claim
    comes back contested or moot."""
    stored = read_ledger()
    verdicts = color(frozenset(stored), frozenset(), desugar(stored), admits_all)
    for claim, f in stored.items():
        assert verdicts[claim] == ("out" if "verdict" in f else "in"), (claim, f)
