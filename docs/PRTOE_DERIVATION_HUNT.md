# The Open Derivations — the model's underived numbers and their current status

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*This document tracks the numbers the model has not yet derived from first principles, and where each one
currently stands. The finished derivations live in the topic documents (cited inline); this is the
working front. Status labels: **derived** (forced from the framework), **candidate** (a closed form
proposed, its referee pending), **estimate** (fixed at argument or profile grade), **input** (an
irreducible assumption, named as such).*

---

## 1. The amplitude ε and its decomposition

The single modification to known physics is a universal fermion-mass shift ε ≈ 1.24%, which decomposes as

$$\varepsilon = c \cdot \bar f \cdot \alpha_c .$$

| factor | value | status |
|---|---|---|
| **c** | 9/10 | **derived** — the census over the universal charged-fermion roster, selected over 12/13 by the dark-energy–neutrino tie (a genuine lock requires a direct-Majorana light neutrino mass, which seats the neutrino on the medium's tenth channel). The 8/9 charge²-weighted reading is excluded by the gravity-blind democratic rule. See [PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md). |
| **f̄** | 2/π ≈ 0.6366 | **candidate** — the winding average, identified as the mean-absolute-sinusoid in the many-turns limit; the closed form is forced in structure, two sub-conditions owed. The ensemble decides the value. The ε-blind ensemble gives c = 0.903 [0.867, 0.942], −0.08σ from 9/10. |
| **α_c** | 3α | **candidate (under test)** — a pre-registered value; the "3" is the transverse-projector trace of the induced loop (spatial dimension d = 3), with two field-theory pieces owed. The running α_c chain is the referee. |

The three ε values in the corpus differ deliberately: 1.232% (production fit), ~1.24% (posterior), 1.2543%
(the derived stack). The gap is inside the posterior width; the running measurements decide.

---

## 2. The dark-energy value

The dark-energy scale is a closed form whose only dimensionful input is the electron mass:

$$\rho_\Lambda^{1/4} = \tfrac{1}{2}\alpha_c^2 M_2 = \tfrac{9}{2}\alpha^4\,\tau\,m_e,\qquad \tau \equiv T_c/m_e .$$

- **Chain (self-consistent):** m_e → T_c → M₂ = α²·T_c = 9.53 eV → ρ_Λ¼ = 2.28 meV, a **genuine 1.5%
  prediction** against the observed 2.25 meV. The α⁴ scaling is derived; M₂ is derived from T_c (not
  selected). See [PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md).
- **τ = T_c/m_e ≈ 0.345 — derived:** it is the chiral-transition-to-string-tension ratio T_c/√σ ≈ 0.34–0.37
  of a QCD-like confining sector (pure glue, at 0.63, is excluded). The dark sector must carry light dark
  quarks (N_f ≥ 2).
- **T_c ≈ 179 keV — derived:** the non-perturbative confining chiral value (τ·m_e). The perturbative
  Coleman–Weinberg estimate (193 keV, log-ambiguous) is a 7%-consistent cross-check. This is the same
  scale BBN watches the ε-ramp switch at.
- **The one input:** the portal **√σ_dark = m_e** — the dark confining sector's scale equals the electron
  mass. This cannot be derived without abandoning τ ≈ 0.35 (a conformal sector that would fix √σ_dark = m_e
  gives the wrong τ; the QCD-like sector that gives τ carries its own scale). It is an **irreducible input**
  — the "meV whisper," ρ_Λ ~ α⁴m_e — but a **falsifiable** one (it predicts ~MeV dark states).

---

## 3. The dark sector

The confining sector that binds the dark energy is a **3-flavour, lepton-partnered confining vacuum at the
electron scale** (√σ_dark ≈ m_e). Its chiral condensate is the dyad (the electron-mass shifter); its three
flavours supply the "3" in α_c = 3α. It sets the dark-energy binding scale only — the dark matter remains
the medium's own ultralight excitations.

- **Cosmology (safe):** the ~MeV dark baryons cannot overclose. To be the dark matter they would need a
  dark asymmetry ~1700× the visible one; at any natural asymmetry they are ≤10⁻³ of it, and symmetric
  relics annihilate away (strong coupling).
- **Footprint (falsifiable):** the light dark states give **ΔN_eff ≈ 0.05–0.3** if the sector thermalised.
  Planck (N_eff = 2.99 ± 0.17) already excludes the late-decoupling / many-dof corners, so the portal must
  freeze out above the QCD scale (T_dec ≳ 1 GeV). CMB-S4 (±0.03) tests the survivor.
  (`scripts/tau_deconfinement.py`, `scripts/dark_neff.py`.)

---

## 4. The neutrino sector

- **Σm_ν ≈ 61.4 meV, normal ordering — recorded prediction**, from the tie ρ_Λ¼ = m_ν,lightest (the DE
  floor equals the lightest neutrino mass). Requires the Majorana mechanism. See
  [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md).
- **The spurion μ = 2.25 meV** — a soft lepton-number-breaking dimension-1 scale that sets both the
  dark-energy floor (ρ_inf = κ_V μ⁴) and the direct light neutrino mass (m_ν = κ_m μ), tie exact to 2.2%.
  The value of μ is **input** (undERIVED), equal to the electron-mass-anchored meV scale of §2.
- **v_L (the seesaw scale)** — two mutually exclusive corners (resonant → MeV, S4-armed; junction
  double-duty → ≥ GeV, S4-dark); the point value awaits the coupling λ′, and CMB-S4 is the corner-selector.

---

## 5. Induced gravity (no bare G)

Gravity is induced by the medium's one-loop content, with no fundamental Einstein–Hilbert term. See
[PRTOE_quantum_gravity.md](PRTOE_quantum_gravity.md).

- **The keystone, str[k₁] = 0 (Pauli finiteness):** the species sum (fermions +1 per Weyl, twelve gauge
  bosons −4 each) is −3 for the Standard Model alone and **0 for the Standard Model plus three right-handed
  neutrinos** — the content the model already needs for Majorana masses. Registered as **P-2026-045**
  (exactly three right-handed neutrinos, three generations, no light steriles).
- **Owed:** the count runs over fermions and gauge bosons only. The Higgs scalars enter the same
  coefficient generically as (1/6 − ξ_H), so the exact-zero balance is ξ-independent only if the induced-G
  scalar weight is zero — otherwise it requires ξ_H = 1/6, the same input the G *value* needs. Verifying
  the scalar coefficient (Visser 2002, Eq. 35) is owed; P-045 carries this caveat.
- **The number of generations is three,** forced by the finiteness condition.
- **The G value is not computed** — it needs the Higgs ξ_H, a Standard-Model input the framework does not
  fix. What stands is the finiteness condition and its forward tests.

## 6. The basement roster

The medium's microscopic content is the **paired lepton-sector vacuum** — leptophilic by identity, with
three flavours (α_c = 3α), neutrinos interior (c = 9/10), and a lepton-number-breaking Goldstone (the
Majoron tie). This is plausibly the same object as the §3 dark confining sector: one 3-flavour,
lepton-partnered, electron-scale confining vacuum. It supplies the roster the §5 str[k₁] balance runs
over. **Status: hypothesis** — coherent and unifying, but the electron-scale portal (§2) is its one
irreducible input.

---

## 7. The genesis and structural numbers

- **λ_phys ≈ (m/Ψ₀)² ≈ 2×10⁻⁹¹ — derived** (the ultralight field's axion quartic), pinned to a factor-~9
  window by two independent bounds: black-hole support below (the quantum-pressure Kaup mass, ~4×10⁹ M☉,
  is exceeded only with a repulsive amplitude quartic) and isocurvature above (P-2026-031). Two quartics
  are involved: a repulsive *amplitude* quartic for the collapse floor, and an attractive *phase* quartic
  for the isocurvature. P-031's amplitude (sub-%- to %-level) rests on an O(1) coefficient.
- **n (the winding integer) — measured, not derived by design:** the one topological draw of the genesis
  (Kibble), n ~ 10–30, the shared source of the ℓ ~ 130 comb, the isocurvature line, the matter asymmetry,
  and the magnetic helicity.
- **η (the baryon asymmetry) — estimate:** η = n × junction transmission; the transfer integral lands at
  the right order (~6×10⁻¹⁰) from recorded inputs. The thermal-leptogenesis route is dead (×40–1000 under).
- **A_s = (α_c/4πk)³ — candidate:** the shot-noise closed form; the count k is unmechanized. The corpus's
  boldest standing claim, deliberately exposed.
- **n_s = 1 − 2/ln(M_Pl/T_on) — derived-estimate:** the census drift; the "2" is the open spatial
  dimensions.
- **z_on ≈ 3.56×10⁷ — fast-profiled estimate,** chain-graded later.
- **The bounce:** ρ_bounce is finite (quantum pressure guarantees a floor; a repulsive amplitude quartic
  sets its value). See [PRTOE_bigbang_no_singularity.md](PRTOE_bigbang_no_singularity.md).

---

## 8. What remains owed

1. **The portal √σ_dark = m_e** — the one irreducible input of the dark-energy / basement sector (§2, §6).
2. **The induced-G scalar coefficient** — verify Visser Eq. 35; decides whether P-045 is ξ-independent
   (§5).
3. **f̄ and α_c referees** — the winding ensemble and the α_c chain, both running (§1).
4. **A_s's count k** — the one unmechanized factor in the amplitude (§7).
5. **The spurion value μ = 2.25 meV** — set by the electron-mass scale, not independently derived (§4).

*Killed approaches and retracted claims are recorded in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md), not here.*
