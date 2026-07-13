> **PROVENANCE NOTE (2026-07-12):** the v4 era (superseded by v5+/the dyad era); for current state see PRTOE_INDEX.md.

# PRTOE v4 dCDF — Honest-Pipeline Results (2026-07-05)

> **DATE NOTE (2026-07-13 pass):** this file's header predates the derivation-hunt/freeze era; statuses herein may be superseded — current conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


All numbers below are from the **clean tree** (dkappa hack removed, perturbation
sector implemented, budget closure exact, null-test validated) against real
likelihoods: Planck 2018 lowl TT+EE, plik TTTEEE lite, Planck lensing, BAO
(6dF + MGS + DR12 consensus), Pantheon+SHOES. Single-point evaluations via
cobaya `evaluate` (system python; clik is py3.12-only); MCMC via CosmicForge.

## Headline

| point | χ² total | Δ vs ΛCDM |
|---|---|---|
| ΛCDM anchor (H₀=67.4, fiducial) | 2515.45 | — |
| dCDF hand-tuned (H₀=69, ξ=0.15, n_s=0.98) | 2511.57 | −3.9 |
| dCDF CosmicForge best fit (H₀=70.40) | **2496.24** | **−19.2** |

Best fit: ω_b=0.02280, H₀=70.40, logA=3.068, n_s=0.9826, z_reio=8.13,
ξ_Neff=0.403, ρ_inf=0.7007, log₁₀β=−8.09, A_planck=1.0019.
Derived: σ8=0.827, S₈=0.826 (ΛCDM: 0.833), Ω_m≈0.30.
Breakdown: plik 592.8 (+10.2), lensing 9.56 (+0.6), lowl.TT 21.4 (−2.1),
BAO 8.5 (−0.1), SN 1467.2 (**−27.8**).

The model buys ~3 km/s/Mpc of H₀ and a slightly lower S₈ at almost no CMB
cost. A second multistart mode at H₀=69.44 (ξ=0.240) sits Δχ²=1.1 away —
the H₀–ξ degeneracy valley is flat between at least 69.4 and 70.4.

## The three structural findings (in causal order)

1. **δ_m definition (dcdf_deltam_mode, default 1).** Galaxies trace baryons
   plus the fluid's clustering part (1+w)ρ; the smooth de Sitter floor is not
   matter. Mode 0 (full density in the denominator) produced σ8(z→0) decay
   and *negative* fσ8 — an artifact, not physics. Mode 1 restored
   fσ8(DR12) = (0.476, 0.477, 0.474) vs BOSS (0.497, 0.459, 0.436) untuned
   and took BAO DR12 χ² from 593 → 8.2. Modes 1 and 2 (baryons only) are
   statistically indistinguishable because (1+w)ρ_dcdf → 0 at late times.

2. **Acoustic-scale locking.** The unified fluid + ξ_Neff shift both r_s and
   D_A; θ* must be held at the Planck value (100θ*=1.04189 for the anchor).
   The viable region is the θ*-locked contour in (H₀, ξ): roughly
   ξ ≈ 0.15 at H₀=69 → 0.40 at H₀=70.4 → 0.60 at 71 → 1.0 at 73.
   Off-contour points are catastrophic (0.9% θ* offset ≈ +1600 on plik).

3. **Damping tail prices the H₀ relief.** Along the contour, fixed-fiducial
   totals: H₀=69 → +11.6; 71 → +228; 73 → +759; 74.8 → +1418 (vs ΛCDM).
   The n_s–N_eff degeneracy absorbs part (optimum n_s ≈ 0.98–0.995;
   ω_b wants to stay at 0.0224). SN gains saturate at −40 by H₀≈73.
   Net optimum: H₀ ≈ 70–70.5.

## Falsification / validation status

- **β→0 null test: PASSED.** At β=0 the background is exactly ΛCDM
  (p ≡ −ρ_inf) and δρ_dcdf obeys the CDM equation; the pipeline reproduces
  the ΛCDM anchor to σ8 5-decimal agreement and Δχ²=1.4 (residual: β=1×10⁻¹²,
  ρ_inf set to 5 digits). Any future perturbation-sector change must re-pass
  this (configs: job scratch evals/NF_null_closed.yaml).
- The null test caught a real bug on first run: **budget overclosure**
  (configs passed Omega0_dcdf = 1−Ω_b, ignoring Ω_r+Ω_ncdm ≈ 1.5×10⁻³ → +20
  plik). Fixed in input.c: the shooting now targets exact internal closure;
  the passed Omega0_dcdf is only the trigger/seed (it MUST still be present —
  shooting registration scans the input file).

## Internal falsifiable-test matrix (2026-07-05 night, at CosmicForge best fit)

| test | verdict |
|---|---|
| β→0 exact null (sync gauge) | PASS — σ8 to 5 decimals, Δχ² 1.4 |
| ξ_Neff ↔ N_ur equivalence | PASS — bit-exact (0.0 everywhere) |
| precision stability (tight tols) | PASS — σ8 stable to 5×10⁻⁶ |
| β-branch smoothness (8×10⁻⁹ → 1×10⁻⁴) | PASS — smooth, monotone σ8 decline |
| gauge invariance (sync vs newtonian) | bulk PASS (median 1×10⁻⁴ = ΛCDM baseline); **known defect**: localized 0.26% TT deviation at ℓ=10–12 decaying to baseline by ℓ>1500 — late-time-ISW/newtonian-branch gauge transform near w→−1. Unused in production (all runs synchronous); impact ≪ cosmic variance at those ℓ. Fix candidate: (1+w) factors in the dcdf gauge-transform / metric_euler terms in perturbations.c. |

## v5 transition (2026-07-05, late night): β deleted from the model

The MCMC drove β to its null limit (log₁₀β ≈ −8 at best fit; every β ≥ 1×10⁻⁶
destroys σ8) so β was **removed from the model entirely**: w(ρ) = −e^(−s) =
−ρ_inf/ρ exactly (p ≡ −ρ_inf, ΛCDM-form background), cs² ≡ 0. β's original
purpose — a positive sound speed for gradient stability and S₈ suppression —
is the classic unified-dark-matter sound-speed trap; the model achieves its
S₈ easing through geometry instead. dCDF v5 = 8 sampled parameters (+1 vs
ΛCDM: ξ_Neff only). Old v4 configs passing dcdf_beta now fail loudly.

CodeRabbit review of the v4 commit (7 findings): fixed the
effective_f_sigma8 memory leak (perturbations_sources_at_k_and_z never
freed its spline buffers — leaked every likelihood eval), Omega0_dcdf=0
silently skipping budget closure (now rejected), silently-discarded
Ω_cdm under use_dcdf (now warns), Saha-proxy H₀ unit error (dead code,
c_gamma/c_EM sandbox only), idm_g missing semicolon (cosmetic; compiled
correctly). The delta_cb-contamination finding was a false positive — the
cb snapshot precedes the dCDF stress-energy block; a guard comment now
protects that ordering. The derivation-doc logistic-ansatz critique is
moot: that section defended β's cs² guarantee and β no longer exists.

## Interpretation notes / open items

- **β is unused** (best fit 10⁻⁸, i.e. the exact-ΛCDM-background limit of the
  fluid). The H₀ relief comes from ξ_Neff + the fluid's budget unification,
  not from the barotropic deformation. Candidate simplification for v5:
  drop β (removes one Occam penalty from the evidence).
- **n_s = 0.983, ξ = 0.40**: the model claims Planck's n_s=0.965 is a
  ΛCDM-conditional inference. This is the standard high-N_eff signature and
  is falsifiable by better damping-tail data (ACT/SPT).
- S₈ = 0.826 at best fit (mode 2: 0.813) vs ΛCDM 0.833 — mild easing, not a
  full resolution of the weak-lensing preference (~0.77).
- Evidence (ln Z) comparison vs ΛCDM: pending (CosmicForge bridge sampling,
  dCDF run + ΛCDM twin lcdm_forge_v1.yaml queued). Parameter accounting:
  ΛCDM samples 7 (ω_b, ω_cdm, H₀, logA, n_s, z_reio, A_planck), dCDF samples
  9 (ρ_inf replaces ω_cdm; ξ_Neff and log₁₀β are the net +2). χ² −19.2 with
  2 extra parameters needs Δln Z to count as a detection; β→0 at best fit
  suggests a β-free 8-param variant would carry a smaller Occam penalty.
  Fixed symmetrically in both models: m_ncdm=0.06, T_cmb, N_ur base 2.0328.
  Never-sampled sandbox knobs (dcdf_c_gamma, dcdf_c_EM) remain 0/off.
- H₀=70.4 closes ~55% of the gap to SHOES (74.0±1.0); Pantheon+SHOES χ²
  improves −27.8, so the SN data endorse the partial move. Full 73+ remains
  blocked by the damping tail (ξ≈1.0 territory).

## Reproduction

- Best-fit configs and the θ*/n_s/ω_b grids: job f9b88ca9 scratch (archived)
  `tmp/evals/*.yaml` (T*, D_*, F_*, G_*, NF_*, BF_*).
- MCMC: `dcdf_forge_v1.yaml` + `run_cosmicforge.py --cores 12 --multistart 2
  --mcmc-steps 600 --mcmc-chains 4`; ΛCDM twin `lcdm_forge_v1.yaml`.
- **Traps**: OMP_NUM_THREADS=1 in ~/.bashrc throttles CLASS 12× (set
  per-command); clik imports only under system python3.12; after any
  rebuild verify BOTH classy .so files (conda cp313 + in-tree cp312) are
  newer than every source .c file.
