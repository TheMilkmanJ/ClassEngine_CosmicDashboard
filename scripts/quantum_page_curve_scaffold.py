#!/usr/bin/env python3
"""Page-curve dynamics scaffold — design + minimal 0D bookkeeping (NOT a result).

PRTOE_information_paradox.md: coefficient paid; curve un-run.
This script:
  1) States the registered dynamical object
  2) Implements a *toy* burnt-diary / Page-like S_rad(v) shape for unit tests
  3) Refuses to claim PRTOE prediction — toy only

Real work still owed: phonon Hawking flux off a finite sonic-horizon core
with healing-length cutoff (analog gravity), not this 0D cartoon.
"""
from __future__ import annotations

import math
from pathlib import Path


def toy_page_S_rad(v: float, S_BH: float = 1.0) -> float:
    """Toy Page-like radiation entropy vs evaporated fraction v ∈ [0,1].

    Early thermal rise ~ v, late purification fall ~ (1-v); continuous.
    NOT derived from condensate microphysics.
    """
    if v < 0 or v > 1:
        raise ValueError("v in [0,1]")
    # Smooth Page-like: peaks near v=0.5 at S_BH/2 for the simple ansatz
    # S = S_BH * 4 v (1-v)  → max  S_BH at v=0.5? 4*0.25=1 → max S_BH
    # Standard cartoon: peak S_BH/2 at Page time ~ half evaporation for old holes
    return S_BH * 4.0 * v * (1.0 - v) * 0.5  # max = S_BH/2 at v=0.5


def main() -> None:
    out = Path("docs/working_logs/_runs/quantum_null_hardening_20260803")
    out.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Page-curve dynamics — scaffold (2026-08-03)\n\n",
        "## Registered object (still OPEN)\n\n",
        "Compute $S_{\\mathrm{rad}}(v)$ vs Page time for **phonon Hawking flux** "
        "off a **finite-density sonic-horizon core** (healing length $\\xi$), "
        "with unitarity enforced by the core as a finite quantum system.\n\n",
        "Blocked on: nothing in the coefficient/roster layer "
        "(those are paid). Blocked on: **doing the dynamics**.\n\n",
        "## Design requirements (pre-registered)\n\n",
        "1. Horizon = sonic (analog), not fundamental causal knife.\n",
        "2. Core = single quantum system of size $\\sim\\xi$ (no shredder).\n",
        "3. Early radiation ≈ thermal; late radiation purifies (Page turn).\n",
        "4. Kill if: no Page turn under unitary core evolution; or firewall "
        "required against sonic-horizon leakage.\n",
        "5. Forbidden: drawing a Page curve from $S=A/4G$ alone without dynamics.\n\n",
        "## Toy bookkeeping (NOT a PRTOE result)\n\n",
        "Ansatz $S_{\\mathrm{rad}}(v) = \\tfrac12 S_{\\mathrm{BH}}\\cdot 4v(1-v)$ "
        "peaks at $S_{\\mathrm{BH}}/2$ when $v=1/2$.\n\n",
        "| v | S_rad / S_BH |\n|---:|---:|\n",
    ]
    for v in [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]:
        lines.append(f"| {v:.2f} | {toy_page_S_rad(v):.4f} |\n")

    lines.append("\n## Status\n\n")
    lines.append("| item | grade |\n|---|---|\n")
    lines.append("| Coefficient 1/4 | paid (area_law script) |\n")
    lines.append("| Roster extension | candidate-grade (entropy.md) |\n")
    lines.append("| Toy Page shape | **illustration only** |\n")
    lines.append("| Condensate Page curve | **OPEN — not run** |\n")

    path = out / "PAGE_CURVE_SCAFFOLD.md"
    path.write_text("".join(lines))
    print("".join(lines))
    print("wrote", path)
    # sanity: peak at 0.5
    assert abs(toy_page_S_rad(0.5) - 0.5) < 1e-12
    assert toy_page_S_rad(0.0) == 0.0 and toy_page_S_rad(1.0) == 0.0


if __name__ == "__main__":
    main()
