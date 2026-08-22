"""The ownership scan: where the fleet's stipulations and the law disagree.

The law is the ownership theory (llm-claims/design.claims.kb/ownership.md),
and this scan does not restate it: `ownership.py` beside that theory is
imported and run over the real fleet, so `owner`, `reach` and the findings
have exactly one definition. What lives here is the adapter -- reading
ledgers off disk, deciding what a claim *says* -- plus the reporting.

Three scans, one per way the corpus can depart from the law:

- the default, **contention** -- one word owned twice in one ledger, an
  error charged to both entries, which only a person can settle
  (CONTENTION): a failing exit. A word stipulated by a theory and its own
  descendant is inert instead, the outer owning (OUTERMOST_WINS), and one
  stipulated in two different ledgers is legal, namespaces being
  per-ledger (SORT_REACH).
- `--trespass` -- an owned word said by one of the owner's own siblings,
  with no import to license it (TRESPASS), ranked by the force of the
  stipulation behind it (EXCLUSION_FORCE). A queue, not an error list:
  each finding has four honest repairs (FOUR_POSITIONS) and the scan
  picks none of them.
- `--idle` -- imports with neither lens witnessed: the taker never says
  the taken words, and no claim in its interior cites into the prior's
  tree (IDLE_UNDECIDABLE). A claim-level `why:` into the prior is the
  support lens made mechanical (IDLE_TEST's tell); what remains may
  still carry support on the arrow alone, so idle entries are
  adjudicated by reading and are never errors.

`--candidates` asks the fourth question, which is about the ontology
rather than about a departure from it: which words a theory should own
(SHOULD_OWN), measured as concentration outside the owner's interior --
inside it, saying the owner's word is the point. `--census` prints the
one-line summary ARITY's `verify:` runs.

Run from the repo root.
"""

import argparse
import importlib.util
import re
import sys
from collections import Counter
from collections.abc import Iterable, Mapping, Sequence
from pathlib import Path

from .ledger import Theory, read_ledger


def load_law():
    """The runnable law, imported from beside the theory the claims cite."""
    here = Path(__file__).resolve()
    path = here.parents[4] / "llm-claims/claims.kb/design.claims.kb/ownership.py"
    assert path.exists(), (path, "the law must sit beside its theory")
    spec = importlib.util.spec_from_file_location("ownership_law", path)
    assert spec and spec.loader, path
    module = importlib.util.module_from_spec(spec)
    sys.modules["ownership_law"] = module
    spec.loader.exec_module(module)
    return module


law = load_law()


def ledger_roots(under: Path = Path()) -> tuple[Path, ...]:
    """Every ledger under the working tree, worktree copies excepted."""
    return tuple(
        sorted(
            path
            for path in under.rglob("*.claims.kb")
            if path.is_dir() and ".claude" not in path.parts
        )
    )


def fleet() -> tuple[Theory, ...]:
    """Every theory in every ledger."""
    return tuple(
        theory for root in ledger_roots() for theory in read_ledger(root).theories
    )


def site(theory: Theory) -> str:
    """A fleet-unique name: the collection's path."""
    return str(theory.path)


def ledger_of(theory: Theory) -> Path:
    """The `*.claims.kb` the theory lives in -- itself, for a ledger's own."""
    here = theory.path
    return next(one for one in (here, *here.parents) if one.name.endswith(".claims.kb"))


def address(theory: Theory) -> tuple[str, ...]:
    """The law's path form: the ledger, then the steps down to the theory.

    The ledger heads the tuple because the law reads the namespace off it
    (SORT_REACH), and siblinghood off the rest.
    """
    root = ledger_of(theory)
    return (str(root),) + theory.path.relative_to(root).parts


def speech(path: Path) -> str:
    """The claim speaking: body only, code spans struck.

    A backticked name is a literal quoted from elsewhere, not this claim
    saying the word, so it never counts as speech -- the same cutout the
    mentions scan makes.
    """
    body = re.sub(r"\A---\n.*?\n---\n", "", path.read_text(), flags=re.DOTALL)
    return re.sub(r"```.*?```|`[^`]*`", " ", body, flags=re.DOTALL)


def prose(path: Path) -> str:
    """What the law listens to: the claim's speech, lowercased."""
    return speech(path).lower()


def quotes(theory: Theory, word: str) -> Iterable[tuple[str, str]]:
    """Each sentence in the theory's own voice that says the word.

    The evidence a finding is adjudicated on: the disposition turns on
    which sense the site meant, and only the sentence tells.
    """
    for claim in (theory.defining, *theory.claims):
        if claim:
            for block in speech(claim.path).split("\n\n"):
                for line in re.split(r"(?<=[.!?;:])\s+", " ".join(block.split())):
                    if says(line.lower(), word):
                        yield claim.path.name, line
        else:
            pass


def says(text: str, word: str) -> bool:
    """The word on word boundaries, bare or plural."""
    return re.search(rf"(?<!\w){re.escape(word)}s?(?!\w)", text) is not None


def own_text(theory: Theory) -> str:
    """What this theory says in its own voice -- its claims, not its children's.

    Descendants speak for themselves: the law reaches them through
    containment, so folding their prose in here would charge a parent for
    a word only its child said.
    """
    return " ".join(
        prose(claim.path) for claim in (theory.defining, *theory.claims) if claim
    )


def spoken(text: str, words: Iterable[str]) -> frozenset[str]:
    """Which of the words the text says -- bare or plural, phrases included.

    Single words go through a token set because the candidate list is the
    whole fleet's ontology and a regex apiece is the scan's hot loop.
    """
    tokens = frozenset(re.findall(r"[a-z][a-z'-]*", text))
    singles = frozenset(word for word in words if " " not in word)
    phrases = frozenset(word for word in words if " " in word)
    return frozenset(
        word for word in singles if word in tokens or f"{word}s" in tokens
    ) | frozenset(word for word in phrases if says(text, word))


def homes(theories: Sequence[Theory]) -> Mapping[Path, Theory]:
    """Each defining claim's file, to the theory it defines -- how `why:` lands."""
    return {
        theory.defining.path.resolve(): theory for theory in theories if theory.defining
    }


def contended(theories: Sequence[Theory]) -> frozenset[str]:
    """Words the law cannot assign an owner: two stipulators in one ledger.

    Asked of the law itself, one ledger at a time -- `owner` raising is the
    definition, not a rule restated here.
    """
    barrel = adapt(theories, frozenset())
    namespaces = {law.ledger_of(one) for one in barrel}
    found = set()
    for word in {word for one in barrel for word in one.ontology}:
        for namespace in namespaces:
            try:
                law.owner(barrel, word, namespace)
            except law.Contention:
                found.add(word)
    return frozenset(found)


def adapt(theories: Sequence[Theory], candidates: frozenset[str]) -> frozenset:
    """The fleet in the law's own terms: paths, ontologies, speech, imports.

    `candidates` is what to listen for; pass the empty set when only
    ownership is in question, since reading every claim is the expensive
    half and stipulations alone answer it.
    """
    home = homes(theories)
    return frozenset(
        law.Theory(
            path=address(theory),
            ontology=frozenset(theory.ontology),
            says=spoken(own_text(theory), candidates) if candidates else frozenset(),
            imports=tuple(
                address(home[prior.path.resolve()])
                for prior in theory.priors
                if prior.path.resolve() in home
            ),
        )
        for theory in theories
    )


def doubles(theories: Sequence[Theory]) -> Iterable[tuple[str, str, Theory, Theory]]:
    """Each word two theories both stipulate, and how the law reads the pair."""
    for one in theories:
        for other in theories:
            if site(one) < site(other):
                here, there = one.path.resolve(), other.path.resolve()
                if here in there.parents or there in here.parents:
                    verdict = "inert"
                elif ledger_of(one) != ledger_of(other):
                    verdict = "foreign"
                else:
                    verdict = "contending"
                for word in sorted(set(one.ontology) & set(other.ontology)):
                    yield word, verdict, one, other


def trespasses(theories: Sequence[Theory]) -> tuple[tuple[str, tuple, tuple], ...]:
    """The law's word findings, gathered per stipulation, heaviest first.

    Force is the tally itself: a stipulation's force is the findings it
    generates (EXCLUSION_FORCE), so grouping the findings once beats asking
    the law's `force` per word, which recomputes the whole scan each call.
    """
    candidates = {word for theory in theories for word in theory.ontology}
    barrel = adapt(theories, frozenset(candidates - contended(theories)))
    docket: dict[tuple[str, tuple], set[tuple]] = {}
    for owner_path, site_path, word in law.word_findings(barrel):
        docket.setdefault((word, owner_path), set()).add(site_path)
    return tuple(
        (word, owner_path, tuple(sorted(sites)))
        for (word, owner_path), sites in sorted(
            docket.items(), key=lambda row: (-len(row[1]), row[0])
        )
    )


def usage(theories: Sequence[Theory]) -> Mapping[str, Mapping[str, Counter[str]]]:
    """Per ledger, per word: how many times each theory says it.

    Plurals fold into their singular where the ledger says both, matching
    the word boundary the law's own `says` reads. Possessives and primes
    drop with the apostrophe, so `owner's` counts as owning.
    """
    tally: dict[str, dict[str, Counter[str]]] = {}
    for theory in theories:
        book = tally.setdefault(str(ledger_of(theory)), {})
        for word, count in Counter(
            re.findall(r"[a-z]{3,}(?:-[a-z]+)*", own_text(theory))
        ).items():
            book.setdefault(word, Counter())[site(theory)] += count
    for book in tally.values():
        for word in [one for one in book if one.endswith("s") and one[:-1] in book]:
            book[word[:-1]].update(book.pop(word))
    return tally


def sayers(theories: Sequence[Theory]) -> Mapping[str, frozenset[str]]:
    """Fleet-wide, each word to the sites that say it -- how English is spotted.

    Concentration inside one ledger cannot tell a coinage from a function
    word: `they` is concentrated wherever most of the prose is. A word the
    rest of the fleet says as freely is English, and the fleet is the only
    sample this scan has to say so with.
    """
    tally: dict[str, set[str]] = {}
    for theory in theories:
        for word in set(re.findall(r"[a-z]{3,}(?:-[a-z]+)*", own_text(theory))):
            tally.setdefault(word, set()).add(site(theory))
    for word in [one for one in tally if one.endswith("s") and one[:-1] in tally]:
        tally[word[:-1]] |= tally.pop(word)
    return {word: frozenset(where) for word, where in tally.items()}


def interior_sites(root: Theory, theories: Sequence[Theory]) -> frozenset[str]:
    """The owner's site and every site under it -- where its words are at home."""
    home = root.path.resolve()
    return frozenset(
        site(one)
        for one in theories
        if one.path.resolve() == home or home in one.path.resolve().parents
    )


def reaches(theories: Sequence[Theory]) -> Mapping[str, frozenset[str]]:
    """Each site to the sites it imports, the chain included (IMPORT_CHAIN)."""
    home = homes(theories)
    priors = {
        site(one): tuple(
            site(home[cited.path.resolve()])
            for cited in one.priors
            if cited.path.resolve() in home
        )
        for one in theories
    }
    found = {}
    for start in priors:
        seen: set[str] = set()
        frontier = [start]
        while frontier:
            for step in priors[frontier.pop()]:
                if step not in seen:
                    seen.add(step)
                    frontier.append(step)
        found[start] = frozenset(seen)
    return found


def stipulators(theories: Sequence[Theory]) -> Mapping[str, Mapping[str, str]]:
    """Per ledger, each owned word to its owner's site, the outermost winning."""
    found: dict[str, dict[str, str]] = {}
    for theory in sorted(theories, key=lambda one: len(one.path.resolve().parts)):
        book = found.setdefault(str(ledger_of(theory)), {})
        for word in theory.ontology:
            book.setdefault(word, site(theory))
    return found


def candidates(
    theories: Sequence[Theory], floor: int, ceiling: int
) -> tuple[tuple[str, str, str, int, int], ...]:
    """SHOULD_OWN, both directions: what to own, and what to stop owning.

    The question is asked of a stipulation, never of a ledger. Spread is
    counted *outside the owner's interior*, because that is where the
    counterfactual lives: inside, saying the owner's word is the point.
    Counted per ledger instead, a ledger-root entry is charged for the
    ambience that is its whole reason to sit at the root -- a root's
    interior is the ledger, so its word can never generate a finding at
    all.

    The two sides mirror each other across that boundary:

    - **cull** -- an owned word said by more than `ceiling` theories
      outside its owner is ambient vocabulary however unusual it looks,
      and owning it polices noise.
    - **own** -- an unowned word one theory leans on, where every other
      sayer is already inside that theory or imports it, costs no
      finding today and arms the counterfactual tomorrow. The gate is
      one *stipulator*, not one sayer: a coinage does not stop being a
      coinage when a theory that imports it says it once. What that
      loosening lets through, the fleet-wide count catches -- a word the
      other ledgers say as freely is English, however hard this one
      leans on it.
    """
    owned = stipulators(theories)
    everywhere = sayers(theories)
    at = {site(one): one for one in theories}
    inside = {site(one): interior_sites(one, theories) for one in theories}
    reach = reaches(theories)
    found = []
    for ledger, book in usage(theories).items():
        for word, where in book.items():
            home = owned.get(ledger, {}).get(word)
            if home is None:
                home = max(where, key=lambda one: (where[one], len(at[one].path.parts)))
                loose = [
                    one
                    for one in where
                    if one not in inside[home] and home not in reach[one]
                ]
                uses = sum(count for one, count in where.items() if one in inside[home])
                abroad = everywhere.get(word, frozenset()) - inside[home]
                if not loose and uses >= floor and len(abroad) <= ceiling:
                    found.append(("own", home, word, uses, len(abroad)))
                else:
                    pass
            else:
                out = [one for one in where if one not in inside[home]]
                if len(out) > ceiling:
                    found.append(
                        ("cull", home, word, sum(where[one] for one in out), len(out))
                    )
                else:
                    pass
    return tuple(sorted(found, key=lambda row: (row[0], -row[4], row[1], row[2])))


def interior_text(root: Theory, theories: Sequence[Theory]) -> str:
    """Everything the theory's interior says, as one blob."""
    home = root.path.resolve()
    region = [
        theory
        for theory in theories
        if theory.path.resolve() == home or home in theory.path.resolve().parents
    ]
    return " ".join(own_text(theory) for theory in region)


def cites_into(claim, target: Theory) -> bool:
    """One of the claim's `why:` paths resolves into the target theory's tree."""
    tree = target.path.resolve()
    defining = target.defining.path.resolve() if target.defining else None
    return any(
        cited.path.resolve() == defining or tree in cited.path.resolve().parents
        for cited in claim.why
    )


def support_witnessed(root: Theory, prior: Theory, theories: Sequence[Theory]) -> bool:
    """A claim in the taker's interior rests on the prior's tree by `why:`.

    This is the support lens read mechanically: cross-theory citation by
    claim-relative path is a normal way to write support, and an import
    whose interior carries such an arrow is not idle, whatever words go
    unsaid. The taker's own defining claim is excluded -- its citation
    IS the import under adjudication, so it cannot witness itself.
    """
    home = root.path.resolve()
    skip = root.defining.path.resolve() if root.defining else None
    for theory in theories:
        there = theory.path.resolve()
        if not (there == home or home in there.parents):
            continue
        for claim in (*theory.claims, *filter(None, [theory.defining])):
            if claim.path.resolve() != skip and cites_into(claim, prior):
                return True
    return False


def idle_imports(theories: Sequence[Theory]) -> Iterable[tuple[Theory, Theory]]:
    """Imports with neither lens witnessed: no taken word said by the
    taker's interior, and no interior `why:` landing in the prior's tree."""
    home = homes(theories)
    for theory in theories:
        text = interior_text(theory, theories)
        for cited in theory.priors:
            prior = home.get(cited.path.resolve())
            if (
                prior
                and not any(says(text, word) for word in prior.ontology)
                and not support_witnessed(theory, prior, theories)
            ):
                yield theory, prior


def census(theories: Sequence[Theory]) -> str:
    """One line: the shape of the gap between the corpus and the law (ARITY)."""
    tally = {"contending": 0, "inert": 0, "foreign": 0}
    for _, verdict, _, _ in doubles(theories):
        tally[verdict] += 1
    idle = len(list(idle_imports(theories)))
    total = sum(len(theory.priors) for theory in theories)
    pairs = ", ".join(f"{count} {verdict}" for verdict, count in tally.items())
    docket = trespasses(theories)
    return (
        f"doubles: {pairs}; imports: {idle} idle of {total}; trespasses:"
        f" {sum(len(sites) for _, _, sites in docket)} over {len(docket)} stipulations"
    )


def report(theories: Sequence[Theory]) -> int:
    """The default scan: every double, judged, contention failing."""
    failing = 0
    rows = sorted(
        doubles(theories),
        key=lambda row: (row[1], row[0], site(row[2]), site(row[3])),
    )
    for word, verdict, one, other in rows:
        if verdict == "contending":
            failing += 1
            print(
                f"finding: {word!r} owned by both {site(one)} and {site(other)}"
                f" -- charged to both entries (CONTENTION); one has to lose it"
            )
        elif verdict == "inert":
            outer, inner = sorted(
                (one, other), key=lambda theory: len(theory.path.resolve().parts)
            )
            print(
                f"inert: {word!r} restated by {site(inner)} inside"
                f" {site(outer)} -- the outer owns (OUTERMOST_WINS)"
            )
        else:
            pass  # foreign doubles are legal: namespaces are per-ledger
    print(census(theories))
    return 1 if failing else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--census", action="store_true", help="one summary line")
    parser.add_argument(
        "--trespass", action="store_true", help="owned words said by siblings"
    )
    parser.add_argument(
        "--cite", action="store_true", help="quote the trespassing sentences"
    )
    parser.add_argument(
        "--idle", action="store_true", help="the idle-import adjudication queue"
    )
    parser.add_argument(
        "--candidates", action="store_true", help="what to own, and what to release"
    )
    parser.add_argument(
        "--floor", type=int, default=8, help="uses before a word is worth owning"
    )
    parser.add_argument(
        "--ceiling", type=int, default=4, help="theories past which a word is ambient"
    )
    args = parser.parse_args()
    theories = fleet()
    if args.census:
        print(census(theories))
        return 0
    elif args.trespass:
        rows = trespasses(theories)
        spoke = {address(theory): theory for theory in theories}
        for word, owner_path, sites in rows:
            print(f"force {len(sites):>2}  {word!r} owned by {'/'.join(owner_path)}")
            print(f"          said by: {' '.join(site[-1] for site in sites)}")
            if args.cite:
                for site_path in sites:
                    for claim, line in quotes(spoke[site_path], word):
                        print(f"    {site_path[-1]}/{claim}")
                        print(f"      {line}")
            else:
                pass
        skipped = contended(theories)
        print(
            f"{sum(len(sites) for _, _, sites in rows)} trespasses over"
            f" {len(rows)} stipulations -- cull, move, admit, or uniquify each;"
            f" {len(skipped)} contended words skipped as undecidable"
        )
        return 0
    elif args.candidates:
        rows = candidates(theories, args.floor, args.ceiling)
        for verdict, home, word, uses, spread in rows:
            if verdict == "cull":
                print(
                    f"cull {word!r} owned by {home} -- said outside it by"
                    f" {spread} theories, {uses} times"
                )
            else:
                print(
                    f"own  {word!r} for {home} -- {uses} uses there, said"
                    f" outside it by {spread} theories, none a would-be finding"
                )
        culls = sum(1 for row in rows if row[0] == "cull")
        print(
            f"{culls} owned words are ambient (>{args.ceiling} theories outside"
            f" the owner); {len(rows) - culls} unowned words concentrate"
            f" (>={args.floor} uses, one stipulator, <={args.ceiling} sayers abroad)"
            f" -- SHOULD_OWN decides, not this scan"
        )
        return 0
    elif args.idle:
        queue = sorted(idle_imports(theories), key=lambda pair: site(pair[0]))
        for taker, prior in queue:
            note = (
                " (which stipulates no words)"
                if not prior.ontology
                else " and says none of its words"
            )
            print(
                f"adjudicate: {site(taker)} imports {site(prior)}{note}"
                f" -- no interior why: lands there either"
            )
        total = sum(len(theory.priors) for theory in theories)
        print(
            f"{len(queue)} idle of {total} imports -- neither lens witnessed;"
            f" resolve each by reading"
        )
        return 0
    else:
        return report(theories)


if __name__ == "__main__":
    raise SystemExit(main())
