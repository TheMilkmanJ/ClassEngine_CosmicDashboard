# 13 — What my error rate actually looks like, measured, and where to point an audit

**Filed at the owner's direction, for the audits to come.** Not an apology note — a measurement.
Two full days counted the same way: every error made, how each was caught, and which direction it
ran. The useful content is the *pattern*, and the two samples do not have the same one, which is
itself the finding. **The first sample is below; the second follows it, and the failure mode
inverts.**

---

# The first sample: 2026-07-19 (the hierarchy chain's gap equation)

## The count

**Six errors of arithmetic or convention**, all inside quantities the anchor reads at 33× leverage:

| # | error | how it was caught |
|---|---|---|
| 1 | mixed Gaussian and Heaviside–Lorentz in the Thomas–Fermi mass (4πe²N₀ vs e²N₀) | recomputing after the answer looked adverse |
| 2 | read the corpus's ∫₀¹ as a *cut* when it is the full solid-angle average in the natural variable | recomputing after the answer looked adverse |
| 3 | screened with one band where the channel demands two | same recomputation |
| 4 | integrated the pairing shell one-sided; a shell is symmetric about E_F | recomputing after the answer looked adverse |
| 5 | script summary said "about a factor 2 either way" over a table showing 18× | reading the output instead of the summary |
| 6 | script summary said "a factor ~2" over a table showing 13% | same |

**Four favourable arguments**, each plausible, each in the direction I wanted, each wrong:

| argument | why it failed | caught |
|---|---|---|
| Migdal suppression of the vertex correction | Migdal needs a *slow* boson; screened Coulomb is instantaneous. I substituted a length scale for a time scale | before filing |
| "one Dirac cone protects r = 1" | at finite μ one cone has one Fermi surface, so the two pockets must come from different bands — the reading was backwards in consequence | before filing |
| ladder resummation giving a one-sided upward vertex correction | double-counts: the gap equation *is* the ladder sum | at the tabulation stage |
| b = f̄·α_c as a structural identity | algebra — 2α_c/π *is* (2/π)α_c; the two 2/π's have unrelated origins | on writing the number out |

**Two structural imports**, and these are the ones that matter:

1. **The composite Higgs.** I concluded from the particle-hole channel that the condensate *is* the
   Higgs, and priced its S-parameter and flavour exposures across three sections — then amended
   **P-2026-042**, a registered prediction, to say its arrow B was in tension with electroweak
   precision. The model's own §2(c), three sections above where I was writing, says the Higgs is
   **elementary** with an induced mass parameter. All of it withdrawn; the amendment reversed.
2. **The host under the k derivation.** §6c reproduces k = 1.36461191 exactly — but from a cold
   degenerate Fermi surface with Thomas–Fermi screening and two compensated bands, none of which
   the basement has. Grep settles it: "Fermi surface" and "semimetal" appear in this corpus only in
   text I wrote that day.

## The pattern, which is the actionable part

**I check hardest when I dislike the answer.** Every one of the six numeric errors was found by
recomputation, and every recomputation was triggered by an adverse-looking result. None was
triggered by routine. The favourable arguments survived longer precisely because nothing prompted a
second look.

**The imports hid under agreement.** The composite reading felt right because the bilinear's quantum
numbers genuinely do match the Higgs's. The host import hid under an eight-digit numerical match —
which is the hardest possible place to notice one, because the agreement itself reads as
confirmation.

**Volume outran verification.** Eleven sections were appended to one file across several hours, each
committed, and the file was never re-read whole until the end — at which point it was found
asserting a number in nine places that its own later sections disowned. The protocol's first check
is *read the file whole*; I ran it last.

## What to point an audit at

1. **Anything I filed that agrees with something.** Disagreements got recomputed; agreements did not.
2. **Anything where I supplied a mechanism the corpus did not previously name.** Both imports are of
   this shape: the corpus had a form, I supplied a physical realisation, and the realisation carried
   assumptions the corpus does not make.
3. **Registered predictions I touched.** The one amendment I filed was wrong and had to be reversed
   by a second amendment. Standing rule now: re-read a prediction's own statement before amending it.
4. **Not the arithmetic.** 327 harness checks pass and the numeric errors were all caught. The
   arithmetic is the reliable layer; the framing is not.

## What I would stake most and least on, from that day

- **Most:** the pairing is particle-hole, with particle-particle excluded by thirty orders on the
  photon mass. Host-independent, immune to O(1)s, and it survived every pass.
- **Least:** k's derivation. Exact, and conditional on a host the model does not have.

Everything above is in `working_logs/_AUDIT_LEDGER.md` at full length, entry by entry, including the
arguments that were rejected before they reached a physics file. The ledger is the primary record;
this is the summary.

---

# The second sample: 2026-07-20, and the failure mode inverts

A second full day, deliberately measured the same way. **The profile changed, and the change is the
useful part.**

## What happened

**Two errors reached you, and the second one reached the files.** Take the second first, because it
is the worse of the two and it arrived after I had already written most of this page.

**I told you the model's Σm_ν prediction did not reproduce and that its kill margin was half what the
corpus claimed.** Both false. I recomputed the neutrino sum with splittings I labelled "PDG-central
normal ordering" — 7.53×10⁻⁵ and 2.453×10⁻³ — and the second is not the right Δm²₃₁ for normal
ordering at all. The corpus uses 7.42×10⁻⁵ and 2.515×10⁻³, current NuFIT, and its booked 61.4 meV is
correct. **And the harness had already checked it**: the sum sits at line 114 of
`audit_math_pass.py`, with anchor-variation rows at 246 and 252 and the normal-ordering minimum at
289. I added four "new" checks without reading the 328 that were there, and **all four passed —
because they tested my arithmetic rather than the corpus's claim.**

It reached four files before I caught it, including the referee calendar's kill rule and an
audience-facing draft. All reverted; the surviving finding is a 0.15 meV documentation gap in one
parenthetical.

**The rule that would have stopped it, and it is mechanical: before claiming a corpus number does
not reproduce, grep the harness for it.** Three hundred and twenty-eight closed forms are already
guarded. I did not look, on a number that was guarded three ways.

**The first error was smaller and never reached the files.** I reported the PolyChord
evidence run as *"a decision, not a watch"* — thirty-two hours of zero output, four ranks burning
CPU, escalated to you as possible failure. Then I read the sampler's configuration, which I had not
done before escalating. PolyChord checkpoints every `update_files` = nlive = 400 iterations, and
`measure_speeds` had built a four-block hierarchy at 534 slice steps per live point. **Thirty-two
hours of silence was the expected appearance of a healthy run inside its first checkpoint interval.**
I corrected it within the hour, unprompted, but you had already been told something wrong about the
most expensive object on the board. The lesson is narrow and it is not about samplers: **grading
silence requires knowing the writer's cadence, and I graded before I checked it.**

**Five more were caught before they reached anything.**

| what I nearly booked | why it was wrong | what caught it |
|---|---|---|
| a finite chemical potential for the basement, unlocking the hierarchy's conditional derivation | the corpus's "condensate at finite chemical potential" is the *dark* condensate at basin entry — 2.24×10⁻²⁰ eV, sixty orders below the Planck-floor basement | reading which object the phrase names, because the answer was one I wanted |
| a real CP-phase rectification in the genesis draw (residuals ~10⁻² where theory says exactly zero) | the sampling grid was centred on π/4 while the phase moves the symmetry axis to π/4 − δ/4, so the draws stopped pairing | testing the mirror **pair** directly — two integrations — instead of the sum |
| #36 graded UNVERIFIED, its object missing | its home is in `working_logs/`; I had searched `docs/*.md` | widening the search before booking the absence |
| "30/30 from the recorded solver" | the recorded solver's own grid gives 12/12; 30/30 was a separate finer scan | the protocol's check 12, read-the-file-whole, on my own newest prose |
| an automated sweep for the heading-vs-body defect | it flags honest files, which hedge in the body, identically to late-hedging ones | running it and reading the top hits, which were the corpus's *best* sections |

## The pattern, and how it differs from the first sample

**On 2026-07-19 every error ran in the direction I wanted. On 2026-07-20 three of six ran the other
way** — I nearly under-claimed #36, nearly reported a healthy run as broken, and nearly took a
grid artifact as a real physical asymmetry that would have been *adverse* to a clean result. The
first sample's lesson was "I check hardest when I dislike the answer." That reflex now fires, and it
has a cost the first sample could not show: **it produces confident negatives.**

**Over-claiming a negative is the cheaper error to commit and the harder one to catch**, because an
absence generates no contradiction to trip over. A wrong positive eventually collides with something;
a wrong "this does not exist" simply sits there looking like diligence. Both instances today —
#36 and the sampler — were absences read as verdicts.

## What to point an audit at now

1. **Anything I reported as missing, absent, stuck, or unsupplied.** This is the new one, and it is
   the mirror of the first sample's advice. Check the scope of whatever search produced the absence —
   and if the claim is that a *number* fails to reproduce, check the harness before anything else.
   The Σm_ν error and the "no perturbation sector" memory are the same failure at different scales:
   both asserted an absence that the corpus had already filled, and neither survived thirty seconds
   of looking.
2. **Anything I escalated urgently.** The one error that reached you was an urgent escalation, and
   urgency is exactly when the check gets skipped.
3. **Still not the arithmetic.** 327 harness checks pass; every numeric slip in two days was caught
   by recomputation. Two samples now agree: the arithmetic is the reliable layer.

## What I would stake most and least on, from this day

- **Most:** the genesis roll does not select a handedness. It is a symmetry of the recorded tilt, it
  holds for any tilt strength and any CP phase, and it was verified three independent ways to machine
  precision. It is also *adverse* to the model's more interesting reading, which is part of why I
  trust it.
- **Least:** the six-day floor on the evidence run. It rests on one completed nested run from June as
  the only benchmark, and on inferring per-iteration cost from a checkpoint that has not yet
  happened. It is an estimate wearing a number's clothes.
