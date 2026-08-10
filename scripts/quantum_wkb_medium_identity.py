#!/usr/bin/env python3
"""WKB barrier exponent vs medium evanescent decay — shared math identity.

docs/exploratory/PRTOE_quantum_tunneling.md claims the WKB factor
  exp(−∫ dx √(2m(V−E))/ℏ)
is the medium's sub-threshold (evanescent) decay, verbatim.

This script does NOT invent new physics. It records the standard identity:

  For a rectangular barrier of height V > E and width L,
    κ = √(2m(V−E)) / ℏ
    T ~ exp(−2 κ L)   (thick-barrier WKB / exact rectangular limit)

  Evanescent wave in a forbidden region (Helmholtz / phonon / EM under cutoff):
    ψ ~ exp(−κ x), same κ from the same dispersion when V−E is the gap.

Provenance (textbook — NOT a PRTOE discovery):
  WKB / Gamow factor: standard quantum mechanics (e.g. Landau & Lifshitz QM;
  Messiah; any graduate QM barrier chapter). Rectangular exact limit T~exp(−2κL).
  Content boundary: shared-math identity between WKB and linear-wave evanescent
  decay under isomorphic dispersion. Does NOT derive ℏ or Born rule.

Assumptions:
  (A1) Non-relativistic Schrödinger or isomorphic linear wave equation.
  (A2) Slowly varying / rectangular barrier (standard WKB regime).
  (A3) "Medium" language maps κ to the same algebraic expression —
       this is an *identification of formulas*, not a derivation of ℏ.

Run: python3 scripts/quantum_wkb_medium_identity.py
"""
from __future__ import annotations

import math
from pathlib import Path

# Natural units for a numerical demo: ħ = 1, m = 1
HBAR = 1.0
MASS = 1.0


def kappa(V: float, E: float, m: float = MASS, hbar: float = HBAR) -> float:
    if V <= E:
        raise ValueError("need V > E for forbidden region")
    return math.sqrt(2.0 * m * (V - E)) / hbar


def wkb_log_T_thick(V: float, E: float, L: float) -> float:
    """log transmission ~ −2 κ L (leading exponential)."""
    return -2.0 * kappa(V, E) * L


def medium_log_amp(V: float, E: float, x: float) -> float:
    """log |ψ| for evanescent profile exp(−κ x)."""
    return -kappa(V, E) * x


def main() -> None:
    out = Path("docs/working_logs/_runs/quantum_null_hardening_20260803")
    out.mkdir(parents=True, exist_ok=True)

    cases = [
        # V, E, L
        (2.0, 1.0, 1.0),
        (4.0, 1.0, 0.5),
        (10.0, 1.0, 0.2),
        (2.0, 0.5, 2.0),
    ]

    lines = [
        "# WKB ↔ medium evanescent identity (2026-08-03)\n\n",
        "## Algebra\n\n",
        "$$\\kappa = \\frac{\\sqrt{2m(V-E)}}{\\hbar}$$\n\n",
        "Thick barrier: $\\ln T \\sim -2\\kappa L$.  "
        "Evanescent amplitude: $\\ln|\\psi(x)| = -\\kappa x$.\n\n",
        "At $x = L$, $2\\,|\\ln|\\psi|| = |\\ln T|$ (same $\\kappa$).\n\n",
        "## Numerical checks (ħ=m=1)\n\n",
        "| V | E | L | κ | −2κL (WKB) | −κL (medium@L) | 2×medium = WKB? |\n",
        "|---:|---:|---:|---:|---:|---:|---|\n",
    ]

    all_ok = True
    for V, E, L in cases:
        k = kappa(V, E)
        wkb = wkb_log_T_thick(V, E, L)
        med = medium_log_amp(V, E, L)
        match = abs(2.0 * med - wkb) < 1e-12
        all_ok = all_ok and match
        lines.append(
            f"| {V} | {E} | {L} | {k:.6f} | {wkb:.6f} | {med:.6f} | "
            f"{'PASS' if match else 'FAIL'} |\n"
        )

    lines.append("\n## Grade\n\n")
    lines.append("**Shared-math hardened:** WKB thick-barrier exponent is "
                 "identically twice the medium decay over the same interval.\n")
    lines.append("**Josephson / macroscopic tunneling:** same *class* of sub-threshold "
                 "phase dynamics; SI-volt calibration is a precision *receipt*, not a "
                 "cosmological proof.\n")
    lines.append("**Not derived:** microscopic origin of ℏ or the particle spectrum.\n")
    lines.append("**Kill:** confirmed tunneling rates outside standard QM (or preferred-frame "
                 "imprint on tunneling times if ever established).\n")

    path = out / "WKB_MEDIUM_IDENTITY.md"
    path.write_text("".join(lines))
    print("".join(lines))
    print("wrote", path)
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
