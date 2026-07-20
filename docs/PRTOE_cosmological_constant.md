# The Cosmological Constant from Vacuum Occupancy

> **The flagship's grade.** The dark-energy scale follows the closed form
> ρ_Λ¼ = (9/2)α⁴·τ·m_e, where the α⁴ is derived — the condensate's own binding α_c² times the
> electromagnetic handshake α² — and the single order-one number τ = T_c/m_e is supplied by the
> Koide sector's circulant kernel: Parseval fixes |f₁/f₀| = 1/√2 once Q = 2/3, and τ = −ln|f₁/f₀| =
> **½ln2 = 0.34657** follows. The chain descends from a lepton-mass fact and nothing cosmological
> enters it. It gives **T_c = 177.10 keV** and
>
> > **ρ_Λ¼ = 2.2599 meV against the observed 2.25 — +0.44%.**
>
> **The 0.44% is the whole claim, and the reason is worth stating before anything else.** Inverting
> the observation gives τ = 2.25/((9/2)α⁴m_e) = **0.34506**, which returns 2.25 by construction — a
> perfect match that predicts nothing. The kernel's 0.34657 sits 0.44% above that value, so the gap
> between them is precisely what distinguishes a derivation from a back-solve. **A lattice T_c/√σ
> for SU(2) with N_f = 3 decides it** (P-2026-048), and it must reach 0.22% precision to tell the
> two apart — a demanding number, and nobody has computed it yet.
>
> **What remains conditional:** α_c = 3α is a registered bet under MCMC test, and the portal
> √σ_dark = m_e — why the dark scale equals the electron mass — is the one irreducible input. The
> pinning is not derived and the file says so where it arises.


> **Whose coupling is whose — the flagship's two fields.** ½α_c²M₂ hides that
> the dark-energy scale is a **cross of BOTH dark fields**, not one field's product. Substituting
> α_c = d·α and M₂ = α²·T_c collapses it to a closed form (verified identical to 4×10⁻¹⁹):
>
> > **ρ_Λ¼ = (d²/2)·α⁴·T_c = (9/2)·α⁴·T_c = 2.2599 meV** *(observed 2.25; +0.44%)*
>
> | factor | owner | why |
> |---|---|---|
> | **α⁴** = α_c² × α² | **the dCDF** | α_c² is its **binding**; α² is the **EM handshake** — and α is the dCDF's own coupling because **light is its massless Goldstone** ([PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md) §4) |
> | **T_c** | **the dyad** | its condensation temperature, 177.10 keV — the Koide kernel's τ = ½ln2 times the electron mass |
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

$$E_b = \tfrac{1}{2}\,\alpha_c^2\,M_2, \qquad \alpha_c = 3\alpha = 0.021892,\quad M_2 = \alpha^2 T_c = 9.43\ \text{eV}$$

$$E_b = 2.2599\ \text{meV}$$

**(b) The occupancy statement.** The vacuum's gravitating density is one binding
quantum per coherence cell of volume 1/E_b³:

$$\rho_\Lambda = E_b^4 \quad\Longrightarrow\quad \rho_\Lambda^{1/4} = 2.2599\ \text{meV}$$

**Measured: ρ_Λ^{1/4} = 2.25 meV — the chain lands +0.44% above it, with zero adjustable
parameters in the final step.**

**(c) The provenance of M₂.** M₂ is fixed two ways that now agree: the condensate's
effective-theory dictionary (a ghost-condensate-class EFT, M₂⁴ = X₀²P₂) puts it in a
natural band 2.7–9.7 eV, and the electromagnetic handshake gives M₂ = α²·T_c = 9.43 eV
at the kernel-sourced T_c = 177.10 keV. So M₂ is *derived* from T_c, not selected to hit the
answer: the chain runs one way — m_e → T_c → M₂ → ρ_Λ¼ = 2.2599 meV, +0.44% against the observed
2.25. The free inputs are the portal (√σ_dark = m_e, below) and α_c = 3α (under MCMC test).

**A closed form for the scale.** The dyad and the condensate communicate only through the shared
electron, and both couplings are electromagnetic, which fixes the condensate's mass scale as
M₂ = α²·T_c (T_c the dyad's condensation temperature). The dark-energy scale is then a closed form
whose only dimensionful input is the electron mass:

$$\rho_\Lambda^{1/4} = \tfrac{1}{2}\alpha_c^2\,M_2 = \tfrac{9}{2}\,\alpha^4\,\tau\,m_e, \qquad \tau \equiv T_c/m_e .$$

The α⁴ scaling is derived — the condensate's own binding (α_c²) times the electromagnetic handshake
(α²). The one order-one number left is **τ = T_c/m_e**, and it is sourced.

**τ = ½ln2 = 0.34657**, from the Koide sector's circulant kernel: Parseval fixes the kernel's own
modulus at |f₁/f₀| = 1/√2 once Q = 2/3, and τ = −ln|f₁/f₀| follows. Nothing cosmological enters —
the chain descends from Q, a lepton-mass fact measured to ten parts per million. It gives
**T_c = 177.10 keV** and

> **ρ_Λ¼ = (9/2)α⁴·τ·m_e = 2.2599 meV against the observed 2.25 — +0.44%.**

The distinction that matters: inverting the observation gives 2.25/((9/2)α⁴m_e) = **0.34506**, which
would make the chain run backward and return 2.25 by construction — a 0.0% match dressed as a
prediction. The kernel's 0.34657 sits **0.44% above** that, and the gap *is* the prediction. A
lattice T_c/√σ for SU(2), N_f = 3 decides it (P-2026-048), and must reach 0.22% precision to tell
the two apart.

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
 ρ_m is minimum), so **Ω_Λ/Ω_m ≤ 0.40 across the entire expansion** (monotonic to a max
 of 0.398; coefficient sweep tops out ~O(1) with no closed solution above C≈0.5) — a factor **5.5 below
 the observed 2.2**. And for the model's OWN eternal-expansion fate (flat torus → infinite 4-volume),
 ⟨ρ_m⟩ → 0 ⟹ **Λ → 0**. **KP cannot seat dark energy where it is observed.**
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
 sub-Ohmic lineshape exists to supply it. The O(1) coefficient of the frozen equilibrium
 excitation follows the tie's arrow: the equality's source is the mass-generation
 identity read forward — the tenth-channel seat term, the floor SETTING m₁ — so the coefficient
 rides κ_m = b^(−1/4) ≈ 1, and what survives is the basement-gated seat constant b rather than
 a specific-heat calculation. The original statement stands beneath it: the condensate is **still settling from the one
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
*suppressed residual*, not the full sum. **The 7.1 does not descend to 2.67 — there is no such
step.** The two are *independent* readings, not a chain:
16π²α_c^{3/2} = **0.5115**, and 7.1 × 0.5115 = 3.63 while 7.1 × 0.5115¼ = 6.00 — **neither is 2.67**.
Where 2.67 actually comes from is the perturbations door's own formula, ρ = E_b⁴/(16π²c_s³) with
c_s = √α_c:

> **ρ¼ = E_b/(16π²α_c^{3/2})¼ = 2.2599/0.84569 = 2.672 meV**

**And the factor is not a suppression.** In that formula it is a **divisor < 1**, so it *raises*
the flagship binding by **+18.2%** — an **enhancement**. The full phonon sum's role is unchanged and
still holds: it over-predicts by **3.2×**, which is what licenses reading Λ as a residual rather
than the full sum. But the residual's *size* is not obtained by applying the phase-space factor to
7.1. So the thermal-door scale (2.25 meV, forward) and the perturbations-door coefficient (2.672)
are **one number to ~19%** — the honest statement — and the owed O(1) (effective mode count g_*,
the exact Landau cap) is the gap between **E_b and E_b/(16π²α_c^{3/2})¼**, not between 7.1 and 2.67.
**Located precisely:** the flagship E_b = ½α_c²M₂ = 2.2599 meV (**+0.44%**) and the tie
m_ν = 2.250 meV agree to that same 0.44%, and both sit at the observed 2.25; the perturbations
2.672 is the *un-cancelled* full phonon sum, +18.2% above E_b, which is exactly the phase-space
factor.

**The cancellation fraction is not an independent unknown, and the reason is algebraic rather than
numerical.** Door B is not a separate computation that happens to land nearby — it is *defined* as
E_b/Φ¼ by the perturbations door's own formula above. So f = (door A / door B)⁴ = Φ identically,
for any E_b whatever, and quoting a percentage agreement between them would be quoting a rounding
error. The content is the identity itself: **there is no free coefficient to build here.** What made
it look like there was one was computing f from the *observed* value instead of the model's own:
f = (2.25/2.672)⁴ = 0.503 against Φ = 0.5115, and that 1.7% gap in density is nothing but the
model's own +0.44% gap to the observation raised to the fourth power. One owed item fewer, on an
algebraic ground that does not depend on the value of τ.

The earlier reading of f — as a partial Gibbs–Duhem cancellation on the mode sum — is a different
object, and it remains **the genuinely un-built calculation.**

**Why it stays unbuilt, stated exactly (2026-07-20).** It was scoped as an independent object that
might pay where the perturbative route had stalled. It is neither independent nor payable, for two
reasons that do not share a fix.

*(i) It is not independent of the λ problem — it **is** the λ problem.* The mode sum's *raw* value
is a divergent reference vacuum, absorbed into the bare Λ; the only physical output is the
**renormalized residual**, and for a Bogoliubov spectrum that residual is, by a standard superfluid
identity, precisely the Lee–Huang–Yang term already recorded above — the LHY correction *is* the
regularized zero-point mode sum ½Σ(E_k − …), not a different calculation that happens to agree.
So the mode sum inherits the control failure rather than escaping it: at the derived λ = 26–46 the
next-order (Wu) term is **1.1× to 2.1×** the LHY term it corrects, so the series is inverted, and a
mode-sum build at this order would return a number its own next order overturns. Nothing is bought
by assembling the sum by hand.

*(ii) Even at controlled λ, the object has the wrong equation of state.* A genuine ½Σℏω_k over the
Goldstone branch (ω = c_s k) under the medium's **preferred-frame** cutoff has the pressure of a
linear massless dispersion: **w = +⅓, not −1.** Only a Lorentz-invariant regulator returns
p = −ρ — and a Lorentz-invariant regulator is exactly what a condensate with a rest frame does not
have. Taken seriously, the mode-sum framing therefore argues *against* a clean w = −1 residual.
This blocker is structural and survives any improvement in λ.

**What this leaves standing.** The flagship does not run through this object: it reads the
condensation energy (Door A, ½α_c²M₂), which is frame-safe and needs no mode sum. #123 should be
read as *closed to investment at this order* — it reopens only if the SU(2) N_f = 3 lattice returns
λ below the control edge λ\* = 22.41 **and** a frame-compatible regulator is exhibited. *(An
equipartition reading — f = ½
from a zero-point K = V split, giving 2.27 meV — was tried and
**failed** on two independent grounds. (i) The number is not independent: 16π²α_c^{3/2} = 0.5115 ≈ ½,
so ½-of-door-B = 0.994 × E_b — the flagship binding energy re-packaged, so the "+0.9%" restates
E_b rather than testing it. (ii) The mechanism is invalid: a
harmonic condensate mode is honestly **w = 0** (⟨w⟩ = (n−2)/(n+2) = 0 at n = 2 — the textbook reason
an oscillating scalar is cold dark matter), not w = −1; the (+1, −1) split reads classical pure-state
extremes off a stationary quantum ground state, and the "redshift only the kinetic half" rescue
violates the uncertainty principle. The only honestly w = −1 object is the static potential floor V₀
at coefficient **1** → 2.67 meV (+19%), value un-sourced — no home for a ½. **What DOES survive
(the other half):** the ¼ + ¼ split is exact, and both halves together give w = 0 = **cold dark
matter** — which is just the dCDF's own excitation sector (dust-like below z_on) re-confirmed by the
virial theorem. So the analysis correctly identifies the condensate mode as *dark matter*; it only
fails to give the *dark-energy* value. A consistency check with the two-era dCDF, not a new result —
and a reminder that in a unified DM+DE fluid the "residual" and the "excitation" are the same
object's two faces. Autopsy in [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md); full debate in
[Thermal_Half_Discussions.md](working_logs/Thermal_Half_Discussions.md).)*

**What the door's cap actually is, and what therefore cannot fix it.** The cap is **E_b itself**,
and §2(a) derives E_b as the *universal two-body form* ½α²M — the **ℓ = 0 Coulomb ground state**,
the dark Rydberg, spherically symmetric by construction. It is **not a BCS pairing gap**. So no
gap-anisotropy weighting and no pair-counting of collective modes bears on it: those act on a
many-body gap, and this is a two-body bound state. **The perturbations door sits at +18.2%
(ρ¼ = 2.672 meV), and the factor between the doors is the derived phase-space measure by
construction** — door B is defined as E_b/Φ¼ — so no separate cancellation coefficient is owed
(above).

**A physical reading of the cancellation f (argument-grade).** The "partial cancellation" that
takes the un-cancelled sum (2.67) down to the observed residual (2.25) has a standard superfluid
identity: it is the **renormalization of the reference zero-point.** The two doors are two
*different* objects. **Door B (2.672) = the raw phonon zero-point sum** ½Σℏω_k over the Goldstone
modes (ω = c_s k up to the E_b cutoff, c_s = √α_c) — a UV-divergent *reference vacuum*, present with
or without the condensate and absorbed into the bare Λ. **Door A (2.2599) = the condensation energy**
½α_c²M₂ — the order-parameter-dependent depth of the Mexican hat, the physical energy difference
between the condensed and un-condensed vacuum (the superfluid analogue of the BCS condensation
energy ½N(0)Δ²). The physical dark energy is the **condensation energy** — the vacuum shift the
condensate actually causes — so the flagship correctly reads Door A (2.2599, +0.44%), and 2.672 is
the reference it sits on, not a competing prediction. **This reading does not lean on
16π²α_c^{3/2} ≈ ½** — the coincidence that sank the equipartition reading — it is
condensation-vs-reference, pure superfluid logic. *(One caveat stays live: it fixes **which
door**, not the **value**; and the quantum correction is **O(1), not small** — the
zero-point/mean-field ratio 1/(16π²c_s³) = 1.955 because c_s = √α_c = 0.148 is small — so an
irreducible ~O(1) strong-coupling piece remains, the same un-built number, pinned only
non-perturbatively by the SU(2) lattice. A first route that tried to make the Goldstone shift
symmetry zero the zero-point outright **fails** — shift symmetry makes the vacuum energy
θ-independent, i.e. constant, not zero; see
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md).)*

**What the O(1) actually is — computed, tribunal-adjudicated (2026-07-17).** The residual is the
**soft-phonon quantum correction to the condensation energy**, and the relativistic Bogoliubov
calculation (built, then adversarially adjudicated — full record in
[Thermal_O1_Discussions.md](working_logs/Thermal_O1_Discussions.md)) settles its size
class. **The feared O(1) was an artifact:** the 1.955 (= 1/(16π²c_s³), the door-gap number) is the
**UV-divergent, un-renormalized reference** — verified divergent ∝ k_max² — not a physical
correction; renormalization (counterterm = the physical mass renormalization, derived not fitted)
flips the coupling power from α_c^{−3/2} to α_c^{+1/2}. The physical, scheme-independent remainder
is the non-analytic Lee–Huang–Yang term:

> **ΔE/E_MF = (8/15π²)·√α_c·λ·[1 + O(α_c)] = 0.0080·λ ⟹ Δρ_Λ¼/ρ_Λ¼ ≈ 0.0021·λ, w = −1**

(derived within the stated relativistic |φ|⁴ completion; the coefficient carries no α_c and no
16π²α_c^{3/2} structure — the circularity test passes). **What this buys and what it costs, both
honest.** It buys: the correction is **percent-class, not O(1), for any controlled coupling** —
SAFE for λ ≲ 10; the series loses control above λ* ≈ 22 (the next-order term overtakes), where
neither safe nor exposed is certifiable. It costs: **the +0.44% regrades to mean-field-level
consistency** — E_b is the *prediction*, not an absorber of radiative pieces, so the flagship
carries an un-pinned O(λ · few %) radiative band for any λ ≳ 0.2–0.5; the *precision* of the
+0.44% is exposed even though its *existence* is not, and a percent-class radiative band is wider
than the gap itself. **The coupling λ is mapped from the sector's own NJL coupling** (equivalently
the gas parameter √(na³), the position on the BEC side), and the map puts it past the control edge —
so the size stays ESTIMATE, now for a stated reason rather than for a missing object.

**The two frames.** **Frame 1 (naive uniform dilute-gas map, c_s² = gn/m): self-inconsistent,
rejected.** Holding c_s² = α_c with any cosmological density gives E_MF = ½α_c·ρ_mass, which misses
E_MF = ρ_Λ by ~100–250×; making them meet needs ρ_mass ≈ 64× today's critical density. The
uniform-gas frame cannot carry the flagship's own identities — confirming the operative frame is the
composite/P(X) one. **Frame 2 (composite NJL/linear-sigma map — the strong sector's own quartic):
λ = m_σ²/2f² = 2(M/f)².** In the tribunal's normalisation (V = λ|φ|⁴ for complex φ, so φ = (σ+iπ)/√2
gives V = ¼λ(σ²+π²)²) this is *the same* λ the LHY coefficient multiplies — the two conventions
coincide, which is what lets the map be cashed rather than merely written.

**The g → λ map, forward.** Two standard NJL results close it with no new input: m_σ = 2M in the
chiral limit, and the one-loop decay constant at the same 3-momentum cutoff the sector's own gap
equation already uses, f² = N_c M²·F(y)/2π² with y = M/Λ and F(y) = ln((1+√(1+y²))/y) − 1/√(1+y²).
**M² cancels:**

$$\lambda \;=\; \frac{4\pi^2}{N_c\,F(M/\Lambda)}$$

so the quartic depends on nothing but the colour count and the cutoff-to-constituent-mass ratio —
and that ratio is fixed by the four-fermion coupling through the gap equation. The chain runs on
booked inputs alone: τ = ½ln2 ⟹ g = 1/I(τ) = 2.830 (critical value 2) ⟹ M/Λ = 0.595, M = 304 keV
(against the BCS consistency check's 312 keV) ⟹ F = 0.4317 ⟹ **λ = 45.7** at N_c = 2. The identical
formula run on QCD returns f_π = 93.1 MeV against the measured 92.4 — 0.7% — so the machinery is
calibrated rather than assumed. *(The four-fermion g is not itself the quartic: reading λ ← g ≈ 2.8
understates it ~16-fold, equating a fermionic contact coupling with a bosonic self-coupling.)*

**The number, with its band.** The regularisation cancels in the ratio
λ_dark/λ_QCD = (3/N_c)(F_QCD/F_dark) = 1.755, so the band comes from anchoring on QCD, where the
dominant systematic — the NJL σ mass, put at 2M by leading order and well below that by the physical
f₀(500) — is measured: **λ = 26–46, centre ≈ 36.** The colour count is what carries it off the QCD
value: at N_c = 2 the dark quartic is 3/2 of the three-colour one at the same M/Λ.

**Where that lands.** Every reading in the band sits **above** the control edge λ\* = 22.4 (1.1× to
2.1×; √(na³) = 0.043–0.077, so it is series *control* that fails, not diluteness). The LHY term is
therefore the wrong order to quote — its formal value would be ΔE/E_MF = 22–39%, hence
Δρ_Λ¼/ρ_Λ¼ = 5.4–9.8%, while the next term of the same series is already larger. **So the λ gate and
the τ gate MERGE, and the merge is forced rather than marginal** — the composite quartic sits past
where perturbative control ends, so the flagship's radiative band needs the same non-perturbative
SU(2) N_f = 3 treatment that owes τ. One lattice job gates both open numbers. *(Grade: the map is
**derived** — closed form, no new input, QCD-validated to 0.7%; the **size stays ESTIMATE**, now
because the series is past control at the model's own λ rather than because λ was missing. The
+0.44% keeps its existence claim and loses its precision claim.)*

**The partial wave is data-selected, and it is s-wave.** A Coulombic two-body spectrum is
E_n = ½α_c²M₂/n², and partial wave ℓ requires n ≥ ℓ+1 — so the channel picks the level:

| channel | lowest allowed level | E_b | vs observed 2.25 |
|---|---|---|---|
| **s-wave (ℓ = 0)** | 1s | **2.2599 meV** | **+0.44%** |
| p-wave (ℓ = 1) | 2p | 0.565 meV | −74.9% |
| f-wave (ℓ = 3) | 4f | 0.141 meV | −93.7% |

**The flagship's agreement requires ℓ = 0**, so the hydrogenic form is not a choice but a
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

**Grade: the DE value's structure stands (ρ_Λ¼ = (9/2)α⁴τ·m_e) with τ sourced by the Koide
kernel, landing +0.44% above the observation; the lattice T_c/√σ for SU(2) is what confirms or
kills it, and the perturbations door's O(1) is un-built with its owed object named.** Menu-watched, not read:
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
