# The radio lattice — five bands, one ε, locked ratios

Glossary: [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md). Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Amplitude: [PRTOE_THE_AMPLITUDE.md](PRTOE_THE_AMPLITUDE.md).

Thread 12. Two registered predictions ride it (P-2026-022, P-2026-027) and one open candidate (P-029). Radio cosmology gains a correlated, ratio-locked multi-band fingerprint.

**Audience grade.** Weights are **derived** from atomic/plasma coefficients (four of five labeling-free). Pattern is a **registered bet** until dark-ages data exist. Synchrotron row is **convention-bearing** (fixed-field −1ε vs fixed-energy −3ε). Below z = 50: **nulls** (today’s constants). Do not claim a detection that does not exist.

---

## 0. Structure

Every radio observable depends on atomic physics through a different power of the electron mass. A universal m_e shift (the electron-coupled scalar, +1.2543% above the transition) therefore marks each band with a known, different weight — a lattice of correlated shifts with fixed ratios:

| observable | ε-weight | physics |
|---|---|---|
| 21cm hyperfine (and D 92cm) | **+2ε** | ν ∝ α⁴m_e²/m_p |
| radio recombination lines | **+1ε** | Rydberg ∝ m_e |
| plasma dispersion (FRB/pulsar DM) | **−1ε** | the dispersion constant e²/2πm_e c ∝ 1/m_e, so an inferred DM shifts by −ε at fixed electron column *(the plasma frequency itself, ω_p ∝ m_e^−½, carries half this weight — the observable is the delay, not ω_p)* |
| synchrotron characteristic ν | **−1ε** | ν_c ∝ γ²eB/m_e — the **fixed-field** reading: B and the emitting Lorentz factor γ held, so the weight is the coefficient’s alone *(the **fixed-energy** labeling instead lets γ = E/m_e c² ∝ 1/m_e float, carrying the same expression to −3ε — this row is the table’s one convention-bearing entry, and the labeling must be declared before it is read)* |
| Faraday rotation | **−2ε** | RM ∝ n_e B/m_e² |

## 1. Why the lattice beats any single measurement

A single anomalous shift in any band is systematics until proven otherwise. The electron-coupled scalar predicts the pattern: **+2 : +1 : −1 : −1 : −2**, simultaneously, in the same epochs/sightlines — with the D-to-H frequency ratio exactly preserved (4.338649 at every z — the P-027 two-line lock, which tests **universality**: α and m_e enter the two hyperfine lines identically and both cancel from their ratio, so the lock excludes *species-dependent* shifts and does **not** by itself distinguish a varying m_e from a varying α — that separation is the five-band pattern’s job) and the modulation comb (P-029, fundamental ℓ₁ ≈ 3.1n ≈ 31–94) ruled along the same axis as the ε-dipole (P-024).

Generic new physics moves these bands independently; varying-α models move them with different weights (α enters the 21cm line at α⁴ but dispersion not at all) — **the lattice discriminates that scalar not just from ΛCDM but from every other varying-constant hypothesis, by arithmetic.**

## 2. Instruments and epochs

The shifted regime is z > 50: the dark ages (the D/H referee against the CMB backlight; the lunar-farside band, driven by the terrestrial RFI reality) and cosmic dawn’s edge structure (P-022’s three-verdict shape: the edge frequency mapping shifted +2.5%; its retired A/B edge-shape fork is recorded in [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md)).

Below z = 50 the lattice predicts nulls (today’s constants are the lab’s) — quasar-epoch drift searches must stay quiet (they have).

## 3. Scope

- Signal sizes are hard: dark-ages radio is a lunar-farside program. The BipoSH/isotropy-estimator instrument is **built** (`scripts/biposh_estimator_pass.py`, 2026-07-28; shared with the low-ℓ thread); what remains is **data application** (pattern-frame \(a_{\ell m}\)), which is external, not a missing desk check.
- The lattice’s weights assume the fundamental-mass-philia structure (graded) — a measured pattern **violating** the ratio table (e.g., +2ε in 21cm with an unshifted RRL row) kills the electron-coupled scalar’s universality outright: the lattice is its own executioner.
- Four of the five rows are labeling-free: 21cm, RRL, dispersion and Faraday are line frequencies and path integrals, whose held-fixed inputs (n_e, B, the electron column) are non-atomic, so their weights read straight off the coefficients. The synchrotron row is the exception — its ν_c carries a γ² whose scaling depends on how the emitting population is labeled (fixed-field −1ε vs fixed-energy −3ε, table above). **The executioner clause therefore binds on the four labeling-free rows**; synchrotron enters the pattern only once an analysis states which labeling it used.

## Sources

[Field1958] (the hyperfine line’s m_e dependence), [RybickiLightman1979] (the dispersion and Faraday coefficients), [Bowman2018] (the cosmic-dawn edge), [Cooke2018] (the deuterium pole). Full list: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).
