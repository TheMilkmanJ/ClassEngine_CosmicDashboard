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
required, are in hunt entries 228–229.) What the model does **not** derive is the pinning — *why* the
dark scale equals the electron mass. That one input is irreducible: it is the meV coincidence
ρ_Λ ~ α⁴m_e, and it cannot be derived without spoiling the value of τ. So the honest reading: the
dark-energy *scale* follows a derived closed form in α with a single dimensionful input, the electron
mass; the value lands within a few percent; and the one un-derived step is stated plainly, not hidden.

**(d) Why the 10¹²⁰ never appears.** The Λ⁴ catastrophe is the *loop-pricing* of the
vacuum — a mode sum. In this framework the condensate's ground state *is* the vacuum,
and its gravitating energy is its *binding* energy — an occupancy count. The mode sum
is the wrong ledger: it double-counts fluctuations that the no-bare-terms principle
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
 Veltman-class sum both FAIL — the whole medium pays what the parts cannot). The
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
- **The thermal door — the residual's dynamics** (hunt entries 165/175–183): the candidate
 chain is now end-to-end mechanism-shaped — the deviation is EXPANSION-SOURCED (free decay
 would die by e^{−10⁵}; the settling law is an attractor), the friction partner is the
 neutrino bath (the medium's only tree-level coupling; the friction turns on where
 free-streaming turns off), and the freeze — Γ = H at T_f — lands at z ≈ 12 with a
 decade-wide fade (z ≈ 32 → 4): **w = −1 exact through the observable range, untuned; the
 settling's ash banks as dark matter (the drain, the fluid's own dust face); the frozen
 residual is Λ.** Candidate grade throughout: the attractor/√N session is the doubly
 load-bearing promotion computation (the coupling exponent AND the drain magnitude from one
 calculation). The original statement stands beneath it: the condensate is **still settling from the one
 genesis injection** — thermal counterflow (the fountain effect, the corpus's own
 genesis name) persists while any deviation from the T = 0 ground state remains, dying
 only asymptotically (the third law's ramp). The residual excitation of a nearly-settled
 medium is small — today's gradients are CMB-uniform at the 10⁻⁵ class — giving Λ's
 smallness qualitatively for free.
- **The perturbations door** (entry 165 addendum): the textbook zero-point mode sum —
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
dig (the three-door guideline; a diagnostic, not an executioner). Menu-watched, not read:
Λ^{1/4} ≈ 2.25 meV sits ~10× today's photon temperature — the known cosmic
near-coincidence, unclaimed.

## 5. Falsification conditions

(i) the running α_c measurement lands > 2σ from 3α (the triangle loses a leg);
(ii) DESI DR3 establishes w ≠ −1; (iii) the thaw chain's posterior excludes zero;
(iv) Σm_ν measured robustly above ~70 meV, or inverted ordering; (v) the pairing-gap
computation failing to sustain k ≈ 1.36 unravels the hierarchy leg.

## Where the dead ends live

Two dead ends set this file's honest grade. The "residual IS the dressing" identity (entry 6)
downgraded to *suggestive* once run at 3α (0.846 vs 0.835), and the triangle's "0.1% match"
(entry 7) turned out to *select* the free dial x₀ rather than pin it. Both are logged in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) (the mathematical self-audit and the
superseded-claims index) — which is why §2 states the closure as occupancy *without* leaning
on the identity.


## References

[Planck 2018] (the measured ρ_Λ); Volovik, *The Universe in a Helium Droplet*
(vacuum-as-condensate precedent); [Sakharov 1967] (the induced-action ancestry).
Full entries: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md); derivation chain: the internal hunt
log, entries 6–7, 38, and the thermal-door arc (140, 165 + addendum).
