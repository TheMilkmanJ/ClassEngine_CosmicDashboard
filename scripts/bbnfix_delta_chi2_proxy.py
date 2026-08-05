#!/usr/bin/env python3
"""bbnfix_delta_chi2_proxy — gate-hard min−logpost Δ proxy (NOT full Laplace).

Checklist Step C.1 (`docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`):
  Report Δ(min −logpost) between dyad_mnu_bbnfix and cmp_lcdm_mnu_bbnfix only
  after both chains have R−1 < 0.05 AND converged: true (self-stop).

This is a **proxy**, not bookable Laplace ΔlnZ:
  - missing Hessian volume / prior measure
  - equal-prior comparisons only; label method explicitly

Hard refuse if gate fails (exit 2). No PolyChord. No MCMC surgery.

Usage (repo root):
  python3 scripts/bbnfix_delta_chi2_proxy.py
  python3 scripts/bbnfix_delta_chi2_proxy.py --force-peek   # prints but marks UNBOOKABLE
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent.parent
CH = REPO / "chains"
PAIR = ("dyad_mnu_bbnfix", "cmp_lcdm_mnu_bbnfix")  # model, control
RBAR = 0.05


def last_rminus1(name: str) -> float | None:
    p = CH / f"{name}.progress"
    if not p.is_file():
        return None
    lines = p.read_text().strip().splitlines()
    if not lines:
        return None
    parts = lines[-1].split()
    if len(parts) < 4:
        return None
    return float(parts[3])


def checkpoint_converged(name: str) -> bool | None:
    p = CH / f"{name}.checkpoint"
    if not p.is_file():
        return None
    text = p.read_text()
    if "converged: true" in text:
        return True
    if "converged: false" in text:
        return False
    return None


def min_minuslogpost(name: str) -> dict:
    """Cobaya chain col 1 is minuslogpost (after weight col 0)."""
    best = None
    per_rank = {}
    for i in (1, 2, 3):
        path = CH / f"{name}.{i}.txt"
        if not path.is_file():
            per_rank[i] = None
            continue
        # skip header line starting with #
        d = np.loadtxt(path, comments="#")
        if d.ndim == 1:
            d = d.reshape(1, -1)
        m = float(d[:, 1].min())
        per_rank[i] = m
        best = m if best is None else min(best, m)
    return {"root": name, "min_minuslogpost": best, "per_rank": per_rank}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--force-peek",
        action="store_true",
        help="compute even if gate fails; mark UNBOOKABLE (default: refuse)",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="optional JSON write path under docs/working_logs/_runs/",
    )
    args = ap.parse_args()

    print("=" * 72)
    print("bbnfix Δ(min −logpost) proxy — NOT full Laplace")
    print("=" * 72)

    gate = {}
    ok = True
    for name in PAIR:
        r = last_rminus1(name)
        c = checkpoint_converged(name)
        gate[name] = {"Rminus1": r, "converged": c}
        r_ok = r is not None and r < RBAR
        c_ok = c is True
        print(
            f"  {name}: R−1={r}  converged={c}  "
            f"({'OK' if r_ok and c_ok else 'NOT READY'})"
        )
        if not (r_ok and c_ok):
            ok = False

    if not ok and not args.force_peek:
        print("\n  REFUSED — need both R−1 < 0.05 AND converged:true on both chains.")
        print("  This proxy is not bookable as Laplace ΔlnZ. No PolyChord.")
        print("=" * 72)
        return 2

    if not ok and args.force_peek:
        print("\n  WARNING: --force-peek with gate open → UNBOOKABLE numbers only.")

    rows = {name: min_minuslogpost(name) for name in PAIR}
    for name, row in rows.items():
        print(f"  {name}: min_minuslogpost = {row['min_minuslogpost']}  ranks={row['per_rank']}")

    m_model = rows[PAIR[0]]["min_minuslogpost"]
    m_ctrl = rows[PAIR[1]]["min_minuslogpost"]
    if m_model is None or m_ctrl is None:
        print("  ERROR: missing chain ranks for min −logpost.")
        return 2

    # lower minuslogpost = better fit; Δ = model − control (negative favors model)
    delta = float(m_model - m_ctrl)
    print(f"\n  Δ(min −logpost) = model − control = {delta:+.6f}")
    print("  Caveat: NOT full Laplace (no Hessian volume / prior measure).")
    print("  Prefer CosmicForge Hessian Laplace for bookable ΔlnZ after gate.")
    print("  Do NOT substitute pre-bbnfix ΔlnZ ≈ +2.6.")

    payload = {
        "tool": "scripts/bbnfix_delta_chi2_proxy.py",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "gate_ok": ok,
        "bookable_as_laplace": False,
        "method": "min_minuslogpost_proxy_only",
        "pair": list(PAIR),
        "gate": gate,
        "min_minuslogpost": {n: rows[n]["min_minuslogpost"] for n in PAIR},
        "delta_min_minuslogpost_model_minus_control": delta,
        "caveats": [
            "Not full Laplace evidence",
            "Missing Hessian volume and prior measure",
            "BBN-fixed stack only when gate_ok",
            "No PolyChord",
        ],
        "page_curve_claimed": False,
    }
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(payload, indent=2) + "\n")
        print(f"  wrote {args.out}")
    print("=" * 72)
    return 0 if ok else 3  # 3 = peeked under open gate


if __name__ == "__main__":
    raise SystemExit(main())
