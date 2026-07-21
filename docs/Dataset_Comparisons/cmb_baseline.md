# The CMB baseline — the model reproduces the acoustic peaks

*The model's modified CLASS at the fiducial **derived** stack — the dcdf as the whole dark sector,
varying-mₑ = 1.0125 — produces a CMB temperature spectrum whose acoustic peaks land on Planck's,
tracking ΛCDM to a couple percent. Code: `scripts/cmb_baseline.py`, `scripts/cmb_baseline_plot.py`;
figure `chains/cmb_baseline.png`.*

## The setup that matters

The model has **no separate ω_cdm and no Ω_Λ**: Ω_dcdf = 1 − Ω_b, so the dcdf superfluid is the
*entire* dark sector — dark matter and dark energy in one medium. The C_ℓ run uses the derived
census amplitude and tilt (A_s = 2.088×10⁻⁹, n_s = 0.9641), the derived varying-mₑ = 1 + 27α/5π =
1.01254, and the dcdf occupancy/onset — i.e. the model's own numbers, not a free CMB fit.

## The result

| TT peak | model (ℓ, D_ℓ μK²) | Planck (ℓ, D_ℓ) |
|---|---|---|
| 1st | 221, 5631 | ~220, ~5750 |
| 2nd | 537, 2536 | ~540, ~2500 |
| 3rd | 814, 2485 | ~810, ~2500 |
| 4th | 1128, 1211 | ~1130, ~1200 |

Against a ΛCDM reference (Planck 2018, also from CLASS — and ΛCDM fits Planck, so this is a
transitive check), the model's TT tracks it to **mean 1.9%, max 2.9% over ℓ = 30–2500**, first peak
−1.65%. Derived structure numbers: σ8 = 0.818, S8 = 0.816, Ω_m = 0.299.

## What this does and does not settle

The census A_s/n_s, the dcdf dark sector, and varying-mₑ — the model's own numbers — produce the
acoustic peaks at the right places and heights.
And the full MCMC (which fits the cosmology + nuisance parameters) reaches ΔlnZ ≈ +2.6 over ΛCDM, so
at best-fit it *fits* Planck; the ~2% here is the frozen fiducial stack, not the fitted point.

It does not yet clear the "from first principles" bar. Three pieces stand:
1. **A_s and n_s forced, not adopted.** They are set to the derived census values here and land the
   peaks — but forcing them rigorously from the genesis (no residual freedom in the amplitude ξ/ℓ_H =
   3.45×10⁻³ and the tilt) is the scaling-mechanism residual, still open.
2. **The dark-sector perturbation conversion channel** (dcdf → dark radiation) is off in the fiducial
   run — a small (~10⁻⁴ on S8) implementation item to turn on for a full first-principles C_ℓ.
3. **A real Planck-likelihood χ² at the derived (not fitted) stack** — the honest test is whether a
   *zero-parameter* derived prediction matches Planck at full precision, versus the current fit that
   still adjusts H0, ω_b, z_reio.

Baseline established — the model reproduces the CMB acoustic structure with its own derived stack;
the residual to "from first principles" is precision plus the two pieces above, not the peaks.

## The Planck χ² at the derived stack

Evaluated once at the fixed derived stack (`scripts/cmb_chi2.py`, a single point, no chain), the
Planck 2018 χ² is 1215 — lowl.TT 22.7, lowl.EE 397.9, highl plik TTTEEE 782.0, lensing 12.4 — against
1012 for ΛCDM at its Planck best-fit. Δχ² = +203, and almost all of it (+198) is in the high-ℓ
TT/TE/EE; the low-ℓ and lensing sit level with ΛCDM. So the ~2% eyeball residual is a Δχ² ≈ 200 at
Planck precision — the χ², not the eye, is the honest metric.

This is at the fixed fiducial background: H0 = 69.6 there is a SHOES-compromise, not the CMB-preferred
value, and the model still fits four background parameters (H0, ω_b, z_reio, ρ_∞). So +203 is the
un-refit penalty — an upper bound on the miss that fitting those four recovers most of (the full chain
reaches ΔlnZ ≈ +2.6 over the joint CMB+BAO+SN data). The derived physics parameters (A_s, n_s,
varying-mₑ) are fixed; the background is not. The model reproduces the peak structure and fits the
joint data when refit, but the derived stack is not itself a zero-parameter CMB fit. The number that
closes this is the CMB χ² minimised over the four background parameters with the physics held fixed.

## Why the high-ℓ penalty is high, and that it is fixable

The +198 is diagnosed (`scripts/cmb_chi2_diagnose.py`) as a peak-alignment miss, not a shape failure.
The model's TT peaks sit at a constant ~0.18% higher ℓ than ΛCDM's (peak 1: 221 vs 220; peak 7: 2012
vs 2010) — a constant fractional drift is the fingerprint of an acoustic-scale mismatch, since θ_s
places the peaks at ℓ ≈ nπ/θ_s. The residual tracks the peak slope (correlation −0.66), the signature
of a horizontal ℓ-shift of the comb rather than a height error. And 100·θ_s = 1.04047 for the model
against 1.04194 for ΛCDM — off by 0.14%, about five times Planck's 0.03% precision on the acoustic
scale. θ_s is a pure background quantity, set by H0, ω_b, and the recombination redshift that
varying-mₑ controls, all among the four background parameters the fit turns; the CMB pins θ_s to
0.03%, so any real fit hits it and the whole comb slides back into place, collapsing the high-ℓ
penalty. The model's peak heights, damping, and tilt are already right (0.45% RMS residual); the
fiducial H0 = 69.6 simply is not the θ_s-matched value. What remains to check is whether a residual
high-ℓ tension survives once θ_s is restored — the CMB χ² minimised over the four background
parameters answers it.

## Sources

The modified CLASS (`python/classy`), the model config (`cmp_prtoe_fixed.yaml`). ΛCDM reference:
Planck 2018 TT,TE,EE+lowE+lensing best-fit.
