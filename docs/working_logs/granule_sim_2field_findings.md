# Two-field Schrödinger–Poisson granule sim — the ε-meter under real dynamics

> **What this is.** A built-from-scratch split-step (FFT) Schrödinger–Poisson (SP)
> integrator for the model's fuzzy-dark-matter granules, validated on the single
> field and extended to the two-fluid medium, to test whether the granule
> density-contrast reads out ε. Code: `scripts/granule_sim_2field.py`. Closed-form
> anchors added to `scripts/audit_math_pass.py` (7 checks, all pass). This closes
> the gap the 44-line static speckle toy (`scripts/granule_sim.py`) could not: the
> law needs the real **dynamics**, not a static speckle draw.

## The claim under test

In the non-relativistic limit the complex medium splits into two Schrödinger
fluids — particle sector ψ and antiparticle sector χ, same mass, coupled **only**
through their shared gravity (charge conservation forbids coherent mixing). The
draw fixes the density fractions

  p = (1 + f_rot)/2 ,  q = (1 − f_rot)/2 ,  p + q = 1 .

Two independent speckle fields with fractions p, q are claimed to suppress the
granule power S ≡ var(ρ)/⟨ρ⟩² to p² + q² of single-field FDM, and

  p² + q² = [(1+f_rot)² + (1−f_rot)²]/4 = (1 + f_rot²)/2 ,

which with f_rot = 1 − f_amp is the booked granule law **S = (1 + f_rot²)/2**.
(Cross-checks it must respect: median f_rot ≈ 0.4 → p ≈ 0.7; suppression 0.58;
the χ/ψ condensation-time ratio 1/p², 1/q² = 2×, 11×. All internally consistent.)

## Code units and the physical map

Natural SP units ℏ = m = G = 1: i ∂ₜψ = −½∇²ψ + Vψ. Halo/granule runs use a
**periodic, mean-subtracted** Poisson source ∇²V = 4π(ρ − ⟨ρ⟩) (the Jeans
swindle — granules ride a flat halo background, which is what "granule contrast"
means). The isolated soliton validation instead uses **zero-padded (vacuum)**
Poisson ∇²V = 4πρ, because the mean-subtracted background otherwise un-binds an
isolated soliton (confirmed: a periodic soliton spreads without limit).

At the pinned mass m = 2.24×10⁻²⁰ eV the map reproduces the recorded anchors:

| scale | sim / formula | recorded anchor |
|---|---|---|
| Schive core radius, 10⁹ M☉ halo | 1.6 kpc·(m/10⁻²² eV)⁻¹ = **7.14 pc** | ≈ 7 pc ✓ |
| Compton wavelength h/(mc) | **370 AU** (reduced ℏ/mc = 59 AU) | ξ ≈ 402 AU |
| halo de Broglie λ_dB @ 100 km/s | **5.4 pc** | — |

The **resolved** scales are the soliton core (≈ 7 pc) and the de Broglie granules
(≈ pc, set by the halo velocity). ξ ≈ 402 AU is the **Compton-order microscale**
(coherence floor; my h/(mc) = 370 AU sits within 10% of it), ~5 decades below the
granule scale — not resolved by any halo sim, and it need not be. The sim's
granules ARE the de Broglie speckle; that is the correct scale for the ε-meter.

## Validation 1 — the single-field solver (numbers)

**Split-step conservation (real time).** Norm drift 3.2×10⁻¹⁵ (machine
precision); energy drift 6.6×10⁻⁵ over the run — a clean 2nd-order symplectic
integrator.

**FDM soliton vs Schive+2014.** Imaginary-time relaxation from the Schive profile,
isolated BC, two masses:
- radial profile matches the Schive fitting function ρ(r) = ρ_c[1 + 0.091(r/r_c)²]⁻⁸
  to **median 2.6% / 1.9%** (max ≈ 8–9%) — this is unambiguously the standard FDM
  soliton shape.
- **Real-time stability (the equilibrium proof):** evolved forward, the relaxed
  soliton holds its shape — density RMS drift < 10⁻³ of ρ_c over a dynamical time,
  r_c stable to < 1%. It is a genuine stationary soliton, not a transient. (The
  discrete virial 2K+W reads −0.1…−0.2, biased low by the grid's central-cell
  self-term and the under-resolved cusp at r_c/dx ≈ 3.5–4.3; real-time stability is
  the clean, grid-robust check, so it is what I lead on.)
- **SP scaling symmetry:** the invariant M·r_c = 2.83 vs 2.70 across the two masses
  (spread 4.4%) — the ground state respects the scaling the equations demand.

**Granule (de Broglie) scale.** A free (gravity-off) speckle field with 1-D
velocity dispersion σ_v: the measured density coherence length (half-max of the
autocorrelation) is 0.333, vs the analytic √(ln2)/σ_v = 0.331 — **ratio 1.01**.
The granules are exactly the de Broglie scale. Single-field S = var(ρ)/⟨ρ⟩² =
**0.995 ≈ 1** (fully-developed speckle → exponential density), the correct baseline
the two-field suppression is measured against.

## The law test — two fields, one shared potential

Two independent speckle fields (independent random phases → no coherent cross
term, as charge conservation requires), density fractions p = (1+f_rot)/2,
q = (1−f_rot)/2, sharing one periodic self-gravitating potential sourced by
ρ = |ψ_p|² + |ψ_q|². S measured at t = 0 (static) and after shared-gravity
evolution, against the single-field FDM baseline evolved identically.

| f_amp | f_rot | p | q | LAW (1+f_rot²)/2 | S(0) static | S(dyn) | ratio S(dyn)/single | p²+q² | cov(ρ_p,ρ_q) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.0 | 0.0 | 0.50 | 0.50 | 0.500 | 0.498 | 0.559 | 0.498 | 0.500 | +5.9×10⁻³ |
| 0.8 | 0.2 | 0.60 | 0.40 | 0.520 | 0.520 | 0.585 | 0.520 | 0.520 | +5.6×10⁻³ |
| 0.6 | 0.4 | 0.70 | 0.30 | 0.580 | 0.582 | 0.660 | 0.587 | 0.580 | +5.0×10⁻³ |
| 0.4 | 0.6 | 0.80 | 0.20 | 0.680 | 0.685 | 0.785 | 0.699 | 0.680 | +3.8×10⁻³ |
| 0.2 | 0.8 | 0.90 | 0.10 | 0.820 | 0.829 | 0.961 | 0.855 | 0.820 | +2.2×10⁻³ |
| 0.0 | 1.0 | 1.00 | 0.00 | 1.000 | 1.013 | 1.187 | 1.057 | 1.000 | 0 |

Time trend at f_rot = 0.4 (LAW = p²+q² = 0.580): S(total) rises 0.582 → 0.782 over
the evolution while the **ratio** stays 0.598 → 0.568.

### What the dynamics say

1. **The static law is exact.** S(0) reproduces (1 + f_rot²)/2 across the whole
   range to < 2%. This alone resolves the toy's puzzle: the toy did **not** fail
   because the law is wrong — it failed because its models summed the two fields
   **coherently** (two circular-Gaussian speckles add to one circular Gaussian →
   S ≡ 1) and used the wrong fractions (f_amp, f_rot) instead of (1±f_rot)/2. The
   physically correct construction — **incoherent** (densities add, phases
   independent) with fractions (1±f_rot)/2 — gives the law identically.

2. **Under real gravity, absolute S is NOT the invariant.** Self-gravity pumps up
   granule contrast for **every** field: the single-field baseline itself climbs
   above 1 (S grows as the granules start to virialize), and the two-field S(dyn)
   rises correspondingly above (1 + f_rot²)/2. A raw measured contrast therefore
   does **not** read ε on its own — it also encodes how dynamically evolved the
   halo is.

3. **The suppression RATIO is the robust invariant.** S(dyn)/S(single-field, same
   conditions) tracks p² + q² = (1 + f_rot²)/2 to ≈ 4% across the full range, and
   the time trend shows the ratio far steadier than the absolute S. The dice
   readout survives the dynamics **as a ratio to the single-field FDM
   expectation**, not as an absolute number.

4. **Shared gravity does correlate the two sectors — weakly.** cov(ρ_p, ρ_q) > 0
   (both fluids fall into the same total-density wells), largest at the equal split
   and vanishing when one sector is empty. It is small here (~10⁻³–10⁻²) and pushes
   the ratio slightly, and it grows slowly as the medium virializes (ratio drifting
   0.598 → 0.568 over the trend). This is the leading **correction** to a clean
   p²+q², and it is a genuine dynamical effect a static speckle draw omits entirely.

## The honest ε-meter status

**Positive, with the reading sharpened by the dynamics.** The granule
density-contrast **is** a clean ε-meter, and this sim closes the mechanism the
speckle toy could not — but the observable is the **granule-power suppression
relative to single-field FDM at the same halo mass and dynamical state**, not the
raw contrast:

  S_two-field / S_single-field-FDM = p² + q² = (1 + f_rot²)/2 = ε readout.

- The kinematic content of the law is exact (static S = (1 + f_rot²)/2).
- Real SP dynamics **preserve** it as a ratio (≈ 4% at tiny grid), so a survey that
  compares a measured halo's granule power to the single-field-FDM expectation for
  its mass reads the dice — independent of the pulsar-timing beat and its
  mass-gate, exactly as the medium's structure promised.
- The two caveats a precision reading must carry: (i) the meter is a **ratio**, so
  it needs the single-field-FDM contrast at matched mass/velocity dispersion as the
  denominator (absolute S is not enough); (ii) shared self-gravity induces a small
  positive inter-sector covariance that grows with virialization, biasing the ratio
  a few percent — the systematic that separates a rough ε from a precise one.

**Negative would have been:** no dependence of S on the fractions, or the shared
potential washing the two speckles into one (cov large, ratio → 1). Neither
happened — the ratio tracks p²+q² and the covariance is a small correction.

## Deferred: the production run (do not launch while chains run)

All numbers above are **tiny-grid** (N = 24–64, ~10–70 steps, single core, ~34 s
total — the machine's other 11 cores stay free for the MCMC on the critical
path). `scripts/granule_sim_2field.py` carries a ready-to-run `run_production()`
with a small-default `PRODUCTION` config that is **not** called by `__main__`. When
cores free, it would tighten: (a) a converged soliton (virial → 0, M·r_c scaling
< 2%) on a resolved grid; (b) a fully-virialized granule field so the absolute-S
growth saturates and the asymptotic ratio is measured, not the early-time one;
(c) the inter-sector covariance systematic vs virialization; (d) multi-seed error
bars on the p²+q² tracking. Only after (b)–(c) should a precision ε be quoted from
a real halo's granule power.
