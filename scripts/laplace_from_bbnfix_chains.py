#!/usr/bin/env python3
"""Full Laplace evidence from bbnfix chain files (MAP + sample covariance).

Default chain dir: docs/chains (Facebook-export bundle). Also works on chains/.

  logZ ≈ -min(minuslogpost) + (d/2) ln(2π) + (1/2) ln det(Σ)

NOT nested. NOT the Δχ² proxy. See docs/working_logs/_runs/laplace_docs_chains_bbnfix_20260808/.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent.parent
SAMPLED = {
    "dyad_mnu_bbnfix": [
        "omega_b", "H0", "logA", "n_s", "z_reio", "dcdf_rho_inf", "varying_me",
        "A_planck", "A_act", "P_act", "Tcal", "Ecal", "m_ncdm",
    ],
    "cmp_lcdm_mnu_bbnfix": [
        "omega_b", "H0", "logA", "omega_cdm", "n_s", "z_reio",
        "A_planck", "A_act", "P_act", "Tcal", "Ecal", "m_ncdm",
    ],
    # DESI-DR2 twins (same sampled params as old-BAO legs)
    "dyad_mnu_bbnfix_desidr2": [
        "omega_b", "H0", "logA", "n_s", "z_reio", "dcdf_rho_inf", "varying_me",
        "A_planck", "A_act", "P_act", "Tcal", "Ecal", "m_ncdm",
    ],
    "cmp_lcdm_mnu_bbnfix_desidr2": [
        "omega_b", "H0", "logA", "omega_cdm", "n_s", "z_reio",
        "A_planck", "A_act", "P_act", "Tcal", "Ecal", "m_ncdm",
    ],
}
PAIR_OLD = ("dyad_mnu_bbnfix", "cmp_lcdm_mnu_bbnfix")
PAIR_DESI = ("dyad_mnu_bbnfix_desidr2", "cmp_lcdm_mnu_bbnfix_desidr2")
PAIR = PAIR_OLD  # default


def load_ranks(ch: Path, root: str):
    header = None
    blocks = []
    for i in (1, 2, 3):
        path = ch / f"{root}.{i}.txt"
        with path.open() as f:
            first = f.readline()
        cols = first.lstrip("#").split()
        if header is None:
            header = cols
        data = np.loadtxt(path, comments="#")
        if data.ndim == 1:
            data = data.reshape(1, -1)
        blocks.append(data)
    return header, blocks


def gate_ok(ch: Path, root: str) -> dict:
    prog = (ch / f"{root}.progress").read_text().strip().splitlines()
    last = prog[-1].split()
    r = float(last[3])
    ck = (ch / f"{root}.checkpoint").read_text()
    conv = "converged: true" in ck
    return {"Rminus1": r, "N": float(last[0]), "timestamp": last[1],
            "converged": conv, "ready": (r < 0.05 and conv)}


def laplace_one(ch: Path, root: str, ignore_rows: float) -> dict:
    header, blocks = load_ranks(ch, root)
    mlp_i = header.index("minuslogpost")
    w_i = header.index("weight")
    names = SAMPLED[root]
    idx = [header.index(n) for n in names]
    d = len(names)
    all_mlp = np.concatenate([b[:, mlp_i] for b in blocks])
    map_mlp = float(all_mlp.min())
    xs, ws = [], []
    for b in blocks:
        start = int(len(b) * ignore_rows)
        bb = b[start:]
        if len(bb) == 0:
            continue
        xs.append(bb[:, idx])
        ws.append(bb[:, w_i])
    X = np.vstack(xs)
    W = np.concatenate(ws)
    W = np.maximum(W, 0.0)
    W = W / W.sum()
    mu = (W[:, None] * X).sum(axis=0)
    xc = X - mu
    n_eff = 1.0 / float(np.sum(W ** 2))
    cov = (W[:, None] * xc).T @ xc
    cov *= n_eff / max(n_eff - 1.0, 1.0)
    evals = np.linalg.eigvalsh(cov)
    if np.any(evals <= 0):
        cov = cov + np.eye(d) * (1e-12 * max(1.0, float(np.max(np.abs(evals)))))
    sign, logdet = np.linalg.slogdet(cov)
    if sign <= 0:
        raise RuntimeError(f"{root}: cov not PD")
    logz = -map_mlp + 0.5 * d * math.log(2.0 * math.pi) + 0.5 * logdet
    evals = np.linalg.eigvalsh(cov)
    return {
        "root": root,
        "gate": gate_ok(ch, root),
        "d_sampled": d,
        "map_minuslogpost": map_mlp,
        "logdet_cov": float(logdet),
        "cov_cond": float(evals.max() / max(evals.min(), 1e-300)),
        "n_eff_weights": n_eff,
        "n_rows_postburn": int(len(X)),
        "logZ_laplace": float(logz),
        "ignore_rows": ignore_rows,
        "method": "Laplace (MAP + weighted sample covariance)",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chain-dir", type=Path, default=REPO / "docs" / "chains")
    ap.add_argument("--ignore-rows", type=float, default=0.3)
    ap.add_argument("--out-dir", type=Path, default=None)
    ap.add_argument(
        "--which",
        choices=["old", "desi"],
        default="old",
        help="old-BAO pair (default) or DESI-DR2 twins",
    )
    args = ap.parse_args()
    ch = args.chain_dir
    pair = PAIR_DESI if args.which == "desi" else PAIR_OLD
    results = {r: laplace_one(ch, r, args.ignore_rows) for r in pair}
    delta = results[pair[0]]["logZ_laplace"] - results[pair[1]]["logZ_laplace"]
    proxy = results[pair[0]]["map_minuslogpost"] - results[pair[1]]["map_minuslogpost"]
    print(f"dyad  logZ={results[pair[0]]['logZ_laplace']:.6f}  map={results[pair[0]]['map_minuslogpost']:.6f}")
    print(f"lcdm  logZ={results[pair[1]]['logZ_laplace']:.6f}  map={results[pair[1]]['map_minuslogpost']:.6f}")
    print(f"ΔlnZ_Laplace (dyad-lcdm) = {delta:+.6f}")
    print(f"Δ(min -logpost) proxy    = {proxy:+.6f}")
    for r in pair:
        print(f"  {r}: cond(Σ)={results[r]['cov_cond']:.3e} ready={results[r]['gate']['ready']}")
    if args.out_dir:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        payload = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "chain_dir": str(ch),
            "which": args.which,
            "pair": list(pair),
            "legs": results,
            "delta_lnZ_laplace_model_minus_control": delta,
            "delta_min_minuslogpost_model_minus_control": proxy,
            "not_nested": True,
        }
        out_name = "laplace_desi.json" if args.which == "desi" else "laplace.json"
        (args.out_dir / out_name).write_text(json.dumps(payload, indent=2) + "\n")
        print(f"wrote {args.out_dir / out_name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
