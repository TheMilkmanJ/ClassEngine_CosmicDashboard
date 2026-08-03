# The dCDF — the Superfluid Piece (identity file)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim
> conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*Identity file for the dCDF. Quantitative derivations live in
[PRTOE_v4_dCDF_derivation.md](exploratory/PRTOE_v4_dCDF_derivation.md) /
[PRTOE_v5_dCDF_complete.md](archive/PRTOE_v5_dCDF_complete.md); this file is what it is, not the
derivation. It is one of three dark fields — the others are the electron-coupled scalar
([PRTOE_dyad_gas.md](PRTOE_dyad_gas.md)) and the Majoron, which the one-scale corner's tie-death
keeps distinct from it.*

## 0. Derived core, open residue

What is already derived in this branch:

- the field is a two-era dark superfluid with an exact `w = −1` floor;
- the onset clock `H = m` and the radiation-like to dust-like crossover are derived;
- the s-wave channel is selected by the binding data;
- the quartic floor is finite and sets the no-singularity support scale;
- the topological / winding side is what carries the chirality and axis-family information.

What is still open:

- the residual magnitude **from this sector's own dynamics** (it is supplied by the Koide-kernel
  route — see §5 and the note there; what fails here is the fluctuation–dissipation closure);
- the exact link between the condensate floor and the bounce dynamics.

*(The matter-asymmetry sign correlation from the genesis draw is **not** still open: the joint
draw was run 2026-07-20 and finds θ̇ and n independent — the cross-messenger lock is void, not
pending; see [PRTOE_igmf_helicity.md](PRTOE_igmf_helicity.md) and §3 below.)*

So the dCDF is already mostly derived structurally. The open residue is the residual magnitude
and the sign/correlation junctions, not the existence of the component itself.

---

## 1. What it is

Field 1 of the two-field dark sector: a cosmological **superfluid** that unifies dark matter and
dark energy. Ultralight quantum **m ≈ 2.24×10⁻²⁰ eV** (the onset clock — effectively massless on
any laboratory scale). Ground state **w = −1 exactly** (the de Sitter floor, P = −ρ_inf);
excitations are radiation-like above the H = m onset (z ≈ 4×10⁷) and dust-like below — **one
fluid, two eras**.

## 2. Its structure: an s-wave-binding, baryon-free condensate

**The binding channel is s-wave, and the data selects it.** E_b is a Coulombic two-body level
(E_n = ½α_c²M₂/n², partial wave ℓ requiring n ≥ ℓ+1), so the channel picks the level: the s-wave
ground state gives **2.2599 meV** vs the observed 2.25, against **−74.9%** for p-wave and
**−93.7%** for f-wave ([PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md) §4c). The
flagship's agreement *requires* ℓ = 0.

**The mechanism: the medium is He-3-A missing its baryonic matter.** He-3 pairs p-wave *because*
its baryonic hard core suppresses ℓ = 0 — chiral superfluidity is not intrinsically p-wave; helium
is made of baryons. A medium with no baryonic core leaves the s-wave channel unsuppressed, which is
the channel the data selects. The finiteness balance independently selects a dark **SU(2)** sector,
whose pseudo-real fundamental makes its baryons **bosonic diquarks** — no fermionic hard core
exists, the lightest baryon is the **scalar** diquark, and two-color QCD is the canonical
diquark-BEC realization of the BCS–BEC crossover the occupancy argument requires
([PRTOE_PREREGISTERED_PREDICTIONS.md](PRTOE_PREREGISTERED_PREDICTIONS.md), P-2026-048; one
uncomputed lattice number decides it).

**What this identity does NOT source.** Two claims once rested here and rest elsewhere:
- **The chirality** — parity-odd signatures (GW handedness, IGMF helicity, LSS parity, the AD
  matter bias) are signed by the **genesis winding integer n**, not by a pairing channel. The
  three-membered family (matter / magnetism / metric) is one integer:
  [PRTOE_igmf_helicity.md](PRTOE_igmf_helicity.md) (P-2026-028, sign(helicity_B) = sign(n)),
  [PRTOE_lss_parity.md](PRTOE_lss_parity.md), [PRTOE_baryogenesis.md](PRTOE_baryogenesis.md),
  [PRTOE_gravitational_waves.md](PRTOE_gravitational_waves.md).
- **The generation count** — forced by **Pauli finiteness**: str[k₁] = 16·N_gen − 48 = 0 ⟹
  **N_gen = 3** uniquely, pure heat-kernel species counting with no nodes and no angular momentum
  ([PRTOE_quantum_gravity.md](PRTOE_quantum_gravity.md) §5.2–5.3; P-2026-045, conditional on
  ξ_H = 1/6).

*(The retired "He-3-A class / p-wave L" reading of this section — which sourced both of the above
from node topology — is in [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md). Literal
He-3-as-medium is retired there on four independent shots.)*

## 3. Its charge: abundance + asymmetry

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

## 4. Its light

Light is the dCDF's **massless Goldstone mode** (the transverse collective mode of the
condensate). *This identification carries a second load as of 2026-07-19: it is what makes α the
medium's own coupling rather than an external one, and so what lets the hierarchy's pairing kernel
be electromagnetic without α being obliged to run to the pairing scale
([PRTOE_hierarchy_problem.md](PRTOE_hierarchy_problem.md) §6g).* The medium is EM-neutral → transparent → zero optical birefringence; the parity is
forced into the metric instead. Full account: [PRTOE_light.md](exploratory/PRTOE_light.md).

## 5. What it does NOT close

- The dark-energy **value** does **not** forward-close from the neutrino microphysics: the
 fluctuation-dissipation response is **ohmic (s = 1)**, a **21-dex miss**. The boiling-free
 superfluid-λ reading gives s ≈ 0.69 and also misses. **The sub-ohmic/critical closure
 (s ≈ 0.26) is not an escape hatch and was wrongly carried here as one until 2026-07-28**: this
 file presented it as merely *conditional* on the settling attractor being self-organized-critical
 (*otherwise the transition boils, first-order* — that clause remains true and is cited elsewhere
 for its grammar, since first-order is how this sector goes wrong),
 but the standing ruling is stronger and structural — **the sub-ohmic self-tuning belongs to the
 dark-matter channel, not the dark-energy one**, so it is not a route to this value at any
 confidence in the SOC premise ([PRTOE_honest_status.md](PRTOE_honest_status.md), which states it
 flatly: the settling response is ohmic in the dark-energy channel, the floor's value is not fixed
 by the settling, the coincidence problem stands, and there is *"still no working self-tuning
 mechanism for the value"*). Read the two together and the conditional disappears: the honest
 status is **no mechanism**, not **a mechanism awaiting a premise**.
- **w = −1 is exact and derived**; the residual's *magnitude* is the owed piece **from this
  sector's own dynamics** — the qualifier matters and was missing until 2026-07-28. The magnitude
  **is** supplied elsewhere, by a route this file never mentioned: the Koide-kernel chain gives
  ρ_Λ¼ = (d²/2)·α⁴·T_c = 2.2599 meV ([PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md)),
  with α, m_e and d = 3 as inputs and nothing cosmological in it. Read together, the two files say:
  the number exists, and **the dCDF cannot yet produce it from its own fluctuation–dissipation
  response**, which is ohmic (s = 1) and misses by 21 decades.

  That is a genuine open item and it should not be softened — but neither should it be stated in a
  way that implies the dark-energy scale is underived corpus-wide, which is how this bullet read on
  its own. The honest form: **one route supplies it at existence grade, this sector's own route
  fails by 21 dex, and the two facts belong in the same sentence.** (The supplying route carries its
  own caveats: a +0.44% offset that is ~1.8σ on the observational error, and the corpus's own
  dof-family estimate of τ pointing to ~+4% — both recorded in
  [PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md) §3.)

## Where the dead ends live

Literal He-3-as-medium (four shots) and the DE-amplitude inversion are in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md). The chirality/GW-parity dead ends are under
**"Birefringence."**

## Sources / see also

Derivations: [PRTOE_v4_dCDF_derivation.md](exploratory/PRTOE_v4_dCDF_derivation.md),
[PRTOE_v5_dCDF_complete.md](archive/PRTOE_v5_dCDF_complete.md). The Goldstone: [PRTOE_light.md](exploratory/PRTOE_light.md).
Genesis: [PRTOE_white_holes.md](PRTOE_white_holes.md). The three-door map:
[PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md) §4b, read through
[PRTOE_quantum_trio.md](exploratory/PRTOE_quantum_trio.md). The open derivations:
[PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md).
