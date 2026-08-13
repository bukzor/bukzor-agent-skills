# Epistemic Dimensions of Claims: Prior Art Survey

A survey of academic and practical frameworks that classify claims along
multiple dimensions, with focus on how different claim types afford different
modes of challenge. Compiled to inform the design of a unified knowledge
representation scheme.

## Foundational Frameworks

### Toulmin Model of Argumentation (1958)

Stephen Toulmin's model decomposes an argument into six components, each
independently challengeable:

| Component | Role | Challenge mode |
|-----------|------|----------------|
| Claim | The assertion | Direct denial |
| Data/Grounds | Supporting evidence | Factual challenge (data is wrong) |
| Warrant | Inferential principle connecting data to claim | Inference is invalid or inapplicable |
| Backing | Support for the warrant | Warrant's authority is contested |
| Qualifier | Degree of certainty ("probably," "certainly") | Strength is overstated/understated |
| Rebuttal | Conditions under which claim fails | Unacknowledged exceptions exist |

Key contribution: separating **strength of inference** (qualifier) from
**truth of premises** (data) from **validity of reasoning pattern** (warrant).
These are three independent axes.

### Searle's Speech Act Taxonomy (1975)

John Searle classified illocutionary acts by their **direction of fit** —
the relationship between words and world:

| Category | Direction of fit | Example |
|----------|-----------------|---------|
| Assertives | Word-to-world (words must match reality) | "The system is down" |
| Directives | World-to-word (reality should change) | "Fix the system" |
| Commissives | World-to-word | "I will fix it" |
| Expressives | No direction of fit | "I'm sorry it's down" |
| Declarations | Both directions (saying makes it so) | "You're fired" |

Key contribution: **direction of fit** determines what counts as a valid
challenge. Assertives are challenged on truth. Directives on authority or
reasonableness. Declarations on institutional standing. You cannot refute a
directive ("fix this") with a factual claim ("it's not broken") — these
are different speech act types with different challenge surfaces.

### Pollock's Defeater Taxonomy (1970s–2000s)

John Pollock identified two fundamentally distinct ways a justified belief
can be defeated:

| Defeater type | What it attacks | Example |
|---------------|----------------|---------|
| Rebutting | The conclusion directly | Counter-evidence for the negation |
| Undercutting | The evidence-to-conclusion link | Showing the inference is unreliable here |

These are logically independent: a conclusion can be true despite flawed
reasoning (undercutting succeeds, rebutting fails), and reasoning can be
valid while the conclusion happens to be false due to misleading evidence
(rebutting succeeds, undercutting fails).

Later work extended this with **higher-order defeaters** — evidence that
the reasoning *process itself* is unreliable (e.g., the reasoner was
impaired).

### AGM Belief Revision (1985)

Alchourrón, Gärdenfors, and Makinson formalized three operations on
belief sets:

| Operation | When applied | Effect |
|-----------|-------------|--------|
| Expansion | New info compatible with existing beliefs | Add belief, close under logic |
| Contraction | Need to stop believing something | Remove belief, preserve maximum |
| Revision | New info contradicts existing beliefs | Add new, remove enough old to maintain consistency |

Key contribution: beliefs have an implicit **entrenchment ordering** — how
reluctant you are to give them up. During revision, the least-entrenched
beliefs are discarded first. This gives every belief a continuous score
representing its resistance to change.

## Multi-Dimensional Frameworks

### Habermas's Validity Claims (1981)

Jürgen Habermas argued that every communicative act simultaneously makes
four validity claims, each independently challengeable:

| Validity claim | Domain | Challenged by | Redeemed by |
|----------------|--------|---------------|-------------|
| Truth | Objective world | Empirical counter-evidence | Theoretical discourse |
| Rightness | Social/normative world | Moral argument | Practical discourse |
| Sincerity | Subjective/inner world | Behavioral inconsistency | Consistent behavior |
| Comprehensibility | Language itself | Showing ambiguity | Explicative discourse |

Key contribution: a claim can be accepted as **true** while challenged as
**normatively illegitimate**, or accepted as **sincere** while challenged
as **unclear**. The four dimensions are fully independent.

### Modal Logic: Four Modalities

Four types of modality represent fundamentally different grounds for claims:

| Modality | Concerns | Operators | Challenge mode |
|----------|----------|-----------|----------------|
| Alethic | Necessity/possibility | necessarily, possibly | Show a world where it fails |
| Epistemic | Knowledge/belief | knows, believes | Provide counter-evidence |
| Deontic | Obligation/permission | ought, may, must not | Challenge the norms |
| Bouletic | Desire/preference | wants, prefers | Challenge the desire |

Key contribution: **Hume's guillotine** — you cannot derive an OUGHT from
an IS. The epistemic and deontic modalities are logically independent.
Challenging a deontic claim ("you ought to X") with epistemic evidence
("but X is false") is a category error.

### Bayesian Epistemology

Formal epistemology identifies multiple independent dimensions of a belief
state:

| Dimension | What it captures | Range |
|-----------|-----------------|-------|
| Credence | Degree of belief | [0, 1] |
| Resilience | How much credence changes with new evidence | [0, 1] |
| Weight of evidence (Keynes) | How much evidence underlies the credence | [0, ∞) |
| Higher-order credence | Confidence in one's own credence | [0, 1] |
| Precision (Joyce, Sturgeon) | Whether credence is a point or interval | point vs [a, b] |

Key contribution: two agents can share credence 0.7 but differ in
**character** — one based on massive evidence (high weight, high resilience),
another on near-ignorance (low weight, low resilience, imprecise). Credence
alone is insufficient.

### T-Box vs A-Box (Description Logic)

Knowledge representation distinguishes two fundamentally different kinds of
statements:

| Component | Contains | Character | Challenge mode |
|-----------|---------|-----------|----------------|
| T-Box (Terminological) | Definitions, hierarchies, axioms | Analytic/stipulative | Propose better definitions |
| A-Box (Assertional) | Individual facts, instances | Empirical/contingent | Contrary evidence |

Key contribution: the difference between **what we mean by our terms**
(T-Box) and **what we claim about the world using those terms** (A-Box).
These require fundamentally different kinds of challenge.

### Walton's Argumentation Schemes (2008)

Douglas Walton cataloged 96 argumentation schemes, each with specific
**critical questions** that constitute legitimate challenges. Examples:

| Scheme | Critical questions |
|--------|-------------------|
| From expert opinion | Is the expert credible? Right field? Do others agree? |
| From analogy | Are cases similar in relevant respects? Critical differences? |
| From cause to effect | Is there really a causal link? Intervening factors? |
| Practical reasoning | Side effects? Better alternatives? Is goal desirable? |

Key contribution: different argument **types** have fundamentally different
**vulnerability profiles**. The critical questions *are* the dimensions of
challenge, and they vary by scheme.

### Levine's Six Types of Claims

Peter Levine identified six claim types requiring different kinds of evidence:

| Type | Example | Evidence required | Challenge mode |
|------|---------|-------------------|----------------|
| Descriptive | "Turnout was 60%" | Observation, measurement | Better data |
| Causal | "Education causes higher income" | Experimental evidence | Confounders |
| Conceptual | "Democracy means rule by the people" | Conceptual analysis | Better conceptualization |
| Classificatory | "This regime is a democracy" | Applying criteria | Criteria wrong or misapplied |
| Interpretive | "The speech was a call to action" | Hermeneutic evidence | Alternative interpretations |
| Normative | "We should increase turnout" | Values, principles | Competing values |

## Convergent Dimensions

Across these frameworks, certain dimensions recur independently:

### 1. Truth / Ontological Standing

How well does this claim correspond to reality?

Appears in: Habermas (truth), alethic modality (necessity/possibility),
Bayesian credence, Pollock (rebutting defeaters target this), Toulmin
(data challenges target this), T-Box/A-Box (A-Box claims have contingent
truth values).

Range: 0 (false) to 1 (true). Applies primarily to descriptive/empirical
claims. For stipulative claims (definitions, conventions), truth is 1 by
construction — the axis becomes irrelevant rather than contested.

### 2. Certainty / Epistemic Confidence

How confident is the knower in their assessment?

Appears in: Bayesian credence + higher-order credence, Toulmin (qualifier),
epistemic modality, AGM (entrenchment ordering).

Range: 0 (no basis) to 1 (absolute certainty). Independent of truth —
one can be highly certain about a low-probability assessment. Weight of
evidence and resilience (Bayesian) are related but potentially derivable
dimensions.

### 3. Normativity / Direction of Fit

Is this about what IS or what OUGHT to be?

Appears in: Searle (direction of fit), Hume's guillotine, deontic vs
epistemic modality, Habermas (truth vs rightness), Levine (descriptive
vs normative), T-Box constraints.

This is the most structurally significant dimension because it determines
which **class** of challenge is valid. Descriptive claims are challenged
by counter-evidence. Normative claims are challenged by competing values.
Crossing the boundary (challenging an OUGHT with an IS) is a category
error.

### 4. Analytic / Basis

Is this claim true by definition or by contingent fact?

Appears in: T-Box vs A-Box, Levine (conceptual vs descriptive), the
a priori / a posteriori distinction, Walton (different schemes for
definitional vs empirical claims).

Correlated with normativity (definitions are stipulative, hence normative)
but independent — mathematical truths are analytic but descriptive;
empirically-grounded recommendations are synthetic but normative.

## Challenge Modes: A Synthesis

The frameworks converge on a compact set of challenge types:

| Challenge mode | What it targets | Primary frameworks |
|----------------|----------------|--------------------|
| Rebuttal | The claim's truth value directly | Pollock, Toulmin (counter-claim) |
| Undercutting | The evidence-to-claim link | Pollock, Toulmin (warrant challenge) |
| Definitional | Conceptual fitness of terms | T-Box revision, Levine |
| Normative reframing | The values underlying a prescription | Hume, deontic logic, Habermas |
| Scope/qualifier | The claim overstates its reach | Toulmin (qualifier), Walton |
| Authority | The speaker's standing to claim | Searle (declarations), Walton |
| Sincerity | Whether speaker actually holds position | Habermas, Searle |

Pollock's rebuttal and undercutting may unify into a single "correctness"
challenge whose character varies with the claim's basis — rebuttal
dominates for empirical claims, undercutting for inferential claims. This
is consistent with the observation that few claims are equally vulnerable
to both; most cluster at the empirical or inferential end.

## Key Relationships Between Dimensions and Challenges

The central finding across frameworks: **a claim's position on the
dimension axes determines its vulnerability profile.** Different regions
of the dimension space afford different challenge modes:

- High truth-relevance, low normativity → correctness challenges (rebuttal/undercutting)
- High normativity, low truth-relevance → utility challenges (normative reframing)
- High analytic → definitional challenges (conceptual fitness)
- Any position → scope challenges (qualifier/overstating)

This means the "type" of a claim (observation, inference, definition,
prescription) need not be stored explicitly. It is determined by the
claim's coordinates on the continuous axes, and the valid challenge modes
follow from those coordinates.

## References

- Alchourrón, Gärdenfors, Makinson. "On the Logic of Theory Change." *Journal of Symbolic Logic* 50(2), 1985.
- Habermas, Jürgen. *The Theory of Communicative Action.* 1981.
- Joyce, James. "A Defense of Imprecise Credences." *Philosophical Perspectives* 24(1), 2010.
- Levine, Peter. "Six Types of Claim." peterlevine.ws, 2016.
- Pollock, John. *Contemporary Theories of Knowledge.* 1986.
- Searle, John. "A Taxonomy of Illocutionary Acts." *Minnesota Studies in Philosophy of Science* 7, 1975.
- Toulmin, Stephen. *The Uses of Argument.* 1958.
- van Eemeren, Frans & Grootendorst, Rob. *A Systematic Theory of Argumentation.* 2004.
- Walton, Douglas, Reed, Chris & Macagno, Fabrizio. *Argumentation Schemes.* 2008.
