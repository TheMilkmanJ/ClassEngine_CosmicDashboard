# A well-posed gap in the two-color lattice literature: T_c/√σ for SU(2) with N_f = 3 light fundamental flavours

*Approved for circulation (owner, 2026-07-18).*

## The computation

Finite-temperature lattice determination of the transition temperature in units of the string
tension, **T_c/√σ, for SU(2) gauge theory with N_f = 3 degenerate light Dirac fermions in the
fundamental representation**, with:

1. **both transitions separately** — the chiral crossover (chiral-susceptibility peak) and the
   deconfinement crossover (Polyakov-loop susceptibility peak). In two-colour QCD the Polyakov peak
   *weakens* as the quarks lighten, opposite to the three-colour behaviour (Kaczmarek, Karsch &
   Laermann, hep-lat/9809059, at N_f = 4 staggered on N_τ = 4 — a short proceedings contribution,
   and to our knowledge the only statement of this kind), so the splitting is itself a result;
2. **a chiral extrapolation**: ensembles at m_PS/√σ ≲ 1 with the quark-mass slope measured (the
   SU(3) benchmark is T_c/√σ = 0.40(1) + 0.039(4)·(m_PS/√σ), Karsch–Laermann–Peikert,
   hep-lat/0012023 — untested in a pseudo-real theory);
3. the scale set by the string tension directly, or by r₀/t₀/w₀ with the conversion stated on the
   same ensembles;
4. at least two temporal extents (N_τ = 6, 8; 10–12 if affordable) for a continuum-limit
   statement — coarse-lattice SU(3) values drifted downward ~10% in the continuum, and whether
   SU(2) does the same is unknown.

## Why it is interesting independent of any particular model

- **The gap is real.** Two-color QCD has a substantial finite-temperature and finite-density
  literature at N_f = 2. On the staggered side, Astrakhantsev et al. (arXiv:1808.06466) measure
  √σ₀ = 476(5) MeV on-ensemble at a = 0.044 fm and m_π = 740(40) MeV, and Kudrov, Bornyakov & Goy
  (arXiv:2511.19789) place the deconfinement crossover at T_d(0) = 230(10) MeV, equivalently
  r₀T_d(0) = 0.55(4), on the same improved-staggered action. Taken together these give
  **T_d/√σ ≈ 0.48** — 0.483 read directly, or 0.487 through r₀ = 0.468(4) fm, which is the one
  internal cross-check available. On the Wilson side, Iida–Itou–Lee (arXiv:2008.06322 and
  JHEP 10 (2024) 022) give two determinations of the chiral crossover that disagree at the ~30%
  level. **No published T_c/√σ exists for N_f = 3 light fundamental flavours** (a literature
  sweep, 2026-07; N_f = 4 exists only in qualitative form from the 1980s–90s).
- **Flavour-dependence in a pseudo-real theory.** In SU(3) the flavour suppression of T_c/√σ
  *saturates* (−0.21 for the first two flavours, only −0.03 for the third). SU(2)'s fundamental
  representation is pseudo-real — the chiral symmetry is enlarged (SU(2N_f) → Sp(2N_f)), the
  Goldstone count differs (14 at N_f = 3), and whether the SU(3) saturation pattern transfers is
  an open, clean question.
- **Conformal-window safety.** N_f = 3 sits well below the SU(2) fundamental window edge
  (N_f ≈ 6: arXiv:1111.4104, 1511.01968), so the theory confines and breaks chiral symmetry —
  the computation is conventional, not frontier-exotic.
- **Cost is modest.** Two colors, three light flavours, moderate volumes; the existing N_f = 2
  ensembles and tuning are a natural starting point.

## The discretization is the hard choice, and we do not pretend otherwise

N_f = 3 is the least comfortable flavour count to discretize, and anyone costing this computation
will see that first.

**Staggered.** Three flavours require the odd root, det^(3/4) — rooted staggered where it is least
comfortable, since the rooting cannot be read as a taste-averaging over an integer number of
physical flavours. Two-colour QCD adds a second problem on top: with fundamental quarks the
staggered action does not reproduce the continuum symmetry-breaking pattern, a point made
explicitly by Astrakhantsev et al. in the very paper quoted above for √σ. Since the pseudo-real
enlargement SU(2N_f) → Sp(2N_f) is precisely what makes the N_f dependence interesting here, a
discretization that deforms it is not a neutral choice.

**Wilson.** The symmetry pattern is correct, at the cost of explicit chiral-symmetry breaking at
finite lattice spacing, which is exactly what a chiral-crossover determination is trying to
measure — and the two existing N_f = 2 Wilson determinations disagree at ~30%.

We do not claim to know which way this should be settled. **We state it because the choice is part
of the computation and not a detail beneath it**, and because a result whose discretization is not
argued for will not settle anything at the precision discussed below.

## A pre-registered stake (stated for transparency)

An independent phenomenological program carries a **publicly pre-registered bet on this number**,
placed before any dedicated computation existed: **T_c/√σ = 0.34657** for the chiral transition,
with pre-committed kill conditions.

**The precision matters more than the central value, and we would rather say so up front.** The bet
distinguishes two hypotheses that sit **0.44% apart**:

| | T_c/√σ | what a return here would mean |
|---|---|---|
| **the program's prediction** | **0.34657** (= ½ln2, from an independent lepton-sector identity) | the prediction is sourced |
| the null | 0.34506 | the program is reading a cosmological observation back, and predicts nothing |

So a determination carrying **σ > 0.44% cannot distinguish them and is registered in advance as
scoring neither way** — which, given that published T_c/√σ determinations typically carry 1–3%, is
the expected outcome of a standard-precision calculation. **Discrimination needs σ ≲ 0.22%.**

Two clauses are executable at ordinary precision and remain live: a determination outside
**[0.330, 0.370]** falsifies the program's dark-energy sector outright, and the best current
inference from measured neighbours (the N_f = 2 anchors above plus the SU(3) flavour-dependence) is
**0.39 ± 0.05**, centred *above* the bet — so the falsification clause is genuinely at risk.

Whatever one thinks of the underlying model, the epistemic situation is unusual: a falsifiable,
pre-committed number waiting on a computation the field can do with existing tools, with the
precision it would take to settle it stated in advance rather than negotiated afterwards.

## Contact / provenance

The registration and the literature sweep are timestamped in a public
repository (git history; registry entry P-2026-048):
github.com/TheMilkmanJ/ClassEngine_CosmicDashboard. Correspondence: J. Pulford,
pulfordj420@gmail.com.

## References

Kaczmarek, Karsch, Laermann, *Thermodynamics of two-colour QCD*, Nucl. Phys. B Proc. Suppl. **73**
(1999) 441 (hep-lat/9809059) · Karsch, Laermann, Peikert, *Quark mass and flavour dependence of the
QCD phase transition*, Nucl. Phys. B **605** (2001) 579 (hep-lat/0012023; Eq. 3.14 is the fit
quoted above) · Astrakhantsev, Bornyakov, Braguta, Ilgenfritz, Kotov, Nikolaev, Rothkopf,
*Lattice study of static quark-antiquark interactions in dense quark matter*, JHEP **05** (2019) 171
(arXiv:1808.06466; source of √σ₀ = 476(5) MeV) · Kudrov, Bornyakov, Goy, *Studying properties of
the SU(2) QCD by lattice field theory methods*, arXiv:2511.19789 (source of T_d(0) = 230(10) MeV
and r₀T_d(0) = 0.55(4)) · Iida, Itou, Lee, arXiv:2008.06322; JHEP **10** (2024) 022 ·
Karavirta et al., arXiv:1111.4104; arXiv:1511.01968.
