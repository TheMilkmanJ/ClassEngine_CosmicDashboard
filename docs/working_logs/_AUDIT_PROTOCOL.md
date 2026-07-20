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

## The thirteen checks

Run all thirteen. Record what was found, even when nothing was.

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
