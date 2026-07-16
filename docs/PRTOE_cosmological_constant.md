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

**The seam identification of M₂ (hunt 210–211 — scaling derived, digit rides T_c).** The dyad–dCDF
meeting (the seam) NAMES M₂'s base scale: **M₂ = α²·T_c**, the dyad condensation temperature
(T_c ≈ 193 keV) times an α². And the **α² is DERIVED** (hunt 211): the two dark fields share exactly
one coupling channel — the electron — and both vertices are electromagnetic (dCDF↔e via its
photon-Goldstone ~α; dyad↔e via the EM self-energy m_e-shift ~α), so their handshake is α×α = α².
Ramp-confirmed: sweeping M₂ = α^n·T_c, only **n=2** lands (n=1 is 137× high, n=3 is 137× low). Then
**ρ_Λ¼ = ½α_c²M₂ = (9/2)α⁴T_c**, with **α⁴ = α_c² (dCDF binding) × α² (EM handshake)** — every power
named. M₂ = α²T_c = 10.3 eV matches the freely-selected 9.39 eV to 9%. At central T_c → 2.46 meV
(1.09×); exact 2.25 meV at T_c = 176 keV, inside the band. **Grade:** the α⁴ *scaling* is derived
(power-counting) AND ramped (only n=2); the *digit* rides **T_c**. And T_c does NOT pin at leading-log
(hunt 212): T_c = m_e0√(3(L−1)/2π²) is coupling-independent (κ cancels), but the leading-log L−1 carries
an RG-scheme spread of a **factor ~10** in the value (0.21×–2.04× across μ ∈ {T_c, πT_c, 2πT_c} × MS-bar
{0, 3/2}) — a first-pass μ=T_c/MS-bar landing of 0.96× proved a non-robust scheme artifact under the ramp.
A partial 2-loop pass (hunt 213) fixed the thermal side EXACTLY and found the model's high-T
Δm²=(κm_e²/3)T² is **out of regime** (T_c < m_e): the exact fermion loop (Boltzmann-suppressed electrons)
pushes T_c UP ×1.4, so at the natural scale μ=v the DE estimate **over-predicts ~2×** (T_c≈369 keV). The
remaining residual — the zero-T leading-log — needs the genuine 2-loop β-functions (not in the corpus).
**The T_c closer was BUILT** ([PRTOE_build_2loop_Veff_spec.md](PRTOE_build_2loop_Veff_spec.md); hunt 215) —
result a **definite negative**: the 2-loop RG-improvement does NOT pin T_c. There is no SSB at μ=m_e, and
the scale-stationary PMS sits at μ ~ e⁻¹⁰⁰ m_e (unphysical) for any 2-loop coefficient, because the O(α)
curvature is too weak. So **T_c is perturbatively ILL-DEFINED** — the electron-CW condensation is a
large-log/marginal effect, and this seam DE route has no perturbative T_c to evaluate. **The
non-perturbative gap equation was then built** (hunt 216): treating the dyad as the fermion-bilinear
composite the model says it is, the NJL/BCS gap equation is cutoff-regulated → **T_c = Λ·τ(g) is
WELL-DEFINED** (log-ambiguity resolved), and for natural inputs (compositeness Λ=m_e, coupling g~2.8,
just above the critical g_c=2) **ρ_Λ¼ = (9/2)α⁴·Λ·τ(g) lands 1.0–1.1×**. So the arc is ill-defined →
well-defined. Deriving (Λ, g) (hunt 217): **Λ = m_e** (electron-bilinear composite) and **g > g_c = 2**
(condensation ⟺ supercritical; the α_c binding is 300× too weak, so it's genuinely strong) are DERIVED —
leaving **ρ_Λ¼ = (9/2)α⁴·m_e·τ** with only the O(1) strong-coupling τ = T_c/m_e ≈ 0.34 as the residual:
the DE value = α⁴·m_e·(O(1)). The DE-value T_c and the varying-m_e VEV are cross-constrained; a ~3× mismatch appeared and was
**RESOLVED** (hunt 218): the perturbative VEV (100 keV) was internally inconsistent (T_c > v, unphysical
for a condensate — BCS wants T_c/v = 0.567 < 1), so the gap equation CORRECTS it to the consistent
v ≈ 340 keV. Since only ε = κv² is observable, re-fitting the free κ preserves ε = 1.24% exactly and the
T_c window is unchanged — **no observable breaks**. The dyad sector is now BCS-coherent (v ≈ 340 keV,
T_c ≈ 185 keV, v < m_e = Λ). So the only remaining DE-value residual is the single O(1) strong-coupling
τ = T_c/m_e ≈ 0.34. (The earlier factor-3 tension was a BCS/perturbative-inconsistency artifact, not the
structural d=3.) **Deriving τ (hunt 219):** unitarity gives τ~0.167 (2× low); the conjecture **τ = 1/d =
1/3** gives the clean **ρ_Λ¼ = (d/2)α⁴m_e = (3/2)α⁴m_e = 2.17 meV (0.966×)** — the d² of α_c=3α partially
cancels the 1/d, tying τ to the structural d=3. But τ=1/d is ~5% low and NOT gap-derived (the coupling
g*(τ=1/d)/g_c isn't fixed across d), so it is a CONJECTURE, not a derivation. **Arc landing:** the DE
value converges to the conjectured closed form **ρ_Λ¼ = (d/2)α⁴m_e** (0.966×), everything fundamental
(d=3, α, m_e), with τ=1/d the single unproven assumption. The p-wave gap was then built (hunt 220): at
T_c the chiral p-wave angular factor **factors out**, so the pairing channel (s/p/f) is irrelevant to τ —
τ is set purely by the MAGNITUDE of the microscopic pairing coupling g_p, a strong-coupling O(1) the
corpus does not specify. So the digit's last input is g_p (a model-building input), not the pairing
structure. The DE value stands at (d/2)α⁴m_e (0.966×) — the honest floor of the marathon. **Deeper (hunt 221):**
the digit's last input g_p (the strong pairing coupling → τ) is sourced by NO existing interaction — α,
α_c=3α, the Majoron (g~10⁻⁸), and the ε-fitted κ all give g ≪ g_c=2 by 2–15 orders. The model has no
strong sector. So τ is either a FREE parameter (fundamental scalar) or requires a NEW strong pairing
sector to be written down (composite) — a piece of theory to be BUILT, not a computation. The DE value's
digit rests on the one thing the model doesn't yet contain: the strong force that binds the medium.
Not the α⁴m_e coincidence — m_e misses at 2.9×; T_c is fixed by the seam physics, not the fit. Net: the
scaling is derived, the digit stays open pending the 2-loop T_c — a motivated estimate, not a derivation.

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
- **The background door — FALSIFIED as a value mechanism** (the KP self-consistency solve, done
  properly — hunt 209): on the finite 4-volume, **Λ_eff = ¼⟨T^µ_µ⟩ = ¼⟨ρ_m⟩**. The self-consistent
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
