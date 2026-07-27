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
SKIP = {"weight", "minuslogpost", "minuslogprior", "minuslogprior__0", "chi2"}
BURN = 0.30
MAXP = 8


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


def main() -> None:
    os.makedirs("docs/plots", exist_ok=True)
    lines = [
        "# Production-chain parameter tables (GetDist)",
        "",
        "> ForJustin/12 item 5(b)'s instrument (`scripts/make_getdist_tables.py`).",
        "> Regenerated per run at its landing; the running pair and Route-D join",
        "> at convergence. Means with 68% limits, 30% burn-in.",
        "",
    ]
    for root, desc in ROOTS:
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
        lines.append(f"## {root} — {desc} ({n} post-burn samples)")
        lines.append("")
        lines.append("| parameter | mean | 68% limits |")
        lines.append("|---|---|---|")
        marge = samples.getMargeStats()
        for p in names:
            try:
                d = marge.parWithName(p)
                lines.append(f"| {p} | {d.mean:.5g} | "
                             f"[{d.limits[0].lower:.5g}, {d.limits[0].upper:.5g}] |")
            except Exception:
                lines.append(f"| {p} | — | — |")
        lines.append("")
    with open("docs/PRTOE_CHAIN_TABLES.md", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("   tables → docs/PRTOE_CHAIN_TABLES.md")


if __name__ == "__main__":
    main()
