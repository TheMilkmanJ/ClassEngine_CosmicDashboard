#!/usr/bin/env python3
"""CHSH correlator for two-mode squeezed / pair states — Tsirelson null.

Referenced by docs/exploratory/PRTOE_quantum_trio.md and
PRTOE_quantum_entanglement.md:

    B(r) = 2 * sqrt(1 + tanh(2r)^2)

Provenance (literature — NOT a PRTOE discovery):
  Z.-B. Chen, J.-W. Pan, G. Hou, Y.-D. Zhang,
  "Maximal Violation of Bell's Inequalities for Continuous Variable Systems,"
  Phys. Rev. Lett. 88, 040406 (2002); arXiv:quant-ph/0103051.
  Optimal pseudospin-CHSH on TMSV: B_max = 2√(1+K²) with K=tanh(2r).

Content boundary (Claude red CURE 2026-08-03):
  The B(r) curve is a literature property of any TMSV under the pseudospin
  CHSH operator. The model's only claim is identification of the squeezing
  parameter r with the medium's pair parameter; reaching Tsirelson is not a
  model prediction. This script is a registered-null verification harness.

Properties (Chen et al. family at optimal angles):
  - r → 0:  B → 2          (classical CHSH bound)
  - r → ∞:  B → 2√2        (Tsirelson bound)
  - B ≤ 2√2 for all r      (never superquantum)

This does NOT derive QM. It enforces the model's registered null:
"exact QM correlations; Tsirelson is a permanent kill line."

Assumptions (explicit):
  (A1) Pair state is two-mode squeezed vacuum (or equivalent Bell family
       parameterized by squeeze r).
  (A2) Optimal CHSH measurement angles for that family (Chen et al. setting).
  (A3) Substrate quantization (standard bosonic modes) — not derived here.
  (A4) No superquantum boxes (PR box etc.) — outside scope.

See also: docs/working_logs/_runs/quantum_null_hardening_20260803/CHSH_PROVENANCE.md

Run: python3 scripts/quantum_chsh_tsirelson.py
"""
from __future__ import annotations

import math
from pathlib import Path

TSIRELSON = 2.0 * math.sqrt(2.0)  # ≈ 2.828427
CLASSICAL = 2.0


def B_chsh(r: float) -> float:
    """Optimal CHSH value for two-mode squeeze parameter r ≥ 0."""
    if r < 0:
        raise ValueError("r must be ≥ 0")
    t = math.tanh(2.0 * r)
    return 2.0 * math.sqrt(1.0 + t * t)


def main() -> None:
    out = Path("docs/working_logs/_runs/quantum_null_hardening_20260803")
    out.mkdir(parents=True, exist_ok=True)

    rs = [0.0, 0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]
    rows = []
    max_B = 0.0
    for r in rs:
        B = B_chsh(r)
        max_B = max(max_B, B)
        rows.append((r, B, B / TSIRELSON, B - CLASSICAL))

    # Limits
    B0 = B_chsh(0.0)
    Binf = B_chsh(50.0)
    ok_classical = abs(B0 - CLASSICAL) < 1e-12
    ok_tsirelson = abs(Binf - TSIRELSON) < 1e-9
    ok_never_super = max_B <= TSIRELSON + 1e-12

    lines = [
        "# CHSH / Tsirelson null hardening (2026-08-03)\n\n",
        "## Formula\n\n",
        "$$B(r) = 2\\sqrt{1 + \\tanh^2(2r)}$$\n\n",
        f"Tsirelson bound $2\\sqrt{{2}}$ = **{TSIRELSON:.10f}**\n",
        f"Classical CHSH bound = **{CLASSICAL:.1f}**\n\n",
        "## Table\n\n",
        "| r | B(r) | B / Tsirelson | B − 2 |\n|---:|---:|---:|---:|\n",
    ]
    for r, B, ratio, excess in rows:
        lines.append(f"| {r:.2f} | {B:.8f} | {ratio:.6f} | {excess:+.6f} |\n")

    lines.append("\n## Limit checks\n\n")
    lines.append(f"- B(0) = {B0:.12f}  classical={CLASSICAL}  "
                 f"**{'PASS' if ok_classical else 'FAIL'}**\n")
    lines.append(f"- B(r→∞) ≈ {Binf:.12f}  Tsirelson={TSIRELSON:.12f}  "
                 f"**{'PASS' if ok_tsirelson else 'FAIL'}**\n")
    lines.append(f"- max B in table ≤ Tsirelson  "
                 f"**{'PASS' if ok_never_super else 'FAIL'}**\n")

    lines.append("\n## Grade\n\n")
    lines.append("**Null-hardened:** the registered CHSH family saturates Tsirelson "
                 "from below and never exceeds it.\n")
    lines.append("**Not derived:** why nature uses this Hilbert space / Born rule.\n")
    lines.append("**Kill:** any confirmed CHSH > 2√2 (superquantum) or a preferred-frame "
                 "leak that spoils Bell statistics at current precision.\n")

    report = out / "CHSH_TSIRELSON.md"
    report.write_text("".join(lines))
    print("".join(lines))
    print("wrote", report)
    if not (ok_classical and ok_tsirelson and ok_never_super):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
