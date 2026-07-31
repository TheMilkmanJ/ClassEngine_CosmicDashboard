#!/usr/bin/env python3
"""
First-principles mutual friction α_B → census γ* (Phase 1b, 2026-07-31).

Does NOT invert α_B from A_s. Builds α_B from the recorded portal amplitude ε,
pushes it through the overdamped VOS map fixed in census_vos_microphysics.py,
and referees the prediction against the r-triangle f(r=1) and measured A_s.

Physical chain
--------------
1. The only small dimensionless coupling of the genesis winding medium to a
   dissipative channel is the electron-coupled portal amplitude
       ε = c · f̄ · α_c = 27α/(5π) ≈ 1.2543%.
   Mutual friction is a *response rate* (power of the coupling): leading
   dissipative entry is second order,
       α_B = ε².
   (First order in ε is the reversible mass shift δm/m = ε|cos θ|; dissipation
   starts at ε².)

2. Overdamped VOS structure (already forced by small γ*; see
   census_vos_microphysics.py):
       c_chop = O(1)   # topological reconnections — not portal-suppressed
       k_mom  = α_B²   # curvature momentum friction-suppressed
   with radiation β = 1/2:
       γ* = sqrt[ k_mom (k_mom + c_chop) ] ≈ α_B · sqrt(c_chop)   (k_mom ≪ c_chop)
           = ε² · sqrt(c_chop).

3. Chopping coefficient:
   Leading (c_chop = 1):  γ* = ε²                 [Route L]
   Transverse plane of a line defect is 2D, so the loop-chopping phase space
   carries a factor d_⊥ = 2:
       c_chop = 2,   γ* = ε² √2                 [Route T]
   Route T is the primary candidate; Route L is the coefficient-free floor.

4. Rejected alternatives (computed below for the record):
   - Thermal f_n = (T/T_c)⁴ at chain stage-5 z~10⁶: α_B ~ 10⁻¹² (too small)
     and *runs* with z (cannot hold γ* fixed across CMB decades).
   - Phonon ρ_n(T_d)/ρ_dm at ζT_γ: α_B ≫ 1 (not overdamped; wrong regime).
   - Global-string (T/η)² at Ψ₀: α_B ~ 10⁻⁴⁷ (irrelevant).
   - Identifying γ* = α_c²/2 with no force law: numerical near-miss only.

Grade rule
----------
  DERIVED:          force law fixes γ* with no free O(1) and matches f to ≲10%.
  CANDIDATE CLOSED: force law + one named O(1) (here d_⊥=2) matches; kill if
                    d_⊥ cannot be defended or if A_s residual fails.
  OPEN:             scale wrong by ≫O(1).
"""
from __future__ import annotations

import math
import sys

# ---- recorded PRTOE (no A_s in the prediction inputs) ----
ALPHA = 1.0 / 137.036
ALPHA_C = 3.0 * ALPHA
EPS = 27.0 * ALPHA / (5.0 * math.pi)          # = c·f̄·α_c
F_BAR = 2.0 / math.pi
C_FRAC = 9.0 / 10.0
K_SCREEN = math.log(1.0 + math.pi / (2.0 * ALPHA_C)) / math.pi
L_STAR = 61.86
AS_MEAS = 2.100e-9
AS_CLOSED = (ALPHA_C / (4.0 * math.pi * K_SCREEN)) ** 3
R_FID = 1.0
BETA = 0.5
T0_EV = 2.34865e-4                            # CMB T0 in eV
TC_DYAD_EV = 177.10e3                         # kernel T_c


def f_of_As(As: float, r: float = R_FID) -> float:
    return (2.0 * math.pi**2 * As) ** (1.0 / 3.0) / (r * L_STAR) ** (2.0 / 3.0)


def As_of_f(f: float, r: float = R_FID) -> float:
    return (r * L_STAR) ** 2 * f**3 / (2.0 * math.pi**2)


def gamma_overdamped(c_chop: float, k_mom: float, beta: float = BETA) -> float:
    return math.sqrt(k_mom * (k_mom + c_chop) / (4.0 * beta * (1.0 - beta)))


def v_overdamped(c_chop: float, k_mom: float, beta: float = BETA) -> float:
    return math.sqrt(k_mom * (1.0 - beta) / (beta * (c_chop + k_mom)))


def main() -> int:
    print("=" * 72)
    print("First-principles α_B → γ* (portal ε² + overdamped VOS)")
    print("=" * 72)

    # verify ε stack
    eps_stack = C_FRAC * F_BAR * ALPHA_C
    assert abs(eps_stack - EPS) / EPS < 1e-12

    f_ref = f_of_As(AS_CLOSED, R_FID)
    print(f"\n(0) Inputs (prediction side — no A_s):")
    print(f"  ε = c·f̄·α_c = {EPS:.6e}")
    print(f"  ε² = {EPS**2:.6e}   ε⁴ = {EPS**4:.6e}")
    print(f"  α_c = {ALPHA_C:.6e}, f̄ = {F_BAR:.6f}, c = {C_FRAC}")
    print(f"\n(0b) External referee only:")
    print(f"  f(r=1) from closed A_s = {f_ref:.6e}")
    print(f"  f(r=1) from measured A_s = {f_of_As(AS_MEAS):.6e}")
    print(f"  A_s closed = {AS_CLOSED:.6e}, measured = {AS_MEAS:.6e}")

    # ---- rejected thermal routes ----
    print(f"\n(1) Rejected thermal routes (record):")
    for z, tag in ((1e6, "chain stage-5"), (1e8, "T/Tc~0.13"), (7.5e8, "near Tc")):
        T = T0_EV * (1.0 + z)
        fn = (T / TC_DYAD_EV) ** 4 if T < TC_DYAD_EV else 1.0
        print(f"  f_n=(T/T_c)^4 at z={z:.1e} ({tag}): {fn:.4e}")
    print("  → stage-5 value ~1e-12 (too small); runs with z (breaks constant γ*).")
    print("  phonon ρ_n(ζT_γ)/ρ_dm at z~1e6: α_B ≫ 1 (not overdamped; wrong regime).")
    print("  (T/Ψ₀)² radiation friction at pour scale: ~1e-47 (irrelevant).")

    # ---- primary routes ----
    alpha_B = EPS**2
    k_mom = alpha_B**2          # = ε⁴
    print(f"\n(2) Portal friction:")
    print(f"  α_B = ε² = {alpha_B:.6e}  (second-order dissipative response)")
    print(f"  k_mom = α_B² = ε⁴ = {k_mom:.6e}")
    print(f"  v* and γ* for c_chop ∈ {{1, 2}}:")

    results = {}
    for c_chop, name in ((1.0, "L: c_chop=1 (coefficient-free)"),
                         (2.0, "T: c_chop=2 (transverse plane d_⊥)")):
        g = gamma_overdamped(c_chop, k_mom)
        v = v_overdamped(c_chop, k_mom)
        As_pred = As_of_f(g, R_FID)
        results[name] = dict(gamma=g, v=v, As=As_pred,
                             ratio_f=g / f_ref,
                             ratio_As=As_pred / AS_MEAS,
                             ratio_As_c=As_pred / AS_CLOSED)
        print(f"  {name}")
        print(f"    γ* = {g:.6e}   v* = {v:.6e}")
        print(f"    γ*/f_ref = {g/f_ref:.4f}")
        print(f"    A_s(r=1,γ*) = {As_pred:.6e}   "
              f"vs meas {As_pred/AS_MEAS:.4f}×, vs closed {As_pred/AS_CLOSED:.4f}×")

    # β-stationarity under Route T
    print(f"\n(3) γ(β) under Route T (k=ε⁴, c=2) — n_s≈1 robustness:")
    for b in (0.45, 0.50, 0.55, 2.0 / 3.0):
        g = gamma_overdamped(2.0, k_mom, b)
        tag = "  <- radiation" if abs(b - 0.5) < 1e-9 else (
            "  <- matter" if abs(b - 2.0 / 3.0) < 1e-9 else "")
        print(f"  β={b:.3f}: γ*={g:.6e}{tag}")

    # residual red tilt order-of-magnitude from approach-to-scaling
    # a = β(1+v²); transient ~ t^{a-1}; not a full n_s calc
    gT, vT = results["T: c_chop=2 (transverse plane d_⊥)"]["gamma"], \
             results["T: c_chop=2 (transverse plane d_⊥)"]["v"]
    # recompute v for route T
    vT = v_overdamped(2.0, k_mom)
    a_exp = BETA * (1.0 + vT**2)
    print(f"\n(4) Approach-to-scaling transient (order-of-magnitude, not n_s):")
    print(f"  v*(Route T) = {vT:.6e},  a-1 = {a_exp-1:+.6e}")
    print(f"  (red tilt residual still open as a full computation — see tilt_envelope).")

    # ---- grade ----
    rT = results["T: c_chop=2 (transverse plane d_⊥)"]
    rL = results["L: c_chop=1 (coefficient-free)"]
    print("\n" + "=" * 72)
    print("GRADE")
    print("=" * 72)

    if abs(rT["ratio_f"] - 1.0) < 0.05 and abs(rT["ratio_As"] - 1.0) < 0.05:
        grade = "CANDIDATE_CLOSED"
        detail = (
            "Route T (α_B=ε², c_chop=d_⊥=2, k_mom=ε⁴) lands γ* and A_s inside 5% "
            "of the r=1 triangle / measured amplitude WITHOUT fitting to A_s. "
            "Named residual: defend d_⊥=2 as the loop-chopping factor (transverse "
            "plane of a line defect), or replace it with a computed reconnection "
            "coefficient from the medium Lagrangian."
        )
    elif abs(rL["ratio_f"] - 1.0) < 0.35:
        grade = "CANDIDATE_O1"
        detail = "Route L (no d_⊥) is O(1); coefficient still open."
    else:
        grade = "OPEN"
        detail = "Portal scale does not land on f."

    print(f"  {grade}")
    print(f"  {detail}")
    print(f"""
  DERIVED (no free fit):
    - α_B = ε² from second-order portal dissipation
    - k_mom = α_B² = ε⁴ from overdamped friction suppression
    - c_chop = O(1) from topological reconnections (not ε-suppressed)
    - Route L floor: γ* = ε² = {rL['gamma']:.4e}  ({rL['ratio_f']:.3f} × f_ref)

  CANDIDATE (one named O(1)):
    - c_chop = d_⊥ = 2  →  γ* = ε²√2 = {rT['gamma']:.4e}
      ({rT['ratio_f']:.4f} × f_ref,  A_s = {rT['ratio_As']:.4f} × measured)

  KILL CONDITIONS:
    - d_⊥ shown not to control VOS chopping (reconnection sims / medium Lagrangian)
    - independent A_s channel (closed form) moves by ≫5% while Route T held fixed
    - promoting Route T while silently fitting c_chop to A_s

  NOT CLAIMED:
    - n_s − 1 = −0.035 from this α_B alone (still envelope / transient)
    - thermal f_n route
    - zero free parameters of the whole model (Track B inputs remain)
""")
    print("SUMMARY")
    print(f"  grade={grade}")
    print(f"  eps2={EPS**2:.6e}")
    print(f"  gamma_L={rL['gamma']:.6e}")
    print(f"  gamma_T={rT['gamma']:.6e}")
    print(f"  ratio_f_T={rT['ratio_f']:.6f}")
    print(f"  ratio_As_T={rT['ratio_As']:.6f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
