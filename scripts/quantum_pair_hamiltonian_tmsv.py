#!/usr/bin/env python3
"""Pair Hamiltonian → TMSV squeeze r → CHSH B(r) harness.

Resource: single-thread. No PolyChord. No inventing medium microphysics.

What this DOES:
  - Standard two-mode quadratic pair Hamiltonian
      H = ω (a†a + b†b) + λ (ab + a†b†)
    (textbook generator of two-mode squeezing)
  - Diagonalize / use closed form: effective squeeze r = artanh(λ/ω) for |λ|<ω
    (equivalently integrate Heisenberg eqs; here closed form)
  - Map r → B_max = 2√(1+tanh²(2r))  [same literature family as quantum_chsh_tsirelson.py]
  - Scan λ/ω and write a table

What this does NOT do:
  - Derive ω, λ from PRTOE medium numbers  → medium r remains MISSING_INPUT
  - Claim CHSH discovery
  - Close EN-D2/D3 as paid medium derivation

Usage:
  OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_pair_hamiltonian_tmsv.py
"""
from __future__ import annotations

import json
import math
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

OUT_DIR = Path("docs/working_logs/_runs/quantum_arxiv_worklist_20260803")
OUT_JSON = OUT_DIR / "pair_hamiltonian_tmsv.json"
OUT_MD = OUT_DIR / "PAIR_HAMILTONIAN_TMSV.md"


def r_from_lambda_over_omega(x: float) -> float:
    """For H = ω(n_a+n_b) + λ(ab+h.c.), |x|=|λ/ω|<1, stationary squeeze r = artanh(x).
    (Standard parametric amplifier / two-mode squeezing map.)
    """
    x = float(np.clip(x, -0.999999, 0.999999))
    return float(0.5 * math.log((1 + abs(x)) / (1 - abs(x))))  # artanh(|x|)


def B_of_r(r: float) -> float:
    """Literature TMSV pseudospin CHSH max (Chen et al.)."""
    K = math.tanh(2.0 * r)
    return 2.0 * math.sqrt(1.0 + K * K)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    omega = 1.0
    xs = np.linspace(0.0, 0.95, 20)
    rows = []
    for x in xs:
        r = r_from_lambda_over_omega(x)
        B = B_of_r(r)
        rows.append(
            {
                "lambda_over_omega": float(x),
                "r": r,
                "B_max": B,
                "tsirelson": 2 * math.sqrt(2),
                "below_tsirelson": B <= 2 * math.sqrt(2) + 1e-12,
            }
        )

    all_below = all(r["below_tsirelson"] for r in rows)
    # medium pin: NOT derived
    medium_r_derived = False
    medium_lambda_omega_derived = False

    payload = {
        "hamiltonian": "H = ω(a†a+b†b) + λ(ab+a†b†)",
        "hamiltonian_class": "standard_textbook_pair_quadratic",
        "medium_omega_derived": False,
        "medium_lambda_derived": False,
        "medium_r_derived": medium_r_derived,
        "EN_D2_D3_status": "MISSING_INPUT — H is literature form; medium (ω,λ) not pinned",
        "all_B_below_tsirelson": all_below,
        "rows": rows,
        "non_claims": [
            "not a PRTOE discovery of CHSH",
            "not a derivation of medium r",
            "does not close atomic QM",
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2))

    md = f"""# Pair Hamiltonian → TMSV → CHSH harness

**Script:** `scripts/quantum_pair_hamiltonian_tmsv.py`  
**JSON:** `pair_hamiltonian_tmsv.json`

## Hamiltonian (textbook)

\\[
H = \\omega(a^\\dagger a + b^\\dagger b) + \\lambda(ab + a^\\dagger b^\\dagger)
\\]

Closed map \\(|\\lambda/\\omega|<1 \\Rightarrow r = \\mathrm{{artanh}}(|\\lambda/\\omega|)\\), then
literature \\(B_{{\\max}}(r)=2\\sqrt{{1+\\tanh^2(2r)}}\\).

## Result

| check | status |
|---|---|
| All B ≤ Tsirelson in scan | {"PASS" if all_below else "FAIL"} |
| Medium ω derived | **NO** |
| Medium λ derived | **NO** |
| Medium r derived | **NO** |
| EN-D2/D3 | still **MISSING_INPUT** |

## What would pay medium r

A corpus-licensed derivation of \\((\\omega,\\lambda)\\) or of \\(r\\) from medium numbers
(gap, density, stiffness, …) **without free dials**. That object is **not on disk**.

## Non-claims

Not CHSH discovery; not atomic QM; not Born.

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_pair_hamiltonian_tmsv.py
```
"""
    OUT_MD.write_text(md)
    print("PAIR H → TMSV harness")
    print(f"  rows={len(rows)} all_below_tsirelson={all_below}")
    print(f"  medium_r_derived={medium_r_derived} EN-D2/D3 still MISSING_INPUT")
    print(f"  wrote {OUT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
