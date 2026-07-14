# The Cosmological Constant from Vacuum Occupancy

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*Status:* ***exploratory / under internal review*** *— conditional on: the occupancy
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

$$E_b = \tfrac{1}{2}\,\alpha_c^2\,M_2, \qquad \alpha_c = 3\alpha = 0.021892,\quad M_2 = 9.39\ \text{eV}$$

$$E_b = 2.251\ \text{meV}$$

**(b) The occupancy statement.** The vacuum's gravitating density is one binding
quantum per coherence cell of volume 1/E_b³:

$$\rho_\Lambda = E_b^4 \quad\Longrightarrow\quad \rho_\Lambda^{1/4} = 2.251\ \text{meV}$$

**Measured: ρ_Λ^{1/4} = 2.25 meV. Agreement: 4 parts in 10⁴, zero adjustable
parameters in the final step.**

**(c) The provenance of M₂, stated honestly.** M₂ derives from the condensate's
effective-theory dictionary (a ghost-condensate-class EFT whose coefficients were fixed
early in the program): M₂⁴ = X₀²P₂. One dictionary parameter (a hierarchy exponent with
a natural band e⁻³⁰–e⁻³⁵, i.e. M₂ between 2.7 and 9.7 eV) is *selected* by this
closure rather than independently fixed — so the triangle {ρ_Λ, M₂, α_c = 3α} is one
constraint wearing three names, not three independent confirmations. The running MCMC
that measures α_c grades the triangle. (An earlier draft claimed an additional
loop-dressing factor matched the residual; that claim was input-inconsistent and is
retired in the public failures ledger.)

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

## 4b. The three doors to Λ (2026-07-14 — the thermal-door arc; hunt entries 140/165)

One quantity, three independent readings, one demanded number — the medium's own
consistency structure applied to its most famous problem:

- **The thermodynamic door — the cancellation** (hunt entry 140): a self-sustained
  condensate's equilibrium vacuum has **identically zero pressure by the Gibbs–Duhem
  relation** — the enormous vacuum energies do not gravitate at equilibrium (and the
  roster demonstrably cannot pay this bill species-by-species: str[1] = −68 and the
  Veltman-class sum both FAIL — the whole medium pays what the parts cannot). The
  observed Λ = the deviation from equilibrium, whose dynamic face is the still-settling
  fountain (below). *Both cancellation-and-residual statements are THERMAL readings —
  the door correction of hunt entry 170.*
- **The background door — THE VALUE** (the corpus's own §7a, finally seated at its door):
  on the model's finite 4-volume, **Λ_eff ≈ ¼⟨T^µ_µ⟩ ≈ (3/4)·ρ_m(turnaround)** — a pure
  expansion-history quantity — computes **Λ^{1/4} = 1.71 meV against the observed 2.25
  (0.76×, the right decade FROM A MECHANISM)**, with its owned caveats (the KP
  self-consistency O(1)s; the turnaround-timing corner). **This is the only door with a
  NUMBER on the table — and it was sitting in the background sector unconnected to this
  frame until the operator asked which door the VALUE question was missing.**
- **The thermal door — the residual's dynamics** (hunt entry 165): the condensate is **still settling from the one
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

## References

[Planck 2018] (the measured ρ_Λ); Volovik, *The Universe in a Helium Droplet*
(vacuum-as-condensate precedent); [Sakharov 1967] (the induced-action ancestry).
Full entries: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md); derivation chain: the internal hunt
log, entries 6–7, 38, and the thermal-door arc (140, 165 + addendum).
