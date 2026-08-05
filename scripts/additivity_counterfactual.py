#!/usr/bin/env python3
"""Additivity axiom instrument — what follows IF logs add vs if they don't.

NO FABRICATIONS. Does not derive the axiom. Shows algebraic consequences only.

Under shared log-additivity + equipartition in d=3:
  M_eff / M = exp(<E_kin>/T) = exp(3/2)
  exponent contribution = 3/2

Counterfactual: incomplete additivity (weight w of events that cohere):
  effective exponent = w * 3/2

Also documents independence: A_s, n_s, Koide power, hierarchy 3/2 share the axiom
(independence audit row 8) — not computed here, only cited.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path("docs/working_logs/_runs/derivation_sprint_20260803/R4b_ADDITIVITY_COUNTERFACTUAL.md")
OUT_JSON = Path("docs/working_logs/_runs/derivation_sprint_20260803/r4b_additivity.json")


def main() -> int:
    d = 3
    equip = d / 2.0  # 3/2
    rows = []
    for w in [1.0, 0.9, 0.5, 0.0]:
        exp = w * equip
        rows.append(
            {
                "additivity_weight_w": w,
                "exponent": exp,
                "M_eff_over_M": math.exp(exp),
                "note": "w=1 full shared additivity; w<1 incomplete co-addition",
            }
        )

    # residual arithmetic quoted in hierarchy (1.5014 vs 1.5) is not recomputed here
    payload = {
        "claim": "IF shared log-additivity AND NR equipartition THEN exponent = d/2",
        "axiom_derived": False,
        "equipartition_under_NR": True,
        "rows": rows,
        "correlated_riders": [
            "hierarchy -3/2",
            "A_s shot count",
            "n_s variance-linearity",
            "Koide power reading",
        ],
        "source": "PRTOE_INDEPENDENCE_AUDIT.md row 8; R4-additivity-neck",
        "page_curve_claimed": False,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2))

    lines = [
        "# R4b — Additivity counterfactual instrument\n\n",
        "**axiom_derived: false.** This script does not derive log-additivity.\n\n",
        "## IF axiom + NR equipartition\n\n",
        f"d={d} → ⟨E_kin⟩/T = d/2 = **{equip}** exactly under full additivity (w=1).\n\n",
        "| w (additivity weight) | effective exponent | M_eff/M |\n|---:|---:|---:|\n",
    ]
    for r in rows:
        lines.append(
            f"| {r['additivity_weight_w']} | {r['exponent']:.4f} | {r['M_eff_over_M']:.6f} |\n"
        )
    lines.append(
        "\n## Non-claims\n\n"
        "- Not a derivation of the axiom\n"
        "- Not a kill of A_s/n_s (only correlation under independence audit)\n"
        "- Hierarchy residual 1.5014 vs 3/2 is a separate arithmetic object\n"
    )
    OUT.write_text("".join(lines))
    print("".join(lines))
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
