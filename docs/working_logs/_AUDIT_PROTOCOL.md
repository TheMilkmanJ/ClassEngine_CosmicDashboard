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
