#!/usr/bin/env python3
"""
Are the three MPI ranks in one basin?

An external reviewer named this as the single thing that would move the program's
score: "all three MPI ranks in one basin + a real R-1 path (even if LCDM wins)."
R-1 itself is a between-chain statistic that cobaya reports only at checkpoints,
but the underlying question -- do the ranks agree about where the posterior is --
is answerable RIGHT NOW from the chain files on disk.

This does not compute Gelman-Rubin. It answers the prior question: if the ranks
are exploring different basins, no amount of further running fixes it, and the
configuration needs attention instead of patience.

Three diagnostics per chain, per rank:
  (1) best -logpost         -- are they finding the same minimum?
  (2) mean/spread of -logpost over the last half (post-burn-in proxy)
  (3) per-parameter means   -- the decisive one; a rank in another basin shows
                              up as a parameter mean many within-rank sigmas away

Pre-stated control: ranks of the SAME chain sample the SAME posterior, so under
good mixing every per-parameter mean should sit within a few within-rank standard
errors of the pooled mean. A rank sitting >5 standard errors out on several
parameters at once is not slow mixing, it is a different basin.
"""

import glob
import os
import math

CHAINS = "/home/themilkmanj/prtoe_class/chains"
BASES = ["cmp_lcdm_mnu_bbnfix", "dyad_mnu_bbnfix"]


def read_rank(path):
    """Return (header_names, rows) where rows are lists of floats."""
    names, rows = [], []
    with open(path) as fh:
        for line in fh:
            if line.startswith("#"):
                if not names:
                    names = line.lstrip("#").split()
                continue
            parts = line.split()
            try:
                rows.append([float(x) for x in parts])
            except ValueError:
                pass
    return names, rows


def wmean(vals, wts):
    W = sum(wts)
    return sum(v * w for v, w in zip(vals, wts)) / W if W else float("nan")


def wstd(vals, wts, mu):
    W = sum(wts)
    if W <= 0:
        return float("nan")
    var = sum(w * (v - mu) ** 2 for v, w in zip(vals, wts)) / W
    return math.sqrt(max(var, 0.0))


def analyse(base):
    paths = sorted(glob.glob(os.path.join(CHAINS, base + ".*.txt")))
    if not paths:
        print(f"  no chain files for {base}")
        return
    print("=" * 78)
    print(f"  {base}   ({len(paths)} rank file(s))")
    print("=" * 78)

    ranks = []
    names = None
    for p in paths:
        nm, rows = read_rank(p)
        if not rows:
            continue
        names = names or nm
        ranks.append((os.path.basename(p), rows))

    if len(ranks) < 2:
        print("  SINGLE RANK -- no between-rank statement is possible, and no")
        print("  Gelman-Rubin statistic can ever be produced from this run.")
        return

    # ---- (1) and (2): -logpost per rank ---------------------------------
    print(f"\n  {'rank':<28} {'N':>7} {'best':>11} {'mean(2nd half)':>15} {'sd':>8}")
    for fn, rows in ranks:
        lp = [r[1] for r in rows]
        w = [r[0] for r in rows]
        half = len(rows) // 2
        lp2, w2 = lp[half:], w[half:]
        mu = wmean(lp2, w2)
        sd = wstd(lp2, w2, mu)
        print(f"  {fn:<28} {len(rows):7d} {min(lp):11.3f} {mu:15.3f} {sd:8.3f}")

    bests = [min(r[1] for r in rows) for _fn, rows in ranks]
    print(f"\n  spread in best -logpost across ranks: {max(bests)-min(bests):.3f}")
    print("    (a large spread means the ranks have not found the same minimum)")

    # ---- (3) per-parameter means ----------------------------------------
    if not names or len(names) < 3:
        print("\n  no usable parameter header; skipping per-parameter comparison")
        return

    npar = min(len(names), min(len(rows[0]) for _f, rows in ranks))
    # columns 0,1 are weight and -logpost; parameters start at 2
    print(f"\n  PER-PARAMETER RANK COMPARISON (second half of each rank)")
    print(f"  {'parameter':<22} " + " ".join(f"{'rank'+str(i+1):>12}" for i in range(len(ranks)))
          + f" {'max|z|':>8}")
    worst_overall, worst_par = 0.0, ""
    for j in range(2, min(npar, 10)):
        col_mu, col_se = [], []
        for _fn, rows in ranks:
            half = len(rows) // 2
            vals = [r[j] for r in rows[half:]]
            wts = [r[0] for r in rows[half:]]
            mu = wmean(vals, wts)
            sd = wstd(vals, wts, mu)
            neff = max(len(vals), 1)
            col_mu.append(mu)
            col_se.append(sd / math.sqrt(neff) if neff else float("nan"))
        pooled = sum(col_mu) / len(col_mu)
        zs = []
        for mu, se in zip(col_mu, col_se):
            zs.append(abs(mu - pooled) / se if se and se > 0 else float("nan"))
        mz = max(z for z in zs if not math.isnan(z)) if any(not math.isnan(z) for z in zs) else float("nan")
        if not math.isnan(mz) and mz > worst_overall:
            worst_overall, worst_par = mz, names[j]
        print(f"  {names[j]:<22} " + " ".join(f"{m:12.5g}" for m in col_mu) + f" {mz:8.1f}")

    print(f"\n  WORST per-parameter rank separation: {worst_overall:.1f} standard errors"
          f"  (on {worst_par})")
    if worst_overall > 5:
        print("  READ: the ranks disagree far beyond their own sampling error on at least")
        print("  one parameter. That is a basin/burn-in problem, not slow mixing -- more")
        print("  wall-clock at these settings does not fix it.")
    else:
        print("  READ: rank means agree within a few standard errors -- consistent with")
        print("  one basin, and R-1 should fall as samples accumulate.")


def main():
    print("\n  Do the MPI ranks agree about where the posterior is?")
    print("  (this is the question BEHIND R-1, answerable now from files on disk)\n")
    for b in BASES:
        analyse(b)
        print()


if __name__ == "__main__":
    main()
