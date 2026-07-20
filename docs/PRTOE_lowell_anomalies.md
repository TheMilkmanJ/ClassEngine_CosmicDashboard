# The Low-ℓ CMB Anomalies — the Cavity's Line Spectrum (2026-07-11)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*Thread 5 of the atom-grammar survey. Status: computed and graded — the cavity computation is in,
it relocates the test from the power spectrum to the off-diagonal covariance, and it hands the
BipoSH referee a specific pattern. The model gives the
large-angle anomalies a HOME and, distinctively, ONE SHARED AXIS with two registered
predictions. The improvement: standard cosmology must call these flukes (and pays a ~0.1%-class
look-elsewhere embarrassment); the model expects them as a family.*

## 0. The anomalies (real features, officially accidents)

At the largest angles the CMB persistently misbehaves: the low quadrupole (less power at ℓ=2
than ΛCDM predicts), the quadrupole–octupole alignment ("the axis of evil"), the hemispherical
power asymmetry, parity preferences. Each is 2–3σ-ish; ΛCDM's verdict is cosmic variance plus
a posteriori selection — permanently unexplainable BY CONSTRUCTION, since ΛCDM's largest
scales are statistically isotropic and Gaussian by assumption.

*(The cold spot is routinely listed alongside these and is a different kind of object —
localized and sign-definite where these are directional. The model's machinery breaks the
isotropy assumption and not the Gaussian one, so it reaches the four above and not that one;
the verdict is in [PRTOE_cmb_anomalies.md](PRTOE_cmb_anomalies.md).)*

## 1. The model's structure: the universe is a cavity with a spectrum and an axis

Three recorded/graded objects bear directly on the largest angles:
1. **The torus** (P-013, flat, compact — the omk run re-confirmed the model keeps it): a
 compact topology DISCRETIZES the largest modes — the "missing" ℓ=2 power is the cavity's
 infrared mode cutoff (no modes longer than the box). The atom reading (§10, recorded): the
 low-ℓ sky is the cavity's LINE SPECTRUM — the cycle odometer.
2. **The winding axis** (graded): the n ≠ 0 winding singles out ONE DIRECTION on the
 sky — the natural seed for alignment/asymmetry families. Standard cosmology has no axis;
 this model cannot avoid having exactly one.
3. **The axis is SHARED and already registered twice**: P-2026-024 (the ε-dipole) and
 P-2026-029 (the winding comb, fundamental ℓ₁ ≈ 31–94) both point along it. The anomalies join a THREE-member
 family with two falsifiable siblings: **the axis-of-evil direction should coincide with the
 comb axis and the ε-dipole axis.** One direction, four phenomena — or the family dies
 together.

## 2. The improvement, stated precisely

**The cavity computation** (`scripts/torus_lowell_pattern.py`). Summing the torus's discrete
mode lattice against the continuum for a scale-invariant potential at the recorded
last-scattering distance, with the integrated Sachs–Wolfe term carried alongside the ordinary
one: the suppression is confined to the lowest multipoles and dies away by ℓ ≈ 4 — the
observed pattern. At the smallest torus the matched-circles nulls permit (L ≈ 27.6 Gpc) the
quadrupole retains **90%** of its power, and no other multipole moves by more than half a
percent.

**A finite box is a lattice, not a low-k cutoff, and the difference is the whole depth.** The
natural estimate — integrate the continuum and discard everything below k_min = 2π/L — returns
49% at this floor. It is wrong in a specific way: a torus does not *empty* the region near
k_min, it *concentrates* it, putting six modes exactly at k_min carrying their full cells'
weight. Done as the mode sum the calculation actually is, the same box retains 90%. The
estimate and the sum are checked against each other in the script, which also verifies the sum
two independent ways — shell multiplicities under the addition theorem against a mode-by-mode
sum over spherical harmonics, agreeing to five decimals — and confirms that retention returns
to unity as the box grows.

**What that is worth, with the error bar attached.** The quadrupole carries 63% cosmic
variance — five modes, irreducible by any amount of data. Against that scale: the observed
deficit sits about 1σ below expectation, this prediction sits 0.16σ below, and the two are
roughly **0.9σ apart**. So the honest statement is neither that the model predicts the anomaly
(the data does not demand any particular depth) nor that it falls short (the data cannot
resolve the difference): **the mechanism produces a suppression in the right place, of a size
the quadrupole alone can never grade.**

**Three ways to deepen it were computed, and all three fail for one structural reason** —
suppression requires *removing* long-wavelength modes, and none of them removes any.
Anisotropy shallows the effect (long axes keep supplying the modes a short axis takes away);
the integrated Sachs–Wolfe contribution is sourced where the relevant modes sit above the
cutoff, so adding it dilutes; the winding modulation is multiplicative, so it convolves power
upward rather than removing it. What the torus gives is what it gives.

**The shape is not gradeable either.** Scoring the whole pattern across ℓ = 2–6 against cosmic
variance gives a total signal-to-noise of **0.16**. The power spectrum — diagonal, a handful of
modes per multipole — cannot see this torus at all, at any multipole, in any combination. That
closes the entire power-spectrum route, not just the quadrupole.

**Where the test actually lives: the correlations a torus makes and isotropy forbids.** A
compact space breaks statistical isotropy, so the covariance of the sky's harmonic
coefficients is not diagonal — and the off-diagonal entries carry the information the spectrum
does not. Over ℓ = 2–6 alone there are **990 independent pairs against five power-spectrum
numbers**, of which 111 are non-zero, and computing them at the recorded torus size gives a
total signal-to-noise of **1.4** — modest, and it is the only channel that has any.

**The predicted pattern, specific enough to look for** (correlation coefficients in the cube's
own frame; the overall sign of the ℓ ↔ ℓ ± 2 family is a phase convention, the relative signs
are not):

| pair | ρ |
|---|---|
| (ℓ = 4, m = −4) × (ℓ = 4, m = +4) | +0.47 |
| (ℓ = 2, m = −2) × (ℓ = 2, m = +2) | +0.38 |
| (ℓ = 6, m = −6) × (ℓ = 6, m = +6) | +0.37 |
| (ℓ = 3, m = 0) × (ℓ = 5, m = 0) | −0.36 |
| (ℓ = 3, m = ∓3) × (ℓ = 5, m = ±5) | +0.33 |
| (ℓ = 3, m = ∓1) × (ℓ = 5, m = ∓1) | +0.28 |

Every non-zero entry obeys the cube's own selection rule — Δm ≡ 0 (mod 4) and ℓ − ℓ′ even, the
signature of its four-fold symmetry about each axis and its inversion symmetry — and the
covariance comes out real to machine precision, as that symmetry requires. The strongest
entries are m ↔ −m at fixed multipole and ℓ ↔ ℓ+2 at fixed m, which is what "alignment" means
when written in harmonic coefficients, and therefore where the quadrupole–octupole alignment
claims live. **The referee already exists on the calendar (the BipoSH joint pass); what was
missing until now was a prediction to hand it.**

*(The integrated Sachs–Wolfe term costs the pattern about a third of its reach: on the ordinary
Sachs–Wolfe term alone the same torus scores 2.0, and the ISW's near-isotropic power adds to
the diagonal without adding to the off-diagonal. That is the same dilution that shallows the
quadrupole, showing up in the channel the test actually lives in.)*

Not "the model explains the anomalies". What is computed above is the torus's own prediction;
what is not built is the **confrontation** — a low-ℓ likelihood that scores a measured covariance
against the pattern in the table, which is the BipoSH pass's job and is analysis-limited rather
than theory-limited. The improvement is structural: ΛCDM
CANNOT expect these features even in principle; this model REQUIRES a discretized large-scale
spectrum and exactly one preferred axis, and it has independently pre-registered where that
axis is testable. The anomalies convert from embarrassments-of-chance to
predictions-in-waiting.

## 3. The honest risks

- The torus size (L ≥ 27.6 Gpc) risked being too large for the mode cutoff to explain the low
 quadrupole quantitatively. The cavity computation settled it, and the answer is split: the
 suppression *does* land where the anomaly is (confined to the lowest multipoles, dying by
 ℓ ≈ 4), but at 90% quadrupole retention it is far below what cosmic variance can resolve.
 So thread (1) does not weaken to aesthetic — it **relocates**, out of the power spectrum
 (total S/N 0.16, unusable at any multipole) and into the off-diagonal covariance
 (S/N 1.4, 990 pairs over ℓ = 2–6). The claim survives with its test moved, not lowered — but
 the channel it moved to is thinner than the first pass reported, and 1.4σ of structure is not
 something a single analysis will settle.
- Planck's isotropy analyses constrain dipolar power modulation at large scales — the same
 BipoSH class flagged for the comb; the family must survive it jointly.
- A measured axis-of-evil direction INCONSISTENT with a future comb/ε-dipole axis kills the
 family linkage cleanly.

*Standard cosmology looks at the largest scales, sees structure, and files it under luck. This
model looks at the same sky and sees what an atom always shows when you finally view it whole:
lines, and an axis. The cavity computation has now said where the resemblance can be checked —
not in how much power each scale carries, which cosmic variance will never resolve, but in which
scales are correlated with which, where a compact space leaves a pattern isotropy forbids.*
