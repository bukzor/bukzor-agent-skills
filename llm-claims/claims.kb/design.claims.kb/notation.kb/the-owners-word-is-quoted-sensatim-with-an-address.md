---
label: VOICE
standing: agent
authority: >-
  @bukzor 2026-09-09, f9bdf6f0#L109, proposed the callout; the address
  requirement and the single agent form are the agent's additions, veto
  invited; the fidelity standard is the owner's, a29c9a99
why:
  - the-sigil-signs-the-judge.md
  - agent-fiat-gets-its-own-sigil.md
  - ../ownership.md
---

# The Owner's Word Is Quoted *Sensatim*, With an Address

In prose, the owner's voice takes one form: a `> [!@bukzor] <address>`
callout quoting the owner *sensatim* at that address -- the words as
typed, silently emended only where they would now mislead. A typo, and
a label renamed since, are the standing instances and not the
definition: the test is whether the unmended token would transmit
something the owner did not send, and it is the reader's test, not the
editor's. What no emendation licenses is paraphrase. An agent's
composition in prose -- a paraphrase, a derivation, law elicited from
the owner's answers -- takes one form, `> [!DRAFT] <address>`, and names
the `[!@bukzor]` spans it derives from: the proposal and what would
overturn it, its route only where the veto turns on it. An address is a transcript
record (`<session>#L<n>`) or a commit the owner authored. Nothing else
in a body speaks for the owner. The address is what lets a reader check
an emendation against the record.

> [!@bukzor] f9bdf6f0#L109
> That's partly wrong in spirit, partly wrong in word. In spirit, I want
> agent to _discuss_ with me and _elicit_ law in my voice. In word, a
> transcription of what I said _should_ be "in my voice". I here propose
> standardizing a `> [!@bukzor]` markdown callout for delimiting such
> sections. We've used this as a convention several places but I don't
> think it's recorded as a special form anywhere it would/could be used
> for that purpose.

The sigil signs the judge on a claim (the-sigil-signs-the-judge.md),
but a body carries quotations and paraphrases with no judge named, and
that is where attribution fails. Three sessions in the 2026-08-29
window credited the owner with sentences an agent wrote; the sitting
that proposed this claim carried an agent's "the collection dissolves"
as the owner's verdict. The failing case is never a missing marker.
The digest that was misread had every role labeled. Paraphrase drops
the label, and only a span with an address survives paraphrase,
because a checker can then confirm the span sits at that record with
the owner's role -- the quote half of `claude-code-holistics/verify.py`
already does this for digests. The marker is for the reader; the
address is what makes the marker true.

The standard is borrowed; only the word for it is new. Textual editing
calls the act **silent emendation**, and splits a text into
*accidentals* -- spelling, pointing, the token -- against
*substantives*, the readings that carry the author's meaning: an editor
may regularize the first and never the second. Law states it as a negative, *no material change*, and prices
the gap as *immaterial variance*, a departure between what was said and
what is reported that does not touch the substance. Latin marks the two
ends of the axis: *ipsissima verba*, the very words, against *ipsissima
vox*, the very voice. This claim sits on the vox side and close to its
edge -- the meaning is held, and the only wording freedom is repair.

*Sensatim* is a coinage, minted here and not found in the lexica, on the
model of *verbatim* and the authority of Jerome's rule for translators
(*Ep.* 57): *non verbum e verbo, sed sensum de sensu* -- not word from
word, but sense from sense. The `-atim` suffix is distributive, which is
the point: it names the unit at which fidelity is owed, word by word or
sense by sense. Two shapes stand nearby and mean other things: *sensim*
is attested and means "gradually", and late Latin's *sensatus*
("sensible") is why a Romance ear may hear "sensibly" -- neither
survives the contrast with *verbatim*, which is the only place the word
is ever used.
The word is wanted because English has no positive term for the
relation: only negations (*no material change*) and phrases (*in
substance*, *to the same effect*).

The first sentence of this claim is the word's definition, and the only
one anywhere. A use too far from it to read it writes *sensatim*
(rather than verbatim), which carries the contrast that is the whole
content, and cites this claim for the rest.

What was in the wild before this claim, counted across `~/repo` and
`~/.claude` outside trash: `[!@bukzor]` 272, `[!@claude]` 49,
`[!FABLE]` 1074, `[!DRAFT]` 523 -- two axes, who and status, and the
agent's voice in three spellings. One file already carried provenance on
the title line, `> [!@bukzor] (keeper-transcribed from the 2026-08-25
sitting chat)`; this claim makes that the rule and gives it a checkable
form.

Why the agent form is `[!DRAFT]` and not a who-shaped twin:

- `[!DRAFT]` says what the reader must do, veto or ratify, which is
  what `+` asks (agent-fiat-gets-its-own-sigil.md), and it is the word
  the standing law itself uses ("enters as a draft marked
  agent-authored and vetoable").
- which agent wrote it is provenance, and provenance lives in the
  address: the session names the model.
- `[!@claude]` and `[!FABLE]` are retired spellings; a sweep is a
  rename, not a re-signing.

Declined:

- **A trailing attribution line** (`> -- @bukzor, <address>`): standard
  markdown practice, but the reader learns whose voice it was after
  reading it, and a checker has to find the last line of the quote.
- **`standing: user` and `authority:` alone**: per file, not per span,
  and `authority:` is exactly the field agents were filling from memory
  of who typed what. Both stay; a `standing: user` claim's `authority:`
  now carries an address or points at the body's callout.
- **A fenced block with an info string** (` ```quote @bukzor `): the most
  machine-readable form, and it renders as code, which prose is not.
- **A reference-style link definition** for the address: markdown-native
  and one definition serves every use, but a second place to look; the
  title line already has room.

Known collision: `L109` is label-shaped, so `llm-claims-kb-mentions`
reports every `#L<n>` address as an unresolved citation. Two honest
repairs, neither taken here: the scanner exempts a callout's title line,
or the address form becomes `<session>:<n>`, which is what `grep -n`
prints and is not label-shaped. The first keeps the form the digests,
the review, and GitHub's own line anchors already use; the second costs
the tool nothing.

Cost: an address per quotation. Words the owner typed where no
transcript exists -- an editor, a chat outside Claude Code -- have a
commit or nothing; with nothing, the callout still carries who
transcribed it and when, in the pre-existing form, and the gate cannot
check it. That is the honest residue, not a second rule.

Renders everywhere: GitHub styles only its five fixed callout types, and
any other type degrades to a blockquote showing the literal marker,
which is the point.

> [!@bukzor] dfc18e9d
> I think it's less-incoherent to retcon the verbatim quotes than to say those aren't labels.
> Please hold "user, verbatim" slightly more lightly. I care much more about the meaning than the words.

> [!@bukzor] a29c9a99
> I want "user authority" to have this kind of property. *meaning* held
> tightly, but *wording* held more loosely.
> [...] that's an enumeration where we have no certainty it's exhaustive.
> Instead, name the category.
> [...] sensatim, as in sensum de sensu, as distinct from verbatim, as in
> verbum e verbo

> [!DRAFT] a29c9a99
> The standard is a condition, not a synonym for "verbatim": an
> enumeration of licensed edits cannot be shown exhaustive, and a test
> can. So a checker compares the span's sense against the record rather
> than its bytes, and has an answer for edits nobody enumerated.

Not built: a checker that walks every `[!@bukzor]` in a ledger to its
address and role. `verify.py` in `claude-code-holistics` is the
prototype; generalizing it is a work item, not a condition of this
claim.
