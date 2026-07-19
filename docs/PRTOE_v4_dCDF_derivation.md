# PRTOE v4 — dCDF (Dynamic Cold Dark Fluid): Action → Equations → Stability

> *Some statuses in this file may be superseded by later work; the current conditionality of every claim is tracked in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


> **v5 UPDATE (2026-07-05): β has been deleted from the model.** The MCMC
> drove β to its null limit (log₁₀β ≈ −8; any β ≥ 10⁻⁶ destroys σ8), so the
> barotropic deformation was removed entirely: the equation of state is now
> **w(ρ) = −ρ_∞/ρ exactly** (equivalently p ≡ −ρ_∞, a ΛCDM-form background)
> with **c_s² ≡ 0**. dCDF v5 samples 8 parameters — only +1 (ξ_Neff) vs ΛCDM.
> Everything below remains the correct derivation of the general P(X)
> framework, but the β-specific sections are now **historical**: §3.2 (the
> two-parameter family), §9.4 (logistic ansatz — a review also found its
> c_s²≥0 claim unproven, which is moot now), and the β rows of the parameter
> dictionaries. Configs passing `dcdf_beta` now fail loudly. Current results,
> validation matrix, and best fit: `PRTOE_v4_dCDF_results.md`.

**Status: derived, implemented, and first successfully run end-to-end
(2026-07-04)** — background+perturbations+Cl/Pk all complete with sane
(non-NaN, smoothly-varying) output; classy import confirmed working; budget
closes to Ω_tot=1.00001 for Ω0_dcdf=0.9492 alongside standard baryons/ncdm.
Three real bugs found and fixed during first build (not just typos —
genuine physics/units errors caught by actually running the code, exactly
the kind of thing hand-derivation can't catch):
1. **Budget double-fill**: forcing Ω_Λ's shooting flag to "already set" only
 blocked *that* auto-fill branch; Ω_fld's `else if` then filled the
 residual instead. Fix: wrap the whole λ/fld/scf auto-fill chain in
 `if (pba->use_dcdf==_FALSE_)`, not just the λ branch.
2. **Units mismatch**: `dcdf_rho_inf` is documented "in H0² units" but was
 never actually multiplied by H0² before being compared against
 `rho_dcdf` (which *is* in absolute units via the `Ω_ini·H0²·a⁻³` initial
 condition). Since H0²~5×10⁻⁸ is tiny, the floor ended up enormous
 relative to everything else and the fluid froze at the wrong value
 immediately, swamping the whole universe (age came out as 0.024 Gyr,
 should be ~14). Fixed by scaling `dcdf_rho_inf *= H0²` at read time, and
 correspondingly un-scaling it in the shooting xguess formula (which
 works in dimensionless Ω units).
3. **Synchronous gauge needs nonzero CDM**: forcing `Omega0_cdm` to a literal
 0 breaks CLASS's synchronous-gauge assumption (comoving slicing is
 *defined* relative to the CDM rest frame) — fatal error in
 `perturbations_init`. Fixed by using CLASS's own existing
 `ppr->Omega0_cdm_min_synchronous` floor (1×10⁻¹⁰, physically negligible)
 instead of an exact zero.

Also confirmed numerically: for β→0 the continuity equation with
`w=-e⁻ˢ` integrates in closed form to `ρ(a) = ρ_∞ + K·a⁻³`, giving
`Ω0_dcdf(today) ≈ Ω_ini_dcdf + ρ_∞` (in dimensionless Ω units) almost
exactly — this is the shooting initial-guess formula now used in
`input.c`, and it converges in 4 function evaluations.

**Sample working parameters** (`test_dcdf_v4.ini`): h=0.674, Ω0_dcdf=0.9492
(closes budget with Ω_b=0.049, one 0.06eV ncdm species, radiation),
dcdf_beta=1×10⁻⁷, dcdf_rho_inf=0.7 → age=13.98 Gyr, σ8=0.789, w(today)≈-0.70,
c_s²(today)≈5×10⁻⁸ (order β, as predicted). Falsifiability tests (§6) still
not run — this was a functionality check, not yet a physics comparison
against ΛCDM.
This supersedes the v3 (F(φ)R non-minimal coupling) program, which is closed —
see `[[prtoe-screening-nogo]]` memory / `archive/root_cleanup_20260705/HANDOFF_FOR_GEMINI.md` for the four
independent H₀-rescue attempts that failed by direct calculation. v4 does **not**
modify gravity. It replaces separate CDM + Λ (or CDM + fld) with a single dark
fluid whose equation of state depends on its own density, unifying "dark matter"
(dense, clustering, dust-like) and "dark energy" (dilute, relaxed, vacuum-like)
as two regimes of one medium — the direct formalization of the trampoline
analogy: one fabric, stretched near mass, flat far from it.

## 0. Why not v3's approach, in one paragraph

v3 coupled a scalar field to curvature, `F(φ)R`, and tried to get an H₀ win from
the induced sound-horizon shift. Four independent attempts (trace-kick from
φ=0, ξ₁ sign flip, λ sign flip, negative φ_ini) all failed or were provably
sign-locked. v4 abandons curvature coupling entirely: gravity is exactly GR.
The only non-standard physics is in the dark sector's internal dynamics — a
structurally simpler, lower-risk place to put new physics, since it trivially
evades every PPN/solar-system constraint that v3 needed screening machinery
for.

## 1. Action

$$ S = \int d^4x\sqrt{-g}\Big[\frac{M_{pl}^2}{2}R + P(X)\Big] + S_m[g_{\mu\nu},\psi_b] \tag{1} $$

Single real scalar field φ, purely kinetic (shift-symmetric: no explicit φ in
P), $X \equiv -\tfrac12 g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi = \tfrac12\dot\phi^2$
on FLRW. Baryons/photons couple only through $g_{\mu\nu}$, minimally — ordinary
matter never sees the field directly.

Standard k-essence stress tensor (Garriga–Mukhanov 1999) gives, on the
homogeneous background:

$$ \rho = 2X P_X - P, \qquad p = P(X) \tag{2} $$

and the field equation (no explicit φ-dependence ⟹ shift current conserved):

$$ \frac{d}{dt}\big(a^3 P_X \dot\phi\big) = 0 \quad\Longrightarrow\quad a^3 P_X\dot\phi = \text{const} \tag{3} $$

Because ρ and p are both single-valued functions of X alone, **p(ρ) is exactly
barotropic** — no non-adiabatic pressure perturbation, unlike v3's F(φ,R)
sector. This is the structural simplification that lets the perturbation
sector collapse onto CLASS's existing fluid machinery (§4).

## 2. No Q term — this is one fluid, not two

The original v4 skeleton posited `ρ_d' = -3H(1+w(ρ_d))ρ_d + Q` with Q "sourced
by the matter trace." That's a leftover from an *interacting-dark-energy*
mental model (two sectors exchanging energy) and is inconsistent with the
"genuinely one fluid" framing. **Q = 0.** The continuity equation is closed:

$$ \rho_d' = -3\mathcal{H}(1+w(\rho_d))\,\rho_d \tag{4} $$

The R/3H² = Ω_m(z) trace-clock (the one piece of the v1–v3 program that
survived every rewrite) is repurposed, not discarded: it no longer gates an
energy transfer, it identifies which regime a *given point in space* is in —
dust-like inside a halo (locally dense), vacuum-like in a void (locally
dilute). The "contact threshold" is a **density**, not a time.

## 3. The de Sitter fixed-point constraint (the error caught and corrected)

If $w(\rho)=-1$ identically anywhere, eq. (4) forces $\rho'=0$ there — the
density cannot keep diluting while sitting at $w=-1$. So any viable w(ρ) must
approach $-1$ only as $\rho\to\rho_\infty$, a genuine fixed point (de Sitter
attractor), never at $\rho=0$. Define

$$ s \equiv \ln(\rho/\rho_\infty) \geq 0 \tag{5} $$

**General local stability condition at the fixed point.** Sound speed for a
barotropic k-essence fluid is $c_s^2 = dp/d\rho$ (adiabatic, exact — see §1).
Writing $p=w(\rho)\rho$ and changing variables to $s$:

$$ c_s^2(s) = w(s) + \frac{dw}{ds} \tag{6} $$

At $s=0$: $c_s^2(0) = -1 + w'(0)$, so **any viable model needs $w'(0)\ge 1$**
— a clean, model-independent requirement, checked before committing to a
specific shape.

### 3.1 The single-parameter family fails to decouple two things it needs to

The Chaplygin-gas-derivable family (Bento–Bertolami–Sen, hep-th/0202064),
$p=-A/\rho^\alpha$, integrates the continuity equation in closed form:

$$ \rho(a) = \big[A + Ba^{-3(1+\alpha)}\big]^{1/(1+\alpha)} \tag{7} $$

verified limits: $a\to0$ gives $\rho\propto a^{-3}$, $w\to0$ (dust); $a\to\infty$
gives $\rho\to A^{1/(1+\alpha)}\equiv\rho_\infty$, $w\to-1$ (vacuum). In terms
of $s$: $w(s) = -e^{-\gamma s}$ with $\gamma=1+\alpha$, and

$$ c_s^2(s) = (\gamma-1)\,e^{-\gamma s} \tag{8} $$

which **peaks exactly at the fixed point**, $c_s^2(0)=\gamma-1=\alpha$. This
is the whole Sandvik–Tegmark–Zaldarriaga–Frieman (PRD 69, 123524, 2004)
tension in one line: **α simultaneously controls "how different from ΛCDM"
and "how large the dangerous peak sound speed is."** They are the same knob.
Making the model interesting (α not tiny) makes it fail LSS constraints;
making it safe (α→0) makes it degenerate with ΛCDM+dust. No amount of
sharpening a *single-parameter* transition escapes this — an earlier version
of this derivation claimed otherwise and was wrong; corrected here.

### 3.2 A genuine two-parameter family that decouples them

Pin $\gamma=1$ exactly (marginal: zero sound speed *at* the fixed point) and
add a quadratic correction to the exponent:

$$ w(s) = -\exp\big[-(s+\beta s^2)\big], \qquad \beta > 0 \tag{9} $$

$$ c_s^2(s) = 2\beta s\, e^{-(s+\beta s^2)} \tag{10} $$

**Always $\ge0$ by construction** (no gradient instability, any β>0). Peak
value, located near $s^*\approx1$ for small β (from $2\beta s^2+s-1=0$):

$$ c_s^2(\text{peak}) \approx 0.74\,\beta \tag{11} $$

Verified numerically (not just algebraically) at β = 1×10⁻¹, 1×10⁻³, 1×10⁻⁵, 1×10⁻⁷:
peak scales linearly with β exactly as predicted, **while the transition
width stays fixed at $s\sim4$–$5$ regardless of β** (checked: reaches
$w>-0.01$ at $s\approx4.6$ for β from 1×10⁻¹ down to 1×10⁻⁷). This is the
decoupling §3.1 lacked: β suppresses the dangerous peak sound speed
independently of how compressed (in e-folds of density) the transition is.
This is now the adopted background equation of state.

**Honest limitation:** the peak-$c_s^2$ estimate is a proxy, not a Boltzmann
calculation. Whether $\beta\sim10^{-7}$ (chosen to target peak $c_s^2\sim10^{-7}$,
comfortably below Sandvik-type bounds) actually reproduces a viable matter
power spectrum is a numerical question — the first real test to run once the
code below is built.

## 4. Perturbations

Because §1 established exact barotropicity, this is an ordinary imperfect
fluid with no anisotropic stress. **These are the same equations CLASS
already implements for `has_fld`** (Ma & Bertschinger 1995 synchronous
gauge), reused rather than reinvented:

$$ \delta' = -(1+w)\Big(\theta+\frac{h'}{2}\Big) - 3\mathcal{H}(c_s^2-w)\delta \tag{12} $$

$$ \theta' = -\mathcal{H}(1-3c_s^2)\theta + \frac{c_s^2}{1+w}k^2\delta \tag{13} $$

with $w$ and $c_s^2$ now functions of the background density
$\bar\rho_d(a)$ via eqs. (9)–(10), evaluated at each timestep, rather than
constants (`w0_fld`/`wa_fld`) or a fixed `cs2_fld`. This directly replaces
v3's custom δφ + Bardeen-potential + N_gal/galileon sector — no new
perturbation formalism needs to be invented, only two background-dependent
functions plugged into the existing fluid equations.

## 5. Stability / degrees of freedom

- **Gravity:** unmodified GR. No galileon ghost/gradient conditions, no
 Vainshtein screening, no G_eff/PPN bookkeeping — the entire "protective
 machinery" category from v1–v3 does not apply here.
- **DOF:** single scalar, 2 phase-space DOF (φ, φ̇), nothing exotic.
- **No-ghost:** $P_X + 2X P_{XX} > 0$ (equivalently, $\partial \rho / \partial X > 0$ for the k-essence branch used here).
- **No-gradient:** $c_s^2\ge0$ — satisfied identically by construction for
 eq. (10), any $\beta>0$. This is a structural improvement over v3, where
 the galileon no-ghost/no-gradient conditions had to be checked numerically
 at every background point and had a narrow compatibility window.

## 6. Falsifiability tests — now well-posed, not yet run

1. **r_s / H₀.** The transition (eq. 9–10) is not automatically near
 recombination — GCG-type transitions naturally sit at $z\sim0$ (to match
 today's $\Omega_{DE}$). To get *any* r_s effect, $\rho_\infty$ (equivalently
 the transition redshift $z_t$) must be deliberately placed near
 matter-radiation equality. This is a design choice requiring
 $\Omega_m(z_{eq})$ to stay consistent with BBN/CMB once placed there — not
 automatic, needs to be checked once implemented.
2. **σ8.** Controlled by $c_s^2(\bar\rho_d(a))$ evaluated during matter
 domination — needs to be small enough there to avoid Sandvik-type power
 suppression, while nonzero enough at today's mean density to differ from
 ΛCDM. β is the knob; §3.2's peak-$c_s^2\approx0.74\beta$ estimate is the
 starting point, to be confirmed against an actual computed $P(k)$.
3. **Halo profile.** Same $c_s^2(\rho)$ evaluated at galactic/halo densities
 (≫ cosmological mean). A residual nonzero $c_s^2$ there predicts a
 **cored** profile rather than an NFW cusp — potentially a feature (core-cusp
 problem) rather than a bug, *if* the residual sound speed lands at kpc
 scale rather than Mpc scale. Not yet checked.

## 7. Parameter dictionary (for the code)

| Symbol | Code name | Meaning |
|---|---|---|
| $\rho_\infty$ | `pba->dcdf_rho_inf` | de Sitter floor density, H0² units |
| $\beta$ | `pba->dcdf_beta` | quadratic shape parameter, eq. (9) |
| $\Omega_{d,\rm ini}$ | `pba->Omega_ini_dcdf` | dust-era amplitude (shooting unknown) |
| $\Omega_{d,0}$ | `pba->Omega0_dcdf` | target density fraction today (shooting target) |
| $s$ | — | $\ln(\rho_d/\rho_\infty)$, computed, not stored as a parameter |

## 8. Open theory debts ([DERIVE] tags, honest as of implementation start)

- **[DERIVE]** §3.2's family was constructed to satisfy the local
 no-gradient condition and match the two asymptotic limits; it was *not*
 derived top-down from a specific $P(X)$ via the reconstruction procedure
 referenced in §1. The general k-essence "designer" reconstruction
 (inverting $a^3P_X\sqrt{2X}=\text{const}$ against a target $\rho(a)$) is
 known to exist for any smooth target — it has not been carried out
 explicitly for eq. (9). Doing so is not required to run the background +
 perturbation code (§4 only needs $w(\rho)$, $c_s^2(\rho)$), but is required
 before claiming a complete UV picture.
- **[DERIVE]** The peak-$c_s^2\approx0.74\beta$ estimate (§3.2) is a
 proxy for the real observable (suppressed matter power spectrum). Needs a
 computed $P(k)$ comparison, not just the peak value.
- **[DERIVE]** Transition redshift placement (test 1 above) has not been
 checked against BBN $N_{eff}$/matter-radiation-equality bounds.

## 9. v4.1 — Split the Lagrangian, not the fluid

Prompted by the user's two-piece intuition ("one mode stays always active, a
constant rate of relaxed expansion; mass and density add the extra dynamism"),
generalized (after establishing that any single barotropic fluid is secretly
just a $w(a)$ reparametrization — §6/8 above are unavoidable for *any* dCDF-style
model) to the one construction that actually adds new freedom: keep one field,
one action, but split the **Lagrangian**, not the **fluid**.

### 9.1 Action

$$ P(X) = P_{\rm kin}(X) - \Lambda, \qquad P_{\rm kin}(0)=0 \tag{14} $$

$\Lambda$ is a bare additive constant in the Lagrangian, not a second fluid.
Standard k-essence stress tensor gives

$$ \rho = 2XP_X - P = \rho_{\rm kin}(X) + \Lambda, \qquad p = P_{\rm kin}(X) - \Lambda \tag{15} $$

i.e. the field still has exactly one continuity equation, exactly one dynamical
degree of freedom — but its energy density is the kinetic piece riding on top
of a flat floor $\Lambda$, and as $X\to0$ (field relaxes / dilutes), $\rho\to\Lambda$,
$p\to-\Lambda$, $w\to-1$ **unconditionally**, with no fixed-point fine-tuning
required. This is the "constant rate of relaxed expansion" the user described:
the floor is not a limit the kinetic piece has to be steered into (§3's whole
problem), it is a separate additive term that is *already* exactly de Sitter
by construction.

### 9.2 Code consequence: Λ needs no new code

Because $\Lambda$ enters $\rho$ additively and contributes no perturbations
(it is a true constant, not a field value that varies with $X$), it is
*exactly* CLASS's existing `has_lambda`/`Omega0_lambda` mechanism — vanilla,
untouched, since v1. Re-enabling `Omega0_lambda` (which v4.0 zeroed out) and
letting it float freely in the shooting budget reintroduces it with zero new
code. The only new physics is $\rho_{\rm kin}(X)$, which reuses v4.0's
machinery (background ODE + `has_fld`-style perturbations) applied to
$\rho_{\rm kin}$ alone rather than $\rho_d$.

This is also why the H₀/r_s conclusion from §6 test 1 **carries over
unchanged**: at high density (early universe), $\rho_{\rm kin}\to$ dust
($w_{\rm kin}\to0$) by construction (§9.4), and $\Lambda$ is negligible next to
$\rho_{\rm kin}$ there — so the expansion history pre-recombination is
ΛCDM+CDM to arbitrary precision regardless of $w_{\rm kin}$'s shape. Nothing
in this section changes that; Gemini's ongoing v4.0 MCMC χ² result is not
wasted, it answers the same H₀ question for v4.1 too.

### 9.3 What's now free: $\rho_{\rm kin}$ no longer needs a fixed point

Since $\Lambda$ supplies the late-time acceleration on its own, $\rho_{\rm kin}$
is **not** required to approach any particular floor as $X\to0$ — it can go to
zero. Define $s=\ln(\rho_{\rm kin}/\rho_*)$ for some reference density $\rho_*$
(now a free placement parameter, not a fixed point). This removes the GCG
no-go's coupling (§3.1) entirely: nothing forces $w_{\rm kin}\to-1$ anywhere,
so the constraint "$c_s^2=0$ at the point where $w=-1$" that pinned $\gamma=1$
in v4.0 simply does not apply. $w_{\rm kin}(s)$ is free to be *any* function
with $w_{\rm kin}\to0$ as $s\to+\infty$ (dust at high density — required so
$\rho_{\rm kin}$ behaves as CDM at early times/high-z) and $c_s^2\ge0$
everywhere (no-gradient, eq. 16 below).

### 9.4 Ansatz: attempt and rejection, then the logistic family

**First attempt (rejected):** a Gaussian bump in $w_{\rm kin}(s)$,
$w_{\rm kin}=-w_0\exp(-s^2/2\sigma^2)$, to localize the pressure near $s=0$.
Direct computation of $c_s^2=w_{\rm kin}+dw_{\rm kin}/ds$ shows this goes
**negative** on the rising side of the bump for any $\sigma$ — the same
no-gradient failure mode as v3's badly-tuned regions. Rejected.

**Working ansatz** — logistic crossover from dust (high $s$) to a pressure
plateau (low $s$):

$$ w_{\rm kin}(s) = \frac{w_1}{1+e^{s/\Delta}} \tag{16} $$

with $w_1<0$ (pressure, matching a decelerating-to-accelerating role) and
$\Delta>0$ the transition width in e-folds of density. This gives

$$ c_s^2(s) = w_{\rm kin}(s)\left[1-\frac{1}{\Delta}\left(1-\frac{w_{\rm kin}(s)}{w_1}\right)\right] \tag{17} $$

(verified symbolically against the direct derivative $w_{\rm kin}+dw_{\rm kin}/ds$;
difference is identically zero). Writing $x=w_{\rm kin}/w_1\in[0,1]$, eq. (17)
is $c_s^2=w_1\,x(1-(1-x)/\Delta)$, a downward parabola in $x$ with critical
point $x^\star=(1-\Delta)/2$. For $\Delta\ge1$, $x^\star\le0$ falls outside the
physical range $x\in[0,1]$, so $c_s^2$ is monotonic in $x$ over the physical
range and its minimum is at the boundary $x=0$ (i.e. $c_s^2=0$, attained only
as $s\to+\infty$). **$\Delta\ge1$ is therefore sufficient for $c_s^2\ge0$
everywhere** — no-gradient satisfied globally, not just asymptotically.

### 9.5 No-ghost, checked explicitly (not just asserted)

For k-essence, the standard identity is
$c_s^2 = P_X/(P_X+2XP_{XX})$. No-ghost requires the denominator
$P_X+2XP_{XX}=\partial\rho/\partial X>0$ (needed for $\rho$ to be a
monotonic, invertible function of $X$ at all — the same requirement that lets
"$w(\rho)$" mean anything). Given no-ghost holds, $c_s^2\ge0 \iff P_X\ge0$.
Since (9.4) enforces $c_s^2\ge0$ by construction and the $s\leftrightarrow X$
map is built to be monotonic (the field dilutes monotonically as it relaxes,
same continuity-equation argument as v4.0 §5), both conditions hold together:
$\partial\rho/\partial X>0$ and $P_X\ge0$. No ghost, no gradient instability,
confirmed for this specific ansatz rather than asserted by analogy.

### 9.6 Falsifiability recheck — σ8 and halo profile, actually computed this time

I flagged to Gemini that halo-profile "might reopen" since $\Lambda$ removes
the fixed-point constraint that forced v4.0's double-exponential suppression.
Checked numerically rather than left as a hope:

**σ8 (linear era, $s\lesssim5$: today's mean matter density out to $z\sim3$–5).**
Eq. (17) decays as $c_s^2(s)\sim w_1 e^{-s/\Delta}$ for $s\gg\Delta$ — a
**single** exponential in $s$, versus v4.0's **double** exponential
$e^{-(s+\beta s^2)}$. This is a genuine, quantitative improvement: much
gentler suppression per e-fold, so a given peak $c_s^2$ (set by $w_1$) stays
"live" over a wider density range before collapsing to zero. Confirmed
numerically (scan over $\Delta\in\{1,2,3,5,8\}$, $w_1\in\{10^{-6},10^{-4},10^{-2}\}$).

**Halo profile (galactic/halo overdensity relative to mean matter density,
$s\approx11.5$–$16$).** Eq. (16)–(17) give $c_s^2$ that is monotonically
decreasing in $s$ once past its peak (which sits at/near $s\to-\infty$, i.e.
$c_s^2\to w_1$ as $s\to-\infty$, decaying to $0$ as $s\to+\infty$). This is
structural, not a tuning accident: **any** $w_{\rm kin}(s)$ that must go to
$0$ (dust) as $s\to+\infty$ and is built from a single monotonic crossover has
a $c_s^2(s)$ that can only decay (or stay flat) as $s$ increases past the
transition — it cannot be small at $s\approx0$–$5$ (required for σ8 safety)
and then *larger again* at $s\approx11.5$–$16$ (required for a halo-core
signature), because that would require $c_s^2$ to have a local minimum
followed by a rise — i.e. a genuine **bump**, not a monotonic crossover.

So: pick $\Delta,w_1$ to keep $c_s^2$ negligible at $s\lesssim5$ (σ8-safe) and
the halo-density value is *by construction* even smaller (same conclusion as
v4.0, test 3 — closed, not reopened). Pick $\Delta$ wide enough that $c_s^2$
survives out to $s\approx12$–$16$, and $c_s^2$ is then *also* non-negligible
(same order of magnitude, since the decay is only single-exponential and
$\Delta$ comparable to the whole range flattens the profile) at $s\approx0$–$5$
— wrecking σ8 the same way v4.0's β did, just via a different knob. There is
no $(\Delta,w_1)$ that threads both needles with a monotonic $w_{\rm kin}(s)$.

**Honest correction of my message to Gemini:** a genuine halo-core signature
would require $c_s^2(s)$ itself to be a *bump* (small at $s\sim0$–5, rising to
non-negligible at $s\sim12$–16, presumably falling again beyond that), which
is mathematically constructible — integrate the linear ODE
$w_{\rm kin}'(s)+w_{\rm kin}(s)=c_s^2(s)$ (integrating factor $e^s$) for any
chosen target bump $c_s^2(s)$ — but that is curve-fitting a feature at a
hand-picked density with no independent physical motivation (no fixed point,
no reconstruction from a target $P(k)$ or rotation-curve fit forces the bump's
location or width). It is achievable but not a prediction; flagging it as an
"epicycle" rather than pursuing it, unless the user wants to explicitly go
that route.

### 9.7 Verdict

- **H₀ / r_s:** unchanged from v4.0 — still no relief, same mechanism-inverted
 result Gemini found, since $\rho_{\rm kin}\to$ dust at high-$z$ regardless of
 the ansatz (§9.2).
- **σ8:** genuinely freed from the GCG no-go coupling (§9.3) — $w_1,\Delta$ are
 two independent knobs with no fixed-point tax, and the single-exponential
 tail (§9.6) is gentler than v4.0's double-exponential. Structurally *better*
 machinery, though it still can't do more than v4.0 could (suppress growth by
 some amount at the cost of a cliff — the freedom is in how the cliff is
 shaped, not in avoiding the cliff).
- **Halo profile:** still closed, now for a sharper, more general reason than
 v4.0's "6 orders of magnitude, specific to the double-exponential" — *any*
 monotonic single-crossover $w(\rho)$ has this property, independent of the
 particular shape. This generalizes past v4.1 too: it applies to every dCDF
 variant built as "dust at high $\rho$, something else at low $\rho$" via one
 smooth crossover.

### 9.8 Parameter dictionary addendum

| Symbol | Code name | Meaning |
|---|---|---|
| $\Lambda$ | `pba->Omega0_lambda` (re-enabled, vanilla) | de Sitter floor, exact, from action's additive constant |
| $\rho_*$ | `pba->dcdf_rho_star` | reference density for $s=\ln(\rho_{\rm kin}/\rho_*)$, free placement |
| $w_1$ | `pba->dcdf_w1` | pressure-plateau depth, eq. (16) |
| $\Delta$ | `pba->dcdf_delta` | transition width in e-folds; $\Delta\ge1$ required (§9.4) |

Not yet implemented in code — this section is derivation only, per the
"fully flesh out the math before touching code" rule. Handed to Gemini
(2026-07-04) for implementation + numerical validation against actual CLASS
output (this section's $c_s^2(s)$ formulas are algebra-level, not yet checked
against a real perturbation run), since v4.0's code pattern (background ODE +
`has_fld`-mirrored perturbation sector) is a well-defined mechanical port and
Gemini has the larger usage budget for the build/test/MCMC-integration cycle.
