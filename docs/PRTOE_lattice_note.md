# A well-posed gap in the two-color lattice literature: T_c/√σ for SU(2) with N_f = 3 light fundamental flavours

**STATUS: APPROVED FOR CIRCULATION (owner, 2026-07-18).**

## The computation

Finite-temperature lattice determination of the transition temperature in units of the string
tension, **T_c/√σ, for SU(2) gauge theory with N_f = 3 degenerate light Dirac fermions in the
fundamental representation**, with:

1. **both transitions separately** — the chiral crossover (chiral-susceptibility peak) and the
   deconfinement crossover (Polyakov-loop susceptibility peak). In SU(2) with light quarks the two
   are known to decouple (Kaczmarek, Karsch & Laermann, hep-lat/9809059: the Polyakov peak
   *weakens* as quarks lighten — opposite to SU(3)), so the splitting is itself a result;
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
  literature at N_f = 2 (rooted-staggered: Astrakhantsev et al., arXiv:1808.06466, with
  √σ = 476(5) MeV on-ensemble and T_d(0) = 230(10) MeV; Wilson: Iida–Itou–Lee, arXiv:2008.06322
  and JHEP 10 (2024) 022, whose two determinations of the chiral crossover disagree at the ~30%
  level). **No published T_c/√σ exists for N_f = 3 light fundamental flavours** (a literature
  sweep, 2026-07; N_f = 4 exists only in qualitative form from the 1980s–90s).
- **Flavour-dependence in a pseudo-real theory.** In SU(3) the flavour suppression of T_c/√σ
  *saturates* (−0.21 for the first two flavours, only −0.03 for the third). SU(2)'s fundamental
  representation is pseudo-real — the chiral symmetry is enlarged (SU(2N_f) → Sp(2N_f)), the
  Goldstone count differs (14 at N_f = 3), and whether the SU(3) saturation pattern transfers is
  an open, clean question.
- **Conformal-window safety.** N_f = 3 sits well below the SU(2) fundamental window edge
  (N_f ≈ 6: arXiv:1111.4104, 1511.01968), so the theory confines and breaks chiral symmetry —
  the computation is conventional, not frontier-exotic.
- **Cost is modest.** Two colors, three staggered or Wilson flavours, moderate volumes; the
  Braguta-school N_f = 2 ensembles and tuning are a natural starting point.

## A pre-registered stake (stated for transparency)

An independent phenomenological program carries a **publicly pre-registered bet on this number**
(registered 2026-07-16, amended 2026-07-17, before any dedicated computation existed):
**T_c/√σ = 0.3503 ± 0.02** for the chiral transition, window [0.330, 0.370], with pre-committed
kill conditions — a lattice determination outside the window falsifies the program's dark-energy
sector; a value at 0.345 is registered as *not* confirming it. The best current inference from
measured neighbours (the N_f = 2 anchors above plus the SU(3) flavour-dependence) is
**0.39 ± 0.05** — centred *above* the bet, so the bet is live in both directions. Whatever one
thinks of the underlying model, the epistemic situation is unusual: a falsifiable, pre-committed
number waiting on a computation the field can do with existing tools.

## Contact / provenance

The registration, its amendment history, and the literature sweep are timestamped in a public
repository (git history; registry entry P-2026-048):
github.com/TheMilkmanJ/ClassEngine_CosmicDashboard. Correspondence: J. Pulford,
pulfordj420@gmail.com.

## References

Kaczmarek, Karsch, Laermann, hep-lat/9809059 · Karsch, Laermann, Peikert, hep-lat/0012023 ·
Astrakhantsev et al., arXiv:1808.06466; review arXiv:2511.19789 · Iida, Itou, Lee,
arXiv:2008.06322; JHEP 10 (2024) 022 · Karavirta et al., arXiv:1111.4104; arXiv:1511.01968.
