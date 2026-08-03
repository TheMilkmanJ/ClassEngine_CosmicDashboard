#!/usr/bin/env python3
"""koide_wilson_holonomy_inventory — Branch A Wilson holonomy gate check (2026-08-03).

Does NOT compute a holonomy. Does NOT fit lepton masses. Does NOT elastic-hit 2/9.

Purpose: prove whether corpus-fixed inputs exist for a zero-free-knob Wilson-line
electric holonomy of the dark SU(2) gauge field around the family cycle, as named in
T6 / debt_koide_20260803 REPORT §3. If any required input is missing or is itself a
free dial, the script exits 2 with MISSING_INPUTS and refuses to invent one.

Pre-registered bins (filed in REPORT before this script scores anything; repeated
here only for documentation — this script never scores a holonomy value):

  θ★_0 = 2/9
  θ★_+ = 2/9 + 2π/3
  θ★_- = 2/9 − 2π/3
  W_hit = 3 · max(σ_θ_mass, half-millidegree)  [from stated uncertainties]
  Bin HIT_PRIMARY : |θ_W − θ★_0| ≤ W_hit
  Bin HIT_SIBLING : min(|θ_W − θ★_+|, |θ_W − θ★_-|) ≤ W_hit  and not HIT_PRIMARY
  Bin ELSE        : neither

Run: nice -n 19 python3 scripts/koide_wilson_holonomy_inventory.py
"""
from __future__ import annotations

import math
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ---- pre-registered targets (documentation only; no scoring without θ_W) ----
TWO_NINE = 2.0 / 9.0
SIG_THETA_MASS = 8.348e-6  # rad; T6 / P-051 pole-mass σ on δθ
HALF_MILLIDEG_RAD = 0.0005 * math.pi / 180.0  # corpus "±0.0005°" watch bar
W_HIT = 3.0 * max(SIG_THETA_MASS, HALF_MILLIDEG_RAD)

THETA_STAR = {
    "primary": TWO_NINE,
    "sibling_plus": TWO_NINE + 2.0 * math.pi / 3.0,
    "sibling_minus": TWO_NINE - 2.0 * math.pi / 3.0,
}


def check_path(rel: str) -> bool:
    return (ROOT / rel).is_file()


def main() -> int:
    print("=" * 72)
    print("KOIDE BRANCH-A WILSON HOLONOMY — INPUT INVENTORY (no free knobs)")
    print("=" * 72)
    print()
    print("PRE-REGISTERED bins (do not change after scoring begins):")
    print(f"  θ★_primary     = 2/9              = {THETA_STAR['primary']:.12f} rad")
    print(f"  θ★_sibling+    = 2/9 + 2π/3       = {THETA_STAR['sibling_plus']:.12f} rad")
    print(f"  θ★_sibling-    = 2/9 − 2π/3       = {THETA_STAR['sibling_minus']:.12f} rad")
    print(f"  σ_θ_mass       = {SIG_THETA_MASS:.6e} rad  (P-051 / T6 pole-mass)")
    print(f"  half-millideg  = {HALF_MILLIDEG_RAD:.6e} rad  (T6 2/9 ±0.0005° bar)")
    print(f"  W_hit          = 3·max(...)       = {W_HIT:.6e} rad")
    print("  Bins: HIT_PRIMARY | HIT_SIBLING | ELSE  (mutually exclusive; W << π/3)")
    print()

    # Required physical inputs for θ_W = electric holonomy of A along family cycle C.
    # Status: PRESENT / PARTIAL / MISSING. PARTIAL and MISSING both block a zero-knob run.
    requirements = []

    # (1) Gauge field / connection on the family scale
    gauge_candidates = [
        "data/dark_su2_gauge_config.npy",
        "data/wilson_Amu.npy",
        "data/family_triangle_connection.json",
        "output/dark_su2_gauge.dat",
    ]
    gauge_found = [p for p in gauge_candidates if check_path(p)]
    # also refuse to treat T14 condensate psi fields as dark SU(2) A_μ
    t14_psi_note = (
        "T14 psi_n*.npy are condensate wavefunctions for H_kin, not dark SU(2) A_μ"
    )
    if gauge_found:
        requirements.append(("dark_SU2_A_mu", "PRESENT", f"found {gauge_found}"))
    else:
        requirements.append(
            (
                "dark_SU2_A_mu",
                "MISSING",
                "no dark-SU(2) gauge-field archive in data/ or output/; "
                + t14_psi_note,
            )
        )

    # (2) Closed family-cycle path C with corpus-fixed metric/spacing
    # c₂ target 4/(3 ln 2) is phase-derived (circular for testing 2/9);
    # bare Y-junction geometry returns √3 outside modulus band — underived.
    c2_from_phase = 4.0 / (3.0 * math.log(2.0))  # circular if used as Wilson input
    c2_geometry = math.sqrt(3.0)  # Steiner/Y bare geometry
    requirements.append(
        (
            "family_cycle_path_C",
            "PARTIAL",
            f"topology equilateral asserted; bare Y-geometry c₂={c2_geometry:.5f} "
            f"≠ phase-derived c₂={c2_from_phase:.5f}; using phase-derived c₂ to test "
            f"2/9 is circular; spacing not independently fixed",
        )
    )

    # (3) Winding background fixed (n, orientation relative to triangle)
    # Canonical: n ≳ 1.65 bound only; L_gen never assigned (_CANONICAL_VALUES).
    requirements.append(
        (
            "winding_background_n",
            "MISSING",
            "n is a lower bound (n ≳ 1.65), not a determination; L_gen unassigned; "
            "Widnall n~11–25 is a different object (genesis vortex azimuthal modes), "
            "not a dark-gauge A_μ background on the family triangle",
        )
    )

    # (4) Coupling / electric projection without free dial
    # α_d ≲ 2.2 stability bound only; pure-gauge Branch A alone dies (forced combination).
    requirements.append(
        (
            "alpha_d_or_electric_projection",
            "PARTIAL",
            "α_d only bounded (≲2.2 at target spacing), not fixed; pure-gauge ring "
            "collapses (forced-combination theorem) so hybrid connection needed and "
            "not constructed; adjoint ε^abc algebra exact but not a numerical A",
        )
    )

    # (5) Existing holonomy evaluator script
    holonomy_scripts = [
        "scripts/koide_wilson_holonomy.py",
        "scripts/wilson_family_cycle.py",
        "scripts/branch_a_holonomy.py",
    ]
    found_scripts = [p for p in holonomy_scripts if check_path(p)]
    if found_scripts:
        requirements.append(("holonomy_evaluator", "PRESENT", str(found_scripts)))
    else:
        requirements.append(
            (
                "holonomy_evaluator",
                "MISSING",
                "no zero-knob Wilson-line evaluator for the family cycle exists; "
                "this inventory intentionally does not invent one",
            )
        )

    # (6) Forbidden circular inputs (must not be used as knobs)
    circular = [
        "μ_face = (2/9)·T_c  (assumes the answer)",
        "θ_hop = μ/T from KMS with μ chosen to land 2/9",
        "c₂ = 4/(3 ln 2) used as geometry input to test 2/9",
        "fit of A_μ or path to lepton masses / arg b",
    ]
    print("FORBIDDEN as inputs (circular / elastic hit 2/9):")
    for c in circular:
        print(f"  - {c}")
    print()

    print("REQUIRED INPUTS:")
    print(f"  {'name':<36} {'status':<8} note")
    print("  " + "-" * 68)
    n_ok = n_block = 0
    for name, status, note in requirements:
        print(f"  {name:<36} {status:<8} {note[:90]}")
        if len(note) > 90:
            print(f"  {'':<36} {'':<8} …{note[90:180]}")
        if status == "PRESENT":
            n_ok += 1
        else:
            n_block += 1

    print()
    print("=" * 72)
    print("VERDICT")
    print("=" * 72)
    if n_block == 0:
        print("  ALL INPUTS PRESENT — holonomy evaluation would be licensed.")
        print("  (No evaluator invoked in this inventory-only run.)")
        return 0

    print(f"  MISSING_INPUTS: {n_block} of {len(requirements)} requirements block a")
    print("  zero-free-knob Wilson holonomy. Refusing to invent gauge fields, fix n,")
    print("  pick α_d, or use phase-derived c₂. No θ_W produced. No bin scored.")
    print()
    print("  Pre-registration stands: bins and W_hit are filed for the day a")
    print("  corpus-fixed A_μ + path + winding background exist without dials.")
    print("  OPEN-THEORY / #102 phase source: UNCHANGED.")
    return 2


if __name__ == "__main__":
    # keep cwd stable for relative path checks
    os.chdir(ROOT)
    sys.exit(main())
