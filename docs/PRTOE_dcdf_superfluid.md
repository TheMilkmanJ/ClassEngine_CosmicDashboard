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

- the residual magnitude **from this sector's own dynamics** (it is supplied by the Koide-kernel
  route — see §5 and the note there; what fails here is the fluctuation–dissipation closure —
  FDT here is ohmic and misses);
- the exact link between the condensate floor and the bounce dynamics (**bounce not derived**).

*(The matter-asymmetry sign correlation from the genesis draw is **not** still open: the joint
draw was run 2026-07-20 and finds θ̇ and n independent — the cross-messenger lock is void, not
pending; see [PRTOE_igmf_helicity.md](PRTOE_igmf_helicity.md) and §3 below.)*

So the dCDF is already mostly derived structurally. The open residue is the residual magnitude
and the bounce junction, not the existence of the component itself.

---

## 1. What it is

Cosmological superfluid unifying DM and DE. Ultralight mass **m ≈ 2.24×10⁻²⁰ eV** (onset clock). Ground state **w = −1** (de Sitter floor). Excitations radiation-like above H = m (z ~ 4×10⁷), dust-like below — **one fluid, two eras**. Implemented in CLASS (`use_dcdf`, dispersion rad phase, optional conversion/thaw).

## 2. Structure

**s-wave binding, selected by data.** Coulombic two-body levels: s-wave gives **2.2599 meV** vs observed 2.25; p-wave −75%; f-wave −94% ([PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md)). Agreement requires ℓ = 0.

**Analogy (not identity):** ³He-A pairs p-wave because of a baryonic hard core. A medium without a fermionic hard core leaves s-wave open. Finiteness balance selects dark **SU(2)** with bosonic diquarks (pseudo-real fundamental) — canonical diquark-BEC / BCS–BEC language (P-2026-048; lattice T_c/√σ still owed).

**What this identity does not source.** Two claims once rested here and rest elsewhere:
- **The chirality** — parity-odd signatures (GW handedness, IGMF helicity, LSS parity, the AD
  matter bias) are signed by the **genesis winding integer n**, not by a pairing channel. The
  three-membered family (matter / magnetism / metric) is one integer:
  [PRTOE_igmf_helicity.md](PRTOE_igmf_helicity.md) (P-2026-028, sign(helicity_B) = sign(n)),
  [PRTOE_lss_parity.md](PRTOE_lss_parity.md), [PRTOE_baryogenesis.md](PRTOE_baryogenesis.md),
  [PRTOE_gravitational_waves.md](PRTOE_gravitational_waves.md).
- **The generation count** — forced by **Pauli finiteness**: str[k₁] = 16·N_gen − 48 = 0 ⟹
  **N_gen = 3** uniquely, pure heat-kernel species counting with no nodes and no angular momentum
  ([PRTOE_induced_gravity.md](PRTOE_induced_gravity.md) thin attach;
  [PRTOE_quantum_gravity.md](PRTOE_quantum_gravity.md) §5.2–5.3 full hub; P-2026-045, conditional on
  ξ_H = 1/6). SM alone: **−1/2** (Visser) / **−3** (Weyl deficit).

Literal He-3-as-medium: **retired** (failures ledger).

## 3. Charge: abundance + asymmetry

Carries the dark **abundance/asymmetry** charge (the AD-spiral, "charge = abundance"). The genesis
draw is **a candidate source of the matter asymmetry** (why the hot baryonic pour contains matter at
all) — candidate at the magnitude/route grade, not at the absolute-sign grade. *"The superfluid
fathered the visible universe"* = this claim at that grade. The **AD-direct rectification** that
would have locked matter's temporal rotation θ̇ to the spatial winding n has been run
([working_logs/T14_igmf_helicity_owed.md](working_logs/T14_igmf_helicity_owed.md)): the two signs
are independent, so the cross-messenger lock is void rather than unbuilt.

**The temporal factor is settled and it is a coin.** The genesis tilt's reflection symmetry
θ → π/2 − θ leaves release-at-rest and the uniform prior invariant while flipping L = R² θ̇, so the
roll generates rotation with no preferred sense — verified to machine precision at every tilt
strength. So the sector cannot name which handedness means matter *a priori*. The **correlation**
has since been computed: one draw carrying both the winding and the rotation was built and run
(#154, 2026-07-20) and finds the two signs **independent** — joint correlation −0.06 to +0.09
against a ±0.13 floor. The absolute-handedness question is therefore closed as *void*, not pending.

## 4. Light

Light as massless Goldstone of the condensate (load-bearing for “α is the medium’s coupling” in hierarchy pairing). EM-neutral → transparent → no optical birefringence. Detail: [exploratory/PRTOE_light.md](exploratory/PRTOE_light.md).

## 5. What it does not close

- **DE value** does not forward-close from this sector’s FDT (ohmic, ~21 dex miss). Sub-ohmic SOC is **not** a DE self-tuning escape (belongs to DM channel). Magnitude **is** supplied at existence grade by Koide-kernel ρ_Λ¼ = (9/2)α⁴ T_c = 2.2599 meV — **one route supplies, this sector’s own route fails; both belong in the same sentence.**
- **w = −1** exact and derived for the floor; optional Route-D thaw is a separate registered fork (DESI DR3).

## Dead ends / sources

Failures: [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md). v4/v5 derivation docs; CC file; [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md).

---

## Claims ledger & discipline (2026-08-03) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Two-era dark superfluid; exact w = −1 floor | **derived** (structural) | §0–1; CLASS use_dcdf | Route-D thaw is separate fork |
| 2 | Onset clock H = m; radiation→dust crossover | **derived** | §1; background.h | m rides roster-trial / α_c |
| 3 | s-wave channel selected by binding data (2.2599 meV) | **derived** (data selection) | §2; CC file | p/f-wave excluded by miss |
| 4 | Residual DE magnitude from *this* sector’s FDT | **failed** (ohmic miss ~21 dex) | §5 | Magnitude supplied by Koide route instead |
| 5 | Bounce junction / link to floor dynamics | **OPEN-BLOCKED** | §0 | **OPEN-THEORY:** bounce not derived |
| 6 | Chirality from genesis n, not pairing channel | **interpretation** (reseat) | igmf_helicity; lss_parity | Joint draw: θ̇ ⊥ n (void lock) |
| 7 | Light as massless Goldstone of condensate | **candidate** | §4; [exploratory/PRTOE_light.md](exploratory/PRTOE_light.md) | Load-bearing *identification* for α = medium coupling; bare α still OPEN-BLOCKED on light ledger |
| 8 | AD absolute-handedness lock void (independent signs) | **machine-backed** | #154 joint draw | Correlation −0.06…+0.09 vs ±0.13 |
| 9 | CLASS `(.)w_dcdf` history bare/conv/thaw/both through onset | **machine-backed** | [working_logs/_runs/w_a_onset_20260803/REPORT.md](working_logs/_runs/w_a_onset_20260803/REPORT.md); `scripts/w_a_onset_truth.py` | Barotropic dust→DE only; **not** the #17 rad-onset ramp |
| 10 | `(.)w_dcdf` **blind to thaw** (instrument) | **machine-backed** | [working_logs/_runs/debt_p042_d2_cures_20260803/REPORT.md](working_logs/_runs/debt_p042_d2_cures_20260803/REPORT.md) | Thaw column in w_dcdf truth table **VOID**; do not quote thaw from w_dcdf |
| 11 | Onset template R(x)=x²/(1+x²) centers + analytic log10 bias vs H=m | **machine-backed** / desk | [working_logs/_runs/debt_p042_template_20260803/REPORT.md](working_logs/_runs/debt_p042_template_20260803/REPORT.md) | Equipartition +0.2386 dex; full onset-likelihood bias **OPEN-BLOCKED** |
| 12 | Pre-onset high-z budget is photons/ν not w_dcdf | **machine-backed** | debt_p042_d2_cures high-z table; P-053 ΔN_eff | P-042 pre-onset w=1/3 referee = dark-radiation budget |

**Non-claims:** not DE precision from FDT; not chirality source; literal He-3 medium retired; not thaw physics from `(.)w_dcdf`; not onset-likelihood bias closed.

**Triage:** elevate-in-place. Physics ceiling: structural derived; residual magnitude / bounce **OPEN-BLOCKED**; D2 instrument/template **partial paid**.
