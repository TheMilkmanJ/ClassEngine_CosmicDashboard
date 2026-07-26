"""bounce_task5_door_budget — the MeV question as a single ledger (2026-07-27).

QUESTION (task #5)
  BBN needs a weak-equilibrium start: T ≳ 1 MeV.  The door delivers keV-class
  budgets.  Assemble every computed channel into one ledger, price the new
  quench channel from the translation table, and name the live levers.

THE QUENCH CHANNEL, PRICED HERE (new)
  The translation table found modes with k·ξ ≲ 2.5 cross the door as a quench
  (squeezed — quanta created).  Generous estimate: occupation gain Δn ~ 1 per
  mode up to k* = 2.5/ξ, mean energy ~2·m·c_s² per quantum:
      ρ_quench ≈ (k*³/6π²)·⟨ε⟩ ≈ 0.5·m·c_s²/ξ³
  with the recorded m = 2.24×10⁻²⁰ eV, c_s = √(3α), ξ = ħ/(m·c_s).

GRADE RULE
  A ledger of computed numbers and named pendings.  No channel is invented;
  no pending is prejudged.
"""
from __future__ import annotations

import math

M_EV = 2.24e-20
C_S = math.sqrt(3.0 / 137.036)
T_EXIT_KEV = 2.8            # M2 door budget (CMB-class seed, shear included)
MEV_KEV = 1000.0


def main() -> None:
    mc2 = M_EV * C_S**2                       # eV
    inv_xi = M_EV * C_S                       # 1/ξ in eV
    rho_quench = 0.5 * mc2 * inv_xi**3        # eV⁴, generous
    rho_exit = (T_EXIT_KEV * 1e3) ** 4
    rho_mev = (MEV_KEV * 1e3) ** 4

    print("=" * 78)
    print("The MeV door budget — one ledger (task #5)")
    print("=" * 78)
    print(f"\n   the bar: ρ(1 MeV) = {rho_mev:.2e} eV⁴;  the door: ρ_exit = "
          f"{rho_exit:.2e} eV⁴  (deficit ×{rho_mev/rho_exit:.1e})")
    print("\n   channel                          size            verdict")
    print(f"   door budget (computed, M2)       T_eff = 2.8 keV   ×1.6e10 under in density")
    print(f"   electron-family gates (recorded) 177–511 keV       ×2–5.6 under in T; candidate clock only")
    print(f"   quench injection (NEW, priced)   {rho_quench:.1e} eV⁴   "
          f"×{rho_exit/rho_quench:.0e} under the DOOR itself — closed")
    print(f"   compression free param (retired) N_med ≳ 6.2       fabricated; replaced by measured overshoot")
    print(f"   1D rebound overshoot (verified)  ×~1 (order unity)  does not fund MeV")
    print(f"   spherical focusing               PENDING            the adaptive run (in flight)")
    print(f"   SM-sector crossing (task #14)    UNWRITTEN          the bath's photons ARE most of the")
    print(f"                                                       energy; its physics could dominate")
    print("\nREAD")
    print("  1. The quench channel closes immediately: creating long-wavelength")
    print(f"     medium quanta at the door injects ~{rho_quench:.0e} eV⁴ — about 97")
    print("     orders below even the door's own keV budget. Honest and dead.")
    print("  2. Every computed channel is keV-class or below. The MeV question")
    print("     now rests on exactly TWO live levers, both named, neither")
    print("     prejudged: the spherical focusing amplification (a number the")
    print("     adaptive run is computing right now), and the Standard-Model")
    print("     sector's crossing (task #14 — where most of the bath's energy")
    print("     actually lives, and the only channel big enough to matter if")
    print("     focusing falls short).")
    print("  3. If both levers fail, the honest endpoint is: the reconstruction")
    print("     under-funds BBN and says so — that becomes an outer-spec tension")
    print("     for the whole build, not a knob to turn.")
    print("=" * 78)

    assert rho_quench < 1e-80
    assert rho_mev / rho_exit > 1e9
    assert rho_exit / rho_quench > 1e90


if __name__ == "__main__":
    main()
