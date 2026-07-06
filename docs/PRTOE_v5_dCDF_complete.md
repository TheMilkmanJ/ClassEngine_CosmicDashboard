# dCDF v5 — The Complete Model: Physics, Math, Implementation, Results

**Status (2026-07-05): current production model.** This document is
self-contained: the action, the background and perturbation equations as
implemented, why the model has exactly this form (including the death of β),
the parameter accounting, the validated results, and the open falsifiers.
It supersedes reading `PRTOE_v4_dCDF_derivation.md` + `PRTOE_v4_dCDF_results.md`
as a pair; those remain the historical record of how v4 → v5 happened.

---

## 1. The model in one paragraph

dCDF (Dynamic Cold Dark Fluid) replaces **both** cold dark matter and the
cosmological constant with a **single barotropic dark fluid** whose pressure
is exactly constant:

$$ p_d \equiv -\rho_\infty \qquad\Longleftrightarrow\qquad w(\rho) = -\frac{\rho_\infty}{\rho} = -e^{-s},\quad s \equiv \ln(\rho/\rho_\infty) \ge 0 $$

with adiabatic sound speed $c_s^2 = dp/d\rho \equiv 0$. Dense regions of the
fluid behave as dust ($w\to0^-$ as $s\to\infty$); as the fluid dilutes toward
its de Sitter floor $\rho_\infty$ it behaves as vacuum energy ($w\to-1$ at
$s=0$). One medium, two regimes — the direct formalization of the trampoline
picture: one fabric, stretched near mass, flat far from it. Gravity is
**exactly GR**; baryons and photons couple only minimally through the metric.
Alongside the fluid, the model carries one extra radiation parameter,
$\xi_{N_{\rm eff}}$ ($N_{\rm eff} = 3.044 + \xi$). Total sampled parameters:
**8, i.e. +1 versus ΛCDM.**

Headline (full honest pipeline — Planck 2018 lowl TT+EE, plik TTTEEE lite,
lensing, BAO 6dF+MGS+DR12, Pantheon+SHOES):

| point | χ² total | Δ vs ΛCDM |
|---|---|---|
| ΛCDM anchor (H0=67.4) | 2515.45 | — |
| dCDF best fit (H0=**70.40**, ξ=0.403) | **2496.24** | **−19.2** |

with S8 = 0.826 vs ΛCDM's 0.833 and Pantheon+SHOES carrying −27.8 of the
improvement. Bayesian evidence comparison (PolyChord, nlive 500) in flight.

---

## 2. Action and microphysics

$$ S = \int d^4x\,\sqrt{-g}\left[\frac{M_{\rm pl}^2}{2}R + P(X)\right] + S_m[g_{\mu\nu},\psi] , \qquad X \equiv -\tfrac12 g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi $$

A single shift-symmetric (purely kinetic) k-essence scalar. The standard
stress tensor (Garriga–Mukhanov 1999) gives on the FLRW background

$$ \rho = 2XP_X - P, \qquad p = P(X), $$

and shift symmetry conserves the current: $a^3 P_X \dot\phi = \text{const}$.
Because ρ and p are both functions of X alone, **p(ρ) is exactly barotropic**
— there is no non-adiabatic pressure perturbation, ever. This is what lets
the entire perturbation sector collapse onto CLASS's existing fluid
machinery (§4).

**The v5 microphysical realization.** A constant-pressure fluid is not an
exotic request of k-essence: expand any $P(X)$ about an extremum $X_0$
($P_X(X_0)=0$),

$$ P(X) \simeq P_0 + \tfrac12 P_2\,(X-X_0)^2 . $$

Solving the conserved-current equation near $X_0$ gives exactly
$\rho(a) = \rho_\infty + K a^{-3}$ with $\rho_\infty = -P_0$, $p = P_0$, and
$c_s^2 = P_X/(P_X + 2XP_{XX}) \to 0$. This is the Scherrer purely-kinetic
unified-dark-matter construction (PRL 93, 011301, 2004). dCDF v5 **is** that
fluid — the k-essence "designer reconstruction" debt carried by v4 is
discharged: the explicit $P(X)$ above generates the model.

No-ghost: $\partial\rho/\partial X = P_X + 2XP_{XX} > 0$ requires $P_2 > 0$
on the $X > X_0$ branch — satisfied by construction; the same condition makes
ρ(X) monotone so that "w(ρ)" is well defined. No-gradient: $c_s^2 = 0$ is the
marginal case; there is no gradient instability and no pressure support (the
fluid clusters exactly like CDM, §4). Degrees of freedom: one scalar, two
phase-space DOF, GR untouched — no PPN/screening machinery required.

**One fluid, not two.** There is no interaction term Q: the continuity
equation is closed,

$$ \rho_d' = -3\mathcal{H}\,(1+w(\rho_d))\,\rho_d . $$

The de Sitter floor is not a second component exchanging energy with a first;
it is the low-density regime of the same medium. The regime label is a
**density**, not a time: a halo interior sits at $s \sim 12$–16 (dust), a
void sits near $s \approx 0$ (vacuum).

---

## 3. Background: exact solution

With $w = -\rho_\infty/\rho$ the continuity equation integrates in closed
form:

$$ \rho_d(a) = \rho_\infty + K a^{-3} . $$

**The background is exactly ΛCDM-form.** $\rho_\infty$ plays Ω_Λ's role
(best fit $\rho_\infty = 0.7007$ in units of the critical density — the code
stores `dcdf_rho_inf` in H0² units and scales at read time), and the $Ka^{-3}$
part plays CDM's role. $s = \ln(\rho/\rho_\infty)$ is clamped ≥ 0 in the code;
the fluid can approach but never undershoot its floor (de Sitter attractor:
at $s=0$, $1+w=0$ forces $\rho'=0$).

**Budget closure (shooting).** The fluid's primordial amplitude
`Omega_ini_dcdf` is the shooting unknown; the target is **exact internal
closure** computed from the initialized background:

$$ \Omega_{d,0} = 1 - \Omega_k - \Omega_\gamma - \Omega_b - \Omega_{ur} - \Omega_{ncdm} - (\text{all other components}) . $$

The input parameter `Omega0_dcdf` is only the **trigger and seed** — CLASS's
shooting registration scans the input file for target names, so the parameter
must be present (any rough positive value, e.g. `1 - Omega_b`) but its value
is not the target. `Omega0_dcdf ≤ 0` is rejected loudly; omitting it entirely
would silently produce a fluid with no density (this failure mode is now
impossible: `use_dcdf` requires it). The closed-form background gives the
shooting initial guess $\Omega_{d,\rm ini} \approx \Omega_{d,0} - \rho_\infty$;
convergence in ~4 evaluations. Getting this closure exact matters at the
χ² ≈ 20 level: the earlier approximation `Omega0_dcdf = 1−Ω_b` ignored
$\Omega_r + \Omega_{ncdm} \approx 1.5\times10^{-3}$ and cost +20 on plik
(caught by the null test, §7).

---

## 4. Perturbations

Exact barotropicity + no anisotropic stress ⟹ the standard Ma–Bertschinger
fluid equations (synchronous gauge), with $w(\bar\rho_d(a))$ evaluated each
timestep and $c_s^2 = 0$:

$$ \delta' = -(1+w)\left(\theta + \frac{h'}{2}\right) + 3\mathcal{H}\,w\,\delta $$
$$ \theta' = -\mathcal{H}\,\theta $$

With $c_s^2 = 0$ there is no $k^2\delta$ pressure source in the Euler
equation: θ decays and the fluid free-falls exactly like CDM. (The v4 code
carried a regularization ratio $c_s^2/(1+w) \to 2\beta$ near $w = -1$; its
exact β→0 limit, 0, is what v5 implements.)

**The physically meaningful statement** is in terms of δρ, not δ: with
$\delta p \equiv 0$ and $\bar p \equiv -\rho_\infty$ constant, the perturbed
conservation equations for $\delta\rho_d$ and $(\rho+p)\theta_d$ coincide with
those of a CDM component of density $Ka^{-3}$. The fluid's clustering part
**is** CDM, exactly; the floor does not perturb.

### 4.1 What do galaxies trace — `dcdf_deltam_mode`

Because one fluid carries both "matter" and "vacuum," the definition of
$\delta_m$ (which feeds σ8, fσ8, halofit, and the lensing spectra) is a
modeling decision, made explicit as `dcdf_deltam_mode`:

| mode | δ_m includes | verdict |
|---|---|---|
| 0 | baryons + fluid at **full** density weight ρ | **artifact**: σ8(z→0) decays, fσ8 goes negative (δρ dilutes as a⁻³ while ρ→ρ_∞ stops diluting) |
| 1 | baryons + fluid's **clustering part**, weight (1+w)ρ = ρ−ρ_∞ | **default & correct**: the de Sitter floor is not matter |
| 2 | baryons only | statistically tied with mode 1 (Δχ² ≈ 0.5) since (1+w)ρ_d → 0 late |

Mode 1 took BAO DR12 χ² from 593 → **8.2** (ΛCDM: 7.5) with untuned
fσ8(DR12) = (0.476, 0.477, 0.474) vs BOSS (0.497, 0.459, 0.436). Since
$(1+w)\rho_d = Ka^{-3}$ exactly, mode-1 δ_m is *identical* to ΛCDM's
matter definition — modes 1 and 2 converging late is the same fact seen
twice. Effective $\Omega_m$ (for consistency relations) counts
$(1+w)\rho_d$: best fit $\Omega_m \approx 0.30$.

### 4.2 The exact ΛCDM degeneracy — stated honestly

Sections 3 and 4 together imply: **the dCDF fluid at v5 is exactly
degenerate with ΛCDM** at both background and linear-perturbation level.
This is verified, not assumed — the null test (§7) reproduces the ΛCDM
anchor to 5 decimals in σ8 and Δχ² = 1.4 (residual: finite shooting
precision). Therefore:

- The −19.2 χ² gain is carried by $\xi_{N_{\rm eff}}$ and the re-optimized
  (H0, n_s) along the θ*-locked ridge (§6) — **not** by the fluid's internal
  dynamics.
- The unification itself is presently an *interpretation with equal
  likelihood*: it buys parameter economy (CDM density and Λ replaced by one
  floor parameter + exact closure) and a framework in which the dark sector
  can lawfully acquire density-dependent physics later (SIDM-type
  extensions, `docs/PRTOE_v5_SIDM_scoping.md`), but it is not itself the
  source of the fit improvement.
- Anything that would make the fluid *observably* different from ΛCDM at
  linear order (a sound speed, a w(ρ) deformation) is exactly what the data
  killed (§5).

---

## 5. How β lived and died (the sound-speed trap)

v4 carried a two-parameter equation of state
$w(s) = -\exp[-(s+\beta s^2)]$, giving $c_s^2 = 2\beta s\,e^{-(s+\beta s^2)}
\ge 0$ with peak $\approx 0.74\beta$. The design goal was to decouple "how
different from ΛCDM" from "how large the dangerous sound speed" — the
coupling that kills the generalized Chaplygin gas (Sandvik–Tegmark–
Zaldarriaga–Frieman 2004: the GCG exponent α controls both, so the model is
either ΛCDM-degenerate or LSS-dead). The β family achieved the decoupling
*algebraically*, but the data's verdict was unambiguous:

- The honest-pipeline MCMC drove β to its null limit (log₁₀β ≈ −8 at best
  fit, i.e. the exact-ΛCDM-background boundary of the prior).
- Every β ≥ 10⁻⁶ only destroyed structure: σ8 0.827 → 0.185 at β = 10⁻⁴.
  A unified-dark-matter sound speed suppresses P(k) below the sound horizon
  — there is no observationally allowed window in which it *helps*.
- The v4.1 exploration (logistic $w_{\rm kin}(s)$ riding on a bare Λ)
  sharpened this into a structural no-go: **any** monotonic single-crossover
  w(ρ) — dust at high density, something else at low — has a $c_s^2(s)$ that
  can only decay past the transition. It cannot be σ8-safe at $s \lesssim 5$
  and non-negligible at halo densities ($s \approx 12$–16). A halo-core
  signature would require a hand-placed *bump* in $c_s^2(s)$ with no
  independent motivation — an epicycle, rejected.

So β was **deleted** (2026-07-05), not merely fixed to zero: removed from
`background.h` (w and c_s² are now the closed forms of §1), from `input.c`
(configs passing `dcdf_beta` fail loudly), and from `perturbations.c` (the
2β regularization replaced by its exact limit). The MCMC's posterior served
as the amputation criterion: a parameter the data pins to its null limit,
whose every nonzero excursion is punished, carries pure Occam penalty in the
evidence and no explanatory power.

---

## 6. The ξ_Neff sector and the structure of the fit

$\xi_{N_{\rm eff}}$ adds relativistic energy: $N_{\rm eff} = 3.044 + \xi$,
implemented on the ultra-relativistic species (verified bit-exact equivalent
to the same shift in `N_ur`). The fit's anatomy, established by direct scans:

1. **Acoustic-scale locking.** The unified budget + extra radiation shift
   both $r_s$ and $D_A$; the data pin $100\,\theta_* = 1.04189$ to ~0.03%.
   The viable region is a one-dimensional ridge in (H0, ξ):
   ξ ≈ 0.15 at H0=69 → 0.40 at 70.4 → 0.60 at 71 → 1.0 at 73.
   Off-ridge points are catastrophic (+0.9% in θ* ≈ +1600 on plik).
2. **The damping tail prices the H0 relief.** Along the ridge, the Silk-
   damping cost grows ~quadratically in ξ: totals +11.6 at H0=69, +228 at
   71, +759 at 73, +1418 at 74.8 (fixed fiducials). The n_s–N_eff degeneracy
   absorbs part (optimum n_s ≈ 0.98); higher ω_b does not help.
3. **SN push the other way.** Pantheon+SHOES gains saturate at ~−40 by
   H0 ≈ 73. The net optimum of (2) vs (3) lands at **H0 ≈ 70–70.5** —
   closing ~55% of the gap to SH0ES (74.0 ± 1.0), endorsed by the SN
   likelihood (−27.8), blocked beyond that by the damping tail.

## 7. Validation — the falsifiable-test matrix (all at/near best fit)

| test | verdict |
|---|---|
| exact null (fluid ⇒ ΛCDM; v5 form) | **PASS** — σ8 0.81301 vs anchor 0.81304, total 2516.7 vs 2515.5 |
| ξ_Neff ↔ N_ur equivalence | **PASS** — bit-exact (difference 0.0 everywhere) |
| precision stability (tightened tolerances) | **PASS** — σ8 stable to 5×10⁻⁶ |
| β-branch smoothness (pre-deletion, 8×10⁻⁹→10⁻⁴) | **PASS** — smooth monotone σ8 decline (then β removed) |
| gauge invariance (synchronous vs newtonian) | bulk **PASS** (median deviation 10⁻⁴ = ΛCDM baseline); **known defect**: 0.26% TT deviation at ℓ=10–12 on the *newtonian* dCDF branch (late-ISW, (1+w)→0 gauge-transform terms suspect), decaying to baseline by ℓ>1500. Harmless in production (all runs synchronous; those ℓ are cosmic-variance dominated) — must be fixed before ever running newtonian. |
| 6-corner prior-box stress test (v5, β-free) | **PASS** — all corners run gracefully |

The null test earns its keep: on its first run it caught the budget-
overclosure bug (§3), a real +20-χ² error invisible to every other check.

## 8. Results

Best fit (CosmicForge: bobyqa multistart → Laplace → MH; 600×4 chains,
acceptance ~27%):

| parameter | ΛCDM anchor | dCDF best fit |
|---|---|---|
| ω_b | 0.02237 | 0.02280 |
| H0 | 67.4 | **70.40** |
| ln(10¹⁰A_s) | 3.044 | 3.068 |
| n_s | 0.9649 | **0.9826** |
| z_reio | 7.67 | 8.13 |
| ξ_Neff | — | **0.403** |
| ρ_∞ | — | 0.7007 |
| A_planck | 1.0 | 1.0019 |

Derived: σ8 = 0.827, **S8 = 0.826** (ΛCDM 0.833), Ω_m ≈ 0.30.
χ² breakdown vs ΛCDM: plik +10.2, lensing +0.6, lowl.TT −2.1, BAO −0.1,
**SN −27.8** → total **−19.2**. A second multistart mode at H0=69.44
(ξ=0.240) sits only Δχ²=1.1 away: the ridge is flat over at least
69.4–70.4.

**Evidence:** in flight. CosmicForge bridge-sampling ln Z (MH run) and a
PolyChord pair (dCDF `dcdf_pc_v1.yaml` vs ΛCDM twin `lcdm_pc_v1.yaml`,
nlive 500, num_repeats 2d) are running. Back-of-envelope from prior/posterior
widths: Δln Z ≈ +5 to +7 in dCDF's favor if the χ² gain survives
marginalization — the +1-parameter Occam penalty is small because the one
extra parameter (ξ) is doing real work.

## 9. Falsifiable predictions (external, not yet tested)

1. **Damping tail (ACT/SPT).** The best fit *requires* N_eff ≈ 3.45 and
   n_s ≈ 0.983. High-ℓ TT/TE/EE data sharper than Planck's tail directly
   test this — the model claims Planck's n_s = 0.965 is a ΛCDM-conditional
   inference. If ACT/SPT pin n_s low and N_eff at 3.04 at these precisions,
   dCDF's H0 mechanism is dead.
2. **Weak lensing S8.** Prediction S8 = 0.826: mild easing toward the WL
   preference (~0.77), not a resolution. A joint WL fit must not degrade
   the CMB side.
3. **BBN.** ΔN_eff = 0.40 at BBN shifts Y_p and D/H; consistency with
   primordial-abundance measurements is required, not yet checked.

## 10. Implementation map (code ↔ physics)

| symbol | code | notes |
|---|---|---|
| ρ_∞ | `pba->dcdf_rho_inf` | read in critical-density units, scaled by H0² at read time; prior [0.50, 0.80] |
| Ω_d,ini | `pba->Omega_ini_dcdf` | shooting unknown |
| Ω_d,0 | `pba->Omega0_dcdf` | shooting **trigger + seed only**; must be present and > 0; target is exact closure (§3) |
| w(ρ) | `w_dcdf()` in `background.h` | `-exp(-s)` = −ρ_∞/ρ |
| c_s²(ρ) | `cs2_dcdf()` in `background.h` | returns 0.0 identically |
| s | computed | `dcdf_s_of_rho()`, clamped ≥ 0 |
| δ_m definition | `dcdf_deltam_mode` | default 1 (§4.1) |
| ΔN_eff | `xi_Neff` | added to N_ur: N_eff = 3.044 + ξ; prior [0, 1.3] |
| sandbox | `dcdf_c_gamma`, `dcdf_c_EM` | environmental-coupling experiments; 0/off in all production runs |

Perturbations: fluid block in `source/perturbations.c` (synchronous gauge,
fld-mirrored); the δ_m accumulation block **must stay after** the
delta_cb/theta_cb snapshot (cb quantities are baryon+CDM only by contract —
guard comment in code). `use_dcdf = yes` replaces CDM (floored at
`Omega0_cdm_min_synchronous` = 10⁻¹⁰ because synchronous gauge is defined in
the CDM rest frame) and disables the lambda/fld/scf budget auto-fill chain.

Fixed symmetrically in dCDF and the ΛCDM twin: one massive neutrino
m_ncdm = 0.06 eV, T_cmb, N_ur base. ΛCDM samples 7 parameters
(ω_b, ω_cdm, H0, logA, n_s, z_reio, A_planck); dCDF samples 8
(ρ_∞ replaces ω_cdm; +ξ_Neff).

## 11. Open items

- **Newtonian-gauge defect** (§7): fix the (1+w)→0 gauge-transform terms
  before any newtonian-gauge use.
- **Evidence numbers**: harvest CosmicForge bridge ln Z + PolyChord pair
  when runs complete; that decides whether −19.2 is a detection or a
  flexible-model tax.
- **ACT/SPT damping-tail test** (§9.1) — the sharpest external falsifier.
- **BBN check** of ΔN_eff = 0.40.
- **SIDM-type extension scoping** (`PRTOE_v5_SIDM_scoping.md`): the lawful
  place for new dark-sector physics is now density-dependent
  *interactions* (not sound speed — §5 closed that door).

## 12. Reproduction and traps

- MCMC: `dcdf_forge_v1.yaml` via `run_cosmicforge.py --cores 12
  --multistart 2 --mcmc-steps 600 --mcmc-chains 4`; ΛCDM twin
  `lcdm_forge_v1.yaml`. PolyChord: `dcdf_pc_v1.yaml` / `lcdm_pc_v1.yaml`
  via **system** `/usr/bin/mpirun -n 4` (PolyChordLite links system OpenMPI;
  the conda mpirun on PATH is a deadlock trap).
- `OMP_NUM_THREADS=1` in `~/.bashrc` throttles CLASS ~12× (CLASS v3.3.4's
  C++ std::thread task system reads that env var). Do not edit bashrc (it
  protects MPI runs); set `OMP_NUM_THREADS` per command.
- clik imports only under **system** python3.12 — all likelihood evals via
  `/usr/bin/python3 -m cobaya`. The conda env (`prtoe_gold`, cp313) is for
  physics probes only.
- After any rebuild, verify **both** classy `.so` files (conda cp313 +
  in-tree cp312) are newer than every source `.c` — a stale editable-install
  `.so` silently shadows the fresh one.
- Any probe sweeping `dcdf_deltam_mode` (or any dCDF param) must pass it
  into `classy.set()` explicitly — identical outputs across "modes" means
  the parameter never reached C.
- Old v4 configs passing `dcdf_beta` fail loudly. This is intentional.

---

*History: v1–v3 (F(φ)R non-minimal coupling + screening) closed — four
independent H0-rescue mechanisms failed by direct calculation. v4
(β-deformed dCDF) superseded by this document. Full v4 derivation including
the GCG no-go algebra and the v4.1 logistic exploration:
`PRTOE_v4_dCDF_derivation.md`. Results archaeology:
`PRTOE_v4_dCDF_results.md`.*
