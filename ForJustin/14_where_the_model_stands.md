# 14 — Where the model stands after 2026-07-19/20, and what needs you

**Written to survive the conversation.** Two days moved the hierarchy chain more than anything since
the basement rebuild, and one long overnight session closed the audit machinery. This is the
consolidated picture: what changed, which direction it ran, and the four things waiting on your call.
Everything here is verified against the files; nothing is a fresh claim.

## What got stronger

**The gap equation is solved.** k = ln(1 + π/2α_c)/π reconstructs *exactly* — Monte-Carlo confirmed —
as the Fermi-surface average of a Thomas–Fermi-screened Coulomb exchange in the particle-hole
channel, with the screening constant b = 2α_c/π falling out of standard pieces and no chosen ones.

**The pairing channel is decided, and host-independently.** A particle-particle condensate of two
charge-e fermions gives the photon an Anderson–Higgs mass ~9.5×10¹¹ eV against a bound of 10⁻¹⁸ —
**excluded by thirty orders.** Particle-hole is forced, not preferred. This is the single most robust
result in the chain: it survives any O(1), any host, and every pass it has been put through.

**α_c's scale is settled by data.** A_s selects 3α(0) at −0.4%, against +28% at α(M_Z).

**One of §6c's conditions turned out to be already supplied.** Keeping the band velocity explicit
gives b = 2α_c/(πv), so the booked constant is that at **v = 1** — and a linear node *is* a cone whose
slope defines the emergent light speed, so the recorded Fermi point supplies it free. Worth knowing
because it is the first thing a condensed-matter reader attacks: graphene's analogous velocity is
c/300, which is exactly why its effective coupling is O(1) rather than O(α).

## What got weaker, and this is the honest half

**The anchor is a mechanism, not a measurement.** The chain runs end to end, but ∂lnM/∂lnk = 33.5
amplifies every O(1), so the value is **1–8 TeV, not 1.57 TeV at 2.5%**. The +0.14% agreement with
4πm_H is a coincidence of one convention inside that band. The dominant uncorrected term is the
crossed-box vertex correction, whose conventional sign is **downward** — so the honest reading is
that the band's lower half is favoured.

**k's exactness rides a host the corpus does not have.** The derivation needs a Fermi surface at
finite μ with two velocity-matched bands; the recorded basement is a Fermi point at μ = 0, which §6a
shows cannot pair at this coupling at all. **This is the hierarchy chain's largest open exposure**,
and it is now precisely stated rather than gestured at:

- Three routes to the finite μ were walked and all three fail — the corpus's own finite-μ language
  (that is the dark condensate at basin entry, sixty orders below), the model's own matter asymmetry
  (η = 6.14×10⁻¹⁰ leaves k_F/T short by ten orders, and the shortfall *is* η's smallness so no
  re-pricing closes it), and the hot reading (which misses the screening constant by 1.6–2×).
- The "two bands" condition is sharper than it sounds. The Planck-floor roster is the SM's 48 Weyl
  fermions plus three right-handed neutrinos, and Thomas–Fermi counts species carrying *density*, so
  the factor 2 asserts **exactly two of fifty-one are doped off the node**. Nothing recorded selects
  the pair.

**The chirality family cannot name which handedness means matter, and that is now proven rather than
owed.** The genesis tilt is invariant under θ → π/2 − θ while the charge L = R²θ̇ is odd under it, so
the uniform release prior splits exactly evenly — verified three ways to machine precision, at every
tilt strength, and robust to any CP phase in the tilt. The absolute sign is *forbidden by a symmetry
the model does not break*, not merely uncomputed. What might still survive is the **relative** lock
between rotation and winding, and no solver in the corpus can compute it: one carries time evolution
without winding, the other winding without time evolution.

## The evidence run

**Healthy, not stalled — and I got this wrong before getting it right.** I escalated the ~33 hours of
zero output as a possible failure before reading the sampler's configuration. PolyChord checkpoints
every `update_files` = nlive = 400 iterations, and `measure_speeds` built a four-block hierarchy at
534 slice steps per live point, so one write interval is tens of hours. The absent log(Z), dead-point
file and `.stats` are what interval one looks like from outside.

**But the throughput is the real content.** The only completed nested run on this stack (archived
ΛCDM, 2026-06-20) closed at 1809 iterations, which puts this one at **≥ 6 days before the ΛCDM twin,
and the twin doubles it**. That figure is an *inference* from the schedule and one benchmark, not a
measurement — **the first dead-point file is what converts it**, and as of 41.7 h elapsed it has not
appeared.

One thing worth knowing separately: the `.stats` files sitting in `chains/` for these models are
**minimizer** outputs (`nlive: 1`), not nested evidence. That is the correct provenance for a Laplace
ΔlnZ, and every file labels the +2.635 correctly — but the filenames read like finished evidence runs
to a stranger.

## What the audit found, and what it says about the corpus

Eleven mis-grades in 110 completed tasks, **all of them in composite ("A + B + C") tasks and none in
roughly a hundred single-object checks.** Two structural gaps closed: 542 task references that no
repo reader could resolve now have an index, and the propagation rule finally caught its last two
carriers — one of which was a *heading* contradicting its own section.

**Set against that: every test built to find the corpus dirty came back clean.** Seven of ten payoff
checks, five of six wave-9 tasks, three of three heading spot-checks, and the registry's harness
coverage. The documentation discipline is good; the defects cluster in exactly two places —
composite-task bookkeeping and retraction propagation — and those two now have machinery.

## My own error rate, because it bears on how to read the above

Full accounting is in `ForJustin/13`. The short version: **three of my claims in that session were
wrong and I caught all three**, but the worst reached four files before I did — I asserted the model's
Σm_ν prediction did not reproduce, using a Δm²₃₁ that is not the right one for normal ordering, when
the harness had it guarded three ways. Fully reverted. The failure mode inverted between the two
measured days: from over-claiming favourable results to **over-claiming absences**, which is cheaper
to commit and harder to catch, because an absence produces no contradiction to trip over.

**Point audits at anything I reported as missing, absent, stuck, or unsupplied.**

## The four things that need you

1. **#99 — the evidence run's horizon.** Nothing to decide until the first checkpoint lands, unless
   you want it stopped now. The ≥6-day floor is inference; the dead-point file makes it real.
2. **ForJustin/12's sequencing.** Item 5 is three-quarters delivered (the vanilla-CLASS diff, the
   stability page, the varying-m_e comparison); the fourth part needs chains free. Items 1–4 need
   your order, and item 4 competes with the chains for cores.
3. **The paper's framing**, and whether anything publishes before PolyChord speaks.
4. **Two builds, both scoped to hand off.** #141 is the crossed-box vertex correction — the object is
   named, the prior is adverse, and the file records why two previous *arguments* failed where an
   integral is wanted. #154 is the joint genesis draw: evolve the six-channel phase configuration
   through the roll-up and read sign(θ̇) against sign(n) on one trajectory.
