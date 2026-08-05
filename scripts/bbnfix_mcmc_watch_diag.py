#!/usr/bin/env python3
"""bbnfix MCMC watch diagnostic — UNBOOKABLE.

Reports:
  - cobaya progress R−1 + checkpoint Rminus1_last + converged
  - chain file lengths / mtimes (growth)
  - optional crude multi-chain R−1 on raw params (not cobaya's measure)

Does NOT book H0/posteriors. Gate remains book_bbnfix_when_ready.py.
"""
from __future__ import annotations

import time
from datetime import datetime
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent.parent
CH = REPO / "chains"
PAIR = ("dyad_mnu_bbnfix", "cmp_lcdm_mnu_bbnfix")


def last_progress(name: str):
    p = CH / f"{name}.progress"
    if not p.is_file():
        return None
    lines = [ln for ln in p.read_text().splitlines() if ln.strip() and not ln.startswith("#")]
    if not lines:
        return None
    parts = lines[-1].split()
    return {
        "N": float(parts[0]),
        "t": parts[1] if len(parts) > 1 else "?",
        "Rminus1": float(parts[3]),
        "mtime": datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec="seconds"),
    }


def checkpoint(name: str):
    p = CH / f"{name}.checkpoint"
    if not p.is_file():
        return None
    text = p.read_text()
    conv = True if "converged: true" in text else (False if "converged: false" in text else None)
    rlast = None
    for line in text.splitlines():
        if line.strip().startswith("Rminus1_last:"):
            try:
                rlast = float(line.split(":", 1)[1].strip())
            except ValueError:
                pass
    return {
        "converged": conv,
        "Rminus1_last": rlast,
        "mtime": datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec="seconds"),
    }


def chain_growth(name: str):
    out = []
    for i in (1, 2, 3):
        f = CH / f"{name}.{i}.txt"
        if not f.is_file():
            continue
        n = sum(1 for ln in f.open() if ln.strip() and not ln.startswith("#"))
        out.append(
            {
                "rank": i,
                "rows": n,
                "mtime": datetime.fromtimestamp(f.stat().st_mtime).isoformat(timespec="seconds"),
                "bytes": f.stat().st_size,
            }
        )
    return out


def crude_r1(name: str, burn_frac: float = 0.5) -> float | None:
    mats = []
    for i in (1, 2, 3):
        f = CH / f"{name}.{i}.txt"
        if not f.is_file():
            return None
        rows = []
        for ln in f.open():
            if not ln.strip() or ln.startswith("#"):
                continue
            rows.append([float(x) for x in ln.split()])
        a = np.asarray(rows)
        s = int(len(a) * burn_frac)
        mats.append(a[s:, 2:])  # skip weight, minuslogpost
    m = min(len(x) for x in mats)
    X = np.stack([x[-m:] for x in mats], axis=0)  # R,N,P
    R, N, P = X.shape
    mean_i = X.mean(axis=1)
    mean = mean_i.mean(axis=0)
    B = N * ((mean_i - mean) ** 2).sum(axis=0) / max(R - 1, 1)
    W = ((X - mean_i[:, None, :]) ** 2).sum(axis=(0, 1)) / max(R * (N - 1), 1)
    var = (N - 1) / N * W + B / N
    rhat = np.sqrt(var / np.maximum(W, 1e-300))
    return float(rhat.max() - 1.0)


def main() -> int:
    print("=" * 72)
    print("bbnfix MCMC watch diagnostic — UNBOOKABLE")
    print(f"stamp: {datetime.now().isoformat(timespec='seconds')}")
    print("gate authority: progress R−1 < 0.05 AND checkpoint converged:true")
    print("=" * 72)
    for name in PAIR:
        print(f"\n--- {name} ---")
        pr = last_progress(name)
        ck = checkpoint(name)
        gr = chain_growth(name)
        if pr:
            print(
                f"  progress: N={pr['N']:.0f} R−1={pr['Rminus1']:.6f} t={pr['t']} "
                f"(file mtime {pr['mtime']})"
            )
        else:
            print("  progress: MISSING")
        if ck:
            print(
                f"  checkpoint: converged={ck['converged']} "
                f"Rminus1_last={ck['Rminus1_last']} (mtime {ck['mtime']})"
            )
        else:
            print("  checkpoint: MISSING")
        if gr:
            rows = [g["rows"] for g in gr]
            print(
                f"  chains: ranks={len(gr)} rows={rows} "
                f"latest_mtime={max(g['mtime'] for g in gr)}"
            )
        try:
            r1 = crude_r1(name)
            if r1 is not None:
                print(
                    f"  crude param R−1 (burn 50%, max over params): {r1:.4f} "
                    f"— NOT cobaya measure; NOT bookable"
                )
        except Exception as e:
            print(f"  crude R−1 failed: {type(e).__name__}: {e}")
        try:
            from getdist import loadMCSamples

            s = loadMCSamples(str(CH / name), settings={"ignore_rows": 0.3})
            g = float(s.getGelmanRubin())
            print(
                f"  GetDist max GR (ignore_rows=0.3): {g:.6f} "
                f"— diagnostic only; booking still needs cobaya self-stop"
            )
        except Exception as e:
            print(f"  GetDist GR failed: {type(e).__name__}: {e}")
        ready_prog = bool(pr and pr["Rminus1"] < 0.05)
        ready_stop = bool(ck and ck["converged"] is True)
        print(f"  bookable_leg: {ready_prog and ready_stop} (R−1_ok={ready_prog}, stop_ok={ready_stop})")
    print("\n" + "=" * 72)
    print("REFUSE booking from this script. Use: python3 scripts/book_bbnfix_when_ready.py")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
