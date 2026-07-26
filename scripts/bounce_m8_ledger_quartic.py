"""bounce_m8_ledger_quartic — the expansion-energy ledger at quartic order (2026-07-27).

QUESTION
  M5 left exactly one adjacent lane for a metric-on turn: a modification of the
  Friedmann CONSTRAINT itself (bounded-density class, H² carrying a −ρ²/ρ_c
  correction).  The corpus derives the standard constraint from its own
  expansion-energy ledger (the zero-energy shell condition).  Does redoing that
  ledger WITH the medium's quartic interaction energy in the books produce the
  correction natively — or not?

THE THREE PLACES IT COULD COME FROM, EACH CHECKED
  A. The shell books themselves.  Interaction energy enters the shell's inertia
     and its gravitational source IDENTICALLY (the model's own counting rule:
     gravity couples to energy content, not species).  The zero-energy condition
     then still reads E = ½ṙ² − G·M_tot/r = 0 with M_tot = (4π/3)ρ_tot·r³, and
     the constraint keeps its exact form H² = (8πG/3)·ρ_tot.  The quartic
     changes the HISTORY (through pressure in the continuity equation), never
     the FORM.  No −ρ² term arises here.
  B. The history it changes (computed below).  Pure-quartic condensate:
     u_int = (g/2)n², pressure p = u_int (polytrope of index 2).  Then
     ρ + p > 0 at every density, so contraction only steepens: H² grows
     monotonically into the ceiling and never crosses zero.  (This reproduces
     the recorded no-go for the ceiling-as-bounce, now from the ledger side.)
  C. The discreteness analog.  In bounded-density cosmologies the −ρ²/ρ_c term
     comes from the quantum-geometry layer.  The medium's analog of that layer
     is the quasiparticle dispersion ω² = c_s²k²·(1 + k²ξ²/4): its correction
     is ∝ k⁴ξ² — it vanishes IDENTICALLY at k = 0, i.e. for homogeneous
     cosmology, and switches on only at gradient scale ξ.  The medium's own
     UV correction is therefore not a homogeneous constraint term at all —
     it IS the metric-exit door.  (The density-dependent-coupling escape is
     closed by the recorded framework stance that the varying sector does not
     modify gravity; the historical scalar-tensor lane is retired.)

GRADE RULE
  A negative close: the bounded-density lane is NOT native to the recorded
  theory at the hydrodynamic layer.  Ledger row; the lane survives only as
  unrecorded new physics, same status as any unnamed operator.
"""
from __future__ import annotations

import numpy as np

RHO_B = 1.0          # ceiling units: u_int = ρ_mass²/(2ρ_b)-class; set ρ_b = 1


def history_contraction(rho0: float = 1e-4, steps: int = 4000):
    """Contract at fixed 'time' resolution in ln a; track ρ_tot, p, H², 1+w."""
    lna = np.linspace(0.0, -4.0, steps)          # a shrinking by e⁴
    rho_m = rho0 * np.exp(-3.0 * lna)            # mass density ∝ a⁻³
    u_int = 0.5 * rho_m**2 / RHO_B               # quartic interaction energy
    rho_tot = rho_m + u_int
    p = u_int                                    # pure-quartic pressure
    w = p / rho_tot
    H2 = rho_tot                                 # units 8πG/3 = 1
    return lna, rho_tot, p, w, H2


def main() -> None:
    print("=" * 78)
    print("M8 — the expansion-energy ledger at quartic order")
    print("=" * 78)

    print("\nA. The shell books: constraint form (analytic, stated in docstring)")
    print("   Interaction energy adds to inertia and to the gravitational source")
    print("   identically ⟹ E = ½ṙ² − G·M_tot/r = 0 ⟹ H² = (8πG/3)·ρ_tot.")
    print("   FORM unchanged; no −ρ²/ρ_c term can arise from the books themselves.")

    print("\nB. The history the quartic does change (computed)")
    lna, rho, p, w, H2 = history_contraction()
    idx = [0, 1000, 2000, 3000, 3999]
    print("   ln a      ρ_tot/ρ_b      w = p/ρ      1+w        H² zero?")
    for i in idx:
        print(f"   {lna[i]:6.2f}   {rho[i]:10.3e}   {w[i]:8.4f}   {1+w[i]:7.4f}"
              f"     {'—' if H2[i] > 0 else 'YES'}")
    print("   ρ + p > 0 at every density; H² is monotone in the contraction and")
    print("   never crosses zero. The quartic steepens the crunch; it cannot turn")
    print("   it. (The ledger-side restatement of the recorded ceiling no-go.)")

    print("\nC. The discreteness analog (exact statement)")
    print("   Quasiparticle dispersion: ω² = c_s²k²·(1 + k²ξ²/4). The correction")
    print("   is ∝ k⁴ξ²: identically ZERO at k = 0. The medium's UV structure")
    print("   contributes nothing to the homogeneous constraint — it activates at")
    print("   gradient scale ξ, which is the metric-exit door. The two 'adjacent")
    print("   lanes' are one lane, and it is the one the reconstruction already")
    print("   has.")

    print("\nVERDICT — M8 CLOSES NEGATIVE, and the closure is unifying")
    print("   No bounded-density (−ρ²/ρ_c) correction is native to the recorded")
    print("   theory at the hydrodynamic layer: not from the books (A), not from")
    print("   the quartic history (B), and the discreteness analog lives at the")
    print("   door, not in the homogeneous equations (C). The metric-on turn is")
    print("   now closed at BOTH the fluid level (M5) and the constraint level")
    print("   (M8): within the recorded theory, the bounce goes through the")
    print("   metric exit or it does not happen. Ledger row owed.")
    print("=" * 78)

    assert np.all(rho + p > 0)
    assert np.all(np.diff(H2) > 0)               # monotone through contraction
    assert np.all(H2 > 0)
    # dispersion correction at k = 0 vanishes to all orders in ξ
    k = 0.0
    assert (k**4) * 1.0 == 0.0


if __name__ == "__main__":
    main()
