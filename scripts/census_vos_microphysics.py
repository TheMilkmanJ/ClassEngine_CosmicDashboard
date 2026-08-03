#!/usr/bin/env python3
"""
Phase 1 E2E — census γ*/f from medium microphysics (not inverted from A_s).

Companion: docs/working_logs/census_gamma_star_derivation.md
Prior: scripts/census_scaling_network.py (class exhibited),
       scripts/as_normalization_triangle.py (f target at r~1).

WHAT THIS DOES
  1. Restates the overdamped VOS fixed point (Martins–Shellard).
  2. Maps a single mutual-friction number α_B → (v*, γ*) under the
     symmetric ansatz c_chop = k_mom = α_B (the minimal one-parameter
     overdamped closure).
  3. Records the curvature–friction force-balance estimate and why it
     alone cannot replace VOS (H-dependence / non-scaling).
  4. Compares γ* to the triangle target f(r=1) ≈ 2.21e-4 WITHOUT
     using A_s as an input to the microphysics — A_s appears only as
     the external referee of the prediction.
  5. Tests whether any *already recorded* PRTOE dimensionless
     (α_c, ε, c_s, f̄, …) forces α_B (or γ*) at the needed size.

HONEST RULE
  If γ* is obtained by solving for α_B from the A_s target, that is an
  *inversion*, not a derivation. The derivation grade requires
  α_B (or c_chop, k_mom) from medium constants first.
"""
from __future__ import annotations

import math
import sys

# ---------------------------------------------------------------- recorded PRTOE
ALPHA = 1.0 / 137.036
ALPHA_C = 3.0 * ALPHA
C_S = math.sqrt(ALPHA_C)          # BEC sound speed in c=1 units
EPS = 27.0 * ALPHA / (5.0 * math.pi)
F_BAR = 2.0 / math.pi
C_FRAC = 9.0 / 10.0
K_SCREEN = math.log(1.0 + math.pi / (2.0 * ALPHA_C)) / math.pi
L_STAR = 61.86                    # from as_normalization_triangle (computed)
AS_CLOSED = (ALPHA_C / (4.0 * math.pi * K_SCREEN)) ** 3
AS_MEAS = 2.100e-9
R_FID = 1.0                       # order-one conversion rate (triangle centre)

BETA_RAD = 0.5


def f_target(r: float = R_FID, As: float = AS_CLOSED) -> float:
    """Imprint cell fraction f = k·ξ from A_s = r² L*² f³ / 2π²."""
    return (2.0 * math.pi**2 * As) ** (1.0 / 3.0) / (r * L_STAR) ** (2.0 / 3.0)


def vos_fixed_point(beta: float, c_chop: float, k_mom: float):
    """Full VOS fixed point (same algebra as census_scaling_network.py)."""
    v2 = k_mom * (1.0 - beta) / (beta * (c_chop + k_mom))
    if v2 <= 0.0 or v2 >= 1.0:
        return float("nan"), float("nan")
    v = math.sqrt(v2)
    gamma = k_mom / (2.0 * beta * v)
    return gamma, v


def vos_overdamped_symmetric(alpha_B: float, beta: float = BETA_RAD):
    """
    Minimal one-parameter overdamped closure: c_chop = k_mom = α_B.
    For β=1/2: γ = α_B * √2,  v = 1/√2  (independent of α_B magnitude
    only if v formula uses equal coeffs — check).

    With c = k = α_B, β=1/2:
      v² = α_B*(1/2) / (1/2 * 2α_B) = 1/2  → v = 1/√2  (NOT small!)
    That is NOT the overdamped branch — equal O(α_B) coeffs with α_B→0
    still give v~O(1). Overdamping needs k_mom << c_chop or an explicit
    friction that suppresses v.

    Correct overdamped branch (small v): from matching
      γ = c_chop v / (2(1-β))     (A, v²≪1)
      γ = k_mom / (2 β v)         (B)
    ⇒ v² = k_mom(1-β)/(β c_chop) when k_mom ≪ c_chop
    ⇒ γ  = sqrt( k_mom c_chop / (4 β (1-β)) )   (approx)
    """
    # Relativistic-equal-coeff branch (diagnostic only)
    g_eq, v_eq = vos_fixed_point(beta, alpha_B, alpha_B)
    return g_eq, v_eq


def gamma_overdamped(c_chop: float, k_mom: float, beta: float = BETA_RAD) -> float:
    """Small-v fixed point γ = sqrt[ k_mom (k_mom + c_chop) / (4β(1-β)) ]."""
    return math.sqrt(k_mom * (k_mom + c_chop) / (4.0 * beta * (1.0 - beta)))


def v_overdamped(c_chop: float, k_mom: float, beta: float = BETA_RAD) -> float:
    v2 = k_mom * (1.0 - beta) / (beta * (c_chop + k_mom))
    return math.sqrt(max(v2, 0.0))


def main() -> int:
    print("=" * 72)
    print("Phase 1 — census γ*/f from medium microphysics")
    print("=" * 72)

    f_closed = f_target(R_FID, AS_CLOSED)
    f_meas = f_target(R_FID, AS_MEAS)
    print("\n(0) External referee only (not used as microphysics input):")
    print(f"  closed-form A_s = (α_c/4πk)³ = {AS_CLOSED:.4e}")
    print(f"  f(r=1) from closed A_s = {f_closed:.4e}")
    print(f"  f(r=1) from measured A_s = {f_meas:.4e}")
    print(f"  recorded medium: α_c={ALPHA_C:.5f}, c_s={C_S:.5f}, ε={EPS:.5f},")
    print(f"                   f̄={F_BAR:.5f}, c={C_FRAC:.2f}, k={K_SCREEN:.5f}")

    # ---------------------------------------------------------- (1) VOS algebra
    print("\n(1) Overdamped VOS fixed point (algebra):")
    print("  γ² = k_mom (k_mom + c_chop) / [4β(1-β)]")
    print("  v² = k_mom (1-β) / [β (c_chop + k_mom)]")
    print("  Radiation β=1/2 ⇒ γ = sqrt(k_mom(k_mom+c_chop)), v = sqrt(k/(c+k))")

    # ---------------------------------------------------------- (2) force balance
    print("\n(2) Curvature–friction force balance (why it is not enough alone):")
    print("  κ = 2π/m, ξ_h = 1/(m c_s),  κ = 2π c_s ξ_h  (identity).")
    print("  Tension μ ~ ρ_s κ² ln(ℓ/ξ_h)/(4π); friction γ_0 = ρ_s κ α_B.")
    print("  Balance + Hubble: ξ H ~ sqrt( (κ H ln)/(4π α_B) ).")
    print("  Problem: right-hand side still carries H (and m) → not a pure")
    print("  constant γ* unless α_B or ln runs to cancel H. Scaling γ* = const")
    print("  requires the dimensionless VOS reduction, not bare force balance.")
    print("  ⇒ mutual friction must enter as dimensionless (c_chop, k_mom).")

    # ---------------------------------------------------------- (3) one-param map
    print("\n(3) One-parameter overdamped maps → target f:")
    # Map A: k_mom = α_B², c_chop = 1  (chopping O(1), momentum suppressed by friction²)
    # Map B: k_mom = α_B², c_chop = α_B  (both friction-suppressed, chop linear)
    # Map C: k_mom = c_chop = α_B²      (symmetric friction-squared)
    # These are ANSÄTZE, not derivations — graded as such.
    target = f_closed
    maps = {
        "A: k=α_B², c=1": lambda a: (1.0, a * a),
        "B: k=α_B², c=α_B": lambda a: (a, a * a),
        "C: k=c=α_B²": lambda a: (a * a, a * a),
        "D: k=α_B, c=1": lambda a: (1.0, a),
    }
    print(f"  {'map':22s} {'α_B for γ=f':>12s} {'γ(α_B)':>10s} {'v*':>10s}")
    alpha_needed = {}
    for name, fn in maps.items():
        # binary search α_B in (1e-8, 1)
        lo, hi = 1e-8, 1.0
        for _ in range(80):
            mid = math.sqrt(lo * hi)
            c, k = fn(mid)
            g = gamma_overdamped(c, k)
            if g < target:
                lo = mid
            else:
                hi = mid
        a_star = math.sqrt(lo * hi)
        c, k = fn(a_star)
        g = gamma_overdamped(c, k)
        v = v_overdamped(c, k)
        alpha_needed[name] = (a_star, g, v)
        print(f"  {name:22s} {a_star:12.4e} {g:10.4e} {v:10.4e}")

    # ---------------------------------------------------------- (4) recorded candidates
    print("\n(4) Do recorded PRTOE numbers force α_B or γ* without A_s?")
    candidates = {
        "α_c": ALPHA_C,
        "ε": EPS,
        "c_s": C_S,
        "α_c²": ALPHA_C**2,
        "α_c²/2": ALPHA_C**2 / 2.0,
        "ε²": EPS**2,
        "ε·α_c": EPS * ALPHA_C,
        "ε·α_c·f̄": EPS * ALPHA_C * F_BAR,
        "α_c·f̄·c": ALPHA_C * F_BAR * C_FRAC,  # = ε
        "α/(4π)": ALPHA / (4.0 * math.pi),
        "(α_c/(4πk))": ALPHA_C / (4.0 * math.pi * K_SCREEN),
        "c_s⁴/2": C_S**4 / 2.0,
    }
    print(f"  {'candidate':20s} {'value':>12s} {'as γ*? ratio':>14s} {'as α_B mapA γ':>14s}")
    for name, val in candidates.items():
        ratio_as_gamma = val / target
        # interpret as α_B in map A (k=α², c=1): γ = sqrt(α_B² (α_B²+1)) ≈ α_B
        gA = gamma_overdamped(1.0, val * val)
        print(f"  {name:20s} {val:12.4e} {ratio_as_gamma:14.3f} {gA:14.4e}")

    # Best near-misses for γ* itself
    print("\n(5) Near-misses if a candidate is *identified with γ* (not derived):")
    ranked = sorted(candidates.items(), key=lambda kv: abs(math.log(kv[1] / target)))
    for name, val in ranked[:6]:
        print(f"  {name:20s}  {val:.4e}  vs f={target:.4e}  (ratio {val/target:.3f})")

    # ---------------------------------------------------------- (6) structural result
    print("\n(6) Structural results that DO land without A_s pin:")
    # Identity κ = 2π c_s ξ_h
    print("  [ok] κ = 2π c_s ξ_h  (quantum of circulation ↔ healing length)")
    # Overdamped branch selection: target γ << 1 forces v << 1 under map A/B/C
    aA, gA, vA = alpha_needed["A: k=α_B², c=1"]
    print(f"  [ok] target γ~{target:.2e} selects overdamped branch under map A:")
    print(f"       α_B~{aA:.2e}, v*~{vA:.2e}  (superfluid mutual-friction regime)")
    # Equal-coeff map fails overdamping
    g_eq, v_eq = vos_overdamped_symmetric(aA)
    print(f"  [ok] equal-coeff ansatz c=k=α_B does NOT overdamp (v*~{v_eq:.2f});")
    print("       momentum parameter must be friction-suppressed vs chopping.")
    # Stationarity of γ(β) at radiation — already in census_scaling_network
    g_lo = gamma_overdamped(1.0, aA * aA, 0.45)
    g_mid = gamma_overdamped(1.0, aA * aA, 0.50)
    g_hi = gamma_overdamped(1.0, aA * aA, 0.55)
    print(f"  [ok] γ(β) near radiation under map A: "
          f"{g_lo:.3e}, {g_mid:.3e}, {g_hi:.3e} (minimum at β=1/2 class)")

    # ---------------------------------------------------------- grade
    print("\n" + "=" * 72)
    print("GRADE")
    print("=" * 72)
    # Is any candidate within 20% of target as γ* with a mechanism story?
    best_name, best_val = ranked[0]
    best_ratio = best_val / target
    within_20 = abs(math.log(best_ratio)) < math.log(1.2)
    # α_c²/2 is 8.6% high — numerically close but NO mechanism forces γ*=α_c²/2
    mechanism_for_best = best_name in ()  # none yet
    if within_20 and mechanism_for_best:
        grade = "CANDIDATE CLOSED"
        detail = f"{best_name} = γ* with mechanism"
    elif within_20:
        grade = "NUMERICAL NEAR-MISS ONLY"
        detail = (
            f"{best_name} sits at ratio {best_ratio:.3f} to f(r=1), but no "
            f"medium equation forces that identification — coincidence risk "
            f"(α_c~0.022, target~2e-4 ⇒ many α_c/100-class combos look close)."
        )
    else:
        grade = "OPEN — one mutual-friction number"
        detail = "no recorded constant lands on f without A_s inversion"

    print(f"  {grade}")
    print(f"  {detail}")
    print("""
  DERIVED today:
    - overdamped branch selection is forced by the smallness of f (v*≪1)
    - equal-coeff VOS cannot produce that branch; k_mom must be
      friction-suppressed relative to chopping (map structure)
    - bare curvature–friction balance is insufficient (retains H)
    - κ ↔ ξ_h identity holds on recorded (m, c_s)

  NOT DERIVED today:
    - the absolute value γ* = f ≈ 2.21×10⁻⁴ from medium constants alone
    - α_B from first principles (phonon/normal-fluid content at imprint)
    - any safe identification γ* = α_c²/2 or similar without a force law

  RETYPED RESIDUE:
    One dimensionless mutual-friction (or VOS pair) number for the genesis
    tangle. Inversion from A_s gives α_B ~ 2×10⁻⁴ under map A — that is a
    *measurement* of the tangle's dissipation, not a derivation of A_s.

  KILL CONDITION for a future claim of derivation:
    A papered identification γ* = f(α_c,ε,…) that only matches because both
    sides were built from A_s, or a free α_B fitted to A_s and then declared
    derived.
""")

    # machine-readable summary line for harnesses
    print("SUMMARY")
    print(f"  grade={grade.replace(' ', '_')}")
    print(f"  f_target_closed={f_closed:.6e}")
    print(f"  best_numerical={best_name}:{best_val:.6e}:ratio={best_ratio:.4f}")
    print(f"  alpha_B_mapA_inverted={alpha_needed['A: k=α_B², c=1'][0]:.6e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
