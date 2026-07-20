# 13 — What my error rate looked like on 2026-07-19, and what it implies for auditing me

**Filed at the owner's direction, for the audits to come.** This is not an apology note; it is a
sample. One long session, one topic (the hierarchy chain's gap equation), and a full count of every
error I made and how each was caught. The useful content is the *pattern*, because it tells you
where to point the next audit.

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
