"""bounce_rp_required_X — reverse-engineered stress-energy window for a homogeneous FRW bounce.

Racing Point method: before naming microphysics, read off what the outer workings require.

Flat FRW:
    H  = 0  =>  rho_tot = 0
    dH > 0  =>  rho_tot + p_tot < 0

With radiation + X (floor negligible or w=-1):
    rho_X = -rho_rad
    p_X   < -rho_rad/3
    =>  w_X > 1/3   with rho_X < 0

This script only prints that aero target at recorded scales. It does not invent X.
"""
from __future__ import annotations

import math

T_c_eV = 177.10e3
gstar = 10.75
m_eV = 2.24e-20
lam = 2e-91
rho_L = (2.25e-3) ** 4


def rho_rad(T_eV: float, g: float = gstar) -> float:
    return (math.pi**2 / 30.0) * g * T_eV**4


def main() -> None:
    rho_b = m_eV**4 / lam
    rr = rho_rad(T_c_eV)

    print("=" * 72)
    print("RP required X window (homogeneous FRW bounce aero target)")
    print("=" * 72)
    print("  At radiation-dominated handover:")
    print("    rho_X = -rho_rad")
    print("    p_X   < -rho_rad/3")
    print("    w_X   > 1/3   (with rho_X < 0)")
    print()
    print(f"  At T_c = {T_c_eV/1e3:.2f} keV:")
    print(f"    |rho_X| = {rr:.3e} eV^4")
    print(f"    |rho_X|/rho_Lambda  = {rr/rho_L:.3e}")
    print(f"    |rho_X|/rho_bounce  = {rr/rho_b:.3e}")
    print()
    print("  At residual radiation f * rho_bounce:")
    for f in (1e-6, 1e-3, 1e-2, 1e-1, 1.0):
        r = f * rho_b
        print(
            f"    f={f:.0e}: |rho_X|={r:.3e} eV^4  "
            f"|rho_X|/rho_L={r/rho_L:.3e}"
        )
    print()
    print("VERDICT:")
    print("  DE-scale legal parts cannot fill this window (orders short).")
    print("  Homogeneous fluid bounce needs crunch-scale negative energy with w>1/3,")
    print("  or the reconstruction must leave homogeneous FRW (Build RP-A).")
    print("=" * 72)

    assert rr / rho_b > 1e6
    assert rr / rho_L > 1e20


if __name__ == "__main__":
    main()
