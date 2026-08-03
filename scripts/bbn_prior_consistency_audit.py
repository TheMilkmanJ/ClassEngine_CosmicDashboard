#!/usr/bin/env python3
"""BBN-prior consistency audit — does the sampler's deuterium law match the corpus's?

The PRTOE chains carry a Gaussian BBN prior on (omega_b, varying_me) with a D/H term

    D/H = 2.53e-5 * exp(-1.6*ln(omega_b/0.02236) + 0.4*(m_e-1)),  sigma = 0.030e-5

Three of those choices disagree with what the corpus states elsewhere:

  1. [RESOLVED IN THE SAMPLER'S FAVOUR] the exponent was flagged against the corpus's
     -1.83, but a direct wide omega_b scan through the production splice measures -1.66
     (scripts/prym_omega_b_elasticity.py). The -1.83 was a differencing artefact and is
     retired. The sampler's -1.6 is low by 4%, well inside the numerics floor. Kept as a
     variant below only to show how little the axis matters;
  2. sigma is the observational error alone, not the standing width +/-0.0476e-5 settled
     by #157 on 2026-07-21 (obs 0.030 (+) PRIMAT post-LUNA theory 0.037);
  3. the normalisation 2.53e-5 at the pivot is ~3% above what the production PRyM run
     reports for the same configuration (the standing prediction is 2.387e-5).

This script re-weights the existing posterior under corrected deuterium laws and reports
how far omega_b, H0 and m_e move. Importance weights are w * exp(logP_new - logP_old),
which is exact as long as the effective sample size stays healthy (reported per variant).

Usage:
  python3 scripts/bbn_prior_consistency_audit.py
  python3 scripts/bbn_prior_consistency_audit.py --chain chains/dyad_mnu_mcmc.1.txt
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CHAIN = ROOT / "chains" / "dyad_mnu_mcmc.1.txt"

PIVOT_OB = 0.02236          # the prior's omega_b pivot
LCDM_OMEGA_B = 0.022517     # cmp_lcdm.stats best fit (NB: control carries no BBN prior)

# --- the D/H term exactly as coded in the chain input yamls ---
DH_NORM_ASRUN = 2.53e-5     # normalisation at the pivot
DH_EXP_ASRUN = -1.6         # d ln(D/H) / d ln omega_b
DH_ME_ASRUN = 0.4           # d ln(D/H) / d(m_e - 1)
DH_OBS = 2.527e-5           # Cooke central
DH_SIG_ASRUN = 0.030e-5     # observational error alone

# --- what the corpus says ---
DH_EXP_CORPUS = -1.6667     # MEASURED: wide omega_b scan, prym_omega_b_elasticity.py
DH_SIG_SETTLED = 0.0476e-5  # #157 standing width: obs 0.030 (+) PRIMAT theory 0.037

# The pivot normalisation implied by the PRODUCTION PRyM run: the standing prediction is
# 2.387e-5 at the as-run posterior omega_b (0.022768) and m_e = 1.012543. Undoing the
# omega_b and m_e legs along the production exponent puts PRyM at 2.459e-5 at the pivot,
# i.e. 3.0% below the 2.53e-5 the sampler's prior assumes. That gap is the PRyM/PArthENoPE
# inter-code spread the corpus names as unfolded -- here it sits INSIDE the fit.
DH_NORM_PROD = 2.4467e-5

# --- the Y_p term (unchanged across variants) ---
YP_A, YP_B, YP_C = 0.2471, 0.0096, 0.17
YP_OBS, YP_SIG = 0.2449, 0.0040


def load_cobaya(path: Path):
    header = None
    rows = []
    with path.open() as f:
        for line in f:
            if line.startswith("#"):
                parts = line.lstrip("#").split()
                if "weight" in parts and "omega_b" in parts:
                    header = parts
                continue
            if line.strip():
                rows.append([float(x) for x in line.split()])
    if header is None:
        raise SystemExit(f"no cobaya header with weight/omega_b in {path}")
    return {name: i for i, name in enumerate(header)}, np.asarray(rows, float)


def wmean(w, x):
    return float(np.sum(w * x) / np.sum(w))


def wstd(w, x):
    m = wmean(w, x)
    return float(math.sqrt(np.sum(w * (x - m) ** 2) / np.sum(w)))


def dh_of(ob, me, norm, expo, me_coef):
    return norm * np.exp(expo * np.log(ob / PIVOT_OB) + me_coef * (me - 1.0))


def logp_bbn(ob, me, *, expo, sig, norm=DH_NORM_ASRUN, dh_on=True):
    """Log of the BBN prior. Y_p term always on; D/H term switchable."""
    yp = YP_A + YP_B * np.log(ob / PIVOT_OB) + YP_C * (me - 1.0)
    lp = -0.5 * ((yp - YP_OBS) / YP_SIG) ** 2
    if dh_on:
        dh = dh_of(ob, me, norm, expo, DH_ME_ASRUN)
        lp = lp - 0.5 * ((dh - DH_OBS) / sig) ** 2
    return lp


def ess(w):
    """Kish effective sample size."""
    return float(np.sum(w) ** 2 / np.sum(w ** 2))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chain", type=Path, default=DEFAULT_CHAIN)
    ap.add_argument("--burn-frac", type=float, default=1 / 3)
    args = ap.parse_args()

    idx, a = load_cobaya(args.chain)
    for k in ("weight", "omega_b", "varying_me", "H0"):
        if k not in idx:
            raise SystemExit(f"chain missing column {k}: {sorted(idx)}")

    a = a[int(len(a) * args.burn_frac):]
    w0 = a[:, idx["weight"]]
    ob = a[:, idx["omega_b"]]
    me = a[:, idx["varying_me"]]
    H0 = a[:, idx["H0"]]

    lp_asrun = logp_bbn(ob, me, expo=DH_EXP_ASRUN, sig=DH_SIG_ASRUN)

    variants = [
        ("as-run (exp -1.60, sig 0.030)",
         dict(expo=DH_EXP_ASRUN, sig=DH_SIG_ASRUN)),
        ("measured exponent (-1.667, sig 0.030)",
         dict(expo=DH_EXP_CORPUS, sig=DH_SIG_ASRUN)),
        ("settled width (exp -1.60, sig 0.0476)",
         dict(expo=DH_EXP_ASRUN, sig=DH_SIG_SETTLED)),
        ("both corrections (-1.667, sig 0.0476)",
         dict(expo=DH_EXP_CORPUS, sig=DH_SIG_SETTLED)),
        ("+ production norm (PRyM-consistent)",
         dict(expo=DH_EXP_CORPUS, sig=DH_SIG_SETTLED, norm=DH_NORM_PROD)),
        ("D/H term removed (CMB+BAO+SNe+Y_p only)",
         dict(expo=DH_EXP_CORPUS, sig=DH_SIG_SETTLED, dh_on=False)),
    ]

    print("=" * 78)
    print("BBN-PRIOR CONSISTENCY AUDIT — sampler's deuterium law vs the corpus's")
    print("=" * 78)
    print(f"chain: {args.chain}")
    print(f"samples after burn: {len(a)}  (sum w = {w0.sum():.0f}, ESS = {ess(w0):.0f})")
    print()
    print(f"{'variant':<40} {'omega_b':>10} {'%vsLCDM':>9} {'H0':>8} {'m_e-1 %':>9} {'ESS':>7}")
    print("-" * 78)

    base = None
    for name, kw in variants:
        lp_new = logp_bbn(ob, me, **kw)
        d = lp_new - lp_asrun
        w = w0 * np.exp(d - d.max())
        row = (wmean(w, ob), 100.0 * (wmean(w, ob) / LCDM_OMEGA_B - 1.0),
               wmean(w, H0), 100.0 * (wmean(w, me) - 1.0), ess(w))
        if base is None:
            base = row
        print(f"{name:<40} {row[0]:>10.6f} {row[1]:>+9.3f} {row[2]:>8.3f} "
              f"{row[3]:>9.3f} {row[4]:>7.0f}")

    print()
    print("READING THE D/H CONSEQUENCE (production-law exponent -1.667, normalised to the")
    print("standing prediction 2.387e-5 at the as-run posterior omega_b):")
    ob_asrun = base[0]
    for name, kw in variants:
        lp_new = logp_bbn(ob, me, **kw)
        d = lp_new - lp_asrun
        w = w0 * np.exp(d - d.max())
        ob_v = wmean(w, ob)
        # rescale the standing 2.387 prediction along the production exponent
        dh = 2.387 * (ob_v / ob_asrun) ** DH_EXP_CORPUS
        sig_row = (2.527 - dh) / 0.0476
        print(f"  {name:<40} D/H = {dh:.3f}e-5   {-sig_row:+.2f} sigma (width 0.0476)")

    print()
    print("NOTE: the prior's own normalisation (2.53e-5 at the pivot) predicts")
    print(f"  D/H = {dh_of(ob_asrun, 1.012543, DH_NORM_ASRUN, DH_EXP_ASRUN, DH_ME_ASRUN)*1e5:.3f}e-5 "
          f"at the as-run posterior, against the production PRyM value 2.387e-5")
    print("  — a ~3% inter-code offset between the sampler's BBN law and the production run.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
