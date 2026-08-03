#!/usr/bin/env python3
"""Emit a production-faithful BBN prior block for NEW chain configs.

PRTOE_deuterium_row.md §8 lists, among the things that change the D/H number without being a
fake cure: "a production-faithful D/H term in the joint likelihood -- the live chain's BBN prior
still uses a stale formula". This script is that term. It does not heal the row; it prices the
trade honestly.

THE AS-RUN PRIOR (every cmp_prtoe_* and dyad_* input yaml):

  Y_p = 0.2471  + 0.0096*ln(ob/0.02236) + 0.17*(m_e-1)          vs 0.2449 +/- 0.0040
  D/H = 2.53e-5 * exp(-1.6*ln(ob/0.02236) + 0.4*(m_e-1))        vs 2.527e-5 +/- 0.030e-5

Five of those constants were checked against the production network by wide scans (numba on;
scripts/prym_omega_b_elasticity.py and prym_supersession_pricing.py carry the data). Each is
measured over a baseline long enough to clear the solver's ~0.1% non-smoothness -- none is
differenced from a pair of runs.

  constant              as-run     measured    verdict
  --------------------  ---------  ----------  ------------------------------------------
  D/H exponent          -1.6       -1.656      FINE (3.4% low, inside the numerics floor)
  D/H m_e coefficient    0.4        0.4761     19% low
  D/H normalisation      2.53e-5    2.4467e-5  3.4% HIGH -- the big one
  D/H sigma              0.030e-5   0.0476e-5  observational only; #157 standing width
  Y_p normalisation      0.2471     0.24691    0.05 sigma high
  Y_p m_e coefficient    0.17       0.1632     4% high (fine)

THE ONE THAT MATTERS is the normalisation. At the pivot the prior believes production PRyM makes
D/H = 2.53e-5 when it makes 2.4467e-5. The prior therefore thinks the model sits 3.4% closer to
Cooke than it does, and under-penalises high omega_b throughout the fit. That 3.4% is the
PRyM/PArthENoPE inter-code spread the corpus names as an unfolded external systematic -- it has
been sitting INSIDE the likelihood the whole time.

The exponent is included for completeness only: the corpus's -1.83 was retired (a differencing
artefact) and the as-run -1.6 turns out to be right to 3.4%.

Usage:
  python3 scripts/bbn_prior_production_faithful.py          # print the yaml block
"""
from __future__ import annotations

PIVOT = 0.02236

# --- measured against the production network ---
DH_NORM = 2.4467e-5     # PRyM at the pivot, m_e = 1 (omega_b scan power law)
DH_EXP = -1.656         # d ln(D/H) / d ln omega_b
DH_ME = 0.4761          # d ln(D/H) / d(m_e - 1)
DH_SIG = 0.0476e-5      # #157 standing width: obs 0.030 (+) PRIMAT post-LUNA 0.037
DH_OBS = 2.527e-5       # Cooke

YP_NORM = 0.24691       # PRyM at the pivot, m_e = 1
YP_OB = 0.0096          # d Y_p / d ln omega_b (unchanged; weak and not re-measured)
YP_ME = 0.1632          # d Y_p / d(m_e - 1)
YP_SIG = 0.0040
YP_OBS = 0.2449         # Aver


def main():
    expr = (
        "lambda omega_b, varying_me: -0.5*( "
        f"(({YP_NORM} + {YP_OB}*__import__('numpy').log(omega_b/{PIVOT})"
        f" + {YP_ME}*(varying_me-1.0) - {YP_OBS})/{YP_SIG})**2"
        f" + (({DH_NORM:.6g}*__import__('numpy').exp({DH_EXP}*__import__('numpy')"
        f".log(omega_b/{PIVOT}) + {DH_ME}*(varying_me-1.0)) - {DH_OBS})/{DH_SIG})**2 )"
    )
    print("# production-faithful BBN prior -- paste into NEW chain configs.")
    print("# Do NOT retrofit completed runs; their yamls are records.")
    print("prior:")
    print(f"  bbn: '{expr}'")
    print()
    print("Sanity, at the standing point (omega_b = 0.022768, m_e = 1.012543):")
    import math
    ob, me = 0.022768, 1.012543
    dh = DH_NORM * math.exp(DH_EXP * math.log(ob / PIVOT) + DH_ME * (me - 1.0))
    yp = YP_NORM + YP_OB * math.log(ob / PIVOT) + YP_ME * (me - 1.0)
    old = 2.53e-5 * math.exp(-1.6 * math.log(ob / PIVOT) + 0.4 * (me - 1.0))
    print(f"  D/H  new prior {dh*1e5:.4f}e-5   ({(dh-DH_OBS)/DH_SIG:+.2f} sigma on the standing width)")
    print(f"       as-run     {old*1e5:.4f}e-5   ({(old-DH_OBS)/0.030e-5:+.2f} sigma on its obs-only width)")
    print(f"       production PRyM reports 2.387e-5 -- the new prior lands "
          f"{100*(dh*1e5/2.387-1):+.2f}% from it, the as-run one {100*(old*1e5/2.387-1):+.2f}%.")
    print(f"  Y_p  new prior {yp:.5f}    ({(yp-YP_OBS)/YP_SIG:+.2f} sigma vs Aver)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
