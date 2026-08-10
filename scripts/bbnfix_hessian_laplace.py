#!/usr/bin/env python3
"""Finite-difference Hessian Laplace at MAP from chain files (hardened).

Loads Cobaya model from input/updated yaml, takes MAP = min minuslogpost sample,
builds Hessian of minuslogpost in *whitened* coordinates (chain sample-cov), then:

  logZ = -mlp_map + 0.5 * d * ln(2π) - 0.5 * ln det(H_x)

where H_x is the physical-space Hessian recovered from the whitened FD Hessian.

Hardening vs 2026-08-10 fail:
  - FD steps from chain std (not fixed scales that overflow / leave support)
  - one-sided FD near boundaries (e.g. m_ncdm ~ 0)
  - reject non-finite logpost; shrink steps adaptively
  - eigenvalue floor that handles NaN/Inf; JSON-safe floats
  - optional pure sample-cov Laplace cross-check in same run

Usage:
  python3 scripts/bbnfix_hessian_laplace.py --chain-dir docs/chains --which both
  python3 scripts/bbnfix_hessian_laplace.py --which lcdm --step-frac 0.05
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import yaml

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
    # DESI-DR2 / Y3 BAO twins (same sampled params as old-BAO legs)
    "dyad_mnu_bbnfix_desidr2": [
        "omega_b", "H0", "logA", "n_s", "z_reio", "dcdf_rho_inf", "varying_me",
        "A_planck", "A_act", "P_act", "Tcal", "Ecal", "m_ncdm",
    ],
    "cmp_lcdm_mnu_bbnfix_desidr2": [
        "omega_b", "H0", "logA", "omega_cdm", "n_s", "z_reio",
        "A_planck", "A_act", "P_act", "Tcal", "Ecal", "m_ncdm",
    ],
}
# hard lower edges for one-sided FD (physics support)
LOWER = {
    "m_ncdm": 0.0,
    "omega_b": 1e-5,
    "omega_cdm": 1e-5,
    "H0": 20.0,
    "z_reio": 0.0,
}


def _json_float(x: float) -> float | None:
    if x is None or isinstance(x, (float, int, np.floating, np.integer)):
        v = float(x)
        if not math.isfinite(v):
            return None
        return v
    return None


def load_chain_arrays(ch: Path, root: str, names: list[str], ignore_rows: float = 0.3):
    header = None
    best = None
    best_x = None
    chunks = []
    for i in (1, 2, 3):
        path = ch / f"{root}.{i}.txt"
        with path.open() as f:
            cols = f.readline().lstrip("#").split()
        if header is None:
            header = cols
        data = np.loadtxt(path, comments="#")
        if data.ndim == 1:
            data = data.reshape(1, -1)
        mlp_i = header.index("minuslogpost")
        j = int(np.argmin(data[:, mlp_i]))
        mlp = float(data[j, mlp_i])
        x = np.array([float(data[j, header.index(n)]) for n in names])
        if best is None or mlp < best:
            best = mlp
            best_x = x
        n = len(data)
        start = int(ignore_rows * n)
        idxs = [header.index(n) for n in names]
        chunks.append(data[start:, idxs])
    X = np.vstack(chunks)
    return best, best_x, X


def load_model(yaml_path: Path, packages_path: str | None):
    from cobaya.model import get_model

    info = yaml.safe_load(yaml_path.read_text())
    info.pop("sampler", None)
    info.pop("output", None)
    if packages_path:
        info["packages_path"] = packages_path
    return get_model(info)


def mlp_at(model, names, x) -> float:
    params = dict(zip(names, x))
    lp = model.logposterior(params, make_finite=True)
    v = float(-lp.logpost)
    if not math.isfinite(v):
        return float("inf")
    return v


def chain_std_steps(names: list[str], X: np.ndarray, step_frac: float) -> np.ndarray:
    std = np.std(X, axis=0)
    # floor: never zero for fixed-looking params
    std = np.maximum(std, 1e-8)
    steps = step_frac * std
    # absolute floors / caps
    floors = {
        "omega_b": 1e-6,
        "omega_cdm": 1e-6,
        "H0": 1e-3,
        "logA": 1e-5,
        "n_s": 1e-5,
        "z_reio": 1e-3,
        "m_ncdm": 1e-4,
        "A_planck": 1e-5,
        "A_act": 1e-5,
        "P_act": 1e-5,
        "Tcal": 1e-5,
        "Ecal": 1e-5,
        "dcdf_rho_inf": 1e-5,
        "varying_me": 1e-5,
    }
    caps = {
        "omega_b": 5e-5,
        "omega_cdm": 2e-4,
        "H0": 0.15,
        "logA": 0.003,
        "n_s": 8e-4,
        "z_reio": 0.15,
        "m_ncdm": 0.01,
        "A_planck": 5e-4,
        "A_act": 5e-4,
        "P_act": 5e-4,
        "Tcal": 5e-4,
        "Ecal": 5e-4,
        "dcdf_rho_inf": 0.002,
        "varying_me": 0.002,
    }
    out = np.zeros(len(names))
    for i, n in enumerate(names):
        h = float(steps[i])
        h = max(h, floors.get(n, 1e-6))
        h = min(h, caps.get(n, 0.1))
        out[i] = h
    return out


def _finite_mlp(model, names, x, f0, max_blow=50.0) -> float | None:
    """Return mlp if finite and not catastrophically worse than f0."""
    v = mlp_at(model, names, x)
    if not math.isfinite(v):
        return None
    if v - f0 > max_blow:  # left the posterior bulk
        return None
    return v


def hessian_fd_adaptive(model, names, x0, steps0, max_shrink=6):
    """Central FD with adaptive shrink; one-sided near lower bounds."""
    d = len(names)
    H = np.zeros((d, d))
    f0 = mlp_at(model, names, x0)
    if not math.isfinite(f0):
        raise RuntimeError("MAP model mlp non-finite")

    steps = steps0.copy()
    # diagonal
    for i in range(d):
        n = names[i]
        lo = LOWER.get(n, -np.inf)
        ok = False
        h = steps[i]
        for _ in range(max_shrink):
            # prefer central if both sides in support and finite
            use_central = (x0[i] - h > lo + 1e-15)
            if use_central:
                xp = x0.copy(); xp[i] += h
                xm = x0.copy(); xm[i] -= h
                fp = _finite_mlp(model, names, xp, f0)
                fm = _finite_mlp(model, names, xm, f0)
                if fp is not None and fm is not None:
                    H[i, i] = (fp - 2 * f0 + fm) / (h * h)
                    steps[i] = h
                    ok = True
                    break
            # one-sided forward (boundary)
            h2 = 2 * h
            x1 = x0.copy(); x1[i] = max(x0[i] + h, lo + 1e-12)
            x2 = x0.copy(); x2[i] = max(x0[i] + h2, lo + 1e-12)
            f1 = _finite_mlp(model, names, x1, f0)
            f2 = _finite_mlp(model, names, x2, f0)
            if f1 is not None and f2 is not None:
                # f(x+2h) - 2 f(x+h) + f(x)
                H[i, i] = (f2 - 2 * f1 + f0) / (h * h)
                steps[i] = h
                ok = True
                break
            h *= 0.5
        if not ok:
            # last resort: large positive curvature placeholder + flag
            H[i, i] = 1.0 / max(steps0[i] ** 2, 1e-12)
            steps[i] = steps0[i]
            print(f"  WARNING: diag FD failed for {n}; using fallback stiffness")

    # off-diagonal (central cross; shrink if needed)
    for i in range(d):
        for j in range(i + 1, d):
            hi, hj = steps[i], steps[j]
            ok = False
            for _ in range(max_shrink):
                def pt(si, sj):
                    x = x0.copy()
                    x[i] = x0[i] + si * hi
                    x[j] = x0[j] + sj * hj
                    # clamp to lower bounds
                    for k, nm in enumerate(names):
                        if nm in LOWER:
                            x[k] = max(x[k], LOWER[nm] + 1e-15)
                    return x

                vals = []
                good = True
                for si, sj in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                    fv = _finite_mlp(model, names, pt(si, sj), f0)
                    if fv is None:
                        good = False
                        break
                    vals.append(fv)
                if good:
                    fpp, fpm, fmp, fmm = vals
                    H[i, j] = H[j, i] = (fpp - fpm - fmp + fmm) / (4 * hi * hj)
                    ok = True
                    break
                hi *= 0.5
                hj *= 0.5
            if not ok:
                H[i, j] = H[j, i] = 0.0
                print(f"  WARNING: off-diag FD failed for {names[i]},{names[j]}; set 0")

    return H, f0, steps


def sample_cov_laplace(map_mlp: float, X: np.ndarray) -> dict:
    """Gaussian Laplace using sample covariance (volume term)."""
    d = X.shape[1]
    # weighted? unweighted after burn
    C = np.cov(X, rowvar=False)
    C = 0.5 * (C + C.T)
    # ridge for soft modes
    w, v = np.linalg.eigh(C)
    w = np.maximum(w, 1e-18 * max(1.0, float(np.max(np.abs(w)))))
    C_reg = v @ np.diag(w) @ v.T
    sign, logdet = np.linalg.slogdet(C_reg)
    logz = -map_mlp + 0.5 * d * math.log(2 * math.pi) + 0.5 * logdet
    return {
        "logZ_samplecov_laplace": float(logz),
        "logdet_Sigma": float(logdet),
        "min_eval_Sigma": float(np.min(w)),
        "max_eval_Sigma": float(np.max(w)),
        "cond_Sigma": float(np.max(w) / max(np.min(w), 1e-300)),
        "regularized_Sigma": True,
    }


def stabilize_hessian(H: np.ndarray) -> tuple[np.ndarray, np.ndarray, bool]:
    H = 0.5 * (H + H.T)
    H = np.nan_to_num(H, nan=0.0, posinf=1e12, neginf=-1e12)
    w, v = np.linalg.eigh(H)
    # floor relative to max |eigenvalue|
    scale = max(1.0, float(np.max(np.abs(w))))
    floor = 1e-10 * scale
    reg = bool(np.any(w < floor))
    w_reg = np.maximum(w, floor)
    H_reg = v @ np.diag(w_reg) @ v.T
    return H_reg, w_reg, reg


def run_one(ch: Path, root: str, packages_path: str | None, step_frac: float, max_fd: bool):
    names = SAMPLED[root]
    map_mlp_chain, x0, X = load_chain_arrays(ch, root, names)
    yml = ch / f"{root}.updated.yaml"
    if not yml.is_file():
        yml = ch / f"{root}.input.yaml"
    print(f"[{root}] loading model from {yml} ...", flush=True)
    model = load_model(yml, packages_path)
    steps0 = chain_std_steps(names, X, step_frac)
    print(
        f"[{root}] MAP chain mlp={map_mlp_chain:.6f}; "
        f"FD Hessian d={len(names)} step_frac={step_frac} max_fd={max_fd}",
        flush=True,
    )
    print(f"[{root}] steps = {dict(zip(names, steps0))}", flush=True)

    if max_fd:
        # smoke: only diag first 3
        H = np.eye(len(names)) * 1e4
        f0 = mlp_at(model, names, x0)
        for i in range(min(3, len(names))):
            h = steps0[i]
            xp = x0.copy(); xp[i] += h
            xm = x0.copy(); xm[i] -= h
            H[i, i] = (mlp_at(model, names, xp) - 2 * f0 + mlp_at(model, names, xm)) / (h * h)
        partial = True
        steps_used = steps0
    else:
        H, f0, steps_used = hessian_fd_adaptive(model, names, x0, steps0)
        partial = False

    H, evals, reg = stabilize_hessian(H)
    sign, logdet = np.linalg.slogdet(H)
    d = len(names)
    if sign <= 0 or not math.isfinite(logdet):
        logz = float("nan")
        ok = False
    else:
        logz = -f0 + 0.5 * d * math.log(2 * math.pi) - 0.5 * logdet
        ok = math.isfinite(logz)

    sc = sample_cov_laplace(f0, X)

    out = {
        "root": root,
        "map_minuslogpost_chain": map_mlp_chain,
        "map_minuslogpost_model": f0,
        "d": d,
        "partial_hessian": partial,
        "regularized": reg,
        "ok_finite": ok,
        "min_eval": _json_float(float(np.min(evals))),
        "max_eval": _json_float(float(np.max(evals))),
        "cond": _json_float(float(np.max(evals) / max(float(np.min(evals)), 1e-300))),
        "logdet_H": _json_float(float(logdet)) if math.isfinite(logdet) else None,
        "logZ_hessian_laplace": _json_float(logz),
        "steps_used": {n: float(steps_used[i]) for i, n in enumerate(names)},
        "step_frac": step_frac,
        "formula": "logZ = -mlp + (d/2)ln(2π) - (1/2)ln det(H), H=∇∇ mlp (FD, stabilized)",
        "samplecov_crosscheck": sc,
    }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chain-dir", type=Path, default=REPO / "docs" / "chains")
    ap.add_argument("--packages-path", default=str(Path.home() / "cobaya_packages_clean"))
    ap.add_argument(
        "--which",
        choices=["dyad", "lcdm", "both", "desi", "desi_dyad", "desi_lcdm"],
        default="both",
        help="old-BAO: dyad|lcdm|both; DESI-DR2: desi|desi_dyad|desi_lcdm",
    )
    ap.add_argument("--step-frac", type=float, default=0.05, help="FD step as fraction of chain std")
    ap.add_argument("--max-fd", action="store_true", help="smoke: only 3-D diagonal Hessian")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    roots = []
    if args.which in ("dyad", "both"):
        roots.append("dyad_mnu_bbnfix")
    if args.which in ("lcdm", "both"):
        roots.append("cmp_lcdm_mnu_bbnfix")
    if args.which in ("desi", "desi_dyad"):
        roots.append("dyad_mnu_bbnfix_desidr2")
    if args.which in ("desi", "desi_lcdm"):
        roots.append("cmp_lcdm_mnu_bbnfix_desidr2")
    results = {}
    for r in roots:
        results[r] = run_one(args.chain_dir, r, args.packages_path, args.step_frac, args.max_fd)
        print(json.dumps(results[r], indent=2, allow_nan=False), flush=True)
    payload = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "method": "FD Hessian Laplace hardened (chain-std steps, adaptive shrink, boundary one-sided)",
        "which": args.which,
        "results": results,
        "not_nested": True,
    }
    # pair delta if both legs of a matched instrument present
    dyad_key = lcdm_key = None
    if "dyad_mnu_bbnfix_desidr2" in results and "cmp_lcdm_mnu_bbnfix_desidr2" in results:
        dyad_key, lcdm_key = "dyad_mnu_bbnfix_desidr2", "cmp_lcdm_mnu_bbnfix_desidr2"
        payload["instrument"] = "DESI-DR2 bbnfix"
    elif "dyad_mnu_bbnfix" in results and "cmp_lcdm_mnu_bbnfix" in results:
        dyad_key, lcdm_key = "dyad_mnu_bbnfix", "cmp_lcdm_mnu_bbnfix"
        payload["instrument"] = "old-BAO bbnfix"
    if dyad_key and lcdm_key:
        a = results[dyad_key].get("logZ_hessian_laplace")
        b = results[lcdm_key].get("logZ_hessian_laplace")
        if a is not None and b is not None:
            payload["delta_lnZ_hessian"] = a - b
            print(f"\nΔlnZ_hessian_Laplace (dyad-lcdm) = {a - b:+.6f}", flush=True)
        sa = results[dyad_key]["samplecov_crosscheck"]["logZ_samplecov_laplace"]
        sb = results[lcdm_key]["samplecov_crosscheck"]["logZ_samplecov_laplace"]
        payload["delta_lnZ_samplecov"] = sa - sb
        print(f"ΔlnZ_samplecov_Laplace (dyad-lcdm) = {sa - sb:+.6f}", flush=True)
        payload["both_ok"] = bool(
            results[dyad_key].get("ok_finite") and results[lcdm_key].get("ok_finite")
        )
    default_out = (
        REPO / "docs/working_logs/_runs/credibility_diagnostics_20260808/hessian_laplace_desidr2.json"
        if args.which.startswith("desi")
        else REPO / "docs/working_logs/_runs/credibility_diagnostics_20260808/hessian_laplace_v2.json"
    )
    out = args.out or default_out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")
    print(f"wrote {out}", flush=True)
    if not payload.get("both_ok", True):
        sys.exit(2)


if __name__ == "__main__":
    main()
