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

## The parameters

The derived stack fixes the model's own numbers — the census A_s = 2.088×10⁻⁹ and n_s = 0.9641,
varying-mₑ = 1.0125, and the dcdf as the whole dark sector — and fits four background parameters, H0,
ω_b, z_reio, and the dcdf occupancy ρ_∞, against ΛCDM's six. The dark-sector perturbation conversion
channel (dcdf → dark radiation) is off in this run, a ~10⁻⁴ effect on S8. Over the joint CMB+BAO+SN
data the full fit reaches ΔlnZ ≈ +2.6 over ΛCDM.

## The Planck χ²

At the fiducial derived stack, evaluated once (`scripts/cmb_chi2.py`, a single point), the Planck 2018
χ² is 1215 — low-ℓ TT 22.7, low-ℓ EE 397.9, high-ℓ plik TTTEEE 782.0, lensing 12.4 — against 1012 for
ΛCDM at its Planck best fit. The low-ℓ and lensing sit level with ΛCDM; the difference is in the
high-ℓ TT/TE/EE.

## The acoustic scale

The high-ℓ difference is one quantity: the acoustic scale. The model's TT peaks sit at a constant
~0.18% higher ℓ than ΛCDM's (peak 1: 221 vs 220; peak 7: 2012 vs 2010), and 100·θ_s = 1.04047 at the
fiducial stack against 1.04194 for ΛCDM. The residual tracks the peak slope (correlation −0.66), a
shift of the comb along ℓ rather than a change in height; the peak heights, damping, and tilt match to
0.45% RMS. θ_s is set by H0, ω_b, and the recombination redshift that varying-mₑ controls, and the
joint fit sets it through those background parameters (`scripts/cmb_chi2_diagnose.py`).

With the four background parameters free, the model fits the Planck spectrum at χ² = 1025 — a residual
of +13 over ΛCDM's 1012, high-ℓ 595 against ΛCDM's 584 — so it fits the CMB comparably
(`scripts/cmb_realign_4d.py`). The fit sits at H0 = 70.8 and ω_b = 0.0229, and that ω_b is the one
deuterium is in tension with: on this single knob the CMB peak alignment and the deuterium abundance
pull opposite ways.

## Sources

The modified CLASS (`python/classy`), the model config (`cmp_prtoe_fixed.yaml`). ΛCDM reference:
Planck 2018 TT,TE,EE+lowE+lensing best-fit.
