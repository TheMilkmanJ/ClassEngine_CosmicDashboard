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
out to follow from something already in hand), or **gated** (named the specific external thing it
waits on — a run, a lattice number, a measurement). "Owed" on its own is none of those.

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
