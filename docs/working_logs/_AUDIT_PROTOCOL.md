# The deep audit protocol — one file at a time

*The standard set by the Fairbank pass (2026-07-19). A file is not "audited" until every check below
has been run against it. Three files a day at this depth beats thirty at a skim, because the defects
that matter are the ones a hostile reader finds, and they do not surface from reading quickly.*

## Why one file at a time

The batch passes caught formatting, jargon, and stale numbers. They did not catch:

- a letter contradicting its own headline four sections later
- a registry entry that did not say what the file citing it claimed
- a number quoted at two different stages of the same calculation, in the same document
- the model's own annotation calling a headline claim non-distinctive, while the audience-facing
  file sold it as distinctive
- two anchors mixed inside one derivation, overstating a floor by 2×

Every one of those needs the *whole* file in view at once, plus its sources. None of them survive a
three-file sweep, and all of them are the kind a referee opens with.

## The checks

**Numbered entries 1–38, plus six lettered sub-entries (2a, 9a, 15a, 27d, 33a, 36a) — 44 in all.**
Run every one. Record what was found, even when nothing was.

*The count is written this way deliberately. A bare "the forty checks" went stale three times in a
single day (2026-07-28) as entries were added, which is check 9a's own defect occurring in the file
that documents it. **Stating the range and the sub-entries separately makes the heading verifiable by
`grep -cE '^\*\*[0-9]+\.'` rather than by memory** — and a count nobody can check is a count that
will be wrong.*

*(This line read "run all thirty-three" while the heading above said thirty-seven — the exact
stale-cardinality defect check 9a describes, sitting in the file that describes it. Caught
2026-07-28 while adding check 35. The lesson generalises: the count-word most likely to rot is the
one nearest the list you just extended.)*

*Checks 1–13 came from the 2026-07-19 Fairbank pass and the deep audit. **Checks 14–19 were
added 2026-07-20**, each from a defect that survived all thirteen — which is the point of
recording them: every one was found by a person reading, and none would have been caught by
the checks that existed that morning. **Checks 22–25 were added 2026-07-28**: 22 from
audience-facing prose that passed every terminology check and still read as narrative; 23 from
two sectors whose numbers each passed alone and failed jointly; 23a from an absence claim that
searched the working tree and not the history; 24 from a posterior interval read at R−1 = 93 and
used for a year as a measurement; 25 from a capability probe that reported a thread budget
instead of a core count, which sent a wrong recommendation to the owner; and 26 from a `pkill -f`
that matched its own shell and took six freshly-launched MPI ranks with it. **Checks 27–30 were
added the same day**: 27 and its sub-entries from a ratio matched in the wrong direction and an
over-correction that withdrew a correct result; 28 from 23 harness checks that could not fail; 29
from two frames whose disagreement turned out to be a physical delivery law rather than a
convention; and 30 from a degeneracy that was lifted without fixing the parameter it was lifted
for. **27c and 31 closed the same day**: 27c from a cumulative acceptance rate misread as a current
one, which nearly reversed a correct ruling on the production chains; and 31 from seven open items
worked in one session of which **none was solved** — every one already paid, duplicated, superseded,
moot or misclassified, which is a fact about how a debt-recording corpus behaves rather than about
that session.*

**1. Read it whole, line by line.** Not grep. The contradictions live between sections.

**2. Recompute every number** from its own inputs. Where a closed form exists, add it to
`scripts/audit_math_pass.py` so it can never silently rot.

> **2a. Before reporting that a number fails to reproduce, grep the harness for it.** On 2026-07-20 a
> pass "found" that the corpus's Σm_ν = 61.4 meV did not follow from its splittings and that the kill
> margin was half what was claimed. It was the auditor's splittings that were wrong, and the harness
> had the sum guarded three ways — the value, two anchor variations, and the normal-ordering minimum.
> Four replacement checks were then written *on top of* the existing ones and all four passed,
> because they tested the auditor's arithmetic rather than the corpus's claim. **A check that books
> the auditor's own value is worse than no check**: it converts an error into a guard that will
> defend it. The wrong claim reached four files, including a referee decision rule.
>
> Two rules follow. Grep first — the harness is 328 closed forms and costs one command. And when
> adding a check, **read the neighbouring checks for the same quantity before writing a new one**;
> if the quantity is already guarded, the job is to reconcile with it, not to add a second opinion.

**3. Grade every claim's status.** Derived, assumed, data-selected, or fitted — and does the file
say which? "Derived" covering an assumed input is the most common defect in this corpus.

**4. Internal consistency.** Does §7 contradict §2? Is the same quantity quoted at two stages of one
calculation without saying so?

**5. External consistency.** Does it agree with the registry, the ledger, and every file it cites?
Where it disagrees, which one is right — and is the other one stale or wrong?

**6. Citations.** Does every referenced source exist, is it in `BIBLIOGRAPHY.md`, and does it say
what the file claims? A number attributed to the literature is the fastest way to lose a reader.

**7. Staleness.** Was something fixed elsewhere that this file still carries in its old form?
Especially: values re-derived, mechanisms retired, kills reversed.

**8. Audience laws.** No process narration, no amendment tags, no deuterium rows, no announcing its own
honesty. A document that keeps pointing at its integrity reads anxious; one that states limitations
in the same tone as results reads honest.

**9. Is the confidence earned?** For each strong claim: could a competent hostile reader knock it
down with one question? If yes, either strengthen it or state the limit first.

> **9a. Read the headings and lead sentences alone, against what the sections beneath them
> establish.** This is the corpus's most repeated defect and it has its own signature: the
> qualification is present and honest, and it arrives after the sentence a skimming reader would
> quote. On 2026-07-19/20 it was found five times — `information_paradox` line 8 against line 60;
> `cosmic_magnetism`'s DETERMINED SIGN against T14's open link; hierarchy **§6c's heading** claiming
> what its own three conditions withdraw; **§6e's heading** ("Why the two bands screen equally")
> against a body saying nothing supplies that match; and `igmf_helicity` **§1** asserting the
> parity-lock that the same file's later sections show is unestablished. **Placement is a correctness
> property when the claim is bold and the caveat is prose.**
>
> Headings are the worst case and the cheapest fix. They are what a referee quotes, they are written
> before the section's conclusion is known, and they are edited least often because the body is where
> the work happens. **When a section's finding changes, re-read its heading** — nothing else in the
> file is as likely to be left behind, and a heading that survives its own refutation reads as a
> claim the corpus still makes.
>
> **The commonest way to create this defect is to add an item to a list.** Every count-reference to
> that list — "the three conditions below", "all three fail", "three requirements met" — goes stale
> the instant a fourth appears, and counts are exactly what nobody re-greps. On 2026-07-20 adding one
> condition to hierarchy §6c invalidated its own lead sentence *and* a cross-reference three
> paragraphs above, both written by the same hand in the same hour. **After adding to or removing
> from any enumerated list, re-read the paragraph that introduces it and grep the file for its
> cardinality words.**
>
> **That was first written here as "the one instance of this defect that is fully mechanical to
> catch". It is not, and the correction is worth more than the claim was.** A sweep was built the
> same hour — find ordered lists, take their length, compare against count-words in the six lines
> above. Across 141 live files it returned two hits and **both were false**: hierarchy §6c, where the
> scanner broke on a display equation inside item 3 and undercounted a correct list; and
> `white_holes`, where "holds **two** outright and deviates from **two**" counts subsets of a
> correctly-introduced list of four. Zero true positives.
>
> So this check fails to mechanize for the same reason 9a does, and the reason is worth stating once:
> **count-words in prose refer to many things, and list boundaries in markdown carrying mathematics
> do not parse reliably.** Both attempts produced instruments whose output needed a human read to
> triage, which is the work the instrument was supposed to save. Read the paragraph. Do not build the
> third sweep.
>
> **Do not try to automate this. It was tried on 2026-07-20 and it does not work.** A sweep for
> assertive headings sitting over bodies that hedge repeatedly returned 31 candidates, and the two
> strongest were the corpus's *best-behaved* sections: `koide_relation` §2, whose heading carries an
> inline "honest status" and whose first body line is "Koide is one derived number away, modulo one
> linkage that is not built"; and `quantum_gravity` §4a, which derives S = A/4G and then bounds it
> under "What the medium contributes, and what it does not". Both were flagged **because** they hedge
> honestly, which is the same textual signature as hedging late. The discriminator is whether the
> caveat arrives before or after the sentence a skimmer would quote — an ordering judgement, not a
> string. All five real instances were found by reading the file. **This check is a read, and pattern
> matching on it produces false positives at a rate that will bury the real ones.**

**10. Is the distinctive content actually distinctive?** A prediction indistinguishable from the
generic expectation is not a prediction. Check the separation against the resolution of whatever
would measure it.

**11. Would this survive the reader it is written for?** Name that reader. Then read it as them.

**12. Re-read the file whole, after the edits.** Not a grep — a read. The edits are the newest and
least-tested prose in the document, and they are written while holding one defect in mind rather
than the whole file. This has already caught a repair that dangled and contradicted itself in the
same sentence (`blackholes_no_singularity`, 2026-07-19), which no pattern sweep would have found.

**13. Work the file's own owed items.** An "owed", "un-run", "underived" or "queued as a named
computation" is a **work order, not a label**. Before closing a file, take each one and either
compute it, show it reduces to something already recorded, or state precisely what it is gated on
and why that gate is real. A file that has been made internally consistent but still carries the
same blanks it started with is tidier, not more complete — and the goal is derived and model-backed,
not well-formatted.

The honest outcomes are: **closed** (computed, with the number and its check), **reduced** (it turns
out to follow from something already in hand), **gated** (named the specific external thing it waits
on — a run, a lattice number, a measurement), or **docketed** (real desk work with no gate — it gets
a task number, and the file names it). "Owed" on its own is none of those.

**The fourth outcome is the one that leaks.** Work that is neither closed nor gated has nowhere to go
without it, so it stays as the bare word and reads, indefinitely, as though someone were on it. The
2026-07-19 sweep found the shape of the leak: `hierarchy_problem` carried "the gap equation's k
(owed)" three paragraphs above three concordant determinations of that same k — a debt already paid —
while the file's *real* debt, that no pairing kernel was ever specified and no gap equation ever
solved in the medium, was named nowhere at all. Eight further undocketed items came out of the same
sweep. Both failures are check 13 not being run: the first dies on "is this actually still owed?",
the second on "what does this file owe that it has not said out loud?"

**14. THE DEAD PREMISE UNDER A LIVE CONCLUSION (2026-07-20 — the day's most expensive class).**
When a claim is checked, the check almost always lands on its *number*. If the number is right the
claim is passed, and its *reason* is never re-read. So a premise can die and its conclusion keep
certifying it, indefinitely. On 2026-07-20 one retired identity leg — "Ψ carries L, so |Ψ|² carries
L = 0; U(1)_L screens nothing" — was still asserted in **eight** forward files a day after its
retirement, including the red-team brief, which was actively telling adversaries not to attack the
corpus's weakest premise. Every conclusion survived with four orders to spare; only the reason had
died. **The check: when a premise is retired, grep the CONCLUSIONS it supported, not the premise's
own wording** — the conclusions are what survived, and they are load-bearing. The harness cannot
see this class at all: every arithmetic check passes.

**14a. A suppression is not a symmetry.** The same episode's tell: a claim filed under *principled
silence* whose surviving support was a two-loop *number*. A number can be reopened by better data;
a symmetry cannot. When a symmetry argument dies and a numerical one survives, the claim must move
categories, not just change wording.

**15. ABSENCE INFERRED FROM A SEARCH THAT COULD NOT HAVE FOUND IT.** Committed at least four times
in one day by the main session: searching `nine grips` when the corpus said **NINTH GRIP**;
`input rather than` when the doc said **an input**; `c = 0.789262` when the file wrote **c = 0.789**;
and a `grep -lv` count that listed every file because *some* line always fails to match. Each time
the conclusion was "it is missing" and each time it was present. **The rule: before booking anything
ABSENT, search on three distinct phrasings plus one distinctive number, and state which forms you
tried.** A negative result is a claim about your search, not about the corpus, until you have shown
otherwise. (This is check 2a's mirror and it fires far more often.)

> **15a. AN ABSENCE CLAIM SILENTLY EXPIRES, AND NOTHING RE-READS IT (2026-07-28).** Check 15 is
> about searches that could not have found the thing. This is the opposite and it is more common:
> the search was *fine* and the claim was *true when written* — and then someone built the missing
> object, and the sentence asserting its absence sat there aging into a falsehood. A claim of
> absence is the only kind of claim that can be invalidated by work the corpus itself does, without
> anyone touching the sentence.
>
> A sweep on 2026-07-28 found four live ones, and three had been true at the minute they were
> written. `igmf_helicity` said "no script, notebook or C source in the corpus holds a
> three-dimensional genesis flow field" — `scripts/ring_toroidal_3d.py` had been committed **six
> hours before that file was last edited**. The same file said "the corpus has no source for the
> other [poloidal] factor" while `ring_rollup_poloidal_v3.py` had already returned five rings with
> five correct signs. The failures ledger said of a Δτ integral "no such number exists anywhere in
> the corpus"; the integral was run and committed **32 minutes later**, and the row was never
> revisited. In every case the *working log* was updated and the *forward-facing file* was not.
>
> **The rule: when a script, run or number lands, grep the corpus for claims that it does not
> exist** — `no script`, `nowhere`, `not retained`, `no source`, `never`, `no such`, `exists
> nowhere` — before closing the session that produced it. An absence claim is a perishable
> statement about the corpus's own contents, and the thing most likely to falsify it is the next
> commit. Treat "nothing computes X" as carrying an implicit expiry date, and make the commit that
> computes X responsible for finding it.

**16. THE FAVOURABLE ARGUMENT WHERE AN INTEGRAL WAS OWED.** The vertex correction (#141) was
attempted twice and retracted twice; both attempts were verbal arguments, and **both happened to
point the favourable way**. The integral, when finally run, confirmed the adverse prior. **The rule
the hierarchy file already states, generalised: where a well-posed calculation exists, an argument
about its sign is not evidence — and an argument that lands favourably should be treated as wrong
until the calculation says otherwise.** Two for two is not a coincidence worth a third trial.

**17. AN UNPINNED INPUT QUOTED AT ITS FAVOURABLE END.** Baryogenesis recorded "a factor 122: AT the
pre-committed 10² acceptance boundary, neither inside nor past it" — true only at the top of a range
that nothing pins. `L_gen` is never assigned a value anywhere in the corpus; at the torus floor the
same η needs a target 6–18× larger and the row lands well past its boundary (#180). **The check: for
every verdict stated as "at the boundary" or "just inside", ask which end of which range it was
evaluated at, and whether that range has a booked lower bound.**

**18. A NAME THAT CARRIES UNITS THE QUANTITY DOES NOT.** `scripts/de_value_g_to_lambda.py` computes
a variable named `f_over_root_sigma` which is algebraically **f/Λ** — the decay constant in units of
an NJL regulator, not of a string tension. Λ = √σ was inherited, never derived, and two scripts made
two different physical statements about the same 511 keV while silently identifying them. The result
was a phantom 2.39× "two routes disagree" that dissolved on inspection (#134). **The check: for any
ratio quoted across sectors, confirm the denominator is the same object in both — the variable name
is not evidence.** The tell was already printing: the script compared its own output to a band and
landed below it.

**19. THE RECORDED BAND AND THE RECORDED RANGE WERE NEVER THE SAME COMPUTATION.** The exact-kernel
T_c band was recorded as 250–530 keV over L−1 ∈ [1, 10]; recomputing from the same kernel gives
307–714 keV, and 250–530 corresponds to L−1 ∈ [0.50, 4.78] (#182). No script reproduced the booked
pair, and the audit pass was still checking a superseded route. **The check: where a band is quoted
beside the range it was swept over, re-run one endpoint.** A band and its stated domain drifting
apart is invisible to every consistency check that reads only one of them.

**20. DO NOT FORCE A FINDING. Verify the defect before naming it (owner ruling, 2026-07-20).**
An audit that must produce findings will produce them, and a manufactured defect costs more than a
missed one: it burns the reader's trust in every real finding beside it, and it sends someone to
"fix" correct work. **Backtrack the suspected issue and confirm it is an issue before claiming it.**

The failure has a signature — a suspicion arriving from a *search* rather than from *reading*. Four
times on 2026-07-20 the main session was one command from announcing a defect that did not exist:
"29 of 29 files quote +0.44% without the caveat" (a `grep -lv` artifact — the test listed every
file); "the crossed-box result never landed in hierarchy_problem" (the file wrote **c = 0.789**, not
the full `0.789262`); "the Z₄ result never propagated" (the doc said **an input**, not the phrase
searched for); and a near-miss on `cosmological_constant`'s headline, which states +0.44% bare and
was about to be "corrected" — until reading the next line showed it is a *τ-space* statement where
0.44% is exact arithmetic between two candidate τ values and needs no control caveat.

Each was caught by opening the file. None would have been caught by refining the search.

**The rule, in order:** (i) reproduce the suspicion by *reading the passage whole*, not by re-running
a pattern; (ii) establish what the passage is actually claiming — a statement about τ-space is not a
statement about ρ_Λ¼, and a bound is not a determination; (iii) find the canonical value and its
provenance (see `docs/working_logs/_CANONICAL_VALUES.md`) rather than assuming the first carrier you
met is right; (iv) only then name it. **"Clean" is a result.** Report it plainly and often. Two
mechanization attempts in this protocol's own history — the cardinality sweep and the
assertive-heading sweep — returned *only* false positives across 141 files, and both were retracted;
that is the shape of a forced finding at scale.

**20a. A disagreement between two files is not yet a defect.** It is a question with three possible
answers: the first is wrong, the second is wrong, or they are about different objects. On
2026-07-20 the last was the answer twice — a 2.39× "two routes disagree" that was a units error
between f/Λ and f/√σ (#134), and a T_c "conflict" where the two scales turned out to be two
genuinely different objects (#182). **Establish which of the three before writing either one down as
wrong.**

**THE RETIREMENT→TASK JOIN (mechanized 2026-07-20, docket #172).** A retirement kills content, and
that content usually belongs to a task. Commits already carry their task number; retirement rows did
not — which is how #59 sat marked complete straight across its own retraction. Nothing pointed from
the kill back to the task whose object had just died, so nothing prompted a re-grade.

This is now a commit-gate check rather than a habit, on the same footing as the naming and husk
laws: a **newly added** row in the failures ledger carrying RETIRED must either name the task it
kills (`#N`) or rule itself clear (`(no docket)`). Silence is the only disallowed answer. The
existing ledger is deliberately not retrofitted by the gate — the check binds what is being written
now, so it costs nothing to adopt and cannot be satisfied by leaving the row vague. Verified in both
directions before adoption: an unjoined row exits 1, a joined row exits 0.

**Propagation runs in both directions.** A result is not filed until the files inheriting it are
updated *in the same commit* — and the same applies when a claim is **withdrawn**. A retraction
creates propagation debt retroactively: the carrying files looked correct when they were written and
became wrong hours later, so nothing prompts a re-check. On 2026-07-19 a single withdrawal left six
files asserting an unqualified claim its home file had already retracted. **When a claim is
withdrawn, re-run its propagation list, not just its home file.**

**Two joins the corpus lacks, both found by the 2026-07-19/20 reverse audit and both one line to
fix.** *(i)* **A retirement should name the task it kills.** The failures ledger records kills
correctly and the board never hears: #59 sat closed for days on content the ledger had retired the
next day as a category error. A retirement entry carrying the task number whose content it kills —
exactly as commits already carry task numbers — closes that gap. *(ii)* **A withdrawal should
enumerate its inheriting files in the commit that makes it.** Recall is what failed: three
withdrawals were filed on 2026-07-19 and one was propagated, by the pass named for propagating them.

**And one habit at task-creation, which is where the defect actually originates.** Ten of the ten
mis-grades that audit found were *composite* — "A + B + C" queues or "every X" sweeps — and not one
single-object task failed in roughly a hundred checks. #28 and #29 are the same three-part shape with
opposite outcomes; the only difference is whether all the parts happened to land. **Do not bundle
deliverables under one number, and give any "every X" task a named completion test when it is
written.** An audit after the fact costs a day; the discipline costs a sentence.

**21. PROPAGATE FROM THE SOURCE, NEVER FROM THE DISPLAY (2026-07-20 — caught in the act).** A
number quoted to two significant figures is a *rendering* of a number the corpus holds to more. When
a new factor multiplies through, it must multiply the quantity, not its rendering — otherwise the
display's rounding is promoted to a real digit and compounds with every further step. Checking a
subagent's Fock-insertion band, I multiplied the booked display **0.73–2.4 TeV** by e^(−a) = 0.7553,
got an upper edge of **1.81**, and was one keystroke from filing the agent's **1.78** as an error.
The agent was right: the band's source is **1.6–5.2 TeV**, and 5.2 × e^(−(c+a)) = **1.784**. The
2.4 was itself 2.362 rounded, and my arithmetic inherited that 1.6% and called it a discrepancy.

The rule: **before propagating a quoted number, find where it was computed and take the value from
there.** If the source cannot be found, that is the finding — a number with no computable origin is
check 15's problem, not a rounding question. And the tell that this has happened is specific and
recognizable: a mismatch of **one to two percent** against a value someone else derived, sitting on a
quantity that has passed through two or more multiplications. That size is too large for float error
and too small for a real disagreement. It is almost always a display in the chain.

Note which direction this cuts. The failure here would not have been a wrong number in a file — it
would have been **a correct number overwritten with a wrong one**, and filed as a fix. Check 20 says
do not force a finding; this is the arithmetic case of it, and it is the more dangerous one, because
the forcing looks like diligence right up until the source band is read.

**A process rule that has now failed twice, in two different disguises: NEVER PIPE THE GATE.**
`scripts/check_before_commit.sh` signals failure through its **exit code**. Both of these commit
over a red gate:

    bash scripts/check_before_commit.sh; git commit ...              # separate statements
    bash scripts/check_before_commit.sh | tail -3 && git commit ...  # tail's exit code, not the gate's

The second is the nastier one, because it *looks* correct — the `&&` is right there, and the
terminal even prints "REFUSING TO COMMIT" immediately above a successful commit. A pipeline's status
is its **last** command's, and `tail` always succeeds. The only safe form is the gate as its own
unpiped command:

    bash scripts/check_before_commit.sh && git add <explicit paths> && git commit ...

If the output is too long, redirect to a file and grep the file *afterwards* — never in the pipeline
that guards the commit.

**22. REGISTER, NOT JUST VOCABULARY — the forward-facing prose test (owner ruling, 2026-07-28).**
The de-jargon rule swaps house codenames for field terms. It does not catch prose that has the
right *words* in the wrong *register*: narrative sentences in an audience file read, in the owner's
words, like "story letters to people we want to take this seriously." The rule is separate from
check 3 and has to be run separately, because a paragraph can pass every terminology check and
still be unpublishable.

The tells, all taken from audience-facing prose written the day this check was added:

| tell | example written | field-physics form |
|---|---|---|
| anthropomorphic verb | "an overdamped phase does not **feel** a mass" | "the pinning enters as the relaxation rate" |
| dramatic verb | "**destroys** the asymmetry", "begins to **bite**" | "suppresses", "exceeds the threshold" |
| house verb | the limit "**rides**" the steepness; the coupling "**shakes**" the phase | "is set by the gradient"; "drives" |
| narrative heading | "**What the averaging returns.**" | "**Second-order averaging.**" |
| story connective | "**So** the transmission … fixes one number" | state the result directly |
| prose numerals | "**seventeen orders** under" | "a factor 10⁻¹⁷ below" |
| emphasis as argument | italics carrying the persuasion | let the number carry it |

**The positive form, and the test to apply:** display the equation, define every symbol, give the
verification tolerance and the range checked, state the regime of validity, state the required
value and the kill condition. **A referee must be able to extract the claim, its inputs and its
falsifier without reading a single adjective.** If a sentence survives deleting all its adjectives
and adverbs with its physics intact, it passes; if it collapses, it was carrying argument in the
wrong place.

**23. AN OVER-DETERMINED SET MUST BE CLOSED, NOT MERELY EACH MEMBER GUARDED (2026-07-28 — found
twice in one day, in unrelated sectors).** Wherever a section records more numbers than it has
independent unknowns, the surplus is a free consistency test, and a harness that checks each
number against its own source cannot see it. Two instances, both invisible for months:

- **The Koide watches.** A = √2 and arg f₁ = 2/9 were each tested against m_τ and each sat under
  1σ. Together they leave the ring only its overall scale, so they also fix m_μ/m_e — a ratio
  known to 22 ppb — where they miss by 9.8 ppm, or **452σ**. Every individual check passed.
- **The junction rectifier.** ω_J ≈ 5.7 keV, j = ω_J²/Γ_φ ≈ 6 meV, Γ_φ/θ̇ ≈ 10⁷ and the needed
  R = ω_J²/(2Γ_φθ̇) ≈ 5×10⁻⁵ are four numbers over three unknowns. Substituting Γ_φ collapses R
  to j/(2θ̇), and the set misses closure by **a factor 9**. Which input carries it is undetermined.

The harness already contains the correct pattern, in one place: `chk("sqrt3_derivation", "B =
omega_J/Gamma_par = 1/sqrt(2)", 0.7071, math.sqrt(1.5)/math.sqrt(3))` **computes** the surplus
member from the other two rather than booking it separately. That line would have caught either
defect above had it been written for those sectors.

**27b. AN OVER-CORRECTION IS A DEFECT, AND TWO RECORDED FRAMES MAKE ONE INEVITABLE
(2026-07-28).** A kernel sweep returned k_singlet/k_doublet = 2 and was matched to the ring-on-ring
condition. A later pass judged it against T6's √m-field convention — where the null reads
ε_charged = 2ε_neutral, the inverse — and **withdrew a correct result**. The corpus states the
ring-on-ring frame outright ("the singlet is twice as stiff"), so the original match was right and
the withdrawal was the error.

Both slips have one cause: **two frames for one condition, with the bridge unstated.** The
canonical normalizations R_c = √(3/2)R, M_c = √3M relate them and no file writes that down.

**The check: when two frames for one condition are on the books, neither is "the" convention.**
Before withdrawing a result for disagreeing with a recorded statement, confirm the statement is in
the same frame — and if the bridge between frames is unwritten, record *that* as the defect rather
than adjudicating between them. Withdrawing correct work costs as much as asserting wrong work,
and it is harder to notice because it looks like rigour.

**27a. AND A QUANTITY IS NOT ITS DIMENSION-MATE — CHECK WHAT THE BOUND CONSTRAINS
(2026-07-28, the same day, by the same hand, after writing 27).** Having just written check 27
about matching ratios without checking their variables, I compared ω₁ = μ_face against the
Maldacena–Shenker–Stanford chaos bound and reported a route closed at 28×. **μ_face is a chemical
potential**; the MSS bound constrains a *scrambling rate*; the pacing bound constrains a *hop
rate*. In natural units all three are "keV", which is exactly why the error survived a numerical
check — the arithmetic was right and the objects were not the same kind of thing.

**The check: before comparing a quantity to a bound, name what the bound constrains and confirm
the quantity is that.** Natural units erase the dimensional guard-rail that would catch this in SI,
so in ħ = c = k_B = 1 the discipline has to be manual. Writing check 27 did not prevent 27a, which
is the honest lesson: a protocol entry protects against the instance you wrote it from, and the
class is wider than the instance.

**27. A RATIO IS NOT A NUMBER — CHECK ITS VARIABLES AND ITS DIRECTION BEFORE MATCHING IT
(2026-07-28).** A kernel sweep returned singlet:doublet = 2 on a three-defect ring and was reported
as delivering "the 2:1 the R_c = M_c condition names". It does not. The condition's own convention
(T6) is ε_charged = 2·ε_neutral on the **√m fluctuation field** — the *charged* modes twice as
stiff — while the sweep was in **radial displacements**, where its 2 is the *neutral* mode twice as
stiff. Same number, opposite direction.

*The diagnosis in this entry was incomplete, and check 29 carries the correction.* "Other
coordinates" is not the cause: both frames resolve the same two irreps and both use the same
canonical amplitudes, so the normalizations cancel from every ratio and cannot flip a direction.
The flip is physical — the two rooms assume different energy-delivery laws. The rule below is
still the right first move; it just does not finish the job on its own.

This is check 18's family (*"for any ratio quoted across sectors, confirm the denominator is the
same object in both"*) extended to the numerator and to the sign. **The check: before matching a
computed ratio to a required one, write both as explicit quotients — which mode over which mode,
in which field — and confirm the variable sets coincide.** Two "2:1"s in one corpus are more likely
to be inverses in different coordinates than a hit.

The same pass turned up why the trap was open: the ring-on-ring autopsy states the requirement as
w_breath/w_shape = 2 and T6 states it as ε_charged = 2ε_neutral, both describing R_c = M_c. They
reconcile only through the canonical normalizations R_c = √(3/2)R, M_c = √3M, and **no file states
that bridge** — an owed reconciliation now recorded in the ledger.

**26. `pkill -f` MATCHES YOUR OWN COMMAND LINE, AND KILLS MORE THAN YOU AIMED AT (2026-07-28 —
twice in one hour).** `pkill -f "bounce_m6_rebound_dst.py"` was issued to stop one dead job. The
pattern appeared in the issuing shell's *own* command line, so pkill killed that shell (exit 144) —
and took the six MPI ranks launched minutes earlier with it, despite their having been `setsid`
detached. The same mistake had already destroyed an in-flight file rewrite an hour before. Both
times the visible symptom was an odd exit code, not an error message naming what died.

**The check: never `pkill -f` on a string that appears in the command you are typing.** Resolve to
PIDs first (`pgrep -f … | grep -v $$`, or read the PID and `kill` it), and after any kill, verify
that everything you did *not* intend to stop is still running. The verification is the part that
was missing: the chains were confirmed dead only because an unrelated CPU reading looked wrong
four commands later.

**25. A CAPABILITY PROBE MAY BE REPORTING A BUDGET, NOT THE RESOURCE (2026-07-28 — caught by the
owner, not by me).** I reported "the box has one core" from `nproc` = 1, built a throughput
analysis on core contention, told the owner MPI would buy nothing, and put it in the chain-ops
memory. All of it was wrong: GNU `nproc` honours **`OMP_NUM_THREADS`**, which is 1 here. The
machine is a 6-core/12-thread i7-9850H, every process carries the full `fff` affinity mask, and
`top` showed 41.6% idle while I was describing a saturated core. The measurements were right and
the diagnosis inverted, which is the dangerous combination — a wrong *cause* attached to correct
*data* survives every consistency check the data would fail.

**The check: before attributing a symptom to a resource limit, confirm the limit with a second
tool that reads the resource rather than a budget.** Here: `nproc --all`, `lscpu`, `/proc/cpuinfo`,
`taskset -p`, the cgroup's `cpuset.cpus.effective` — any one of which would have caught it. The
family is general: `free` inside a container, `df` across a bind mount, `ulimit` versus the cgroup,
`CUDA_VISIBLE_DEVICES` versus the GPU count. **A recommendation that depends on a resource ceiling
must name the tool that measured the ceiling.**

**24. A POSTERIOR QUOTED FROM A CHAIN INHERITS THAT CHAIN'S CONVERGENCE STATE, AND A WIDTH
INHERITS IT HARDER THAN A POINT (2026-07-28).** The α_c band [0.0205, 0.0214] was read off
`cmp_prtoe_zon` when its last recorded R−1 was **93.1** against a `Rminus1_stop` of 0.05, and was
then used for a year as though it were a measurement. Sweeping every chain in the tree
(`scripts/chain_posterior_provenance_audit.py`): **none of the eighteen has ever recorded R−1 at or
below its own stopping target**, the best being 0.910 against 0.05.

That does not condemn the numbers. A chain far from convergence can still have a well-located
mode, and most of what the corpus quotes — H₀ = 69.9, S₈ = 0.823, ε ≈ 1.24%, ξ = 0.142 — is a
best-fit *point*, which is a much weaker claim and survives. **The distinction that matters is
point versus width.** An unconverged chain's interval carries no width guarantee at all, and is
typically too *narrow* rather than too wide, because the chain has not finished exploring — so
every σ built on one is inflated in the flattering direction.

The corpus already gets this right in two places and they are the template:
`PRTOE_s8_growth.md` refuses interim values outright ("their converged posteriors are the
mechanism's test; **no interim value carries**"), and `PRTOE_REFEREE_CALENDAR.md` carries a full
forensic account of the routeD collapse, including the acceptance-rate tell (0.897 → 0.991 means
the proposal is shrinking, not that the fit is good) and the warning that an archived dead chain
"reads like a fresh measurement (it did, twice)".

**The check: for every number attributed to a chain, state (a) which chain, (b) its R−1 at the time
of reading, and (c) whether the quantity is a point or a width.** A width from an unconverged chain
may be quoted only with its R−1 beside it. Live items this flags for re-check on convergence, both
currently well-caveated but neither carrying its chain's state: `PRTOE_deuterium_row.md`'s
"m_e = 1.01246 ± 0.00456 (2.7σ from 1)" and `PRTOE_THREE_EQUATIONS.md`'s
"`varying_me` = 1.0126 ± 0.0041".

**23a. AN ABSENCE CLAIM OVER A VERSIONED TREE MUST SEARCH THE HISTORY (2026-07-28).** The indirect
band on α_c was reported as having "no derivation anywhere in the repository", on a sweep that
honestly stated its scope — all `.md`, all chain inputs, all `.py`/`.yaml`/`.json`/`.log` — and
every item in that scope was true. None of it was `git log -S`. The derivation was in the commit
that registered the prediction, and recovering it voided three results built on the absence.
**The check: for any claim that something is not in the repository, `git log -S`/`git log -G` the
string across all refs, or state in the claim that the history was not searched.** A file deleted
after its number was quoted leaves exactly this trace and no other.

**The check: count the independent unknowns, count the recorded numbers, and if the second exceeds
the first, take a spanning subset and predict the rest.** A booked value that agrees with its own
source proves nothing about the set. The tell is a section quoting three or more numbers that a
substitution visibly relates — and the harness entry for it reading `chk(name, booked, booked)`
in disguise, i.e. checking a decimal against its own surd rather than against the other members.
When the set does close, record that too: closure confirmed is a result, and it is what
distinguishes this check from fishing.

**28. A CHECK THAT CANNOT FAIL IS NOT A CHECK (2026-07-28).** The regression harness graded every
booking *relatively*: `ok = booked == 0 or abs(got-booked)/abs(booked) <= tol`. The guard was put
there to avoid dividing by zero and it did that — by making the check pass unconditionally. **23 of
the harness's checks were unfalsifiable**, and they were exactly the load-bearing ones: every claim
of the form "this residual vanishes", "this quantity is exactly zero", "no solution dopes an
up-type quark". A "must vanish" assertion is precisely the kind that should be graded hardest, and
it was the kind that could not fail. All 23 turned out to be satisfied when graded absolutely — the
cost of the defect was zero this time, which is the reason it survived so long.

The same family has a second member: a booking whose expected value and computed value trace back
to the same literal. One was written this same session — `chk(..., 7/5, (lambda: [t for t in
[7/5]][0])())` — which tests Python, not physics. It was replaced with a numerical root-solve of
the curve it was supposed to be checking.

**The check: for every assertion in a harness, ask what recomputed value would make it print FAIL.**
If no value would, the line is documentation wearing a test's clothes. Grade zero bookings against
an absolute tolerance; make the expected value and the computed value travel by different routes;
and be most suspicious of the checks that have never once failed.

**29. A RATIO NEEDS ITS DELIVERY LAW, NOT ONLY ITS FRAME (2026-07-28).** Check 27 says a ratio is
not a number — name the variables and the direction. That is necessary and it was not sufficient.
The Koide null is recorded in two places as a stiffness relation: T6's reduction gives
ε_charged = 2ε_neutral (doublet stiffer), the ring-on-ring entry gives k_S = 2k_D (singlet
stiffer). Both name their variables. Both state their direction. They are still inverse, and three
cycles were spent withdrawing and restoring a correct result while trying to decide which
convention was "the" one.

Neither was. The underlying statement, R_c = M_c, is about **amplitudes**; every stiffness
statement is that constraint pushed through a rule for how energy sits in the modes, and with the
singlet at one degree of freedom against the doublet's two, the rules disagree by mode-counting
factors. The corpus uses four — thermal equipartition, sudden quench, equal sector delivery,
doublet-gets-half — which convert one null into ε_D/ε_S ∈ {2, √2, 1, ½}. A factor 4, spanned by
physics, not by bookkeeping. And the reconciliation that had been *assumed* (canonical
normalizations) provably cannot do the job: both frames grade the same two irreps, so the
normalizations enter every ratio as a fixed factor and cancel out of the comparison.

**The check: before comparing two stiffnesses, two powers, or two amplitudes across sections, name
the law that converted the underlying constraint into that quantity — and check the degree-of-
freedom count each side assumed.** A normalization difference rescales both sides and cannot flip a
direction; if the direction flips, the disagreement is physical and the two results are answers to
different questions. Neither may be withdrawn in favour of the other until the law is fixed.

**30. LIFTING A DEGENERACY IS NOT THE SAME AS FIXING A PARAMETER (2026-07-28).** The Koide phase φ
was shown to be an exactly flat direction of the democratic graph, because the two charged modes are
degenerate and rotations in their plane are a symmetry. The obvious repair — make the
inter-generation coupling complex, which demonstrably splits ε₁ from ε₂ — was written up as the
answer. It is not. The ring field is **real**, so f₂ = f₁\* and the two modes are not independent:
|f₁| = |f₂| always, and only the *sum* ε₁ + ε₂ = 2a − 2·Re b enters the energy, which carries no φ.
The splitting is real and does no work. Caught by checking the energy at three φ values instead of
reasoning from the spectrum: constant to 9×10⁻¹⁵ at every arg b.

The error is seductive because both halves are true — the degeneracy *is* what makes φ flat, and a
complex bond *does* lift it. What fails is the inference between them, and it fails on a constraint
that lives in the field's reality condition rather than in the Hamiltonian at all.

**The check: before concluding that lifting a degeneracy fixes a parameter, count the physical
configuration space, not the mode space.** Write the general real configuration explicitly (here:
three real f_k ↔ M, R, φ), and confirm the parameter in question survives as an independent
coordinate that the perturbation actually distinguishes. A reality condition, a gauge condition or a
constraint can tie modes the spectrum treats as separate — and then a term that splits the spectrum
still cannot see the parameter. The corrected result was stronger than the wrong one: *no* term at
*any* order in the ring's own real potential can reach φ, since Z₃ plus evenness forces V = F(cos 3φ).

**27c. A CUMULATIVE AVERAGE IS NOT THE CURRENT RATE (2026-07-28).** The two production chains were
relaunched under MPI, and their logs reported acceptance of 0.207% against 5.434% before the
relaunch — a 26× collapse, which would have inverted the recommendation that put them on three ranks
and argued for reverting. It was about to be reported as a finding.

The number is real and the reading was wrong. Cobaya's "N steps taken, and M accepted" is
**cumulative since the run started**, and the run had just spent its first ~1100 steps climbing to
the posterior peak from a fresh start — the burn-in transient sits in the denominator forever.
Differencing consecutive rows per rank instead gives the *current* rate: **6–11%**, at or above the
5.4% the serial runs had, with the covmat confirmed loaded. The chains were healthy the whole time.

The general form is worth having, because this corpus has already met it in physics: **a ratio
accumulated over a history is not the ratio holding now, and the two differ by exactly whatever
transient the history contains.** The f̄ window question is the same distinction — an average over the
winding versus the value at the epoch ε acts — and it was open for months there. **The check: before
quoting any rate, ask over what window it was accumulated, and if the window includes a transient
(burn-in, spin-up, a quench), difference the series instead.** A rate that has been averaged since
t = 0 answers a question nobody asked.

**31. AN OPEN-ITEM COUNT OVERSTATES THE DEBT, AND THE DOMINANT CLOSURE MODE IS "ALREADY PAID"
(2026-07-28).** A marker sweep found 246 open-debt markers across 72 live files, 70 of them
"owed"-class after excluding archive and ledger material. Triaged, 57 looked desk-doable. Seven were
then worked in one session. **None was solved.** Every one closed some other way:

| item | how it closed |
|---|---|
| the area law's field content | **already paid** by a prior task, unpropagated across seven files |
| light's 56% unsupplied share | **not independent** — the same debt as the basement's, read in a second channel |
| the pair-harmonic kernel question | **superseded** — its premise was removed by a later result |
| the seat sector's owed number | **duplicate** of an existing board item |
| the §2 wall "owed twice" | **halved** — the second amendment died on loop order |
| κ_v's value | **moot** — the mechanism it normalises is dead three times over |
| T14's conversion law | **reclassified** — a run, not a derivation, and blocked on one already executing |

The pattern is not luck. A corpus that records debts faithfully and closes them in the file that
owns them will accumulate markers faster than it retires them, because retirement requires editing
*every* file that ever cited the debt, and nobody does that. The count therefore measures
**bookkeeping lag**, not remaining physics.

**The check: before working any open item, spend five minutes trying to close it without doing the
work.** Grep the debt's own object across the tree; check whether a later dated section in the same
file already pays it; check the board for a duplicate; check whether its premise survived. Expect
this to succeed more often than not. **A session that closes seven items by finding six of them
already dead is not a session that avoided the work — it is one that avoided doing the work twice.**

The corollary matters for planning. Do not estimate remaining effort from the marker count, and do
not report it to an owner as a workload. Report it as an upper bound with the triage rate attached.

**A refinement, from getting the triage itself wrong the same day.** The first sweep sorted markers
into two bins — desk-doable, or needs a run — by testing for run-words (chain, MCMC, lattice,
telescope, integrator). That is the wrong partition, and it inflated the desk column. **There is a
third class: model-building**, which is neither a desk computation nor a run, and which the corpus
grades explicitly where it occurs ("this is where the model-building lives"; "model-building, not a
desk computation"). Two items sorted as desk-doable were sitting under exactly that heading, and a
desk session cannot move either. **Test for all three bins, and take the corpus's own grading of an
item over your inference from its wording** — a file that says what class its own debt belongs to is
better evidence than a keyword search over the sentence that states it.

**32. NAME THE SECTOR BEFORE QUOTING A MEDIUM PROPERTY (2026-07-28).** The program carries more than
one condensate, and they have different sound speeds, different critical velocities, and different
coherence lengths. The vacuum's excitations ride the light cone, so its Landau velocity is c. The
ultralight dark condensate has c_s = √α_c = 0.148 c and ξ = 402 AU. Both are correctly called "the
medium" in their own files.

The failure this produces is not an arithmetic error — it is a result that is right about one sector
and gets written up as though it were about the other. A decoherence null derived from the dark
condensate's parameters was drafted as "the medium cannot decohere a superposition," which reads as a
claim about the vacuum, and would then appear to contradict the vacuum's own zero-drag certificate.
Both statements were true; the write-up merged two sectors that the physics keeps apart.

**The check: whenever a derivation consumes c_s, ξ, v_c, m, or a density, name which condensate
supplied it, in the result's own title, before the result leaves the desk.** The tell that you have
skipped this is a sentence containing "the medium" with no qualifier. And when a new result appears
to contradict an existing certificate, suspect a sector mismatch before suspecting either result —
that is the cheaper diagnosis and, here, the correct one.

**REFINEMENT, same day, after failing this check a second time.** The rule above catches the error at
write-up. That is too late, and the second failure proves it: a turnaround time was lifted from
`PRTOE_coincidence_problem.md` and attached to the w = −1 row as a correction, when the file's own
opening line — "the floor is *not* a constant" — marks it as belonging to the **Route-D** branch,
whose competitor P-2026-018 has no turnaround at all. The published "correction" was wrong, and it
contradicted a claim that had been right.

**Ask the question at PICKUP, not at write-up.** The moment a number is lifted out of a file, before
any use is made of it, ask: *which sector, branch, epoch, or convention does this number belong to?*
The cost is one line. The cost of asking later is a correction that has to be corrected.

This generalises past condensates. The same failure mode covers **branches of a registered fork**
(P-2026-018 vs Route-D), **conventions** (§6d's factor two), **epochs** (Ψ₀ at onset vs today), and
**sectors** (vacuum vs dark condensate). In every case the number is correct and the *scope* is
what travels wrong — which is why no numerical check can catch it and why the harness stayed green
through all four.

**33. STATE THE GRADE BEFORE COMPUTING, AND SAY WHICH INPUTS ARE FITTED (2026-07-28).** An external
reviewer named the program's characteristic failure precisely: landing on an observed number after a
long chain, then demoting the claim to "existence, not precision." The demotion is correct
epistemics. Doing it *after* seeing the landing is not, because the grade then depends on how close
the number came, which is the one thing the grade is supposed to be independent of.

The same day, this failed in the sharpest possible way. Ψ₀ was diluted from onset to the present and
found to reproduce Ω_DM to 0.09%, and that was written up as the model landing on the measured dark
matter density. But Ψ₀ *is fixed by demanding today's abundance* — `PRTOE_PHYSICS_DOMAINS.md` row 70
says so outright. The computation inverted its own defining relation and recovered its input. Four
correct digits, harness checks passing, and no content whatever.

**The check, in two parts, both before the first number is produced:**

1. **Write the grade down first.** State what result would count as confirmation, what would count as
   a null, and what the claim's evidence class will be *whatever* comes out. If that cannot be
   written before the computation, the computation is not yet a test of anything.
2. **List every input and mark each as measured, derived, or fitted-to-the-target.** If any input was
   fixed by demanding the very quantity being recovered, the result is circular and must be labelled
   so in the script, in the harness row, and in any prose that quotes it. Circular checks are still
   worth running as arithmetic tripwires — they catch slipped exponents and wrong dilution laws — but
   they are never evidence, and a harness row that does not say so will be misread later, including
   by the person who wrote it.

The tell is a result that agrees far better than the messiness of the derivation should allow. Four
digits out of a chain with three modelling choices in it is not a triumph; it is a signal that the
answer was in the inputs.

**34. ASK "WHAT FIXED THIS?" OF EVERY INPUT, BEFORE THE LANDING IS WRITTEN UP (2026-07-28).** Two
headline claims died the same day by one mechanism: a quantity fixed by demanding X, then reported as
landing on X. Ψ₀ was fixed by demanding today's dark matter abundance and then found to redshift onto
it. The scale ladder defined α_eff ≡ v/c and then found ½α_eff² at every rung, which is the virial
theorem. **Both were caught by accident, while doing something else.** That is not a method.

The test is one line per input — *what fixed this?* — and the answers sort into three bins: measured
externally, derived from something independent, or **fixed by demanding the very quantity now being
recovered**. Any input in the third bin makes the landing empty, however many digits agree.

**Run it on every landing before writing the landing up, not after.** Applied deliberately across
five headline claims (`scripts/circularity_sweep.py`), it returned:

| claim | verdict |
|---|---|
| Ψ₀ → Ω_DM | **circular** — relabelled |
| the scale ladder | **definitional** — retired |
| ρ_Λ¼ = (9/2)α⁴T_c | clean, but a ~1.8σ *offset* rather than an agreement |
| A_s = (α_c/4πk)³ | clean, with a standing fence that must not be removed |
| ε = c·f̄·α_c | clean, but inherits c = 9/10's status as a counting choice |

Two of five were empty. Two of the three survivors needed weaker wording. **A sweep that finds
nothing is cheap; a sweep never run is how two dead claims stood for months.**

The corollary is about fences. Where an input has two provenances — A_s's k has a closed-form value
*and* an A_s-measured one — the fence separating them is load-bearing. Quoting k as A_s-derived while
also quoting A_s as a k-prediction closes the loop, and the fence is the only thing preventing it.
Fences of this kind should be annotated with what they prevent, so a later editor does not remove one
as redundant.

**35. A MARKER SWEEP NEEDS THREE FILTERS BEFORE ITS COUNT MEANS ANYTHING (2026-07-28).** Check 31
says an open-item count overstates the debt. Measuring it properly showed *how*, and the correction
is mechanical.

A raw grep for owed-work markers (`is owed`, `still owed`, `remains open`, `not yet derived`,
`un-derived`) returned **83** hits across 35 forward-facing files. Three filters cut it:

| filter | removes | why |
|---|---|---|
| **negations** | 5 | `"**no** separate cancellation coefficient is owed"` matches an `is owed` grep and means the opposite |
| **the failures ledger** | 11 | recorded deaths, not live debts — the file exists to hold them |
| **archive and dated logs** | 8 | state-as-of-their-date by convention; not current work |
| **every other historical directory** | — | see below; this is the one that is easy to miss |

Leaving **67** corpus-wide, of which **16 more** are open *predictions awaiting referees* rather than
desk items. Restricted to the live forward-facing files, the count is **19**.

**The fourth filter deserves its own warning: "archive" is not the only name history hides under.**
The first pass here excluded `archive/`, `working_logs/` and `exploratory/` and still returned two
markers from `PRTOE_Working_Formulation.md` — which sits in **`historical_v1-v3_scalar_tensor/`**, the
retired scalar-tensor formulation. They read exactly like live debts. **Enumerate the directories
first (`find . -maxdepth 1 -type d`) and decide each one's status explicitly**, rather than excluding
the names you happen to remember. This corpus has seven such directories and three of them are
historical under three different naming conventions.

**A second false-positive class, found the same way:** a file's own *meta-statements* match the
pattern — "this document tracks the numbers the model has **not yet derived**", "what **remains
open** is labeled open" — as does any correction text that quotes the wording it is retiring. Those
are not debts either, and no regex distinguishes them. The count is a starting point for reading,
never a workload.

**The negation filter is the one that bites**, because it inverts meaning rather than merely
inflating the count — a sweep that reports "no X is owed" as an open debt will send someone to
re-derive a thing already settled. Grep for the marker, then read the forty characters before it.

**And the reason this check exists at all:** on the day it was written, four consecutive dockets
turned out to be model-building, run-gated, or data-gated, which made "the desk is empty" feel
established. It was not — the sweep found roughly forty live items. **A run of non-desk tasks is
evidence about the last four items, not about the remainder.**

**36. FINDINGS TRAVEL INWARD BY DEFAULT; SOMEONE HAS TO CARRY THEM OUT (2026-07-28).** Three defects
found in one day had the same shape, and it is not concealment — it is drift with a direction.

| the honest number | where it was written | where it was missing |
|---|---|---|
| the anchor's factor-11 band (§6d's convention ×2, §6f's residual ×5.6) | hierarchy §6d/§6f | the risk page, which had **no mention of the hierarchy chain at all** |
| every chain unconverged, best 265× over target | each chain's own `.progress` | the parameter tables presenting them, and the evidence section |
| the τ collision — the dof-family band putting ρ_Λ¼ at +4.3%, not +0.44% | `PRTOE_DERIVATION_HUNT.md` | the dark-energy file **and** the risk page |

In every case the person who found it wrote it down accurately, in the file they were working in.
Working files are where investigation happens, so that is where findings land. **Nothing in the
process pushes them the other way**, and a headline is edited least often precisely because it is
settled — so the caveat accumulates inward while the claim stays put.

**The check: when a result changes what a headline should say, edit the headline in the same
session, not the working file alone.** And the reverse direction, which is cheaper and catches the
backlog: **when auditing a forward-facing file, grep the working logs for its own key quantity** —
τ, the anchor, the chain name — and ask whether anything found there has failed to arrive.

The tell is a working file containing a qualification *more specific* than the headline it belongs
to. A headline reading "+0.44%" over a working log reading "a few percent above the observation" is
not two views of one result; it is one result and one stale advertisement.
is necessary and is not sufficient: both test what you thought to test.

## Recording

Each completed file gets a line in `_AUDIT_LEDGER.md`: date, what was found, what changed. A file
audited and found clean is recorded too — that is a result, not a non-event.

Findings needing the owner go to `ForJustin/` and the file moves on. A wall does not stop the queue.

## Order

Audience-facing first, deepest-cited first, because those carry the most exposure per defect:

1. The Fairbank set — done 2026-07-19
2. The flagship trio: THREE_EQUATIONS, MATH_SPINE, THE_AMPLITUDE
3. The entry points a new reader hits: INDEX, READERS_GUIDE, DEPENDENCY_TREE, honest_status
4. The registry and the ledger
5. Domain files, by citation depth
6. Working logs

## The payoff check — a second instrument, and it catches a different defect

The reverse audit asks *"is this closed task's object actually closed?"* and finds bookkeeping
errors. A second question finds something else: **for each OPEN task, what does its payoff look like
if it succeeds — and does any file already claim that payoff?**

It found the sharpest defect of the 2026-07-20 pass. T14 grades link 5 — the AD-direct rectification
— as "[OWED — THE one missing link]". Its payoff, if it lands, is the three-way convergence of
matter asymmetry, helicity and winding on a single draw. And `PRTOE_cosmic_magnetism.md` was
asserting exactly that, as a standing result, in an audience-facing domain file: "magnetic helicity
with a **DETERMINED SIGN** … the SAME topological draw that set matter-over-antimatter." The
specialist file graded it open; the domain file sold the conclusion. Corrected: the sector predicts a
helicity sign *relative to the winding*, and cannot say which handedness the matter universe
corresponds to until link 5 lands.

**Why the reverse audit could not have found it.** That pass walks *completed* tasks. This defect
lived at the far end of an *open* one — a claim standing in the corpus as though the open work had
already succeeded. Nothing in a completed-task sweep looks there.

**Run it on the open board, not the closed one.** For each open task: name the payoff, grep for it,
and check whether any file states it as established rather than as owed. Applied the same day to
#115 (payoff: A = √2 derived, after five recorded routes to it died), the check came back **clean** —
the flagships use Q = 2/3 as *measured input* and derive the kernel modulus from it, and the
dependency tree grades the chain candidate. A clean result is worth recording too: it says the
sector's documentation held under a targeted attack on its most-attacked object.

**37. A LIVE NUMBER BELONGS IN THE RUN LOG UNTIL IT STOPS MOVING (2026-07-28).** Check 36 says carry
findings outward to the headline. This is its boundary condition, and it was learned by getting it
wrong the same afternoon.

A running-chain reading put the model 41 log-units behind ΛCDM+mν. It was hedged correctly —
labelled a burn-in snapshot, with the descent explicitly "not established as having stopped" — and
then written onto the **risk page**, on the reasoning that a reader asking about current evidence
deserves to know the number in progress is adverse. Four hours later the same chain's leading rank
had descended 42 units and stood 0.6 log-units *ahead*. The risk page had been asserting something
false for four hours, correctly hedged and still wrong.

**The distinction check 36 does not make, and needs:**

| kind of finding | where it goes |
|---|---|
| a **settled** result that changes what a headline should say | the headline, same session |
| a **live** number from a process still running | the run log only, however well hedged |

A hedge does not fix placement. "This is a burn-in snapshot" sitting under a risk-page heading still
reads, to anyone skimming, as *the current state of the evidence* — and skimming is what that page
is for.

**The test before writing a number outward: could this move by more than the margin I am quoting,
without anything being wrong?** If yes it is not a finding yet, it is a reading. The chain pair
demonstrated the point at zero cost by producing a strongly adverse and a mildly favourable reading
six hours apart, from the same data, with no error in either.

**And the asymmetry to watch in oneself:** the temptation is to report a favourable reversal with
more energy than the adverse original, or to quietly drop the original. Record both, side by side,
in the order they occurred.

**38. A DOCKET WRITTEN AT THE MOMENT OF CONFUSION RECORDS THE CONFUSION, NOT THE DEBT (2026-07-28).**
Three dockets worked in one session turned out to be misnamed, and in each case the misnaming was
the reason the item looked hard:

| docket, as written | what it actually was |
|---|---|
| #58 "supply the density of states and k_F" | the DOS was already supplied and **k_F does not exist in the construction** — it cancels twice |
| #72 "supply the seeding step's conversion law" | the law was already supplied and convention-free; the missing thing was one **input sign**, gated on a running experiment |
| #67 "derive Ψ₀'s profile through z_x" | the fraction was already supplied; the missing thing was a **modelling ruling**, and under two of three readings the profile is one line |

None was a physics gap. Each was written when the author could see that *something* was owed but not
yet what, and the wording froze that uncertainty into a task title — which then survived unchallenged
because titles are what get scanned and bodies are what get read.

**The check, when opening any docket: before working it, restate what is owed in one sentence using
the corpus's current vocabulary, and compare that against the docket's own title.** Where they
differ, the title is usually the stale one, and the difference is usually the whole job. Retitle
first; the work often shrinks or dissolves.

**The tell** is a docket asking for an *object* ("supply X", "derive the shape of Y") when the file
it refers to already contains that object under a different name, or contains everything except a
one-line ruling. Objects are what a confused author asks for; rulings and inputs are what is
generally missing.

This compounds with check 31 — the dominant closure mode is "already paid" — and explains part of
it. An item can be paid and still look open because the docket is asking for the wrong thing.

> **27d. SAMPLE COUNT IS NOT PROGRESS, AND ON A HETEROGENEOUS POSTERIOR IT CAN RUN BACKWARDS
> (2026-07-28).** Sibling of 27c, which caught a cumulative acceptance rate misread as a current one.
> This is the same disease in a different instrument.
>
> On the running dyad pair, the three MPI ranks stood at 325 / 1173 / 498 samples. The rank with
> **3.6× the samples had made a fifth of the progress** — 24.8 log-units of descent against rank 1's
> 114.1, and sitting 234 log-units from the basin rank 1 had already reached. The cause is mundane:
> rank 2 was at H₀ = 64, away from the model's region, where CLASS evaluates faster. It accumulated
> samples quickly while going nowhere.
>
> **So on any posterior where likelihood cost varies across parameter space — which is every
> cosmology chain — sample count measures how cheap a region is, not how converged a rank is.** The
> fastest-accumulating rank is often the one furthest from the answer, because being wrong is cheap.
>
> This was nearly quoted the wrong way the same day: "992 and 1759 samples" was reported for the two
> runs with the larger number attached to the model, which reads as the model chain being further
> along. It was the opposite.
>
> **Report per-rank −logpost and its trend, never the pooled sample count.** If a single number is
> wanted, use the worst rank's distance from the best rank's basin — that is what convergence
> actually waits on.

> **36a. A CORRECTION FIXES ONE INSTANCE; THE CLAIM HAS SEVERAL (2026-07-28, same day as 36).**
> Check 36 is about findings failing to travel from working files to headlines. This is its twin:
> **corrections failing to travel from the place you noticed the error to the other places the error
> lives.** Both were demonstrated the same afternoon, by the person who had just written 36.
>
> A cross-reference to "hierarchy §2b" was corrected in the failures ledger at midday. The section
> does not exist — it is §2 part (b). By evening the same phantom was found in **four more files**:
> the dependency tree, the derivation hunt, the audit ledger and T6's working log. Separately, the
> anchor's honest band was written into the hierarchy header in the afternoon, and §6 was still
> quoting "+0.14%" as a settled figure at the end of the day, because the header's qualification
> says "every anchor number quoted in **§2** below" and §6 is not §2.
>
> **The check: after correcting a claim, grep the corpus for the claim's own distinctive string —
> not for the docket number, which never appears in prose.** One command, and it is the difference
> between a correction and a correction that took.
>
> **And the trap that makes a blind replace worse than nothing:** `PRTOE_deuterium_row.md` genuinely
> *has* a §2b, "The nuclear-data systematic, measured inside the pipeline". A search-and-replace on
> `§2b` would have corrupted three correct references while fixing five wrong ones. **Grep for the
> qualified string — "hierarchy §2b" — never the bare token.** The same applies to any symbol or
> section number that more than one file uses legitimately, which in this corpus is most of them.

> **33a. AN HONEST LABEL IS NOT A GUARD (2026-07-28).** Check 33 requires every input to be marked
> measured, derived, or fitted. That is necessary and it is not sufficient, because **a label
> travels with a number without stopping it.**
>
> The radio-lattice paper's RRL precision was written into the source as "~7e-6, inferred from
> fitted-velocity uncertainties, **NOT sourced**". The labelling was exactly right. The number was
> still wrong by one to two orders — the row is limited by bulk gas motion at 6.7e-5 to 2.7e-4, not
> by a velocity fit — and it sat in the working number for the sensitivity budget for hours,
> correctly labelled the whole time. Had the paper been assembled from that block, the label would
> have travelled into a footnote and the wrong figure into the arithmetic.
>
> **The rule: a number marked "inferred" is not permitted to be the working value.** Either it gets
> sourced, or the slot stays empty and the downstream calculation is not attempted. An empty slot
> stops work; a labelled slot does not, which is precisely why the labelled one is more dangerous.
>
> The same applies to "provisional", "estimate", "order of magnitude" and "pending verification".
> Each reads as a caveat and functions as permission.

---

**39. "Waiting on an external referee" is a claim about the adjudicator, not a licence to stop
work — and it hides desk debt better than any other label on the board.**

Three of the five items opened on 2026-07-28 carried referee-style tags. All three tags were about
*who decides*, and none of them was true about *whether anything remained to do first*:

- **#33** was tagged "MCMC-queued behind capacity." It needed no chain at all — the item asked for a
  literature refresh of a comparison table. The work was already done in the file, and what actually
  remained was verifying the one citation the corpus had booked as a bare arXiv identifier with no
  author, title, or year. Verifying it **moved the number against this model**, which is the direction
  a fairness pass exists to find.
- **#29** was tagged "21-cm referee." The fork it was waiting on had been **collapsed twelve days
  earlier** — one reading retired as an illegal step — and the registry already said so. Two
  forward-facing files were still presenting the dead fork as live.
- **#28** was tagged "external referees." True, and irrelevant: the fence the referee's answer would
  be graded against **has no number in the corpus**. A detection and a null would both be arguable.

**The rule: before parking an item on an external referee, state the grading rule and check that
every number in it exists.** A pre-registered fork whose fence is qualitative is not pre-registered
— it is a place to have an argument later. Ask three questions and answer them in writing:
(i) *has the referee already reported, or has the fork already collapsed for internal reasons?*
(ii) *is the discriminator stated as a number on both sides?* (iii) *if the answer arrived tomorrow,
could it be graded without a judgement call?* Any "no" is desk work, and it is desk work **now**,
because it is exactly the work that cannot be done honestly once the data are in hand.

The failure this prevents is not laziness — it is the far more comfortable error of believing the
board is blocked when it is merely unexamined. Related: **38** (misnamed dockets are not hard ones)
and **36a** (a closure that leaves its own markers stale).

---

**40. A number reconstructed from a rounded intermediate is not a second opinion — it is the first
number with error added, and it will be mistaken for a disagreement.**

θ̇ was carried at 59.7 eV (derived: θ̇ = m·(T_sph/T_on)³, every input sourced) and at 58.5 eV
(reconstructed by back-multiplying θ̇/H, a ratio recorded to two significant figures). The 2.05% gap
between them is *entirely* the truncation of 2.450×10⁶ to 2.4×10⁶. Three files recorded this as a
"two-percent internal disagreement worth naming rather than averaging", and the adjudication came
down **for the artifact and against the derivation** — praising the reconstruction for having "each
of its inputs sourced", which was the exact virtue of the number it demoted.

The failure has a signature worth memorising: **the discrepancy got attributed to a physical
parameter.** The ledger concluded "the gap is a g\* choice: 59.7 eV would require g\* = 111.1." That
arithmetic is right and the inference is empty — it holds a two-figure quantity fixed and pushes a
2% residual into whichever parameter is nearest. A quantity known to two figures **cannot support a
2% inference about anything**, and a discrepancy at the size of the rounding is the rounding until
proven otherwise.

**The rule: before adjudicating a small numerical conflict, check the significant figures of every
intermediate on both paths.** If either path passes through a rounded quantity, the conflict's size
must exceed that rounding before it is a conflict at all. And when two routes to one number
disagree, ask which is *primary* — the one computed from inputs, or the one reconstructed from a
recorded output. The reconstruction never wins on provenance; it inherits the primary's provenance
plus its own truncation.

The other half of this entry: **the argued-about gap is often not the largest one.** Here the onset
temperature is carried at 9.41, 9.46 and 9.5 keV across the corpus — 1.0%, cubed into **2.9%** on
θ̇ — while three files adjudicated a 2% artifact. Look for the unargued spread before spending a
paragraph on the argued one. Related: **9a** (labelled slots read as caveats and function as
permission) and **36a** (stale markers left by one's own closure).

---

**41. "The chain is running" is a claim about the box, and it decays silently. Verify it against
`ps`, not against the sentence that asserted it last week.**

Six separate places in the corpus asserted that a computation was live when it was not — found on
2026-07-28 by sweeping for run-status language and checking each against the process list:

| file | claimed | actual |
|---|---|---|
| `PRTOE_MATH_SPINE.md` §7 | "the running Route-D chain is the single decider" | one chain file, dead since 07-20 |
| `PRTOE_MATH_SPINE.md` (second site) | "its adjudicating chain is running" | same chain — **missed on the first fix that same day** |
| `PRTOE_s8_tension.md` | "The conv_desi chain (running)" | dead since 07-22, R−1 = 13.25 |
| `PRTOE_s8_growth.md` | "converged posteriors (running)" | same chain |
| `PRTOE_PREREGISTERED_PREDICTIONS.md` | "the adjudicator is still running" | same chain |
| `T4_s8_growth_owed.md` (earlier find) | "the chain is running again" | died a second time |

**Two failure modes, and the second is worse.** The first is ordinary decay: a run ends, and the
prose that described it does not. The second is that **a dead chain reads exactly like a scheduled
one** — "waiting on the chain" is indistinguishable from "waiting on nothing" from inside the
document, so the debt looks handled and nobody looks for another route. The Route-D case is the
sharpest: the chain was not merely dead but **single-chain**, so the statistic it could produce was
blind to the failure mode the gate cared about, however long it ran. That is
unfalsifiable-by-construction waiting.

> *Corrected 2026-07-29.* This paragraph first said a single chain "could never have produced the
> Gelman–Rubin statistic". **It can** — with one process the sampler splits the chain into
> `Rminus1_single_split` segments (default 4) and computes a within-chain split-R̂; two other
> single-chain runs here recorded R−1 = 13.25 and R−1 = 40.36. What a split-R̂ **cannot** do is
> detect confinement to a single basin, since every segment shares it. The conclusion is unchanged
> and the phrase is now accurate: the gate was waiting on a number that could not fail in the
> relevant way. Ironically this is protocol **46**'s pattern — a check incapable of detecting the
> thing it was there to detect — appearing in the diagnosis rather than in the audit.

**The rule: any sentence claiming a computation is running, pending, or in flight must be checked
against `ps` and the file's own mtime before it is relied on, and re-checked whenever the claim is
quoted.** Two commands. Also check *multiplicity*: a convergence gate needs ≥2 chains, so a
one-chain run cannot satisfy it and the gate is mis-specified rather than slow.

**And fix every site at once.** The math spine carried the same false claim twice; one was corrected
in the morning and the other survived until an explicit sweep that afternoon. Related: **36a** (a
closure that leaves its own markers stale) — which this is an instance of, committed *while writing
the correction for the other instance*.

---

**42. A proxy is not the quantity. Before trusting a number you derived, check that what you computed
is what its name claims — the reported value is usually one directory away.**

Protocol 40 covers a factor read off a *rounded* input. This is its sibling and it bit three times in
one session, each time on a quantity that had an authoritative version available:

| what was computed | what it actually measured | where the real value was |
|---|---|---|
| "acceptance = 97–99.8%", from accepted-rows ÷ total-weight in the **chain file** | nothing — chain files store only *accepted* points, so that ratio is ~1 by construction | the launchlog, in the sampler's own words: **5.3–6.2%**, the *opposite* diagnosis |
| "8 script citations are missing", from `grep -rh … \| grep -v /archive/` | everything, unfiltered — **`-h` strips filenames, so the archive filter had nothing to match** | the same grep without `-h`: **6**, one of which had no live citation at all |
| "`burn_in: 40 → 300` will help the ranks escape a trap" | a *discard length*, which has no effect on escaping anything | the sampler printed its own resolved target: **5400 accepted steps**, ≈20 h of silence |

**The shape:** in each case a derived quantity was preferred to a reported one, and the derivation
was never checked against what the name promised. Two of the three pointed the *wrong way* — the
acceptance error inverted the diagnosis (too-small steps vs too-large), and the grep error
manufactured work that did not exist.

**The rule, in order:**
1. **Prefer the reported number.** Samplers, compilers and libraries state their own diagnostics.
   If you are deriving one they already publish, you are choosing the worse source.
2. **Sanity-check the magnitude before acting.** 99% acceptance and 5% acceptance imply opposite
   fixes; either would have been caught by asking "is this plausible for a tuned MCMC?"
3. **Verify the filter filters.** A pipeline stage that silently passes everything looks identical to
   one that finds nothing to remove. Test it on a case you know should be excluded.
4. **Change parameters by mechanism, not by name.** Ask what the knob *does*, not what it is called.

**And say so when it reaches something outward-facing.** The acceptance error had been written into
`PRTOE_fairbank_note_draft.md`, a letter to a named person, before it was caught. It was corrected
within the same session rather than at the end — the cost of a correction rises steeply once someone
has read it. Related: **40** (rounded intermediates), **41** (status claims that decay).

---

**43. `pgrep -f X` matches the shell that is running it, if X appears in that shell's own command
line. This bug produced two unrelated failures in one day.**

**Failure one — it killed the wrong thing.** Stopping the model chain with
`PIDS=$(pgrep -f "cobaya.run.*dyad_mnu_bbnfix"); kill $PIDS` also matched the *bash process issuing
the command*, because that process's command line contained the pattern. The shell killed itself
mid-script. Harmless here, but the same construction aimed at anything important is a self-inflicted
outage, and it is invisible in review because the pattern looks correct.

**Failure two — it created immortal watchers.** Eight background shells of the form

    while pgrep -f granule_selfgravity >/dev/null; do sleep 30; done; echo DONE; cat …

**can never exit.** The `pgrep` matches the `while` loop's own shell forever, so the watcher outlives
its target indefinitely — the oldest found had been polling for **two days** for a process that
finished in minutes. They cost almost nothing in CPU, which is exactly why they accumulate: the
symptom is a cluttered background list, not a slow machine, and nobody investigates clutter.

**The fixes, in preference order:**
1. **Kill by explicit PID.** Capture the PID at launch (`$!`) or read it once, then `kill 12345`.
2. **Bracket the first character** so the pattern cannot match itself: `pgrep -f "[g]ranule_selfgravity"`.
3. **Wait properly** — `wait $PID` for a child, or watch the artefact (`while [ ! -f done.flag ]`)
   rather than the process table.
4. **Never poll for a name you also typed in the polling command.**

**And the corollary that costs the most: verify what you did NOT intend to stop is still alive.**
That is check **26**, and it is why the chain kill was recoverable — the reference chain was
confirmed running within seconds. Related: **42** (a proxy measuring something other than its name),
of which this is the process-table instance.

---

**44. Never append to a file a running process holds open. Your text will be overwritten and you
will not be told.**

The 3D toroidal run wrote its log through a `>` redirection, so the process carried its own file
offset. A `>>` append lands at end-of-file; the process then continues writing **at its own,
earlier offset** and overwrites whatever was appended. There is no error, no warning, and the file
looks fine — the loss is only visible if you go looking for the specific text.

**What it cost here:** the *pre-registered acceptance criterion* for that run, appended at t = 6.25/8
and gone by completion. That note's entire value was fixing the verdict's conditions before the
answer was visible; losing it damaged precisely the discipline it existed to serve. The run log was
untracked in git, so there was no recovery.

**The rule: write notes to a separate file — `<run>.notes.md` — and reconcile after the process
exits.** If a note must live in the log, append it only once the writer has exited (`kill -0 $PID`
to confirm). And **put anything that functions as a pre-registration under version control the
moment it is written**, so its timestamp is attested by something other than a mutable file.

**Recovery discipline, if it happens anyway:** find a secondary artifact that carries the same
content with an earlier, independent timestamp (here, a script whose docstring held the criterion,
written 27 minutes before the result). Restore the text **labelled as restored**, state what the
attestation now rests on, and say plainly that it is weaker than an untouched original. A restored
pre-registration presented as if it were the original is a provenance claim you can no longer back.

Related: **41** (status claims that decay), **43** (`pgrep -f` matching its own shell) — all three are
the same failure of treating a name as the thing.

---

**45. A field's NAME is not its DEFINITION. When a number will drive a diagnosis, read the code that
computes it — especially when a second number with the same name disagrees.** (2026-07-29)

The model chain's `.progress` file has a column named `acceptance_rate` reporting **0.9736**. The
launchlog reports **745 accepted / 8018 steps = 9.3 %**. Both are "the acceptance rate" by name;
they differ by a factor of ten, and they license opposite diagnoses — *proposal far too narrow*
versus *proposal poorly matched and exploring slowly*. The second is the one that drove a re-tune
and a paragraph in an outward-facing letter.

Reading `cobaya/samplers/mcmc/mcmc.py` settled it in one function:

```python
def get_acceptance_rate(self, first=0, last=None):
    return ((last or self.n()) - (first or 0)) / self.collection[OutPar.weight][first:last].sum()
```

Stored rows ÷ Σ weights. Under fast-parameter oversampling each accepted sub-step is written as its
own row, so the weights sit near 1 and this ratio is **pinned near unity whatever the proposal is
doing**. Confirmed numerically on the live reference chain: 2154 rows / 2221 total weight = 0.970,
reproducing the column; against 745 / 8018 = 9.3 % from the step counters. The column is not wrong —
it is a different quantity wearing a name that invites misuse as a health metric.

**What made this dangerous rather than merely confusing:** the earlier correction reached the right
conclusion — launchlog authoritative, ~0.97 an artifact — but recorded the *wrong reason*, that
"chain files store only accepted points so the ratio is ≈1 by construction." Weights do record
rejections; that reasoning is false, and it happened to point at a true conclusion. **A right answer
resting on a wrong reason survives every check that tests the answer**, and it will break the moment
it is applied somewhere the coincidence does not hold.

**The rule:** when two sources disagree about a named quantity, do not adjudicate by plausibility or
by which one you already believe. Open the definition. Then state, in whatever document quotes the
number, **which counter you read and why the other one differs** — a reader checking your figure
will find the more conveniently-named column first, and reach the opposite conclusion about your
competence with better evidence than you gave them.

Related: **42** (a proxy is not the quantity) — 45 is its inverse, where the *same name* hides two
quantities rather than one quantity hiding behind a stand-in. Also **40**: a conclusion inherits the
soundness of its derivation, not merely the truth of its result.

---

**46. A check that cannot fail is not evidence, and a count that mixes the two kinds overstates
both. Audit the audit.** (2026-07-29)

The corpus leans on a headline: *"1282 closed-form checks, all pass."* That number is worth exactly
what the checks are worth. Reading an unrelated line surfaced this one:

```python
chk("S8 pair", "g candidate identity 10*eps == 54a/pi", 1.0,
    (10*27/(5*math.pi)*(1/137.035999)) / (54/(math.pi*137.035999)), 1e-12)
```

With ε defined as 27α/(5π), that ratio reduces to (10·27/5)/54 = 1 **for any α**. It cannot fail. It
is a fine transcription check on 10·27/5 = 54, but its *label* read as though the pass list were
evidence for g = 10ε — which is precisely the claim docket #82 records as **still owed**. The check
was passing, correct, and rhetorically doing work it had not earned.

`scripts/audit_selfcheck_tautology_scan.py` now parses every `chk()` call site and flags three
patterns: **T1** ratio-to-one (reduces to an identity regardless of inputs), **T2** literal echo
(the booked value appears verbatim inside the computed side), **T3** constant-free (pure literal
arithmetic, so only transcription is tested).

**Result: 161 of 1236 call sites flagged, 13.0%.** Which is the reassuring direction — **87% are
substantive recomputations** — but the 13% should be *stated*, not blurred into the headline.

> **REFINEMENT, made within the hour and before the 13% was quoted anywhere.** Spot-checking the
> `deuterium_row` block (93 checks, 12 pure-literal — the same 13%) showed **T3 conflates two
> different things**, and only one of them is a weakness:
>
> - *Pinning an external input* — "d ln(D/H)/d ln ω_b (production, **measured**)", "Pisanti's rate
>   error vs PRyM-on-PRIMAT-bands", "τ_n bottle→beam". **You cannot recompute a measurement.**
>   Pinning is the correct and necessary check for these, and flagging them as weak is simply wrong.
> - *Pinning something that could have been derived* — where an independent route existed and was
>   not taken. This is the only case that represents a missed opportunity.
>
> So **13% is an upper bound on the soft checks, not an estimate of them**, and the real figure is
> lower by however many are external-input pins. The scanner cannot separate these automatically,
> because the distinction is about provenance, not syntax — it lives in whether the number came from
> a measurement or from the theory. **Do not quote 13% as a defect rate.** Quote it as "13% are
> definition- or input-pins rather than independent recomputations, most of them legitimately so."

**The rule, in three parts:**

1. **Flagged does not mean wrong.** T3 in particular is a legitimate way to pin a definition or catch
   a transcription slip, and a lot of this file's value is exactly that. Do not delete these.
2. **But relabel any T1/T2 whose label implies a physical identity.** The fix is the label, not the
   check. A reader scanning a pass list credits what the label says.
3. **Quote the split, not just the total.** "N checks pass" invites the reading that N independent
   facts were verified. When the number is used as evidence — in a letter, a paper, a risk page —
   say how many recompute a quantity by an independent route and how many pin a definition.

The deeper point, and the reason this sits next to **40** and **45**: *the failure modes that survive
longest are the ones that keep passing.* A wrong number gets caught. A check that cannot fail never
gets caught, because nothing it can do looks like failure.

---

**47. A plausible code path is not a diagnosis. Find the log line that proves which mechanism
actually fired.** (2026-07-29)

The model chain's proposal was never re-learned. Reading cobaya's source turned up a mechanism that
explained it perfectly: learning is refused while R−1 exceeds `learn_proposal_Rminus1_max` (2.0, or
30.0 early), and a chain whose ranks sit in different basins never gets under either. That became the
recorded diagnosis, complete with a memorable framing — *"the mechanism that would fix the proposal
is gated behind the problem it would fix"* — and it reached **the reader-facing risk page and the
Fairbank letter**, carrying the further claim that *more running time could not repair it*.

It was wrong. Isolating the archived run's MPI section (the launchlog is append-mode across
relaunches, so this required finding the last rank-prefixed `Sampling!` line first) shows what
actually happened:

```
[1 : mcmc] Ready to check convergence and learn a new proposal covmat (waiting for the rest...)
[2 : mcmc] Ready to check convergence and learn a new proposal covmat (waiting for the rest...)
```

…and rank 0 never announcing it. *"All chains are ready"* never appears. **No convergence statistic
is ever computed** — so the R−1 gate was never reached, let alone triggered. Learning is a
**collective checkpoint** at `learn_every` = 40·d accepted samples *per rank*; with d = 13 that is
520, and the ranks held 467 / 1684 / 658. Two ranks blocked for hours waiting on a third that was
**53 samples** short.

**Why the wrong diagnosis was so convincing:** it explained every symptom. The proposal never
adapted ✓. The covmat mtime never advanced ✓. R−1 never appeared to fall ✓. It was consistent with
all the evidence *and it named a real code path* — the gate exists, and would plausibly have bitten
next. It was simply not the one that fired.

**The rule:** when the evidence is an *absence* — nothing adapted, nothing was written, nothing
converged — an absence is consistent with every mechanism that would produce it. **Ranking candidate
mechanisms by plausibility is not diagnosis.** Go find the positive artifact: the log line that only
one hypothesis predicts. Here it was six words — *"waiting for the rest"* — which the R−1 story does
not predict at all and which settles it outright.

**And the corollary that cost the most:** the wrong mechanism carried a wrong *prognosis*. "R−1 is
locked out" implies more wall-clock cannot help; "one rank is 53 samples short" implies it very
nearly could. A published claim about what *will not work* inherits every weakness of the diagnosis
behind it.

Related: **45** (read the definition, not the label) — 47 is the same discipline applied to
mechanisms rather than quantities. Also **40**: a conclusion inherits the soundness of its
derivation, not the truth of its result — here the result ("never re-learned") was true throughout,
which is exactly why the faulty derivation survived so long.

**48. Before fitting a recorded set of numbers, open the script that produced them.** Controls test
whether your check could fail. They cannot test whether your *quantity* is the right one, because the
symbol's definition lives somewhere else — and a script that fits four numbers correctly, with every
control passing, will state a confident wrong answer.

This fired on #85 (2026-07-29). The corpus records four energy-delivery laws as ε_D/ε_S ∈ {2, √2, 1,
½}. A new instrument reproduced all four as ε_mode ∝ k^p at p ∈ {0, ½, 1} and concluded there were
three laws rather than four, with a two-way fork remaining. Every control passed, including a real
anti-control showing the family could not fit 3, 1/3 or 4. But ε is a **stiffness** — fixed by
⟨f²⟩ ∝ 1/ε and ω ∝ √ε in two scripts that both predate the new one — and the fit had read it as an
**energy**. The two constructions agree at p = 0 and nowhere else, so the agreement at √2 and 1 was a
coincidence of small powers of 2.

**Why four points is not reassuring.** A one-parameter family sweeping a continuum will pass through
small integers and their square roots, and the corpus's characteristic ratios are all built from 2.
Four hits looks like confirmation and is nearly free. The fifth point is what discriminates: the
zero-point law lands on **4** under the correct algebra and on √2 under the wrong one, and the
recorded set contains neither.

**The tell you can act on.** If the numbers you are fitting came from somewhere — a script, a table,
an earlier note — then their definition came with them, and reading it costs one file open. If they
came from nowhere, that is the finding, and no fit should be attempted at all.

Related: **42** (the proxy is not the quantity) — 48 is 42's *preventive* form, since 42 is normally
discovered after the fact. **45** (a field's name is not its definition) is the same discipline for a
single number; 48 extends it to a set. And **46**: the withdrawn script's controls were not weak or
tautological, which is the uncomfortable part — strong internal controls do not reach outside the
file they live in.

**49. A control count is a claim, and it goes stale the moment the script grows.** Every "N controls"
in the corpus tells a reader how hard a result was tested. It is written once, when the script is
first described — and then controls get added, and nobody re-counts. `scripts/control_count_sweep.py`
checks all of them against the scripts they name.

First run, 2026-07-29: **18 claims, 6 wrong** — three found by hand and three by the sweep, spanning
docs/, working logs and the ledger. Every one was written the same day as the script it described.
The over-stated ones are what matter: an under-stated count is merely stale, an over-stated one claims
testing that was never done. This is protocol **46**'s defect (a count that overstates the evidence)
arriving by drift instead of by tautology, which is why 46's discipline does not catch it — 46 asks
whether each check *can fail*, and these checks all could.

**Why the sweep does not rewrite.** Control counts live in prose that also says what the controls
*found*, and no substitution can tell a stale count from a deliberate count of a subset. It reports
and stops; the fixes are manual, one at a time.

**Run it after any session that adds controls to an existing script** — that is the exact motion that
breaks the claims, and it is invisible to every other check in this file.

**50. Before recording a finding as NEW, search the shelf for it.** Deriving something correctly is
not the same as finding it. A result you reached by thinking is new *to you*; whether it is new *to
the corpus* is a separate question with a cheap answer — one grep — and skipping it produces write-ups
that overstate what a session bought.

This fired twice on 2026-07-29, in the same session, in two different ways:

- **#2.** I graded a live docket against α_dark ≈ 3.2 and reported that it "does not reproduce in any
  convention." The value had been **retracted eleven days earlier**, in the same file I was writing
  into — *"wrong sign in the gauge channel"*. I checked the number and not its status.
- **#13.** I recorded the bounded-density lane H² ∝ ρ(1 − ρ/ρ_c) as the route my earlier answer had
  missed. The corpus names it in **three** places and had already graded it *un-derived, named in the
  reconstruction, not stocked*. One of those three even says *"searching the corpus does not turn up a
  completed derivation"* — the search had been done, and recorded, and I did not read it.

**The two failure modes are distinct and both are cheap to avoid.** One is a stale *input* (a number
whose status changed); the other is a stale *claim of priority* (a result the shelf already holds).
The first is caught by grepping the quantity's name for RETRACTED/WITHDRAWN before using it. The
second is caught by grepping the finding's own distinctive expression — here `rho/rho_c` — before
writing "this was missed."

**What it costs when you skip it.** Not the physics: in both cases the algebra was right. What breaks
is the *ledger* — a session that reports two discoveries when it made one correction and one
re-derivation leaves the next reader with a wrong picture of where the work stands, which is exactly
what the failures ledger exists to prevent.

Related: **45** (a field's name is not its definition) and **48** (open the script that produced the
numbers) are the same discipline applied to quantities and to number-sets; 50 applies it to *status
and priority*. Also **40**: a conclusion inherits the soundness of its derivation — and a claim of
novelty inherits the thoroughness of the search behind it.
