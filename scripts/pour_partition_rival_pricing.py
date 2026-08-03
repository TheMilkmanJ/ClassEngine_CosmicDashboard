"""pour_partition_rival_pricing — task #11: the partition's rivals priced against the committed window (2026-07-27).

THE QUESTION THIS PRICES
  pour_partition_structure.py found the coincidence: the committed window
  ζ_BBN ∈ [0.25, 0.35] maps back to a pour-epoch energy share
  s = ρ_dark/ρ_SM = (27/112)·ζ_pour⁴ ∈ [0.9%, 3.5%], and s = α_c lands at
  the window's center.  Coincidence grade, because the pour's dynamics
  haven't derived the share.  What CAN be done at the desk is the house
  move: enumerate the natural rival partition rules and price each one
  against the committed window.  A rule that lands outside is dead as the
  partition's origin; the survivors define the live class.

THE RIVALS (each a physically-motivated share, no tuning)
  equipartition  s = g_dark/g_SM = 27/112 (dark sector born at the common
                 temperature — full thermal contact at the pour)
  gravity       s = (T_pour/M_Pl)³ (the recorded isolation strength —
                 gravitational-class transfer only)
  alpha_bare    s = α (one vertex at the BARE electromagnetic coupling)
  alpha_c_sq    s = α_c² (two medium vertices)
  epsilon       s = ε = 27α/5π (the electron-coupled scalar's own
                 fractional coupling — the corpus's other natural percent)
  alpha_c       s = α_c = 3α (one vertex at the MEDIUM's coupling — the
                 flagged coincidence)

CONVERSION (recorded dof arithmetic, verified in pour_partition_structure)
  ζ_pour = (s·112/27)^{1/4};  ζ_BBN = 0.568·ζ_pour;
  ΔN_eff = 27·ζ_BBN⁴/(7/4).  Committed: ζ_BBN ∈ [0.25, 0.35]
  ⟺ ΔN_eff ∈ [0.06, 0.24].
"""
from __future__ import annotations

M_PL_GEV = 1.22e19
T_POUR_GEV = 8.0e16
ALPHA = 1.0 / 137.036
ALPHA_C = 3.0 * ALPHA
EPS = 27.0 * ALPHA / (5.0 * 3.141592653589793)
RUNBACK = 0.568
ZLO, ZHI = 0.25, 0.35


def price(s: float):
    zeta_pour = (s * 112.0 / 27.0) ** 0.25
    zeta_bbn = RUNBACK * zeta_pour
    dneff = 27.0 * zeta_bbn ** 4 / (7.0 / 4.0)
    return zeta_pour, zeta_bbn, dneff


def main() -> None:
    print("=" * 78)
    print("The pour partition's rivals, priced against the committed window")
    print("=" * 78)
    rivals = [
        ("equipartition (27/112)", 27.0 / 112.0),
        ("gravity ((T/M_Pl)^3)", (T_POUR_GEV / M_PL_GEV) ** 3),
        ("bare alpha", ALPHA),
        ("alpha_c squared", ALPHA_C ** 2),
        ("epsilon = 27α/5π", EPS),
        ("alpha_c = 3α", ALPHA_C),
    ]
    print(f"\n   committed: ζ_BBN ∈ [{ZLO}, {ZHI}]  ⟺  ΔN_eff ∈ [0.06, 0.24]\n")
    print("   rule                       s          ζ_BBN     ΔN_eff    verdict")
    survivors = []
    for name, s in rivals:
        zp, zb, dn = price(s)
        alive = ZLO <= zb <= ZHI
        v = "SURVIVES" if alive else ("dead (above)" if zb > ZHI else "dead (below)")
        if alive:
            survivors.append((name, s, zb, dn))
        print(f"   {name:<25}  {s:.3e}  {zb:.4f}   {dn:.4f}    {v}")

    print("\n   the window's discrimination:")
    print("   * full thermal contact is EXCLUDED (ΔN_eff = 1.61 — the committed")
    print("     window itself kills equilibration, as the roster argument found);")
    print("   * gravitational-class transfer is EXCLUDED (ΔN_eff ~ 10⁻⁶ — the")
    print("     dark sector would be born essentially empty);")
    print("   * two-vertex and BARE-coupling shares fall below the window — the")
    print("     factor 3 in α_c = 3α is load-bearing: it moves the one-vertex")
    print("     share from outside the window to its center.")
    print(f"\n   survivors: {len(survivors)} — the single-medium-vertex class:")
    for name, s, zb, dn in survivors:
        print(f"     {name:<22} → ΔN_eff = {dn:.3f}")
    if len(survivors) == 2:
        d1, d2 = survivors[0][3], survivors[1][3]
        sep = abs(d2 - d1)
        print(f"\n   the two survivors differ by ΔN_eff = {sep:.3f}; at CMB-S4's")
        print(f"   forecast σ(ΔN_eff) ≈ 0.03 that is a {sep/0.03:.1f}σ separation —")
        print("   the registered prediction (P-2026-059, s = α_c → 0.146) and the")
        print("   ε-share alternative (0.084) are DISTINGUISHABLE by the same")
        print("   measurement that tests the window itself.")

    print("\nVERDICT: the committed window is not permissive — it discriminates")
    print("   partition CLASS.  Three rival classes die (equilibration, gravity,")
    print("   sub-percent couplings); the live class is exactly one vertex at a")
    print("   medium-percent coupling, with two members (α_c and ε) that CMB-S4")
    print("   separates.  The pour's own dynamics still owe WHICH member — the")
    print("   coincidence stays coincidence-grade — but the rule's CLASS is now")
    print("   priced, not assumed.")
    print("=" * 78)


if __name__ == "__main__":
    main()
