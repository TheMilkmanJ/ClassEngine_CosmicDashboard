# The Electron-Coupled Scalar — the Thermal-Sector Field (identity file)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim
> conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*Identity file for the electron-coupled scalar. Quantitative derivation lives in
[PRTOE_me_trigger.md](PRTOE_me_trigger.md) /
[PRTOE_me_mechanism_math.md](PRTOE_me_mechanism_math.md); this file is what it is. It is one of
three dark fields — the dCDF superfluid ([PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md)),
this field, and the Majoron (§2).*

## 0. Derived core, open residue

What is already derived or forced in this branch:

- the coupling operator must be even in the dark field, so the leading invariant is |Ψ|²;
- H†H is excluded by D/H and the quark channel;
- L̄He is the standing operator choice for δm_e;
- the shift amplitude is ε = c·f̄·α_c = 27α/5π;
- the screening threshold is sharp rather than smooth, because it is set by a local
  curvature criterion rather than by a temperature;
- the high-f thermal restoration relation makes (λ, f, T_c) a two-parameter family;
- the Majoron is a separate field, so this field remains leptophilic by data rather than by
  a symmetry argument.

What is still open:

- which Standard-Model operator the singlet multiplies in the UV completion above f;
- the exact T_c pin within the remaining band;
- the crunch-sector bridge that would make the already-computed high-f portal rate law relevant
  to the bounce.

So this field is not merely a narrative in the parts the corpus already prices. The open residue
is specific and small: operator selection, exact pinning, and the portal rate.

---

## 1. What it is

Field 2 of the dark sector: a **charge-free field that couples to the electron**. It is a
high-scale pseudo-Goldstone — decay constant **f ≈ 100–500 TeV** (a named input), coupling
**κ = ε/f²**, so the delivered shift ε = κf² = 1.2543% comes from the frozen zero mode. Its
condensation is driven by its own lepton-number-breaking potential; the electron loop supplies
the ramp's timing, and the timing relation ties the decay constant, the quartic and the
transition temperature into a two-parameter family
([PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §4). The ramp is keyed at **T_c = 177.10 keV** —
the kernel-sourced value (τ = ½ln2 through Parseval),
lattice-refereed at P-2026-048; the coded pipeline still runs the earlier 179 keV, a
difference priced at 0.002σ on D/H ([PRTOE_CODE_MANIFEST.md](PRTOE_CODE_MANIFEST.md)). *(That
keying value is the confining sector's scale rather than this field's own restoration temperature,
which the exact thermal kernel puts at **307–714 keV** — a band that **excludes** the keying value
by 1.73× at its bottom, so the two are **not one object**, consistent with
[PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §6 ruling this field neither of the confining
sector's condensates. The ≤ 0.32σ whole-fence swing that made this look costless is stated on
[70, 500] keV, and **53% of this field's own band lies above that fence**, where the field reaches
n/p freeze-out. **That re-keying has since been priced and it fails** (2026-07-27): running the
production abundance pipeline with the ramp keyed on this field's own band moves helium-4 by
+0.50σ at the band's bottom to +1.37σ at its top, with deuterium adding up to +0.79σ, against a
0.32σ fence — so the abundances themselves pin the ramp's onset to the confining sector's scale,
and the two remain distinct objects by measurement rather than by assumption
([PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md)).)*

*(A note on the file's "gas" label: it is a role name, not a phase claim — this field's
**complementary role** to the dCDF superfluid, the hot/thermal/lepton-binding side against the
cold/chiral/abundance side. The field condenses; it is not a classical gas.)*

## 2. Leptophilic — and what carries the leptophilia

The field lives in the lepton sector and couples to **leptons, not hadrons**. What forces that is
**data, not the broken symmetry**: a universal quark-mass shift at ε would move the deuterium
binding by −4ε and land at +12–18σ on D/H. The symmetry argument that *does* bite is the reverse
one — dark-U(1) forbids any coupling linear in Ψ, which is why the operator is the
quadratic-canonical m_e(φ) = m_e0(1 + κφ²).

**Lepton number does not deliver it.** A phase-blind |Ψ|² operator cannot see the Majoron's
current, which couples to the phase; and the Majoron forces the *neutrino* coupling σNN, not the
charged-lepton Yukawa. So |Ψ|²·ψ̄ψ and |Ψ|²·(LH)(LH)/Λ carry independent coefficients and lepton
number screens neither ([PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §0).

**The un-derived core is which Standard-Model operator the singlet multiplies — docket #125, and
it is an assumption, not a selection.** Three couplings are open to a dimension-2 dark singlet.
**H†H** is the only renormalizable one and would shift the Higgs vev, moving every mass including
the quarks — excluded at ε by the same 12σ, and bounded to λ_p ≲ 5×10⁻¹¹…1×10⁻⁹ across the f
window. **(LH)(LH)** reaches δm_ν alone and cannot deliver δm_e at any coefficient. The standing
choice is the third, **ψ̄ψ**, and nothing forces it: a gauge singlet couples to every Yukawa
operator with its own coefficient. What is computed rather than assumed is that the choice is
stable — the standing operator's own electron loop feeds H†H at λ_p ≤ 1.1×10⁻¹³, from ~500× under
that bound at its tightest corner to ~10⁶× under at the loosest, so excluding the
renormalizable portal costs no tuning inside the
effective theory. The finer fork, and the one with a signature: writing the singlet into the
lepton doublet's normalization instead of into each mass operator ties δm_ν/m_ν = 2·δm_e/m_e.
That point is the one the pipeline runs, and no measurement can reach it — 1.5 meV on Σm_ν inside
a window whose exit restores the present-day value the sky actually measures.

**The Majoron is a separate field.** The single-scale reading that merged them (f = v_L) is
tie-dead — its condensate-friction ceiling sits at v_L ≲ 2.4 TeV against a thermalization floor of
40 TeV — so the sector carries two lepton-number-breaking scales and **three dark fields**, not two
([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §6). The Majoron keeps the neutrino tie that
was once read as this field's own: tree coupling σNN → Majorana neutrino mass → **0νββ must occur**,
with the shared-scale tie ρ_inf¼ = m_ν,lightest (**Σm_ν ≈ 61.4 meV, normal ordering**). Which v_L
corner it sits at — TeV-class or MeV — is open, and CMB-S4 is the selector. (Full:
[PRTOE_neutrino_home.md](PRTOE_neutrino_home.md),
[PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md).)

## 3. What it does to hydrogen: varying-m_e

Inside its window it shifts the electron mass by **ε = 1.2543%** (= c·f̄·α_c = 27α/5π). A heavier
electron → **deeper atomic binding** → hydrogen recombines **earlier/hotter** → smaller sound
horizon → **H₀ ≈ 69.9** instead of 68.2 (the Hubble-tension mechanism). In one line: this field
makes hydrogen more tightly bound. Evidence: ΔlnZ ≈ +2.6 (marginal, SH0ES-conditional, and a
Laplace estimate — nested sampling is deferred to cluster time, so the number has no confirmer in
prospect and rests on the MCMC chains it is computed from).
(Full: [PRTOE_hubble_tension.md](PRTOE_hubble_tension.md),
[PRTOE_THE_AMPLITUDE.md](PRTOE_THE_AMPLITUDE.md).)

## 4. Complementarity with the superfluid

Whatever role the superfluid carries, this field carries the complement:

| | dCDF (superfluid) | the electron-coupled scalar (thermal side) |
|---|---|---|
| charge | abundance / asymmetry | none — it is charge-free; its L-breaking partner is the Majoron |
| symmetry role | chiral / parity-odd | **electron-coupling** (a total singlet: Lorentz-scalar, dark-neutral, gauge-neutral, L-neutral) |
| thermal role | cold, condensed floor | **hot, thermal, binds hydrogen** |
| its excitation | light (Goldstone) | the pseudo-Goldstone of its own L-breaking potential at f |

They meet at the **critical seam** — the sub-Ohmic, smooth region recorded in
the derivation log. The complementarity is a candidate framing; the field assignments above are
established (dCDF = chiral abundance-carrier; the electron-coupled scalar = the leptophilic
electron-coupler).

## Where the dead ends live

The lepton/hadron varying-constant hierarchy (P-2026-011 — leptons shifting ~13× more than
hadrons) is retired and lives in [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) under
**"Retracted predictions"**. The scope of the surviving universality, stated precisely: the
coupling is **multiplicative-universal *within* the lepton sector** (no flavour structure — the
Koide protection) and **exactly leptophilic *across* sectors** — forced by **data**: a universal
quark-mass shift at ε would move the deuterium binding by −4ε ≈ −5%, a +12–18σ D/H
catastrophe on the recorded Dent–Stern–Wetterich elasticity. *(This was once billed as forced
twice over, the second arrow being lepton number itself. That arrow does not fire: the operator is
a total singlet and L-neutral, so lepton number screens the quark bilinear no more than the lepton
one — §2. The data arrow alone carries it, at 12σ.)* A quarks-included reading of the
P-011 retraction's wording is superseded by that adjudication; the census's "universal charged
roster" is the *counting measure* for c = 9/10, a different object from the coupling's flavour
reach.

## Sources / see also

Derivation: [PRTOE_me_trigger.md](PRTOE_me_trigger.md),
[PRTOE_me_mechanism_math.md](PRTOE_me_mechanism_math.md). The amplitude ε:
[PRTOE_THE_AMPLITUDE.md](PRTOE_THE_AMPLITUDE.md). The Majoron:
[PRTOE_neutrino_home.md](PRTOE_neutrino_home.md). H₀:
[PRTOE_hubble_tension.md](PRTOE_hubble_tension.md).
