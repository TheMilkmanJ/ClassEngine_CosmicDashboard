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
| **f̄** | 2/π ≈ 0.6366 | **candidate (coupling form data-selected)** — the winding average, the mean-absolute-sinusoid ⟨\|cos\|⟩ in the many-turns limit. The equidistribution is granted; the one owed piece was *the coupling form* (which functional of the winding projection sets f̄), now resolved — see below. The ε-blind ensemble gives c = 0.903 [0.867, 0.942], −0.08σ from 9/10. |

**The coupling form, resolved.** Once equidistribution is granted, the winding projection is cos θ with θ uniform on [0, 2π), and *which average* sets f̄ is the coupling's order. Four candidates, and the model's own data adjudicates: signed-linear ⟨cos⟩ = **0** (a signed projection averages to nothing — excluded outright by the observed ε > 0, so the coupling must be sign-insensitive); rectified-linear ⟨\|cos\|⟩ = **2/π = 0.6366**; RMS √⟨cos²⟩ = **0.7071**; variance ⟨cos²⟩ = **0.5**. A first-order Yukawa mass shift δm = g·A_eff is **linear** in the winding-projected condensate amplitude, and mass-positivity **rectifies** the sign — giving the mean-absolute, 2/π. The quadratic readings are the subleading (energy-density) coupling. And the corpus's two independent measurements — fit-implied f̄ = 0.6253, winding-sim = 0.635 — **both land on 2/π** (+1.8%, +0.3%) and **reject RMS at +13%** and variance further still. So the coupling form is not a free choice: mass-positivity kills the signed average, leading-order dominance picks linear over quadratic, and the data confirms the selection over the RMS alternative. **Residual:** "leading-order dominates" is generic but not proved from the un-built family-coupling Lagrangian — so f̄ = 2/π is *strengthened candidate, coupling form data-selected*, not an absolute closure. The running winding ensemble remains the value's referee.
| **α_c** | 3α | **candidate (under test)** — a pre-registered value; the "3" is the transverse-projector trace of the induced loop (spatial dimension d = 3), with two field-theory pieces owed. The running α_c chain is the referee. |

The three ε values in the corpus differ deliberately: 1.232% (production fit), ~1.24% (posterior), 1.2543%
(the derived stack). The gap is inside the posterior width; the running measurements decide.

---

## 2. The dark-energy value

The dark-energy scale is a closed form whose only dimensionful input is the electron mass:

$$\rho_\Lambda^{1/4} = \tfrac{1}{2}\alpha_c^2 M_2 = \tfrac{9}{2}\alpha^4\,\tau\,m_e,\qquad \tau \equiv T_c/m_e .$$

- **Chain:** m_e → T_c → M₂ = α²·T_c = 9.53 eV → ρ_Λ¼ = 2.28 meV vs the observed 2.25. The α⁴
  scaling and M₂ = α²·T_c are real STRUCTURE, but **the "1.5%" is NOT a sourced prediction** —
  T_c = 179 keV is the observed ρ_Λ inverted-and-rounded (0.34506 → 0.35), not independently
  derived (see the NOT-INDEPENDENTLY-SOURCED bullet below and §6). It becomes a prediction only
  with a lattice T_c/√σ for SU(2). See [PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md).
- **τ = T_c/m_e = 0.3503 — derived; and 0.345 is the OBSERVATION, not a second derivation.**
  The derived T_c = 179 keV gives τ = 179/511 = **0.3503** ⟹ ρ_Λ¼ =
  (9/2)α⁴τ·m_e = **2.2842 meV** *(the +1.5% is the rounding, not a sourced prediction — see below)*. The number **0.345** is
  ρ_Λ¼(observed)/((9/2)α⁴m_e) = 2.25/6.5207 = **0.34506** — *the observed dark-energy density read
  backwards*, which the registry states plainly (P-2026-048: *"fixed by the observed dark-energy
  density … the flagship's 1.5% prediction read backwards"*). **Quoting 0.345 as "derived" implies
  T_c = 176.3 keV and silently converts the +1.5% prediction into a 0.0% match — i.e. it deletes
  the prediction it is cited to support.** The lattice band T_c/√σ ≈ 0.34–0.37 is **not an independent check either** — it is an **SU(3)**
  value and this model's dark sector is **SU(2)** (P-2026-048), the pure-glue anchors disagree by
  ~11% (SU(3) 0.63 vs SU(2) 0.69–0.71), and no published SU(2) N_f = 3 number exists. The model's
  τ = 0.3503 sits inside the band, **and so does the observation's 0.345** — the band is 8.5% wide
  and cannot tell them apart. The band is that **of a QCD-like confining sector** (pure glue, at 0.63,
  is excluded), which requires the dark sector to carry **light dark quarks (N_f ≥ 2)** — consistent
  with P-2026-048's N_f = 3.
- **T_c ≈ 179 keV — NOT INDEPENDENTLY SOURCED. This is the flagship's
  weakest joint and it was not stated where the flagship is claimed.** The three routes on offer:
  **(i) "τ·m_e" is CIRCULAR** — τ ≡ T_c/m_e, so this defines T_c by itself (line 42 derives τ *from*
  T_c; this line derives T_c *from* τ). **(ii) the perturbative route** T_c = m_e0·√(3(L−1)/2π²) is
  **log-ambiguous over ~40–450 keV** ([PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §; a 10× band) and
  gives 193 keV at the μ = T fixed point, not 179. **(iii) the lattice band** T_c/√σ ≈ 0.34–0.37 is
  **an SU(3) value, and this model's dark sector is SU(2)** (P-2026-048) — §6 already flags this as
  a live risk, and no published T_c/√σ for SU(2) with N_f = 3 exists.
  **What the band actually delivers:** with √σ = m_e, T_c ∈ [173.7, 189.1] keV ⟹ **ρ_Λ¼ ∈ [2.217,
  2.413] meV — a ±4.2% window that contains BOTH the observed 2.25 AND the model's 2.284.**
  **So the flagship's "+1.5% prediction" is the gap between two points inside one band, sourced
  from the wrong gauge group.** The honest grade is: ρ_Λ¼ is predicted **to ±4.2%**, and the
  observation sits inside — real, but not the 1.5% the spine, the CC file and THREE_EQUATIONS
  quote. **What would make it a 1.5% prediction: a lattice T_c/√σ for SU(2), N_f = 3** — the
  number P-048 bets on, still uncomputed. The perturbative
  Coleman–Weinberg estimate (193 keV, log-ambiguous) is a 7%-consistent cross-check. This is the same
  scale BBN watches the ε-ramp switch at.
- **The one input:** the portal **√σ_dark = m_e** — the dark confining sector's scale equals the electron
  mass. This cannot be derived without abandoning τ ≈ 0.35 (a conformal sector that would fix √σ_dark = m_e
  gives the wrong τ; the QCD-like sector that gives τ carries its own scale). It is an **irreducible input**
  — the "meV whisper," ρ_Λ ~ α⁴m_e — but a **falsifiable** one (it predicts ~MeV dark states).
- **Head-on pass: confirmed irreducible, and the total-input count named.** A direct
  re-attack finds no derivation — the τ-vs-scale obstruction above is a genuine fork, not a gap to be
  filled. What the pass *does* fix is the honest scope: √σ_dark = m_e is the one dimensionful input **of
  this (dark-energy / confining) sector**, and it is *not* the theory's sole dimensionful anchor. The
  ultralight quantum mass **m = 2.24×10⁻²⁰ eV** (the onset clock z_on, a separately *measured* input;
  [PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §Field 1) sets the DM / healing-length sector independently.
  So the theory carries **exactly two dimensionful inputs** — m_e (confining/DE) and m (ultralight/onset) —
  each falsifiable, each anchoring a different sector; every other scale (τ, T_c, M₂, ρ_Λ, Σm_ν, ξ) is one
  of these two times pure numbers. Two anchors, not one — the honest count, stated so no later pass mistakes
  m_e for the sole input or tries to re-derive the portal.

---

## 3. The dark sector

The confining sector that binds the dark energy is a **3-flavour, lepton-partnered confining vacuum at the
electron scale** (√σ_dark ≈ m_e). Its chiral condensate is the dyad (the electron-mass shifter). It sets
the dark-energy binding scale only — the dark matter remains the medium's own ultralight excitations.

> **The flavour count's receipt was withdrawn and replaced.** This section previously
> read *"its three flavours supply the '3' in α_c = 3α"* — **retired**: that 3 is the spatial
> dimension d (§1, MATH_SPINE §0), so it never supported the flavour count. τ requires only
> N_f ≥ 2 (§2), so the count stood unsupported. The candidate replacement is **Pauli finiteness
> applied to this sector**, which forces **dark SU(2) with N_f = 3** as the unique integer solution
> of str[k₁]_dark = 2·N_f·N_c − 4(N_c² − 1) = 0 — see the flag in §6, **including its live risk**
> (τ's 0.34–0.37 band is an SU(3) value, and τ scales ρ_Λ¼ linearly). **Until that is settled the
> flavour count is a candidate, not a derivation**, and the colour group N_c — never named anywhere
> in this corpus — is an open slot this argument would fill.

- **Cosmology (safe):** the ~MeV dark baryons cannot overclose. To be the dark matter they would need a
  dark asymmetry ~1700× the visible one; at any natural asymmetry they are ≤10⁻³ of it, and symmetric
  relics annihilate away (strong coupling).
- **Footprint (falsifiable) — RE-PRICED at N_c = 2, and the answer changed sign.** The old
  figure (**ΔN_eff ≈ 0.05–0.3**) came from a *generic scan* over g_dark = 2, 4, 8, taken because the colour
  group was unknown. With the group fixed to SU(2) (§6), the count is determined — and **pseudo-reality
  enlarges the chiral symmetry to SU(6) → Sp(6), giving 2N_f² − N_f − 1 = 14 Goldstones**, not the
  N_f² − 1 = 8 an SU(3) sector gives. That is **1.75× the old scan's ceiling**, and it puts
  **ΔN_eff = 0.375 even at the earliest possible decoupling** — above Planck's ΔN_eff ≲ 0.3 (2σ), at *any*
  T_dec (the largest g_dark Planck admits is 11.2). **The sector cannot escape by making the Goldstones
  heavy:** a pseudo-Goldstone is lighter than its confinement scale (√σ_dark = m_e = 511 keV) by
  construction, and **τ is spending exactly that lightness** — heavy dark quarks push T_c/√σ back toward
  the pure-glue 0.69–0.71 and break §2's value. **The ramp audit made it worse:** n/p freeze-out is at
  T ≈ 700 keV while T_c = 179 keV, so **T/T_c ≈ 3.9 — the dark sector is DECONFINED at freeze-out** and the
  Goldstones do not exist yet; the correct count there is dark quarks + gluons = **27**, giving
  **ΔN_eff = 0.723** → ΔY_p ≈ +2.3σ *added to* the model's **+1.09σ adverse Y_p scar (ramped) → ≈ +3.4σ**. **Consequence: the dark sector must have
  NEVER THERMALISED with the SM.** Registered as the fifth kill of **P-2026-048**.
  (`scripts/dark_neff_su2.py`; predecessor `scripts/dark_neff.py`, `scripts/tau_deconfinement.py`.)
- **THE NON-THERMALIZATION ESCAPE — BUILT (2026-07-17), TRIBUNAL-ADJUDICATED (2026-07-18):
  verdict NARROWED.** The kill is **CONFIRMED on the recorded model** (the v ≈ 175 keV electron-CW
  dyad thermalizes; margins 10⁸–10¹⁷, strengthened in trial: the U(1) seal, the 2-dof floor
  ΔN_eff = 1.14, the fluctuation nail); **one branch survives — the zero-mode/high-f dyad
  (v ≈ 100–500 TeV)**: gates cleared by 10⁸–10⁹, the ramp's synchronizer survives (first order in
  κ vs κ² thermalization), the fifth-force wall closed by the corpus's own operator-level gate
  (billing symmetry: the recorded model needs the same gate ~10⁸-worse for electron g−2 before
  cosmology), residual **ΔN_eff ≈ 0.06–0.24 with the committed ξ window (§8 item 1b) — a CMB-S4 (±0.03)
  detection target**. The branch's
  price sheet (P1–P6: a new ~100-TeV input, the dyad=condensate identification drops, the
  electron-CW mechanism dies as recorded, BBN books re-run, the gate's owed checklist, a
  genesis-ξ commitment) is booked and paid; **the branch is the standing configuration (§8
  item 1b)**.
  √σ_dark = m_e and the flagship survive either way. Full record + verdict:
  [Nontherm_Kill_Discussions.md](threaded_physics_working/Nontherm_Kill_Discussions.md) §6.
  The original build's detail, for the recorded-model kill it established: The rate check Γ(dark–SM) < H at all T, run on the
  model's own recorded couplings: **(i)** gravity and the census-closed portals pass (Γ/H ≈ 3×10⁻⁷
  even at the pour scale — the standard gravitational escape holds *for those channels*). **(ii) The
  dyad–electron channel is fatal:** the [ESTABLISHED] electron-CW mechanism needs κm_e² ~ 10⁻² active
  in the SM bath to source the T_c = 179 keV ramp; that coupling (the post-SSB fluctuation vertex
  g_ee = 2εm_e/v = 0.073 at v ≈ 175 keV — quadratic-canonical, see the fork resolution below) gives
  **Γ/H ~ 10¹⁵–10¹⁹ from BBN to reheating** — full thermal equilibrium.
  The bound is g_ee < 1.8×10⁻¹⁰ (equivalently v ≳ 3.6×10⁴ GeV): violated by 10⁸·⁶ in coupling. Under
  the bound the mechanism's maximum deliverable amplitude is ε_max ≈ 2×10⁻¹⁶ vs the needed 1.25×10⁻²
  — **the size-XOR-quiet wall (gate-0 §7.3) recurring: a dyad big enough to source ε thermalises;
  one quiet enough not to cannot source ε.** **(iii)** The corpus's own identification (the dyad IS
  the SU(2) sector's chiral condensate, §6) drags the full 27 dof in: ΔN_eff = 27/(7/4) = **15.4**;
  even a detached thermalised dyad alone gives 4/7 = **0.571** > Planck's 0.3. **(iv) The timing
  pincer (normalization-independent):** the BBN engine codes the ramp on T_γ with T_c = 179 keV;
  synchrony requires ξ = T_d/T_γ = 1 (⟹ ΔN_eff = 15.4); the priced dilution ξ = 0.465 puts dark
  confinement at T_γ = 385 keV and the escape's ξ ≤ 0.284 at ≥ 630 keV — desynchronising the coded
  window ("OFF at n/p freeze-out, GROWING below T_c"). Every branch closes. **(v)** The only
  recorded normalization that passes (f_L = 2.3×10¹¹ GeV, by 10⁵) is the §7.6-killed single-field
  era's — it cannot produce the coded ramp; reviving it is a different model. **Net: the ΔN_eff
  escape, the ε-ramp mechanism, and √σ_dark = m_e are pairwise-incompatible as recorded** — the
  sharpest structural tension in the corpus, sharper than BBN D/H. *The normalization fork surfaced here is RESOLVED (2026-07-17): the operator is
  **quadratic-canonical** — dark-U(1) forbids the linear coupling
  ([PRTOE_gate0_qft_derivation.md](PRTOE_gate0_qft_derivation.md) §1, which pre-labels the linear
  amplitude formula as the quadratic operator's value); the "linear g_ee" is only the post-SSB
  fluctuation vertex 2κv·m_e0. The recorded v ≈ 100 keV was a conflation (the delivered shift ε
  inserted in the slot of the dimensionless coupling κm_e0²), with the closed-form fix
  v = m_e0·[ε(L−1)/4π²]^{1/6} ≈ 175 keV, κm_e0² ≈ 0.108, g_ee ≈ 0.073 — **T_c, τ, and ρ_Λ untouched
  (κ cancels in T_c)**, the gate-0 reduction survives at a more robust 1/6-power. All rate changes
  from the fix are ≤ 10² and adverse to the model — the escape-failure finding is unaffected
  (marginally strengthened).* (Worked script: the non-thermalization build, 2026-07-17; every crux
  number independently re-verified at booking.)
- **THE m_q SQUEEZE — three constraints, one variable, and τ pulls against the other two.**
  The dark quark mass is asked to be **light** by τ (**0.3503** derived; the rows here were computed at 0.345 — a +1.5% shift, immaterial to this squeeze) (§2 — heavy quarks drive T_c/√σ back toward the
  pure-glue 0.69–0.71), and **heavy** by two independent others: (i) **ΔN_eff/Y_p**, which needs Boltzmann
  suppression and gets none while τ keeps the quarks light; and (ii) **the depth law + the coded BBN ramp**,
  because **N_f = 3 degenerate light quarks give a FIRST-ORDER transition at any N_c** (the Columbia-plot
  corner — SU(3) included, so this predates and is independent of §6's SU(2)), whereas the BBN engine's
  standing treatment is ε *"GROWING below T_c — the order-parameter birth **ramp**"*
  ([PRTOE_THE_AMPLITUDE.md](PRTOE_THE_AMPLITUDE.md)), and a first-order transition **jumps** the order
  parameter rather than growing it. Amendment 5 (the depth law, TOTAL) makes that step illegal outright: a
  dynamical discontinuity is not quantized, not topological, not a protected zero, so it has **no exemption
  clause**. [PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md) §5 already names this failure mode —
  *"otherwise the transition boils, first-order"* — for a different sector, in the same grammar.
  **RUN — the window is NOT empty, and it pins m_q.** The framing that raised the alarm was
  wrong: *"N_f = 3 light quarks → first order"* is the **chiral-limit** statement, and this sector is not in
  the chiral limit ("light" means light *relative to Λ*, not massless). Against the QCD anchors τ is quoted
  from (chiral T_c/√σ ≈ 0.300 at m_π/√σ = 0; physical ≈ 0.352 at 0.318), **τ (0.345 as this row's input; derived 0.3503) sits at
  m_π/√σ ≈ 0.274**, while the Columbia first-order corner ends at **0.06–0.16** — the sector is **above it
  by 1.7–4.6×**. **The transition is a CROSSOVER**, so τ and the depth law are compatible and the coded
  order-parameter birth ramp is correct. What the squeeze buys instead of a kill is a number the model never
  had: **m_π,dark ≈ 140 keV**, and via GMOR **m_q,dark ≈ 38 keV**. ΔN_eff is *not* rescued by it — at
  freeze-out the sector is deconfined and m_q/T = 0.055 is unsuppressed — so P-048's non-thermalisation kill
  carries that constraint, not the mass. **Two of three compatible; the third is a registered kill.**

---

## 4. The neutrino sector

- **Σm_ν ≈ 61.4 meV, normal ordering — recorded prediction**, from the tie ρ_Λ¼ = m_ν,lightest (the DE
  floor equals the lightest neutrino mass). Requires the Majorana mechanism. The tie now has a
  **forward mechanism** (`scripts/kubo_freeze.py`): the dark condensate thermally settles into the
  cosmic neutrino bath (its only tree-level partner) with Γ/H ≈ 5×10¹⁰ ≫ 1 — it tracks the bath — and
  the settling freezes when the bath goes non-relativistic and decouples. The **lightest** neutrino is
  the last relativistic friction partner (heavier species go NR earlier), so it sets the final freeze.
  **The tie's arrow is re-homed:** the equality's *source* is the mass-generation identity read
  forward (the tenth-channel seat term — operator exhibited, with its UV form; the floor SETS m₁),
  and the kubo settling above is the *dynamics* that then freezes there by construction. See
  [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md).
- **The spurion μ = 2.25 meV** — a soft lepton-number-breaking dimension-1 scale that sets both the
  dark-energy floor (ρ_inf = κ_V μ⁴) and the direct light neutrino mass (m_ν = κ_m μ), tie exact to 2.2%.
  **Graded: μ is not an independent input.** It equals ρ_Λ¼ = m_ν,lightest = the
  electron-mass-anchored meV whisper of §2 (the flagship chain (9/2)α⁴τ·m_e = **2.284 meV** *(structure real; the +1.5% is the τ rounding)*, against the observed 2.25 — a **+1.5%** prediction), with κ_V, κ_m
  the O(1) ties; it is downstream of the *one* irreducible input, the portal √σ_dark = m_e (§6), not a
  separate knob.
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
- **Checked — the caveat is now named:** the count runs over fermions and gauge bosons only. The Higgs scalars enter the same
  coefficient generically as (1/6 − ξ_H), so the exact-zero balance is ξ-independent only if the induced-G
  scalar weight is zero — otherwise it requires ξ_H = 1/6, the same input the G *value* needs. **Verified:
  Visser 2002, Eq. 35 assigns each real scalar the weight (1/6 − ξ), confirming the ξ_H = 1/6 (conformal
  Higgs) requirement. The "hole" reduces to one named assumption (§8 item 2).** P-045 carries this caveat.
- **The number of generations is three,** forced by the finiteness condition.
- **The G value is not computed** — it needs the Higgs ξ_H, a Standard-Model input the framework does not
  fix. What stands is the finiteness condition and its forward tests.

## 6. The basement roster

> **ADJUDICATED: the "3" in α_c = 3α is the SPATIAL DIMENSION d, not the flavour
> count.** §1 and [PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §0 hold (*"α_c = 3α = d·α"*, the
> transverse-projector trace of the induced loop). **§3's claim that "its three flavours supply the
> '3' in α_c = 3α" is therefore retired** — a false receipt. This was the third instance of one
> attribution pattern (chirality double-sourced from the winding n *and* p-wave L; the generation
> count from str[k₁] = 0 *and* Weyl nodes; the "3" from d *and* flavours) — and in every case the
> redundant claimant lost.
>
> **What that leaves, and the candidate that replaces it.** With the α_c receipt withdrawn, nothing
> held the dark flavour count at 3: τ requires only N_f ≥ 2 (§2), and the corpus never names the
> dark colour group N_c at all. But [PRTOE_quantum_gravity.md](PRTOE_quantum_gravity.md) §5.2 states
> the finiteness sum runs over **"every field in the vacuum — not the model's coupling roster"** —
> and **the §5 table counts only the Standard Model's 48 Weyl fermions and 12 gauge bosons. The dark
> sector is missing from the model's own sum.** That is a defect regardless of what follows.
> Supplying it, and requiring the dark sector to self-cancel (the SM part already does, and the
> Higgs contributes zero at ξ_H = 1/6):
>
> **str[k₁]_dark = 2·N_f·N_c − 4(N_c² − 1) = 0 ⟹ N_f = 2(N_c² − 1)/N_c**
>
> | N_c | 2 | 3 | 4 | 5 | 6 |
> |---|---|---|---|---|---|
> | N_f | **3 — integer** | 5.33 | 7.5 | 9.6 | 11.67 |
>
> **N_c = 2 is the unique colour group admitting an integer flavour count, and it gives N_f = 3
> exactly** (quarks +12, gluons −12). The same condition that forces three generations would force
> **dark SU(2) with three flavours** — a real receipt where the α_c one was false.
>
> **The consilience — SU(2) independently delivers three things the model already
> required, for reasons that have nothing to do with this counting.** Two-color QCD's fundamental
> representation is **pseudo-real**, so a colour singlet needs an **even** number of quarks:
> **its baryons are bosons — diquarks** [Kogut–Stephanov–Toublan; Hands et al.].
> 1. **The BEC side, which §4 demands.** The occupancy argument's owned assumption is that it holds
>    *"on the strong-coupling (BEC) side of the BCS–BEC crossover… verified to fail on the weak side."*
>    Two-color QCD is the **canonical diquark-BEC system** and the textbook realization of the
>    **BEC–BCS crossover**. §4 already wrote the punchline — *"the two sides of condensed matter's
>    most famous crossover perform the two famous jobs in one vacuum"* — without naming the group
>    that provides the crossover.
> 2. **ℓ = 0, which the DE value selects.** The lightest SU(2) baryon is the **scalar diquark** —
>    s-wave. That is the channel [PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md)
>    §4c's table selects at +1.5% and excludes at −74.6% (p-wave) and −93.7% (f-wave).
> 3. **"He-3-A missing its baryonic matter" — as group theory, not analogy.** He-3 pairs p-wave
>    because its baryonic hard core suppresses ℓ = 0. In two-color QCD there **are no fermionic
>    hard-core baryons**: the baryons are bosonic diquarks. The core that forces helium up to L = 1
>    does not exist, so s-wave is unsuppressed — which is precisely the mechanism §4c invokes and
>    precisely what the ℓ = 0 selection needs.
>
> **REGISTERED as P-2026-048** — the dark colour group is SU(2), N_f = 3, and
> **T_c/√σ = 0.3503 ± 0.02** for SU(2) with three light flavours *(the registered value 0.345 is the observed ρ_Λ inverted — see §2)*; see
> [PRTOE_PREREGISTERED_PREDICTIONS.md](PRTOE_PREREGISTERED_PREDICTIONS.md). The model's first
> prediction addressed to a *lattice computation* rather than a telescope.
>
> **CANDIDATE, not banked — one number decides it, and it is not yet computed.** *The τ collision:*
> τ comes from the band T_c/√σ ≈ 0.34–0.37 of a **QCD-like (SU(3))** sector *(and 0.345 specifically is the observed ρ_Λ inverted — see §2's re-grade; the two provenances are not the same claim)*, with SU(3) pure
> glue at 0.63 excluded — and τ scales ρ_Λ¼ **linearly**, so the flagship's 1.5% rides on it.
> Lattice anchors are firm for pure glue (**SU(3): 0.63; SU(2): 0.69–0.71**, ~11% higher), but
> **no published T_c/√σ for SU(2) with N_f = 3 light flavours was located** — the two-color
> literature is dominated by N_f = 2 at finite *density*. An independent adversarial analysis
> (defend-vs-challenge with a neutral referee — [Basement_Roster_Discussions.md](threaded_physics_working/Basement_Roster_Discussions.md))
> sharpened this on two points, both sides self-correcting against their own interest. First, the
> SU(3) √σ **cancels** in the transport: the glue→N_f=3 reduction is a pure temperature ratio
> r₃ = 1 − T_c^phys/T_c^glue, so √σ divides out — the earlier naive **0.38–0.39** was partly a
> mixed-convention artifact, not a real value. Second, the convention-clean unquenching reduction is
> ~42% (not 45%), which puts the honest dof-family band at **τ ≈ 0.355–0.382, centre ~0.36**
> (ρ_Λ¼ a few percent **above** the observation), pointing the right way on physics (N_f/N_c = 1.5 vs
> SU(3)'s 1.0). A dedicated literature sweep (2026-07-17, every paper read in full — the addendum in
> [Basement_Roster_Discussions.md](threaded_physics_working/Basement_Roster_Discussions.md)) then
> anchored the question to measured neighbours: **no lattice determination of SU(2) N_f = 3 exists
> anywhere**; the measured anchors are SU(2) N_f = 2 at **T_d/√σ = 0.483(23)** (deconfinement, heavy
> quarks; Braguta school) and a chiral crossover pinned only to **0.36–0.48** (Iida–Itou–Lee, ~30%
> internal systematic), with the SU(3) N_f-dependence (Karsch–Laermann–Peikert) showing the flavour
> suppression **saturates** (−0.21 for two flavours, −0.03 for the third). The inference bracket:
> **τ(SU(2), N_f = 3, chiral) ≈ 0.39 ± 0.05** (generous 0.34–0.45), every step past the measured
> 0.483 an SU(3)-analog transfer, stated not hidden. **Verdict (standing): τ = 0.3503 sits at the
> BOTTOM EDGE of the literature bracket — permitted, not favoured; the centre (~0.40) is above the
> model. Reaching 0.3503 requires BOTH (i) the transition being the chiral/condensation one, not
> deconfinement (if the mechanism keys on deconfinement, the supported value is ~0.48 — real
> tension), AND (ii) near-maximal continuum/chiral-limit suppression. On fork (i) the model has a
> genuine argument: the dCDF's T_c is a pairing/condensation transition — the chiral-condensate
> analog, not the Polyakov-loop one — and in SU(2) the two transitions demonstrably DECOUPLE
> (Kaczmarek et al.: the Polyakov susceptibility peak shrinks with lighter quarks, opposite of
> SU(3)), so the chiral T_c legitimately sits below the deconfinement number (argument-grade). Fork
> (ii) is not arguable from here — only a dedicated SU(2) N_f = 3 lattice run decides it, and this
> sweep establishes nobody has run one.**
> *Assumptions, named:* dark quarks Dirac and in the fundamental — adjoint or Weyl/Majorana content
> changes the counting. *Also owed:* the ΔN_eff footprint (§3) is priced for the existing roster and
> would need re-pricing at N_c = 2; and the SU(2) N_f ≥ 2 chiral transition is reported **first
> order**, which should be checked against the settling-attractor requirement in
> [PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md) §5 (different transition, but worth the check).

**The two condensates, kept distinct.** The SU(2) sector carries two condensates: the **diquark**
condensate ⟨qq⟩ — which *is* the dCDF, and which owns this section's consilience (the BEC side, the
scalar-diquark ℓ = 0 selection, the no-hard-core grammar are all ⟨qq⟩ statements and stand) — and
the sector's own **chiral** condensate ⟨q̄q⟩, an internal object with no SM coupling. **The dyad is
neither**: it is the separate high-decay-constant field of §8 item 1b. The honest re-price of the
former one-object reading, in three parts: (i) **the single T_c splits into two electron-anchored
scales** — the SU(2) confinement scale τ·m_e = 179 keV (the flagship's, portal-anchored,
lattice-gated) and the dyad's electron-loop restoration scale (the κ-independent formula, log-band
[40, 900] keV; the recorded BBN stability fence covers [179, 369]); their near-equality is two
anchors coinciding at the electron scale for separate reasons (the portal vs the electron loop),
not one object. (ii) **The Majoron scale, priced at all three corners (2026-07-18).** The registry already
carries v_L's two corners (resonant → MeV, S4-armed; non-resonant → ≥ GeV, S4-dark; CMB-S4 the
corner-selector), and the ν-tie's recorded forward mechanism (`scripts/kubo_freeze.py`) rides the
Majoron vertex: Γ/H ∝ (m₃/v_L)², = 5×10¹⁰ at the 4.2 MeV launch value, unity at **v_L ≈ 0.9 TeV**,
9.6×10⁻⁶ at 300 TeV. Against the thermalization floor f ≳ 40 TeV this gives a clean three-corner
table — with one further constraint lane in the books: **ν free-streaming at recombination.**
The Majoron's νν̄ ↔ φ channel
re-couples the neutrino bath at Γ/H(z ≈ 1100) ∝ g²m₃²/(4πTH) — and the CMB is a free-streaming
referee. The tested table (estimate grade — order-of-magnitude rates; the literature anchors and a
proper Boltzmann pass are owed):

| corner | tie tracking | ν recoupling at z ~ 1100 | standing |
|---|---|---|---|
| **A: f = v_L ≈ 100–500 TeV** | dead (no window; 40× gap) | never (Γ/H ~ 10⁻⁷) — CMB-safe, S4-dark, 0νββχ-invisible | quiet, at the tie's price |
| **B: v_L in the corridor (below)** | was "alive" via the retracted channel | *(withdrawn — the corridor's fences rode P-2026-049)* | dissolved with the retraction |
| **C: v_L ~ MeV** | alive (5×10¹⁰, condensate-friction) | *(the deep-recoupling stress was the retracted channel)* | **alive — lane-clean** |

**The corridor's floor fence and the recoupling epoch are withdrawn** (the νν̄ ↔ φ channel is
kinematically closed at the recorded Majoron mass m_J ~ (1–3)H₀ ≪ 2m₁ — P-2026-049 retracted,
autopsy in [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md)); for an ultralight Majoron the
free-streaming lane returns no discriminator at any corner (g⁴ exchange only, Γ/H ≲ 10⁻⁵
everywhere; the massless-mediator CMB bound g ≲ few×10⁻⁷ is passed by ≥ 20× at the MeV corner).
**What stands on this fork:** the one-scale corner remains tie-dead (the condensate-friction
channel is a coherent-mode rate, not coalescence: ceiling v_L < 0.94 TeV for the settling
dynamics); the TeV and MeV corners are **both alive**, and the corner-selector is the registry's
original referee — the CMB-S4 Majoron/ν-interaction search (a detection at g ~ 10⁻⁸–10⁻⁹ selects
the MeV corner and its resonant-leptogenesis lane; a null leans high-v_L). **The SN1987A lane,
verified against the literature (2026-07-18): both corners clear.** The Majoron–ν channel is
kinematically open in the supernova core and ungated, and the bounds are: the classic
luminosity/trapping exclusion band **3×10⁻⁷ < g < 2×10⁻⁵** (Kachelriess et al. 2000; Farzan
hep-ph/0211375, medium effects included), and the modern SN1987A likelihood analysis
(arXiv:2410.11517, PRD) at **g₁₁ ≲ 10⁻⁷–10⁻⁶ for m₁ ~ 1–10 meV** — which applies to the
mass-basis-diagonal singlet Majoron through matter-induced off-diagonal couplings. The MeV
corner's largest coupling (g₃₃ = 1.2×10⁻⁸) clears the classic band by ~25× and the modern
bound by ≥ 8×; the high-v_L corner clears everything by ≥ 5 orders. The census's other
lanes clear: stellar cooling (dyad gate closed in stars), μ→eJ (singlet Majoron — tree charged
coupling absent), BBN thermalization (coalescence closed, 2↔2 is g⁴), long-range forces
(matter coupling two-loop-suppressed; ν self-interaction below ultralight-mediator bounds).
The two-scale structure (f ≠ v_L, three dark fields) stands on the one-scale corner's tie-death
alone. Corner selection: **open — both corners lane-clean; CMB-S4 is the selector.**

**What the test settles and what it leaves (post-retraction state):** the TeV and MeV corners
are both lane-clean and CMB-S4 is the sole selector (a g ~ 10⁻⁸–10⁻⁹ detection selects MeV and
its resonant-leptogenesis lane; a null leans high-v_L); the one-scale corner stays tie-dead on
the condensate-friction ceiling alone. **The un-merger's residue is PAID:** the tie's mode is
re-homed — the tenth-channel mass relation (the seat term, operator exhibited with its UV form;
[PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md)); the seat constant b is the remaining
basement-gated number. *(The tie's numerical
equality, and the c = 9/10 lock that seats on the equality, are untouched by the corner choice —
what varies is the mechanism's grade.)* The corner selection is open. (iii) The
one-object field economy is lost — an aesthetic price, stated as one.

The medium's microscopic content remains the **paired lepton-sector vacuum** — leptophilic by
identity, with three flavours (see the flag above — the α_c receipt is retired; the finiteness
candidate is live), neutrinos interior (c = 9/10), and a lepton-number-breaking Goldstone (the
Majoron tie) — read as the §3 dark confining sector's own description: one 3-flavour,
lepton-partnered, electron-scale confining vacuum. It supplies the roster the §5 str[k₁] balance runs
over. **Status: hypothesis** — coherent, and the electron-scale portal (§2) is its one
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
- **A_s = (α_c/4πk)³ — candidate:** the shot-noise closed form. Its pieces are more mechanized than the
  "highest-risk" label suggests: **k = ln(1+π/2α_c)/π is a genuine screened-interaction
  integral** k = (1/π)∫₀¹ dq/(q + 2α_c/π) — the effective gap-equation coupling, audited into the Eliashberg
  window [1.35, 1.37], *not* a landing fit; the **4π is the standard 1-loop factor**, and the **cube is the
  three spatial dimensions**. So A_s = 1/N with N = (4πk/α_c)³ assembles from a derived coupling, a loop
  factor, and 3D. The genuine residual is the exact O(1) **normalization of the shot-noise count** (the
  "count C" — whether the assembly is exactly (4πk/α_c)³), which lands A_s to −0.35%. Deliberately exposed;
  referees are the live zero-parameter run and the Eliashberg k-audit.
- **n_s = 1 − 2/ln(T₀/k), k-local — mechanism candidate (exhibited): 0.9677 at the pivot,
  predicted running −5.2×10⁻⁴** (the banked k-independent 1 − 2/ln(M_Pl/T_on) = 0.9641 is retired
  to consistency-check grade). **The 2D-Gaussian mechanism route, adjudicated by computation (2026-07-17):** the
  candidate microphysics (winding field as a 2D transverse log-correlated height model, δ ~ h²) had
  its owed step — the exact χ²-field convolution P_δ(k) — computed, and **the direct reading
  FAILS**: the exact spectrum is k²P_δ ∝ ln(k/k_IR) (numerics match the analytic 2·ln(k/k_IR)/π to
  4 decimals), giving tilt **+1/ln(k/k_IR)** — wrong sign (blue), wrong coefficient (1 not 2), and
  IR-anchored where the banked form needs UV. The earlier σ⁴ argument conflated the one-point
  variance with the per-mode spectrum. Autopsy in
  [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md). **What survives:** the scale identities are
  real and verified (k_UV = a_on·T_on = T₀ exactly; ln(T_on/m) = ln(M_red/T_on) + 0.49, the banked
  argument to O(1) inside ~55). **The surviving route exhibited — the modulation map (2026-07-18):**
  the mode laid down at scale k is an **envelope × shot** product, ζ_k = A(k)·s_k — s_k the
  A_s mechanism's own scale-invariant shot imprint, A(k) the imprint susceptibility at that scale's
  imprint time. The envelope **multiplies instead of convolving** (it is deterministic in k — a
  function of imprint time, not a fluctuating field squared at the same point), which is exactly
  how the route evades the χ² kill; the killed convolution survives only as an additive residual,
  subdominant provided the winding roughness obeys Δ² ≲ 2×10⁻⁶ per log (six decades of room below
  O(1); accumulated σ² ≲ 10⁻⁴ — the weak-modulation regime, self-consistent). The envelope reads
  the verified variance: A(k) ∝ σ²(k) = Δ²·ln(k_UV/k), UV-anchored at the verified k_UV = T₀. Then
  k³P ∝ [ln(k_UV/k)]² and **n_s(k) = 1 − 2/ln(T₀/k)**: at the pivot, ln(T₀/k*) = 61.86 →
  **n_s = 0.9677** (+0.66σ from Planck), with **predicted running α_s = −2/L² = −5.2×10⁻⁴**
  (Planck −0.0045 ± 0.0067: consistent; a falsifiable edge — the map requires tiny *negative*
  running). **The exponent is data-selected, f̄-grammar:** among the natural readings A ∝ σ
  (n_s = 0.9838, +4.5σ, dead), A ∝ σ² (0.9677, +0.7σ), A ∝ σ⁴ (0.9353, −7σ, dead), only the
  variance-linear map survives — and the linearity has its structural exhibit: for a
  log-correlated field each log-shell contributes **equally** to the frozen-quanta count and to
  the one-point variance, so accumulated population and σ²(k) are the same object up to the
  per-shell constant; if the imprint susceptibility is additive over frozen quanta (one unit of
  response per quantum — the identical additivity the A_s shot count already rides), then
  A ∝ population ⟺ A ∝ σ² with no new assumption. The variance-linearity is the additivity
  statement, inherited from the A_s mechanism rather than chosen. **The
  argument fork resolves:** the map is k-local, so the pivot/running form 0.9677 is the
  mechanism's number; the banked k-independent ln(M_Pl/T_on) = 55.6 form (0.9641, −0.2σ) retires
  to consistency-check status — same log-family within 10%, which is why the fork existed. Noted
  plainly: the mechanism's number sits *farther* from Planck central than the retired form
  (0.66σ vs 0.20σ) — the map is falsifiable on both n_s tightening and the running's sign.
  Grade: **mechanism candidate (exhibited)** — sign, anchor, and running structural; the
  linearity exponent exhibited at additivity level (shared with A_s, one assumption not two)
  and independently data-selected; the Δ² subdominance condition named.
- **z_on ≈ 3.56×10⁷ — fast-profiled estimate,** chain-graded later.
- **The bounce:** ρ_bounce is finite (quantum pressure guarantees a floor; a repulsive amplitude quartic
  sets its value). See [PRTOE_bigbang_no_singularity.md](PRTOE_bigbang_no_singularity.md).

---

## 8. What remains owed

1. **The portal √σ_dark = m_e** — the one irreducible input of the dark-energy / basement sector (§2, §6).
1b. **The high-f dyad.** The dyad is a high-decay-constant field: **f_dyad ≈ 100–500 TeV**, a
   dimensionful **input** — un-derived, stated as such (the window: fifth-force/g−2 set the floor
   ~10¹⁴ eV; tracking sets the ceiling ~10²⁵ eV; the quoted band is where every constraint clears
   simultaneously). With it the model commits to **ONE genesis dilution
   ξ = T_dark/T_γ ∈ [0.25, 0.35]** used consistently everywhere it appears (ΔN_eff, the BBN books,
   sector pricing — no per-window ξ), predicting **ΔN_eff = (27/(7/4))·ξ⁴ = 0.06–0.24, centred
   ≈ 0.1 — CMB-S4 (±0.03) adjudicates directly**; a confirmed ΔN_eff < 0.03 or > 0.3 kills the
   committed window from either side. The dyad is **not** the SU(2) sector's chiral condensate
   (that sector keeps its own condensate and its own T_c/√σ story — the two-color consilience
   points are sector-internal and stand); its condensation is driven by its own L-breaking
   potential, with the electron loop's κ-independent T_c formula supplying the T_γ-keyed ramp
   timing (the predecessor configuration's record:
   [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md)). **The windowed BBN books under this configuration (2026-07-18; response-coefficient
   propagation on the recorded ramped baseline — the ramp profile is unchanged, the branch adds only
   its ξ residual):** across the *entire pre-committed* ξ window the joint p reads
   **0.15–0.29** (0.093 without the residual) — the residual ΔN_eff pushes D/H toward Cooke
   (−1.89σ → **−0.3 to −1.2σ**, crossing zero near the window top) while Y_p pays mildly
   (+1.09σ → +1.3 to +1.8σ vs Aver; the EMPRESS fork worsens to ≈ +4σ — the helium fork remains
   the pivot). The improvement is **anchor-independent in direction** (a relative D/H shift; even
   the adverse-end −2.9σ reading moves to ≈ −1.3σ) and **hostage to its own falsifier** (CMB-S4
   must see the same ΔN_eff). *Provenance note: the ξ window predates this propagation — the D/H
   healing is a consequence, not a fit.* Grade: estimate (linear responses, dY_p/dN = 0.011–0.013,
   ∂ln(D/H)/∂N = 0.135); a full nuclear-code re-run is owed only if the joint verdict becomes
   load-bearing. **The gate's laboratory checklist (2026-07-18; estimate-grade, conditional on the recorded
   curvature-gate form):** all three named checks clear, none closely. The gate is
   **curvature-keyed, not density-keyed** — and that type distinction decides the hardest test:
   atom-interferometry vacuum-chamber experiments kill density-gated (chameleon-class) scalars
   because a vacuum chamber removes the screen, but **curvature penetrates vacuum chambers** —
   every terrestrial laboratory sits ~25 orders above a structure-class gate edge
   (Earth-surface curvature 3.4×10⁻²³ m⁻² vs the galactic 8.4×10⁻⁴⁸), so the coupling is off in
   any lab regardless of chamber contents. EP satellites (MICROSCOPE) are irrelevant by
   kinematics alone: the force range is mm–cm and the source–test separation is ~700 km — the
   Yukawa factor is e^{−2×10⁷}. Casimir-band (μm) experiments constrain μm-range forces; the
   dyad's mm–cm range lives in torsion-balance territory, already fenced (S_⊕ < 2.1×10⁻¹¹
   required; the recorded exponential form delivers immeasurably more). **The honest price, stated
   plainly: the gate that clears the laboratory closes the laboratory as a test** — the local-force
   channel is unobservable by construction, and the configuration's falsifiable channels are
   cosmological (the ΔN_eff window at CMB-S4, the BBN books, DESI). **Still owed:** the high-f
   condensation mechanism's full spec. The gate form itself is now **derived at class level**
   (an event-triggered gate is a survival probability — exponential-power class, the power form
   retired; [PRTOE_me_mechanism_math.md](PRTOE_me_mechanism_math.md) gate section), which
   grounds the checklist's exponential-form reliance; the remaining form residual is the seed
   exponent n.
2. *(resolved) The induced-G scalar coefficient* — verified: Visser Eq. 35 assigns each
   real scalar the weight (1/6 − ξ), not zero, so P-045's str[k₁] = 0 is **not** ξ-independent — it
   requires ξ_H = 1/6 (conformal Higgs). Natural (the conformal value) and self-consistent with the
   G-value's own need, but an input: induced-G finiteness is conditional on conformal Higgs coupling
   (§5). The "hole" reduces to one named assumption.
3. **f̄ and α_c referees** — the winding ensemble and the α_c chain, both running (§1).
4. *(sharpened) A_s's count* — audited: k = ln(1+π/2α_c)/π is a *derived* screened-interaction
   integral (the gap-equation coupling), not the unmechanized part; the 4π is the 1-loop factor and the cube
   is 3D. The genuine residual is the O(1) normalization of the shot-noise count N = (4πk/α_c)³ (the "count
   C"), lands A_s to −0.35%, refereed by the live run + the Eliashberg k-audit (§7).
5. *(closed as owed) The spurion μ = 2.25 meV* — graded as **not** an independent input:
   it is the electron-anchored meV whisper (ρ_Λ¼ = m_ν = 9/2 α⁴ τ m_e), downstream of item 1. One fewer
   free number than the list once carried.

*Killed approaches and retracted claims are recorded in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md), not here.*

---

## The open surface, consolidated (2026-07-18)

After the seam campaign, the selector compression, and the chain-free closures, the model's
entire remaining open surface is:

| open object | what it decides | gated on |
|---|---|---|
| the Koide kernel chain's last link (the 1:1 thermal-twist transfer) | A = √2 AND θ = 2/9 — the full charged-lepton spectrum | the transfer derivation (desk); then the lattice triple (T_c/√σ + F_π/√σ + w·√σ, one campaign) + the P-2026-051 lock |
| ~~the linear-map postulate~~ — DISCHARGED: the −3/2 derived at additivity grade (boost-dressed cutoff, geometric mean, equipartition — hierarchy §2b) | the anchor's −3/2 | the shared additivity neck (one assumption corpus-wide; the ring-on-ring trial tests its Koide instance) |
| the seat constant b | κ_m's exact value | the basement build |
| T_c/√σ for SU(2), N_f = 3 | the flagship's ±4.2% → a 1.5% prediction | the lattice (external; the note APPROVED FOR CIRCULATION) |
| ΔN_eff ∈ [0.06, 0.24] | the genesis ξ window | CMB-S4 |
| the running referees (f̄/α_c chains; the evidence pair) | the amplitude stack; dyad vs ΛCDM | the box |
| the +2.51% dark-ages frequency offset | the ε mechanism, astrophysics-free | lunar-farside 21-cm |

Conditions paid at desk grade this cycle: the Koide aggregation supply (N ≈ 1.5×10¹⁸, nine
orders of headroom), the gate's sharpness (n_eff ≥ 35, hard-step class, conditional on
winding-seed identity), the n_s linearity (shot additivity, shared with A_s). Everything else
in the corpus is derived, priced, or dead with a receipt.
