#!/usr/bin/env python3
"""Bekenstein quarter as heat-kernel ratio — null-hardening for QG §4a.

    1/G ~ N / (12 π ε²)     (induced Newton, scalar)
    S   ~ N A / (48 π ε²)   (entanglement, scalar)
    S / (A/G) = 12π/48π = 1/4

Species N and cutoff ε cancel. This verifies the *ratio arithmetic* and
roster structure stated in PRTOE_quantum_gravity.md §4a / PRTOE_entropy.md.

Provenance (literature coefficients — NOT a PRTOE discovery of the 1/4):
  - 12π structure (induced Newton / Sakharov class): model QG §4a cites
    Sakharov–Visser; this script does not re-derive it.
  - 48π structure (scalar entanglement / brick-wall class): candidate
    primary locators for the heat-kernel horizon entropy coefficient —
    G. 't Hooft, Nucl. Phys. B256, 727 (1985) (brick wall);
    M. Srednicki, Phys. Rev. Lett. 71, 666 (1993) (area law from vacuum
    entanglement). BIBLIOGRAPHY 't Hooft entry previously admitted the
    heat-kernel mention carried no bibliographic data — this header
    records those locators so the exhibit is not a bare "standard" claim.
  - Species cancellation of N,ε in the ratio: FFZ-class observation
    (see QG refs); arithmetic identity 12π/48π = 1/4 only.

Content boundary: this script verifies ratio arithmetic and cancellation.
  Does NOT derive Bekenstein–Hawking from first principles.
  Does NOT compute a dynamical Page curve (D9 OPEN).
"""
from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    out = Path("docs/working_logs/_runs/quantum_null_hardening_20260803")
    out.mkdir(parents=True, exist_ok=True)

    # Coefficient ratio (independent of N, ε, A)
    c_G = 12.0 * math.pi   # denominator structure for 1/G ~ N/(c_G ε²)
    c_S = 48.0 * math.pi   # S ~ N A /(c_S ε²)
    quarter = c_G / c_S
    ok = abs(quarter - 0.25) < 1e-15

    # Numerical demo with dummy N, ε, A — cancels
    N, eps, A = 48.0, 1e-3, 4.0 * math.pi * 100.0**2
    invG = N / (12.0 * math.pi * eps**2)
    S = N * A / (48.0 * math.pi * eps**2)
    ratio = S / (A * invG)
    ok2 = abs(ratio - 0.25) < 1e-12

    lines = [
        "# Area-law quarter = heat-kernel ratio (2026-08-03)\n\n",
        "## Algebra\n\n",
        "$$\\frac{1}{G} = \\frac{N}{12\\pi\\varepsilon^2},\\qquad "
        "S = \\frac{N A}{48\\pi\\varepsilon^2}"
        "\\quad\\Rightarrow\\quad "
        "\\frac{S}{A/G} = \\frac{12\\pi}{48\\pi} = \\frac{1}{4}.$$\n\n",
        f"12π/48π = **{quarter:.16f}**  "
        f"**{'PASS' if ok else 'FAIL'}**\n\n",
        f"Numerical cancel (N={N}, ε={eps}, A={A:.4g}): "
        f"S/(A/G) = **{ratio:.16f}**  "
        f"**{'PASS' if ok2 else 'FAIL'}**\n\n",
        "## What this pays / does not pay\n\n",
        "| object | status |\n|---|---|\n",
        "| Coefficient 1/4 for minimal scalars | **paid** (ratio) |\n",
        "| Species + cutoff cancellation | **paid** |\n",
        "| Roster extension (spin-½, gauge+edges, ξ=1/6 scalar) | **candidate-grade** in entropy.md §3 |\n",
        "| Dynamical Page curve S_rad(v) | **OPEN** — not this script |\n\n",
        "## Kill\n\n",
        "Rejecting edge-mode restoration for gauge fields without a replacement "
        "that preserves the ratio (per QG §4a).\n",
    ]
    path = out / "AREA_LAW_QUARTER.md"
    path.write_text("".join(lines))
    print("".join(lines))
    print("wrote", path)
    if not (ok and ok2):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
