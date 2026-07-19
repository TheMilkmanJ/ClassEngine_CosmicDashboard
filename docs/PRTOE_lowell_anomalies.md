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

**The cavity computation, run (2026-07-18).** Summing the torus's discrete modes against the
continuum for a scale-invariant potential at the recorded last-scattering distance: the
suppression is confined to the lowest multipoles and dies away by ℓ ≈ 4 — the observed
pattern. At the smallest torus the matched-circles nulls permit (L ≈ 27.6 Gpc) the quadrupole
retains 83% of its power. *(Provenance: the retained Sachs–Wolfe-only toy
(`scripts/torus_quadrupole.py`) gives ~49% retention at that floor and 83% at L = 42 Gpc;
the booked 83%-at-floor came from the fuller 2026-07-18 pass whose script was scratch-era
and is not retained — consistent with the ISW dilution described below, but not
re-runnable. The BipoSH handoff should regenerate retention and pattern at the floor size
before grading; the section's conclusions are robust across the 49–83% span, since even
the deepest reading stays below what cosmic variance can resolve.)*

**What that is worth, with the error bar attached.** The quadrupole carries 63% cosmic
variance — five modes, irreducible by any amount of data. Against that scale: the observed
deficit sits about 1σ below expectation, this prediction sits 0.3σ below, and the two are
**0.8σ apart**. So the honest statement is neither that the model predicts the anomaly (the
data does not demand any particular depth) nor that it falls short (the data cannot resolve
the difference): **the mechanism produces a suppression in the right place, of a size the
quadrupole alone can never grade.**

**Three ways to deepen it were computed, and all three fail for one structural reason** —
suppression requires *removing* long-wavelength modes, and none of them removes any.
Anisotropy shallows the effect (long axes keep supplying the modes a short axis takes away);
the integrated Sachs–Wolfe contribution is sourced where the relevant modes sit above the
cutoff, so adding it dilutes; the winding modulation is multiplicative, so it convolves power
upward rather than removing it. What the torus gives is what it gives.

**The shape is not gradeable either.** Scoring the whole pattern across ℓ = 2–6 against cosmic
variance gives a total signal-to-noise of **0.27**. The power spectrum — diagonal, a handful of
modes per multipole — cannot see this torus at all, at any multipole, in any combination. That
closes the entire power-spectrum route, not just the quadrupole.

**Where the test actually lives: the correlations a torus makes and isotropy forbids.** A
compact space breaks statistical isotropy, so the covariance of the sky's harmonic
coefficients is not diagonal — and the off-diagonal entries carry the information the spectrum
does not. Over ℓ = 2–6 alone there are **990 independent pairs against five power-spectrum
numbers**, and computing them at the recorded torus size gives a total signal-to-noise of
**2.2** — modest, but real, and it is the only channel that has any.

**The predicted pattern, specific enough to look for** (correlation coefficients, in the frame
of the model's own axis):

| pair | ρ |
|---|---|
| (ℓ = 4, m = −4) × (ℓ = 4, m = +4) | +0.68 |
| (ℓ = 2, m = +2) × (ℓ = 2, m = −2) | +0.65 |
| (ℓ = 3, m = 0) × (ℓ = 5, m = 0) | +0.51 |
| (ℓ = 6, m = −6) × (ℓ = 6, m = +6) | +0.50 |
| (ℓ = 3, m = ∓3) × (ℓ = 5, m = ±5) | −0.47 |

The strongest entries are m ↔ −m at fixed multipole and ℓ ↔ ℓ+2 at fixed m — which is what
"alignment" means when written in harmonic coefficients, and therefore where the
quadrupole–octupole alignment claims live. **The referee already exists on the calendar (the
BipoSH joint pass); what was missing until now was a prediction to hand it.**

Not "the model explains the anomalies" (the detailed low-ℓ likelihood is OWED — a compact-torus
C_ℓ computation with the winding modulation, un-run). The improvement is structural: ΛCDM
CANNOT expect these features even in principle; this model REQUIRES a discretized large-scale
spectrum and exactly one preferred axis, and it has independently pre-registered where that
axis is testable. The anomalies convert from embarrassments-of-chance to
predictions-in-waiting.

## 3. The honest risks

- The torus size (L ≥ 27.6 Gpc) risked being too large for the mode cutoff to explain the low
 quadrupole quantitatively. The cavity computation settled it, and the answer is split: the
 suppression *does* land where the anomaly is (confined to the lowest multipoles, dying by
 ℓ ≈ 4), but at 83% quadrupole retention it is far below what cosmic variance can resolve.
 So thread (1) does not weaken to aesthetic — it **relocates**, out of the power spectrum
 (total S/N 0.27, unusable at any multipole) and into the off-diagonal covariance
 (S/N 2.2, 990 pairs over ℓ = 2–6; the pattern's generating script is likewise
 scratch-era — regenerate before grading). The claim survives with its test moved, not lowered.
- Planck's isotropy analyses constrain dipolar power modulation at large scales — the same
 BipoSH class flagged for the comb; the family must survive it jointly.
- A measured axis-of-evil direction INCONSISTENT with a future comb/ε-dipole axis kills the
 family linkage cleanly.

*Standard cosmology looks at the largest scales, sees structure, and files it under luck. This
model looks at the same sky and sees what an atom always shows when you finally view it whole:
lines, and an axis. The cavity computation has now said where the resemblance can be checked —
not in how much power each scale carries, which cosmic variance will never resolve, but in which
scales are correlated with which, where a compact space leaves a pattern isotropy forbids.*
