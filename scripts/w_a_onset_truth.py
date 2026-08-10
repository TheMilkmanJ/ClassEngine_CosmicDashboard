#!/usr/bin/env python3
"""P-042 science debt: CLASS truth table for w_dcdf(a) under bare/conv/thaw.

Usage (from repo root, with project classy on PYTHONPATH):
  PYTHONPATH=python python3 scripts/w_a_onset_truth.py

Writes docs/working_logs/_runs/w_a_onset_<stamp>/REPORT.md + .npz
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))
from classy import Class  # noqa: E402


def run_bg(extra: dict) -> dict:
    cosmo = Class()
    h, omega_b = 0.70, 0.0224
    cosmo.set(
        dict(
            h=h,
            omega_b=omega_b,
            omega_cdm=0.0,
            Omega_Lambda=0.0,
            Omega0_dcdf=1.0 - omega_b / h**2,
            N_ur=2.0328,
            N_ncdm=1,
            m_ncdm=0.06,
            T_ncdm=0.71611,
            output="",
            use_dcdf="yes",
            dcdf_rho_inf=0.70,
            dcdf_z_rad_onset=4.0e7,
            **extra,
        )
    )
    cosmo.compute()
    bg = cosmo.get_background()
    z = np.asarray(bg["z"], float)
    out = dict(
        z=z,
        a=1.0 / (1.0 + z),
        w=np.asarray(bg["(.)w_dcdf"], float),
        rho=np.asarray(bg["(.)rho_dcdf"], float),
        cs2=np.asarray(bg["(.)cs2_dcdf"], float),
    )
    cosmo.struct_cleanup()
    cosmo.empty()
    return out


def main() -> None:
    stamp = time.strftime("%Y%m%d_%H%M%S")
    out = Path(f"docs/working_logs/_runs/w_a_onset_{stamp}")
    out.mkdir(parents=True, exist_ok=True)
    configs = {
        "bare": dict(dcdf_conv_g=0.0, dcdf_floor_thaw=0.0),
        "conv": dict(dcdf_conv_g=0.12, dcdf_floor_thaw=0.0),
        "thaw": dict(dcdf_conv_g=0.0, dcdf_floor_thaw=0.12),
        "both": dict(dcdf_conv_g=0.21, dcdf_floor_thaw=0.03),
    }
    results = {k: run_bg(v) for k, v in configs.items()}
    z_marks = [1e8, 4e7, 1e7, 1e6, 1e5, 1e4, 1e3, 100, 10, 1, 0]

    def w_at(res, z0):
        i = int(np.argmin(np.abs(res["z"] - z0)))
        return float(res["w"][i])

    lines = [
        f"# Model true w_dcdf(a) — {stamp}\n\n",
        "CLASS `(.)w_dcdf`. h=0.70, dcdf_rho_inf=0.70, z_rad_onset=4e7.\n\n",
        "| z | bare | conv | thaw | both |\n|---:|---:|---:|---:|---:|\n",
    ]
    for z0 in z_marks:
        row = [f"{z0:g}"] + [
            f"{w_at(results[t], z0):+.6f}" for t in ("bare", "conv", "thaw", "both")
        ]
        lines.append("| " + " | ".join(row) + " |\n")

    savez = {}
    for tag, res in results.items():
        n = len(res["a"])
        idx = np.linspace(0, n - 1, min(500, n)).astype(int)
        for k in ("a", "z", "w", "cs2"):
            savez[f"{tag}_{k}"] = res[k][idx]
    np.savez(out / "w_a_dcdf_curves.npz", **savez)
    (out / "REPORT.md").write_text("".join(lines))
    print("".join(lines))
    print("wrote", out)


if __name__ == "__main__":
    main()
