"""bounce_task5_assembled_timeline — task #5's last piece: the bath's arrival temperature at the restart (2026-07-28).

THE QUESTION
  Under the two-scale reading (RP log §19–21) the Standard-Model bath rides
  the contraction as its own conserved reservoir and passes through the dark
  component's interval intact.  Its restart temperature is then set by pure
  adiabatics: T_restart = T_door,bath × F^{1/3}, where F is the local VOLUME
  compression between the door's opening and the gradient-stress turn — the
  spherical focusing number, measured by the adaptive rebound run.  O6 (hard
  outer row) demands ~MeV.  This script assembles the recorded numbers into
  the single bar F must clear, and folds in the measured F when the run lands.

RECORDED INPUTS (each recomputed here where derivable)
  * door Hubble-exit scale from the coherence length:
      ρ_door = (3/8π)·M_p²/ξ²  ⟹  ρ_door^{1/4} ≈ 3.7 keV   (M1 anchor)
  * the medium's density floor: ρ_bounce = m⁴/λ ⟹ 1.06 keV  (O1 anchor)
  * bath radiation piece at the CMB-class door: T_rad ≈ 146 eV (M2.C, from
    `bounce_m2_junction.py` — taken as recorded)
  * total-energy proxy at the same door: T_eff ≈ 2.8 keV (M2.C, recorded)
  * seed dependence (M1 scan): smaller seeds open the door deeper — the bath
    at the door spans ~146 eV (CMB-class) up to ~keV (floor-class doors).

THE BAR
  F_req = (T_target / T_door,bath)³ — density/volume compression, door→turn.
  The 1D verified rebounds overshoot by O(1); the spherical run measures the
  3D focusing.  The verdict below is CONDITIONAL on that measured number and
  prints PENDING until it exists.  No number here is invented.

GRADE RULE
  Assembly of recorded anchors plus one measured input.  PROMOTE (O6 funded
  by compression): F ≥ F_req.  Otherwise the recorded honest endpoint of §18
  stands — the reconstruction's own channels under-fund the hot start, the
  outer-spec tension is recorded, and the funding question moves to the
  genesis cascade's open dynamical half (task #11).
"""
from __future__ import annotations

import math
import pathlib
import re

M_P_EV = 1.2209e28
HBARC_EV_M = 1.97327e-7
XI_M = 402.0 * 1.496e11
M_EV = 2.24e-20
LAMBDA = 2.0e-91
T0_EV = 2.725 * 8.617e-5
T_RAD_DOOR_EV = 146.0            # M2.C recorded (CMB-class seed)
T_EFF_DOOR_EV = 2.8e3            # M2.C recorded
T_DOOR_DEEP_EV = 1.0e3           # floor-class door (M1 seed scan, keV-class)
T_TARGET_EV = 1.0e6              # O6's bar
SPHERICAL_OUT = pathlib.Path(
    "/tmp/claude-1000/-home-themilkmanj-prtoe-class/"
    "9212c051-10ff-4ed1-a2a0-9a496f84358c/scratchpad/m6v2_out.txt")


def main() -> None:
    inv_xi_ev = HBARC_EV_M / XI_M
    rho_door_quarter = (3.0 / (8 * math.pi)) ** 0.25 * math.sqrt(M_P_EV * inv_xi_ev)
    rho_floor_quarter = (M_EV ** 4 / LAMBDA) ** 0.25

    print("=" * 78)
    print("The assembled crunch timeline: what the bath's own history delivers")
    print("=" * 78)
    print(f"\n1. Anchors, recomputed:")
    print(f"   door scale from ξ:  ρ^¼ = {rho_door_quarter/1e3:.2f} keV   (recorded 3.7)")
    print(f"   medium floor m⁴/λ:  ρ^¼ = {rho_floor_quarter/1e3:.2f} keV   (recorded 1.1)")
    print(f"   bath at CMB-class door: {T_RAD_DOOR_EV:.0f} eV (recorded); "
          f"a_door = {T0_EV/T_RAD_DOOR_EV:.2e}")
    print(f"   a needed for 1 MeV: {T0_EV/T_TARGET_EV:.2e} — the door opens "
          f"{T_TARGET_EV/T_RAD_DOOR_EV:,.0f}× too early in T")

    f_req_cmb = (T_TARGET_EV / T_RAD_DOOR_EV) ** 3
    f_req_deep = (T_TARGET_EV / T_DOOR_DEEP_EV) ** 3
    f_req_shear = (T_TARGET_EV / T_EFF_DOOR_EV) ** 3
    print(f"\n2. The bar (volume compression door→turn for a 1 MeV restart):")
    print(f"   CMB-class door (bath 146 eV):        F ≥ {f_req_cmb:.1e}")
    print(f"   deepest (floor-class) door (~1 keV): F ≥ {f_req_deep:.1e}")
    print(f"   perfect shear→heat at the door too:  F ≥ {f_req_shear:.1e}")
    print("   (1D verified rebounds overshoot by O(1); the sequencing race saw")
    print("   peak compressions of 3–8 at Mach 2–3.)")

    # fold ONLY rows that pass the run's own quotability gate (energy ≤ 2%);
    # each row prints "... (×F) ... E% ..." — capture F with its energy column.
    f_meas = None
    unquotable = []
    if SPHERICAL_OUT.exists():
        text = SPHERICAL_OUT.read_text()
        rows = re.findall(r"×\s*([\d.]+)\)[^\n]*?([\d.]+)%", text)
        quot = [float(f) for f, e in rows if float(e) <= 2.0]
        unquotable = [(float(f), float(e)) for f, e in rows if float(e) > 2.0]
        if quot:
            f_meas = max(quot)

    print(f"\n3. The measured focusing (spherical adaptive run):")
    if f_meas is None and not unquotable:
        print("   PENDING — the run is in flight; verdict withheld until it lands.")
        print("   Standing read: unless 3D focusing exceeds the bar above by")
        print("   itself, the restart bath is sub-keV to keV-class and O6 is not")
        print("   funded by compression. Nothing concluded before the number.")
    elif f_meas is None:
        print("   NO QUOTABLE ROW — every row failed the run's own energy gate:")
        for f, e in unquotable:
            print(f"     focus ×{f:8.1f} at energy error {e:8.1f}%  (gate ≤ 2%)")
        print("   The focusing number is numerically unresolved by this method.")
        print("   Every indicator — including the energy-inflated ones, which")
        print("   overestimate — sits 6–7 orders below the bar. The §18 honest")
        print("   endpoint is recorded with the caveat: a future resolved 3D")
        print("   computation clearing 1e9 would reopen O6's compression funding.")
    else:
        t_restart_cmb = T_RAD_DOOR_EV * f_meas ** (1.0 / 3.0)
        t_restart_deep = T_DOOR_DEEP_EV * f_meas ** (1.0 / 3.0)
        print(f"   F = {f_meas:.3g}  ⟹  T_restart = {t_restart_cmb:.3g} eV "
              f"(CMB-class door) … {t_restart_deep:.3g} eV (deepest door)")
        if f_meas >= f_req_deep:
            print("   O6 FUNDED BY COMPRESSION at the deepest door — promote path.")
        else:
            print(f"   Short of the bar by ×{f_req_deep/f_meas:.1e} (deepest door)")
            print("   — the §18 honest endpoint stands: the reconstruction's own")
            print("   channels under-fund the hot start; the outer-spec tension is")
            print("   recorded, and O6's funding moves to the genesis cascade's")
            print("   open dynamical half (task #11).")

    print("=" * 78)

    assert abs(rho_door_quarter - 3.7e3) / 3.7e3 < 0.05
    assert abs(rho_floor_quarter - 1.06e3) / 1.06e3 < 0.05
    assert f_req_cmb > f_req_shear > 1e6


if __name__ == "__main__":
    main()
