"""area_law_roster_extension — task #30: does the quarter survive the full roster? (2026-07-28)

THE QUESTION (entropy file §3's named residual)
  S/(A/4G_induced) = 1 is derived for minimally coupled scalar content,
  where the horizon-area divergence and the induced-1/G divergence are one
  heat-kernel coefficient and every regulator cancels in the ratio.  For
  the model's full roster the two divergences split per class, and the
  literature has adjudicated each split.  This script assembles the
  per-class status — standard results adopted with their sources, nothing
  invented — and does the roster bookkeeping that says how much of the
  quarter rides on which commitment.

THE PER-CLASS LEDGER (literature-standard)
  * MINIMAL SCALARS — ratio 1, unconditional (the corpus's own §3 result;
    conical-deficit argument, regulator-independent).
  * SPIN-½ — ratio 1, unconditional: fermions produce NO contact term
    (Kabat 1995), and their area and 1/G divergences share one coefficient
    (the Frolov–Fursaev induced-gravity program's standard statement).
  * GAUGE FIELDS — the naive ratio is broken by the Kabat contact term (a
    negative horizon divergence); Donnelly & Wall (PRL 114, 111603; PRD 94,
    104053) identify that term as the EDGE MODES' entanglement entropy —
    with edge modes counted as horizon entropy, the ratio is restored.
    CONDITION E: edge modes are physical horizon entropy (the modern
    standard reading).
  * NON-MINIMAL SCALARS — the ξRφ² term feeds 1/G with weight (1−6ξ) while
    naive entanglement is ξ-blind; the Wald/generalized-entropy ⟨φ²⟩
    horizon term carries the same (1−6ξ) and restores the ratio
    (Solodukhin).  CONDITION W: generalized (Wald-inclusive) entropy.
    For the corpus's own conformal-Higgs condition (ξ = 1/6 — already
    required for induced-G finiteness, hunt §5) the class contributes ZERO
    to both sides and drops out identically.

ROSTER BOOKKEEPING (unit convention: one real minimal scalar = 1 unit;
  one 4D Dirac fermion = 2 units on both sides — Kabat's standard; one
  gauge boson = 2 physical polarizations = 2 naive units, made whole by
  condition E)
  fermions: 48 Weyl = 24 Dirac → 48 units, UNCONDITIONAL
  gauge:    SM 12 + dark SU(2) 3 = 15 bosons → 30 units under CONDITION E
  scalars (minimal): the medium's fields (superfluid complex 2, the
    electron-coupled scalar 1, Majoron 1) → 4 units, UNCONDITIONAL
  Higgs (conformal): 4 real dof → 0 units both sides (drops out)

GRADE RULE
  The per-class ratio-1 statements are adopted literature results, cited;
  the bookkeeping is arithmetic.  VERDICT: candidate grade, conditional on
  E (and W where non-conformal non-minimal content ever enters).  KILL:
  the model rejecting edge-mode entropy — the gauge sector's ~37% of the
  quarter breaks with it.
"""
from __future__ import annotations

N_WEYL = 48
N_GAUGE = 12 + 3
SCALAR_UNITS_MINIMAL = 4.0
HIGGS_REAL_DOF = 4


def main() -> None:
    ferm_units = (N_WEYL / 2) * 2.0
    gauge_units = N_GAUGE * 2.0
    total = ferm_units + gauge_units + SCALAR_UNITS_MINIMAL
    print("=" * 78)
    print("The quarter against the full roster — per-class ledger and bookkeeping")
    print("=" * 78)
    print("\n   class              units   ratio S/(A/4G)   condition")
    print(f"   48 Weyl fermions    {ferm_units:4.0f}    1, exact         none (no contact term)")
    print(f"   {N_GAUGE} gauge bosons     {gauge_units:4.0f}    1 with edge modes E: edge modes = horizon")
    print("                                               entropy (Donnelly–Wall)")
    print(f"   minimal scalars     {SCALAR_UNITS_MINIMAL:4.0f}    1, exact         none (the §3 result)")
    print(f"   conformal Higgs      0      drops out       ξ = 1/6 is the corpus's own")
    print("                                               induced-G finiteness condition")
    print(f"\n   roster total: {total:.0f} units — of which UNCONDITIONAL "
          f"{ferm_units + SCALAR_UNITS_MINIMAL:.0f} ({100*(ferm_units+SCALAR_UNITS_MINIMAL)/total:.0f}%),")
    print(f"   riding on condition E: {gauge_units:.0f} ({100*gauge_units/total:.0f}%).")

    print("\nVERDICT: the quarter SURVIVES the full roster at candidate grade,")
    print("   conditional on ONE modern-standard commitment — edge modes count")
    print("   as horizon entropy (the Donnelly–Wall identification of Kabat's")
    print("   contact term). Fermions and minimal scalars (63% of the roster's")
    print("   units) satisfy it unconditionally; the conformal Higgs drops out")
    print("   of both sides by the corpus's own finiteness condition; condition")
    print("   W (Wald-inclusive entropy for non-minimal content) is held in")
    print("   reserve for any future non-conformal scalar. KILL: rejecting")
    print("   edge-mode entropy — the gauge sector's 37% breaks the quarter.")
    print("=" * 78)

    assert abs(total - 82.0) < 0.5
    assert gauge_units / total < 0.5


if __name__ == "__main__":
    main()
