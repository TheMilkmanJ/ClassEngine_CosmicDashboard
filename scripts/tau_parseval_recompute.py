#!/usr/bin/env python3
"""Permanent recompute: τ = ½ln2 from Q=2/3 via Parseval (R3-tau-lock).

NO FABRICATIONS. Does not derive Q=2/3 or the e^(-τ) thermal-weight identification.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path("docs/working_logs/_runs/derivation_sprint_20260803/R3_TAU_RECOMPUTE.json")
ME = 0.51099895e6  # eV


def tau_from_Q(Q: float) -> dict:
    rho2 = (Q - 1.0 / 3.0) / (2.0 / 3.0)
    if rho2 <= 0:
        raise ValueError(f"invalid Q={Q}")
    rho = math.sqrt(rho2)
    tau = -math.log(rho)
    return {
        "Q": Q,
        "rho": rho,
        "rho2": rho2,
        "tau": tau,
        "half_ln2": 0.5 * math.log(2.0),
        "tau_minus_half_ln2": tau - 0.5 * math.log(2.0),
        "T_c_keV": tau * ME / 1e3,
    }


def main() -> int:
    exact = tau_from_Q(2.0 / 3.0)
    measured = tau_from_Q(0.6666605)
    assert abs(exact["tau_minus_half_ln2"]) < 1e-12
    out = {
        "identity": "Parseval Q=1/3+(2/3)rho^2; tau=-ln rho",
        "exact_Q_2_3": exact,
        "measured_Q": measured,
        "conditions_R3": [
            "measured Q=2/3",
            "sqrt(sigma_dark)=m_e pin",
            "e^(-tau) thermal-weight reading of kernel modulus",
        ],
        "thermal_delivery_used": False,
        "locking_without_Q": "OPEN",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))
    print("PASS exact tau=1/2 ln2 at Q=2/3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
