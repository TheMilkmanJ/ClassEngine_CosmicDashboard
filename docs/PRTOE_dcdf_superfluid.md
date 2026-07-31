# dCDF — the superfluid piece (identity file)

Glossary: [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md). Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Derivation: [exploratory/PRTOE_v4_dCDF_derivation.md](exploratory/PRTOE_v4_dCDF_derivation.md). Code: [PRTOE_CODE_MANIFEST.md](PRTOE_CODE_MANIFEST.md).

One of three dark fields — with the electron-coupled scalar ([PRTOE_dyad_gas.md](PRTOE_dyad_gas.md)) and the Majoron ([PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md)).

## 0. Derived core / open residue

**Derived / forced**

- Two-era dark superfluid; exact **w = −1** floor (p = −ρ_inf)
- Onset clock H = m; radiation → dust crossover
- s-wave channel selected by binding data
- Finite quartic floor (no-singularity support scale)
- Topological / winding side carries chirality and axis-family information

**Open**

- Residual DE *magnitude from this sector’s own* fluctuation–dissipation (supplied elsewhere by Koide-kernel route; FDT here is ohmic and misses)
- Matter-asymmetry sign correlation from genesis draw
- Exact link from condensate floor to bounce dynamics (**bounce not derived**)

Structurally the dCDF is mostly derived. Residue is magnitude/sign/bounce, not existence of the fluid.

---

## 1. What it is

Cosmological superfluid unifying DM and DE. Ultralight mass **m ≈ 2.24×10⁻²⁰ eV** (onset clock). Ground state **w = −1** (de Sitter floor). Excitations radiation-like above H = m (z ~ 4×10⁷), dust-like below — **one fluid, two eras**. Implemented in CLASS (`use_dcdf`, dispersion rad phase, optional conversion/thaw).

## 2. Structure

**s-wave binding, selected by data.** Coulombic two-body levels: s-wave gives **2.2599 meV** vs observed 2.25; p-wave −75%; f-wave −94% ([PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md)). Agreement requires ℓ = 0.

**Analogy (not identity):** ³He-A pairs p-wave because of a baryonic hard core. A medium without a fermionic hard core leaves s-wave open. Finiteness balance selects dark **SU(2)** with bosonic diquarks (pseudo-real fundamental) — canonical diquark-BEC / BCS–BEC language (P-2026-048; lattice T_c/√σ still owed).

**Does *not* source**

- **Chirality** — parity-odd sky signatures signed by genesis winding n, not pairing channel.
- **N_gen = 3** — Pauli finiteness (str[k₁] = 0 for SM+3ν_R at ξ_H = 1/6). SM alone: **−1/2** (Visser) / **−3** (Weyl deficit). [PRTOE_quantum_gravity.md](PRTOE_quantum_gravity.md).

Literal He-3-as-medium: **retired** (failures ledger).

## 3. Charge: abundance + asymmetry

Carries dark abundance/asymmetry (AD-spiral language). Genesis draw is a **candidate** matter-asymmetry source; sign correlation unbuilt. Temporal rotation is a **coin** under reflection symmetry of the tilt — absolute matter handedness not named a priori.

## 4. Light

Light as massless Goldstone of the condensate (load-bearing for “α is the medium’s coupling” in hierarchy pairing). EM-neutral → transparent → no optical birefringence. Detail: [exploratory/PRTOE_light.md](exploratory/PRTOE_light.md).

## 5. What it does not close

- **DE value** does not forward-close from this sector’s FDT (ohmic, ~21 dex miss). Sub-ohmic SOC is **not** a DE self-tuning escape (belongs to DM channel). Magnitude **is** supplied at existence grade by Koide-kernel ρ_Λ¼ = (9/2)α⁴ T_c = 2.2599 meV — **one route supplies, this sector’s own route fails; both belong in the same sentence.**
- **w = −1** exact and derived for the floor; optional Route-D thaw is a separate registered fork (DESI DR3).

## Dead ends / sources

Failures: [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md). v4/v5 derivation docs; CC file; [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md).
