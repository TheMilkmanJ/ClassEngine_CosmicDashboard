#!/usr/bin/env python3
"""Measure d ln(D/H) / d ln omega_b directly from the production PRyM splice.

WHY THIS EXISTS. The corpus carried d ln(D/H)/d ln omega_b = -1.83, sourced to "the
production run" and used to argue that the textbook -1.6 "understates the sensitivity by
14%". That number was never measured. It was obtained by dividing two BOOKED, ROUNDED D/H
values across the 1.1% omega_b step:

    log(2.372 / 2.420) / log(1.011) = -1.83

Running the production splice at those two points (m_e = 1, T_c = 0.179, numba on) gives
2.373576 and 2.416372. Redoing the same short-baseline difference on those freshly run values
gives -1.61, not -1.83.

WHY THE DIFFERENCING IS UNSOUND. PRyM is bit-for-bit DETERMINISTIC -- repeat runs agree to every
digit -- but its D/H output is NOT SMOOTH in omega_b at the ~0.1% level:

  wide-scan log-log fit residuals              ~1e-3
  a 0.071% omega_b step (0.022517 -> 0.022533) returns an apparent slope of -0.34, not -1.66

Across a 1.1% baseline that non-smoothness alone puts +/-0.15 of scatter on a differenced slope.
That, not any physics, is where -1.83 came from.

THE CONFIGURATION IS VERIFIED AND THE BOOKED ROWS STAND. The triple was made at eps = 1.24% and
T_c = 0.179 -- what bbn_witness documents. Y_p settles it, being far less exposed to the D/H
non-smoothness: the windowed run reproduces Y_p to 0.0004% at that config, against 0.013% at the
re-pinned 177.10 keV. D/H then reproduces to 0.072% and the LCDM control to 0.15%, inside a few
times the solver's own resolution. Nothing is re-booked.

WHAT THIS MEASURES. A wide (6%) omega_b scan at fixed everything-else, fitted in log-log --
a 6x longer lever arm, so the same non-smoothness costs ~3% instead of ~18%. Recorded results,
`prym_ramped_splice.py <shift> 0.179 <wb_scale>`, PRyM pivot 0.02230, NUMBA ON:

  m_e = 1                      m_e = 1.012543 (the model's window)
  wb_scale   D/H x1e5          wb_scale   D/H x1e5
  0.990000   2.500205          0.990000   2.517427
  1.009731   2.416372          1.000000   2.473914
  1.020987   2.373576          1.020987   2.391439
  1.040000   2.305208          1.041000   2.314555
  1.060000   2.230914          1.051000   2.276533

  m_e = 1        : global slope -1.6560, local at the model's omega_b -1.6582
  m_e = 1.012543 : global slope -1.6743, local at the model's omega_b -1.6751
  max log-log fit residual 9.5e-4 -- a clean power law, near-independent of the window.

STANDING VALUE: d ln(D/H)/d ln omega_b = -1.66. The textbook -1.6 was right to within 4%;
the sampler's BBN prior, which codes -1.6, is fine on this axis. A parallel numba-OFF scan
gives -1.64, so the numerics floor on the exponent is ~1.5%.

NUMBA MATTERS. PRyM's numba_flag accelerates the PRyM_thermo integrals and shifts D/H at the
~0.1-0.2% level -- the same size as its non-smoothness in omega_b. Production is numba ON. If the
env's numpy is ahead of numba, prym_ramped_splice.py now falls back to pure numpy rather than
failing; results from that path are cross-checks, not production numbers.

Also recorded here: production PRyM at the prior's own pivot (omega_b = 0.02230, m_e = 1) is
D/H = 2.459e-5, against the 2.53e-5 the chains' BBN prior assumes -- a 2.9% normalisation
offset (the PRyM/PArthENoPE inter-code spread, sitting inside the fit).

Usage:
  python3 scripts/prym_omega_b_elasticity.py            # refit the recorded scan
  python3 scripts/prym_omega_b_elasticity.py --rerun    # re-run PRyM (about 10 min, 10 runs)
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SPLICE = ROOT / "scripts" / "prym_ramped_splice.py"
PIVOT = 0.02230          # PRyM's default Omegabh2
TC = 0.179               # the as-run T_c the booked numbers were made at
MODEL_OB = 0.022768      # the model's omega_b (chain posterior mean)

RECORDED = {          # numba ON -- the production path
    1.0: [(0.990000, 2.500205), (1.009731, 2.416372), (1.020987, 2.373576),
          (1.040000, 2.305208), (1.060000, 2.230914)],
    1.012543: [(0.990000, 2.517427), (1.000000, 2.473914), (1.020987, 2.391439),
               (1.041000, 2.314555), (1.051000, 2.276533)],
}


def run_scan(shift, scales):
    out = []
    for s in scales:
        r = subprocess.run([sys.executable, str(SPLICE), str(shift), str(TC), str(s)],
                           capture_output=True, text=True)
        line = [ln for ln in r.stdout.splitlines() if ln.startswith("RAMPED")]
        if not line:
            raise SystemExit(f"splice produced no RAMPED line for scale {s}:\n{r.stderr[-800:]}")
        out.append((s, float(line[0].split()[8])))
        print(f"  scale {s:.4f} -> D/H = {out[-1][1]:.6f}e-5", flush=True)
    return out


def fit(points):
    s = np.array([p[0] for p in points])
    d = np.array([p[1] for p in points])
    x, y = np.log(PIVOT * s), np.log(d)
    p1 = np.polyfit(x, y, 1)
    p2 = np.polyfit(x, y, 2)
    local = 2 * p2[0] * np.log(MODEL_OB) + p2[1]
    resid = float(np.abs(y - np.polyval(p1, x)).max())
    return float(p1[0]), float(local), resid, p1


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rerun", action="store_true", help="re-run PRyM instead of refitting")
    args = ap.parse_args()

    print("=" * 72)
    print("d ln(D/H) / d ln omega_b FROM THE PRODUCTION PRyM SPLICE")
    print("=" * 72)

    results = {}
    for shift, pts in RECORDED.items():
        if args.rerun:
            print(f"\nre-running m_e shift = {shift} ...")
            pts = run_scan(shift, [p[0] for p in pts])
        results[shift] = fit(pts)
        g, loc, res, p1 = results[shift]
        print(f"\n  m_e shift = {shift}")
        print(f"    global log-log slope        : {g:+.4f}")
        print(f"    local slope at omega_b={MODEL_OB} : {loc:+.4f}")
        print(f"    max fit residual            : {res:.2e}")
        print(f"    D/H at the prior pivot {PIVOT} : "
              f"{np.exp(np.polyval(p1, np.log(PIVOT))):.4f}e-5")

    slopes = [results[k][1] for k in results]
    print()
    print(f"STANDING EXPONENT: {np.mean(slopes):+.3f}  "
          f"(m_e-independent to {abs(slopes[0]-slopes[1]):.4f})")
    print()
    print("THE RETIRED -1.83, reproduced as the booking artefact it was:")
    print(f"  log(2.372/2.420)/log(1.011)                 = "
          f"{np.log(2.372/2.420)/np.log(1.011):+.3f}   <- booked, rounded")
    print(f"  log(2.373576/2.416372)/log(0.022768/0.022517) = "
          f"{np.log(2.373576/2.416372)/np.log(0.022768/0.022517):+.3f}   <- same step, true values")
    print(f"  wide-baseline fit                            = "
          f"{np.mean(slopes):+.3f}   <- the measurement")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
