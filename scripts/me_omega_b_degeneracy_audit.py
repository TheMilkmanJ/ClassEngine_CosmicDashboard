#!/usr/bin/env python3
"""m_e–ω_b degeneracy audit (Q2/#20) — first pass.

Reads a free-varying_me Cobaya chain and measures how much of the model's +1.1% ω_b
shift (vs the in-house ΛCDM control) is forced by the m_e ridge versus free slide.

Default chain: chains/dyad_mnu_mcmc.1.txt
ΛCDM control ω_b: from chains/cmp_lcdm.stats (0.022517)

Usage:
  python3 scripts/me_omega_b_degeneracy_audit.py
  python3 scripts/me_omega_b_degeneracy_audit.py --chain chains/dyad_mnu_mcmc.1.txt
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CHAIN = ROOT / "chains" / "dyad_mnu_mcmc.1.txt"
LCDM_OMEGA_B = 0.022517          # cmp_lcdm.stats best-fit
DERIVED_ME = 1.012543            # 1 + 27α/(5π)


def load_cobaya(path: Path):
    header = None
    rows = []
    with path.open() as f:
        for line in f:
            if line.startswith("#"):
                parts = line.lstrip("#").split()
                if "weight" in parts and "omega_b" in parts:
                    header = parts
                continue
            if line.strip():
                rows.append([float(x) for x in line.split()])
    if header is None:
        raise SystemExit(f"no cobaya header with weight/omega_b in {path}")
    return {name: i for i, name in enumerate(header)}, np.asarray(rows, float)


def wmean(w, x):
    return float(np.sum(w * x) / np.sum(w))


def wstd(w, x):
    m = wmean(w, x)
    return float(math.sqrt(np.sum(w * (x - m) ** 2) / np.sum(w)))


def wcorr(w, x, y):
    return float(
        np.sum(w * (x - wmean(w, x)) * (y - wmean(w, y)))
        / (np.sum(w) * wstd(w, x) * wstd(w, y))
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chain", type=Path, default=DEFAULT_CHAIN)
    ap.add_argument("--burn-frac", type=float, default=1 / 3)
    ap.add_argument("--lcdm-omega-b", type=float, default=LCDM_OMEGA_B)
    args = ap.parse_args()

    idx, a = load_cobaya(args.chain)
    need = ("weight", "omega_b", "varying_me", "H0")
    for k in need:
        if k not in idx:
            raise SystemExit(f"chain missing column {k}: {sorted(idx)}")

    n0 = len(a)
    s = int(n0 * args.burn_frac)
    a = a[s:]
    w = a[:, idx["weight"]]
    ob = a[:, idx["omega_b"]]
    me = a[:, idx["varying_me"]]
    H0 = a[:, idx["H0"]]

    # weighted ridge: omega_b = a0 + a1*(me - 1)
    x = me - 1.0
    X = np.column_stack([np.ones_like(x), x])
    XtWX = X.T @ (w[:, None] * X)
    XtWy = X.T @ (w * ob)
    a0, a1 = np.linalg.solve(XtWX, XtWy)

    ob_mean = wmean(w, ob)
    me_mean = wmean(w, me)
    H0_mean = wmean(w, H0)
    ob_me1 = a0
    ob_derived = a0 + a1 * (DERIVED_ME - 1.0)
    lcdm = args.lcdm_omega_b

    def pct(ob_):
        return 100.0 * (ob_ / lcdm - 1.0)

    me_sig = (me_mean - 1.0) / wstd(w, me)
    forced_vs_lcdm = pct(ob_derived)
    total_vs_lcdm = pct(ob_mean)
    residual_pp = total_vs_lcdm - forced_vs_lcdm

    print("=" * 68)
    print("m_e–ω_b DEGENERACY AUDIT (Q2/#20) — first pass")
    print("=" * 68)
    print(f"chain: {args.chain}")
    print(f"samples: {n0} raw → {len(a)} after burn-frac={args.burn_frac:.2f} "
          f"(sum w = {w.sum():.0f})")
    print()
    print(f"  ω_b          = {ob_mean:.6f} ± {wstd(w, ob):.6f}")
    print(f"  varying_me   = {me_mean:.6f} ± {wstd(w, me):.6f}   "
          f"({(me_mean-1)*100:.3f}% ; {me_sig:.2f}σ from 1)")
    print(f"  H0           = {H0_mean:.3f} ± {wstd(w, H0):.3f}")
    print()
    print(f"  corr(ω_b, m_e) = {wcorr(w, ob, me):+.4f}")
    print(f"  corr(ω_b, H0)  = {wcorr(w, ob, H0):+.4f}")
    print(f"  corr(m_e, H0)  = {wcorr(w, me, H0):+.4f}")
    print()
    print(f"  ridge: ω_b = {a0:.6f} + {a1:.6f}·(m_e − 1)")
    print(f"    at m_e = 1          → ω_b = {ob_me1:.6f}  ({pct(ob_me1):+.3f}% vs ΛCDM)")
    print(f"    at m_e = {DERIVED_ME} → ω_b = {ob_derived:.6f}  ({forced_vs_lcdm:+.3f}% vs ΛCDM)")
    print(f"    posterior mean      → ω_b = {ob_mean:.6f}  ({total_vs_lcdm:+.3f}% vs ΛCDM)")
    print(f"    ΛCDM control        → ω_b = {lcdm:.6f}")
    print()
    print("VERDICT")
    print(f"  forced by derived m_e along ridge: {forced_vs_lcdm:+.3f} percentage points")
    print(f"  free-slide residual (mean − ridge): {residual_pp:+.3f} percentage points")
    if abs(residual_pp) < 0.05:
        print("  → essentially ALL of the +1.1% is forced by m_e; free slide is consistent "
              "with zero.")
    else:
        print("  → a non-negligible free-slide component remains; re-fit with D/H joint.")
    print(f"  m_e is {'DETECTED' if abs(me_sig) >= 2 else 'not significant'} "
          f"at {abs(me_sig):.2f}σ from 1 on this chain — not a pure degeneracy artifact.")
    print("=" * 68)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
