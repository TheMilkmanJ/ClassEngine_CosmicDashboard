#!/usr/bin/env python3
"""
desk_compute_all_safe.py — formulable non-MCMC / non-PolyChord desk compute runner.

Rules:
  - NO FABRICATIONS, no H0 book, no live MCMC surgery, no PolyChord
  - exit 0 ≠ automatic physics PASS (caller grades logs)
  - skips booking / force-getdist / polychord / cobaya-run wrappers
  - OMP_NUM_THREADS=1 recommended by caller

Usage:
  python3 scripts/desk_compute_all_safe.py --pack all --timeout 180 --outdir docs/working_logs/_runs/desk_compute_full_20260804
  python3 scripts/desk_compute_all_safe.py --pack bounce --timeout 120
  python3 scripts/desk_compute_all_safe.py --list
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PAPERS = ROOT / "papers"

# Explicit deny: booking, nested sampling, chain surgery, long getdist force
DENY_SUBSTR = (
    "polychord",
    "poly_chord",
    "book_bbnfix",
    "finalize_h0",
    "make_getdist",
    "bbnfix_when_ready",
    "setup_cloud",
    "run_polychord",
    "build_chain_seed",
    "build_reseed_covmat",
    "watch_tribunal",
    "arxiv_package_audit",  # packaging not physics compute (optional pack)
)

# Packs: ordered lists of (label, argv relative to ROOT as list of str paths/args)
# Prefer short analytic / nogo / recompute. CLASS-heavy packs called separately.

def _py(*parts: str) -> list[str]:
    return [sys.executable, str(ROOT / parts[0]), *parts[1:]]


PACKS: dict[str, list[tuple[str, list[str]]]] = {
    "arithmetic": [
        ("bbn_eps", _py("papers/bbn-eps-bound/recompute_eps_bound.py")),
        ("supertrace_k1", _py("scripts/supertrace_k1_verify.py")),
        ("area_law_quarter", _py("scripts/quantum_area_law_quarter.py")),
        ("tau_parseval", _py("scripts/tau_parseval_recompute.py")),
        ("rho_bounce", _py("scripts/rho_bounce.py")),
        ("fbar_lo", _py("scripts/fbar_leading_order_price.py")),
        ("fbar_cw_lo", _py("scripts/fbar_cw_lo_closure.py")),
        ("fbar_window", _py("scripts/fbar_window_discriminator.py")),
        ("fbar_envelope", _py("scripts/fbar_finite_turn_envelope.py")),
    ],
    "bounce": [],  # filled dynamically from bounce_*.py
    "koide": [],
    "baryo_rm": [
        ("baryo_junction", _py("scripts/baryogenesis_junction_closure.py")),
        ("junction_quartet", _py("scripts/junction_quartet_closure.py")),
        ("rm_coherence", _py("scripts/rm_coherence_kibble.py")),
        ("winding_turn", _py("scripts/winding_turn_budget.py")),
    ],
    "hierarchy": [],
    "page_instrument": [
        ("page_scorecard_v13", _py(
            "scripts/page_protocol_scorecard.py",
            str(ROOT / "docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json"),
        )),
        ("area_law_quarter", _py("scripts/quantum_area_law_quarter.py")),
        ("page_scaffold", _py("scripts/quantum_page_curve_scaffold.py")),
    ],
    "quantum_residual": [
        ("medium_decoherence", _py("scripts/medium_induced_decoherence.py")),
        ("chsh_tsirelson", _py("scripts/quantum_chsh_tsirelson.py")),
        ("medium_r_inventory", _py("scripts/quantum_medium_r_inventory.py")),
        ("wkb_medium", _py("scripts/quantum_wkb_medium_identity.py")),
        ("pair_hamiltonian", _py("scripts/quantum_pair_hamiltonian_tmsv.py")),
    ],
    "alpha_amp": [
        ("alpha_c_band", _py("scripts/alpha_c_band_convergence.py")),
        ("alpha_c_same", _py("scripts/alpha_c_same_response.py")),
        ("amplitude_standing", _py("scripts/amplitude_standing.py")),
        ("amplitude_11_analytic", _py("scripts/amplitude_11_analytic.py")),
        ("bao_scale", _py("scripts/bao_scale.py")),
        ("birefringence", _py("scripts/birefringence_window.py")),
        ("audit_math", _py("scripts/audit_math_pass.py")),
    ],
    "tests_analytic": [
        ("test_local_gravity", _py("scripts/test_local_gravity.py")),
        ("test_bbn_activation", _py("scripts/test_bbn_activation.py")),
    ],
    "current_core": [
        ("validate_dcdf", [sys.executable, str(ROOT / "validate_dcdf.py")]),
        ("test_dcdf_clustering", [sys.executable, str(ROOT / "test_dcdf_clustering.py")]),
    ],
}


def _glob_pack(prefix: str, exclude_sub: tuple[str, ...] = ()) -> list[tuple[str, list[str]]]:
    out = []
    for p in sorted(SCRIPTS.glob(f"{prefix}*.py")):
        name = p.name
        if any(x in name.lower() for x in exclude_sub):
            continue
        if any(d in name.lower() for d in DENY_SUBSTR):
            continue
        label = p.stem
        out.append((label, [sys.executable, str(p)]))
    return out


def build_packs() -> dict[str, list[tuple[str, list[str]]]]:
    packs = {k: list(v) for k, v in PACKS.items()}
    packs["bounce"] = _glob_pack("bounce_")
    packs["koide"] = _glob_pack("koide_")
    packs["hierarchy"] = _glob_pack("hierarchy_") + _glob_pack("basement_")
    # delivery_law cousins used by koide residual
    for p in sorted(SCRIPTS.glob("delivery_law_*.py")):
        packs["koide"].append((p.stem, [sys.executable, str(p)]))
    return packs


def should_skip(path: Path) -> bool:
    n = path.name.lower()
    return any(d in n for d in DENY_SUBSTR)


def run_one(label: str, argv: list[str], outdir: Path, timeout: int) -> dict:
    log = outdir / "logs" / f"{label}.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env.setdefault("OMP_NUM_THREADS", "1")
    env.setdefault("OPENBLAS_NUM_THREADS", "1")
    env.setdefault("MKL_NUM_THREADS", "1")
    t0 = time.time()
    meta = {
        "label": label,
        "argv": argv,
        "timeout_s": timeout,
        "started": datetime.now(timezone.utc).isoformat(),
    }
    try:
        proc = subprocess.run(
            argv,
            cwd=str(ROOT),
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        dt = time.time() - t0
        text = (proc.stdout or "") + ("\n" + proc.stderr if proc.stderr else "")
        log.write_text(text, encoding="utf-8", errors="replace")
        # crude token scan — not a physics grade
        has_pass = bool(re.search(r"\bPASS\b", text))
        has_fail = bool(re.search(r"\bFAIL\b", text))
        meta.update(
            {
                "exit": proc.returncode,
                "elapsed_s": round(dt, 3),
                "log": str(log.relative_to(ROOT)),
                "token_PASS": has_pass,
                "token_FAIL": has_fail,
                "status": "ok" if proc.returncode == 0 else "nonzero",
            }
        )
    except subprocess.TimeoutExpired as e:
        dt = time.time() - t0
        partial = ""
        if e.stdout:
            partial += e.stdout if isinstance(e.stdout, str) else e.stdout.decode("utf-8", "replace")
        if e.stderr:
            partial += "\n" + (e.stderr if isinstance(e.stderr, str) else e.stderr.decode("utf-8", "replace"))
        log.write_text(partial + f"\n\n[TIMEOUT after {timeout}s]\n", encoding="utf-8", errors="replace")
        meta.update(
            {
                "exit": -9,
                "elapsed_s": round(dt, 3),
                "log": str(log.relative_to(ROOT)),
                "token_PASS": False,
                "token_FAIL": False,
                "status": "timeout",
            }
        )
    except FileNotFoundError as e:
        meta.update({"exit": -1, "elapsed_s": 0, "status": "missing", "error": str(e)})
    except Exception as e:
        meta.update({"exit": -2, "elapsed_s": round(time.time() - t0, 3), "status": "error", "error": str(e)})
    return meta


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pack", default="all", help="pack name or 'all' or comma list")
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument(
        "--outdir",
        default="docs/working_logs/_runs/desk_compute_full_20260804",
    )
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--max", type=int, default=0, help="cap jobs (0=all)")
    args = ap.parse_args()

    packs = build_packs()
    if args.list:
        for name, jobs in packs.items():
            print(f"[{name}] {len(jobs)} jobs")
            for lab, argv in jobs:
                print(f"  {lab}: {' '.join(argv[:3])}...")
        print("packs:", ", ".join(sorted(packs)) + ", all")
        return 0

    want = (
        list(packs.keys())
        if args.pack == "all"
        else [p.strip() for p in args.pack.split(",") if p.strip()]
    )
    jobs: list[tuple[str, list[str]]] = []
    for w in want:
        if w not in packs:
            print(f"unknown pack: {w}", file=sys.stderr)
            return 2
        jobs.extend(packs[w])
    # de-dupe by label keep first
    seen = set()
    dedup = []
    for lab, argv in jobs:
        if lab in seen:
            continue
        seen.add(lab)
        dedup.append((lab, argv))
    jobs = dedup
    if args.max > 0:
        jobs = jobs[: args.max]

    outdir = ROOT / args.outdir
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "logs").mkdir(exist_ok=True)

    results = []
    print(f"desk_compute_all_safe: {len(jobs)} jobs → {outdir}")
    for i, (lab, argv) in enumerate(jobs, 1):
        print(f"[{i}/{len(jobs)}] {lab} ...", flush=True)
        meta = run_one(lab, argv, outdir, args.timeout)
        results.append(meta)
        print(f"    exit={meta.get('exit')} status={meta.get('status')} t={meta.get('elapsed_s')}s", flush=True)

    summary = {
        "stamp": datetime.now(timezone.utc).isoformat(),
        "packs": want,
        "timeout_s": args.timeout,
        "n_jobs": len(results),
        "n_exit0": sum(1 for r in results if r.get("exit") == 0),
        "n_nonzero": sum(1 for r in results if isinstance(r.get("exit"), int) and r["exit"] not in (0, None) and r.get("status") != "timeout"),
        "n_timeout": sum(1 for r in results if r.get("status") == "timeout"),
        "n_missing": sum(1 for r in results if r.get("status") == "missing"),
        "results": results,
        "rule": "exit0_neq_PASS; no MCMC; no PolyChord; no book",
    }
    (outdir / "SUMMARY.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    # markdown table
    lines = [
        "# Desk compute SUMMARY",
        "",
        f"**Stamp:** {summary['stamp']}",
        f"**Jobs:** {summary['n_jobs']} · exit0={summary['n_exit0']} · nonzero={summary['n_nonzero']} · timeout={summary['n_timeout']}",
        "",
        "| label | exit | status | t(s) | PASS token | FAIL token | log |",
        "|---|---:|---|---:|---|---|---|",
    ]
    for r in results:
        lines.append(
            f"| `{r['label']}` | {r.get('exit')} | {r.get('status')} | {r.get('elapsed_s', '')} | "
            f"{r.get('token_PASS')} | {r.get('token_FAIL')} | {r.get('log', '')} |"
        )
    lines += [
        "",
        "**Rule:** exit 0 ≠ automatic physics PASS. Promotion only where residual freeze allows.",
        "*NO FABRICATIONS. No PolyChord. No live MCMC surgery. No H₀ book.*",
        "",
    ]
    (outdir / "SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {outdir / 'SUMMARY.md'}")
    return 0 if summary["n_timeout"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
