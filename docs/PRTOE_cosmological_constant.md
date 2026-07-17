# The Cosmological Constant from Vacuum Occupancy

> **The flagship's grade — the "+1.5%" read straight.** The dark-energy scale ρ_Λ¼ = 2.284 meV
> against the observed 2.25 is not a **+1.5% prediction**. The chain's last free number is
> τ = T_c/m_e, and T_c has **no independent source**:
>
> | route offered | what it actually is |
> |---|---|
> | "T_c = τ·m_e" | **circular** — τ ≡ T_c/m_e |
> | the perturbative CW route | **log-ambiguous ~[40, 900] keV**, and gives **193**, not 179 |
> | the lattice band T_c/√σ ≈ 0.34–0.37 | an **SU(3)** value; this model's dark sector is **SU(2)** (P-2026-048). Pure-glue anchors disagree ~11% (SU(3) 0.63 vs SU(2) 0.69–0.71). **No SU(2), N_f = 3 number exists.** |
>
> The number's origin is a rounding: `scripts/tau_deconfinement.py` computes one line,
> **`tau_needed = 2.25/ceiling = 0.34506`** — *the observed dark-energy density inverted*. 0.345
> rounded to two decimals is 0.35; 0.35 × m_e = 178.85 keV → adopted as **179 keV**. The three
> +1.5%s in this corpus are **one number**:
>
> > 179/176.32 = **+1.52%**  ·  0.35029/0.34506 = **+1.52%**  ·  ρ_Λ¼(179)/2.25 = **+1.52%**
>
> So the headline agreement is the gap introduced by rounding the observed density to two decimals.
> What is real: (i) the *structure* ρ_Λ¼ = (9/2)α⁴·τ·m_e — the dark-energy scale as α⁴ times a
> temperature tied to the electron — which makes the sector predictive **once τ is sourced**;
> (ii) the back-solved τ = 0.345 **lands inside the QCD-like lattice band**, a real but **weak**
> check (the band is 8.5% wide, and it is the wrong gauge group). What would make it a prediction:
> **a lattice T_c/√σ for SU(2) with N_f = 3** — the number P-2026-048 bets on, and the number
> nobody has computed.


> **Whose coupling is whose — the flagship's two fields.** ½α_c²M₂ hides that
> the dark-energy scale is a **cross of BOTH dark fields**, not one field's product. Substituting
> α_c = d·α and M₂ = α²·T_c collapses it to a closed form (verified identical to 4×10⁻¹⁹):
>
> > **ρ_Λ¼ = (d²/2)·α⁴·T_c = (9/2)·α⁴·T_c = 2.2842 meV** *(observed 2.25; +1.5%)*
>
> | factor | owner | why |
> |---|---|---|
> | **α⁴** = α_c² × α² | **the dCDF** | α_c² is its **binding**; α² is the **EM handshake** — and α is the dCDF's own coupling because **light is its massless Goldstone** ([PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md) §4) |
> | **T_c** | **the dyad** | its condensation temperature, 179 keV *(the ratio τ = T_c/m_e is what's derived-and-rounded; 179 keV itself is not independently sourced — flagship-grade block)* |
> | **d²/2 = 9/2** | **geometry** | d = the spatial dimension (the same 3 as in α_c = 3α) |
>
> **Neither field produces the number alone**: the dark-energy scale is the dCDF's coupling raised
> to the fourth **weighing the dyad's condensation temperature**. *(Decomposition:
> [PRTOE_build_2loop_Veff_spec.md](PRTOE_build_2loop_Veff_spec.md).)*


> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*Status:* ***exploratory*** *— conditional on: the occupancy
argument (argument-grade, §4), α_c = 3α (a pre-registered bet, currently being decided
by a running MCMC), and the condensate's EFT mass scale (derived within the effective
theory, with the consistency caveat of §2c stated in full). The measurement that can
kill this page within weeks is named in §5.*

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

**Measured: ρ_Λ^{1/4} = 2.25 meV. Agreement: 1.5% (1.01×) — but see the flagship-grade block above: that 1.5% is the τ = 0.345→0.35 rounding, not a sourced prediction; zero adjustable
parameters in the final step.**

**(c) The provenance of M₂.** M₂ is fixed two ways that now agree: the condensate's
effective-theory dictionary (a ghost-condensate-class EFT, M₂⁴ = X₀²P₂) puts it in a
natural band 2.7–9.7 eV, and the electromagnetic handshake gives M₂ = α²·T_c = 9.53 eV
once T_c is pinned at ≈179 keV by the dark sector's confining dynamics (below). So M₂ is
*derived* from T_c, not selected to hit the answer: the chain runs one way —
m_e → T_c → M₂ → ρ_Λ = 2.28 meV. **The 1.5% is not a sourced prediction** (T_c is the observation inverted-and-rounded — see the flagship-grade block); the *structure* of this one-way chain is what would make it one, once T_c/√σ is computed for SU(2).
The free inputs are the portal (√σ_dark = m_e, below) and α_c = 3α (under MCMC test).

**A closed form for the scale.** The dyad and the condensate communicate only through the shared
electron, and both couplings are electromagnetic, which fixes the condensate's mass scale as
M₂ = α²·T_c (T_c the dyad's condensation temperature). The dark-energy scale is then a closed form
whose only dimensionful input is the electron mass:

$$\rho_\Lambda^{1/4} = \tfrac{1}{2}\alpha_c^2\,M_2 = \tfrac{9}{2}\,\alpha^4\,\tau\,m_e, \qquad \tau \equiv T_c/m_e .$$

The α⁴ scaling is derived — the condensate's own binding (α_c²) times the electromagnetic handshake (α²).
The one order-one number left is **τ = T_c/m_e**. **The corpus's 0.345 is what the observed value
fixes it at — the problem, not the answer:** 2.25/((9/2)α⁴m_e) = **0.34506**, the observation inverted. If the observation fixes τ, the chain runs *backward* and
ρ_Λ¼ = 2.25 by construction — a 0.0% match, not the +1.5% prediction §2 claims from the same file.
**The model's τ is 0.3503** (T_c = 179 keV ÷ m_e; P-2026-048 amended). See
[PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §2 for why T_c = 179 keV is itself not
independently sourced.

**What is derived, and what is not.** τ is not a free dial. In the proposed **dark confining sector** — a
"dark colour" force whose condensation *is* the dyad, with its scale pinned to the electron mass — τ is
the chiral-transition-to-string-tension ratio of a QCD-like theory, a near-universal value ≈ 0.34–0.37
that places ρ_Λ¼ at **0.99–1.07×** the observed 2.25 meV. (This sector sets the dark-energy *binding scale*
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
*(The group that supplies that crossover is now named: the finiteness balance selects a dark
**SU(2)** sector, whose pseudo-real fundamental makes its baryons **bosonic diquarks** — the
canonical diquark-BEC realization of this very crossover, and the origin of the s-wave channel
§4c selects. Registered as **P-2026-048**, with the one uncomputed number that decides it.)*
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
 ⟨ρ_m⟩ → 0 ⟹ **Λ → 0** (ramp-confirmed). **KP cannot seat dark energy where it is observed.**
 *Scope:* this falsifies KP as the mechanism for the residual Λ VALUE; KP-sequestering as
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
dig (the three-door guideline; a diagnostic, not an executioner). **The O(1) coefficient
(`scripts/kubo_freeze.py`):** the *full* phonon thermal excitation at the
freeze T = m_ν over-predicts by 3.2× (ρ¼ = (π²/30 c_s³)¼ m_ν = 7.1 meV), confirming Λ is the
*suppressed residual*, not the full sum. **The 7.1 does not descend to 2.70 — there is no such
step.** The two are *independent* readings, not a chain:
16π²α_c^{3/2} = **0.5115**, and 7.1 × 0.5115 = 3.63 while 7.1 × 0.5115¼ = 6.00 — **neither is 2.70**.
Where 2.70 actually comes from is the perturbations door's own formula, ρ = E_b⁴/(16π²c_s³) with
c_s = √α_c:

> **ρ¼ = E_b/(16π²α_c^{3/2})¼ = 2.2842/0.84585 = 2.701 meV**

**And the factor is not a suppression.** In that formula it is a **divisor < 1**, so it *raises*
the flagship binding by **+18.2%** — an **enhancement**. The full phonon sum's role is unchanged and
still holds: it over-predicts by **3.2×**, which is what licenses reading Λ as a residual rather
than the full sum. But the residual's *size* is not obtained by applying the phase-space factor to
7.1. So the thermal-door scale (2.25 meV, forward) and the perturbations-door coefficient (2.701)
are **one number to ~20%** — the honest statement — and the owed O(1) (effective mode count g_*,
the exact Landau cap) is the gap between **E_b and E_b/(16π²α_c^{3/2})¼**, not between 7.1 and 2.70. **Located precisely:** the
flagship E_b = ½α_c²M₂ = 2.284 meV (**1.5% high**) and the tie m_ν = 2.250 meV agree to **1.5%** and
both sit at the observed 2.25; the perturbations 2.70 is the *un-cancelled* full phonon sum
(+18%, exactly the phase-space factor). The one-number demand reduces to the cancellation
fraction f = (2.25/2.70)⁴ = 0.48 — which is **not** the phase-space factor (0.51), so the
equilibrium identity does not simply "remove the measure"; f is a partial Gibbs–Duhem
cancellation on the mode sum — **the genuinely un-built calculation, and it stays un-built.**
*(An equipartition reading — f = ½ from a zero-point K = V split, giving 2.27 meV — was tried and
**failed** on two independent grounds. (i) The number is not independent: 16π²α_c^{3/2} = 0.5115 ≈ ½,
so ½-of-2.70 = 0.994 × E_b — the flagship binding energy re-packaged, and E_b is itself the observed
ρ_Λ inverted-and-rounded, so the "+0.9%" is not fresh evidence. (ii) The mechanism is invalid: a
harmonic condensate mode is honestly **w = 0** (⟨w⟩ = (n−2)/(n+2) = 0 at n = 2 — the textbook reason
an oscillating scalar is cold dark matter), not w = −1; the (+1, −1) split reads classical pure-state
extremes off a stationary quantum ground state, and the "redshift only the kinetic half" rescue
violates the uncertainty principle. The only honestly w = −1 object is the static potential floor V₀
at coefficient **1** → 2.70 meV (+20%), value un-sourced — no home for a ½. **What DOES survive
(the other half):** the ¼ + ¼ split is exact, and both halves together give w = 0 = **cold dark
matter** — which is just the dCDF's own excitation sector (dust-like below z_on) re-confirmed by the
virial theorem. So the analysis correctly identifies the condensate mode as *dark matter*; it only
fails to give the *dark-energy* value. A consistency check with the two-era dCDF, not a new result —
and a reminder that in a unified DM+DE fluid the "residual" and the "excitation" are the same
object's two faces. Autopsy in [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md); full debate in
[Thermal_Half_Discussions.md](threaded_physics_working/Thermal_Half_Discussions.md).)*

**What the door's cap actually is, and what therefore cannot fix it.** The cap is **E_b itself**,
and §2(a) derives E_b as the *universal two-body form* ½α²M — the **ℓ = 0 Coulomb ground state**,
the dark Rydberg, spherically symmetric by construction. It is **not a BCS pairing gap**. So no
gap-anisotropy weighting and no pair-counting of collective modes bears on it: those act on a
many-body gap, and this is a two-body bound state. **The perturbations door sits at +20.0%
(ρ¼ = 2.701 meV) with its O(1) owed** — and the owed object is named: the partial Gibbs–Duhem
cancellation f, not a cutoff artifact.

**A physical reading of the cancellation f (argument-grade).** The "partial cancellation" that
takes the un-cancelled sum (2.70) down to the observed residual (2.25) has a standard superfluid
identity: it is the **renormalization of the reference zero-point.** The two doors are two
*different* objects. **Door B (2.70) = the raw phonon zero-point sum** ½Σℏω_k over the Goldstone
modes (ω = c_s k up to the E_b cutoff, c_s = √α_c) — a UV-divergent *reference vacuum*, present with
or without the condensate and absorbed into the bare Λ. **Door A (2.28) = the condensation energy**
½α_c²M₂ — the order-parameter-dependent depth of the Mexican hat, the physical energy difference
between the condensed and un-condensed vacuum (the superfluid analogue of the BCS condensation
energy ½N(0)Δ²). The physical dark energy is the **condensation energy** — the vacuum shift the
condensate actually causes — so the flagship correctly reads Door A (2.28, +1.5%), and 2.70 is the
reference it sits on, not a competing prediction. **Crucially this does not lean on
16π²α_c^{3/2} ≈ ½** — the coincidence that sank the equipartition reading — it is
condensation-vs-reference, pure superfluid logic. *(Two caveats stay live: (i) it fixes **which
door**, not the **value** — Door A's magnitude still rides on τ = T_c/m_e = observation-inverted, so
the flagship's τ-sourcing gap is untouched; (ii) the quantum correction is **O(1), not small** — the
zero-point/mean-field ratio 1/(16π²c_s³) = 1.955 because c_s = √α_c = 0.148 is small — so an
irreducible ~O(1) strong-coupling piece remains, the same un-built number, pinned only
non-perturbatively by the SU(2) lattice. A first route that tried to make the Goldstone shift
symmetry zero the zero-point outright **fails** — shift symmetry makes the vacuum energy
θ-independent, i.e. constant, not zero; see
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md).)*

**What the O(1) actually is, and why the +1.5% is exposed to it.** The residual O(1) is not a
mystery fraction — it is the **soft-phonon quantum correction** to the condensation energy, and it is
O(1) for a specific reason. A normal 1-loop correction carries 1/16π² = 0.6% (negligible); but the
small sound speed c_s = √α_c = 0.148 makes the soft phonon zero-point pile up as 1/c_s³ ≈ 309, which
**overwhelms the loop factor** — their product is the same **1.955** that appears as the door gap. So
the correction to the mean-field is genuinely O(1), *not* percent-level. Two consequences, both
honest. **(a) The +1.5% is a mean-field (leading-order) agreement**, and the phonon correction is
**positive**, so it pushes ρ_Λ¼ *up, away* from 2.25 (a 30%-of-mean-field finite correction → +8.4%;
the full correction → the +20% perturbation door). The flagship is **exposed** to this O(1), not
protected by it. **(b)** This is exactly the honest **0.99–1.07× band** noted above — that band *is*
this soft-phonon correction. *Skeptic both ways:* the 1.955 is the **raw, unrenormalized** sum, so
the physical finite remainder can be smaller — but the soft-phonon enhancement means the **default is
O(1)** and the burden is on showing it small; nothing in the model does that yet. Pinning it needs
the dCDF quartic coupling (the compositeness Λ, g) and a relativistic renormalized
ground-state-energy calculation — un-built, but now **named** rather than mysterious.

**The partial wave is data-selected, and it is s-wave.** A Coulombic two-body spectrum is
E_n = ½α_c²M₂/n², and partial wave ℓ requires n ≥ ℓ+1 — so the channel picks the level:

| channel | lowest allowed level | E_b | vs observed 2.25 |
|---|---|---|---|
| **s-wave (ℓ = 0)** | 1s | **2.284 meV** | **+1.5%** |
| p-wave (ℓ = 1) | 2p | 0.571 meV | −74.6% |
| f-wave (ℓ = 3) | 4f | 0.143 meV | −93.7% |

**The flagship's 1.5% agreement requires ℓ = 0**, so the hydrogenic form is not a choice but a
selection — the same way f̄'s coupling form is
([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §1). The mechanism behind it: the medium is
**He-3-A missing its baryonic matter**. He-3 pairs p-wave *because* its baryonic hard core
suppresses ℓ = 0 — chiral superfluidity is not intrinsically p-wave; helium is made of baryons.
A medium with no baryonic core leaves s-wave unsuppressed, which is exactly the channel the data
selects. *(The finiteness balance independently selects a dark **SU(2)** sector, whose pseudo-real
fundamental makes its baryons **bosonic diquarks** — the canonical diquark-BEC realization of the
BCS–BEC crossover §4 requires, and the origin of the scalar/s-wave channel. Registered as
**P-2026-048**, candidate grade, with the one uncomputed lattice number that decides it.)*

**The chirality and the generation count are sourced elsewhere, and ℓ = 0 does not touch them.**
The medium's handedness comes from the genesis pour's **winding integer n** — the three-membered
family (matter / magnetism / metric) is one integer, carried by
[PRTOE_igmf_helicity.md](PRTOE_igmf_helicity.md), [PRTOE_lss_parity.md](PRTOE_lss_parity.md),
[PRTOE_baryogenesis.md](PRTOE_baryogenesis.md) and
[PRTOE_gravitational_waves.md](PRTOE_gravitational_waves.md), none of which draw on a pairing
channel. The generation count is forced by **Pauli finiteness**: str[k₁] = 16·N_gen − 48 = 0 ⟹
N_gen = 3 uniquely (**P-2026-045**). Neither rides the medium's partial wave.

**Grade: the DE value's *structure* stands (ρ_Λ¼ = (9/2)α⁴τ·m_e); its "1.5%" is the τ rounding, not a sourced prediction (flagship-grade block), and becomes one only with a lattice T_c/√σ for SU(2); the perturbations door's O(1)
is un-built and its owed object is named.** Menu-watched, not read:
Λ^{1/4} ≈ 2.25 meV sits ~10× today's photon temperature — the known cosmic
near-coincidence, unclaimed.

## 5. Falsification conditions

(i) the running α_c measurement lands > 2σ from 3α (the triangle loses a leg);
(ii) DESI DR3 establishes w ≠ −1; (iii) the thaw chain's posterior excludes zero;
(iv) Σm_ν measured robustly above ~70 meV, or inverted ordering; (v) the pairing-gap
computation failing to sustain k ≈ 1.36 unravels the hierarchy leg.

## Where the dead ends live

Four dead ends set this file's honest grade. The "residual IS the dressing" identity
downgraded to *suggestive* once run at 3α (0.846 vs 0.835); the triangle's "0.1% match" turned out to *select* the free dial x₀ rather than pin it; and two attempts on the perturbations door's O(1) — a pair-count of the collective modes, and a nodal-gap weighting borrowed from the He-3-A order parameter — were raised and retired, the first excluded by the measured LHY coefficient, the second a category error against §2(a)'s two-body s-wave binding. All are logged in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) (the mathematical self-audit and the
superseded-claims index) — which is why §2 states the closure as occupancy *without* leaning
on the identity.


## References

[Planck 2018] (the measured ρ_Λ); Volovik, *The Universe in a Helium Droplet*
(vacuum-as-condensate precedent); [Sakharov 1967] (the induced-action ancestry).
Full entries: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md); derivation chain: the internal hunt
log; the thermal-door arc.
