#!/usr/bin/env python3
"""
Master PRTOE physics/math validation gate (mixed lanes — labels matter).

Runs analytic + CLASS-backed checks. Lanes:
  LEGACY_ST  — use_prtoe + xi/zeta/… (v1–v3 scalar-tensor comparison)
  CURRENT_CORE — use_dcdf + screened varying_me + dcdf_dyad_link (public expansion core)

Steps in this runner:
  1. Local gravity map (Cassini, orbit PPN, EP) — LEGACY_ST helpers / use_prtoe smoke
  2. BBN activation (rho_phi/rho_r during BBN) — LEGACY_ST scalar activation
  3. LEGACY_ST null recovery (use_prtoe ST params≈0 vs LambdaCDM) — NOT current-core null
  4. CLASS ini smoke tests (including unified dark sector where present)
  5. Unified clustering P(k) gate (unified vs split CDM+DE) — LEGACY_ST era scripts

CURRENT_CORE null/identity for publication claims: validate_dcdf.py (use_dcdf),
not scripts/test_prtoe_null_limit.py.

Usage:
  python3 scripts/run_prtoe_physics_validation.py
  python3 scripts/run_prtoe_physics_validation.py --quick   # skip slow LEGACY_ST null mPk
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _python_exe() -> str:
    """Use conda python when it has classy; else current interpreter."""
    conda = os.path.expanduser("~/miniconda3/bin/python")
    if os.path.isfile(conda):
        try:
            r = subprocess.run(
                [conda, "-c", "import classy"],
                capture_output=True,
                timeout=10,
            )
            if r.returncode == 0:
                return conda
        except (subprocess.TimeoutExpired, OSError):
            pass
    return sys.executable


def run_script(name: str, extra_args: list[str] | None = None) -> int:
    cmd = [_python_exe(), os.path.join(ROOT, "scripts", name)]
    if extra_args:
        cmd.extend(extra_args)
    print(f"\n{'='*60}\n>>> {name}\n{'='*60}")
    result = subprocess.run(cmd, cwd=ROOT)
    return result.returncode


def run_class_ini(ini: str) -> int:
    class_bin = os.path.join(ROOT, "class")
    if not os.path.isfile(class_bin):
        print(f"SKIP: {ini} (class binary not found)")
        return 0
    print(f"\n{'='*60}\n>>> ./class {ini}\n{'='*60}")
    result = subprocess.run([class_bin, ini], cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        tail = (result.stderr or result.stdout or "")[-800:]
        print(tail)
    status = "PASS" if result.returncode == 0 else "FAIL"
    print(f"[{status}] {ini} (exit {result.returncode})")
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "PRTOE physics validation suite (mixed lanes). "
            "test_prtoe_null_limit.py is LEGACY_ST only; CURRENT_CORE → validate_dcdf.py."
        )
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Skip slow full LEGACY_ST null-limit mPk (use_prtoe) test",
    )
    args = parser.parse_args()

    failures: list[str] = []
    print(
        "Lane note: steps using use_prtoe / test_prtoe_null_limit are LEGACY_ST "
        "(comparison). CURRENT_CORE public core is use_dcdf + varying_me."
    )

    checks = [
        ("test_local_gravity.py", ["--classy"]),
        ("test_bbn_activation.py", ["--classy"]),
    ]
    for script, extra in checks:
        if run_script(script, extra) != 0:
            failures.append(script)

    for ini in [
        "test_prtoe_null_publication.ini",
        "test_prtoe_bg_only.ini",
        "test_lambda_cdm.ini",
        "test_prtoe_unified_full.ini",
        "test_prtoe_ablation_unified_dm.ini",
    ]:
        if run_class_ini(ini) != 0:
            failures.append(ini)

    if not args.quick:
        # LEGACY_ST only — do not quote as CURRENT_CORE null recovery
        if run_script("test_prtoe_null_limit.py") != 0:
            failures.append("test_prtoe_null_limit.py [LEGACY_ST]")
        if run_script("test_prtoe_unified_clustering.py") != 0:
            failures.append("test_prtoe_unified_clustering.py [LEGACY_ST era]")

    print(f"\n{'='*60}")
    if failures:
        print("VALIDATION FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("ALL CHECKS IN THIS RUNNER PASSED")
    print("  (LEGACY_ST null pass ≠ CURRENT_CORE; CURRENT_CORE → validate_dcdf.py / use_dcdf)")
    return 0


if __name__ == "__main__":
    sys.exit(main())