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
| **Planck+BAO+SN stack:** ΛCDM anchor (H0=67.4) | 2515.45 | — |
| dCDF best fit (H0=70.40, ξ=0.403) | 2496.24 | −19.2 |
| **Joint stack (+ ACT DR6 + SPT-3G):** ΛCDM frozen / refitting | 2817.9 → ~2810 | — |
| dCDF joint refit (**H0=69.05, ξ=0.142**, n_s=0.979) | **2809.81** | ≈ tie |
| dCDF + varying m_e=1.01 (**H0≈70.4**, ξ=0.124; §9.4) | **2801.06** (optimizer final; decomposition control running) | TBD |

**The joint refit happened (2026-07-06) and landed exactly on the
predicted ridge point** — H0 = 69.05, ξ = 0.142 vs the pre-registered
"H0 ≈ 69, ξ ≈ 0.15" (§9.1). Against the *refitting* ΛCDM twin the joint
stack is heading to a statistical tie: the honest current claim is **equal
fit quality on every dataset simultaneously, with H0 = 69.0 and
S8 = 0.824 vs ΛCDM's 67.4 / 0.833** — both tensions eased directionally at
zero χ² cost, for one extra parameter. The varying-m_e extension (§9.4,
same-day discovery) may buy H0 back to ~70.4; its honest credit awaits the
optimization-slack decomposition. Bayesian evidence (PolyChord) queued.

**Read this first — the result decouples into two independent claims:**

1. *ΛCDM + free N_eff, refit, gains 19.2 in χ² on the Planck+BAO+SN stack*
   (driven by ξ_Neff and re-optimized H0/n_s along the acoustic-locked
   ridge, §6) — **and this claim is already under pressure from ACT DR6**
   (measured here directly: +22.7 at the best-fit point, §9.1).
2. *CDM+Λ can be rewritten as one barotropic fluid with no observable
   consequence at linear order* (§3–§4; proven exactly and verified
   numerically, §4.2).

Neither claim borrows support from the other. The unification (2) is the
theoretically interesting structure; the χ² gain (1) is ordinary
extra-radiation phenomenology that any N_eff extension would produce. §4.2
spells out what this means for interpretation.

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

**The v5 microphysical realization — asymptotic, provably never exact.**
First the no-go, which is stronger than a truncation caveat: **no purely
kinetic $P(X)$ realizes $p \equiv -\rho_\infty$ exactly over any interval of
field states.** If $P(X)$ is constant on an interval, $P_X = 0$ there, and
then $\rho = 2XP_X - P = \rho_\infty$ is pinned constant too — pressure
cannot stay fixed while the density sweeps a continuum. This holds for any
$P(X)$, not just a particular expansion. The best possible microphysics is
therefore asymptotic: expand $P(X)$ about an extremum $X_0$ ($P_X(X_0)=0$),

$$ P(X) \simeq P_0 + \tfrac12 P_2\,(X-X_0)^2 , \qquad u \equiv X - X_0 . $$

The conserved current $a^3 P_2 u \sqrt{2(X_0+u)} = \text{const}$ gives, order
by order, $u = u_{(1)} + u_{(2)}$ with $u_{(1)} \propto a^{-3}$ and
$u_{(2)} = -u_{(1)}^2/2X_0 \propto a^{-6}$; substituting into
$\rho + P_0 = 2X_0P_2u + \tfrac32 P_2u^2$ leaves

$$ \rho(a) = \rho_\infty + K a^{-3} + \tfrac12 P_2\,u_{(1)}^2 \propto a^{-6}\ \text{(stiff, w=+1-like tail)} , $$

with $\rho_\infty = -P_0$ and $c_s^2 = P_X/(P_X+2XP_{XX}) = u/(3u+2X_0) \to 0$.
This is the Scherrer purely-kinetic unified-dark-matter construction
(PRL 93, 011301, 2004), carried one order beyond leading. Consequences,
stated honestly:

- §2 establishes **existence** of a no-ghost, no-gradient UV completion with
  a computable error budget — not an exact derivation. The phenomenological
  $w(\rho) = -\rho_\infty/\rho$ of §1/§3 is what is actually implemented and
  integrated.
- Validity across the observationally exercised range requires a **designed
  hierarchy**, and since $u \propto a^{-3}$ grows into the past, the binding
  condition is set by the *earliest* epoch that needs dust behavior. With
  $x \equiv u/X_0$ and $\rho_\infty$ dropped (negligible before today),

  $$ w(x) = \frac{x}{4+3x}, \qquad c_s^2(x) = \frac{x}{3x+2} \;\approx\; 2\,w \ \ (x \ll 1), $$

  so the basin-membership markers ($x \sim 1$: $e^{-25}$ today for
  equality, $e^{-66}$ for BBN) are **qualitative crossover points, not
  safe-dust thresholds**. At $x(z_{\rm eq}) = 0.55$ (the $e^{-25}$ case)
  the fluid has $w \approx 0.10$, $c_s^2 \approx 0.15$ at equality — not
  dust. Quantitative thresholds: $w < 0.01$ at equality needs
  $x_0 \lesssim e^{-27.6}$; $c_s^2 < 0.01$ needs $x_0 \lesssim e^{-28.3}$;
  and because a dark-matter sound speed suppresses $P(k)$ *cumulatively*
  below the sound horizon (the same Sandvik-type mechanism that killed β,
  §5) while $w$ only perturbs the background locally in time, **the sound
  speed is the binding condition**. Both computed 2026-07-06:

  - **P(k)/Jeans bound.** $c_s^2(a) = (x_0/2)a^{-3}$ defines a Jeans scale
    $k_J^2 = 3H_0^2\Omega_m a^2/x_0$ that sweeps *up* through the
    observable band ($k_J \propto a$); modes with $k > k_J(a_{\rm eq})$
    start growing late and lose power by $(a_{\rm eq}/a_k)^2$. No
    matter-era damage requires $x_0 \lesssim e^{-28.6}$ at $k=0.1$/Mpc,
    $e^{-30.0}$ at $k=0.2$, $e^{-33.2}$ at $k=1$/Mpc.
  - **Pre-basin BBN bound (the binding one).** Before basin entry
    ($x > 1$, at $z_x$ where $x_0 e^{3\ln(1+z_x)} = 1$) the fluid is
    radiation-like ($w = c_s^2 = 1/3$; self-consistency: for $u \gg X_0$
    the conserved current gives $u \propto a^{-2}$, so
    $\rho \approx \tfrac32 P_2 u^2 \propto a^{-4}$ — the two regimes'
    scaling laws glue together correctly), with the elegant property that
    its density is a **constant fraction** of the radiation bath:
    $\rho_d/\rho_r = a_x/a_{\rm eq}$, i.e.
    $\Delta N_{\rm eff} = 7.45\,(a_x/a_{\rm eq})$ at all $z > z_x$ —
    including BBN. Requiring $\Delta N_{\rm eff}^{\rm BBN} < 0.2$ gives
    $z_x \gtrsim 1.3\times10^5$, i.e. $\boxed{x_0 \lesssim e^{-35.2}}$ —
    which automatically satisfies every P(k) and halo condition above
    (at the bound, $c_s^2(z_{\rm eq}) \approx 9\times10^{-6}$). The only
    escape is a full $P(X)$ whose large-$u$ behavior departs from the
    quadratic before BBN — logically possible, but then the completion's
    early history is an unconstrained UV story rather than a prediction.

  So the completion's single tuning number is $x_0 \lesssim e^{-35}$,
  set by BBN, with everything else downstream. Cubic terms of the full
  $P(X)$ must stay subdominant over the same range. Achievable to any
  target precision; tuned, and honestly labeled as such.
- **Outside the basin the truncated completion is not dust**: for
  $u \gg X_0$, $P \propto X^2$ gives $w = 1/3$, $c_s^2 = 1/3$ — a
  self-interacting dark-radiation phase (this is in Scherrer's original
  analysis, which requires basin entry "sufficiently early" for the same
  reason). So the completion's early history is a **falsifiable
  prediction**, twice over: the $a^{-6}$ stiff tail just inside the basin,
  and an effective ΔN_eff contribution at BBN if basin entry postdates it —
  the latter interacting directly with the model's own sampled ξ_Neff.
  "How close to the extremum" is an empirical question, not aesthetics;
  attaching numbers (Y_p, D/H shifts vs entry redshift) is an open item
  (§11).

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

**Resurrection test (2026-07-06, sandboxed v4 build; β stays deleted).**
Two hypotheses were given their best shot: (a) β might engage in synergy
with the *engaged* best-fit partners (H0=70.4, ξ=0.403 — the original MCMC
sampled jointly, but this pins them at their optimum); (b) β's σ8
suppression might be rewarded by weak lensing, the one dataset never tested
against β and the one that *wants* lower S8. Scan at the frozen best fit
with DES Y1 cosmic shear added:

| log₁₀β | plik | lensing | SN | DES shear | σ8 | Δtotal |
|---|---|---|---|---|---|---|
| −12 (null) | 593.2 | 9.5 | 1467.2 | 239.8 | 0.8277 | — |
| −8 (v4 MCMC "best") | 592.9 | 9.6 | 1467.2 | 241.4 | 0.8268 | +1.4 |
| −7 | 589.0 | 12.9 | 1467.2 | **269.9** | 0.8190 | +29.1 |
| ≥ −6.5 | — | — | — | — | — | model non-viable |

The verdict is stronger than the original deletion argument: **DES rejects
β harder than any other dataset** (+30 at β=10⁻⁷ while σ8 moves exactly the
direction WL "wants") because β's suppression is a scale-dependent P(k) cut
below the sound horizon, not the amplitude shift lensing prefers — the GCG
literature's warning, measured. At β ≥ 3×10⁻⁷ the high-k perturbation
integration (DES needs P(k) to ~15/Mpc) goes stiff and the model is not
even computable. The logA-compensation probes are moot: amplitude cannot
repair a shape defect. β fails in its designed role, with engaged partners,
against its friendliest dataset.

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
| exact null (fluid ⇒ ΛCDM; v5 form) | **PASS** — σ8 0.81301 vs anchor 0.81304, total 2516.7 vs 2515.5; re-verified bit-identical after the 2026-07-06 gauge-IC fix (σ8 0.81301, total 2516.72) |
| ξ_Neff ↔ N_ur equivalence | **PASS** — bit-exact (difference 0.0 everywhere) |
| precision stability | **PASS, with a real discovery (2026-07-06).** The re-run matrix appeared to fail this test — until the "tightened" knob turned out to be a *loosening*: the in-tree `precisions.h` default for `tol_background_integration` is **1e-10** (not vanilla CLASS's 1e-2; tightened during the v4 stiff-system work), so passing any explicit value overrode it. The dcdf background ODE spans ~42 e-folds and converges slowly in this tolerance: at vanilla 1e-2 the background is ~10% wrong (σ8 0.784→0.661!), at 1e-4 still 0.4% off, converging to the exact closed form only near the in-tree default (verified: 4×10⁻⁸ against ρ_∞+Ka⁻³; θ* stable). All production runs use the converged default. A guard now refuses `use_dcdf` with tolerance > 1e-8. |
| β-branch smoothness (pre-deletion, 8×10⁻⁹→10⁻⁴) | **PASS** — smooth monotone σ8 decline (then β removed) |
| gauge invariance (synchronous vs newtonian) | **PASS** (2026-07-06, after fix) — max TT deviation 2.8×10⁻⁵, at ΛCDM's own gauge-noise floor (2.1×10⁻⁵). The v4-era 0.26% ℓ=10–12 defect was **not** the suspected late-time (1+w)→0 gauge terms: the fluid was missing from the matter budget in `perturbations_initial_conditions` (`rho_m`/`om` counted only baryons under `use_dcdf`, and the α gauge-transform's `delta_tot` had no dcdf term), so the newtonian branch started from a slightly wrong φ_ini and rang a decaying transient into the SW/early-ISW sources. Synchronous (production) was verified unaffected before and after: fluid ≡ ΛCDM per-ℓ to 4×10⁻⁶ at the null point. Note the epistemic status: the `rho_m`/`om` half of the bug lived in IC code shared by both gauges, so synchronous safety was an **empirical finding** (bit-identical null test, σ8 0.81301 / total 2516.72 before and after the fix), not a structural guarantee — only the `delta_tot` half was newtonian-only by construction. Diagnosis chain: per-ℓ ΛCDM control → dust-limit isolation → per-contribution double ratio (SW+eISW, not late ISW) → φ′ transient at z≈5000 → IC audit. |
| 6-corner prior-box stress test (v5, β-free) | **PASS** — all corners run gracefully |

The null test earns its keep: on its first run it caught the budget-
overclosure bug (§3), a real +20-χ² error invisible to every other check.

**Matrix re-run provenance (2026-07-06):** the entire suite above was
re-executed on a single verified binary (gauge IC fix + input guards;
`build/input.o` checked directly, not just `.so` mtimes, since a re-linked
module can carry a fresh timestamp over a stale archive). Results: null
bit-identical (σ8 0.81301, total 2516.72), gauge 2.84×10⁻⁵, ξ↔N_ur
bit-exact (0.0), precision converged (row above), all 6 corners graceful.
The same pass produced the tolerance discovery and its guard — re-running
"already passed" tests on the current binary is what caught it.

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

**Evidence:** in flight. The original MH run predated the β deletion and was
killed and relaunched β-free (`dcdf_forge_v2.yaml`, same priors, refs seeded
at the v4 best fit); superseded in the queue by the joint Planck+ACT+SPT
refit (`dcdf_joint_v1.yaml`, running 2026-07-06); the PolyChord pair (dCDF
`dcdf_pc_v1.yaml` vs ΛCDM twin `lcdm_pc_v1.yaml`, nlive 500, num_repeats 2d)
is queued behind it.

**Phenomenology at the best fit (2026-07-06 probes, vs the ΛCDM anchor):**
age 13.40 Gyr (vs 13.79; both above the ~12.8 Gyr globular-cluster floor);
r_s(drag) 143.5 vs 147.1 Mpc — the ξ_Neff sound-horizon compression that
finances the higher H0, stated as a number; z_eq 3348 vs 3404. Growth:
fσ8(z) against ten compiled RSD points (6dF, MGS, DR12×3, WiggleZ×3,
VIPERS, eBOSS QSO) gives naive χ² 7.75 vs ΛCDM's 7.75 — **statistically
indistinguishable**, the §4.2 degeneracy visible in real growth data. The
linear P(k) ratio vs ΛCDM is a smooth tilt (−17% at k=10⁻⁴/Mpc to +7% at
k=5/Mpc, crossing unity near k≈0.2) — pure (n_s, ω_b, N_eff, Ω_m)
re-optimization, no dark-sector feature; the BAO-band residual (2.7%) is
the r_s phase shift the BAO likelihoods absorb by construction. Back-of-envelope from prior/posterior
widths: Δln Z ≈ +5 to +7 in dCDF's favor if the χ² gain survives
marginalization — the +1-parameter Occam penalty is small because the one
extra parameter (ξ) is doing real work.

## 9. External falsifiers — first one now measured, and it bites

1. **Damping tail (ACT DR6 / SPT-3G): TESTED 2026-07-06 — in tension.**
   The best fit *requires* N_eff ≈ 3.45 and n_s ≈ 0.983; published ACT DR6
   analyses prefer N_eff ≈ 2.9 ± 0.13, ~4σ below. Measured directly in this
   pipeline (point evaluation at the frozen best fit, candl likelihoods,
   calibrations profiled, no refit):

   | dataset | ΛCDM anchor | dCDF best fit | Δχ² |
   |---|---|---|---|
   | ACT DR6 CMB-only TT/TE/EE (135 bdp) | 161.9 | 184.6 | **+22.7** |
   | SPT-3G 2018 TT/TE/EE lite (123 bdp) | 140.5 | 139.4 | −1.1 |

   ACT DR6's damping-tail penalty (+22.7) is the same size as the entire
   Planck+BAO+SN gain (−19.2). SPT-3G (ℓ ≤ 3000, larger errors) is neutral.
   Caveats: a point evaluation overstates tension relative to a joint refit
   — the flat H0–ξ ridge (§6) means a Planck+ACT fit will slide toward
   lower ξ (≈0.15) and lower H0 (≈69), where the Planck-side cost is only
   +11.6 and the ACT penalty largely dissolves. **Honest reading: ACT DR6
   does not kill the model, it compresses the H0 relief from ~3 km/s/Mpc
   toward ~1.5 km/s/Mpc.** A joint Planck+ACT+SPT refit is the required
   next fit, not optional follow-up. (Setup: `candl` + data at
   `~/candl_data`; script in job scratch `act_spt_test.py`.)
2. **Weak lensing S8.** Prediction (joint-refit point) S8 = 0.824: mild
   easing toward the WL preference (~0.77), not a resolution. A joint WL
   fit must not degrade the CMB side. Note the Σm_ν interaction (§9.5).

4. **Varying electron mass (§9.4, tested 2026-07-06).** The
   epoch-response audit identified recombination *timing* as the one H0
   lever the damping tail cannot tax (it changes when recombination
   happens, not H at recombination). Measured, θ*-locked, on the joint
   stack: +1 km/s/Mpc per +1% m_e with **ACT indifferent-to-favorable**
   (163.1 vs 164.0 at m_e=1.01 refit) — the executioner moves to plik's
   peak structure, and the cost curve is steep beyond ~1.5%
   (frozen-slice: +7.9 / +58.9 / +289 at 1/2/4%). A fixed-m_e=1.01
   profile refit reached **2801.06 with H0 = 70.41, ξ = 0.124** — note
   m_e visibly eats ξ's role (the two levers share the r_s budget). The
   >100% refund flags optimization slack in pass-1; a same-companions
   m_e=1.00 control (running) decomposes m_e's honest credit, estimated
   −1 to −3. S8 rises with m_e at fixed amplitude (+0.02/1%) — m_e alone
   anti-solves S8; pairs naturally with Σm_ν (below).

5. **Σm_ν and c_EM (frozen-slice scans, 2026-07-06).** Σm_ν: on a stack
   with no WL likelihood the best fit is pinned at the 0.06 eV floor
   (+12.2 at 0.12 eV, ACT +5.6 joining plik); its S8 payoff
   (0.805 at 0.12 eV) is *unpriced* by current data — the lever becomes
   live only if DES shear joins the stack (projected wash, ±2, at
   Σm_ν ≈ 0.10 with S8 ≈ 0.81). The environmental-exchange coupling
   c_EM is **dead**: +261 at c_EM = 0.005 (plik +198, ACT +41, S8→0.869)
   for 0.5 km/s of H0 — a w-kick on the *dominant* component through
   recombination wrecks the acoustic structure with no clustering
   discount. The environment-coupling idea survives only as
   recombination-rule changes (m_e), not energy-exchange terms.
   ρ_∞(z) drift: queued as a *constraint measurement* (the DESI-flavored
   "is the account being funded" question), expected best fit δ ≈ 0.
3. **BBN: checked at fitting-formula grade (2026-07-06).** With standard
   linearized sensitivities (ΔY_p ≈ 0.0127·ΔN_eff and ∂Y_p/∂ln ω_b ≈
   0.0096, i.e. Y_p ∝ ω_b^0.039; ∂ln(D/H)/∂ln ω_b ≈
   −1.6, ∂ln(D/H)/∂N_eff ≈ +0.10):
   at the best fit (ω_b = 0.0228, ΔN_eff = 0.403), Y_p ≈ 0.2524 — **+1.9σ**
   vs Aver et al. (0.2449 ± 0.0040) — while D/H ≈ 2.55×10⁻⁵ is only +0.8σ
   vs Cooke et al. (2.527 ± 0.030), because the higher ω_b and higher N_eff
   pull D/H in opposite directions and nearly cancel. Helium is thus the
   lone BBN discriminant, mildly disfavoring ξ = 0.40; at the expected
   joint-refit optimum (ξ ≈ 0.15, ω_b ≈ 0.0224) it relaxes to
   Y_p ≈ 0.2492, +1.1σ — unremarkable. PRIMAT-grade confirmation remains
   open (§11). The §2 completion's a⁻⁶ stiff tail / pre-basin radiation
   phase is independently BBN-constrainable (§11).

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

## 10a. Domain of validity: nonlinear structure and compact objects

Because the fluid is ΛCDM-degenerate at linear order (§4.2), its distinctive
physics could only appear nonlinearly — and that is exactly where the
framework has a **structural** limit, not a numerical one:

- **Caustics / no multistreaming.** With c_s² = 0 the field free-falls, and
  dust free-fall forms caustics. CDM survives shell-crossing because
  particles multistream (the phase-space sheet folds); a classical scalar's
  ∇φ is single-valued and cannot fold. At first shell-crossing the fluid
  description this document rests on has already broken down — independent
  of how sensible the δ_m bookkeeping (§4.1) looks. This is the known
  Achilles heel of purely-kinetic unified dark matter; the known
  regularization (ghost-condensate-type higher-derivative terms, e.g.
  (□φ)²) halts caustics at the cost of new UV structure, which reopens the
  §2 exactness question. **Honest scope: linear cosmology solid, virialized
  structure unproven.**
- **Compact objects: dCDF-blind by design.** The fluid couples to baryons
  only through g_μν. Inside a neutron star the dark-sector density is set
  by gravitational capture (~GeV/cm³) against nuclear matter at
  ~1.5×10³⁸ GeV/cm³ (n₀ ≈ 0.16 fm⁻³ × 939 MeV) — 38 orders of magnitude of
  suppression. There is no mechanism by which dCDF matters there, and
  adding one (the `dcdf_c_gamma`/`dcdf_c_EM` sandbox knobs are exactly such
  couplings) reopens the fifth-force/EP constraints that killed v1–v3.
  Minimal coupling also gives GW speed = c exactly (GW170817 trivially
  satisfied). Black holes: shift symmetry supports no-hair conclusions
  (quasi-static accretion at CDM-negligible local density); note the
  Hui–Nicolis theorem is usually stated for Galileon-type/derivatively
  coupled shift-symmetric scalars — its clean applicability to bare P(X)
  should be cite-checked, though the k-essence-accretion literature reaches
  the same conclusion independently. The model's compact-object prediction
  is deliberately boring: identical to ΛCDM.

## 11. Open items

- **Joint Planck+ACT DR6+SPT-3G refit** (§9.1) — now the top-priority fit:
  it determines how much H0 relief survives the damping tail. Expected
  landing zone: the H0 ≈ 69, ξ ≈ 0.15 part of the ridge.
- **Evidence numbers**: CosmicForge v5 MH rerun (`dcdf_forge_v2`, β-free,
  relaunched 2026-07-05 after β deletion) + PolyChord pair queued behind
  it; that decides whether the χ² gain is a detection or a flexible-model
  tax — and any evidence verdict must be re-read against §9.1.
- **BBN check** of ΔN_eff = 0.40 and of the §2 a⁻⁶ tail / pre-basin
  radiation phase (Y_p, D/H shifts as a function of basin-entry redshift).
- **P(k)-suppression integral: COMPUTED 2026-07-06** (see §2) — the Jeans
  analysis gives $x_0 \lesssim e^{-30}$ (LSS to $k=0.2$/Mpc), and the
  pre-basin radiation phase gives the binding BBN bound
  $x_0 \lesssim e^{-35}$, which implies all others. Remaining: cross-check
  the analytic Jeans estimate with a full Boltzmann run (a c_s²(ρ)-enabled
  branch would be needed — low priority since BBN binds regardless). Compute in linear theory up to
  first shell-crossing only — the domain §10a scopes as trustworthy. (In
  collapsing regions the local $x \propto \rho_d$ runs ahead of the
  background at equal cosmic time, but it cannot actually exit the basin
  there: virialized densities are $\sim e^{13} x_0$, eleven e-folds below
  the equality-era background value $e^{24.4} x_0$, so any hierarchy that
  survives equality automatically covers every halo in the late universe —
  with the corollary $c_s^2({\rm halo}) \sim x_0 e^{13}/2 \lesssim 10^{-7}$,
  i.e. the completion's residual stays dust-like inside structure. This
  covers early-forming halos too, not just present-day ones: a halo's
  virial density freezes in at $\Delta_{\rm vir}\bar\rho_m(z_{\rm form})$,
  which would rival the equality-era mean only for
  $z_{\rm form} \approx (1+z_{\rm eq})/200^{1/3} \approx 580$ — long before
  any structure can collapse (first minihalos: $z \sim 20$–$30$), leaving
  $\sim(580/30)^3 \approx 7000\times$ density headroom for the earliest
  objects that ever form. What
  remains at shell-crossing is §10a's caustic limit: §2's tuning bound and
  §10a's structural limit are one boundary, not two independent gaps.)
- **Nonlinear completion** (§10a): specify the higher-derivative terms (or
  the honest effective-theory boundary) before any claim about halo
  interiors.
- **No-hair citation check** (§10a) for bare P(X).
- **SIDM-type extension scoping** (`PRTOE_v5_SIDM_scoping.md`): the lawful
  place for new dark-sector physics is density-dependent *interactions*
  (not sound speed — §5 closed that door).

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
