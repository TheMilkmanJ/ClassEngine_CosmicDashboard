#!/usr/bin/env python3
"""
Rank separation, measured in HONEST standard errors.

WHY THIS EXISTS (2026-07-29, written while the model chain still had zero
post-re-tune samples on disk).

`scripts/rank_basin_diagnostic.py` reports per-parameter rank separation in
"standard errors", computing

    se = sd / sqrt(neff),   with   neff = len(vals)

i.e. it treats every stored MCMC sample as independent. They are not. Markov
chain samples are autocorrelated, so the effective sample size is

    N_eff = N / tau_int          (tau_int = integrated autocorrelation time)

and tau_int is routinely 5-50 for cosmological chains. Using N in place of
N_eff UNDERSTATES the standard error by sqrt(tau_int) and therefore INFLATES
every z-score by the same factor.

This matters beyond bookkeeping:

  * the claim "ranks separated by up to 23,855 standard errors" appears in
    reader-facing documents and in a letter;
  * a TRAPPED chain has a much longer autocorrelation time than a healthy one,
    so the inflation is WORSE for the model chain than for the reference — the
    two quoted numbers are not even inflated by the same factor, and their
    ratio is not safe either.

A second, smaller inconsistency in the original: the mean and sd are WEIGHTED
(wmean/wstd) but the count is the raw row count. For these runs the weights sit
near 1 so it is a minor effect, but it is still weighted moments paired with an
unweighted count.

WHAT THIS CHANGES: exactly one thing — the effective sample size. The statistic
compared (each rank's mean against the pooled mean, in units of that rank's own
standard error) is deliberately IDENTICAL to the original, so any difference in
the output is attributable to the ESS fix alone and to nothing else.

PRE-STATED CONTROL: tau_int >= 1 always, so the corrected z must be LESS THAN OR
EQUAL TO the naive z for every parameter. If any corrected z exceeds its naive
counterpart, tau_int came out below 1 — that is anti-correlation or a bug, and
the run must be rejected rather than reported.
"""

import glob
import math
import os

CHAINS = "/home/themilkmanj/prtoe_class/chains"
BASES = ["cmp_lcdm_mnu_bbnfix", "dyad_mnu_bbnfix"]
MAX_EXPAND = 500_000      # refuse to expand a weighted chain beyond this
SECOND_HALF = True        # match the original instrument's convention


def read_rank(path):
    names, rows = [], []
    with open(path) as fh:
        for line in fh:
            if line.startswith("#"):
                if not names:
                    names = line.lstrip("#").split()
                continue
            try:
                rows.append([float(x) for x in line.split()])
            except ValueError:
                pass
    return names, rows


def expand(vals, wts):
    """Repeat each sample by its integer weight.

    Autocorrelation must be measured on the chain as the sampler actually
    walked it. A stored row with weight w means the walker sat there for w
    steps, and those repeats are the most correlated samples in the series --
    dropping them would bias tau_int DOWNWARD, i.e. back toward the very
    over-optimism this script exists to remove.
    """
    out = []
    for v, w in zip(vals, wts):
        n = int(round(w))
        if n < 1:
            n = 1
        out.extend([v] * n)
        if len(out) > MAX_EXPAND:
            return None
    return out


def tau_int(x):
    """Integrated autocorrelation time, Geyer initial-positive-sequence.

    Returns (tau, method_note). Guarded to tau >= 1.
    """
    n = len(x)
    if n < 16:
        return float("nan"), "too few samples"
    mu = sum(x) / n
    d = [v - mu for v in x]
    c0 = sum(v * v for v in d) / n
    if c0 <= 0:
        return 1.0, "zero variance (parameter is fixed)"

    maxlag = min(n // 3, 2000)

    def rho(k):
        return sum(d[i] * d[i + k] for i in range(n - k)) / (n * c0)

    # Geyer: pair consecutive lags, accumulate while the pair sum stays positive
    total = 0.0
    k = 0
    truncated = False
    while 2 * k + 1 <= maxlag:
        g = rho(2 * k) + rho(2 * k + 1)
        if g <= 0:
            break
        total += g
        k += 1
    else:
        truncated = True

    tau = -1.0 + 2.0 * total
    note = f"Geyer IPS, {k} pairs" + (" (HIT LAG CAP)" if truncated else "")
    return (max(tau, 1.0), note)


def analyse(base):
    paths = sorted(glob.glob(os.path.join(CHAINS, base + ".*.txt")))
    print("=" * 78)
    print(f"  {base}   ({len(paths)} rank file(s))")
    print("=" * 78)
    if not paths:
        print("  no chain files — nothing to measure (expected during burn-in).\n")
        return None

    ranks, names = [], []
    for p in paths:
        nm, rows = read_rank(p)
        if rows:
            ranks.append((os.path.basename(p), rows))
            if nm and not names:
                names = nm
    if len(ranks) < 2:
        print("  fewer than two ranks with samples — separation is undefined.\n")
        return None

    # Grading condition 2 of the #84 pre-registration: matched sample count.
    shortest = min(len(rows) for _f, rows in ranks)
    print(f"  truncating all ranks to the shortest: {shortest} rows"
          f"  (raw: {[len(r) for _f, r in ranks]})")
    ranks = [(f, rows[:shortest]) for f, rows in ranks]

    if not names or len(names) < 3:
        print("  no usable parameter header.\n")
        return None

    npar = min(len(names), min(len(rows[0]) for _f, rows in ranks))
    print(f"\n  {'parameter':<20} {'naive z':>9} {'tau_int':>9} {'N_eff':>9}"
          f" {'HONEST z':>10}   {'inflation':>9}")
    print("  " + "-" * 74)

    worst_naive = worst_hon = 0.0
    worst_par = ""
    control_violations = []

    for j in range(2, min(npar, 10)):
        mus, se_naive, se_hon, taus, neffs = [], [], [], [], []
        bad = False
        for _fn, rows in ranks:
            half = len(rows) // 2 if SECOND_HALF else 0
            vals = [r[j] for r in rows[half:]]
            wts = [r[0] for r in rows[half:]]
            W = sum(wts)
            if W <= 0 or len(vals) < 16:
                bad = True
                break
            mu = sum(v * w for v, w in zip(vals, wts)) / W
            var = sum(w * (v - mu) ** 2 for v, w in zip(vals, wts)) / W
            sd = math.sqrt(max(var, 0.0))

            ser = expand(vals, wts)
            if ser is None:
                bad = True
                break
            t, _note = tau_int(ser)
            if math.isnan(t):
                bad = True
                break
            neff = max(len(ser) / t, 1.0)

            mus.append(mu)
            taus.append(t)
            neffs.append(neff)
            se_naive.append(sd / math.sqrt(len(vals)) if sd > 0 else float("nan"))
            se_hon.append(sd / math.sqrt(neff) if sd > 0 else float("nan"))
        if bad or not mus:
            print(f"  {names[j]:<20}   (not measurable)")
            continue

        pooled = sum(mus) / len(mus)

        def maxz(ses):
            zs = [abs(m - pooled) / s for m, s in zip(mus, ses)
                  if s and s > 0 and not math.isnan(s)]
            return max(zs) if zs else float("nan")

        zn, zh = maxz(se_naive), maxz(se_hon)
        tbar = sum(taus) / len(taus)
        nbar = sum(neffs) / len(neffs)
        infl = zn / zh if zh and zh > 0 and not math.isnan(zh) else float("nan")

        if not math.isnan(zh) and not math.isnan(zn) and zh > zn * 1.0001:
            control_violations.append((names[j], zn, zh))

        if not math.isnan(zn) and zn > worst_naive:
            worst_naive = zn
        if not math.isnan(zh) and zh > worst_hon:
            worst_hon, worst_par = zh, names[j]

        print(f"  {names[j]:<20} {zn:9.1f} {tbar:9.1f} {nbar:9.1f} {zh:10.1f}"
              f"   {infl:8.1f}x")

    print("  " + "-" * 74)
    print(f"  WORST separation, naive  : {worst_naive:10.1f} s.e.")
    print(f"  WORST separation, HONEST : {worst_hon:10.1f} s.e.   (on {worst_par})")
    if worst_hon > 0:
        print(f"  the naive figure is inflated by {worst_naive/worst_hon:.1f}x")

    print("\n  CONTROL (tau_int >= 1, so honest z must not exceed naive z):")
    if control_violations:
        print("    *** VIOLATED — rejecting this run ***")
        for nm, zn, zh in control_violations:
            print(f"      {nm}: naive {zn:.2f} < honest {zh:.2f}")
    else:
        print("    PASS — every parameter's honest z is at or below its naive z.")
    print()
    return {"naive": worst_naive, "honest": worst_hon, "par": worst_par}


def main():
    print()
    print("  RANK SEPARATION IN HONEST STANDARD ERRORS")
    print("  (autocorrelation-corrected effective sample size)")
    print()
    out = {}
    for b in BASES:
        out[b] = analyse(b)

    print("=" * 78)
    print("  WHAT THIS DOES AND DOES NOT CHANGE")
    print("=" * 78)
    print("""
  The corrected figures are the defensible ones. Any statement quoting rank
  separation in standard errors should use the HONEST column, and any document
  carrying the naive number needs re-grading -- not because the direction of the
  conclusion changes (ranks that disagree by hundreds of honest s.e. still
  disagree) but because the magnitude was overstated and the overstatement is
  not uniform across chains.

  The #84 pass/fail bands were fixed in NAIVE units, before any post-re-tune
  sample existed. They are therefore still internally consistent and are NOT
  being moved here. This script reports both columns so the same run can be
  graded against the pre-registered bands AND described honestly.
""")
    print("=" * 78)


if __name__ == "__main__":
    main()
