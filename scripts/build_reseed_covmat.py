#!/usr/bin/env python3
"""
Prepare (do NOT apply) a corrected proposal covariance for the model chain.

WHY THIS IS NEEDED (diagnosed 2026-07-28, scripts/rank_basin_diagnostic.py):
the model chain's three ranks sit in three basins 233 log units apart, because

    seed covmat too narrow -> 97-99.8% acceptance -> ranks crawl and never merge
      -> R-1 stays far above learn_proposal_Rminus1_max (2.0, or 30.0 early)
        -> the proposal is NEVER re-learned -> the ranks stay frozen

confirmed by file mtimes: the reference chain's covmat was rewritten minutes ago
(its R-1 = 1.011 clears the threshold) while the model's has not changed since
before its own run began.

WHAT THIS DOES: builds a covariance from the samples of the rank that DID find
the good basin, writes it to a NEW file, and touches nothing that is running.
Applying it is an owner decision (task #83) and requires stopping the run.

WHAT THIS DOES NOT DO: it does not widen the covariance by a fudge factor. The
empirical covariance of a stuck chain understates the posterior width, so a
scale factor is offered as a SEPARATE, EXPLICIT output rather than folded in
silently -- the owner can see both and choose.

Pre-stated control: the produced matrix must be symmetric and positive-definite
(all eigenvalues > 0), or it is not a usable proposal and must not be written.
"""

import math
import os

CHAINS = "/home/themilkmanj/prtoe_class/chains"
BASE = "dyad_mnu_bbnfix"
GOOD_RANK = 1          # the rank that found best -logpost = 1377.89
BURN_FRAC = 0.3        # discard this leading fraction as burn-in
OUT = os.path.join(CHAINS, f"_reseed_candidate_{BASE}.covmat")


def load(path):
    names, rows = [], []
    with open(path) as fh:
        for line in fh:
            if line.startswith("#"):
                if not names:
                    names = line.lstrip("#").split()
                continue
            p = line.split()
            if len(p) > 3:
                try:
                    rows.append([float(x) for x in p])
                except ValueError:
                    pass
    return names, rows


def cov(cols, wts):
    n = len(cols)
    W = sum(wts)
    mu = [sum(w * c[i] for w, c in zip(wts, zip(*cols))) / W for i in range(n)] \
        if False else [sum(w * v for w, v in zip(wts, col)) / W for col in cols]
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            s = sum(w * (a - mu[i]) * (b - mu[j])
                    for w, a, b in zip(wts, cols[i], cols[j]))
            C[i][j] = C[j][i] = s / W
    return mu, C


def cholesky_ok(C):
    """Return True if C is positive-definite (Cholesky succeeds)."""
    n = len(C)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = C[i][j] - sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                if s <= 0:
                    return False
                L[i][j] = math.sqrt(s)
            else:
                L[i][j] = s / L[j][j]
    return True


def main():
    path = os.path.join(CHAINS, f"{BASE}.{GOOD_RANK}.txt")
    if not os.path.exists(path):
        print("=" * 74)
        print("  NO SAMPLES TO BUILD FROM — the source chain file does not exist.")
        print(f"    looked for: {path}")
        print("""
  Expected during burn-in, and after any relaunch with -f (which deletes previous
  chain files). This script builds a proposal covariance from an EXISTING run's
  samples, so it has nothing to do until a run has written some. Not a defect.

  If you need the covariance from the PRE-RETUNE run, it is preserved under
  chains/_archive_dyad_prefix_20260728_2140/ and can be pointed at by editing
  CHAINS/BASE above.
""")
        print("=" * 74)
        return
    names, rows = load(path)
    if not rows:
        print(f"  no samples in {path}")
        return

    # Only the SAMPLED parameters belong in a proposal covariance. The chain file
    # also carries derived quantities, and including them makes the matrix
    # rank-deficient (35 columns against a few hundred samples). Take the sampled
    # list from the seed covmat's own header, which is authoritative.
    seed = os.path.join(CHAINS, "_seed_covmats_20260728", f"{BASE}.covmat")
    with open(seed) as fh:
        sampled = fh.readline().lstrip("#").split()
    allnames = names[2:]
    pnames = [p for p in sampled if p in allnames]
    idx = [allnames.index(p) for p in pnames]
    print(f"  sampled parameters taken from the seed covmat header: {len(pnames)}"
          f" (chain file carries {len(allnames)} columns incl. derived)")

    start = int(len(rows) * BURN_FRAC)
    use = rows[start:]
    wts = [r[0] for r in use]
    cols = [[r[2 + j] for r in use] for j in idx]

    print("=" * 74)
    print("  RESEED CANDIDATE — built from the rank that found the good basin")
    print("=" * 74)
    print(f"  source     : {os.path.basename(path)}  (best -logpost 1377.89)")
    print(f"  samples    : {len(rows)} total, using {len(use)} after {int(BURN_FRAC*100)}% burn-in")
    print(f"  parameters : {len(pnames)}")

    mu, C = cov(cols, wts)

    print("\n  CONTROL: is the matrix usable as a proposal?")
    ok = cholesky_ok(C)
    print(f"    positive-definite (Cholesky): {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("    -> NOT WRITTEN. A non-PD matrix cannot seed a proposal.")
        return

    print(f"\n  {'parameter':<16} {'mean':>13} {'sd':>13}")
    for k, nm in enumerate(pnames):
        print(f"  {nm:<16} {mu[k]:13.6g} {math.sqrt(C[k][k]):13.6g}")

    # ---- the scale question, stated not hidden ---------------------------
    print("\n  ON SCALING — stated explicitly rather than folded in:")
    print("    Measured acceptance is 5.3-6.2% against a ~25% optimum, and the seed")
    print("    covariance's MARGINAL widths already match this rank's empirical spread")
    print("    (ratios 0.77-1.13). Widths are therefore not the fault; the correlation")
    print("    structure is, and that is exactly what this matrix supplies.")
    d = len(pnames)
    print(f"    d = {d}  ->  2.4/sqrt(d) = {2.4/math.sqrt(d):.4f}")
    print("    Recommended: seed with this matrix AND let learn_proposal re-tune,")
    print("    but ALSO raise learn_proposal_Rminus1_max_early so learning can")
    print("    engage before R-1 falls -- otherwise the same lock recurs.")

    with open(OUT, "w") as fh:
        fh.write("# " + " ".join(pnames) + "\n")
        for i in range(len(pnames)):
            fh.write(" ".join(f"{C[i][j]:.18e}" for j in range(len(pnames))) + "\n")
    print(f"\n  WRITTEN: {OUT}")
    print("  Nothing running was touched. Applying this is task #83, owner's call.")
    print("=" * 74)


if __name__ == "__main__":
    main()
