# PRTOE in Three Equations

The model’s dark-energy scale is

$$\rho_\Lambda^{1/4} = \tfrac{9}{2}\,\alpha^4\,\tau\,m_e$$

— vacuum-occupancy binding energy, built from α⁴ and a temperature tied to the electron. Every factor is sourced except τ = T_c/m_e, which is where the claim now stands.

τ comes from the Koide sector only (no cosmology). The circulant kernel fixes its modulus through Parseval: Q = 2/3 forces |f₁/f₀| = 1/√2, so

$$\tau = \tfrac12\ln 2 \quad\Rightarrow\quad T_c \approx 177\,\mathrm{keV}$$

and ρ_Λ¼ lands on the observed dark-energy scale. That path starts from Q, a lepton-mass fact known to ~10 ppm, via an exact identity ([PRTOE_koide_relation.md](PRTOE_koide_relation.md)).

Treat this as an **existence** claim, not a precision one. The chain gives 2.2599 meV vs observed 2.25, but the composite quartic sits at λ = 26–46, above the control edge λ\* = 22.41, so the LHY correction is uncontrolled (formally 5.4–9.8% on ρ_Λ¼; the next term in the series is already larger).

The price is one hypothesis: charged-lepton √m are thermally populated (what Q = 2/3 says — variance of √m equals mean squared, the Boltzmann second moment, holding to 18 ppm). The referee is one lattice number: T_c/√σ for SU(2) with N_f = 3 — the same non-perturbative job the radiative band needs. **0.34657 supports the kernel and the DE prediction; 0.34506 kills both.**

Claim conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Full derivation: [PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md). Map: [PRTOE_INDEX.md](PRTOE_INDEX.md).

This note is the short form for a physicist who wants the math without the whole repo. The equations are short; the numbers inside them are not.

---

## Equation 1 — Substrate

One complex scalar (a cosmological superfluid) replaces separate dark matter and dark energy:

$$i\hbar\,\partial_t \psi = \left[-\frac{\hbar^2}{2m}\nabla^2 + \lambda|\psi|^2\right]\psi$$

- **Condensate ground state** supplies the w = −1 component (dark energy as the medium’s zero-point sector). Its scale is the vacuum-occupancy binding energy ρ_Λ¼ = ½ α_c² M₂. With τ from the Koide kernel: **2.2599 meV vs measured 2.25 (+0.44%)** — existence, not precision (quartic past control; see above). Structure: M₂ = α² T_c; α_c = 3α is under test. Path: m_e → T_c → M₂ → ρ_Λ (see the cosmological-constant document).
- **Excitations** are the dark matter: radiation-like above z_on, CDM-like below — one fluid, two eras (the dCDF sector in CLASS).
- **Phase winds** on a compact axis: θ(x) = 2π n x/L, n ∈ ℤ (Kibble-generated, topologically protected). That integer sources the anisotropy family: ℓ ∼ 130 comb (P-029), ε-dipole (P-024), isocurvature line (P-031) — one shared axis.

## Equation 2 — Coupling to known physics

The condensate shifts fermion masses by one universal fraction above its condensation temperature:

$$m_f(z) = m_f^0\left[1 + \varepsilon\, f(T/T_c)\right], \qquad T_c \approx 177\ \mathrm{keV}$$

- f is a **ramp**: ≈1 early, →0 after the transition (shape computed, not chosen; nothing here is a pure step).
- ε ≈ 1.24% is the whole modification to known physics: heavier electron at recombination → earlier decoupling → smaller sound horizon → CMB re-fit at H₀ ≈ 69.9 instead of 68.2 (Hubble-tension path, thread 11).
- Implemented in CLASS against full Planck likelihoods. Current Bayesian evidence vs ΛCDM: Δln Z ≈ +2.6 (Laplace; marginal and SH0ES-conditional). Nested sampling is unaffordable on current hardware and waits for cluster time.
- The same ε (one amplitude, window-specific activation: OFF at BBN freeze-out, ON below T_c; see the ε-epoch table in the fingerprint file) is owed everywhere at its epoch weights: BBN, radio-band ratios, de-biased Σm_ν, Koide invariance, underground nulls — the fingerprint lattice (thread 13).

## Equation 3 — Decomposition

ε is not a free fit parameter; it decomposes:

$$\varepsilon = c \cdot \bar{f} \cdot \alpha_c = \tfrac{9}{10} \times \tfrac{2}{\pi} \times 3\alpha = \tfrac{27\alpha}{5\pi} = 1.2543\%$$

against the sky’s fitted ∼1.24%. Three ε values appear in the repo on purpose:

| value | meaning |
|---|---|
| 1.232% | production-chain fit |
| ≈1.24% | posterior-era rounding |
| 1.2543% | derived stack above |

Gap between fit and derivation ≈1.8% of the value; measurements decide.

**How not to grade that gap.** Use the chain posterior, `varying_me` = 1.0126 ± 0.0041 (ε = 1.26 ± 0.41%), which puts 1.2543% near the centre. Do **not** use ±0.0079% from the concordance joint in the table below: that joint already folds in the derived stack, so it cannot test the stack. Against that joint you get a fake ≈1.8σ. Caveats: the posterior is from a chain with R−1 ≫ 0.05 (not quotable), and the evidence run is the definitive statement, not this note.

- **c = 9/10** — counting fraction (assumed). Count is (N−1)/N over the universal charged-fermion roster: 9 charged species + the zero-point seat. Not the leptophilic subset (that drops quarks and cannot reach 9/10). Democratic-9 (9/10) vs neutrino-inclusive 12/13 is settled by the dark-energy–neutrino tie: ρ_Λ¼ = m_ν,lightest is a lock only if the lightest mass is **direct-Majorana** (m₁ ≈ μ = 2.25 meV), seating the neutrino on the tenth channel ([PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md)) → **9/10**. Inverse-seesaw would make the meV match a tuning of two unrelated scales, not a lock.

  Equal weights are **not** forced by gravity’s blindness: an energy-reading coupling weights by energy over every field, not one share per charged species. Charge both selects and weights: Σ N_c Q² over the charged nine is **8**, so c = 8/9 = 0.889; if the neutral seat then weighs zero, c = 1, which the counting argument forbids. **No single criterion forces 9/10** — it is a counting assumption the data can confirm ([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §1). The ε-blind ensemble does not pick: 8/9 is 0.30σ from 9/10 at its width. Standing position for the DE prediction: **9/10, conditional on the tie as lock and equal weights**; independent check is the f̄ ensemble / α_c chain (P-2026-040).

- **f̄ = 2/π = 0.63662** — derived: winding time-average ⟨|cos|⟩ from many-turn equidistribution; coupling form data-selected (P-2026-041). The winding sim’s 0.635 ± 0.026 confirms it (+0.3%); it is not the source of f̄.

- **α_c = 3α** — pre-registered bet (P-2026-040), on the record before the α_c chain converges; ~2.3% above where current data point. Falsifiable; not retrofit.

If those three factors hold, the fixed-ε evidence run is a **zero-extra-parameter** rival to ΛCDM (no Occam penalty). Until then the claim is conditional.

---

## Stated stack (under test)

Numbers stated before the data grade them:

| quantity | stated value | provenance | grade |
|---|---|---|---|
| ε | 1.2403 ± 0.0079% | concordance joint of fit and stack | conditional (three referees) |
| A_s | **2.088×10⁻⁹ frozen**; closed form (α_c/4πk)³ = **2.081×10⁻⁹** (−0.34%) | shot-noise form; k = ln(1+π/2α_c)/π | candidate — exposed |
| n_s | 0.9677 = 1 − 2/ln(T₀/k*) k-local; predicted running α_s = −5.2×10⁻⁴ (run uses 0.9641, k-independent form — consistency check) | modulation map on verified k_UV = T₀ | mechanism candidate |
| z_on | **4.03×10⁷** (log₁₀ 7.605) | H = m on m = 2.24×10⁻²⁰ eV. “Confirmed independently” wording withdrawn 2026-07-28 (ξ ≡ ħ/(m c_s) is defined from m; Schive unresolved; superradiance band is an exposure). Mass clears M87\* (2.9–4.6)×10⁻²¹ exclusion; live falsifier at P-2026-034 where λ-quench shield fails re-derivation by 84 decades | derived identity |
| *(evidence run setting)* | 3.5619×10⁷ | profiled freeze, 0.053 dex below the identity → m = 1.75×10⁻²⁰, ~28% off all three mass checks | **tests this point, not the identity** |
| w | −1 exactly, no thaw | ground state (P-2026-018) | derived |
| Σm_ν | 61.4 meV, normal ordering | m₁ = ρ_Λ¼ + measured splittings; ordering data-selected, not fixed by P-2026-012 (ANN-2026-025) | recorded, not a discriminator (~2.6 meV above m₁ = 0 floor vs ~20 meV resolution). Testable content is m_ββ |
| T_c | **177.10 keV** (τ = ½ln2 = 0.34657) | Koide kernel; no cosmology. 193 keV = perturbative cross-check; 179 keV = BBN pipeline code value | candidate — lattice T_c/√σ for SU(2), N_f = 3 |
| H₀ | 69.9 CMB re-fit (output); 69.70 joint best-fit; 69.82 evidence run | falls out of re-fit | **provisional** — older chains predate standing YHe treatment; may move |

ΛCDM uses six free parameters on the same data; this stack uses **zero**. Retreat is not an option if the sky refuses the numbers. That totality is what the evidence comparison grades.

---

## Why the rest of the repo exists

What does not fit in three lines is the chain *inside* the symbols: why 9/10 (counting), why 2/π (winding history), why 177.10 keV (confining chiral ratio τ · m_e — [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md); 193 keV is never the keying value), why 3α (microphysics, bet-registered). Those are outputs of the field’s history, not axioms. Equations are three lines; receipts are the repository.

**Status (2026-07-20).** Everything above is conditional on one root: the no-bare mechanism’s unconditionality (M3), named as an assumption. Deciders: α_c MCMC (grades 3α and the c-roster), f̄ ensemble, DESI DR3, and the zero-parameter evidence run with ε, A_s, n_s stated in advance. **z_on exception:** the evidence config freezes 0.053 dex off the model’s onset identity, so it grades a nearby point. **Evidence number is Laplace from MCMC**; nested sampling waits on cluster time (~9.8 h/iteration → ~163 days to first checkpoint). Chain convergence is what stands between the model and the headline evidence claim.

## Sources

Full list: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md). This file uses: [Gross1961]/[Pitaevskii1961] (Eq. 1), [Kibble1976]/[Zurek1985] (winding), [HartChluba2020]/[SekiguchiTakahashi2021] (varying-m_e ↔ H₀), [CLASS2011]/[cobaya2021]/[Planck2018]/[Riess2022] (pipeline and data), [Volovik2003]/[BerezhianiKhoury2015] (nearest prior art).
