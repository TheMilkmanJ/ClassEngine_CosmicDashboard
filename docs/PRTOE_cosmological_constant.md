# The Cosmological Constant from Vacuum Occupancy

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*Status:* ***exploratory*** *— conditional on: the occupancy
argument (argument-grade, §4), α_c = 3α (a pre-registered bet, currently being decided
by a running MCMC), and the condensate's EFT mass scale (derived within the effective
theory, with the consistency caveat of §2c stated in full). The measurement that can
kill this page within weeks is named in §5. (Consolidated 2026-07-13; the occupancy
argument integrated from its addendum.)*

---

## 1. The problem as the field states it

Quantum field theory prices the vacuum by summing zero-point modes up to a cutoff:
ρ_vac ~ Λ⁴. With Λ at the Planck scale this exceeds the observed dark-energy density by
~120 orders of magnitude — famously, the worst prediction in the history of physics.
Mainstream approaches fine-tune the difference, invoke anthropic selection, or defer
the question.

## 2. This model's answer

**One sentence**: gravity does not price the vacuum by loop integral; it prices it by
*occupancy* — one binding quantum per coherence cell — and the binding quantum is
exponentially small because it sits at the bottom of a pairing hierarchy.

**(a) The value.** The condensate binds at its own hydrogen-like scale (the universal
two-body form E_b = ½α²M, applied to the condensate's coupling α_c and its EFT mass
scale M₂):

$$E_b = \tfrac{1}{2}\,\alpha_c^2\,M_2, \qquad \alpha_c = 3\alpha = 0.021892,\quad M_2 = \alpha^2 T_c = 9.53\ \text{eV}$$

$$E_b = 2.28\ \text{meV}$$

**(b) The occupancy statement.** The vacuum's gravitating density is one binding
quantum per coherence cell of volume 1/E_b³:

$$\rho_\Lambda = E_b^4 \quad\Longrightarrow\quad \rho_\Lambda^{1/4} = 2.28\ \text{meV}$$

**Measured: ρ_Λ^{1/4} = 2.25 meV. Agreement: 1.5% (1.01×), zero adjustable
parameters in the final step.**

**(c) The provenance of M₂.** M₂ is fixed two ways that now agree: the condensate's
effective-theory dictionary (a ghost-condensate-class EFT, M₂⁴ = X₀²P₂) puts it in a
natural band 2.7–9.7 eV, and the electromagnetic handshake gives M₂ = α²·T_c = 9.53 eV
once T_c is pinned at ≈179 keV by the dark sector's confining dynamics (below). So M₂ is
*derived* from T_c, not selected to hit the answer: the chain runs one way —
m_e → T_c → M₂ → ρ_Λ = 2.28 meV — a genuine 1.5% prediction against the observed 2.25.
The free inputs are the portal (√σ_dark = m_e, below) and α_c = 3α (under MCMC test).
(An earlier draft quoted M₂ as a *selected* value with "4 parts in 10⁴" agreement — that
precision was circular — and added a loop-dressing factor that was input-inconsistent;
both are retired in the public failures ledger.)

**A closed form for the scale.** The dyad and the condensate communicate only through the shared
electron, and both couplings are electromagnetic, which fixes the condensate's mass scale as
M₂ = α²·T_c (T_c the dyad's condensation temperature). The dark-energy scale is then a closed form
whose only dimensionful input is the electron mass:

$$\rho_\Lambda^{1/4} = \tfrac{1}{2}\alpha_c^2\,M_2 = \tfrac{9}{2}\,\alpha^4\,\tau\,m_e, \qquad \tau \equiv T_c/m_e .$$

The α⁴ scaling is derived — the condensate's own binding (α_c²) times the electromagnetic handshake (α²).
The one order-one number left is **τ = T_c/m_e**, which the observed value fixes at 0.345.

**What is derived, and what is not.** τ is not a free dial. In the proposed **dark confining sector** — a
"dark colour" force whose condensation *is* the dyad, with its scale pinned to the electron mass — τ is
the chiral-transition-to-string-tension ratio of a QCD-like theory, a near-universal value ≈ 0.34–0.37
that places ρ_Λ¼ at 0.97–1.07× the observed 2.25 meV. (This sector sets the dark-energy *binding scale*
only; the dark matter remains the medium's own excitations. The derivation, and why a QCD-like sector is
required, are in the open-derivations document.) What the model does **not** derive is the pinning — *why* the
dark scale equals the electron mass. That one input is irreducible: it is the meV coincidence
ρ_Λ ~ α⁴m_e, and it cannot be derived without spoiling the value of τ. So the honest reading: the
dark-energy *scale* follows a derived closed form in α with a single dimensionful input, the electron
mass; the value lands within a few percent; and the one un-derived step is stated plainly, not hidden.

**(d) Why the 10¹²⁰ never appears.** The Λ⁴ catastrophe is the *loop-pricing* of the
vacuum — a mode sum. In this framework the condensate's ground state *is* the vacuum,
and its gravitating energy is its *binding* energy — an occupancy count. The mode sum
is the wrong accounting: it double-counts fluctuations that the no-bare-terms principle
(the framework's founding axiom) assigns to the substrate, not to the emergent
stress-energy.

**(e) Why so small.** E_b is doubly suppressed: a small coupling squared (α_c²) acting
on M₂ ~ 10 eV, which itself sits at the bottom of the pairing exponential
M ~ M_red·e^(−1/kα_c) — the same exponential this model uses for the electroweak
hierarchy. The smallness is inherited twice, tuned zero times.

## 3. Consequences already in force

- ρ_Λ^{1/4} equals the lightest neutrino mass (the model's dark-energy–neutrino tie)
 ⟹ **Σm_ν = 61.4 meV, normal ordering, Majorana mechanism required** — the full
 statement with its caveats lives in the neutrino-sector document.
- w = −1 exactly (a ground state, not a rolling field) — DESI's target.
- The dark-energy floor cannot "thaw" into dynamics (a pre-registered zero, currently
 under test by a dedicated chain).

## 4. Why exactly one quantum per cell (the occupancy argument; argument-grade)

**≥ 1 by stability**: the vacuum is the bound state — every binding mode holds its
quantum or there is no condensate. **≤ 1 by coherence**: one independent mode per
coherence cell by definition — a second quantum in a cell is an excitation, not vacuum.
The two scales coincide because the cell is the binding mode's own wavelength: pinched
from both sides, occupancy is exactly one, and ρ_Λ = E_b⁴ is the unique solution.

**Owned assumption**: this argument holds on the strong-coupling (BEC) side of the
BCS–BEC crossover, where the coherence length equals the bound-state size — verified to
*fail* on the weak-coupling side, which is precisely where the model does *not* use it.
The two sides of condensed matter's most famous crossover perform the two famous jobs
in one vacuum: the weak side's exponential gap digs the electroweak hierarchy; the
strong side's occupancy sets the cosmological constant.

## 4b. Three readings of the same residual

One quantity, three independent readings, one demanded number — the medium's own
consistency structure applied to its most famous problem:

- **The thermodynamic reading — the cancellation:** a self-sustained
 condensate's equilibrium vacuum has **identically zero pressure by the Gibbs–Duhem
 relation** — the enormous vacuum energies do not gravitate at equilibrium (and the
 roster demonstrably cannot pay this bill species-by-species: str[1] = −68 and the
 Veltman-class sum both FAIL — the whole medium does what the parts cannot). The
 observed Λ = the deviation from equilibrium, whose dynamic face is the still-settling
 fountain (below).
- **The background reading — does not fix the value:** on the finite 4-volume, **Λ_eff = ¼⟨T^µ_µ⟩ = ¼⟨ρ_m⟩**. The self-consistent
 closed-universe solve gives coefficient **0.40, not the toy ¾**, so Λ¹ᐟ⁴ = 1.48 meV (0.66×). But the
 fatal, coefficient-INDEPENDENT problem is the RATIO: the a³ 4-volume weight always favors max-a (where
 ρ_m is minimum), so **Ω_Λ/Ω_m ≤ 0.40 across the entire expansion** (ramp-confirmed: monotonic to a max
 of 0.398; coefficient sweep tops out ~O(1) with no closed solution above C≈0.5) — a factor **5.5 below
 the observed 2.2**. And for the model's OWN eternal-expansion fate (flat torus → infinite 4-volume),
 ⟨ρ_m⟩ → 0 ⟹ **Λ → 0** (ramp-confirmed). **KP cannot seat dark energy where it is observed.** The
 earlier "0.76× from a mechanism" matched the value's *decade* by tuning turnaround~now while hiding the
 ratio failure. *Scope:* this falsifies KP as the mechanism for the residual Λ VALUE; KP-sequestering as
 the vacuum-CANCELLATION (the thermodynamic door below) is a separate, untouched claim.
- **The thermal door — the residual's dynamics**: the candidate
 chain is now end-to-end mechanism-shaped — the deviation is EXPANSION-SOURCED (free decay
 would die by e^{−10⁵}; the settling law is an attractor), the friction partner is the
 neutrino bath (the medium's only tree-level coupling; the friction turns on where
 free-streaming turns off), and the freeze is a **decoupling, not a rate-crossing**: the
 condensate stays thermally locked to the *relativistic* neutrino bath (the friction rate
 runs Γ/H ≈ 5×10¹⁰ ≫ 1 — the tracking condition, computed forward), and the settling
 freezes when that bath goes non-relativistic and quits at T = m_ν. Because the **lightest**
 neutrino is the *last* relativistic friction partner (heavier species go NR earlier, at
 z ≈ 300, 50; the lightest at z ≈ 12), it sets the final freeze — **forward-explaining the
 registered tie ρ_Λ¼ = m_ν,lightest = 2.25 meV**: the last bath to quit sets the frozen
 excitation scale. **w = −1 exact through the observable range, untuned; the settling's ash
 banks as dark matter (the drain, the fluid's own dust face); the frozen residual is Λ.**
 Candidate grade: the amplitude *scale* is now FORWARD via the neutrino-decoupling
 freeze-out (`scripts/kubo_freeze.py`); the earlier √N *lineshape-suppression* route (the
 "Γ₀ = 76 meV" target) is retired as an inversion artifact — the collisionless neutrino
 response is Ohmic in **both** the density and the scalar (Majoron) channel, so no
 sub-Ohmic lineshape exists to supply it. The one **owed** piece is the O(1) coefficient of
 the frozen equilibrium excitation (exactly m_ν, or c·m_ν?), which needs the condensate's
 specific heat / equation of state at freeze. The original statement stands beneath it: the condensate is **still settling from the one
 genesis injection** — thermal counterflow (the fountain effect, the corpus's own
 genesis name) persists while any deviation from the T = 0 ground state remains, dying
 only asymptotically (the third law's ramp). The residual excitation of a nearly-settled
 medium is small — today's gradients are CMB-uniform at the 10⁻⁵ class — giving Λ's
 smallness qualitatively for free.
- **The perturbations door**: the textbook zero-point mode sum —
 **the famous door, and the diagnosis of the famous disaster**: the 10¹²⁰ catastrophe is
 what that door yields when opened *while denying the medium* — fluctuations read
 without the equilibrium that cancels them. In the medium, the bulk of the mode sum is
 cancelled by the equilibrium identity; **the residual = the modes still
 out-of-equilibrium** — the same deviation the other two doors name. The registered
 neutrino tie (ρ_Λ^{1/4} = m_ν,lightest = 2.25 meV; the lightest quasiparticle setting
 the floor's quarter-power; post-hoc flag standing) is this door's sharper artifact.

**The demand this section adds (inherited by the thermal program):** the three residuals —
the Gibbs–Duhem deviation, the residual fountain excitation, the un-cancelled mode sum —
**must be one number.** A confirmed three-way mismatch beyond stated widths is a place to
dig (the three-door guideline; a diagnostic, not an executioner). **The O(1) coefficient,
scoped (2026-07-16, `scripts/kubo_freeze.py`):** the *full* phonon thermal excitation at the
freeze T = m_ν over-predicts by 3.2× (ρ¼ = (π²/30 c_s³)¼ m_ν = 7.1 meV), confirming Λ is the
*suppressed residual*, not the full sum. The suppression is the phonon phase-space-with-
cancellation 16π²α_c^{3/2} — the **same object** the perturbations door pins — which lands
ρ¼ = 2.70 meV. So the thermal-door scale (2.25 meV, forward) and the perturbations-door
coefficient (2.70) are **one number to ~20%**; the residual 20% (effective mode count g_*,
the exact Landau cap) is the owed O(1) refinement. **Located precisely (2026-07-16):** the
flagship E_b = ½α_c²M₂ = 2.284 meV (1.3% high) and the tie m_ν = 2.250 meV agree to 1% and
both sit at the observed 2.25; the perturbations 2.70 is the *un-cancelled* full phonon sum
(+18%, exactly the phase-space factor). The one-number demand reduces to the cancellation
fraction f = (2.25/2.70)⁴ = 0.48 — which is **not** the phase-space factor (0.51), so the
equilibrium identity does not simply "remove the measure"; f is a partial Gibbs–Duhem
cancellation on the mode sum. **f is ½ — the pair count (2026-07-16).** The door's sum was run
over the full d³k sphere, counting **k_up and −k_down as two independent modes**. They are not:
in this medium the excitation *is* the (k↑, −k↓) twin — the same object the entanglement seating
calls "a Cooper pair, entangled by construction" ([PRTOE_quantum_trio.md](PRTOE_quantum_trio.md)
§2) and the Koide self-dual reading calls one object's two faces, the −k_down variance face
*equal to* the k_up mean face ([PRTOE_koide_relation.md](PRTOE_koide_relation.md)). One pair is
**one** collective degree of freedom, so the full-sphere sum double-counts it. Counting pairs:

| door | ρ¼ | vs observed 2.25 |
|---|---|---|
| thermal / ν-tie | 2.250 meV | — |
| flagship ½α_c²M₂ | 2.284 meV | +1.5% |
| perturbations, **pair-counted** | **2.271 meV** | **+0.9%** |

**The three doors are one number to 1.5%** — the model's own flagship precision — down from the
~20% spread the un-paired sum showed. And the "genuinely un-built cancellation fraction" is the
**integer 2**: f = 0.4817 against the pair factor 0.5000 (4% in f, 0.9% in ρ¼). The earlier
reading rejected the phase-space 0.51 and never tested 0.50.

**The consistency audit — the tension this must survive, and its one escape (2026-07-16).** A
factor introduced to fix one number must hold everywhere it applies. Running it out:
- **The thermal door is safe.** Thermally excited phonons at +k and −k *are* independent (one can
  exist without the other), so the full-sphere count is right there — and helium's measured phonon
  C_V = (2π²/15)T³/c³ confirms it. The pair claim touches the **ground-state zero-point**, not the
  thermal quasiparticle census; the ν-tie is untouched.
- **The ground-state zero-point is the tension.** Textbook *bosonic* Bogoliubov gives
  E₀ = ½Σ_{all k}(ω_B − ε_k − gn): the ½ *is* the zero-point half, and the sum already runs over the
  full sphere. That object is the LHY term, (8/15π²)m⁴c_s⁵ — **measured** in ultracold Bose gases
  [Navon 2011; Papp 2008; Bose–Bose droplets] at the **un-halved** coefficient. So as a *general*
  rule for condensate zero-points, the halving is **excluded by laboratory data**.
- **The escape, and it is the model's own identity.** The LHY is a *bosonic, unpaired* BEC result.
  This medium is **He-3-A class** — a **BCS-paired fermionic** superfluid ([PRTOE_INDEX.md](PRTOE_INDEX.md);
  [PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md)) — and the corpus reads its excitations in
  Cooper-pair grammar throughout. A paired condensate's ground state is built from pair operators;
  an atomic BEC's is not. The bosonic LHY may simply be the wrong comparison object.
- **But the escape has a price**, and it is named here rather than hidden: the corpus also insists
  the doors "belong to the *condensate grammar*, not to any particular condensate"
  ([PRTOE_quantum_trio.md](PRTOE_quantum_trio.md) §3) — the same faces in a helium cell as in the
  vacuum. That universality claim **cuts against** a counting rule that holds for the medium but
  not for a lab BEC. Either the rule is pairing-specific (and the universality claim needs the
  qualifier "paired condensates"), or the halving is wrong and the 0.9% hit is coincidence.

**The He-3-A comparison, run (2026-07-16) — and then RETRACTED the same day by its own
consistency check. Read the retraction in §4c below before using any number in this block.**
The argument was: **He-3-A is the chiral p-wave (ABM) state**, order parameter Δ(k̂) ∝ (k̂ₓ + ik̂_y),
so |Δ(k̂)| = Δ₀·**sin θ** with **point nodes** on the l̂ axis; the chirality and the nodes are the
*same structure*, and the corpus has **banked** that chirality (IGMF helicity, LSS parity, the
birefringence null), so the nodes are not optional. The door caps its mode sum *at the pairing
gap*; if the gap is nodal, the cap is not a sphere, and the angular integral carries
⟨sin⁴θ⟩ = **8/15**:

| candidate | f | ρ¼ | vs observed | standing |
|---|---|---|---|---|
| required by data | 0.4817 | 2.250 | — | — |
| **He-3-A nodal gap** | **8/15 = 0.5333** | **2.308 meV** | **+2.6%** | **identity-forced, LHY-safe** |
| pair count | 1/2 = 0.5000 | 2.271 meV | +0.9% | fits better; needs a counting rule the measured LHY excludes |
| both applied | 0.2667 | 1.941 meV | −13.7% | **overshoots — mutually exclusive** |

**The two cannot coexist**, and that decides it: the nodal weighting is *forced* by an identity
already spent elsewhere, the pair count is *elective* and carries the LHY tension — so the
**nodal reading is the principled one, and the better-fitting pair count is retired**. The
better-fitting answer loses to the forced one. Result: the door goes from **+20.0% to +2.6%** on
the model's own identity, and the three doors (tie 2.250, flagship 2.284, perturbations 2.308)
are **one number to 2.6%**.

## 4c. RETRACTION of the He-3-A door result, and the incoherence it exposed (2026-07-16)

**The block above is retracted.** Its own consistency check — feeding the anisotropy back through
E_b, promised as an owed item and then run — kills it. **E_b is not a BCS pairing gap.** §2(a)
derives it as *"the condensate binds at its own **hydrogen-like scale** (the **universal two-body
form** E_b = ½α²M)"* — the ℓ=0 Coulomb ground state, the dark Rydberg, **spherically symmetric by
construction**. The He-3-A argument applied **chiral p-wave nodal geometry to an s-wave two-body
binding energy**. That is a category error, and the ⟨sin⁴θ⟩ = 8/15 weight does not apply to it.
**The door returns to +20.0% (ρ¼ = 2.701 meV); the "three doors to 2.6%" claim is void.** The
pair count stays retired on its own merits (the measured-LHY tension, §4b) — nothing rescues the
door today.

**What the retraction exposed is worth more than the result was.** Three descriptions of the same
object do not cohere, and the incoherence predates this pass:
1. **CC §2(a):** E_b = ½α_c²M₂ — a **two-body, s-wave, hydrogenic** binding energy.
2. **[PRTOE_quantum_gravity.md](PRTOE_quantum_gravity.md) §4:** the vacuum budget is *"capped at
   the **pairing gap**"* — a **many-body BCS** object.
3. **[PRTOE_INDEX.md](PRTOE_INDEX.md) / [PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md):**
   the dCDF is **He-3-A class — chiral p-wave**, and that chirality is *spent* on the parity-odd
   signatures (IGMF helicity, LSS parity, birefringence).

A chiral p-wave condensate's gap is **not** a hydrogenic s-wave Rydberg. So at most two of these
three can stand. The fork, stated so it can be decided rather than blurred:
- **s-wave branch:** E_b's hydrogenic derivation stands → the flagship 1.5% stands → but the
  **He-3-A/chiral identity is then wrong for this field**, and every claim spending that chirality
  is exposed (the parity-odd wing).
- **p-wave branch:** the He-3-A identity stands → the chirality claims stand → but
  **E_b = ½α_c²M₂ is the wrong form**, and the flagship's 1.5% is unsupported as derived.
- **two-field branch (the likely escape, and it is untested):** the He-3-A chirality belongs to the
  **dCDF** (the superfluid piece) while E_b's hydrogenic binding belongs to the **dyad** (the gas
  piece) — the two-field split is already the model's structure. But then the door's cap is a
  *dyad* binding energy while the modes summed are the *dCDF's* phonons, and **the door is
  mixing two fields' scales** — which is its own defect, and is not what §4b says it is doing.

**RESOLVED, same day — the partial wave is DATA-SELECTED, and it is s-wave.** The fork is
decidable by arithmetic the model already carries. A Coulombic two-body spectrum is
E_n = ½α_c²M₂/n², and partial wave ℓ requires n ≥ ℓ+1 — so *the channel picks the level*:

| channel | lowest allowed level | E_b | vs observed 2.25 |
|---|---|---|---|
| **s-wave (ℓ = 0)** | 1s | **2.284 meV** | **+1.5%** ✓ |
| p-wave (ℓ = 1) — the "He-3-A class" reading | 2p | 0.571 meV | **−74.6%** |
| f-wave (ℓ = 3) — the L = 3 the 3-generation count demands | 4f | 0.143 meV | **−93.7%** |

**The flagship's 1.5% agreement *requires* ℓ = 0.** The hydrogenic form is therefore not an
oversight and not a choice — it is **selected by the data**, the same way f̄'s coupling form was
(§1, [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md)). This also confirms the retraction
above from an independent direction: the door's cap is a **two-body Coulomb ground state**, not a
BCS gap, so ⟨sin⁴θ⟩ never applied to it. And §4's owned assumption already placed this argument on
the **strong-coupling (BEC) side**, where the bound state *is* the object and its binding energy
*is* the hydrogenic ½α²M — so E_b is internally consistent with its own stated regime.

**Where the cost actually lands: the chirality wing, not the DE value.** The tension is real and
it is now sharp. The CC needs a **strongly-bound s-wave molecule** (BEC side, ℓ = 0). The dCDF's
structure file claims a **p-wave, parity-odd chiral condensate** ([PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md)
§2) and *spends* that chirality on IGMF helicity, LSS parity, GW handedness, and the AD
matter-asymmetry bias. **An s-wave bound state preempts p-wave pairing in the same channel** — for
one species the s-wave singlet, if strongly attractive enough to form a BEC-side molecule, wins
over the p-wave triplet. They cannot both be the ground state of the same channel. Two further
facts sharpen this rather than soften it: (i) the dCDF file **already flags** that a pure p-wave
(L = 1) "= He-3-A" is **insufficient for 3 generations**, which require L = 3 (f-wave) — so the
He-3-A label was a known-defective candidate before this pass touched it; (ii) both p- and f-wave
are exactly the channels the table above excludes at −75% and −94%.

**How sharp the incompatibility is:** the chirality is not an add-on to the pairing — it *is* the
pairing channel. Per the dCDF file, the number of charge-1 Weyl pairs a chiral gap carries **equals
its angular momentum L**, which is why 3 generations demand L = 3. So ℓ = 0 ⟹ L = 0 ⟹ **zero Weyl
pairs, zero generations**, and a parity-*even* singlet with no θ·R·R̃ and no GW handedness. The
s-wave the DE value demands would take the entire chirality wing with it.

**The mechanism that explains the s-wave selection — and prices it (JP, 2026-07-16).** The reading
"*the medium is He-3-A missing its baryonic matter*" supplies the physics behind the table above.
**In He-3, p-wave pairing is caused by the baryonic hard core**: the atoms are composite (2p+1n+2e),
cannot overlap, and the core suppresses ℓ = 0 — pairing is *forced* up to L = 1. It is not that
chiral superfluidity is intrinsically p-wave; it is that helium is made of baryons. **Strip the
baryonic matter and the hard core goes with it, leaving the s-wave channel unsuppressed** — and an
unsuppressed attractive s-wave channel binds in s-wave. That is exactly the ℓ = 0 the data selects
at +1.5%, and it explains *why* the hydrogenic form was the right one all along.

**And the chirality survives it — because the chirality was never sourced from the pairing
(JP, 2026-07-16).** The medium's handedness comes from **the genesis pour** — the helical roll-up
of the model's one realized white hole ([PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §1;
[PRTOE_white_holes.md](PRTOE_white_holes.md)) — carried by the **winding integer n**, not by the
pairing channel's L. This is checkable against every claim that spends it, and every one traces to
n: magnetic helicity is *"SIGNED BY THE GENOME — sign(helicity_B) = sign(n)"*
([PRTOE_igmf_helicity.md](PRTOE_igmf_helicity.md), P-2026-028); LSS parity is *"the winding n (a
signed integer), the genesis helicity, the vortex network"*
([PRTOE_lss_parity.md](PRTOE_lss_parity.md)); baryogenesis is *"the winding integer times ONE
transmission number"* ([PRTOE_baryogenesis.md](PRTOE_baryogenesis.md)); the GW channel carries *"a
genome signature"* ([PRTOE_gravitational_waves.md](PRTOE_gravitational_waves.md)). **The
three-membered chirality family — matter / magnetism / metric — is one integer n**, a
genesis/topological property. **None of it draws on p-wave L.** So s-wave pairing and the chirality
wing are compatible, and what the ℓ = 0 selection actually kills is
[PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md) §2's *redundant second sourcing* of chirality
from the pairing channel — a source nothing downstream ever used.

**What does lose its home:** the **Weyl-point → 3-generation count**, the one claim that uniquely
needed L = 3 (the Weyl-pair count equals L, so ℓ = 0 leaves no nodes to Z₃-split). The generation
count must come from Z₃ as a family symmetry directly, or from elsewhere — **the owed build is
re-pointed, not cancelled** (§2's banner carries it).

**Status: RESOLVED for the DE value and the chirality wing; one re-pointed debt.** The DE value
stands at 1.5% with its partial wave now *data-selected* and its s-wave channel *mechanically
motivated* (no baryonic core → no ℓ = 0 suppression). The perturbations door returns to +20.0%
with its O(1) still un-built — but it is now un-built for a *stated* reason (the cap is a two-body
Coulomb ground state, and no gap-anisotropy or pair-counting trick applies to it). Today's pass
tried two O(1) fixes, retired both, and found that the DE value was never the fragile part.

**Grade: the door is at +20.0% and the O(1) is un-built** — same as this morning, minus two dead
candidates and plus one named structural fork. The DE *value* is unchanged throughout — it stands
as a 1.5% prediction (flagship / tie). Menu-watched, not read:
Λ^{1/4} ≈ 2.25 meV sits ~10× today's photon temperature — the known cosmic
near-coincidence, unclaimed.

## 5. Falsification conditions

(i) the running α_c measurement lands > 2σ from 3α (the triangle loses a leg);
(ii) DESI DR3 establishes w ≠ −1; (iii) the thaw chain's posterior excludes zero;
(iv) Σm_ν measured robustly above ~70 meV, or inverted ordering; (v) the pairing-gap
computation failing to sustain k ≈ 1.36 unravels the hierarchy leg.

## Where the dead ends live

Two dead ends set this file's honest grade. The "residual IS the dressing" identity
downgraded to *suggestive* once run at 3α (0.846 vs 0.835), and the triangle's "0.1% match" turned out to *select* the free dial x₀ rather than pin it. Both are logged in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) (the mathematical self-audit and the
superseded-claims index) — which is why §2 states the closure as occupancy *without* leaning
on the identity.


## References

[Planck 2018] (the measured ρ_Λ); Volovik, *The Universe in a Helium Droplet*
(vacuum-as-condensate precedent); [Sakharov 1967] (the induced-action ancestry).
Full entries: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md); derivation chain: the internal hunt
log; the thermal-door arc.
