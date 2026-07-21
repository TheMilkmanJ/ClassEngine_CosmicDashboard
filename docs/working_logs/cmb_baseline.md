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

**It does not yet clear the "from first principles" bar, and three pieces stand:**
1. **A_s and n_s forced, not adopted.** They are set to the derived census values here and land the
   peaks — but forcing them rigorously from the genesis (no residual freedom in the amplitude ξ/ℓ_H =
   3.45×10⁻³ and the tilt) is the scaling-mechanism residual, still open.
2. **The dark-sector perturbation conversion channel** (dcdf → dark radiation) is off in the fiducial
   run — a small (~10⁻⁴ on S8) implementation item to turn on for a full first-principles C_ℓ.
3. **A real Planck-likelihood χ² at the derived (not fitted) stack** — the honest test is whether a
   *zero-parameter* derived prediction matches Planck at full precision, versus the current fit that
   still adjusts H0, ω_b, z_reio.

**Grade: baseline established — the model reproduces the CMB acoustic structure with its own derived
stack; the residual to "from first principles" is precision + the two pieces above, not the peaks.**

## Sources

The modified CLASS (`python/classy`), the model config (`cmp_prtoe_fixed.yaml`). ΛCDM reference:
Planck 2018 TT,TE,EE+lowE+lensing best-fit.
