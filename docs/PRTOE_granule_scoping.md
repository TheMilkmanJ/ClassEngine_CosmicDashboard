# The Granule-Meter Scoping Study & The Mass Pin (2026-07-07)

> **DATE NOTE (2026-07-13 pass):** this file's header predates the derivation-hunt/freeze era; statuses herein may be superseded — current conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*Two jobs from the morning board: scope whether the granule channel — the
SOLE surviving ε-meter after the reconciliation audit — can ever actually
be read; and pin m inside the audited band [1,3]×10⁻²¹ eV. Every number
re-derived at booking; literature cite-pulled this morning.*

## 1. The instrument: what the granule meter measures

Two incoherent fields (ψ, χ) with number fractions p² = (1+f_rot)/2,
q² = (1−f_rot)/2 each produce speckle; total granule POWER relative to a
single field of the same total density:

    S = p⁴ + q⁴ = (1 + f_rot²)/2,    f_rot = 1 − f_amp

- Free FDM (single field): S = 1.
- Full librator (f_rot = 0): S = 0.5 — the meter's floor.
- **Dice median (f_amp ≈ 0.55–0.67): S ≈ 0.55–0.60.**
- The meter's whole dynamic range is a factor of 2, and the dice
  concentrate near the suppressed end: the target signal is a
  **~40% granule-power deficit** relative to free FDM at the same m.

Everything granule-driven scales with S: heating rates ∝ S, relaxation
times ∝ 1/S (×1.7 at the median), stream-perturbation power ∝ S.

## 2. Feasibility: single objects CANNOT do it; populations CAN

Requirement: distinguish S ≈ 0.58 from S = 1. With per-object
heating-rate calibration honest at ~50% (current sims-vs-data modeling
scatter is at least this):

| sample | σ(S)/S | detection of the deficit |
|---|---|---|
| 1 dwarf | 50% | 0.8σ — hopeless |
| 10 dwarfs | 16% | 2.7σ — marginal |
| 30 dwarfs | 9% | **4.6σ — real** |
| 100 dwarfs | 5% | 8.4σ |

**Verdict: the granule meter is a POPULATION statistic.** It is out of
reach for any single system today, and genuinely reachable with a
Rubin-era UFD census (30+ systems with kinematics) IF per-object
modeling holds at ~50%. The make-or-break (turn-58 binding) therefore
splits: (a) the two-field sims must confirm S = (1+f_rot²)/2 at the
~10% level (spec in §5), and (b) the observational program needs N ≳ 30
dwarfs — a date with Rubin, not a wall.

Corollary booked in the model's favor: **ignoring S biases heating-fit
masses only by S^⅓ = 0.83 (16% low)** — smaller than current modeling
errors, so every free-FDM heating bound we INHERIT (DK included)
transfers safely. The inheritance license survives its own correction.

## 3. The coupled estimator: the pin and the meter are ONE fit

The core radius reads m (Schive core–halo: r_c ≈ 1.6 kpc
(m/10⁻²²)⁻¹(M_h/10⁹M☉)^(−⅓)); the heating rate reads m³/S. Neither
observable reads its parameter alone — and the dyad adds structure free
FDM lacks: cores are ψ-only where χ is uncondensed (Room 5's ×11 lag),
so core-halo normalization carries f_rot and condensation age. The
honest instrument is a JOINT (m, f_rot) fit over a dwarf population
using three observable classes at once: core sizes, heating rates,
core-halo normalization vs redshift/halo-age.

## 4. The mass pin: literature triangulation + a reconciliation hypothesis

Band mapping (Schive at M_h = 10⁹ M☉): m = 1×10⁻²¹ → r_c = 160 pc;
2×10⁻²¹ → 80 pc; 3×10⁻²¹ → 53 pc — the V2 window [60, 200] pc IS the
audited band, consistently.

Literature pulled at booking:
- **Hayashi, Ferreira & Chan 2021 (ApJL 912, L3): 18 UFDs — most
  prefer m > 10⁻²¹ eV.** Reinforces the audited band's bottom from
  data, independently of this morning's audit.
- **Safarzadeh & Spergel 2020 (ApJ 893, 21): MW satellite kinematics
  demand m < 10⁻²¹ and declare free FDM INTERNALLY INCOMPATIBLE**
  (no single m fits Fornax-class and UFD-class systems together).
- Calabrese & Spergel 2016 (MNRAS 460, 4397): Draco II + Tri II
  prefer 3.7–5.6×10⁻²² (below band; two-object fit, superseded in
  spirit by the 18-UFD sample).

**The dyad's angle — booked as HYPOTHESIS, sims-owed:** the free-FDM
"incompatibility" assumes one field, one universal core-halo relation.
The dyad breaks exactly that assumption: χ-lagged halos sit OFF the
universal relation (younger/lighter cores at fixed halo), by amounts
that depend on halo age and f_rot. The mutually-contradictory free-FDM
fits could be the lag SHOWING — the tension in the literature is, on
this reading, evidence-shaped rather than exclusion-shaped. Grade:
consistency-hypothesis until the two-field sims produce the predicted
scatter PATTERN (older halos closer to the universal relation; younger
ones below it). This is P-2026-00X material only after sims — the
Pinning Rule applies and this function is not yet pinned.

**PROVISIONAL PIN: m ≈ 1–2×10⁻²¹ eV** — bottom held by Hayashi+ (most
UFDs > 10⁻²¹) and the audit's A1; top disfavored softly by the same
UFD core sizes (53 pc cores at 3×10⁻²¹ sit below most measured
half-light radii) and watched by M87*. Point estimate honesty: this is
a lean, not a measurement; the joint (m, f_rot) population fit is the
measurement.

**Superradiance graduation status: NOT GRADUATED.** The provisional
lean (1–2×10⁻²¹) sits below the M87* exclusion floor (2.9×10⁻²¹), so the
free-vs-condensate discriminator remains live-IF-heavy. It graduates
only if the joint fit lands the mass in the top third of the band.

## 5. The sim spec (the make-or-break, concretely)

Minimum viable campaign, runnable on existing public codes
(PyUltraLight/UltraDark-class, two-field extension is a config-level
change since ψ and χ share m and couple only through gravity):

1. **S-calibration runs:** matched halos, f_rot ∈ {0, 0.4, 0.8, 1},
   single-field control; measure granule power spectrum and star-particle
   heating; target: confirm S = (1+f_rot²)/2 to ~10%.
2. **Lag runs:** same grid, track soliton formation epoch per field;
   target: the core-halo scatter pattern of §4's hypothesis.
3. **Stream runs (stretch):** GD-1-like stream on the f_rot grid;
   target: whether stream heating adds an independent S readout.

Deliverable per run: S_measured, τ_condense(ψ,χ), core-halo offset.
Kill condition (binding, from the internal review): if sims show granule
observables CANNOT separate S = 0.58 from 1 at population scale, ε is
unobservable, full stop, and the dice edifice is physics without a
readout.

## 6. Fairbank/evidence note (same morning, for the record)

ΛCDM is NESTED in the dyad at varying_me = 1 (the fluid background is
ΛCDM-identical by proof; ξ executed). Therefore the running Fairbank
posterior yields a real Bayes factor WITHOUT PolyChord via
Savage–Dickey: B = π(m_e=1)/p(m_e=1|data). Machinery delivered
(scripts/savage_dickey_dyad.py, runs turn-key on the converged chain).
Preview at R−1 ≫ 0.05 (NOT quotable): varying_me = 1.0126 ± 0.0041
(3.0σ from ΛCDM), ln B ≈ +2.9 dyad-favored. Caveats stamped: chain
unconverged; Gaussian density approximation; prior-width dependent
(flat [0.98, 1.04] — halving the prior width halves B; the prior is
physical, from quasar/BBN-adjacent bounds, and must be defended as
such when quoted). PolyChord remains necessary for the NON-nested [2026-07-13: the zero-parameter PolyChord run is now LIVE — this requirement is being executed]
comparisons and as the S-D cross-check; it is no longer the only door
to an evidence number.

## GRANULE-POWER FORMULA CONFIRMED (Tier-3 partial, 2026-07-07)

Ran the statistical core of the granule sim: two INCOHERENT wave-DM fields
(ψ=particle, χ=antiparticle), each a Gaussian speckle field, total density
ρ = |ψ|² + |χ|². Measured granule power S = Var(ρ)/mean(ρ)² vs the
predicted p⁴+q⁴ = (1+f_rot²)/2.

RESULT (N=2×10⁶ cells): S = (1+f_rot²)/2 CONFIRMED to <1% at f_rot = 0, 0.4, 0.8,
1.0. (An initial 10% offset at N=400 was heavy-tail under-sampling, resolved by
high statistics.) So the ε-meter's LOAD-BEARING number is verified: the
dice-median f_rot~0.4 (f_amp~0.6) gives S~0.58 → granule heating suppressed ~40%
vs free FDM. This is the number dwarf-heating / stellar-stream data would test.

STILL OWED (the bigger Tier-3 piece, needs a real SP integrator, not statistics):
  - full Schrodinger-Poisson DYNAMICS (self-gravity, soliton formation);
  - the ψ/χ CONDENSATION LAG (Levkov rate, Room 5 χ-lag) -- needs time
    evolution to produce the redshift-dependent core-halo scatter pattern;
  - mapping S → actual dwarf-heating rate and comparison to real SPARC/stream data.
Status: statistical core DONE (S-formula confirmed); dynamical sim + data
confrontation NOT started (infrastructure).

## CHI-LAG: analytic scaling confirmed; dynamical sim NOT achieved in-session (2026-07-07)

Attempted a minimal 3D two-field Schrodinger-Poisson sim to demonstrate the
ψ/χ condensation lag DYNAMICALLY. HONEST RESULT: the minimal version (N=32-48,
≤1500 steps) did NOT cleanly condense -- initial contrast was already ~10-13 and
did not grow over the available steps (gravitational Bose-star formation takes many
dynamical times; needs careful ICs far from condensation, a bigger grid, and long
runs with convergence testing). Reported as a failed minimal attempt, not dressed up.

What IS solid: the χ-lag SCALING is analytic (Levkov condensation τ ~ 1/ρ²):
  tau_chi/tau_psi = (p²/q²)²
  f_rot=0.4 → 5.4x ; f_rot=0.54 → 11.2x (matches Room-5 booked ~11x) ; f_rot=0.67 → 26x.

TIER-3 HONEST STATE:
  - S = (1+f_rot²)/2 (granule power): CONFIRMED numerically (<1%).
  - χ-lag = (p²/q²)²: CONFIRMED analytically (Levkov scaling); NOT demonstrated
    dynamically (minimal SP sim failed to condense -- real campaign owed).
  - core-halo SCATTER PATTERN (the observable prediction) + dwarf/stream DATA
    confrontation: NOT done, needs a real SP sim campaign (PyUltraLight/UltraDark-
    class, careful ICs, convergence) = genuine infrastructure beyond a chat session.
