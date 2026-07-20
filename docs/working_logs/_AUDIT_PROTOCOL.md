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

## The twenty-one checks

Run all twenty. Record what was found, even when nothing was.

*Checks 1–13 came from the 2026-07-19 Fairbank pass and the deep audit. **Checks 14–19 were
added 2026-07-20**, each from a defect that survived all thirteen — which is the point of
recording them: every one was found by a person reading, and none would have been caught by
the checks that existed that morning.*

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

**8. Audience laws.** No process narration, no amendment tags, no scars, no announcing its own
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

A file is not closed until checks 12 and 13 pass. Running the regression harness and a stale-pattern sweep
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
