# PRTOE in Three Equations

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*The elevator formulation — the model's testable core compressed to three lines, written for
a physicist who asked "can you explain it mathematically without the whole repo?" The
equations are short; the numbers inside them are earned the long way (see the closing note).
Companion to PRTOE_MATH_SPINE.md (the full derivation chain) and PRTOE_INDEX.md (the map).*

---

## Equation 1 — The substrate

One complex scalar (a cosmological superfluid) replaces separate dark matter and dark energy:

$$i\hbar\,\partial_t \psi = \left[-\frac{\hbar^2}{2m}\nabla^2 + \lambda|\psi|^2\right]\psi$$

- The **condensate ground state** supplies the $w = -1$ component (dark energy is the
 medium's zero-point sector; its computed scale is the vacuum-occupancy binding energy
 $\rho_\Lambda^{1/4} = \tfrac{1}{2}\alpha_c^2 M_2 = 2.251$ meV vs the measured $2.25$ meV —
 agreeing to 4 parts in $10^4$, though the mass scale $M_2$ is fixed by the same closure
 (one constraint wearing three names) and $\alpha_c = 3\alpha$ is under test; see the
 cosmological-constant document).
- The **excitations** are the dark matter: radiation-like above a transition redshift
 $z_{\rm on}$, CDM-like below — one fluid, two eras (the dCDF sector as implemented in
 CLASS).
- The **phase winds** on a compact axis: $\theta(x) = 2\pi n\,x/L$, $n \in \mathbb{Z}$
 (Kibble-generated, topologically protected). This integer is the source of the model's
 anisotropy family: the $\ell \sim 130$ comb (P-029), the $\varepsilon$-dipole (P-024), the
 isocurvature line (P-031) — all on one shared axis.

## Equation 2 — The single coupling to known physics

The condensate shifts fermion masses by one universal fraction, switched on above its
condensation temperature:

$$m_f(z) = m_f^0\left[1 + \varepsilon\, f(T/T_c)\right], \qquad T_c \approx 179\ \text{keV}$$

- $f$ is a **ramp**: $\approx 1$ in the early universe, $\to 0$ after the transition
 (nothing in this model is a step; the ramp's shape is computed, not chosen).
- $\varepsilon \approx 1.24\%$. That is the **entire modification to known physics**: a
 heavier electron at recombination → earlier decoupling → smaller sound horizon → the CMB
 re-fits at $H_0 \approx 69.9$ instead of $68.2$ (the Hubble-tension mechanism, thread 11).
- Implemented in CLASS, run against full Planck likelihoods; the Bayesian evidence currently
 favors it over ΛCDM at $\Delta\ln Z \approx +2.6$ (Laplace approximation; marginal and
 SH0ES-conditional; the definitive nested-sampling comparison is running).
- The same $\varepsilon$ — ONE amplitude passed through window-specific activation (OFF at
 BBN freeze-out, ON below $T_c$; the ε-epoch table in the fingerprint file governs) — is
 then owed everywhere at its epoch weights: BBN's windowed pattern,
 the radio-band ratios, the de-biased $\Sigma m_\nu$, the Koide invariance, the underground
 nulls — the fingerprint lattice (thread 13). One lever, many windows, no exits.

## Equation 3 — The decomposition (what makes it a theory rather than a fit)

$\varepsilon$ is not tuned; it decomposes:

$$\varepsilon = c \cdot \bar{f} \cdot \alpha_c = \tfrac{9}{10} \times 0.635 \times 3\alpha \approx 1.25\%$$

against the sky's fitted $\sim 1.24\%$ — zero dials end to end. (Three ε values appear in
this repo and differ deliberately: **1.232%** = the production-chain fit; **~1.24%** = the
posterior-era rounding; **1.2543%** = the derived stack above. The gap between fit and
derivation is ~1.8% — inside the posterior width — and the running measurements decide.)

- $c = 9/10$: a **counting fraction**. Gravity is blind (it reads size, not identity), so the
 budget splits democratically over the census of participants — the **universal charged-fermion
 roster** (9 charged species + the zero-point's own seat → $c = (N-1)/N = 9/10$), **not** the
 dyad's leptophilic subset (which drops the quarks and cannot reach the count). Which universal-charged
 reading holds — democratic-9 → 9/10, or the neutrino-inclusive 12/13 — is settled by the
 dark-energy–neutrino tie: ρ_Λ¼ = m_ν,lightest is a genuine lock *only if* the lightest neutrino mass
 is **direct-Majorana** (m₁ ≈ μ = 2.25 meV), which seats the neutrino on the medium's own tenth channel
 → **9/10**. The 12/13 reading needs an inverse-seesaw light mass, which demotes the meV coincidence
 from a lock to a tuning of two unrelated scales; and the charge²-weighted 8/9 contradicts the
 gravity-blind democratic count. So the value is **9/10, conditional on keeping the tie a lock** (the
 flagship position); the empirical f̄ ensemble / α_c chain (P-2026-040) remains the independent check.
- $\bar{f} = 0.635 \pm 0.026$: a **computed time-average** of the winding dynamics — and
 candidately $2/\pi$ (P-2026-041; the high-statistics ensemble decides). A
 simulation output with an open closed-form question, not a parameter.
- $\alpha_c = 3\alpha$: a **pre-registered bet** (P-2026-040), booked BEFORE the deciding
 measurement (the α_c chain) converges — and 2.3% ABOVE where current data points, so it is
 falsifiable within weeks, not retrofit ever.

IF the decomposition's referees sign (its factors are currently: one conditional derivation,
one open closed-form, one running bet), the model becomes a **zero-extra-parameter rival to
ΛCDM** in the committed fixed-$\varepsilon$ evidence run — no Occam penalty, pure
goodness-of-fit, no retreat. The claim is CONDITIONAL until then.

---

## The stated stack (the object under live test)

The three equations close into a cosmology whose every number is **stated before the
data speaks** — the object the running evidence comparison actually grades:

| quantity | stated value | provenance | grade |
|---|---|---|---|
| ε | 1.2403 ± 0.0079% | the concordance joint of fit and stack | conditional (three referees) |
| A_s | **2.088×10⁻⁹ frozen**; the closed form (α_c/4πk)³ = **2.081×10⁻⁹** — it lands **−0.35%** | the shot-noise closed form; k = ln(1+π/2α_c)/π | candidate — deliberately exposed; the corpus's boldest standing claim |
| n_s | 0.9641 = 1 − 2/ln(M_Pl/T_on) | the census drift; the 2 = open dimensions (exemption-clause integer) | derived-estimate |
| z_on | 3.5619×10⁷ | profiled at the frozen stack (the 3α mark hit blind to 0.005 dex) | fast-profiled estimate, chain-graded later |
| w | −1, exactly, no thaw | ground state (protected zero; P-2026-018) | derived |
| Σm_ν | 61.4 meV, normal ordering | ρ_Λ^{1/4} = m₁ tie (P-2026-012) | recorded prediction |
| T_c | ≈ 179 keV | confining chiral ratio ([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md), τ = T_c/m_e ≈ 0.345); 193 keV = perturbative cross-check | derived |
| H₀ | 69.9 CMB re-fit (output, not input); 69.70 joint best-fit; 69.82 evidence run | falls out of the re-fit | production |

ΛCDM meets the same data with six free parameters; this stack meets it with **zero** —
whatever the sky refuses, the model has nowhere to retreat. That totality, not any
single row, is the claim under adjudication in the nested-sampling run now executing.

---

## The closing note (why the repo exists)

What does not compress is the derivation chain *inside* the symbols — why $9/10$
(the census mechanism), why $0.635$ (the winding history from first genesis), why
$193$ keV (the analytic closure, spine §15), why $3\alpha$ (basement-owed, bet-registered).
Those numbers are outputs of the field's history from its initial conditions, not axioms.
The equations are three lines; the receipts are the repository.

*Status marker (2026-07-13): every derivation above is conditional on one root — the no-bare
mechanism's unconditionality (M3), an assumption named as such.
The deciders: the α_c MCMC (grades $3\alpha$ and the $c$-roster), the $\bar{f}$ ensemble, DESI DR3,
and PolyChord — **THE ZERO-PARAMETER EVIDENCE RUN is IN PROGRESS as of 2026-07-13** — ε, A_s, n_s,
and z_on all STATED (derived/profiled, statuses in the DEPENDENCY_TREE), no Occam
shelter, full exposure; the sampled-ε referee deferred by design. This file
inherits the verdicts.*

## Sources
Full references in [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md). This file leans on: [Gross1961]/[Pitaevskii1961] (Eq. 1), [Kibble1976]/[Zurek1985] (the winding), [HartChluba2020]/[SekiguchiTakahashi2021] (the varying-m_e ↔ H₀ mechanism), [CLASS2011]/[cobaya2021]/[Planck2018]/[Riess2022] (the pipeline and data), [Volovik2003]/[BerezhianiKhoury2015] (the nearest prior art).
