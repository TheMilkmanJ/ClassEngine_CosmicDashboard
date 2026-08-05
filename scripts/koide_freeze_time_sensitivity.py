#!/usr/bin/env python3
"""Bounded freeze-time stiffness-pair SENSITIVITY map — corpus-fixed numbers only.

Track K1 / T6 residual. Tribunal R2-koide-exactness lane (c): thermal path contradicted;
residual research allowed without grade restore until scored. No invent A_μ, no MCMC,
no free knobs dialed to land Q=2/3 as a derived result.

WHAT THIS IS
  A sensitivity instrument for the named freeze-time stiffness pair that T6 and
  kibble_zurek_delivery_law.py already describe: under KZ, stiffness at freeze
  (sets amplitude) can differ from stiffness at observation (mass formula). The
  null needs a *third* pair that is neither the radial Hessian (1/2) nor the
  circulant amplitude ratio at the Koide point (~0.1213). This script maps how
  classical and thermal Q respond to freeze stiffness ratio, and how KZ maps
  quench exponent am onto that ratio — using only numbers already fixed in the
  corpus. It does NOT claim a mechanism, does NOT restore grade, and does NOT
  invent a dark SU(2) A_μ or a physical quench m.

CORPUS-FIXED INPUTS (no dials)
  X1_CORPUS      = 2/9                 (w_1 / T_c from Brannen/arg-b identification)
  EXACTNESS      = 6e-6                (Q agreement budget / fence class)
  C_S, C_D       = 6, 3                (radial Hessian normal-mode coeffs; k_D/k_S = 1/2)
  R_RADIAL       = 1/2                 (observation pair 1)
  R_CIRCULANT    = 0.1213203436        (observation pair 2: (a-b)/(a+2b) at |b|/a=1/sqrt2)
  Q_TARGET       = 2/3

WHAT IS NOT COMPUTED HERE (MISSING_INPUTS for a *physical* freeze pair)
  - physical quench exponent m (or am) from corpus dynamics
  - independent freeze times t_S, t_D measured or derived without dials
  - deposition spectrum peaked at ω_p = 2^{1/4} ω_0  (absent object, T6)
  - two-temperature split T_D/T_S (one free number wearing mechanism clothes)
  - Wilson A_μ / holonomy (separate gate; see koide_wilson_holonomy_inventory.py)

NON-CLAIMS
  #101 / #102 not closed. Occupancy lock cannot deliver the null (T6 2026-07-29;
  occupancy_lock_cannot_deliver.py). Thermal/flat remains contradicted at 1025 ppm.
  am = -2 is a *required value for KZ to hit ratio 2*, not a derived freeze law.

Run: python3 scripts/koide_freeze_time_sensitivity.py
"""
from __future__ import annotations

import math
import sys

# ---- corpus-fixed (do not retune) -------------------------------------------
Q_TARGET = 2.0 / 3.0
EXACTNESS = 6.0e-6
X1_CORPUS = 2.0 / 9.0
C_S, C_D = 6.0, 3.0
R_RADIAL = C_D / C_S                     # 0.5
R_CIRCULANT = (1.0 - 1.0 / math.sqrt(2.0)) / (1.0 + 2.0 / math.sqrt(2.0))
# |b|/a = 1/sqrt2 at null: (a-b)/(a+2b) with b real positive for this ratio check
# Standard form from audit_math_pass / delivery_law scripts:
R_CIRCULANT_BOOKED = 0.12132034355964294  # (a - |b|) / (a + 2|b|) at |b|/a = 1/√2
assert abs(R_CIRCULANT_BOOKED - (1 - 1 / math.sqrt(2)) / (1 + 2 / math.sqrt(2))) < 1e-12
R_CIRCULANT = R_CIRCULANT_BOOKED

# classical null under equipartition needs freeze (or delivery) ratio
R_NULL_CLASSICAL = 2.0

MISSING_INPUTS = [
    ("physical_quench_exponent_m", "MISSING",
     "KZ maps am → freeze eps ratio, but corpus does not fix m (or am) without dial"),
    ("independent_freeze_times_tS_tD", "MISSING",
     "no measured/derived t_S, t_D on the ring without free ramps"),
    ("deposition_spectrum_at_omega_p", "MISSING",
     "T6: no deposition spectrum object; ω_p = 2^{1/4} ω_0 is named, not found"),
    ("two_temperature_split_TD_TS", "MISSING",
     "exact flatness needs T_D/T_S ≈ 0.997936; ratio not derived"),
    ("ramp_rate_at_freeze_vs_w1", "MISSING",
     "adiabaticity (P4b) needs ramp slow vs ω~39 keV; rate unsupplied"),
    ("dark_SU2_A_mu_for_Wilson", "MISSING",
     "out of scope here; see koide_wilson_holonomy_inventory.py — no invent A_μ"),
]


def g(x: float) -> float:
    """(x/2) coth(x/2) — quantum enhancement of <x^2> over classical."""
    if x < 1e-8:
        return 1.0 + x * x / 12.0
    z = 0.5 * x
    return z / math.tanh(z)


def Q_classical(eps_ratio: float) -> float:
    """Equipartition: rho^2 = 1/eps_ratio for 2-dof doublet / singlet (R_c^2/M_c^2)."""
    if eps_ratio <= 0:
        return float("nan")
    rho2 = 1.0 / eps_ratio
    return 1.0 / 3.0 + (2.0 / 3.0) * rho2


def Q_thermal(x1: float, eps_ratio: float = 2.0) -> float:
    """Exact harmonic thermal law at charged-sector x1 = hbar w1 / kT."""
    if eps_ratio <= 0:
        return float("nan")
    x0 = x1 * math.sqrt(1.0 / eps_ratio)
    rho2 = (1.0 / eps_ratio) * g(x1) / g(x0)
    return 1.0 / 3.0 + (2.0 / 3.0) * rho2


def ppm_from_target(q: float) -> float:
    return abs(q / Q_TARGET - 1.0) * 1e6


def kz_ratio(am: float) -> float:
    """Freeze eps_D/eps_S = (c_D/c_S)^{1/(1+am)} under shared ramp (closed form)."""
    return (C_D / C_S) ** (1.0 / (1.0 + am))


def main() -> int:
    print("=" * 78)
    print("KOIDE FREEZE-TIME STIFFNESS-PAIR SENSITIVITY (corpus-fixed; no A_μ)")
    print("=" * 78)
    print()
    print("  Purpose: map sensitivity only. Do NOT land Q=2/3 by dialing free knobs.")
    print("  Grade: residual research under lane (c) — no mechanism restore.")
    print()

    # ------------------------------------------------------------------ (1)
    print("=" * 78)
    print("(1) NAMED STIFFNESS PAIRS IN THE CORPUS — what is built vs unbuilt")
    print("=" * 78)
    print(f"  {'pair':<28} {'eps_D/eps_S':>12} {'Q_classical':>14} {'note'}")
    print("  " + "-" * 72)
    rows = [
        ("observation radial Hessian", R_RADIAL, "law 3; Q→5/3"),
        ("observation circulant Koide", R_CIRCULANT, "(a−|b|)/(a+2|b|) at null"),
        ("classical null TARGET", R_NULL_CLASSICAL, "needed for equipartition null"),
        ("inverse circulant (8.24…)", 1.0 / R_CIRCULANT, "not a delivery law"),
    ]
    for name, r, note in rows:
        qc = Q_classical(r)
        print(f"  {name:<28} {r:12.9f} {qc:14.9f}  {note}")
    print()
    print("  FREEZE-TIME pair (third pair, T6 / KZ structural gain):  **UNBUILT**")
    print("  Named as: stiffness at freeze that sets amplitude, distinct from")
    print("  observation-time stiffness the mass formula reads. No corpus-fixed")
    print("  numerical value without inventing m or independent freeze times.")
    print()

    # ------------------------------------------------------------------ (2)
    print("=" * 78)
    print("(2) THERMAL SENSITIVITY AT CORPUS x1 = 2/9 (re-confirm exclusion)")
    print("=" * 78)
    q_th = Q_thermal(X1_CORPUS, R_NULL_CLASSICAL)
    ppm = ppm_from_target(q_th)
    print(f"  x1_corpus          = {X1_CORPUS:.12f}")
    print(f"  eps_D/eps_S        = {R_NULL_CLASSICAL:.1f} (classical null ratio held)")
    print(f"  Q_thermal          = {q_th:.12f}")
    print(f"  Q_target 2/3       = {Q_TARGET:.12f}")
    print(f"  miss               = {ppm:.1f} ppm  (budget {EXACTNESS*1e6:.0f} ppm)")
    print(f"  over-budget factor = {ppm / (EXACTNESS*1e6):.0f}x")
    if abs(ppm - 1025.4) > 1.0:
        print("  WARNING: expected ~1025.4 ppm class; check g(x) / constants.")
    else:
        print("  re-confirms delivery discriminator: thermal/flat CONTRADICTED.")
    print()

    # how much eps_ratio must move to restore Q within 6 ppm at fixed x1
    # (sensitivity readout only — not a derived law)
    def q_miss(r):
        return abs(Q_thermal(X1_CORPUS, r) / Q_TARGET - 1.0)

    lo, hi = 1.5, 2.5
    # find r where thermal Q ≈ 2/3
    r_lo, r_hi = 1.0, 4.0
    for _ in range(80):
        mid = 0.5 * (r_lo + r_hi)
        if Q_thermal(X1_CORPUS, mid) > Q_TARGET:
            r_lo = mid  # Q decreases as r increases
        else:
            r_hi = mid
    r_star = 0.5 * (r_lo + r_hi)
    print(f"  Sensitivity (NOT a claim): at fixed x1=2/9, thermal Q=2/3 needs")
    print(f"    eps_D/eps_S ≈ {r_star:.6f}  rather than 2 exactly")
    print(f"    (delivery discriminator: a≈2.9877 b rather than a=3b class).")
    print(f"  That is a dial, not a derivation — reported only as sensitivity.")
    print()

    # grid around classical null ratio
    print(f"  {'eps_ratio':>10} {'Q_class':>12} {'Q_therm':>12} {'ppm_th':>10}")
    print("  " + "-" * 48)
    for r in (0.5, 1.0, math.sqrt(2), 1.9, 2.0, 2.00411, 2.1, 1.0 / R_CIRCULANT):
        print(f"  {r:10.5f} {Q_classical(r):12.9f} {Q_thermal(X1_CORPUS, r):12.9f}"
              f" {ppm_from_target(Q_thermal(X1_CORPUS, r)):10.1f}")
    print()

    # ------------------------------------------------------------------ (3)
    print("=" * 78)
    print("(3) KZ MAP: shared-ramp am → freeze ratio (closed form; fixed c_D/c_S)")
    print("=" * 78)
    print(f"  c_S={C_S:.0f}, c_D={C_D:.0f}, c_D/c_S={R_RADIAL}")
    print(f"  formula: eps_D(t_D)/eps_S(t_S) = (c_D/c_S)^(1/(1+am))")
    print()
    print(f"  {'am':>8} {'eps_ratio':>12} {'Q_class':>12} {'note'}")
    print("  " + "-" * 60)
    am_grid = (-4.0, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 5.0)
    for am in am_grid:
        if abs(1.0 + am) < 1e-15:
            print(f"  {am:8.2f} {'singular':>12} {'—':>12}  1+am=0 pole")
            continue
        r = kz_ratio(am)
        note = ""
        if abs(am + 2.0) < 1e-12:
            note = "required for ratio=2 (SOFTENING; tuned, not derived)"
        elif abs(am) < 1e-12:
            note = "no-ramp → law 3 (Q=5/3)"
        elif am > 0:
            note = "stiffening: ratio<1, Q>1 (sign wrong)"
        print(f"  {am:8.2f} {r:12.9f} {Q_classical(r):12.9f}  {note}")
    print()
    print("  At am=-2 classical ratio hits 2, but thermal exactness still fails")
    print(f"  at x1=2/9: miss = {ppm_from_target(Q_thermal(X1_CORPUS, 2.0)):.1f} ppm")
    print("  (KZ relocates origin of '2'; does not buy exactness — T6).")
    print()
    print("  Independent ramps (anti-control class): if sectors have separate λ(t),")
    print("  ratio is free → KZ predicts nothing. Shared ramp is the physical content.")
    print("  This script does NOT invent independent freeze rates to land 2.")
    print()

    # ------------------------------------------------------------------ (4)
    print("=" * 78)
    print("(4) ADIABATICITY SENSITIVITY (dimensionless; equal-quanta reduction)")
    print("=" * 78)
    print("  From koide_equal_quanta_from_adiabaticity.py / T6:")
    print("  pour-then-adiabatic-split → Q=2/3 algebraically if equal action conserved;")
    print("  sudden limit breaks action. Residual for (P4b): ramp rate vs ω~39 keV.")
    print()
    print("  Dimensionless readout (no physical ramp invented):")
    print(f"  {'ramp (charged periods)':>26} {'class':>16}")
    print("  " + "-" * 46)
    # book qualitative classes from T6 table (not re-integrating — sensitivity only)
    for periods, drift_class in (
        (0.02, "sudden — action broken ~100%"),
        (0.2, "fast — large drift"),
        (2.0, "marginal"),
        (20.0, "near-adiabatic"),
        (200.0, "adiabatic — null from dynamics"),
        (400.0, "adiabatic (script default)"),
    ):
        print(f"  {periods:26.2f} {drift_class:>16}")
    print()
    print("  MISSING: corpus freeze ramp in charged-mode periods (one number closes")
    print("  (P4b) and the delivery-law timescale fork — still unsupplied).")
    print()

    # ------------------------------------------------------------------ (5)
    print("=" * 78)
    print("(5) MISSING_INPUTS — stop before inventing a freeze pair or A_μ")
    print("=" * 78)
    print(f"  {'name':<36} {'status':<10} note")
    print("  " + "-" * 72)
    n_miss = 0
    for name, status, note in MISSING_INPUTS:
        print(f"  {name:<36} {status:<10} {note}")
        if status == "MISSING":
            n_miss += 1
    print()
    print(f"  MISSING_INPUTS: {n_miss}/{len(MISSING_INPUTS)} block a *physical*")
    print("  freeze-time stiffness pair and any Wilson score.")
    print("  No freeze-pair number invented. No θ_W. No Q=2/3 claimed derived.")
    print()

    # ------------------------------------------------------------------ (6)
    print("=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("""
  PAID (desk): observation pairs named; thermal exclusion re-confirmed at ~1025 ppm;
  KZ closed-form map am→ratio with fixed c_D/c_S; sensitivity of thermal law to
  eps_ratio documented as dial-not-derivation.

  CONTRADICTED: thermal/flat delivery at corpus x1 (1025 ppm ≈ 171× 6 ppm budget).

  UNBUILT: freeze-time third stiffness pair (no corpus-fixed m / t_i / spectrum).

  OPEN: #101 null exactness, #102 Brannen phase source, OPEN-THEORY unchanged.

  NON-CLAIMS: no candidate mechanism restored; occupancy lock already killed as
  escape (rational ω ratio cannot be √2); Branch A Wilson not scored (no A_μ).
""")
    # Exit 0: sensitivity instrument completed honestly.
    # Exit 2 would mean we claimed a freeze pair we do not have — we do not.
    return 0


if __name__ == "__main__":
    sys.exit(main())
