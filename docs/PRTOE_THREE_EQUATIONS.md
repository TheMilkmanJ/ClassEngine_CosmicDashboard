# PRTOE in Three Equations

> **THE FLAGSHIP CLAIM, AND ITS GRADE.** The dark-energy scale is
> **ρ_Λ¼ = (9/2)·α⁴·τ·m_e** — the vacuum-occupancy binding energy, α⁴ times a temperature tied to
> the electron. That structure is what makes it predictive rather than descriptive, and every factor
> in it is sourced except τ = T_c/m_e, which is where the whole claim now lives.
>
> **τ is sourced by the Koide sector, and nothing cosmological enters.** The circulant kernel fixes
> its own modulus through Parseval: Q = 2/3 forces |f₁/f₀| = 1/√2, hence
>
> > **τ = ½ln2 = 0.34657 ⟹ T_c = 177.10 keV ⟹ ρ_Λ¼ = 2.2599 meV against the observed 2.25 — +0.44%**
>
> That chain descends from Q, a lepton-mass fact measured to ten parts per million, through an exact
> identity ([PRTOE_koide_relation.md](PRTOE_koide_relation.md)).
>
> **Read the +0.44% as existence, not precision.** The claim it carries is that the chain lands on
> the observed scale with nothing cosmological in it. It is not a claim on the decimal places: the
> composite quartic maps to λ = 26–46, the whole band above the control edge λ\* = 22.41, so the LHY
> correction is uncontrolled at this order — formally 5.4–9.8% on ρ_Λ¼, with the next term of the
> same series already larger.
>
> **Grade: candidate. Its price is one hypothesis** — that the charged-lepton √m are thermally
> populated, which is what Q = 2/3 asserts (it says the variance of √m equals its mean squared, the
> Boltzmann second moment, holding to 18 ppm on the measured masses). **Its referee is one number:**
> a lattice T_c/√σ for SU(2) with N_f = 3 — the same non-perturbative treatment the radiative band
> needs, so the λ and τ gates are one job. **0.34657 crowns the kernel and the dark-energy
> prediction together; 0.34506 kills both.**


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
 $\rho_\Lambda^{1/4} = \tfrac{1}{2}\alpha_c^2 M_2$. With τ sourced by the Koide kernel this is
 **2.2599 meV against the measured 2.25 — +0.44%**, an existence claim rather than a precision one
 (the quartic sits past perturbative control — head of this file); the structure $M_2 = \alpha^2 T_c$ carries it,
 and $\alpha_c = 3\alpha$ is under test. From the dyad's condensation temperature
 ($m_e \to T_c \to M_2 \to \rho_\Lambda$); see the cosmological-constant document.)
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

$$m_f(z) = m_f^0\left[1 + \varepsilon\, f(T/T_c)\right], \qquad T_c \approx 177\ \text{keV}$$

- $f$ is a **ramp**: $\approx 1$ in the early universe, $\to 0$ after the transition
 (nothing in this model is a step; the ramp's shape is computed, not chosen).
- $\varepsilon \approx 1.24\%$. That is the **entire modification to known physics**: a
 heavier electron at recombination → earlier decoupling → smaller sound horizon → the CMB
 re-fits at $H_0 \approx 69.9$ instead of $68.2$ (the Hubble-tension mechanism, thread 11).
- Implemented in CLASS, run against full Planck likelihoods; the Bayesian evidence currently
 favors it over ΛCDM at $\Delta\ln Z \approx +2.6$ (Laplace approximation; marginal and
 SH0ES-conditional; the definitive nested-sampling comparison is unaffordable on the hardware
 available and waits for cluster time).
- The same $\varepsilon$ — ONE amplitude passed through window-specific activation (OFF at
 BBN freeze-out, ON below $T_c$; the ε-epoch table in the fingerprint file governs) — is
 then owed everywhere at its epoch weights: BBN's windowed pattern,
 the radio-band ratios, the de-biased $\Sigma m_\nu$, the Koide invariance, the underground
 nulls — the fingerprint lattice (thread 13). One lever, many windows, no exits.

## Equation 3 — The decomposition (what makes it a theory rather than a fit)

$\varepsilon$ is not tuned; it decomposes:

$$\varepsilon = c \cdot \bar{f} \cdot \alpha_c = \tfrac{9}{10} \times \tfrac{2}{\pi} \times 3\alpha = \tfrac{27\alpha}{5\pi} = 1.2543\%$$

against the sky's fitted $\sim 1.24\%$ — zero dials end to end. (Three ε values appear in
this repo and differ deliberately: **1.232%** = the production-chain fit; **~1.24%** = the
posterior-era rounding; **1.2543%** = the derived stack above. The gap between fit and
derivation is ~1.8% *of the value* — and the running measurements decide.)

> **Which width that gap is "inside" is worth stating, because the wrong one is easy to reach for.**
> The measurement's own width is the chain posterior, `varying_me` = 1.0126 ± 0.0041 — an ε of
> 1.26 ± 0.41% — which puts the derived 1.2543% essentially at its centre. **It is *not* the
> ±0.0079% attached to the concordance joint in the stack table below**: that joint combines the fit
> *with the derived stack*, so it contains the number under test and cannot be used to test it.
> Reading the derived value against that figure returns a spurious ≈1.8σ. Two honest caveats attach:
> the posterior above comes from a chain at R−1 ≫ 0.05 and is **not quotable**, and the definitive
> statement is the evidence run's, not this one's.

- $c = 9/10$: a **counting fraction**, and the decomposition's assumed factor. The count is
 (N−1)/N over the **universal charged-fermion roster** — 9 charged species + the zero-point's own
 seat → $c = 9/10$ — **not** the dyad's leptophilic subset, which drops the quarks and cannot
 reach the count. Which universal-charged reading holds (democratic-9 → 9/10, or the
 neutrino-inclusive 12/13) is settled by the dark-energy–neutrino tie: ρ_Λ¼ = m_ν,lightest is a
 genuine lock *only if* the lightest neutrino mass is **direct-Majorana** (m₁ ≈ μ = 2.25 meV),
 which seats the neutrino on the medium's own tenth channel (the seat operator is exhibited with
 its UV form — [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md)) → **9/10**; the 12/13 reading
 needs an inverse-seesaw light mass, which demotes the meV coincidence from a lock to a tuning of
 two unrelated scales.
 **What the count does not have is a licence for its *weights*.** Equal share per channel was
 read off gravity's blindness, and blindness does not deliver it: a coupling that reads energy
 rather than identity weights by energy over every field present, not one share apiece over nine
 chosen ones — and the roster is chosen by **charge**, an identity-reading criterion. Carried
 through consistently, charge weights as well as selects: Σ N_c Q² over the charged nine is
 exactly **8**, giving c = 8/9 = 0.889, and if the neutral seat then takes weight zero the count
 returns c = 1, which the census excludes. **No single criterion returns 9/10**, so the value is
 a counting assumption the data confirms rather than one the framework forces
 ([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §1). The ε-blind ensemble is the check and
 it does not adjudicate: 8/9 sits 0.30σ from 9/10 at its width, inside its own error bar.
 So the value is **9/10, conditional on keeping the tie a lock and on the equal-weight
 assumption** (the flagship position); the empirical f̄ ensemble / α_c chain (P-2026-040) remains
 the independent check.
- $\bar{f} = 2/\pi = 0.63662$: **derived** — the winding's time-average $\langle|\cos|\rangle$, forced by many-turn equidistribution, with the coupling form data-selected (P-2026-041). *(The winding sim's $0.635 \pm 0.026$ is the output that **confirms** it to +0.3%, not the value of $\bar{f}$ — the high-statistics ensemble is the check, not the source.)* **Derived — not a parameter, and not
 a simulation output.**
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
| A_s | **2.088×10⁻⁹ frozen**; the closed form (α_c/4πk)³ = **2.081×10⁻⁹** — it lands **−0.34%** | the shot-noise closed form; k = ln(1+π/2α_c)/π | candidate — deliberately exposed; the corpus's boldest standing claim |
| n_s | 0.9677 = 1 − 2/ln(T₀/k*) k-local, predicted running α_s = −5.2×10⁻⁴ (the executed run value 0.9641 is the banked k-independent form, now consistency-check grade) | the modulation map: envelope × shot on the verified k_UV = T₀ anchor; the 2 = amplitude-squared | mechanism candidate (exhibited) |
| z_on | **4.03×10⁷** (log₁₀ 7.605) | the H = m identity on m = 2.24×10⁻²⁰ eV, the mass confirmed independently by ξ = 402 AU, the Schive core radii, and the superradiance window — which the mass **clears** (M87\*'s (2.9–4.6)×10⁻²¹ exclusion sits below it), though the same physics carries the model's most live falsifier at P-2026-034's populated band, where the λ-quench shield fails re-derivation by 84 decades | derived identity |
| *(the evidence run's setting)* | 3.5619×10⁷ | a profiled freeze, 0.053 dex below the identity — it implies m = 1.75×10⁻²⁰, which misses all three mass checks by ~28% | **inconsistent with the model's own mass; the run tests this point, not the identity** |
| w | −1, exactly, no thaw | ground state (protected zero; P-2026-018) | derived |
| Σm_ν | 61.4 meV, normal ordering | the m₁ = ρ_Λ¼ tie plus measured splittings; **the ordering is data-selected, not fixed by P-2026-012** (ANN-2026-025) | recorded, but **not a discriminator** — it sits 2.6 meV above the m₁ = 0 floor against ~20 meV planned resolution. The testable content is m_ββ |
| T_c | **177.10 keV** (τ = ½ln2 = 0.34657) | the Koide kernel's modulus through Parseval — no cosmological input; 193 keV is the perturbative cross-check, 179 keV the superseded rounding | candidate — referee is a lattice T_c/√σ for SU(2), N_f = 3 |
| H₀ | 69.9 CMB re-fit (output, not input); 69.70 joint best-fit; 69.82 evidence run | falls out of the re-fit | **provisional** — measured on chains predating the `YHe` correction (2026-07-17); the running job carries the fix and the value may move |

ΛCDM meets the same data with six free parameters; this stack meets it with **zero** —
whatever the sky refuses, the model has nowhere to retreat. That totality, not any
single row, is the claim under adjudication in the nested-sampling run now executing.

---

## The closing note (why the repo exists)

What does not compress is the derivation chain *inside* the symbols — why $9/10$
(the census mechanism), why $2/\pi$ (the winding history from first genesis), why
$177.10$ keV (the confining chiral ratio $\tau \cdot m_e$ — [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md); 193 keV is the perturbative cross-check, **never the keying value**), why $3\alpha$ (basement-owed, bet-registered).
Those numbers are outputs of the field's history from its initial conditions, not axioms.
The equations are three lines; the receipts are the repository.

*Status (2026-07-20): every derivation above is conditional on one root — the no-bare mechanism's
unconditionality (M3), an assumption named as such. The deciders: the α_c MCMC (grades $3\alpha$ and
the $c$-roster), the $\bar{f}$ ensemble, DESI DR3, and the zero-parameter evidence run — with ε, A_s
and n_s stated in advance (derived or profiled, statuses in the DEPENDENCY_TREE), no Occam shelter,
full exposure; the sampled-ε referee deferred by design. **z_on is the exception and is stated as
such above:** that configuration is frozen 0.053 dex off the model's own onset identity, so it grades
a nearby point rather than the stated one. **And the evidence number is a Laplace estimate from
MCMC**, with nested sampling waiting on cluster time: on this hardware a nested iteration costs 9.8 h,
which is 163 days to a first checkpoint. So the chains' own convergence is what stands between the
model and its headline evidence claim. This file inherits the verdicts.*

## Sources
Full references in [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md). This file leans on: [Gross1961]/[Pitaevskii1961] (Eq. 1), [Kibble1976]/[Zurek1985] (the winding), [HartChluba2020]/[SekiguchiTakahashi2021] (the varying-m_e ↔ H₀ mechanism), [CLASS2011]/[cobaya2021]/[Planck2018]/[Riess2022] (the pipeline and data), [Volovik2003]/[BerezhianiKhoury2015] (the nearest prior art).
