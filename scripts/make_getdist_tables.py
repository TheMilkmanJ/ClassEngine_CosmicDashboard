"""make_getdist_tables — ForJustin/12 item 5(b): triangle plots + parameter tables per plot-ready production run (2026-07-27).

For each completed production chain (≳1000 samples with input yaml + covmat,
per the 2026-07-27 inventory), this produces:
  * docs/plots/<name>_triangle.png — the GetDist triangle over the sampled
    cosmological parameters (30% burn-in);
  * a consolidated markdown table (docs/PRTOE_CHAIN_TABLES.md) of means ±68%
    limits per run — the referee-facing numbers, regenerable by rerunning
    this script as later chains converge (the bbnfix pair and Route-D get
    their rows at convergence; this instrument is theirs too).
Cobaya chain format: column names on the header line ("# weight minuslogpost
p1 p2 …"); weights in column 0.
"""
from __future__ import annotations

import os
import numpy as np

os.environ.setdefault("MPLBACKEND", "Agg")
from getdist import plots, MCSamples  # noqa: E402

ROOTS = [
    ("cmp_prtoe_conv_desi", "conversion channel vs DESI stack"),
    ("cmp_prtoe_zon_disp", "onset-identity dispersion run"),
    ("dyad_mnu_mcmc", "the scalar chain, Σm_ν free"),
    ("cmp_prtoe_zon", "onset-identity base run"),
]
# BBN-fixed production pair — add ONLY at booking when both R−1 < 0.05
# AND both checkpoints have converged: true (self-stop). See checklist.
# Do not enable for peeks.
BBNFIX_ROOTS = [
    ("cmp_lcdm_mnu_bbnfix", "ΛCDM+mν BBN-fixed control twin"),
    ("dyad_mnu_bbnfix", "dyad BBN-fixed production twin"),
]
SKIP = {"weight", "minuslogpost", "minuslogprior", "minuslogprior__0", "chi2"}
BURN = 0.30
MAXP = 8
RBAR_BBNFIX = 0.05


def load(root):
    path = f"chains/{root}.1.txt"
    with open(path) as f:
        header = f.readline().lstrip("#").split()
    data = np.loadtxt(path, skiprows=1)
    n0 = int(len(data) * BURN)
    data = data[n0:]
    cols = [(i, n) for i, n in enumerate(header)
            if n not in SKIP and not n.startswith("chi2")
            and not n.startswith("minuslog")][: MAXP + 1]
    idx = [i for i, _ in cols if header[i] != "weight"][:MAXP]
    names = [header[i] for i in idx]
    samples = MCSamples(samples=data[:, idx], names=names, labels=names,
                        weights=data[:, 0], name_tag=root)
    return samples, names, len(data)


def _last_rminus1(root: str) -> float | None:
    path = f"chains/{root}.progress"
    try:
        line = open(path).read().strip().splitlines()[-1]
        return float(line.split()[3])
    except Exception:
        return None


def _checkpoint_converged(root: str) -> bool | None:
    """True/False if checkpoint present; None if missing/unreadable."""
    path = f"chains/{root}.checkpoint"
    try:
        text = open(path).read()
    except OSError:
        return None
    if "converged: true" in text:
        return True
    if "converged: false" in text:
        return False
    return None


def main() -> int:
    """Exit 0 on success; exit 2 if --include-bbnfix requested but gate not ready.

    Without --include-bbnfix / --force-bbnfix, only archive ROOTS are tabulated
    (legacy instrument). Prefer scripts/book_bbnfix_when_ready.py for the
    production pair booking card (three-rank, no table clobber risk).
    """
    import sys

    include_bbnfix = "--include-bbnfix" in sys.argv
    force_bbnfix = "--force-bbnfix" in sys.argv  # override gate (NOT for booking)

    os.makedirs("docs/plots", exist_ok=True)
    lines = [
        "# Production-chain parameter tables (GetDist)",
        "",
        "> ForJustin/12 item 5(b)'s instrument (`scripts/make_getdist_tables.py`).",
        "> Regenerated per run at its landing; the running pair and Route-D join",
        "> at convergence. Means with 68% limits, 30% burn-in.",
        "",
        "> **Warning:** this script overwrites `docs/PRTOE_CHAIN_TABLES.md` body",
        "> when the bbnfix **gate is fully open**. Restore live-status banner if clobbered.",
        "",
    ]
    roots = list(ROOTS)
    # force_bbnfix + incomplete gate → NEVER write living PRTOE_CHAIN_TABLES.md
    unbookable_force = False
    force_meta: dict = {}
    if include_bbnfix or force_bbnfix:
        rmap = {r: _last_rminus1(r) for r, _ in BBNFIX_ROOTS}
        cmap = {r: _checkpoint_converged(r) for r, _ in BBNFIX_ROOTS}
        r_ok = all(v is not None and v < RBAR_BBNFIX for v in rmap.values())
        stop_ok = all(v is True for v in cmap.values())
        both_ok = r_ok and stop_ok
        force_meta = {"rmap": rmap, "cmap": cmap}
        print("=" * 72)
        print("make_getdist_tables — bbnfix gate check")
        print(
            "   bbnfix R−1:",
            ", ".join(f"{k}={v}" for k, v in rmap.items()),
        )
        print(
            "   bbnfix converged:",
            ", ".join(f"{k}={v}" for k, v in cmap.items()),
        )
        if both_ok:
            roots = roots + list(BBNFIX_ROOTS)
            print("   bbnfix: INCLUDED (gate OPEN — bookable path)")
            print("=" * 72)
        elif force_bbnfix:
            # Claude red batch-1 cure: do not put clean numbers on the living shelf.
            unbookable_force = True
            roots = roots + list(BBNFIX_ROOTS)
            print(
                "   WARNING: --force-bbnfix with gate incomplete — "
                "NOT bookable; will NOT write docs/PRTOE_CHAIN_TABLES.md"
            )
            print(
                "   Writing UNBOOKABLE working_logs artifact with in-file banner instead."
            )
            print("=" * 72)
        else:
            print(
                f"   NOT READY — need both R−1 < {RBAR_BBNFIX} AND "
                "converged: true on both bbnfix legs."
            )
            print(
                "   REFUSED: will not write PRTOE_CHAIN_TABLES.md or "
                "bbnfix triangles while gate is closed."
            )
            print(
                "   booking ≠ publishing: even after gate opens, forward tables "
                "prefer Stage B after RED_AUDIT (bbnfix_when_ready_all.sh --write-tables)."
            )
            print(
                "   Re-run after gate: python3 scripts/make_getdist_tables.py "
                "--include-bbnfix"
            )
            print(
                "   Prefer production booking: "
                "python3 scripts/book_bbnfix_when_ready.py"
            )
            print(
                "   --force-bbnfix is UNBOOKABLE-only (working_logs artifact; "
                "never living shelf)."
            )
            print("=" * 72)
            return 2
    bbnfix_names = {r for r, _ in BBNFIX_ROOTS}
    for root, desc in roots:
        try:
            samples, names, n = load(root)
        except Exception as e:
            print(f"   {root}: SKIPPED ({e})")
            continue
        g = plots.get_subplot_plotter()
        g.triangle_plot([samples], names, filled=True)
        out = f"docs/plots/{root}_triangle.png"
        g.export(out)
        print(f"   {root}: triangle → {out} ({n} post-burn samples)")
        tag = ""
        if unbookable_force and root in bbnfix_names:
            tag = " **UNCONVERGED / UNBOOKABLE (force peek)**"
        lines.append(f"## {root} — {desc} ({n} post-burn samples){tag}")
        lines.append("")
        if unbookable_force and root in bbnfix_names:
            r1 = force_meta.get("rmap", {}).get(root)
            conv = force_meta.get("cmap", {}).get(root)
            lines.append(
                f"> **UNCONVERGED / UNBOOKABLE.** force-bbnfix peek. "
                f"R−1={r1} converged={conv}. **Do not quote as results.**"
            )
            lines.append("")
        lines.append("| parameter | mean | 68% limits |")
        lines.append("|---|---|---|")
        marge = samples.getMargeStats()
        for p in names:
            try:
                d = marge.parWithName(p)
                row = (
                    f"| {p} | {d.mean:.5g} | "
                    f"[{d.limits[0].lower:.5g}, {d.limits[0].upper:.5g}] |"
                )
                if unbookable_force and root in bbnfix_names:
                    row = (
                        f"| {p} | {d.mean:.5g} **UNBOOKABLE** | "
                        f"[{d.limits[0].lower:.5g}, {d.limits[0].upper:.5g}] "
                        f"**UNCONVERGED** |"
                    )
                lines.append(row)
            except Exception:
                lines.append(f"| {p} | — | — |")
        lines.append("")
    if unbookable_force:
        from datetime import datetime

        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_dir = f"docs/working_logs/_runs/getdist_force_UNBOOKABLE_{stamp}"
        os.makedirs(out_dir, exist_ok=True)
        banner = [
            "# UNBOOKABLE GetDist force peek — NOT a living chain table",
            "",
            "> **Claude red batch-1 cure (2026-08-04):** `--force-bbnfix` must never",
            "> write clean numbers into `docs/PRTOE_CHAIN_TABLES.md`.",
            ">",
            "> **Gate incomplete.** R−1 / converged below. **Do not quote as results.**",
            ">",
            f"> rmap={force_meta.get('rmap')} cmap={force_meta.get('cmap')}",
            "",
        ]
        path = f"{out_dir}/CHAIN_TABLES_UNCONVERGED.md"
        with open(path, "w") as f:
            f.write("\n".join(banner + lines) + "\n")
        print(f"   tables → {path}  (NOT docs/PRTOE_CHAIN_TABLES.md)")
        print("   living shelf PRTOE_CHAIN_TABLES.md left UNTOUCHED")
        return 0
    with open("docs/PRTOE_CHAIN_TABLES.md", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("   tables → docs/PRTOE_CHAIN_TABLES.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
