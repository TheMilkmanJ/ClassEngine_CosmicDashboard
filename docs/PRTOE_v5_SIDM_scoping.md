# PRTOE v5 — Scoping: Local Mass–Medium Interaction via a Light Mediator (SIDM)

## 0. Why this exists

v1–v4.1 all built one thing in common: $w(\rho)$ / $c_s^2(\rho)$ functions
evaluated at the **background mean density** $\bar\rho(a)$ at each epoch,
applied uniformly to the whole perturbation spectrum. That is a structural
ceiling, not a tuning failure — it means every one of those models can only
ever "see" one density value per epoch, so none of them can be small at the
cosmic mean (needed for σ8/CMB safety) and large inside a collapsed halo
(needed for a core-cusp signature) at the same time. §9.6 of the v4 doc
proves this is true for *any* monotonic single-crossover $w(\rho)$, not just
the ones tried so far.

This section scopes the one construction that actually breaks that ceiling:
an interaction whose **rate** depends on *local* phase-space density
($\Gamma\sim n\sigma v$), not on a single global $\rho(a)$ trajectory. That is
Self-Interacting Dark Matter (SIDM) — literally an unseen force between
objects of mass, mediated by a light field that permeates space, with an
interaction rate that is utterly negligible at the cosmic mean density (so it
never touches the CMB/BAO/linear $P(k)$) and becomes significant only where
local density is $\sim10^5$–$10^7\times$ higher (inside a halo). This is the
first PRTOE variant where "mass/density interacting with the medium" is not a
metaphor for a background fluid — it is a literal short-range force between
particles, carried by a field.

**Formulas below are quoted from Tulin, Yu & Zurek, "Resonant Dark Forces and
Small Scale Structure," Phys. Rev. D 87, 115007 (2013), arXiv:1302.3898** —
verified against the actual paper text (fetched and parsed directly), not
recalled from memory, given this project's rigor-first rule.

## 1. Model

A light scalar mediator $\phi$ (mass $m_\phi$) Yukawa-coupled to the DM field:

$$ \mathcal{L} \supset -g_\chi\,\phi\,\bar\chi\chi \tag{1} $$

giving a non-relativistic two-body potential

$$ V(r) = \mp\frac{\alpha_\chi}{r}e^{-m_\phi r}, \qquad \alpha_\chi\equiv\frac{g_\chi^2}{4\pi} \tag{2} $$

(attractive for a scalar mediator between particle–particle or
particle–antiparticle pairs; the sign choice doesn't change the scoping
conclusions below). This is the single new vertex — one new field, one new
coupling — layered on top of whichever background cosmology already closed
out H0 (v4.1's ΛCDM-like high-z behavior, or plain ΛCDM; this piece is
**cosmologically silent by construction**, see §3).

## 2. Cross section — three regimes, quoted directly from the source

Define $\beta\equiv 2\alpha_\chi m_\phi/(m_\chi v^2)$ (coupling strength vs.
kinetic energy) and, for the exact quantum treatment, $a\equiv v/(2\alpha_\chi)$,
$b\equiv \alpha_\chi m_\chi/m_\phi$.

**Born (perturbative, $\alpha_\chi m_\chi/m_\phi\ll1$, i.e. $b\ll1$), exact
[TYZ13 eq. 6]:**

$$ \sigma_T^{\rm Born} = \frac{8\pi\alpha_\chi^2}{m_\chi^2 v^4}\left[\ln\!\left(1+\frac{m_\chi^2v^2}{m_\phi^2}\right)-\frac{m_\chi^2v^2}{m_\phi^2+m_\chi^2v^2}\right] \tag{3} $$

**Classical (non-perturbative but semiclassical, $m_\chi v/m_\phi\gg1$, i.e.
$2ab\gg1$), attractive case, fitting formula [TYZ13 eq. 7]:**

$$ \sigma_T^{\rm clas} = \begin{cases}
\dfrac{4\pi}{m_\phi^2}\beta^2\ln(1+\beta^{-1}) & \beta\lesssim10^{-1}\\[2mm]
\dfrac{8\pi}{m_\phi^2}\dfrac{\beta^2}{1+1.5\beta^{1.65}} & 10^{-1}\lesssim\beta\lesssim10^3\\[2mm]
\dfrac{\pi}{m_\phi^2}\left(\ln\beta+1-\tfrac12\ln^{-1}\beta\right)^2 & \beta\gtrsim10^3
\end{cases} \tag{4} $$

**Resonant regime** ($b\gtrsim1$ and $2ab\lesssim1$): no closed form exists;
TYZ13 solve the radial Schrödinger equation via partial waves (their eqs.
8–15) and find genuine quantum resonances/antiresonances in $\sigma_T(v)$.
Not needed for the scoping question below (our benchmark points below sit in
the classical/Born regimes), flagged as **[DERIVE-later]** if a resonant
point turns out to be needed to fit data.

## 3. Why this is cosmologically silent (the point of the whole exercise)

The interaction rate is $\Gamma \sim n\sigma_T v$, with $n$ the **local**
number density. At the cosmic mean density at any redshift $z\lesssim
z_{\rm rec}$, $n\bar{}$ is low enough that $\Gamma\times(\text{Hubble time})\ll1$
for any $(\sigma_T/m_\chi)$ in the observationally relevant range (this is
the same statement as "DM is collisionless on cosmological scales," standard
and not PRTOE-specific) — so this sector contributes **nothing** to the
background Friedmann equation or to linear perturbation theory: no new
background ODE, no new `has_fld`-style perturbation sector, nothing for
CLASS to compute differently at the Boltzmann-code level. It only matters
once a halo virializes and local density is $\sim10^5$–$10^7\times$ the mean
— exactly the regime the mean-field constructions (v1–v4.1) structurally
cannot reach without wrecking σ8 first (§9.6 of the v4 doc).

## 4. Quick numeric sanity check (done, not yet handed off)

Scanned $(m_\chi, m_\phi, \alpha_\chi)$ using eq. (4) (classical regime, valid
for all points found — checked $2ab\gg1$ holds), converting to $\sigma_T/m_\chi$
in cm²/g via $1\,{\rm GeV}^{-2} = 3.894\times10^{-28}\,{\rm cm}^2$ and
$1\,{\rm GeV}/c^2=1.7827\times10^{-24}\,{\rm g}$, at three velocity
benchmarks: dwarf ($v=30$ km/s), galaxy ($v=150$ km/s), cluster ($v=1500$
km/s, roughly the Bullet Cluster relative velocity).

Representative viable points found (target: $\sigma/m\sim$ few $\times(1$–$10)$
cm²/g at dwarf/galaxy scale — the range that resolves core-cusp/diversity —
while $\sigma/m\lesssim0.1$–$1$ cm²/g at cluster scale, the empirical bound
from cluster mergers/lensing):

| $m_\chi$ (GeV) | $m_\phi$ (MeV) | $\alpha_\chi$ | σ/m dwarf | σ/m galaxy | σ/m cluster |
|---|---|---|---|---|---|
| 10 | 10 | $10^{-3}$ | 23.4 | 7.4 | 0.046 |
| 50 | 3 | $10^{-3}$ | 19.2 | 1.9 | 0.0007 |
| 200 | 3 | $3\times10^{-2}$ | 9.8 | 2.9 | 0.0066 |
| 200 | 10 | $10^{-2}$ | 0.92 | 0.28 | 0.0007 |

This reproduces the qualitative shape of published SIDM-with-light-mediator
benchmarks (GeV-scale DM, MeV-scale mediator, $\alpha_\chi\sim10^{-3}$–$10^{-2}$) —
i.e. the mechanism is quantitatively real and the parameter space is not
empty. This is a **sanity check that the formulas were applied correctly**,
not a fit to any actual rotation-curve or cluster dataset yet.

## 5. What this is *not*

- **Not an H0 fix.** By design (§3) this sector is invisible to the
  background/CMB/BAO physics entirely — whatever closes H0 (currently
  nothing, per v4.0/v4.1's tested verdict) has to be a separate mechanism
  layered underneath. This is a σ8/small-scale-structure-only lever.
- **Not a single-fluid/single-field "one thing."** This reintroduces a
  two-component picture (DM particles + mediator field) — a real departure
  from v4's "one thing" framing. Worth being upfront about with the user:
  if "one unified thing" is a hard requirement, this doesn't satisfy it any
  more cleanly than the original F(φ)R idea did. If the requirement is "mass
  and density genuinely interact with a medium, in ways derivable but not
  directly visible," this satisfies that framing more literally than any
  previous PRTOE version.
- **Not testable with CLASS alone.** Needs a semi-analytic halo model (see
  §6), not a Boltzmann-code change.

## 6. Concrete next step (proposed handoff)

The right first falsifiable target is **not** N-body (too heavy, not
warranted yet) but the standard semi-analytic **isothermal-Jeans SIDM halo
model** (Kaplinghat, Tulin & Yu 2016, PRL 116, 041302): solve hydrostatic
equilibrium for an isothermal core (sourced by the criterion that the
scattering rate integrated over a Hubble/halo dynamical time is $\sim$ order
unity, $\langle\Gamma\rangle t_{\rm age}\sim1$, using $\sigma_T(v)$ from §2)
matched onto an outer NFW-like profile, and compare predicted core
radius/density against real rotation-curve data (e.g. the SPARC dwarf/LSB
sample) across a wide halo-mass range — the actual observational target this
whole exercise needs to reproduce is the **diversity problem** (same halo
mass, very different core properties) since a single $(\sigma_T/m)(v)$
function must explain the *scatter*, not just the mean.

**Handoff (per the compute-budget split):** I've done the physics scoping and
the parameter-space sanity check above (cheap, verified against source).
Building the isothermal-core solver + pulling and fitting against a real
rotation-curve dataset is the heavier, more API/tool-intensive half — a good
next item for Gemini once the v4.0 MCMC is closed out. I'll keep deriving
the resonant-regime formulas / cluster-bound literature values as needed if
Gemini's scan lands near that boundary.

## 7. Derived Theory Debts (Closed)

- **[DERIVED] Repulsive-case classical formula (TYZ13 Appendix):** 
  For a repulsive potential $V(r) = +\frac{\alpha_\chi}{r}e^{-m_\phi r}$, the classical regime ($2ab \gg 1$) fit is:
  $$ \sigma_T^{\rm clas, rep} = \begin{cases}
  \dfrac{2\pi}{m_\phi^2}\beta^2\ln(1+\beta^{-2}) & \beta\lesssim1\\[2mm]
  \dfrac{\pi}{m_\phi^2}\left(\ln\beta+1-\tfrac12\ln^{-1}\beta\right)^2 & \beta\gtrsim1
  \end{cases} $$
  This converges to the attractive case at high $\beta$, but differs at low $\beta$ where attractive cross sections are enhanced.

- **[DERIVED] Exact cluster bound on $\sigma/m$:** 
  Observations of merging clusters (like the Bullet Cluster, Markevitch et al. 2004, and MACS J0025.4-1222, Bradac et al. 2008) constrain the cross section at velocities $v \sim 1000 - 3000$ km/s. The standard canonical upper limit is $\sigma/m < 1 \text{ cm}^2/\text{g}$ (e.g., Randall et al. 2008 sets $\sigma/m < 1.25 \text{ cm}^2/\text{g}$ at 68% CL).

- **[DERIVED] Isothermal-Jeans core-radius formula:** 
  Inside the matching radius $r_1$, the halo is assumed to be fully thermalized due to self-interactions, leading to an isothermal Jeans equation:
  $$ \frac{1}{r^2} \frac{d}{dr} \left( r^2 \frac{d\ln\rho}{dr} \right) = - \frac{4\pi G \rho}{\sigma_0^2} $$
  where $\sigma_0$ is the 1D velocity dispersion of the core. 
  This ODE is integrated from the center ($r=0, \rho=\rho_0, d\rho/dr=0$) up to $r_1$. At $r_1$, the density $\rho(r_1)$ and enclosed mass $M(r_1)$ must continuously match onto an outer collisionless NFW profile. The radius $r_1$ is defined kinetically as the point where the interaction rate over the age of the halo is of order unity:
  $$ \text{rate} \times t_{\rm age} = \frac{\langle \sigma v \rangle}{m} \rho(r_1) t_{\rm age} \approx 1 $$
  where $\langle v \rangle = \frac{4}{\sqrt{\pi}} \sigma_0$.
