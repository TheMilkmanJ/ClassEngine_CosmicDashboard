# P-042 / P-040 template-offset debt — calibration (2026-08-03)

**Status:** PARTIAL delivery of the TEMPLATE-SHAPE OFFSET item from the
P-040 corollary OWED paragraph in `docs/PRTOE_PREREGISTERED_PREDICTIONS.md`
(near P-2026-042). No MCMC. Analytic ramp + live `#17` form in
`include/background.h` + CLASS `(.)w_dcdf` curves from
`docs/working_logs/_runs/w_a_onset_20260803/w_a_dcdf_curves.npz`.

## 1. Coded ramp template

Define (task convention)

$$R(x)=\frac{x^{2}}{1+x^{2}},\qquad x=\frac{a}{a_{\mathrm{on}}}.$$

- Early ($a\ll a_{\mathrm{on}}$): $R\to 0$. Late: $R\to 1$. Half: $R=1/2$ at $x=1$.
- Live CLASS conformal-origin bundle (`dcdf_rho_rad` / `dcdf_p_rad`) uses
  $x_c=a_{\mathrm{on}}/a$ with
  $\rho=\rho_{\mathrm{dust}}\sqrt{1+x_c^{2}}$,
  $p=\rho_{\mathrm{dust}}\,x_c^{2}/(3\sqrt{1+x_c^{2}})$.
- Bundle EoS identity (checked to $10^{-14}$):

$$w_{\mathrm{bundle}}(a)=\frac{1}{3}\big(1-R(a/a_{\mathrm{on}})\big)
=\frac{x_c^{2}}{3(1+x_c^{2})}.$$

So the retired phenomenological ramp and the live single-mode dispersion
share the **same** $w(a)$ for the dust+rad-extra bundle. Template-shape
offset is then a **center-convention / identification** issue, not a live-vs-old
shape mismatch for this channel.

Reference parameter for this note: `dcdf_z_rad_onset` = 4.000000e+07 ($a_on$=2.500000e-08, log10 z_on=7.602060), matching `w_a_onset_20260803`.

## 2. Template center conventions (rad → dust)

Δlog10 ≡ log10[(1+z_feature)/(1+z_on)] (positive ⇒ feature **earlier** than the a_on parameter).

| convention | x=a/a_on | z_feature | Δlog10 | note |
|---|---:|---:|---:|---|
| param_a_on (R=1/2, w=1/6, inflection) | 1.000000 | 4.000000e+07 | +0.0000 | x=a/a_on=1; also max |dw/dln a| |
| rho_extra=dust equipartition | 0.577350 | 6.928203e+07 | +0.2386 | half of bundle energy in extra vs pure dust piece |
| asymp_rho_rad_equals_dust (xc=1) | 1.000000 | 4.000000e+07 | +0.0000 | dust*xc = dust at xc=1; same as a_on |
| 3p_extra=dust | 0.786151 | 5.088079e+07 | +0.1045 | effective rho_rad:=3p equals dust density |
| w=0.25 | 0.577350 | 6.928203e+07 | +0.2386 | bundle w crosses 0.25 |
| w=1/6 | 1.000000 | 4.000000e+07 | +0.0000 | bundle w crosses 0.16666666666666666 |
| w=0.10 | 1.527525 | 2.618615e+07 | -0.1840 | bundle w crosses 0.1 |
| w=0.05 | 2.380476 | 1.680336e+07 | -0.3767 | bundle w crosses 0.05 |
| kernel_mean_<ln x> (dR/dln a) | 1.000000 | 4.000000e+07 | +0.0000 | W(u)~sech^2(u), u=ln(a/a_on); mean zero |

### Preregistered “0.17 dex” claim

Prereg text: the coded ramp x²/(1+x²) has its own internal conventions (its rad=dust crossing sits 0.17 dex from its a_on parameter).

Exact identities on this ramp:

- `log10(1.5)` = **+0.176091** dex
- `log10(10**(1/6))` = **+0.166667** dex
- `0.5*log10(3) equipartition` = **+0.238561** dex
- `abs dlog10 at w=0.10` = **+0.183988** dex
- `log10(sqrt(e))` = **+0.217147** dex

- **Energy equipartition** ρ_extra=ρ_dust sits at **+0.2386 dex** (½ log10 3), not 0.17.
- **w=0.10 crossing** sits at **-0.1840 dex** (later than a_on).
- Closest simple number to “0.17” is log10(1.5)≈0.176 or 1/6≈0.1667 dex — **not** a unique derived center of R(x).
- Kernel mean of dR/d ln a is **exactly** at a_on (sech² even in ln(a/a_on)).

**Pinned result:** the only *derived* O(0.2) internal offset on this shape is
**equipartition = +0.2386 dex**. The round “0.17 dex” is a **loose envelope**, not a single coded crossing. Prereg ±0.2 dex band remains a fair systematic budget for *mislabeled* centers.

## 3. CLASS `(.)w_dcdf` transition scale — bare vs conv

From `w_a_dcdf_curves.npz` (same setup as onset truth table: h=0.70, dcdf_rho_inf=0.70, dcdf_z_rad_onset=4e7).

**Critical code fact** (`include/background.h`): the `#17` rad-onset term is
added to ρ_tot / p_tot / ρ_r and is **deliberately not folded into** `(.)w_dcdf`.
So `(.)w_dcdf` is the barotropic dust→DE fluid only (w=−ρ_∞/ρ),
and is **≈0 through onset** — it does **not** carry the w=1/3→0 ramp.

| quantity | bare | conv (g=0.12) |
|---|---:|---:|
| w(z~1e8) | -2.840e-24 | -2.661e-24 |
| w(z=z_on=4e7) | -4.290e-23 | -4.020e-23 |
| w(z=0) | -0.734602 | -0.734602 |
| steepest dw/dln a: z | 0.3815 | 0.3815 |
| steepest: a | 0.7238 | 0.7238 |
| steepest: w | -0.5121 | -0.5044 |
| half-to-today w: z | 0.6777 | 0.5729 |
| first w<-1/3: z | 0.6777 | 0.6777 |
| max |Δw| vs bare | 0 | 0.01048 |

### Comparison: template centers vs w_dcdf scales

| object | characteristic log10(1+z) | epoch |
|---|---:|---|
| template a_on / R=1/2 | 7.6021 | rad→dust onset |
| equipartition ρ_extra=dust | 7.8406 | rad→dust |
| bare w_dcdf steepest | 0.1404 | dust→DE (late) |
| conv w_dcdf steepest | 0.1404 | dust→DE (late) |
| bare half-to-today | 0.2247 | dust→DE (late) |
| conv half-to-today | 0.1967 | dust→DE (late) |

**Separation:** onset template center vs bare w_dcdf steepest differs by **7.462 dex** in log10(1+z) (~7.5 decades). These are **not** interchangeable clocks. Conversion shifts the late w_dcdf half-point by Δz ≈ -0.1048 (Δlog10(1+z) ≈ -0.0280), and max|Δw|≈0.010 — late-time only; **zero** imprint on `(.)w_dcdf` at onset.

## 4. log10 bias: template parameter vs physical clock

### 4a. Clock mapping (not shape)

| quantity | value |
|---|---:|
| log10(z_on coded 4e7) | +7.602060 |
| log10(z_on H=m 4.03e7) | +7.605305 |
| log10(z_on alpha_c pred 10^7.55) | +7.550000 |
| log10(z_on BOBYQA 3.5619e7) | +7.551682 |
| dlog10 (H=m - coded) | +0.003245 |
| dlog10 (coded - alpha_c pred) | +0.052060 |
| dlog10 (BOBYQA - alpha_c pred) | +0.001682 |
| dlog10 (H=m - alpha_c pred) | +0.055305 |

- H=m identity vs coded 4e7: **+0.0032 dex** (negligible).
- α_c=3α prediction (7.55) vs H=m (log10 4.03e7 ≈ 7.605): **+0.0553 dex** (abundance/α_c stack, not template shape).
- BOBYQA frozen log10_zon=7.5517 sits on the prediction, not on H=m.

### 4b. Shape-fit bias (synthetic LS on w(a), no cosmology likelihood)

True profiles generated on a ∈ [1e-2, 1e2] a_on; recover a_on' from the coded w=⅓(1−R) template.
Δlog10 z ≡ log10(a_on / a_on') (positive ⇒ recovered z_on higher than true).

| true profile | Δlog10 z |
|---|---:|
| same shape (live ≡ template) | -0.000000 |
| tanh, slope-matched at center (σ=1) | -0.000000 |
| tanh wider (σ=1.5) | -0.000000 |
| asymmetric tanh (σ_early=0.7, σ_late=1.4) | -0.066402 |

**Reading:** pure shape LS on the bundle w(a) recovers the midpoint to ≲1e-3 dex when the true profile is symmetric about a_on. Asymmetry at the level of a two-width tanh shifts the recovered center by **-0.066 dex**. That is the right *order* for the prereg ±0.2 dex caution, but it is **not** a measurement of the CLASS onset likelihood bias.

### 4c. Bottom-line bias budget (this delivery)

| source | log10 bias (dex) | grade |
|---|---:|---|
| internal R=1/2 / inflection / kernel mean vs a_on | 0.000 | settled |
| internal equipartition vs a_on | +0.2386 | settled (convention) |
| 3p=dust vs a_on | +0.1045 | settled (convention) |
| H=m clock vs coded z_on parameter | +0.0032 | settled |
| same-shape w(a) LS fit | ~0 | settled |
| asymmetric-shape w(a) LS (toy) | ~-0.07 | illustrative only |
| **full onset likelihood / MCMC template bias** (CMB+BAO+… free log10_zon) | **unknown** | **still owed** |
| pre-onset true microphysics ≠ dispersion bundle | unknown | still owed |
| Ψ0∝m^(−1/4) bend under conversion (abundance closure) | partial (conv max|Δw|=0.010 late) | still owed |

## 5. Residual still owed

1. **Onset likelihood template bias (main residual).** A real Δlog10 z_on requires fitting the expansion history (and Boltzmann hierarchy) with free `log10_zon`, not LS on an isolated w(a) curve. No MCMC in this delivery — as ordered.
2. **Do not grade 7.55 vs 7.94 with w_dcdf alone.** `(.)w_dcdf` ignores `#17`; the onset clock lives in ρ_dcdf,rad(a) and the total expansion, not in the w_dcdf column.
3. **Prereg 0.17 dex** should be cited as an **O(0.2) convention envelope**; the sharp internal number is equipartition **+0.239 dex**, or **0** if the parameter is defined as the R=1/2 / inflection center (code default).
4. **Conversion/thaw** do not move the rad-onset template center in `(.)w_dcdf`; they matter for the abundance-closure branch of the same OWED paragraph (late w distortion O(0.01)).

## 6. Debt board update

| item | status |
|---|---|
| True w_dcdf(a) bare/conv/thaw/both | **DELIVERED** (`w_a_onset_20260803`) |
| Template definition R(x)=x²/(1+x²), x=a/a_on + live-form identity | **DELIVERED** (this report) |
| Center-convention table vs a_on | **DELIVERED** |
| Compare template centers to CLASS w_dcdf bare/conv scales | **DELIVERED** (epochs incommensurable; numbers above) |
| log10 bias template param ↔ physical clock (analytic) | **DELIVERED** (≈0 for H=m vs code; +0.239 if equipartition misread as center) |
| log10 bias from full onset likelihood | **still owed** |
| Ψ0∝m^(−1/4) under conversion | **still owed** (partial late-w only) |

Artifacts: `numbers.json` (this directory); curves from `docs/working_logs/_runs/w_a_onset_20260803/w_a_dcdf_curves.npz`.
Code refs: `include/background.h` (`dcdf_rho_rad`, `dcdf_p_rad`, comments on retired ramp); `source/background.c` (rad term → ρ_tot only).
