"""bounce_m5_exotic_fluid — M5: is there a native crunch-scale fluid X? (2026-07-26)

QUESTION
  The exotic-fluid reconstruction branch (metric stays on through the crunch)
  needs a component X with, at the handover a_b:
      Σρ = 0   (flat FRW: H = 0)      and      Σp < 0   (then Ḣ > 0).
  Without assuming radiation domination: X must be NEGATIVE and must scale at
  least as fast as the fastest positive component present, with strict
  inequality in w at the crossing.

THE FROZEN-RATIO ANCHOR (the sharp tool of this pass)
  If X scales exactly like a positive component (same a⁻ⁿ), their ratio is
  frozen for ALL time — so whether the combined coefficient is negative is
  decided by TODAY'S measurement, not by crunch physics.  A future crossing
  driven by an equal-scaling negative term requires the corresponding sector
  to be net-negative now, which observation excludes (radiation: N_eff ≈ 3,
  positive; shear: σ² ≥ 0 geometrically).

CANDIDATES PRICED (every recorded corner that could carry ρ < 0)
  1. Bare vacuum (n = 0, ρ < 0)         — turnaround only; frozen magnitude
  2. Torus Casimir, conformal (n = 4)   — frozen ratio + magnitude
  3. Ghost-condensate transient (n = 6) — recorded budget
  4. Trace-anomaly (ρ ~ N·H⁴)           — budget at the deepest metric-on point
  5. Attractive interaction energy      — no recorded attractive channel
  (Canonical matter / radiation / e± / EM / winding / shear / quartic floor
   are NEC-nonnegative or positive — recorded, not re-litigated.)

GRADE RULE
  A negative close of M5 retires the exotic-fluid branch as unbuildable from
  the recorded theory; the formal row goes to the failures ledger.  The
  modified-constraint lane (a −ρ²/ρ_c-class change to the Friedmann equation
  from medium discreteness) is NAMED as adjacent and unwritten — it is not a
  fluid, and it is not fabricated into existence here.
"""
from __future__ import annotations

import math

M_PL = 1.22089e19 * 1e9            # eV
AU_M = 1.496e11
EVINV_TO_M = 1.973269804e-7
H0 = (67e3 / 3.085677581e22) * 6.582119569e-16   # eV
OMEGA_R = 9.0e-5
GSTAR = 10.75
T_C = 177.10e3                     # eV
M_EV = 2.24e-20
LAM = 2e-91
XI = 402.0 * AU_M / EVINV_TO_M     # eV^-1
GPC_EVINV = 1.5637e42 / 1e9 * 1e9  # placeholder replaced below


def rho_c() -> float:
    return 3.0 * H0**2 * M_PL**2 / (8.0 * math.pi)


def rho_rad(T: float) -> float:
    return (math.pi**2 / 30.0) * GSTAR * T**4


def main() -> None:
    gpc = 3.085677581e25 / EVINV_TO_M          # 1 Gpc in eV^-1
    rho_r0 = OMEGA_R * rho_c()
    rho_b = M_EV**4 / LAM

    print("=" * 78)
    print("M5 — native exotic-fluid candidates for the metric-on crunch, priced")
    print("=" * 78)

    print("\n1. Bare vacuum (ρ < 0, constant)")
    r = 2.6e-11 / rho_rad(T_C)
    print(f"   |ρ_bare| ~ ρ_Λ vs ρ_rad(T_c): {r:.1e} — invisible at the deep")
    print("   crunch (recorded). Constant vs blueshifting positives: its only")
    print("   zero-crossing is the LOW-density one — the turnaround, not the")
    print("   bounce. Window: FAIL (w = −1 < 1/3 there anyway).")

    print("\n2. Conformal negative energy (torus Casimir class, n = 4)")
    for L_gpc in (1.0, 14.0):
        L = L_gpc * gpc
        cas = (math.pi**2 / 90.0) / L**4
        print(f"   |ρ_Cas|(L = {L_gpc:4.1f} Gpc) ≈ {cas:.2e} eV⁴  →  "
              f"|ρ_Cas|/ρ_rad,0 = {cas / rho_r0:.1e}")
    print("   Same a⁻⁴ scaling as radiation ⟹ the ratio is FROZEN at today's")
    print("   value forever. A future crossing needs the radiation sector")
    print("   net-negative NOW — excluded by N_eff ≈ 3. Dead twice over:")
    print("   measured sign, and ~119 orders of magnitude.")

    print("\n3. Ghost-condensate transient (negative stiff excursion, n = 6)")
    print("   The recorded arrow sector sits on its stable attractor at the")
    print("   dark-energy scale. The exotic-fluid target needs |ρ_X| at the")
    print("   handover budget — `scripts/bounce_rp_required_X.py` prices the")
    print("   shortfall at 10¹⁹–10³² depending on the handover variant, and the")
    print("   wormhole audit already prices sustained exotic stress ~17 orders")
    print("   under engineering need. No frozen negative a⁻⁶ track exists")
    print("   natively (σ² ≥ 0 geometrically; the ghost excursion is transient")
    print("   and amplitude-capped). Window: FAIL by budget.")

    print("\n4. Trace-anomaly / quantum-curvature terms (ρ ~ N·H⁴)")
    H_door = 1.0 / (math.sqrt(3.0) * XI)
    rho_door = (2.8e3) ** 4                      # M2 exit budget T_eff⁴
    H_floor = math.sqrt(8.0 * math.pi * rho_b / 3.0) / M_PL
    for name, H, need in (("shear door (M2)", H_door, rho_door),
                          ("condensate floor", H_floor, rho_b)):
        anom = 100.0 * H**4                      # generous N = 100
        print(f"   {name:18s}: N·H⁴ ≈ {anom:.2e} eV⁴ vs needed {need:.2e} eV⁴"
              f"  →  short {need / anom:.1e}")
    print("   The metric-on curvature never comes within ~95 orders of the")
    print("   handover budget. Window: FAIL by budget, everywhere.")

    print("\n5. Attractive interaction energy at high density")
    print("   The recorded medium quartic is repulsive (λ > 0, c_s² > 0 — the")
    print("   floor exists because of it); the portal couplings are perturbative")
    print("   and tiny. No recorded channel turns the interaction energy")
    print("   negative at crunch density. Window: FAIL — no candidate exists.")

    print("\nVERDICT — M5 CLOSES NEGATIVE")
    print("  No component of the recorded theory can be the exotic fluid: every")
    print("  negative-energy corner fails on measured sign (frozen ratio), on")
    print("  budget (19–119 orders), or on nonexistence. The exotic-fluid branch")
    print("  is UNBUILDABLE from native parts.")
    print()
    print("  Consequences for the reconstruction:")
    print("  * The hybrid policy collapses: the metric-exit build is the only")
    print("    reconstruction left. It alone carries the bounce, with its two")
    print("    assumed matching rules and the achronal-re-entry price (M4).")
    print("  * The sharpened conditional, now exhaustively priced at the fluid")
    print("    level: IF the metric stays on through the crunch, the recorded")
    print("    theory does not turn. The bounce REQUIRES the metric exit.")
    print("  * The one adjacent unwritten alternative is a modified Friedmann")
    print("    CONSTRAINT (−ρ²/ρ_c class, as in bounded-density cosmologies) —")
    print("    not a fluid; it would need a derivation from medium discreteness")
    print("    near the density ceiling that is not in the corpus. Named, not")
    print("    fabricated.")
    print("=" * 78)

    assert r < 1e-30
    cas14 = (math.pi**2 / 90.0) / (14.0 * gpc) ** 4
    assert cas14 / rho_r0 < 1e-110
    assert rho_door / (100.0 * H_door**4) > 1e90
    assert rho_b / (100.0 * H_floor**4) > 1e90


if __name__ == "__main__":
    main()
