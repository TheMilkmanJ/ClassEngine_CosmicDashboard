#!/usr/bin/env python3
"""ns_routeT_closure — Track A2: wire Route T f into the r-triangle (2026-07-31).

WHAT CHANGES WITH ROUTE T
  A1 candidate-closed the imprint cell fraction from medium microphysics:
      f = γ* = ε² √2 ≈ 2.225×10⁻⁴   (Route T: α_B=ε², c_chop=d_⊥=2, k_mom=ε⁴)
  independent of A_s (no fit).  The normalization triangle
      A_s = r² L*² f³ / 2π²
  previously used A_s + the P-2026-031 isocurvature band to *bound* r and
  *pin* f given r.  With f supplied from the medium, the same equation
  *determines* r.

QUESTIONS THIS SCRIPT ANSWERS
  1. Does r become a point (not just a band)?
  2. Does S/ζ = 1/(r L*) land inside the registered P-2026-031 band?
  3. Does the coherent envelope (n_s = 1 − 2/L*) plus the approach-to-scaling
     transient (a−1 = β(1+v*²)−1) fully account for n_s−1 ≈ −0.035, or leave
     a residual?

GRADE RULE
  CANDIDATE CLOSED: r determined inside the former iso band, residual S/ζ
  inside the registered band, envelope n_s within ≲1σ of measurement.
  OPEN residual: approach-to-scaling contribution not first-principles-
  computed (OOM only) — sub-σ gap after envelope.
  DEAD: r lands outside the iso band, or S/ζ leaves the registered class.
"""
from __future__ import annotations

import math
import sys

# ---- recorded PRTOE (same stack as census_alpha_B_first_principles) ----
ALPHA = 1.0 / 137.036
ALPHA_C = 3.0 * ALPHA
EPS = 27.0 * ALPHA / (5.0 * math.pi)          # c · f̄ · α_c
F_BAR = 2.0 / math.pi
C_FRAC = 9.0 / 10.0
K_SCREEN = math.log(1.0 + math.pi / (2.0 * ALPHA_C)) / math.pi
L_STAR = 61.86
AS_MEAS = 2.100e-9
AS_CLOSED = (ALPHA_C / (4.0 * math.pi * K_SCREEN)) ** 3
BETA = 0.5
C_CHOP_T = 2.0                                 # Route T: d_⊥

# P-2026-031 registered isocurvature amplitude class (triangle band)
ISO_MIN, ISO_MAX = 0.005, 0.02                 # 0.5% – 2%
# broader class quoted in envelope mechanism (sub-% to %)
ISO_CLASS = (0.002, 0.02)

NS_MEAS, NS_SIG = 0.9649, 0.0042
NS_TARGET_TILT = -0.035                        # conventional n_s−1 ≈ −0.035


def gamma_overdamped(c_chop: float, k_mom: float, beta: float = BETA) -> float:
    return math.sqrt(k_mom * (k_mom + c_chop) / (4.0 * beta * (1.0 - beta)))


def v_overdamped(c_chop: float, k_mom: float, beta: float = BETA) -> float:
    return math.sqrt(k_mom * (1.0 - beta) / (beta * (c_chop + k_mom)))


def As_of_r_f(r: float, f: float) -> float:
    return (r * L_STAR) ** 2 * f**3 / (2.0 * math.pi**2)


def r_of_As_f(As: float, f: float) -> float:
    """Invert A_s = r² L*² f³ / 2π²  →  r = √(2π² A_s) / (L* f^{3/2})."""
    return math.sqrt(2.0 * math.pi**2 * As) / (L_STAR * f**1.5)


def f_of_As_r(As: float, r: float) -> float:
    return (2.0 * math.pi**2 * As) ** (1.0 / 3.0) / (r * L_STAR) ** (2.0 / 3.0)


def main() -> int:
    print("=" * 78)
    print("Track A2 closure: Route T f into the normalization triangle")
    print("=" * 78)

    # ---- (0) Route T f from medium (no A_s) ----
    eps_stack = C_FRAC * F_BAR * ALPHA_C
    assert abs(eps_stack - EPS) / EPS < 1e-12
    alpha_B = EPS**2
    k_mom = alpha_B**2
    f_T = gamma_overdamped(C_CHOP_T, k_mom)
    v_T = v_overdamped(C_CHOP_T, k_mom)
    f_T_approx = EPS**2 * math.sqrt(2.0)
    assert abs(f_T - f_T_approx) / f_T < 1e-6

    print("\n(0) Route T f (from A1, independent of A_s):")
    print(f"  ε = c·f̄·α_c = {EPS:.6e}")
    print(f"  α_B = ε² = {alpha_B:.6e},  k_mom = ε⁴ = {k_mom:.6e}")
    print(f"  c_chop = d_⊥ = {C_CHOP_T:.0f}")
    print(f"  f = γ* = ε²√2 = {f_T:.6e}   (exact VOS: {f_T:.6e})")
    print(f"  v* = {v_T:.6e}")

    # ---- (1) Triangle before / after ----
    r_lo = 1.0 / (ISO_MAX * L_STAR)
    r_hi = 1.0 / (ISO_MIN * L_STAR)
    f_at_r1_meas = f_of_As_r(AS_MEAS, 1.0)
    f_at_r1_closed = f_of_As_r(AS_CLOSED, 1.0)

    r_meas = r_of_As_f(AS_MEAS, f_T)
    r_closed = r_of_As_f(AS_CLOSED, f_T)
    As_r1 = As_of_r_f(1.0, f_T)

    print("\n(1) Wire f into A_s = r² L*² f³ / 2π²  — is r determined?")
    print(f"  former iso band:  r ∈ [{r_lo:.3f}, {r_hi:.3f}]")
    print(f"  triangle pin at r=1: f_meas = {f_at_r1_meas:.6e}, "
          f"f_closed = {f_at_r1_closed:.6e}")
    print(f"  Route T f / f(r=1,meas)   = {f_T / f_at_r1_meas:.4f}")
    print(f"  Route T f / f(r=1,closed) = {f_T / f_at_r1_closed:.4f}")
    print(f"  → r(A_s meas,  f_T) = {r_meas:.4f}")
    print(f"  → r(A_s closed, f_T) = {r_closed:.4f}")
    print(f"  A_s(r=1, f_T) = {As_r1:.6e}  "
          f"({As_r1/AS_MEAS:.4f}× meas, {As_r1/AS_CLOSED:.4f}× closed)")
    r_in_band = r_lo <= r_meas <= r_hi
    print(f"  r determined? YES — point value ≈ {r_meas:.3f} "
          f"(not a band); inside former band: {r_in_band}")
    print("  self-consistency: A1 graded Route T against the r=1 triangle;")
    print(f"  solved r = {r_meas:.3f} ≈ 1, so the r=1 referee was not a cheat.")

    # ---- (2) Isocurvature residual ----
    iso_meas = 1.0 / (r_meas * L_STAR)
    iso_closed = 1.0 / (r_closed * L_STAR)
    iso_r1 = 1.0 / (1.0 * L_STAR)
    iso_ok = ISO_MIN <= iso_meas <= ISO_MAX
    iso_class_ok = ISO_CLASS[0] <= iso_meas <= ISO_CLASS[1]

    print("\n(2) Built-in isocurvature residual S/ζ = 1/(r L*) vs P-2026-031:")
    print(f"  registered band (triangle): [{ISO_MIN:.3f}, {ISO_MAX:.3f}] "
          f"= [{100*ISO_MIN:.1f}%, {100*ISO_MAX:.1f}%]")
    print(f"  broader class (envelope doc): [{ISO_CLASS[0]:.3f}, {ISO_CLASS[1]:.3f}]")
    print(f"  S/ζ (r_meas  = {r_meas:.4f}) = {iso_meas:.5f} = {100*iso_meas:.3f}%")
    print(f"  S/ζ (r_closed= {r_closed:.4f}) = {iso_closed:.5f} = {100*iso_closed:.3f}%")
    print(f"  S/ζ (r = 1 fiducial)         = {iso_r1:.5f} = {100*iso_r1:.3f}%")
    print(f"  inside triangle band? {iso_ok}")
    print(f"  inside broader class? {iso_class_ok}")
    print("  READ: residual is the percent-class registered line — one object")
    print("  read twice (mechanism residual ≡ P-2026-031 amplitude class).")

    # ---- (3) n_s: envelope + approach-to-scaling ----
    ns_env = 1.0 - 2.0 / L_STAR
    tilt_env = ns_env - 1.0
    tilt_meas = NS_MEAS - 1.0
    gap = tilt_meas - tilt_env          # residual after envelope
    sigma_env = (ns_env - NS_MEAS) / NS_SIG
    a_exp = BETA * (1.0 + v_T**2)
    a_m1 = a_exp - 1.0

    # Approach OOM: δ ∝ t^{a-1} ∝ k^{-2(a-1)} = k^{+1} for a-1=-1/2.
    # n_s−1|_approach ≈ 3 δ_pivot if |δ|≪1 (see script docstring / md).
    # Envelope already lands within data; approach is NOT computed to a number.
    delta_for_full_tilt = abs(NS_TARGET_TILT) / 3.0
    delta_for_gap = abs(gap) / 3.0

    print("\n(3) n_s − 1 ≈ −0.035: envelope + approach-to-scaling?")
    print(f"  envelope (coherent conversion): n_s = 1 − 2/L* = {ns_env:.5f}")
    print(f"    n_s − 1 = {tilt_env:+.5f}")
    print(f"  measured:  n_s = {NS_MEAS} ± {NS_SIG}")
    print(f"    n_s − 1 = {tilt_meas:+.5f}")
    print(f"  envelope vs data: Δn_s = {ns_env - NS_MEAS:+.5f} "
          f"= {sigma_env:+.2f}σ  (PASS at <1σ)")
    print(f"  residual after envelope: {gap:+.5f}  "
          f"(≈ {abs(gap)/abs(tilt_meas)*100:.1f}% of measured tilt)")
    print(f"  approach-to-scaling (Route T VOS):")
    print(f"    v* = {v_T:.6e}  ⇒  a = β(1+v*²) = {a_exp:.10f}")
    print(f"    a − 1 = {a_m1:.6e}  (red transient; exponent only)")
    print(f"  OOM (not a derivation): n_s−1|_approach ≈ 3 δ_pivot")
    print(f"    to supply full −0.035 alone would need |δ| ~ {delta_for_full_tilt:.4f}")
    print(f"    to close the post-envelope gap {gap:+.5f} need |δ| ~ {delta_for_gap:.5f}")
    print("  NEITHER |δ| is derived from formation epoch + initial mismatch.")
    print("  Approach-to-scaling remains OOM-OPEN; it is not required for")
    print("  data consistency (envelope already +0.66σ) and does not claim")
    print("  to finish the exact −0.035 from first principles alone.")

    # fraction of measured tilt explained by envelope
    frac_env = abs(tilt_env) / abs(tilt_meas)
    print(f"  envelope fraction of measured |n_s−1|: {100*frac_env:.1f}%")

    # ---- (4) Grade ----
    print("\n" + "=" * 78)
    print("GRADE")
    print("=" * 78)

    if not r_in_band or not iso_ok:
        grade = "DEAD"
        detail = (
            "r or S/ζ left the registered band — kill the conversion-rate "
            "normalization path."
        )
    elif abs(sigma_env) < 1.0 and r_in_band and iso_ok:
        grade = "CANDIDATE_CLOSED"
        detail = (
            "Route T f determines r ≈ 0.99 (point, not band); S/ζ ≈ 1.63% "
            "inside P-2026-031; envelope n_s = 0.9677 within 1σ of data. "
            "Named residual: approach-to-scaling amplitude uncomputed "
            f"(post-envelope gap {gap:+.4f}, sub-σ); A1's d_⊥=2 remains."
        )
    else:
        grade = "OPEN"
        detail = "r determined but residual/data consistency incomplete."

    print(f"  {grade}")
    print(f"  {detail}")
    print(f"""
  DETERMINED (were open / banded):
    - f = γ*_T = {f_T:.6e}           (from A1 Route T)
    - r = {r_meas:.4f}                 (from A_s meas + f_T; closed-form: {r_closed:.4f})
    - S/ζ = {100*iso_meas:.3f}%                 (was band 0.7–2.0% over r∈[0.8,2.3])

  CONSISTENT (data / registration):
    - r ∈ former iso band [{r_lo:.2f}, {r_hi:.2f}]
    - S/ζ ∈ P-2026-031 triangle band [{100*ISO_MIN:.1f}%, {100*ISO_MAX:.1f}%]
    - n_s envelope = {ns_env:.4f}  ({sigma_env:+.2f}σ vs {NS_MEAS} ± {NS_SIG})

  STILL OPEN (named, not hidden):
    - approach-to-scaling |δ| at pivot (needs formation epoch + IC mismatch)
    - A1 residual: defend d_⊥ = 2 (or replace with computed c_chop)
    - P-2026-031 external CMB referee at ℓ ≈ 170 (bound, not model-internal)

  NOT CLAIMED:
    - Derived grade (d_⊥ and approach |δ| remain)
    - n_s − 1 = −0.035 exact from approach transient alone
    - zero free parameters of the whole model (Track B inputs remain)

  KILL CONDITIONS:
    - medium reconnection returns c_chop far from 2 with no replacement O(1)
    - CMB bound on correlated isocurvature tightens below ~1% at the residual's
      scale class while r held at ~1
    - envelope form 1 − 2/L* excluded by future running (α_s) precision
""")
    print("SUMMARY")
    print(f"  grade={grade}")
    print(f"  f_T={f_T:.6e}")
    print(f"  r_meas={r_meas:.6f}")
    print(f"  r_closed={r_closed:.6f}")
    print(f"  S_over_zeta={iso_meas:.6f}")
    print(f"  ns_envelope={ns_env:.6f}")
    print(f"  ns_sigma={sigma_env:.3f}")
    print(f"  tilt_gap_after_envelope={gap:.6f}")
    print(f"  a_minus_1={a_m1:.6e}")

    # assertions: arithmetic lock
    assert abs(f_T - 2.225e-4) / 2.225e-4 < 0.01
    assert 0.95 < r_meas < 1.05
    assert r_lo <= r_meas <= r_hi
    assert ISO_MIN <= iso_meas <= ISO_MAX
    assert abs(ns_env - 0.9677) < 5e-4
    assert abs(sigma_env) < 1.0
    assert abs(As_of_r_f(r_meas, f_T) - AS_MEAS) / AS_MEAS < 1e-9
    assert abs(a_m1 + 0.5) < 1e-4

    return 0 if grade == "CANDIDATE_CLOSED" else 1


if __name__ == "__main__":
    sys.exit(main())
