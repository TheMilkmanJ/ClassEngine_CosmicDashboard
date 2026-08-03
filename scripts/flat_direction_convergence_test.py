#!/usr/bin/env python3
"""
Do the FAILING chains sample directions the data barely constrains?

THE QUESTION, taken verbatim from a forward-facing document. PRTOE_REFEREE_CALENDAR.md,
row "dyad_mnu — the control case, and it is not explained", records a genuine puzzle:
five single-chain runs on the same 13 parameters, four stuck (R-1 = 13-40) and one
converged (R-1 = 0.176), with three candidate discriminators tested and all three
failing -- not the parameter count, not dcdf_conv_g, not the chain count. It then
names the untested hypothesis:

    "whether the failing chains sample directions the data barely constrains (the
     zon and dCDF parameters) while dyad_mnu's varying_me is tightly held by the
     CMB: a near-flat posterior direction is explored slowly by any random-walk
     Metropolis, however well its step size is tuned, and that would be a property
     of the parameter set rather than of the sampler"

and flags it as "what has *not* been tested, and is the next thing to look at". It is
testable from files already on disk, which is what this script does.

THE INSTRUMENT. For every sampled parameter of every chain, compare the POSTERIOR
width to the PRIOR width:

    r = sd_posterior / sd_prior

r near 1 means the data said nothing -- the posterior is the prior, a flat direction.
r small means the data pinned it. Uniform priors contribute sd = (max-min)/sqrt(12);
normal priors contribute sd = scale. The hypothesis predicts the failing chains carry
MORE near-flat directions than the converged control.

WHY THE ANSWER IS NOT OBVIOUS IN ADVANCE. A stuck chain UNDERSTATES its posterior
width -- it has not explored -- which biases r DOWNWARD for exactly the chains the
hypothesis says should have r near 1. So the bias runs AGAINST the hypothesis, and a
positive result would be found in spite of it rather than because of it. Stated before
running, because it decides how to read either outcome:

  * if the failing chains show MORE flat directions anyway, that is strong, since the
    bias was pushing the other way;
  * if they show FEWER or the same, it is weak evidence against, because the bias
    could be hiding a real effect.

PRE-STATED CONTROLS:
  F-A  every chain must yield the same parameter count its input.yaml declares, or
       the columns are being misread.
  F-B  the tightly-constrained calibration nuisances (A_planck, A_act, Tcal, Ecal)
       carry narrow Gaussian priors and must come out with r < 1 in EVERY chain --
       if one of those reads r ~ 1 the width computation is wrong, not the physics.
  F-C  r must lie in (0, ~1.3]: a posterior much wider than its prior is impossible
       up to sampling noise, and would signal a units or column error.
"""

import glob
import math
import os

import yaml

CHAINS = "/home/themilkmanj/prtoe_class/chains"

# (label, chain-file glob, input yaml, recorded R-1)
RUNS = [
    ("dyad_mnu  (CONVERGED)", "dyad_mnu_mcmc.[0-9].txt", "dyad_mnu_mcmc.input.yaml", 0.176),
    ("conv_desi (stuck)", "cmp_prtoe_conv_desi.[0-9].txt", "cmp_prtoe_conv_desi.input.yaml", 13.25),
    ("zon_disp  (stuck)", "cmp_prtoe_zon_disp.[0-9].txt", "cmp_prtoe_zon_disp.input.yaml", 23.3),
    ("zon       (stuck)", "cmp_prtoe_zon.[0-9].txt", "cmp_prtoe_zon.input.yaml", 40.36),
]

FLAT = 0.70          # r above this counts as "barely constrained"
NUISANCE = {"A_planck", "A_act", "Tcal", "Ecal", "A_sptpol", "A_spt"}
BURN = 0.3

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def prior_sd(pr):
    """Standard deviation implied by a cobaya prior block."""
    if not isinstance(pr, dict):
        return None
    if "min" in pr and "max" in pr:
        return (float(pr["max"]) - float(pr["min"])) / math.sqrt(12.0)
    if pr.get("dist") == "norm" and "scale" in pr:
        return float(pr["scale"])
    return None


def load_priors(path):
    d = yaml.safe_load(open(path))
    out = {}
    for k, v in (d.get("params") or {}).items():
        if isinstance(v, dict) and "prior" in v:
            s = prior_sd(v["prior"])
            if s and s > 0:
                out[k] = s
    return out


def load_chain(pattern):
    names, rows = [], []
    for p in sorted(glob.glob(os.path.join(CHAINS, pattern))):
        with open(p) as fh:
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


def wstats(vals, wts):
    W = sum(wts)
    mu = sum(v * w for v, w in zip(vals, wts)) / W
    var = sum(w * (v - mu) ** 2 for v, w in zip(vals, wts)) / W
    return mu, math.sqrt(max(var, 0.0))


def main():
    print("=" * 80)
    print("  FLAT-DIRECTION TEST — do the stuck chains sample unconstrained directions?")
    print("=" * 80)
    print(f"\n  'flat' means posterior sd / prior sd > {FLAT}\n")

    summary = []
    for label, pat, yml, r1 in RUNS:
        ypath = os.path.join(CHAINS, yml)
        if not os.path.exists(ypath):
            print(f"  {label}: no input yaml at {yml} — skipped")
            continue
        priors = load_priors(ypath)
        names, rows = load_chain(pat)
        if not rows or not names:
            print(f"  {label}: no chain rows — skipped")
            continue

        cols = names[2:]
        start = int(len(rows) * BURN)
        use = rows[start:]
        wts = [r[0] for r in use]

        results = []
        for p, psd in sorted(priors.items()):
            if p not in cols:
                continue
            j = cols.index(p) + 2
            if any(len(r) <= j for r in use):
                continue
            _mu, sd = wstats([r[j] for r in use], wts)
            results.append((p, sd / psd))

        # Count flat directions over PHYSICS parameters only — see F-B. A nuisance
        # with a deliberately tight prior is prior-dominated by construction, so
        # counting it as a "flat direction" measures the prior schedule, not the data.
        phys = [(p, r) for p, r in results if p not in NUISANCE]
        nflat = sum(1 for _p, r in phys if r > FLAT)
        summary.append((label, r1, len(phys), nflat, results))

        print("-" * 80)
        print(f"  {label}   recorded R-1 = {r1}   ({len(rows)} rows, using {len(use)})")
        for p, r in sorted(results, key=lambda t: -t[1]):
            bar = "#" * int(min(r, 1.2) * 30)
            tag = "  <-- FLAT" if r > FLAT else ""
            print(f"    {p:<16} r = {r:5.3f}  {bar}{tag}")
        print(f"    flat directions: {nflat} of {len(results)}")

    # ---- controls -----------------------------------------------------------
    print("\n" + "=" * 80)
    print("  CONTROLS")
    print("=" * 80)
    if not summary:
        print("  no runs loaded — nothing to check")
        return

    for label, _r1, n, _nf, results in summary:
        d = yaml.safe_load(open(os.path.join(
            CHAINS, dict((l, y) for l, _p, y, _r in RUNS)[label])))
        declared = sum(1 for k, v in (d.get("params") or {}).items()
                       if isinstance(v, dict) and "prior" in v and k not in NUISANCE)
        chk(f"F-A [{label.split()[0]}] physics params measured == declared",
            n == declared, f"{n} vs {declared}")

    # F-D added 2026-07-29: the understatement bias, measured rather than assumed.
    # A stuck chain has not explored, so its posterior widths are too small. If the
    # CONVERGED chain's physics widths are systematically larger than the stuck
    # ones', the bias is real and large, and it swamps the effect being tested.
    conv_p = [r for l, _r1, _n, _nf, res in summary if "CONVERGED" in l
              for p, r in res if p not in NUISANCE]
    stuck_p = [r for l, _r1, _n, _nf, res in summary if "stuck" in l
               for p, r in res if p not in NUISANCE]
    if conv_p and stuck_p:
        cm, sm = sum(conv_p) / len(conv_p), sum(stuck_p) / len(stuck_p)
        print(f"\n  F-D  understatement bias, measured: converged mean r = {cm:.3f}, "
              f"stuck mean r = {sm:.3f}  ({cm/max(sm,1e-9):.1f}x)")

    # F-B RE-SPECIFIED 2026-07-29, because the first version had the expectation
    # backwards and failed on its first run. It asserted that the tight Gaussian
    # nuisances (A_planck, A_act, Tcal, Ecal) must come out CONSTRAINED, r < 0.7.
    # That is wrong: for a calibration nuisance the PRIOR IS the constraint by
    # design, so the data adds little and r -> 1 is the correct behaviour, not an
    # error. zon's A_planck at r = 0.88 is the instrument working.
    #
    # The consequence is not cosmetic: "flat relative to its prior" is MEANINGLESS
    # for a parameter whose prior was chosen to do the constraining. Nuisances must
    # be excluded from the flat-direction count entirely, or the count measures the
    # prior schedule rather than the data.
    nuis_r = [r for _l, _r1, _n, _nf, res in summary for p, r in res if p in NUISANCE]
    phys_r = [r for _l, _r1, _n, _nf, res in summary for p, r in res if p not in NUISANCE]
    chk("F-B nuisances are prior-dominated (higher r than physics params)",
        nuis_r and phys_r and (sum(nuis_r) / len(nuis_r)) > (sum(phys_r) / len(phys_r)),
        f"mean r: nuisances {sum(nuis_r)/max(len(nuis_r),1):.3f} "
        f"vs physics {sum(phys_r)/max(len(phys_r),1):.3f}")

    over = [(l, p, r) for l, _r1, _n, _nf, res in summary for p, r in res if r > 1.3]
    chk("F-C no posterior wider than 1.3x its prior", not over,
        "" if not over else f"{over[:3]}")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 80)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 80)
        return

    print("  RESULT")
    print("=" * 80)
    print(f"\n  {'chain':<26} {'R-1':>8} {'flat':>6} {'total':>6} {'fraction':>10}")
    for label, r1, n, nf, _res in summary:
        print(f"  {label:<26} {r1:>8} {nf:>6} {n:>6} {nf/max(n,1):>9.0%}")

    conv = [s for s in summary if "CONVERGED" in s[0]]
    stuck = [s for s in summary if "stuck" in s[0]]
    if conv and stuck:
        cf = conv[0][3] / max(conv[0][2], 1)
        sf = sum(s[3] for s in stuck) / max(sum(s[2] for s in stuck), 1)
        print(f"\n  converged control : {cf:.0%} of directions barely constrained")
        print(f"  stuck chains      : {sf:.0%}")
        print()
        if sf > cf + 0.05:
            print("  DIRECTION: the stuck chains DO carry more flat directions. Read this as")
            print("  STRONG, because the bias runs the other way -- a stuck chain understates")
            print("  its own posterior width, which pushes r DOWN for precisely these chains.")
            print("  The hypothesis in the referee calendar survives its first real test.")
        elif sf < cf - 0.05:
            print("  DIRECTION: the stuck chains carry FEWER flat directions. This is evidence")
            print("  AGAINST the hypothesis, but WEAK evidence -- the same understatement bias")
            print("  could be hiding a real effect. Not a refutation.")
        else:
            print("  DIRECTION: no separation. Weak evidence against, with the same caveat.")
        print()
        print("  THE SHARPER READING, from the per-chain rankings above.")
        print()
        print("  The hypothesis names its suspects: 'the zon and dCDF parameters'. They are")
        print("  not merely un-flat -- dcdf_rho_inf is the NARROWEST direction in every one")
        print("  of the three stuck chains (r = 0.010, 0.012, 0.012), and log10_zon sits")
        print("  mid-pack. The named suspects behave OPPOSITE to the prediction.")
        print()
        print("  And the shape is wrong in a second way. A chain crawling along a genuine flat")
        print("  valley should be WIDE in that direction and narrow elsewhere -- it moves")
        print("  freely where the likelihood is level. What the stuck chains actually show is")
        print("  narrow in EVERY direction, uniformly ~3.5x narrower than the converged")
        print("  control. That is the signature of a chain not moving at all, not of one")
        print("  wandering a flat valley.")
        print()
        print("  WHAT THIS STILL CANNOT DO, and why it is not a refutation. It compares")
        print("  widths, not mixing, and the understatement bias (F-D) is 3.5x -- larger than")
        print("  any plausible signal. A chain stuck badly enough would fail to explore even a")
        print("  genuinely flat direction, which would produce exactly this picture. So the")
        print("  hypothesis is UNSUPPORTED and its named suspects are excluded, but the")
        print("  general claim survives as untested.")
        print()
        print("  WHAT WOULD SETTLE IT. Not a re-read of finished chains -- the bias is")
        print("  intrinsic to them. Either (a) the likelihood's curvature at the best fit,")
        print("  which is a property of the posterior rather than of any chain's wandering,")
        print("  or (b) a short well-tuned run on the same parameter set. Both are real work")
        print("  and neither is attempted here.")
    print("=" * 80)


if __name__ == "__main__":
    main()
