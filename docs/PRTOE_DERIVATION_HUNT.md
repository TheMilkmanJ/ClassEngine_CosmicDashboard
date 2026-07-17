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
  NEVER THERMALISED with the SM** (then ΔN_eff → 0 and the roster survives, at the price of a hard upper
  bound on the portal coupling). Registered as the fifth kill of **P-2026-048**. CMB-S4 (±0.03) tests it
  either way. (`scripts/dark_neff_su2.py`; predecessor `scripts/dark_neff.py`, `scripts/tau_deconfinement.py`.)
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
  the last relativistic friction partner (heavier species go NR earlier), so it sets the final freeze:
  ρ_Λ¼ = m_ν,lightest, forward at the scale (O(1) coefficient owed — the condensate's specific heat at
  freeze). See [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md).
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
- **Owed:** the count runs over fermions and gauge bosons only. The Higgs scalars enter the same
  coefficient generically as (1/6 − ξ_H), so the exact-zero balance is ξ-independent only if the induced-G
  scalar weight is zero — otherwise it requires ξ_H = 1/6, the same input the G *value* needs. Verifying
  the scalar coefficient (Visser 2002, Eq. 35) is owed; P-045 carries this caveat.
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
> SU(3)'s 1.0). **Verdict: τ = 0.3503 is plausible and in-band, but sits *below* the estimate's
> centre — reachable at the strong-reduction edge, not where the mechanism centrally points; the
> lean is modestly against it, and only an uncomputed SU(2) N_f = 3 lattice T_c/√σ decides it.**
> *Assumptions, named:* dark quarks Dirac and in the fundamental — adjoint or Weyl/Majorana content
> changes the counting. *Also owed:* the ΔN_eff footprint (§3) is priced for the existing roster and
> would need re-pricing at N_c = 2; and the SU(2) N_f ≥ 2 chiral transition is reported **first
> order**, which should be checked against the settling-attractor requirement in
> [PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md) §5 (different transition, but worth the check).

The medium's microscopic content is the **paired lepton-sector vacuum** — leptophilic by identity, with
three flavours (see the flag above — the α_c receipt is retired; the finiteness candidate is live), neutrinos interior (c = 9/10), and a
lepton-number-breaking Goldstone (the
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
- **A_s = (α_c/4πk)³ — candidate:** the shot-noise closed form. Its pieces are more mechanized than the
  "highest-risk" label suggests: **k = ln(1+π/2α_c)/π is a genuine screened-interaction
  integral** k = (1/π)∫₀¹ dq/(q + 2α_c/π) — the effective gap-equation coupling, audited into the Eliashberg
  window [1.35, 1.37], *not* a landing fit; the **4π is the standard 1-loop factor**, and the **cube is the
  three spatial dimensions**. So A_s = 1/N with N = (4πk/α_c)³ assembles from a derived coupling, a loop
  factor, and 3D. The genuine residual is the exact O(1) **normalization of the shot-noise count** (the
  "count C" — whether the assembly is exactly (4πk/α_c)³), which lands A_s to −0.35%. Deliberately exposed;
  referees are the live zero-parameter run and the Eliashberg k-audit.
- **n_s = 1 − 2/ln(M_Pl/T_on) — derived-estimate:** the census drift; the "2" is the open spatial
  dimensions.
- **z_on ≈ 3.56×10⁷ — fast-profiled estimate,** chain-graded later.
- **The bounce:** ρ_bounce is finite (quantum pressure guarantees a floor; a repulsive amplitude quartic
  sets its value). See [PRTOE_bigbang_no_singularity.md](PRTOE_bigbang_no_singularity.md).

---

## 8. What remains owed

1. **The portal √σ_dark = m_e** — the one irreducible input of the dark-energy / basement sector (§2, §6).
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
