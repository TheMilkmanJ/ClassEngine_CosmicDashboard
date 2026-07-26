"""bounce_m4_arrow_boundary — M4: causal character of the non-metric boundary.

QUESTIONS
  1. When is the switch-off / re-entry boundary spacelike (a "moment") vs
     timelike (a "place" — a localized wall in space)?
  2. What does the white-hole prohibition (no local time-reversed emitting
     boundary) cost the reconstruction at re-entry?
  3. Does that cost collide with the inhomogeneous-concentration shortcut
     (the Delta-rho ~ 5e10 route priced in M2b hypothesis H3)?

SETUP
  The boundary is a level set F(t,x) = 0 of the exit criterion (rho_eff =
  rho_exit, equivalently sigma = 1/xi at the shear door). In FRW,
  ds^2 = -dt^2 + a^2 dx^2, the surface is SPACELIKE iff its normal is
  timelike:  (dF/dt)^2 > |grad F|^2 / a^2,  i.e.  |rho_dot| > |grad rho|.
  With rho_eff ~ a^-6 in shear domination, rho_dot = -6 H rho_eff, and a
  contrast delta over proper scale L gives |grad rho| ~ rho * delta / L:

      SPACELIKE  <=>  delta < 6 (L / R_H)        [shear-dominated door]

  and the crossing-epoch offset of a region with contrast delta is

      dt_cross = delta / (6 |H_door|) = delta * R_H / 6.

  Achronality of the re-entry surface then demands (absent a written
  re-synchronization mechanism inside the medium interval)

      hold time of the non-metric interval  >=  dt_cross(max contrast).

GRADE RULE
  This writes a CONSTRAINT on the fabricated matching rules, not a mechanism.
  Nothing here derives the bounce.
"""
from __future__ import annotations

import math

ALPHA = 1.0 / 137.036
C_S = math.sqrt(3.0 * ALPHA)          # corpus-style sound speed ~ 0.148
RH_OVER_XI = math.sqrt(3.0)           # M2: R_H / xi = sqrt(3) at the shear door
N_SHEAR = 6.0                         # rho_eff ~ a^-6 in shear domination
T_MIX_OVER_THEAL = 1.2e7              # M2b: mixmaster window in healing times
DELTA_H3 = 5.0e10                     # M2b H3: concentration replacing compression


def delta_star(L_over_xi: float) -> float:
    """Largest contrast on proper scale L keeping the door spacelike."""
    return N_SHEAR * L_over_xi / RH_OVER_XI


def hold_over_theal(delta: float) -> float:
    """Required non-metric hold time, in healing times t_heal = xi/c_s."""
    dt_over_xi = delta * RH_OVER_XI / N_SHEAR       # dt_cross / xi
    return dt_over_xi * C_S                          # / (xi/c_s)


def main() -> None:
    print("=" * 78)
    print("M4 — causal character of the non-metric boundary (constraint pass)")
    print("=" * 78)
    print()
    print("A. Spacelike condition at the shear door  (delta < 6 L / R_H, R_H = sqrt3 xi)")
    for L in (0.1, 0.5, 1.0, 3.0, 10.0):
        print(f"   L = {L:5.1f} xi   ->  door spacelike up to contrast delta* = {delta_star(L):8.2f}")
    print("   READ: on healing-length scales and above, the door stays spacelike up")
    print("   to ORDER-UNITY contrasts. Sub-xi structure is inside the medium regime")
    print("   anyway. Collapsed regions (delta >> 1 on L >~ xi) turn their door")
    print("   segment TIMELIKE — an ingoing absorbing wall. Absorbing walls are")
    print("   black-hole-class and allowed; the prohibition bites at RE-ENTRY only.")
    print()
    print("B. The re-entry (arrow) constraint")
    print("   A point may not re-enter the expanding metric phase while a causally")
    print("   adjacent region is still on the contracting metric branch: the")
    print("   interface would be a timelike boundary emitting into the contracting")
    print("   exterior — exactly the white-hole-class local object the model")
    print("   forbids. Absent a written re-synchronization mechanism inside the")
    print("   medium interval (that would be a NEW fabricated part, F-A5), the")
    print("   crossing-epoch offsets survive, so the interval must HOLD:")
    print()
    for d, label in ((1.0, "order-unity contrast at the door"),
                     (1.0e3, "deeply nonlinear pockets"),
                     (DELTA_H3, "M2b H3 concentration shortcut")):
        h = hold_over_theal(d)
        print(f"   delta = {d:8.1e}  ({label:34s}):  hold >= {h:9.2e} t_heal")
    print()
    ratio = hold_over_theal(DELTA_H3) / T_MIX_OVER_THEAL
    print("C. Collision with the concentration shortcut (H3)")
    print(f"   hold(H3) / mixmaster window = {ratio:.0f}")
    print("   READ: using Delta-rho ~ 5e10 concentration to replace the assumed")
    print(f"   compression e-folds would demand a hold ~{ratio:.0f}x LONGER than the")
    print("   entire classical chaos window. The causal constraint and the")
    print("   concentration shortcut are in tension: hot patches cannot double as")
    print("   a cheap spacelike re-entry. H3 now carries a causal cost.")
    print()
    print("D. Arrow through the interval")
    print("   With the metric off, time orientation is carried by the medium's own")
    print("   clock (the condensate phase drift <theta_dot> != 0 — the recorded")
    print("   arrow sector). Switch-off and re-entry surfaces are ordered by that")
    print("   clock; NO local time-reversed metric patch is needed anywhere in the")
    print("   assembly: switch-off is an ending cap, re-entry a beginning cap.")
    print()
    print("VERDICT (M4)")
    print("   O8 (no white-hole engine): PASS-SHAPED in structure, at a price now")
    print("   written as an equation: re-entry must be achronal, so the interval")
    print("   holds >= delta_max * R_H / 6, or a re-synchronization mechanism must")
    print("   be exhibited (new fabricated part F-A5, named).")
    print("   Smooth doors (delta <~ 1): hold ~ 0.04 t_heal — causally cheap.")
    print("   Concentration route (H3): hold ~ 2e9 t_heal — causally expensive.")
    print("   The bounce is still NOT derived; M4 adds a hard boundary condition")
    print("   that any future matching rule must satisfy.")
    print("=" * 78)

    assert abs(delta_star(1.0) - 2.0 * math.sqrt(3.0)) < 1e-12
    assert hold_over_theal(1.0) < 0.1
    assert hold_over_theal(DELTA_H3) / T_MIX_OVER_THEAL > 100.0


if __name__ == "__main__":
    main()
