# dCDF v5 — The Complete Model: Physics, Math, Implementation, Results

> **HISTORICAL RESULTS RECORD (banner added 2026-07-13):** the July-6 refit tables below are the frozen record of that fit — numbers herein (H₀ = 69.70, the χ² tables) are that era's; the current production state and its live zero-parameter test: [PRTOE_THE_AMPLITUDE.md](../PRTOE_THE_AMPLITUDE.md) / [PRTOE_DEPENDENCY_TREE.md](../PRTOE_DEPENDENCY_TREE.md).

> *Some statuses in this file may be superseded by later work; the current conditionality of every claim is tracked in [PRTOE_DEPENDENCY_TREE.md](../PRTOE_DEPENDENCY_TREE.md).*

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](../PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](../PRTOE_DEPENDENCY_TREE.md).*


**Status (2026-07-06): current production model.** This document is
self-contained: the action, the background and perturbation equations as
implemented, why the model has exactly this form (including the death of β),
the parameter accounting, the validated results, and the open falsifiers.
It supersedes reading `PRTOE_v4_dCDF_derivation.md` + `PRTOE_v4_dCDF_results.md`
as a pair; those remain the historical record of how v4 → v5 happened.
Companion documents: `PRTOE_PREREGISTERED_PREDICTIONS.md` (the no-hedge
registry, P-2026-001 through -005), `PRTOE_INTERACTION_ATLAS.md` (every
derived fixed relation, admission rule: derived-only, falsified
entry-by-entry), `the internal validation record` (the adversarial review dialogue,
14 turns, formally closed 2026-07-06 with verdict "not proven —
survived"; the four-verdict calculation of §11 is the agreed re-entry
point).

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
| **Planck+BAO+SN stack:** ΛCDM anchor (H₀=67.4) | 2515.45 | — |
| dCDF best fit (H₀=70.40, ξ=0.403) | 2496.24 | −19.2 |
| **Joint stack (+ ACT DR6 + SPT-3G):** ΛCDM frozen / refitting | 2817.9 → ~2810 | — |
| dCDF joint refit (**H₀=69.05, ξ=0.142**, n_s=0.979) | **2809.81** | ≈ tie |
| **THE DYAD** (2026-07-06 BBN-priced refit): fluid + m_e=1.01, **ξ EXECUTED → 0.012** | raw **2798.36**, honest (incl. BBN) **2803.3** at **H₀ = 69.70** | **−6.5 to −8.5** vs refit ΛCDM+BBN (band until the twin completes) |

**The dyad is the current model**: under the full self-consistent stack
(Planck+ACT+SPT+BAO+SN+BBN) the optimizer executed ξ_Neff entirely —
the H₀ story is carried by recombination timing alone, at +1 effective
parameter, with plik *better than the ΛCDM anchor's own* (586.5 vs
586.9) and both tensions eased (H₀ 69.7 = the TRGB ladder value;
S₈ ≈ 0.823). **Two riders belong in this headline, not in footnotes:**
(i) the joint advantage is quoted as a band —
its ΛCDM+BBN baseline was mid-refit when measured; (ii) the champion
carries a **−2.0σ deuterium row** (D/H = 2.468×10⁻⁵, χ² 3.85): the
model holds ω_b for the CMB and underfeeds deuterium — a residual it
cannot relieve without paying the CMB back.
**[SCAR REPRICED, 2026-07-07 — two-barrel attack; see §11
addendum]:** (i) the −2.0σ used obs-only errors; with the post-LUNA
nuclear-theory error (PRIMAT ±0.037, cite-verified) the deuterium row is
**−1.2σ**, and the inter-code controversy (PRIMAT 2.439 vs
PArthENoPE ~2.51-2.54; ΛCDM itself at 1.85σ under PRIMAT —
arXiv:2011.11320 vs 2011.11537) is LARGER than the model's marginal
cost; the champion sits CLOSER to the observed D/H than PRIMAT-ΛCDM
does. (ii) The "cannot relieve without paying the CMB back" clause
is FALSIFIED by the model's own completion: the pre-basin w = 1/3
phase is BBN-only dark radiation (ΔN_eff = 7.45 a_x/a_eq, §11's
boxed bound) that becomes the dark matter itself at basin entry
z_x ~ 10⁵ — invisible to recombination. At optimal z_x ≈ 1.7×10⁵
(inside the booked bound), ΔN_eff(BBN) = 0.15 heals D/H to −0.7σ at
a helium price (Y_p +1.4σ → +1.9σ), net Δχ²_BBN ≈ −1.75. §11's open
item (Y_p/D/H vs entry redshift) is thereby CLOSED, with a healer's
sign. (iii) Headline cascade: the dyad's honest-incl-BBN charge
reprices 5.9 → 3.6 under σ_th, widening the dyad-vs-ΛCDM gap by
~2 χ² (ΛCDM's own BBN charge barely moves). The deuterium row's honest final
form: ~1σ-class inside the field's shared nuclear fog, with a
model-owned bounded partial healer. And the §4.2 rider rides
on: the −8 is m_e's; the fluid is degenerate through all of it — the
dyad wins while the unification watches it win. Census: known
radiation, baryons, one dark medium, one rules amendment. See
P-2026-001 for the no-hedge prediction this commits the model to.

**The joint refit happened (2026-07-06) and landed exactly on the
predicted ridge point** — H₀ = 69.05, ξ = 0.142 vs the pre-registered
"H₀ ≈ 69, ξ ≈ 0.15" (§9.1). Against the *refitting* ΛCDM twin the joint
stack is heading to a statistical tie: the honest current claim is **equal
fit quality on every dataset simultaneously, with H₀ = 69.0 and
S₈ = 0.824 vs ΛCDM's 67.4 / 0.833** — both tensions eased directionally at
zero χ² cost, for one extra parameter. The varying-m_e extension (§9.4,
same-day discovery) may buy H₀ back to ~70.4; its honest credit awaits the
optimization-slack decomposition. Bayesian evidence (PolyChord) queued.

**Read this first — the result decouples into two independent claims:**

1. *ΛCDM + free N_eff, refit, gains 19.2 in χ² on the Planck+BAO+SN stack*
 (driven by ξ_Neff and re-optimized H₀/n_s along the acoustic-locked
 ridge, §6) — a claim that ACT DR6 has now **adjudicated**: the joint
 refit landed on the predicted down-ridge point (H₀ = 69.05, ξ = 0.142)
 and the joint stack is a statistical tie against refit ΛCDM. The
 surviving version of claim 1: *equal fit quality everywhere, both
 tensions eased directionally, zero χ² cost, +1 parameter* — plus a
 possible H₀ → 70.4 extension via recombination timing (m_e, §9.4)
 whose credit is under measurement.
2. *CDM+Λ can be rewritten as one barotropic fluid with no observable
 consequence at linear order* (§3–§4; proven exactly and verified
 numerically, §4.2).

Neither claim borrows support from the other. The unification (2) is the
theoretically interesting structure; the fit behavior (1) is ordinary
expansion-history phenomenology that any same-parameter extension would
produce. §4.2 spells out what this means for interpretation.

---

## 2. Action and microphysics

$$ S = \int d^4x\,\sqrt{-g}\left[\frac{M_{\rm pl}^2}{2}R + P(X)\right] + S_m[g_{\mu\nu},\psi], \qquad X \equiv -\tfrac12 g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi $$

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

$$ P(X) \simeq P_0 + \tfrac12 P_2\,(X-X_0)^2, \qquad u \equiv X - X_0 . $$

The conserved current $a^3 P_2 u \sqrt{2(X_0+u)} = \text{const}$ gives, order
by order, $u = u_{(1)} + u_{(2)}$ with $u_{(1)} \propto a^{-3}$ and
$u_{(2)} = -u_{(1)}^2/2X_0 \propto a^{-6}$; substituting into
$\rho + P_0 = 2X_0P_2u + \tfrac32 P_2u^2$ leaves

$$ \rho(a) = \rho_\infty + K a^{-3} + \tfrac12 P_2\,u_{(1)}^2 \propto a^{-6}\ \text{(stiff, w=+1-like tail)}, $$

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
 (H₀, n_s) along the θ*-locked ridge (§6) — **not** by the fluid's internal
 dynamics.
- The unification itself is presently an *interpretation with equal
 likelihood*. The once-claimed "parameter economy" is **conceded false**
 (2026-07-06): ρ_∞ replaces ω_cdm one-for-one and Λ
 closes by flatness in both models, so the evidence attributable to the
 unification alone is pure prior volume — Δln Z ≈ −0.9 ± 0.5 with the
 declared priors, i.e. slightly *against*. What the unification buys is
 a framework in which the dark sector can lawfully acquire
 density-dependent physics later (the higher-derivative/SIDM route,
 `docs/PRTOE_v5_SIDM_scoping.md`), not statistics. It is not the source
 of any fit improvement.
- Anything that would make the fluid *observably* different from ΛCDM at
 linear order (a sound speed, a w(ρ) deformation) is exactly what the data
 killed (§5).

---

## 5. How β lived and died (the sound-speed trap)

v4 carried a two-parameter equation of state
$w(s) = -\exp[-(s+\beta s^2)]$, giving $c_s² = 2\β s\,e^{-(s+\β s²)}
\ge 0$ with peak $\approx 0.74\β$. The design goal was to decouple "how
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
with the *engaged* best-fit partners (H₀=70.4, ξ=0.403 — the original MCMC
sampled jointly, but this pins them at their optimum); (b) β's σ8
suppression might be rewarded by weak lensing, the one dataset never tested
against β and the one that *wants* lower S₈. Scan at the frozen best fit
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
 The viable region is a one-dimensional ridge in (H₀, ξ):
 ξ ≈ 0.15 at H₀=69 → 0.40 at 70.4 → 0.60 at 71 → 1.0 at 73.
 Off-ridge points are catastrophic (+0.9% in θ* ≈ +1600 on plik).
2. **The damping tail prices the H₀ relief.** Along the ridge, the Silk-
 damping cost grows ~quadratically in ξ: totals +11.6 at H₀=69, +228 at
 71, +759 at 73, +1418 at 74.8 (fixed fiducials). The n_s–N_eff degeneracy
 absorbs part (optimum n_s ≈ 0.98); higher ω_b does not help.
3. **SN push the other way.** Pantheon+SHOES gains saturate at ~−40 by
 H₀ ≈ 73. The net optimum of (2) vs (3) lands at **H₀ ≈ 70–70.5** —
 closing ~55% of the gap to SH0ES (74.0 ± 1.0), endorsed by the SN
 likelihood (−27.8), blocked beyond that by the damping tail.

## 7. Validation — the falsifiable-test matrix (all at/near best fit)

| test | verdict |
|---|---|
| exact null (fluid ⇒ ΛCDM; v5 form) | **PASS** — σ8 0.81301 vs anchor 0.81304, total 2516.7 vs 2515.5; re-verified bit-identical after the 2026-07-06 gauge-IC fix (σ8 0.81301, total 2516.72) |
| ξ_Neff ↔ N_ur equivalence | **PASS** — bit-exact (difference 0.0 everywhere) |
| precision stability | **PASS, with a real discovery (2026-07-06).** The re-run matrix appeared to fail this test — until the "tightened" knob turned out to be a *loosening*: the in-tree `precisions.h` default for `tol_background_integration` is **1×10⁻¹⁰** (not vanilla CLASS's 1×10⁻²; tightened during the v4 stiff-system work), so passing any explicit value overrode it. The dcdf background ODE spans ~42 e-folds and converges slowly in this tolerance: at vanilla 1×10⁻² the background is ~10% wrong (σ8 0.784→0.661!), at 1×10⁻⁴ still 0.4% off, converging to the exact closed form only near the in-tree default (verified: 4×10⁻⁸ against ρ_∞+Ka⁻³; θ* stable). All production runs use the converged default. A guard now refuses `use_dcdf` with tolerance > 1×10⁻⁸. |
| β-branch smoothness (pre-deletion, 8×10⁻⁹→10⁻⁴) | **PASS** — smooth monotone σ8 decline (then β removed) |
| **dyad-configuration battery (2026-07-06, new machinery: m_e sampled, ξ deleted, YHe λ)** | **ALL PASS (5/5).** [1] m_e→1 null: dyad config at m_e=1 reproduces v5-anchor physics smoothly (σ8 0.82799, θ* 1.04929). [2] Gauge invariance *at m_e=1.01* (never before tested with varying constants on): max \|ΔCl/Cl\| = 1.6×10⁻⁴ at ℓ=4 — passes the 10⁻³ gate; note this is ~6× the ΛCDM gauge-noise floor, consistent with the varying-constants module's own gauge sensitivity, not a dcdf defect (the m_e=1 limit reproduces the 2.8×10⁻⁵ figure). [3] Precision stability at the dyad optimum (bg guard active): σ8 shift 5.9×10⁻⁶. [4] Both m_e prior corners (0.98, 1.04) graceful. [5] YHe table → self-consistent λ at the market optimum: σ8 shift 10⁻⁵, max Cl shift 6.6×10⁻³ — the booked inconsistency's measured size, matching the §9.3 pricing (−0.4 in χ², sign-favorable). |
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
| H₀ | 67.4 | **70.40** |
| ln(10¹⁰A_s) | 3.044 | 3.068 |
| n_s | 0.9649 | **0.9826** |
| z_reio | 7.67 | 8.13 |
| ξ_Neff | — | **0.403** |
| ρ_∞ | — | 0.7007 |
| A_planck | 1.0 | 1.0019 |

Derived: σ8 = 0.827, **S₈ = 0.826** (ΛCDM 0.833), Ω_m ≈ 0.30.
χ² breakdown vs ΛCDM: plik +10.2, lensing +0.6, lowl.TT −2.1, BAO −0.1,
**SN −27.8** → total **−19.2**. A second multistart mode at H₀=69.44
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
finances the higher H₀, stated as a number; z_eq 3348 vs 3404. Growth:
fσ8(z) against ten compiled RSD points (6dF, MGS, DR12×3, WiggleZ×3,
VIPERS, eBOSS QSO) gives naive χ² 7.75 vs ΛCDM's 7.75 — **statistically
indistinguishable**, the §4.2 degeneracy visible in real growth data. The
linear P(k) ratio vs ΛCDM is a smooth tilt (−17% at k=10⁻⁴/Mpc to +7% at
k=5/Mpc, crossing unity near k≈0.2) — pure (n_s, ω_b, N_eff, Ω_m)
re-optimization, no dark-sector feature; the BAO-band residual (2.7%) is
the r_s phase shift the BAO likelihoods absorb by construction.

**Evidence forecast, honestly layered (updated 2026-07-06 after the joint
refit).** The naive estimate — Δln Z ≈ +5 to +7 for dCDF from Δχ²/2 ≈ 9.6
minus ξ's Occam penalty ≈ 2 — applies only to the **Planck+BAO+SN stack**,
and will be largely moot the day it lands: that stack omits data
(ACT DR6) we now know is decisive. The layered forecast:

1. *Planck-only PolyChord pair (queued)*: dCDF by ≈ +6 to +8. A semifinal
 trophy awarded after the final was scheduled.
2. *Joint stack, ξ-only model*: Δχ² ≈ 0 (measured tie vs the refit twin)
 minus the same penalty → **ΛCDM by ≈ 1–2**. The flexible-model tax.
3. *Joint stack with the m_e extension (§9.4)*: if the matched-protocol
 control confirms a clean m_e credit of −5 to −9, the triad carries
 Δln Z ≈ 0 to +2 on the dCDF side for +2 parameters — marginal, real,
 and attached to a mechanism (recombination timing) rather than a
 budget knob. This is the live number; it is being measured as this
 revision is written.

**The SH0ES→TRGB scenario (2026-07-07 night; robustness diagnostic,
not a stack change — priors frozen, P-2026-001 remains the referee).**
Four point-evaluations (both models × both SN calibrations) plus the
CCHP-2025 local anchor (69.96 ± 1.54, cite-verified):

| | SN(Pantheon+SHOES) | SN(Pantheon+, shape-only) |
|---|---|---|
| dyad (H₀=69.70) | 1473.4 | 1406.3 |
| ΛCDM anchor (67.4) | 1494.9 | 1403.7 |

Read honestly in both directions: (i) the dyad's SN advantage under
SHOES (−21.5) EVAPORATES under calibration-free Pantheon+ (+2.6,
noise-level) — the current SN-sector credit rides the SH0ES pull
(69.7 sits closer to 73 than 67.4 does); (ii) under a TRGB-calibrated
local anchor the dyad is **0.17σ** from the local measurement and
ΛCDM is 1.7σ — the dyad becomes the model with no tension anywhere on
the sky, its fit advantage reverting to the CMB sector (plik credit),
where it never depended on any ladder. If SH0ES falls, we lose a χ²
subsidy and gain a resolution; if SH0ES stands, P-2026-001 executes
us. Symmetric exposure, on the record.
**Standing language (adopted): the scenario
CONCENTRATES the case — the dyad is a CMB-sector varying-m_e result
with a ladder-independent H₀; the SN sector is calibration-artifact
(retired), small scales null, everything else downstream. And the
"no-tension" property is a CONDITIONAL CONCORDANCE, not a
resolution: the dyad does not dissolve the Hubble tension, it PICKS
THE TRGB SIDE and is concordant iff that wager is right (under
SH0ES at 73.04 ± 1.04 it is 2.3–3.2σ low — a different tension, not
none; the earlier "~4σ" was an inflation, self-corrected). GRADE: **LOOSE-BUT-ANTECEDENT** — the 0.17σ is a
point landing inside a wide anchor (CCHP's ±1.54 sets the whole
test's resolution; any model in ~[67,73] sits within ~1.7σ), so the
smallness of 0.17 earns nothing; what earns is PROVENANCE — 69.70
was θ*-locked and CMB-fixed before any local comparison, with SH0ES
in-stack pulling toward 73 and failing to move it. The meaningful
comparison number is the dyad–ΛCDM separation under the TRGB anchor:
(69.70−67.40)/1.54 = **1.5σ, a mild, real, TRGB-conditional
preference** — a knockout for neither. The dyad's marginalized σ(H₀)
(sampling now) cannot change this grade: TRGB's width dominates any
plausible fold-in.**

> **Pre-registered predictions live in
> `PRTOE_PREREGISTERED_PREDICTIONS.md`** — P-2026-001: the local ladder
> resolves TRGB-side, H₀(local) ∈ [69.0, 71.0] (no hedge; 72+ falsifies
> the H₀ program). P-2026-002: the dark medium cannot decay (shift
> charge; death-condition, shared with stable CDM). P-2026-003: any
> dark-energy drift attributable to the medium is phantom-side with a
> growth-tracking shape, or absent (conditional fingerprint; confirmed
> thawing brackets the completion hierarchy from below). P-2026-004:
> the dyad's 95% upper limit on Σm_ν lands in [0.11, 0.17] eV
> (registered before the posterior run completed; scoring pending —
> §9.5). P-2026-005: the medium rolls-never-oscillates (no
> axion-like PTA/superradiance signals attributable to the dark
> sector; structural, from the kinetic/potential zoo split).
> LIT-2026-001 logs the independent literature convergence on
> varying-m_e (§9.4).

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
 — the flat H₀–ξ ridge (§6) means a Planck+ACT fit will slide toward
 lower ξ (≈0.15) and lower H₀ (≈69), where the Planck-side cost is only
 +11.6 and the ACT penalty largely dissolves. **Honest reading: ACT DR6
 does not kill the model, it compresses the H₀ relief from ~3 km/s/Mpc
 toward ~1.5 km/s/Mpc.** A joint Planck+ACT+SPT refit is the required
 next fit, not optional follow-up. (Setup: `candl` + data at
 `~/candl_data`; script in job scratch `act_spt_test.py`.)
2. **Weak lensing S₈ — substantially settled by the data (2025-26),
 in the dyad's favor.** KiDS-Legacy (complete survey): S₈ = 0.815 ±
 0.019, 0.73σ from Planck; joint KiDS+DES Y3+Pantheon+DESI:
 S₈ = 0.814 ± 0.012. The lensing side came UP — the resolution
 direction requiring no new physics. The dyad's S₈ ≈ 0.826 sits 0.9σ
 from the new WL consensus (ΛCDM's 0.833: 1.6σ) — the model's
 "incidental" easing lands on the concordance point. The S₈-source
 taxonomy (softest-tax ranking): Σm_ν (taxed only by a lensing
 *preference* — mildest; orthodox, no fingerprint), the drift's
 Bianchi withdrawal (native, sign-locked correct, ~10× too small
 alone, and IDENTICAL to P-2026-003's observable (iii) — the model's
 S₈ mechanism and its drift fingerprint are one object), quantum
 pressure (mute — k_J ≥ 5.5/Mpc cuts below the 8 h/Mpc scale), sound
 speed (executed, §5). Note the Σm_ν interaction (§9.5).

4. **Varying electron mass (§9.4, tested 2026-07-06).** The
 epoch-response audit identified recombination *timing* as the one H₀
 lever the damping tail cannot tax (it changes when recombination
 happens, not H at recombination). Measured, θ*-locked, on the joint
 stack: +1 km/s/Mpc per +1% m_e with **ACT indifferent-to-favorable**
 (163.1 vs 164.0 at m_e=1.01 refit) — the executioner moves to plik's
 peak structure, and the cost curve is steep beyond ~1.5%
 (frozen-slice: +7.9 / +58.9 / +289 at 1/2/4%). A fixed-m_e=1.01
 profile refit reached **2801.06 with H₀ = 70.41, ξ = 0.124** — note
 m_e visibly eats ξ's role (the two levers share the r_s budget). The
 >100% refund flags optimization slack in pass-1; a same-companions
 m_e=1.00 control question was settled *analytically* (2026-07-06):
 triangulating both cross-distances between the two optima under a
 quadratic model gave credit −8.5 with a falsifiable midpoint
 prediction (2812.1) that was then measured at 2812.15 — **clean
 credit −8.5 ± 0.5, validated**; the brute-force control was cancelled
 as redundant. S₈ rises with m_e at fixed amplitude (+0.02/1%) — m_e alone
 anti-solves S₈; pairs naturally with Σm_ν (below).

 **Coupling-consistency status — stated so no referee has to ask.**
 What is implemented and fit is the *phenomenological offset*
 (Hart–Chluba instantaneous mode: fixed m_e ratio above z = 50). As
 such it is a bolt-on any ΛCDM extension could wear: if it carries the
 fit, it does so while the unification watches — §4.2's discipline
 applies at +2 parameters. A *sourced* m_e variation requires a
 scalar–electron coupling, which is non-minimal by construction; the
 reason this is not automatically the v1–v3 graveyard is **epoch
 separation** — the lever needs the coupling active only at
 z ≳ 1000, while every killing constraint (EP/MICROSCOPE, atomic
 clocks, Oklo, quasar |Δα/α| ≲ 10⁻⁶) lives at z ≲ 3 — plus a named
 relaxation mechanism (Damour–Polyakov attraction toward vanishing
 coupling) to get from 1% at recombination to ≲10⁻⁶ today
 dynamically. Speculative but structurally native option: gating the
 coupling on ionization, which collapses at recombination — the same
 environmental-switch logic as the (failed) c_EM energy coupling,
 aimed at the rules instead of the conservation floor.

 **The early-time term (the other half of epoch separation).**
 "Active only at z ≳ 1000" is not one epoch — it is *everything before
 recombination, BBN included*, where m_e sets the n↔p weak rates
 (phase space and Q/T), the e± annihilation timing, and EM binding
 corrections. A 1% m_e at recombination is a 1% m_e at BBN, shifting
 Y_p and D/H independently of ξ (ΔY_p ~ 0.1–0.4 × Δm_e/m_e at
 fitting-formula grade — at 1%, comparable to the Aver error bar).
 Note the implemented offset mode *also* carries m_e = 1.01 at BBN but
 does not feed it back into the Y_He table — a small inconsistency to
 book, not just a sourced-version problem. For the sourced version the
 cost is structural: the shift-symmetric, dCDF-native coupling (m_e
 tied to u ≡ X − X₀, which relaxes *for free* because u ∝ a⁻³ dilutes
 into the floor — expansion itself as the least-coupling mechanism)
 ties δm_e to the clustering density Ka⁻³, which **grows into the past
 and is catastrophic at BBN unless it saturates in exactly the
 pre-basin radiation phase** that §2 already flags as the completion's
 early-history falsifier. The m_e-sourcing boundary and the §2
 completion boundary are the same wall — one boundary, not two (cf.
 §11's caustic note).

 **THE DOOR, DUG AND MEASURED (2026-07-06 evening).** All natural
 shift-symmetric couplings of m_e to the medium's state were
 constructed and priced against the three walls (quasar molecular
 absorbers |Δμ/μ| ≲ 10⁻⁷ at z ≲ 2.5; the 1% requirement at
 recombination; BBN):
 - *Linear in x = u/X₀*: relaxes fast (quasar-safe by design) but
 x(rec) = e⁻¹⁴ forces an unnatural g ~ e⁹ and the pre-basin growth
 puts m_e at ~10¹³× standard during BBN. **Dead.**
 - *Logarithmic in ρ (m_e ∝ 1 + g·s)*: natural g ≈ 5×10⁻⁴, survives
 BBN at ~2.9% (Y_p +1.2σ) — and fails the quasar bound by a factor
 of **11,000** (Δm_e/m_e = 1.1×10⁻³ at z=2 vs 10⁻⁷ allowed). The
 log's virtue into the past is its vice at late times. **Dead.**
 - *The shape that survives all three walls*: must rise steeply
 (p ≳ 0.65) below x(rec) and saturate (p ≲ 0.03) above it — a
 bespoke saturation scale at x ≈ e⁻¹⁴ with no natural origin (the
 model's natural scales are x = 1 and x₀). **Epicycle-grade.** The
 least-dead natural variant — saturation at the *equality* scale
 x(z_eq), a physically meaningful threshold — misses the
 recombination requirement by ~10× once BBN caps its amplitude.
 - *Chameleon-type screening* (rescuing quasars by making absorbers
 locally standard): reopens the v1–v3 graveyard. **Not taken.**
 **REOPENED HALFWAY (2026-07-06 night, user-found loophole):** the
 closure above tested *epoch* couplings — m_e tracking the cosmic-mean
 state. A coupling to the *local* medium density is a different
 object: laboratory and quasar-absorber measurements both sit in
 galactic-halo environments (~0.4 GeV/cm³ dark density), so a
 local-state coupling **cancels in exactly the comparison that
 produced the 11,000× exclusion** — the quasar wall constrains
 epoch-coupling only. The recombination-era mean (1,600 GeV/cm³,
 4,000× our halo) gives the right sign for the CMB's m_e = 1.01 with
 a monotonic response. En route, an exact identity: **ρ(basin entry)
 = 2M₂⁴** — the condensate scale *is* the basin-entry density, giving
 a coupling f(ρ/M₂⁴) a natural saturation epoch (z ~ 10⁵). What still
 stands: recombination sits e¹³ below that natural scale, so the
 early-time shape problem (the big-coupling/BBN pincer) survives.
 Door status: **half-open** — late walls evaded by environment
 matching; one wall remains, and it is the same §2 wall as always.
 A separate, weaker-but-legitimate variant is fully untestable by
 variation searches: m_e's *value* set by the medium's constant
 structure (the static Volovik reading — identity rented from a
 time-independent order parameter). Nothing varies; nothing is
 excluded; nothing is predicted. Available as ontology, not physics.
 Verdict (revised): the door is half-open, its remaining wall is the
 §2 wall, and its testable version predicts **environment-dependent
 atomic physics across dark-density gradients** — a channel current
 spectroscopy constrains only weakly (2–3 decades of dark density
 between dwarf cores and cluster cores, largely unprobed for μ/α). Reopening requires
 a mechanism that generates a saturation scale at x ~ x(recombination)
 naturally, or an H₀ mechanism needing only ~0.1% m_e (pointless), or
 screening (graveyard). The honest label survives its own best
 challenge: *phenomenology, carried for its measurement value*.

 **The half-open door's sharpest signature: tunneling (2026-07-06,
 named — not yet derived).** If constants respond to local dark
 density, the most amplified observable anywhere in physics is a
 quantum-tunneling rate: decay rates sit under a Gamow exponential,
 so fractional constant shifts of 10⁻⁸ swing α-decay rates by parts
 in 10³–10⁴ (sensitivities of order 10⁵ are standard in the
 varying-constants literature). Two consequences: (i) *decay rates
 become environment thermometers* — the strongest accessible baseline
 is not a laboratory but **Type Ia supernova light curves**, which
 are ⁵⁶Ni→⁵⁶Co→⁵⁶Fe decay clocks ticking in host environments
 spanning decades of dark density, and Pantheon+ is already in this
 stack; the known SN "mass step" (standardization residuals
 correlating with host mass) is exactly the *shape* such a signature
 would take, though it has mundane astrophysical explanations and no
 claim is made. (ii) The derivation that would promote this from
 named to booked: door coupling magnitude → predicted decline-rate
 contrast vs host dark density → compare against the measured mass
 step's budget. Logged in the Interaction Atlas open list; §11.

 **RECEIPT DERIVED — AND IT COMES OUT FAINT (2026-07-06 night).**
 Normalizing the linear local-state coupling at the recombination-era
 mean (1% at ~1600 GeV/cm³) gives g = 6.3×10⁻⁶ per GeV/cm³:
 laboratory δm_e/m_e = 2.5×10⁻⁶, SN host-to-host contrast
 (0.05–2 GeV/cm³ at SN sites) = 1.2×10⁻⁵ in m_e. Through the
 electron-capture sensitivity (λ_EC ∝ |ψ_e(0)|² ∝ m_e³, so
 dlnλ/dln m_e ≈ 3) the ⁵⁶Co clock contrast is 3.7×10⁻⁵ — about
 4 minutes on the 77-day tail, ~0.04 mmag per decade of flux.
 **The SN mass step (~60 mmag) is ~1500× larger: it is not ours,
 and no current SN dataset can see this signature.** The honest
 reclassification: the tunneling channel is demoted from
 *discriminator* to *consistency check* — the linear door predicts
 (a) zero annual modulation of terrestrial decay rates (the halo is
 smooth along Earth's orbit), consistent with the modern
 high-precision stability nulls that discredited the
 Jenkins–Fischbach claims, and (b) SN decay-clock environmental
 shifts three orders below current photometric precision. The door
 stays half-open precisely because its signatures are this quiet;
 conversely, nothing in decay data can close it. A steeper-than-
 linear coupling would amplify the signature — but steepness is
 exactly what the §2 wall taxes on the early side.

 **Independent convergence (LIT-2026-001, literature sweep
 2026-07-06):** varying-m_e as an H₀ mechanism is now *independently
 preferred at 2–3.6σ by other groups* on Planck(+DESI) stacks
 (arXiv 2606.06495, 2508.09025 among others) — the field converged
 on this lever without the dCDF motivation. This is corroboration of
 the lever, not of the unification: §4.2's discipline is unchanged.
 A null-sound-speed unified fluid indistinguishable from ΛCDM at
 linear order has likewise appeared independently (Kou & Lewis 2026),
 confirming the §4.2 degeneracy from outside.

5. **Σm_ν and c_EM (frozen-slice scans, 2026-07-06).** Σm_ν: on a stack
 with no WL likelihood the best fit is pinned at the 0.06 eV floor
 (+12.2 at 0.12 eV, ACT +5.6 joining plik); its S₈ payoff
 (0.805 at 0.12 eV) is *unpriced* by current data — the lever becomes
 live only if DES shear joins the stack (projected wash, ±2, at
 Σm_ν ≈ 0.10 with S₈ ≈ 0.81).
 **REPRICED IN THE DYAD (2026-07-06 night) — the tax collapsed.**
 The +12.2 figure was measured in the ξ-era configuration; re-running
 the θ*-locked pricing scan at the dyad optimum (m_e = 1.01, ξ = 0)
 gives **+2.8 at Σm_ν = 0.12 eV** (0.20 eV: +29.0) — a 4.4× collapse.
 Mechanism: ξ and Σm_ν competed for the same damping-tail budget;
 executing ξ freed it. The dyad is therefore *structurally compatible
 with the inverted neutrino hierarchy* (⩾ 0.10 eV), which ΛCDM+CMB
 bounds increasingly squeeze — a lab-testable divergence (0νββ
 experiments target exactly this). Registered as **P-2026-004: the
 dyad's marginalized 95% upper limit on Σm_ν lands in [0.11, 0.17]
 eV**. The posterior run (m_ncdm sampled on the full joint stack) is
 in flight; its optimizer phase already landed at m_ncdm = 0.065,
 H₀ = 69.61, χ² = 2801.07 — the profile and the posterior will be
 scored against the registered window when the chains converge, and
 the S₈ side rider is free: Σm_ν = 0.12 eV carries S₈ → 0.807, i.e.
 *toward* the KiDS-Legacy consensus, so the WL data that is absent
 from the stack would pay this lever, not tax it. The environmental-exchange coupling
 c_EM is **dead**: +261 at c_EM = 0.005 (plik +198, ACT +41, S₈→0.869)
 for 0.5 km/s of H₀ — a w-kick on the *dominant* component through
 recombination wrecks the acoustic structure with no clustering
 discount. The environment-coupling idea survives only as
 recombination-rule changes (m_e), not energy-exchange terms.
 ρ_∞(z) drift: upgraded (2026-07-06, post-resurrection) from a null
 constraint to a **conditional fingerprint**. The admissible (δK)²
 operator's fluctuation face funds the floor from *structure
 formation itself* (δρ_floor ~ m̄₂²⟨(δK)²⟩/2, gated by nonlinear
 growth — BBN/CMB-immune at every hierarchy), with the **sign locked
 phantom-side** (m̄₂² > 0 by stability: the floor can only grow) and
 a rigid time-dependence tracking Δ²(k_J, z). Amplitude runs from
 10⁻⁶ (x₀ = e⁻³⁵) to 4×10⁻³ (e⁻⁴³) of critical — the deep end is
 DESI-scale. Consequence: **the hierarchy acquires a second wall** —
 BBN caps x₀ ≤ e⁻³⁵ from above; a confirmed DESI thawing signal
 (w₀ > −1, the current whisper) excludes the deep end and bounds
 x₀ ≳ e⁻⁴⁰ from below. See P-2026-003. **Three riders (adopted):** (i) the
 contribution is drawn from structure's own gravitational energy (Bianchi)
 — an observable funded floor implies an observable *withdrawal*
 (suppressed late growth / ISW / lensing at the sub-percent-to-percent
 level), which must clear existing RSD+S₈ before the deep hierarchy is
 called viable; (ii) the two walls carry unequal confidence — BBN is
 brick, the DESI-thawing lower wall is *chalk* (a contested ~2σ hint
 that may evaporate in DR2/DR3); (iii) the fingerprint's honest size:
 *a genuine scale-locked discriminator that exists only if the
 hierarchy is deep, in a corner the data currently leans away from,
 and even there leaves a growth footprint that must clear RSD first —
 most probably invisible, uniquely ours if seen.* Amplitude AND
 withdrawal to derivation grade ride on the four-verdict calculation
 below (the same nonlinear sector sets both sides of the balance).
3. **BBN: checked at fitting-formula grade (2026-07-06).** With standard
 linearized sensitivities (ΔY_p ≈ 0.0127·ΔN_eff and ∂Y_p/∂ln ω_b ≈
 0.0096, i.e. Y_p ∝ ω_b⁰.039; ∂ln(D/H)/∂ln ω_b ≈
 −1.6, ∂ln(D/H)/∂N_eff ≈ +0.10):
 at the v4 best fit (ω_b = 0.0228, ΔN_eff = 0.403), Y_p ≈ 0.2524 —
 **+1.9σ** vs Aver et al. (0.2449 ± 0.0040) — while D/H ≈ 2.55×10⁻⁵ is
 only +0.8σ vs Cooke et al. (2.527 ± 0.030): higher ω_b and higher
 N_eff pull D/H oppositely and nearly cancel.

 **Self-consistent numbers at the m_e champion (2026-07-06; ω_b =
 0.02284, ξ = 0.124, m_e = 1.01)** — required because m_e = 1.01 above
 z = 50 *includes BBN*, using ∂Y_p/∂ln m_e ≈ +0.17 (honest range
 0.1–0.4) and ∂ln(D/H)/∂ln m_e ≈ +0.4:
 **Y_p ≈ 0.2506 (+1.4σ)** — the refit's ξ collapse (0.403→0.124,
 −0.0035) outweighs m_e's re-spend (+0.0017 central), so helium
 *improves* relative to the v4 point despite the m_e surcharge
 (returns to ~+2.0σ only at the pessimistic sensitivity).
 **D/H ≈ 2.49×10⁻⁵ (−1.3σ)** — the sting relocates: the champion's
 high ω_b lost its ξ compensation, and m_e's +0.4% cannot restore it.
 **The unpriced BBN budget, properly decomposed** (no BBN likelihood
 is in the fit stack): the champion's total charge is ≈ +3.5, but at
 the ξ-only joint champion's own parameters (ω_b = 0.022673, ξ = 0.142,
 m_e = 1) the charge is only **+1.4** (Y_p +1.0σ, D/H −0.6σ) — the
 deuterium sting belongs to the **m_e package**, whose optimizer
 raised ω_b to 0.02284 as part of exploiting the lever. Package
 accounting: m_e's validated CMB credit −8.5 (§9.4) plus its marginal
 BBN charge +2.1 → **net ≈ −6.4**; m_e's *pure* marginal at fixed
 companions is ≈ 0 (its helium cost and deuterium help cancel). The
 joint tie itself carries a mild unpriced +1.4. A loan at ~25%
 interest — favorable, and netted against the controlled number. Adding a BBN likelihood
 (Y_p + D/H as Gaussians) to the joint stack — and feeding varying_me
 back into the Y_He table (a booked code inconsistency, §9.4) — are
 now required for any refit that samples m_e. **Both closed
 (2026-07-06 evening): the dyad config computes Y_He self-consistently
 (YAML-level λ, no C change) and carries the generalized BBN
 prior; the inconsistency priced at the market optimum = 0.66% in raw
 Cls, −0.4 in χ² (ACT −1.5, plik +0.4, SPT +0.7) — sign-favorable,
 absorbed, closed.** PRIMAT-grade
 confirmation remains open (§11). The §2 completion's a⁻⁶ stiff tail /
 pre-basin radiation phase is independently BBN-constrainable (§11).

 **A candidate healer for the deuterium row (2026-07-06, candidate
 grade — coefficients approximate).** The headline's −2.0σ D/H
 residual has one interaction that heals it *with the correct sign
 structure across all three primordial abundances*: a binding-energy
 shift δB_D/B_D ≈ −0.86% at BBN (weaker deuteron → later deuterium
 bottleneck → less D burned into He) heals D/H exactly, improves Y_p,
 and chips lithium in the right direction — using memory-approximate
 Dent–Stern–Wetterich-class sensitivity coefficients. Status honest:
 this is a *candidate*, not a booked result; it awaits (a)
 literature-grade sensitivity coefficients, (b) a coupling
 construction native to the medium (the same shift-symmetric
 discipline as §9.4 — binding energies are QCD/nuclear-scale
 quantities, i.e. this is the strong-sector interaction the atlas
 flags as unwritten), and (c) a check that the healer leaves no new
 deuterium row elsewhere. If all three clear, it becomes P-2026-006. Until
 then the headline deuterium row stands unhealed and the rider stays.

 **UPGRADED TO LITERATURE GRADE (2026-07-06 night; (a) and (c)
 cleared, (b) narrowed to one lever).** The Dent–Stern–Wetterich
 response matrix was pulled from the source (PRD 76, 063513, Tables
 2 and 4): ∂lnY/∂lnB_D for (D, ³He, ⁴He, ⁶Li, ⁷Li) = (−2.8, −2.1,
 +0.68, −6.8, +8.8) in their final treatment; the alternative
 σ ∝ 1/B_D treatment (their Eq. 8) gives D: −1.5, bracketing the
 amendment at **δB_D/B_D ∈ [−1.57%, −0.85%]**. At the central
 coefficients the −0.86% amendment takes D/H from −1.97σ to
 **+0.02σ** (exact heal), Y_p from +1.43σ to **+1.06σ** (improves),
 ⁷Li **−7.6%** (right direction), ³He +1.8% and ⁶Li +5.8% (both far
 inside observational slack). Better: DSW Table 4 gives
 ∂lnB_D/∂ln m̂ = −4 (m̂ = mean light quark mass) while **τ_n and Q_N
 carry zero m̂ response** — so a quark-mass amendment moves the
 binding-energy sector *without touching the n↔p weak rates*: the
 cleanest possible sourcing channel. The m̂-sourced healer needs only
 **δm̂/m̂ = +0.14% to +0.21% at BBN** (f-factor uncertainty spanned:
 healing identical, ⁷Li −7.5% to −8.3%, all side effects safe). This
 is the strong-sector rules amendment, the direct analogue of the
 dyad's m_e = 1.01 in the EM sector, an order of magnitude smaller.
 What remains open is only (b): the medium-native coupling
 construction (why m̂ responds to the substrate, with the same §2
 early-shape wall as m_e). Registered as **P-2026-006 (conditional
 fingerprint)**: if the deuterium row is healed by a substrate
 amendment, it is a quark-mass amendment of +0.14–0.21% at BBN,
 carrying a mandatory correlated signature — ⁷Li *reduced* by
 7–13% and Y_p *reduced* by ~0.5% relative to the unamended dyad. An
 amended model that heals D while raising ⁷Li or Y_p is excluded.

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
delta_cb/θ_cb snapshot (cb quantities are baryon+CDM only by contract —
guard comment in code). `use_dcdf = yes` replaces CDM (floored at
`Omega0_cdm_min_synchronous` = 10⁻¹⁰ because synchronous gauge is defined in
the CDM rest frame) and disables the λ/fld/scf budget auto-fill chain.

Fixed symmetrically in dCDF and the ΛCDM twin: one massive neutrino
m_ncdm = 0.06 eV, T_cmb, N_ur base. ΛCDM samples 7 parameters
(ω_b, ω_cdm, H₀, logA, n_s, z_reio, A_planck); dCDF samples 8
(ρ_∞ replaces ω_cdm; +ξ_Neff).

6. **The five-lever paper audit (2026-07-06; zero CPU).** Applying the
 three-laws screen + the damping-tax test + shift-symmetry structure
 to every remaining candidate coupling: **PBHs** — no expansion role
 possible (the coupling is identity-blind; w = 0 is w = 0); their says
 live in texture, thermal history, seeding, and GW catalogs.
 **Varying G** — an energy lever in rules clothing (raises H at
 recombination) → dies by the ξ gallows. **ν self-interactions** —
 the free-streaming phase shift is now measured present (ACT DR6);
 dead. **Dark phase transition → PTA waves** — shift-symmetric P(X)
 has no potential, hence no latent heat; basin entry is a smooth
 crossover; no signal in this class. **Varying α** — alive but
 predicted inferior to m_e (Thomson surtax σ_T ∝ α²/m_e²); queued as
 the rules-class control scan. Four executions and one demotion at
 the speed of algebra: the screening theory works.
 **α CONTROL SCAN RUN (2026-07-07 night) — THE DEGENERACY BREAK
 Sign convention, pinned: positive
 = χ² PENALTY = worse fit.** θ*-locked pricing, full joint stack,
 H₀ relocked per point; α = 1.0 baseline reproduces the dyad's own
 numbers (plik 586.5). Exact component totals (full reconciliation
 in chains/α_scan_*.1.txt): α = +0.5% buys H₀ = 70.65 at
 **+92.36 total penalty** (plik +55.07, ACT +22.56, SPT +17.44,
 lensing +4.35, BAO +1.16, SN −7.83, lowl −0.38); α = +1% buys
 71.69 at **+432.76** (plik +200.5, ACT +167.3, SPT +62.2). The
 penalties scale quadratically (ratio 4.7 ≈ 2²), as χ² near a
 forbidden direction should. Contrast m_e = +1%: −8.5 (a CREDIT).
 **The result is a hard degeneracy break, not a ranking: the two
 nearest-degenerate recombination knobs (binding ~ m_e α², Thomson
 ~ α²/m_e²) are resolved by the damping tail onto OPPOSITE sides —
 α actively forbidden (~20σ at 1%), m_e actively preferred.**
 Reach, bounded (adopted): this retires the
 freedom-artifact charge for the NEAREST sibling only — of the
 knob family, N_eff was already executed by the joint refit
 (ξ → 0.01, the dyad's origin), α is now broken, a bare z_rec
 shift is the m_e lever's own phenomenological definition; free-Y_p
 and EDE-class members remain unexcluded. And data-selected lever
 ≠ confirmed mechanism: this makes the amendment non-arbitrary in
 its knob, not derived in its origin. Robustness up; evidence
 class unchanged.
 **THE FAMILY CENSUS COMPLETED (same night; expectations pinned in
 the scan header pre-launch; positive = penalty).** Free Y_p:
 PINNED — penalized both directions (−5.6%: +9.4, ACT alone liking
 it −3.5 but overruled; +5.2%: +38.1, ACT +30). Curvature:
 FORBIDDEN both ways (Ω_k = −0.005: +30.4 with H₀ dragged to 68.3;
 +0.005: +44.6 — plik +46.6 even while buying H₀ = 71.05). Running:
 FLAT (α_s = +0.01: −0.5 ≈ noise, and it buys zero H₀ — θ* blind;
 −0.01: +15.7). All pinned expectations met or exceeded in the
 no-credit direction. **Final standings: N_eff executed, α
 forbidden (+433), Y_p pinned, Ω_k forbidden, running flat — the
 m_e credit (−8.5) is the UNIQUE credit-bearer of the entire
 in-code knob family. The freedom-artifact charge survives only as
 the out-of-family EDE-class, which requires physics the code does
 not contain and was therefore never "a knob we grabbed."**

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
 satisfied).
 **Addendum (2026-07-07, scaling grade — the throat de-condensation):**
 the supersolid conjecture was scored and killed on both routes
 (no roton — ideal condensate; no vortex lattice — the ultralight
 circulation quantum is unpayable: a stellar hole mints 1×10⁻¹⁰ vortex
 quanta, M87* mints 0.12, vs ~2000 threading a galaxy), and the
 derivation found the opposite: every BH sits inside ONE coherence
 patch (l_dB(v→c) ≈ 0.02 pc ≫ any horizon — kernel 2.2's regime
 boundary), and accretion drives u ~ X₀ by r ~ r_s, pushing the
 medium OUT of the basin: the superfluid DE-CONDENSES in the throat,
 locally reverting to its pre-basin normal phase (w = 1/3, its own
 excitation gas) — the one place in the late universe where the
 medium's early phase persists. **UPGRADED TO SOLVED (2026-07-07 evening, stationary spherical
 flow):** the critical-flow ODE closes exactly. In the X₀-free
 variables the transonic conditions solve rationally — sonic point
 at **r_c = 3 r_s (the ISCO)** with y_c = 1/3 and critical flux
 Ã = 1; the supersonic branch crosses the basin boundary (y = 1) at
 **r_exit = 1.8393 r_s** (the real root of r³ = r² + r + 1 — the
 tribonacci constant), and X̃ grows without bound approaching the
 horizon; the subsonic branch pins y(horizon) = 1 identically. The
 de-condensation surface is exact: the medium exits its basin at
 1.84 r_s around any Schwarzschild hole. (Normal-carried couplings
 — vev package — locally reactivate inside that surface, negligible
 observables at these volumes.) The old "recycling furnace"
 ideation acquires its mechanism-grade form: holes locally undo the
 condensation, now with the surface computed.
 **Addendum 2 (2026-07-07 night) — the universal horizon, located:**
 on the same exact flow, the khronon foliation's overlap with the
 Killing time is (u·χ) = 1/√X̃ exactly (ξ = t + ψ(r)); the transonic
 branch has y·f → 1 as f → 0 (verified numerically to 1×10⁻⁴), i.e.
 X̃ = 1/f at the horizon, so **(u·χ) = √f: zero AT r_s and positive
 everywhere outside — the medium's universal horizon DEGENERATES onto
 the metric horizon in the probe limit.** No interior trapped region
 for the khronon (contrast khronometric gravity, where backreacting
 khronons hide universal horizons inside r_s — ours is minimally
 coupled, so the foliation is a test structure and GR's horizon
 remains the only one). Consequences: the global time-order (C1e's
 chronology protection) extends regularly to every r > r_s;
 arbitrarily-fast dispersive medium modes can escape from any point
 outside the horizon; landmarks on the flow: (u·χ) = 0.866 at the
 sonic point (ISCO), 0.707 exactly at the basin exit (1.839 r_s). Black holes: shift symmetry supports no-hair conclusions
 (quasi-static accretion at CDM-negligible local density); note the
 Hui–Nicolis theorem is usually stated for Galileon-type/derivatively
 coupled shift-symmetric scalars — its clean applicability to bare P(X)
 should be cite-checked, though the k-essence-accretion literature reaches
 the same conclusion independently. The model's compact-object prediction
 is deliberately boring: identical to ΛCDM.

## 11. Open items

- **Joint Planck+ACT DR6+SPT-3G refit: DONE (2026-07-06)** — landed on
 the predicted ridge point (H₀ = 69.05, ξ = 0.142), then superseded
 same-day by the dyad (ξ executed, m_e = 1.01, H₀ = 69.70; §1
 headline). What remains open from this item: the refit ΛCDM+BBN twin
 must complete to convert the headline's −6.5..−8.5 *band* into a
 single honest number (twin paused for CPU, resumes after the Σm_ν
 run).
- **Evidence numbers**: the PolyChord pair on the *dyad-era* configs
 (`dcdf_pc_v2.yaml` / `lcdm_pc_v2.yaml`, nlive 500, weeks-scale) is
 the live evidence instrument; the pre-dyad forecast layers in §8
 apply. That decides whether the χ² gain is a detection or a
 flexible-model tax.
- **Σm_ν posterior scoring (P-2026-004)** — the full-stack sampled run
 is in flight (optimizer already at m_ncdm = 0.065, χ² = 2801.07);
 on convergence: extract the 95% upper limit, score against the
 registered [0.11, 0.17] eV window, and run the matched ΛCDM+Σm_ν
 control on the identical stack.
- **Binding-sector coefficients (the deuterium row-healer's admission ticket,
 §9.3)** — replace memory-approximate B_D sensitivities with
 literature-grade ones (Dent–Stern–Wetterich 2007 class), construct
 the coupling, audit for new deuterium rows; on success, register P-2026-006.
- **The tunneling signature (§9.4)** — derive the local-state door's
 coupling magnitude → predicted decay-rate contrast across host
 dark-density environments → compare to the SN Ia mass-step budget.
 Promotes the atlas open-list entry or kills it.
- **The force-by-force gap** — the environment program (Transaction
 Atlas preamble) has EM levers booked (m_e, α) but no derived
 substrate coupling for the strong or weak sectors (Λ_QCD, G_F);
 the §9.3 healer is the natural strong-sector entry point.
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
- **THE FOUR-VERDICT CALCULATION** (the program's center of mass): the
 nonlinear two-fluid sector, one derivation reading off (i) the
 soliton core-mass slope vs Schive (fingerprint or FDM-by-another-
 route), (ii) the granule heating rate vs the ultra-faint-dwarf knife,
 (iii) the granule spectrum reshaping by the normal component, and
 (iv) the structure-funded floor amplitude (P-2026-003's condition).
 Lyman-α transfers unconditionally as the backdrop.
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

## 13. The interaction architecture across scales (2026-07-06 exploration)

A mathematical audit of the three-laws pattern (§9.5-adjacent; gravity
the only universal coupling / the background is adiabatic / rules
amendable, conservation laws not) against the atomic-scale vacuum-interaction
catalogue, plus ontology tests for the floor. Everything below is
paper-grade with the arithmetic stated; no CPU consumed.

**The program statement (2026-07-06), and where its accounting lives.**
Every booked equation in this document decomposes as *contents +
environment*: a standard-physics term plus a substrate term (the
dyad's m_e amendment, the fluid's w(x), the candidate δB_D, the funded
floor's structure gate are all instances). The systematic completion of
the environment side — every derived fixed relation, and only derived
ones — is maintained in **`PRTOE_INTERACTION_ATLAS.md`**: four exact
identities (among them ρ(basin entry) = 2M₂⁴ and total energy ≡ 0),
four structural theorems, three one-parameter-many-observables
coherences, an open list (named-not-derived: the tunneling
thermometer, the binding coefficients, the strong/weak gap), and the
walls. One wall is load-bearing for the program's scope and is stated
here precisely, because its precise form matters: **Bell's theorem
does not forbid an interaction account of entanglement — it constrains it.**
The theorem (mathematics, loophole-free experimentally confirmed 2015)
excludes only maps that are simultaneously *local, deterministic-
classical, and measurement-independent*. An interaction map that gives
up exactly one of those premises is untouched. The four available exits:
(i) nonlocal interactions (Bohmian class); (ii) environment-correlated
measurement settings — note that a universal substrate every apparatus
couples to is structurally the *only* kind of object that could
implement this premise honestly; (iii) retrocausal interactions — the
**transactional interpretation of QM (J. Cramer 1986)** already models
every quantum event as an offer/confirmation handshake completing
across the light cone, i.e. entanglement *as a transaction*, published
four decades ago and fully Bell-compatible; (iv) a quantized substrate
(then the map is QM and Bell is satisfied by membership). What this
document's classical fluid cannot do is produce Bell violations while
staying in all three premises at once — no map can, ours included.
Tunneling *rates* are in scope now (§9.4); the entanglement question is
open pending which cost the model's quantum extension elects to pay.

### Correspondences & conjectures (relabeled:
"confirmed" is reserved for certificate-grade results — all-orders
proofs, bounded leakages, stamped caveats. What follows is true-and-
structural but analogy-grade, except where a cross-check is noted.)

**C1 — The three laws are scale-representations of gauge structure +
unitarity.** Law 1's identity-blindness (the medium's coupling reads only w)
is the equivalence principle; its atomic twin (the QED vacuum reads only
charge and mass — Lamb shift and g−2 are identical for any particle of
equal q, m) is charge universality. Both are consequences of locality +
gauge symmetry: *each conserved charge couples through a gauge field*. Law 2's adiabatic
background is S-matrix unitarity one floor down: virtual
processes are exactly reversible; entropy generation is delegated to
real (on-shell) emission — the same architecture as cosmic entropy
being delegated to stars and holes while the sector's conserved quantities stay
clean. Law 3's rules-amendments have a standard-physics precedent: the
vacuum already runs α with probe scale (β = 2α²/3π). The laws are one
architecture expressed at two scales, with the Unruh/Gibbons-Hawking
pair (T = a/2π ↔ T = H/2π — the *same formula*) as the bridge.

**C1a — Every gauge field is a coupling channel; the field is the source,
not the flux (analogy-grade,
calibration-supported).** C1's "each conserved charge couples through a gauge field" runs
both directions: EM is the charged sector's channel exactly as gravity
is the energy sector's. The sharpening: **Gauss's law makes the field
the RECORD OF THE SOURCE, not the flux** — a charge's flux at
infinity cannot be erased, only transferred (evidence: charge
conservation, electron lifetime > 6.6×10²⁸ yr), and the Aharonov–Bohm
effect shows the potential is physically real even
in field-free regions. The source is present even where no
flux flows — measured. The classification this buys: ABELIAN
channels (EM) carry no charge of their own — photons are
uncharged, sources are long-range and additive; NON-ABELIAN ones (color,
weak) couple to themselves — gluons carry color, and a field that
carries its own charge confines; GRAVITY is the extreme case — the
field's own energy gravitates, which is (i) why it is the
UNIVERSAL channel (every other sector has a gravitational coupling), and
(ii) why the funded floor's Bianchi withdrawal (V4) exists at all:
structure's gravitational energy can be tapped because the
field itself carries energy. Model consistency note: the medium is
uncharged — it has no EM charge — so the charged sector
never sees it; every α null is structural for this model (cf. R1:
masses only, α untouched).

**C1b — The conserved-charge inventory — what
other charges must be accounted for? (analogy-grade, evidence quoted).**
Sorting every conserved quantity by whether its charge has a gauge FIELD:

| charge | gauge field | status | evidence |
|---|---|---|---|
| energy-momentum | gravity | self-sourced (its energy gravitates) | everything |
| electric charge | photon | sourced (Gauss law) | e⁻ τ > 6.6×10²⁸ yr |
| color | gluons | sourced + field carries its own charge | confinement: no free color ever seen |
| weak isospin | W/Z | finite-range — massive field (Higgs) | short range; acts within a Compton wavelength |
| baryon number B | **NONE** | unsourced (no gauge field) | proton τ > 2.4×10³⁴ yr — holding so far |
| lepton number L | **NONE** | unsourced (no gauge field) | 0νββ searches — LIVE |
| B−L | none, but anomaly-free | the SM's one exact global charge | the natural candidate to be secretly gauged |
| shift charge (the medium) | the condensate's own U(1) | the model's added charge | P-2026-002's decay ban; vortex/flux quantization |

Three structural consequences: (i) B+L is already anomalously violated
(sphalerons) — the SM itself defaults on that combination at high
temperature; B−L is its one exact global charge. (ii) The quantum-gravity
folklore ("no global symmetries") is, in this language, a single
sentence: **unsourced global charges cannot survive — every exact charge must
have a gauge field.** Its testable fork: either the proton eventually decays
(B violated) or B−L is secretly gauged (a Z′ exists). (iii) The
cosmic baryon asymmetry η ≈ 6×10⁻¹⁰ is the universe's outstanding net
imbalance with no visible counterpart; the Sakharov conditions are the
rules for creating one (a violation mechanism, biased
dynamics, and departure from equilibrium).

**The Fairbank connection, explicit:** neutrinoless double-β decay
— nEXO's target — is precisely the experiment that tests whether
LEPTON NUMBER is a sourced charge or an unprotected global symmetry. A 0νββ
detection = L is violated (Majorana neutrinos are the mechanism)
= the no-global-symmetries principle in action. The dyad's Σm_ν
posterior (P-2026-004, computing) and the inverted-hierarchy window it
may reopen are the mass-scale side of the same question. The program's
top-priority deliverable and its charge architecture meet in one
experiment.

**C1c — Time in the accounting (correspondence-grade with one load-bearing technical identification).**
Three-way split: (i) THE ARROW is the recording direction — virtual processes are
time-symmetric (microscopic reversibility), recorded events accumulate
irreversibly (C4a); past = recorded, future = open, "now" = the recording
front. The arrow requires MATTER to hold the records: a superfluid
alone never records — the arrow is emergent from medium+matter, as
proposed. (ii) THE CLOCK: the condensate has φ̇₀ ≠ 0 — it is a
KHRONON, and the constant-φ foliation it defines is the very slicing
the (δK)² operator already runs on: "time from the superfluid" is not
an addition to this model but a description of machinery already
load-bearing in it. Lab precedent for medium-supplied clocks: time
crystals (realized 2017+). (iii) THE CORRECTION: time is not a third
gateway — it is the SYMMETRY underwriting the first one
(time-translation → gravity → energy: symmetry, bank, debt), closing
C4b's loop: reading a clock = counting accumulated phase (E = ħω) on
energy sources. WALL, stamped: why the universe opened nearly blank (the
past hypothesis / low-entropy start) is underived here as everywhere.

**C1d — Did time start? (interpretive grade, one lab confirmation, EFT wall stamped).** The dichotomy "time began
with the first medium-matter interaction OR everything has always
been" is well-posed but both horns commit a grammar trap (start/always
are clock-words used where no clock exists). Resolved structure:
(i) tenseless option (b) IS the mainstream quantum-gravity picture —
Wheeler–DeWitt: the universe's total state carries NO time parameter;
time is a relational readout inside it (Page–Wootters), demonstrated
on a bench (Moreva et al. 2013: one photon as clock, the other
evolves relative to it, the whole static). (ii) A third option the
dichotomy misses: no-boundary (Hartle–Hawking) — the past is finite
but edgeless (time rounds into space; South Pole, not wall).
(iii) The accounting split, carried over from C1c: the CLOCK (khronon
tick) exists as far back as the medium; the ARROW (recording) waits for
matter — time-order predates time's direction. (iv) WALL: the medium's
own opening lies beyond the EFT cutoff — the model cannot compute its
first page; and the standing cyclic-universe conjecture is option
(b)'s physical form (CCC-class), which would also address the
blank-start wall. Parked, labeled, no claim.

**C1e — Forward-only time travel (correct on direction, mechanism priced, one correction; confirmations routine).** Forward dilation is measured physics (GPS ~38 μs/day;
Hafele–Keating 1971; Kelly twins). The grow-your-own-mass
mechanism works in principle (56 M⊕ in 1 m = 29% slowdown; serious
fast-forward requires hovering near one's own horizon; the physics
permits it — energy must merely balance, ~1×10⁴³ J borrowed and repaid)
but is dominated by velocity or existing wells. Correction:
de-dilation lands in the then-current now — a held fast-forward
button, not a timestamp dial. THE MODEL-SPECIFIC RESULT: backward
travel is doubly and STRUCTURALLY excluded here, more strongly than
in bare GR (which permits Gödel/wormhole CTCs and leans on Hawking's
chronology-protection conjecture): (i) the khronon foliation assigns
every event one reading of the universal clock — no geometry loops
behind itself; (ii) the arrow runs one way — backward travel =
un-recording (C4a). In this model chronology protection is not a
conjecture; it is the medium's clock plus the arrow's definition.

**C1f — The emergence census — what else is emergent?
(calibration-grade, one load-bearing frame).**
Confirmed emergent in ACCEPTED physics: ~99% of ordinary mass (the
QCD vacuum is a condensate; the proton's 938 MeV is condensate
binding — quark Yukawa masses total ~9 MeV; lattice QCD computes it
to percent grade), relativistic light cones (graphene's emergent
c/300 Dirac structure), U(1) gauge fields + monopoles (spin ice,
2009), the Higgs mechanism itself (Anderson found it in
superconductors first), temperature/arrow/quasiparticle identity.
This model's own list: the clock (khronon) and arrow (C1c), the
ripple-particle M_eff = M₂²/m̄₂ (emergent identity), effective
metrics for excitations (analog horizons), chronology protection,
the floor (Λ as ground-state property), and — the live bet — the
constants themselves (the m_e/m̂ amendment program IS
constants-as-emergent). Deliberately NOT emergent here: GR's
dynamics and the photon (minimal coupling — the reason the model
survives GW170817 and the fifth-force graveyard). THE LOAD-BEARING
FRAME: the QCD condensate is mainstream physics' existence proof
that vacuum condensates set matter's parameters — 99% of every
laboratory's mass is condensate-emergent already. This model
proposes one more instance of an accepted kind, reading into the
Yukawa 1% at the 10⁻² level in one epoch — the conservative framing
for any expert audience.

**C2 — The 'what conserves?' question resolves: the invariant is action,
not energy.** Under expansion, each field mode's adiabatic invariant
E/ω — its occupation number, in units of ℏ — is *exactly conserved*;
only the unit (ω) redshifts. The radiation era's "losses to
expansion" are, in action units, no losses at all: nothing leaves any
mode; the unit (ω) redshifts. GR's refusal to define global
energy and the perfect adiabatic invariance of quantum numbers are two
statements of one fact: **the conserved quantity was never energy.
In units of ℏ the count is exactly conserved, always.** (This
retires the "what conserves?" question: there
is no missing energy; there is a redshifting unit and a conserved count.)

**C3 — The two-fluid correspondence.** The dyad's medium with the
(δK)² term has dispersion ω = k²/2M_eff with c_s = 0 — the Bogoliubov
spectrum of an *ideal* (non-self-interacting) Bose condensate, healing
length → ∞. The completion's phase structure then maps onto Landau's
two-fluid model: pre-basin radiation-like phase ↔ normal component;
post-basin floor ↔ condensate fraction; **basin entry (z ~ 10⁵) ↔ the
medium's condensation epoch**. Dark matter and dark energy as the
normal and superfluid fractions of one substance — the trampoline
metaphor's laboratory-physics name. Lab superfluids (helium kept liquid
at T=0 by zero-point energy) are structural cousins of the floor
(the medium kept at ρ_∞ by its condensate nature).

**C3a — Smooth, not foamy (stance-grade,
evidence quoted, reach-wall stamped).** Against Wheeler's quantum foam
(a 1955 picture, not a derivation), the model bets sub-Planck
smoothness. Status: (i) DATA CURRENTLY SIDES WITH SMOOTH — GRB 090510
(Fermi 2009): energy-dependent photon dispersion excluded beyond the
Planck scale at linear order; distant quasar images stay sharp where
foam variants predict blur; the Holometer heard nothing. Quadratic
foam survives only because it is much harder to test. (ii) THE
STRUCTURAL POINT: quantum ≠ boiling — coherent states are quantum and
phase-smooth (the laser calibration), and a CONDENSATE is emergent
calm: below the healing length the order parameter is smooth,
roughness lives in excitations that vanish as they settle. The
condensate paradigm (Volovik school; our C3) predicts the deep UV
gets MORE ordered descending — possibly discrete at bottom, but
coherent: atoms in a superfluid, not bubbles in a boil. Wheeler
conflates quantum with turbulent; this model's ansatz splits them on
the condensate side. (iii) THE SMOOTHNESS ARGUMENT: the vacuum may carry
VIRTUAL texture — that is what vacuum fluctuations are (Casimir, Lamb) — but
never REAL texture: real texture would appear in the energy density
(clean to 121 decimal places — X1's own number) and in the photon
travel times (clean past Planck at linear order). Foam-as-virtual:
real, averages to nothing. Foam-as-real: forbidden and observed absent.
The ground state is smooth because texture is excitation energy
and the ground state has none by definition.
Hedge kept: an argument, not a theorem — cancellations could hide
posted grime behind a clean net (the unsolved half of the Λ problem).
(iv) WALL: this EFT's domain ends at ~20 nm (M₂) — sixty orders above
Planck; the bet is booked as paradigm-aligned stance with
observational confirmations, not a result.

**C4 — Entanglement as the signature of a conserved pair-creation
(2026-07-06 night; analogy-grade, cost elected).** The Bell cost's
model-native exit is (iv), quantize the substrate — and the resulting
picture is lab-precedented, not invented: a condensate has
off-diagonal long-range order (one macroscopic wavefunction, one
global phase — "the medium carries the message as itself"), and real
laboratory condensates pay out their excitations in *entangled pairs*
(two-mode squeezing; measured — entangled phonon pairs 2012, analog-
Hawking pair entanglement across sonic horizons, Steinhauer 2016+),
via exactly the Bogoliubov machinery C3 already maps. The
statement: **why** — conservation forbids solitary creation from
the condensate, so excitations are born in anti-correlated pairs;
entanglement is the two halves of one conserved event. **How** — both
excitations are amplitudes on one global phase, so the correlation is
carried by the medium as itself, with local decoherence and no
signaling. What is NOT claimed: that this reproduces full Bell
violation for arbitrary measurement settings — a classical shared
message caps at CHSH = 2, nature delivers ~2.7, and reaching
Tsirelson's bound (2√2) is the quantitative bar the substrate's
quantum phase sector must hit by derivation. Until that derivation
exists, C4 is a correspondence with laboratory support, not a result.

**C4 DERIVED AND TESTED (2026-07-06 night; conditional on
quantization).** The CHSH value of the medium's pair states was
computed from scratch: for the two-mode squeezed state that pair
creation produces, the pseudospin correlator (Chen–Pan–Hou–Zhang, PRL
88, 040406 (2002) — cite-checked) evaluates analytically to
E(θ_a, θ_b) = cosθ_a cosθ_b + tanh(2r)·sinθ_a sinθ_b, giving
**B(r) = 2√(1 + tanh²2r)** — above the classical cap 2 for *any*
nonzero squeezing, saturating Tsirelson's 2√2 as r → ∞. Known-answer
test: the correlator was recomputed numerically in a 4000-state Fock
basis with no formula input; numeric and closed form agree to
machine precision (rel. diff ≤ 4×10⁻¹⁶ at r = 0.5, 1, 2). And the
squeezing is not a free knob: expansion pair-creation IS a two-mode
squeezer (Grishchuk–Sidorov), with r growing linearly in e-folds
outside the horizon — at r = 5 the Tsirelson deficit is already
6×10⁻⁹. So the conditional statement is now exact: **if the substrate
is quantized, its own expansion history mass-produces maximally
Bell-violating pairs.** What remains conditional is the "if" (the
phase sector's quantization is asserted, not derived) and the audit
caveat (Gaussian/quadrature measurements see a positive Wigner
function and no violation — the signature requires a parity-grade
measurement).

**Calibration — known-answer tests of the interaction
accounting itself (2026-07-06 night; job scratch
`derivation_battery.py`).** Two systems where the interaction language
must reproduce measured numbers or be abandoned: (i) *the hydrogen
atom built from scratch as a variational equilibrium* — localization
energy ħ²/2mr² against Coulomb energy −e²/4πε₀r; the
equilibrium point lands on the Bohr radius to 2.6×10⁻⁶ and on
E_1s = −13.6057 eV to 1.2×10⁻⁹ (the dyad's +1% m_e amendment reprices
it to 13.742 eV and moves z_rec by exactly the +1% CLASS integrates —
one arithmetic, laboratory to last-scattering). (ii) *The laser as
photon condensate* — above threshold a laser is a macroscopically
occupied mode with one global phase (the laboratory's cousin of the
floor; threshold is a condensation transition, Haken's classic
mapping). The derivation — every stimulated
emission copies the phase exactly; every spontaneous
emission adds one quantum of random phase, diluted by the n̄
resident quanta — reproduces the **Schawlow–Townes quantum linewidth
exactly** (ratio 1.000 against the textbook formula; ~1 mHz for a
HeNe benchmark, the known answer). The fundamental noise floor of
every laser on Earth is, in this language, the stream of
spontaneous emissions — and the accounting gets its number right
to the last decimal.

**C4a — Measurement as decoherence (correspondence-grade, evidence quoted, wall stamped).** Superposition
= UNRESOLVED amplitudes: reversible contributions that can still cancel —
which is what interference is (the double slit's paths are unresolved
amplitudes). Measurement = DECOHERENCE: the event records irreversibly to
the environment — C1's own architecture (virtual/reversible vs
real/dissipative) at the single-event level; decoherence is the
reversible-to-recorded transition. THE CORRECTION THAT MAKES IT PHYSICS: what
matters is the RECORD, not the viewing — which-path detectors
kill interference unread (an unread record still decoheres), and the quantum
ERASER un-records coherently and interference returns (an
apparently-decohered process re-coheres if the record never became
permanent). Decoherence has a measured RATE (decoherence times; watched
in real time in cavity QED — Haroche 2012; ~1×10⁻³¹ s for a dust grain,
which is why the macroscopic world is always definite). THE WALL, stamped:
this language does not pick the outcome and does not derive the Born
rule — the rule (probability = |amplitude|²) is
the unsolved measurement problem for every interpretation, ours
included. Filed at C4's edge: same boundary, same honesty.

**C4b — Energy's three roles in the outcome (correspondence-grade).** The proposal "the outcome
with enough energy is preferred" FAILS as an
outcome rule — falsified directly (asymmetric superpositions: the
higher-energy outcome can carry 2% against 98%; probability is
|amplitude|², energy-blind, to interferometric precision) — but
decomposes into three roles that are each correct: (i) **energy
writes the menu** — conservation gates the offer set exactly;
unaffordable outcomes have amplitude zero (thresholds, lines, Gamow);
(ii) **the dominant coupling picks the basis** — this is
einselection (Zurek), the accepted answer to the preferred-basis
problem: the strongest system-environment channel chooses the
LANGUAGE the outcome is recorded in, never its value — the precise
true form of "the dominant coupling sets the basis"; (iii) **energy
is the phase-accrual rate of unresolved amplitudes** — E = ħω is the phase-
accrual rate; evidence: every atomic clock (Cs:
9.19 GHz = E/h read off a two-level system), and COW 1975
(gravitational energy difference between interferometer arms appears
exactly as interference phase). The Born-rule wall (C4a) stands: what
sets the probabilities remains underived, here as everywhere.

**C4c — Conservation is the on-shell condition, not the selection
rule (correspondence-grade, the sharpest landing of the series).** "The chosen outcome conserves
exactly" cannot select among quantum
alternatives — every option already conserves exactly (BKS statistical
conservation killed by Bothe–Geiger 1925: conservation is exact in
each INDIVIDUAL event). But it is precisely the REAL/VIRTUAL
boundary: virtual processes may run off-shell within the one
uncertainty rule (Δt ~ ħ/ΔE — β decay borrows an 80 GeV W, ~1×10⁵× the
available energy, for ~8×10⁻²⁷ s); BECOMING REAL requires exact conservation —
the on-shell condition E² = p² + m² is that sentence
made exact. Every particle ever detected was on-shell; the
off-shell ones exist only inside virtual processes. And the "most logical
choice" clause is the classical limit: paths surviving the
sum-over-histories are those where neighbors agree on accrued phase —
stationary action (δS = 0) as the classical shortcut;
Newton emerges where the sum collapses to one path. The
picture assembled (C4a–C4c): virtual processes off-shell within ħ/ΔE;
becoming real requires conservation; among conserving outcomes amplitudes set the odds
(Born — the wall); the dominant coupling picks the basis.

**C4d — The neighbor rule (exact, no decomposition needed — the golden rule assembled).** "The medium
forbids conserving processes blocked by an occupied final state" is
quantum statistics in transition rates, exactly: every fermionic
final state contributes a VETO factor (1−f) — occupied neighbor ⇒
amplitude zero (evidence: free neutron τ ≈ 880 s vs bound-neutron
immortality in stable nuclei — nuclear stability IS the neighbor
rule; neutron stars = star-sized vetoes by the electron Fermi sea;
the Chandrasekhar calibration = the veto as stellar structure). Every
bosonic final state contributes an INVITATION factor (1+n) —
stimulated emission (the laser calibration above threshold), BEC
(the medium's own floor exists by the friendly half of this rule).
And a final state with no available mode vetoes outright: Purcell
suppression/photonic bandgaps — inhibited spontaneous emission,
measured (O3's thread, named). Assembly: with C4b (menu + phases) and
C4c (on-shell clearance), these clauses reconstruct
FERMI'S GOLDEN RULE one by one — rate = (2π/ħ)·|amplitude|² ·
(density of final states) · (occupancy factors) — probability (Born,
the wall) × available states × occupancy. This language has
now re-derived the master transition-rate law of quantum mechanics
from these axioms.

**C4e — The Born clause: the crack and the road (route-map grade, no result claimed).** The wall decomposes. THE CRACK
(proven): Gleason 1957 — given the Hilbert-space structure, |amplitude|²
is the UNIQUE consistent probability; "why these odds" is answered
(forced); what remains is "why this Hilbert-space geometry." THE ROAD
(published, runs through the superfluid): Madelung — in hydrodynamic
form |ψ|² IS the medium's density, so Born reads "outcomes land where
the substrate's excitation lives"; Valentini's subquantum H-theorem —
arbitrary initial odds RELAX dynamically to |ψ|² (numerically
confirmed), making Born an EQUILIBRIUM of the medium, not an axiom;
rider: early-decoupled sectors could retain quantum NON-equilibrium
(odds ≠ |ψ|²), and a gravity-only condensate is the natural relic
candidate — speculative, named, parked. COSTS, stamped: this road
takes Bell's exit through the NONLOCAL door while C4 elected
quantize-the-substrate — mixing exits owes care; and nothing here
enters the evidence class. CONVERGENCE NOTE: the ingredients of a
medium-specific Born-equilibrium argument (excitation-density
statistics + quantized phase sector) are the same objects V3 and C4's
condition already owe — the five-verdict machinery and the Born
question share parts. One calculation, now with a second prize
behind it.

**C4f — Stability as an exhausted decay channel (correspondence-grade).** The stability law
("everything conserves, netting zero; unstable atoms have a pending
decay") refined to exactness: conservation NEVER
fails (per-event conservation, C4c) — an unstable state is not in
violation but holds an UNEXECUTED FAVORABLE DECAY: stable = conserving
AND no decay available (ground state); unstable = conserving
with a decay pending, half-life = the golden rule's
rate (C4b-d). The "grime" is the decay products hitting
third parties: radiation damage = the decay's byproducts
(dosimetry as its accounting; the medicine cluster).
Evidence: the valley of stability (nuclear physics as a map of
pending decays); the U-238 chain — FOURTEEN consecutive
decays over 4.5 Gyr terminating at Pb-206, the first nuclide
with no decay available (the "cascading chains" made
matter). Cosmic-scale instance: vacuum metastability — this model
bets the floor holds no pending decay (true ground state,
shift-protected) and signed it as P-2026-002.

**C4g — The contingency tree (correspondence-grade).** The picture — every route to
the outcome explored simultaneously, each branch's CONTENT pre-written,
nothing actual until it decoheres — is the sum-over-histories (Feynman),
with Heisenberg's potentia as the stocked-store ontology and one
quantum upgrade that is THE measured classical/quantum split: branches
INTERFERE. Classical trees add probabilities (more routes = more
probability); quantum trees add amplitudes before squaring — two open routes
to the same outcome can cancel to a GUARANTEED null (the double slit;
close one route and the outcome returns). Branch-content pre-written:
correct. Branch-selection pre-made: forbidden (Bell) and
interference-refuted. Corollaries booked: competing decay channels as
racing processes (the first to complete forecloses the rest — branching
ratios are the race statistics); the consistent-histories condition
(only history-sets that have stopped interfering carry probabilities)
arrived unprompted.

**C4h — The equal-weight rule (the Born door re-graded).** Proposal: which
branch decoheres is timing; the odds are amplitude-weight. Scored:
TIMING dies as outcome-selector (2015 loophole-free Bell tests:
spacelike random settings chosen in flight — no timing mechanism
survives) though it stands for channel races (C4g); COST-EFFICIENCY
died in C4b (beam splitters dial arbitrary odds between
identical-energy routes — odds follow preparation, not the energy).
But the EQUAL-WEIGHT structure is Zurek's envariance fine-graining,
inverted one notch: the rule does not weight by size — it counts
ONLY equal-amplitude sub-branches. Every branch splits into equal-amplitude
fine-grained sub-branches; symmetry (envariance) forces equal sub-branches
= equal odds; **probability = the count of equal sub-branches; |ψ|² is the
conversion.** The 98/2 superposition is 98 units
against 2. Genuine rate-level preference exists one
level down: Bose (1+n) — the medium favors a mode
already occupied (every laser). DOOR RE-GRADED: not "locked for
everyone" — two picks in the lock (Gleason: probability forced by Hilbert-space
geometry, proven; Zurek: sub-branch counting, respected but contested
for circularity). Neither fully turned; the second was reconstructed
from the counting argument.
**Addendum — "easier to distribute":** this
one-line follow-up is the third Zurek pillar, quantum Darwinism: the
environment is a broadcast medium; branches become CLASSICAL when
their records copy redundantly into many independently-readable
environmental fragments — classicality is selected by distributional
cheapness (observed: photonic/NV-center redundancy experiments,
2018–19). And interchangeability closes the counting loop: probability can
only be built on interchangeable units — swap-symmetry (envariance)
is exactly what forces equal sub-branches to equal odds. Equal units are not
merely convenient; they are the only division symmetric enough
to define probability.

### Closed

**X1 — The floor is not thermal, not Casimir, not zero-point.** Three
ontologies for ρ_∞ tested dimensionally: Gibbons-Hawking thermal bath
(ρ ~ T_GH⁴) misses by **10¹²⁴**; cosmic-Casimir (ρ ~ H⁴) by **10¹²¹**;
summed zero-point to the Planck cutoff overshoots by **10¹²¹**. The
only surviving ontology is the fourth: **a condensate constant (P₀ of
the medium)** — which is what dCDF asserts. The cosmological-constant
problem relocates to "why is P₀ small" (no worse than standard), but
the *identification* question is settled by elimination.

**X2 — Standard running cannot source the m_e amendment.** QED running
is frozen below T ~ m_e (recombination sits at T/m_e ~ 5×10⁻⁷); thermal
corrections there are O(αT²/m_e²) ≈ 10⁻¹⁵. The 1% epoch-shift the dyad
fits is *structurally* precedented (couplings do run with environment)
but *quantitatively* new physics — the sourcing question stays with
§9.4's epoch-separated mechanisms.

**X3 — Boundary objects live off the inhabitant ladder, and the
horizon is not one that matters.** The Casimir slab realizes effective
w = +3 (super-stiff, forbidden to any fluid inhabitant) because
boundaries are not inhabitants — but the one cosmic boundary available
(the de Sitter horizon) contributes only at the 10⁻¹²¹ level (X1).
No cosmic Purcell loophole at background level.

### Open

**O1 — RESOLVED (2026-07-06): applied and stress-tested.** The map
issued all three certificates (cert 3 exact — δK vanishes on tensors to
all orders since det(e^h)=1; cert 2 closed via the GC dictionary —
M₂ = ρ_dust,0^{1/4}/(2x₀)^{1/4} ≈ 9.4 eV, gravity-mixing spatially at
0.87 kpc but temporally frozen at 3×10²⁰ Hubble times, accumulated
μ−1 ≈ 4×10⁻²¹; cert 1 passed via the Landau mechanism — v_c = 0 means
flows dissolve caustics into de Broglie interference, with the vortex
caveat). Six stress tests then attacked the map itself:
 *Passed, nontrivially*: the pre-basin equation of state w = 1/3 is
 derived independently by background dynamics (P ∝ X²) AND by the
 map's phonon-gas thermodynamics (linear dispersion at c_s² = 1/3 →
 w = n/3 = 1/3) — two roads, one number, the map's first genuine
 cross-check. *Upgraded*: vortices are quantized in SHIFT CHARGE —
 the emergent U(1) of the nonrelativistic limit is the shift symmetry
 itself; the symmetry that builds the model protects its defects.
 *Refined*: caustic dissolution is kinematic (interference,
 instantaneous); halo thermalization is gravity-mediated and fast in
 ultra-faint dwarfs (~10⁻³ Gyr at order-of-magnitude scaling) —
 sharpening the heating knife on the core discriminator.
 *Boundaries stamped*: the correspondence is kinematic and
 compositional, NOT thermodynamic — the medium is collisionless, never
 thermalizes, so Landau two-fluid heat transport (second sound,
 thermal counterflow) does NOT carry over; and there is no counterflow
 degree of freedom at all (both "components" are perturbative pieces
 of one field — the map describes composition, it does not double the
 dynamics).

**O2 —** Does the condensation epoch (basin entry) freeze in any relic
observable? Ideal BECs condense without defect formation (no broken
gauge symmetry in shift-symmetric P(X)), so the default answer is no —
but the pre-basin normal fraction's decay deserves one careful pass.

**Stress-test round (2026-07-06, free-rein pass):** C2 refined — the
action-currency resolution applies to *excitations* (all inhabitants =
mode occupations; adiabatic invariants exact); the condensate is a zero
mode *outside* the excitation spectrum — not a mode but the frame the
modes are measured against. The one number-changing era
(double-Compton/bremsstrahlung, z ≳ 2×10⁶) closed with a measured
confirmation: FIRAS's blackbody (|μ| < 9×10⁻⁵) is the check that the action
count has been conserved since. Basin entry sits at/below that window and
injects nothing (gravity-only) — consistent. C1 survived the
weak-force stress: massive coupling channels exist (W/Z) but the cosmic
one is measured massless to ~10 H₀ (graviton-mass bounds); and Law 2's
dissipative exception channel (spontaneous emission ↔ dark decay) is
CLOSED for our medium by shift symmetry — registered as the model's
second no-hedge prediction, **P-2026-002: the dark medium cannot decay;
one confirmed dark-decay signal kills the identification.** X1
survived the fifth-ontology check (holographic ρ ~ M_Pl²H² is the
Friedmann closure restated — circular). The heating knife quantified as
an honest fork: if the ultra-faint-dwarf heating bounds
(Dalal–Kravtsov-class, m ≳ 3×10⁻¹⁹ eV) hold, dwarf cores shrink below
1 pc and the small-scale discriminator is DEAD — the model reverts to
the pure dyad with §4.2 permanent; if those analyses' relaxation
modeling fails scrutiny (contested), a window at M ~ 1–3×10⁻²¹ eV with
60–200 pc cores survives. The discriminator's life now rests on a
contested astrophysics literature, stated plainly.

**O3 —** Purcell-engineering at sub-cosmic scales: environments that
reshape the dark medium's local mode structure (deep halo interiors,
BH near-zones) could in principle modulate dark-sector interaction
rates the way cavities modulate spontaneous emission. Speculative;
parked until the (δK)² certificates define which modes exist.

---

*History: v1–v3 (F(φ)R non-minimal coupling + screening) closed — four
independent H₀-rescue mechanisms failed by direct calculation. v4
(β-deformed dCDF) superseded by this document. Full v4 derivation including
the GCG no-go algebra and the v4.1 logistic exploration:
`PRTOE_v4_dCDF_derivation.md`. Results archaeology:
`PRTOE_v4_dCDF_results.md`.*
