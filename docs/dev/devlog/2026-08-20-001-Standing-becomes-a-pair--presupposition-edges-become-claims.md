# Devlog: 2026-08-20 — Standing becomes a pair; presupposition edges become claims

## Focus

Executing the accepted triage of the standing theory. The blast
radius held: `standing.kb/` plus one open claim in `genre.kb/`,
nothing else in the ledger moved.

## Findings

- **The old enum was a pair with a coordinate discarded.** A claim
  answers two questions — has it a subject, is what it says upheld —
  and the ledger answered the second on a three-valued interval while
  answering the first with one bit. That is what printed `KING:
  contested, BALD: in`. Standing is now `Color(sense, content)`, both
  coordinates on the same interval, `content is None` exactly where
  `sense == "out"`. Mootness is a gap in the domain, not a fourth
  point, so the moot/defeated exclusion is structural and needs no
  precedence rule.
- **Neither coordinate bounds the other.** A claim whose
  presupposition is disputed can still be settled on its own terms.
  Taking a meet would discard exactly the fact the pair was
  introduced to keep.
- **The engine let a claim presuppose itself.** With `p ⊣ q`, `q ⊣ p`
  and `q` refuted, it returned `q` moot — refuted into
  meaninglessness by its own refutation, with the refuting acts then
  absorbed. `collapse` now takes the transitive closure and asserts
  irreflexivity: a cycle is a modelling error, reported at the entry.
- **The frame graph was the one thing nobody could dispute.** The
  engine took the presupposition relation as a raw argument, never
  through `effective`, never through a stance. That contradicted two
  `user`-signed claims at once (ACT, STANCE). Fixing it is
  conformance, not a new ruling — which is why the design choices
  *inside* the fix are signed `agent` and remain vetoable.
- **A same-size mutation can leave stale bytecode.** `Status(2)` →
  `Status(1)`, restored within the same second, keeps a `.pyc` whose
  mtime and size both match — so the next run silently tests the old
  text. It cost one bogus RED in the `verify:` sweep. Both mutation
  scripts now run with bytecode off, and every result below was
  re-derived under that setting.

## Decisions

### EDGE: every presupposition edge is itself a claim

**Rationale:** `color` takes `edge_claims: Mapping[str, Edge]` and
`frames()` reads the graph a given reader is holding. Two readers who
disagree about whether `p` presupposes `q` compute different senses —
the disagreement is representable instead of being a precondition of
representing anything. An edge nobody upholds is inert,
well-foundedness included: the cycle test is asked of the graph in
hand, never the graph on offer.
**Consequence:** sense uses the same two seeds content does — an edge
surely held to a claim surely out collapses surely; an edge that may
hold to a claim that may be out collapses possibly. A disputed edge
is worth exactly what a disputed presupposition is worth.

### The two levels do not recurse

**Rationale:** an edge-claim may not be either end of an edge, and
both halves are asserted. What an edge-claim presupposes is a
question the ruling declines to ask — nothing has needed it, and an
unasked question stays cheap to open while an answered one does not.
**Consequence:** HOME (below) collides with this on purpose, and says
so; that collision is the content of the ruling it asks for.

### DENIAL is filed as its own claim

**Rationale:** `q` is a presupposition of `p` when asserting and
denying `p` both take `q` for granted. That criterion is what makes
"presupposition is not encodable as an attack" a proof rather than an
assertion, and it is needed *before* anyone files edges as claims.
**Consequence:** two faces, one mechanized. Computationally it is why
a moot claim absorbs content-acts of *either* polarity; as a filing
criterion it is unmechanized discipline, like confinement.

### HOME is filed open, not ruled

**Rationale:** a claim of a theory plausibly presupposes that
theory's defining claim — the failure modes match (a claim under a
fallen theory is unreadable, not false), the edges would be
well-founded, and the far ends are already claims. But the hammer is
large: one act would moot a whole theory, and no ledger here has ever
lost one.
**Consequence:** filed as `open` in `genre.kb/` rather than left in a
devlog, because un-unified it grows into two sense relations. It
names the choice a ruling would have to make: exempt edge-claims from
their own home, or weaken the stratification to bar only edges *into*
edge-claims.

### The two-level statement needs no claim of its own

**Rationale:** the triage wanted TWO-QUESTIONS filed separately.
Rewriting SENSE made its headline exactly that statement, so a second
claim would restate a sentence rather than add one.
**Consequence:** dropped. SENSE was renamed to
`sense-and-content-are-judged-separately.md` to say so from the `ls`.

## Conventions Established

- **A mutation sweep runs with bytecode caching off.** Same-size
  edits restored inside one second defeat `.pyc` invalidation, and
  the failure mode is a green suite that tested the wrong source.
- **`verify:` is widened to the tests that exist, not to the tests
  one wishes for.** Where a body commits to something no test covers
  and the test is cheap, write it; where it isn't, say so here.

## Verification

- 66 tests green; every `verify:` line in the ledger runs green
  except COVERAGE's, which names a test not yet built and is
  sanctioned by the schema as acceptance debt.
- 13 mutations injected against the engine, all caught, all
  attributed to the intended test: the four sense/collapse ones, the
  cycle assertion, the `Color` invariant, the four EDGE ones, and the
  three added by the `verify:` sweep.
- The Kripke countermodel search was promoted from `trash/` to
  `tests/test_declined_readings.py` and is now cited by SENSE and
  DENIAL. It imports nothing from the engine: it witnesses a claim
  the engine's shape rests on, not the engine.

## The verify: sweep

Under-selection found in three claims, all fixed by writing the
missing witness rather than shrinking the body:

- **STATUS** named a four-rung chain and checked one pair of it. New
  `test_the_status_chain_orders_by_commitment` runs the whole chain,
  strictly, in both directions.
- **REWIRE** committed to disjunction *across* rows and to "piling
  evidence into a dead row is spend without effect"; the check
  covered only conjunction within a row. New
  `test_a_second_row_grants_where_the_first_is_dead` covers both.
- **ACT** gained the edge-claim witness, which is what shows the base
  stays claims-only.
- **DENIAL** gained the two Kripke cases that are literally the
  denial test (`both-polarities-refuted`, `de-morgan`).

Not fixed, recorded instead: **COMPUTED and COMPLETION say standing's
values live in the antichain completion, and the engine raises
there.** The claims are honest about it — COMPLETION says the
mechanized operator raises exactly at the missing join — but the
repair they name is unbuilt, so no `verify:` can cover that sentence.
Filed as a todo bullet rather than reworded.

## References

- `docs/dev/devlog/2026-08-20-000-Correct-SENSE-s-certificate-and-vocabulary.md`
  — established the `verify:` coverage convention this session swept
  against.
- `.claude/todo.kb/2026-08-18-000-Lean-port-of-the-engine-tower.md` —
  its postpone condition ("any ruled claim of the standing theory
  re-litigated within the last few sessions") holds harder after
  today.
