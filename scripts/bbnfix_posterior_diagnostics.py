#!/usr/bin/env python3
"""GetDist posterior diagnostics for bbnfix pair (ESS, R-1, means).

Usage (repo root):
  python3 scripts/bbnfix_posterior_diagnostics.py --chain-dir docs/chains
  python3 scripts/bbnfix_posterior_diagnostics.py --chain-dir chains
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent.parent
PAIR = ("dyad_mnu_bbnfix", "cmp_lcdm_mnu_bbnfix")
KEY_PARAMS = {
    "dyad_mnu_bbnfix": ["H0", "m_ncdm", "omega_b", "S8", "dcdf_rho_inf", "varying_me"],
    "cmp_lcdm_mnu_bbnfix": ["H0", "m_ncdm", "omega_b", "S8", "omega_cdm"],
}


def progress_gate(ch: Path, root: str) -> dict:
    prog = (ch / f"{root}.progress").read_text().strip().splitlines()
    last = prog[-1].split()
    ck = (ch / f"{root}.checkpoint").read_text()
    return {
        "Rminus1_progress": float(last[3]),
        "N": float(last[0]),
        "timestamp": last[1],
        "converged": "converged: true" in ck,
    }


def diagnose(ch: Path, root: str, ignore_rows: float) -> dict:
    from getdist import loadMCSamples

    # loadMCSamples wants path without .1.txt suffix, files as root.1.txt
    samples = loadMCSamples(str(ch / root), settings={"ignore_rows": ignore_rows})
    names = list(samples.getParamNames().list())
    # GetDist Gelman-Rubin like
    try:
        gr = samples.getGelmanRubin()
    except Exception as e:
        gr = f"error:{e}"
    try:
        gr_eigen = samples.getGelmanRubinEigenmax()
    except Exception:
        gr_eigen = None

    want = KEY_PARAMS[root]
    stats = {}
    for p in want:
        if p not in names:
            # derived may need latex name
            found = None
            for n in names:
                if n == p or n.endswith("." + p):
                    found = n
                    break
            if found is None:
                stats[p] = {"present": False}
                continue
            p = found
        i = names.index(p) if p in names else samples.index[p]
        # mean, std, ess
        try:
            mean = float(samples.mean(p))
            std = float(samples.std(p))
        except Exception:
            mean = float(samples.mean(i))
            std = float(samples.std(i))
        try:
            ess = float(samples.getEffectiveSamplesGaussianTE(p))
        except Exception:
            try:
                ess = float(samples.getEffectiveSamples())
            except Exception:
                ess = None
        stats[p] = {"present": True, "mean": mean, "std": std, "ess_gauss_te": ess}

    # overall ESS
    try:
        ess_all = float(samples.getEffectiveSamples())
    except Exception:
        ess_all = None

    return {
        "root": root,
        "gate": progress_gate(ch, root),
        "ignore_rows": ignore_rows,
        "n_samples_after_burn": int(samples.numrows) if hasattr(samples, "numrows") else None,
        "gelman_rubin": gr if not isinstance(gr, (float, np.floating)) else float(gr),
        "gelman_rubin_eigenmax": float(gr_eigen) if gr_eigen is not None else None,
        "ess_total": ess_all,
        "params": stats,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chain-dir", type=Path, default=REPO / "docs" / "chains")
    ap.add_argument("--ignore-rows", type=float, default=0.3)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    ch = args.chain_dir
    results = {}
    print("=" * 72)
    print("bbnfix posterior diagnostics (GetDist)")
    print(f"chain_dir={ch}  ignore_rows={args.ignore_rows}")
    print("=" * 72)
    for root in PAIR:
        try:
            results[root] = diagnose(ch, root, args.ignore_rows)
        except Exception as e:
            results[root] = {"root": root, "error": str(e)}
            print(f"  {root}: ERROR {e}")
            continue
        r = results[root]
        g = r["gate"]
        print(f"\n### {root}")
        print(f"  progress R-1={g['Rminus1_progress']:.6f}  N={g['N']:.0f}  converged={g['converged']}")
        print(f"  GetDist GR={r['gelman_rubin']}  GR_eigenmax={r['gelman_rubin_eigenmax']}  ESS_total={r['ess_total']}")
        for p, s in r["params"].items():
            if not s.get("present"):
                print(f"  {p}: MISSING")
                continue
            ess = s.get("ess_gauss_te")
            ess_s = f"{ess:.1f}" if ess is not None else "n/a"
            flag = ""
            if ess is not None and ess < 200:
                flag = "  **LOW ESS**"
            print(f"  {p}: {s['mean']:.6g} ± {s['std']:.6g}  ESS~{ess_s}{flag}")

    payload = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "chain_dir": str(ch),
        "pair": list(PAIR),
        "results": results,
        "pass_hints": {
            "ESS_prefer": ">=200 (prefer >=500) on H0, m_ncdm, model params",
            "GR": "should be near progress R-1; not a second booking authority",
        },
    }
    out = args.out or (REPO / "docs/working_logs/_runs/credibility_diagnostics_20260808/posterior_diagnostics.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, default=str) + "\n")
    print(f"\nwrote {out}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
