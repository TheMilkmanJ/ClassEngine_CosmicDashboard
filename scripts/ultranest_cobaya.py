#!/usr/bin/env python3
"""ultranest_cobaya — receipts-reconstructed UltraNest driver (Google path).

PROVENANCE
  The 2026-08-13 freeze file (sha256 0f7932dcc0ebc88cdab24052afd94fd0a5ff6481203b51e614cf1ec42e728e8f,
  14912 B) was never committed. It is not in git, not in Google Drive, and AWS
  recovery is unavailable. This file is reconstructed from the finished LCDM
  UltraNest receipts so the Google Compute Engine path can launch the same
  engine settings and integrand convention as the booked twin.

  It will NOT match the freeze sha256. Do not claim it is the freeze byte copy.
  Physics / priors / datasets stay in the yaml. This file is glue only.

PINNED FROM RECEIPTS (un_lcdm_*_finished_20260824/25)
  ReactiveNestedSampler, UltraNest 4.5.0, hdf5, vectorized=False, nbootstraps=30,
  ndraw=128..65536, resume=False on a fresh start.
  SliceSampler nsteps=2*ndim (LCDM ndim=12 -> 24), generate_region_oriented_direction.
  run kwargs: min_num_live_points=400, dlogz=0.5, frac_remain=0.01, Lepsilon=0.001.
  Integrand: Cobaya logposterior (like + prior + external BBN).
  Transform: linear unit-cube map onto prior support (not inverse-CDF).
  Summary JSON keys and DONE line format match the peeled receipts.

Usage:
  python scripts/ultranest_cobaya.py YAML OUT [--nlive 400] [--frac-remain 0.01]
  python scripts/ultranest_cobaya.py YAML OUT --resume
  python scripts/ultranest_cobaya.py --self-test
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

PROVENANCE = "receipts-reconstructed-20260904"
FREEZE_SHA256 = "0f7932dcc0ebc88cdab24052afd94fd0a5ff6481203b51e614cf1ec42e728e8f"
SUMMARY_NOTE = (
    "Nested evidence under unit-cube prior on transform support; "
    "Cobaya logposterior (like+prior+external BBN) is the integrand. "
    "Comparable across twins with identical UltraNest settings."
)


def mpi_info():
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
        return comm, comm.Get_rank(), comm.Get_size()
    except Exception:
        return None, 0, 1


def log(msg: str, rank: int = 0) -> None:
    if rank == 0:
        print(f"[ultranest_cobaya] {msg}", flush=True)


def log_all(msg: str) -> None:
    print(f"[ultranest_cobaya] {msg}", flush=True)


def unit_cube_transform(u, lo, hi):
    import numpy as np
    u = np.asarray(u, dtype=float)
    return lo + u * (hi - lo)


def ref_point_from_info(info: dict, names: list[str]) -> dict:
    refs = {}
    params = info.get("params") or {}
    for name in names:
        p = params.get(name) or {}
        ref = p.get("ref")
        if isinstance(ref, dict) and "loc" in ref:
            refs[name] = float(ref["loc"])
            continue
        prior = p.get("prior")
        if isinstance(prior, dict) and "loc" in prior:
            refs[name] = float(prior["loc"])
            continue
        if isinstance(prior, dict) and "min" in prior and "max" in prior:
            refs[name] = 0.5 * (float(prior["min"]) + float(prior["max"]))
            continue
        raise KeyError(f"no ref/loc or prior min/max for {name}")
    return refs


def summary_payload(
    *,
    yaml_path: str,
    out: str,
    params: list[str],
    nlive: int,
    frac_remain: float,
    max_ncalls,
    logz,
    logzerr,
    ncall,
    ncalls_wrapper: int,
    wall_s: float,
    ref_logpost: float,
    ultranest_version: str,
    mpi_size: int,
) -> dict:
    return {
        "yaml": yaml_path,
        "out": out,
        "params": list(params),
        "ndim": len(params),
        "nlive": nlive,
        "frac_remain": frac_remain,
        "max_ncalls": max_ncalls,
        "logz": logz,
        "logzerr": logzerr,
        "ncall": ncall,
        "ncalls_wrapper": ncalls_wrapper,
        "wall_s": wall_s,
        "ref_logpost": ref_logpost,
        "sampler": "ultranest.ReactiveNestedSampler",
        "ultranest_version": ultranest_version,
        "note": SUMMARY_NOTE,
        "mpi_size": mpi_size,
        "driver_provenance": PROVENANCE,
    }


def done_line(logz: float, logzerr: float, wall_s: float, mpi_size: int) -> str:
    return (
        f"DONE logZ={logz:.4f} ± {logzerr:.4f} "
        f"wall={wall_s / 3600.0:.2f}h mpi_size={mpi_size}"
    )


def self_test() -> int:
    import numpy as np

    lo = np.array([0.02, 64.0])
    hi = np.array([0.025, 78.0])
    mid = unit_cube_transform([0.5, 0.5], lo, hi)
    assert np.allclose(mid, [0.0225, 71.0]), mid
    info = {
        "params": {
            "omega_b": {"prior": {"min": 0.02, "max": 0.025}, "ref": {"dist": "norm", "loc": 0.0224}},
            "A_planck": {"prior": {"dist": "norm", "loc": 1.0, "scale": 0.0025}, "ref": {"dist": "norm", "loc": 1.0}},
        }
    }
    refs = ref_point_from_info(info, ["omega_b", "A_planck"])
    assert refs == {"omega_b": 0.0224, "A_planck": 1.0}, refs
    payload = summary_payload(
        yaml_path="cmp_lcdm_mnu_bbnfix_desidr2_ev.yaml",
        out="/tmp/out",
        params=["omega_b", "H0"],
        nlive=400,
        frac_remain=0.01,
        max_ncalls=None,
        logz=-1413.4856513862044,
        logzerr=0.5841554518436771,
        ncall=2048560,
        ncalls_wrapper=21343,
        wall_s=1115735.4040744305,
        ref_logpost=-1720.232770226742,
        ultranest_version="4.5.0",
        mpi_size=96,
    )
    required = {
        "yaml", "out", "params", "ndim", "nlive", "frac_remain", "max_ncalls",
        "logz", "logzerr", "ncall", "ncalls_wrapper", "wall_s", "ref_logpost",
        "sampler", "ultranest_version", "note", "mpi_size",
    }
    missing = required - set(payload)
    assert not missing, missing
    assert payload["ndim"] == 2
    assert payload["note"] == SUMMARY_NOTE
    line = done_line(-1413.4856513862044, 0.5841554518436771, 1115735.4040744305, 96)
    assert line == "DONE logZ=-1413.4857 ± 0.5842 wall=309.93h mpi_size=96", line
    print("[ultranest_cobaya] self-test OK provenance=" + PROVENANCE)
    return 0


def build_model(yaml_path: str):
    import yaml
    from cobaya.model import get_model

    info = yaml.safe_load(Path(yaml_path).read_text())
    info.pop("sampler", None)
    info.pop("output", None)
    t0 = time.time()
    model = get_model(info)
    return info, model, time.time() - t0


def run(args) -> int:
    import numpy as np
    import ultranest
    from ultranest import ReactiveNestedSampler
    from ultranest.stepsampler import SliceSampler, generate_region_oriented_direction

    comm, rank, mpi_size = mpi_info()
    yaml_path = str(Path(args.yaml).resolve()) if Path(args.yaml).exists() else args.yaml
    out = str(Path(args.out))
    if rank == 0:
        Path(out).mkdir(parents=True, exist_ok=True)

    info, model, ready_s = build_model(args.yaml)
    names = list(model.parameterization.sampled_params())
    ndim = len(names)
    nsteps = args.nsteps if args.nsteps is not None else 2 * ndim
    bounds = np.asarray(model.prior.bounds(confidence_for_unbounded=1.0 - 1e-7), dtype=float)
    lo, hi = bounds[:, 0], bounds[:, 1]
    refs = ref_point_from_info(info, names)

    log(f"yaml={args.yaml} ndim={ndim} params={names} mpi_size={mpi_size}", rank)
    log(f"model ready in {ready_s:.1f}s (mpi_size={mpi_size})", rank)

    ref_lp = model.logposterior(refs)
    ref_logpost = float(ref_lp.logpost)
    log(f"ref logpost={ref_logpost:.6f} at { {k: np.float64(v) for k, v in refs.items()} }", rank)

    ncalls_wrapper = 0
    last_logpost = [ref_logpost]
    t_wrap0 = time.time()

    def transform(u):
        return unit_cube_transform(u, lo, hi)

    def loglike(theta):
        nonlocal ncalls_wrapper
        ncalls_wrapper += 1
        try:
            lp = model.logposterior(dict(zip(names, theta)))
            val = float(lp.logpost)
        except Exception:
            val = -1.0e300
        if not np.isfinite(val):
            val = -1.0e300
        last_logpost[0] = val
        if rank == 0 and ncalls_wrapper % 100 == 0:
            dt = max(time.time() - t_wrap0, 1e-9)
            log(f"ncalls={ncalls_wrapper} rate={ncalls_wrapper / dt:.3f}/s last_logpost={val:.4f}", rank)
        return val

    log_all(f"SliceSampler nsteps={nsteps} dir=generate_region_oriented_direction")
    resume = True if args.resume else False
    sampler = ReactiveNestedSampler(
        names,
        loglike,
        transform=transform,
        log_dir=out,
        resume=resume,
        vectorized=False,
        num_bootstraps=30,
        ndraw_min=128,
        ndraw_max=65536,
        storage_backend="hdf5",
    )
    sampler.stepsampler = SliceSampler(
        nsteps=nsteps,
        generate_direction=generate_region_oriented_direction,
    )
    run_kwargs = dict(
        min_num_live_points=args.nlive,
        dlogz=0.5,
        frac_remain=args.frac_remain,
        Lepsilon=0.001,
    )
    if args.max_ncalls is not None:
        run_kwargs["max_ncalls"] = args.max_ncalls
    log_all(f"starting run kwargs={run_kwargs}")

    t0 = time.time()
    result = sampler.run(**run_kwargs)
    wall_s = time.time() - t0
    logz = float(result["logz"])
    logzerr = float(result["logzerr"])
    ncall = int(result.get("ncall") or result.get("ncalls") or 0)

    payload = summary_payload(
        yaml_path=yaml_path,
        out=out,
        params=names,
        nlive=args.nlive,
        frac_remain=args.frac_remain,
        max_ncalls=args.max_ncalls,
        logz=logz,
        logzerr=logzerr,
        ncall=ncall,
        ncalls_wrapper=ncalls_wrapper,
        wall_s=wall_s,
        ref_logpost=ref_logpost,
        ultranest_version=ultranest.__version__,
        mpi_size=mpi_size,
    )
    summary_path = str(Path(out) / "ultranest_summary.json")
    if rank == 0:
        Path(summary_path).write_text(json.dumps(payload, indent=2) + "\n")
        print(json.dumps(payload, indent=2), flush=True)
        log(done_line(logz, logzerr, wall_s, mpi_size), rank)
        log(f"wrote {summary_path}", rank)
    return 0


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="UltraNest + Cobaya driver (receipts-reconstructed)")
    p.add_argument("yaml", nargs="?", help="cobaya yaml (likelihood/theory/params). sampler block ignored.")
    p.add_argument("out", nargs="?", help="UltraNest log_dir (hdf5 checkpoint lives here)")
    p.add_argument("--nlive", type=int, default=400)
    p.add_argument("--frac-remain", type=float, default=0.01, dest="frac_remain")
    p.add_argument("--max-ncalls", type=int, default=None, dest="max_ncalls")
    p.add_argument("--nsteps", type=int, default=None, help="SliceSampler nsteps; default 2*ndim")
    p.add_argument("--resume", action="store_true", help="continue from OUT/results/points.hdf5")
    p.add_argument("--self-test", action="store_true", dest="self_test")
    return p.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.yaml or not args.out:
        parse_args(["--help"])
        return 2
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
