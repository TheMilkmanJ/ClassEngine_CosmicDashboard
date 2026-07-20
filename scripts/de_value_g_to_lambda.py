#!/usr/bin/env python3
"""Task #169 — the g -> lambda map: the composite quartic from the NJL sector.

WHAT WAS MISSING. The Lee-Huang-Yang correction to the dark-energy condensation
energy is DERIVED as a coefficient (Delta E / E_MF = 0.0084 * lambda) but had no
number, because lambda -- the composite scalar's quartic -- was never mapped from
the NJL four-fermion coupling. That is why the dark-energy value's SIZE books
ESTIMATE (cosmological_constant.md:326; the tribunal's Row 4,
Thermal_O1_Discussions.md:734-737).

THE CONVENTION, NAMED FIRST (the corpus's own trap, _AUDIT_LEDGER.md:1122-1126).
The tribunal's Lagrangian is L = |d phi|^2 - m^2|phi|^2 - lambda|phi|^4 for a
COMPLEX phi (Thermal_O1_Discussions.md:84), whose Mexican-hat depth is
(mu^2-m^2)^2/4 lambda (:87). Writing phi = (sigma + i pi)/sqrt(2) turns that into
V = (lambda/4)(sigma^2+pi^2)^2 -- exactly the linear-sigma-model normalization
V = (lambda/4)(phi^2 - v^2)^2 with m_sigma^2 = 2 lambda f^2. So

    lambda = m_sigma^2 / (2 f^2)                                    [tribunal units]

which is the corpus's Frame 2 form (cosmological_constant.md:334) in the SAME
convention as the 0.0084 coefficient. No factor is floating.

THE MAP. Two standard NJL results close it with no new input:
  - chiral limit:  m_sigma = 2M  (M = constituent mass)   => lambda = 2M^2/f^2
  - one loop, 3-momentum cutoff (the SAME regulator the corpus's gap equation
    uses, de_value_gap_equation.py):
        f^2 = N_c M^2 F(y) / (2 pi^2),
        F(y) = ln((1+sqrt(1+y^2))/y) - 1/sqrt(1+y^2),   y = M/Lambda
  The M^2 CANCELS:

    ****  lambda = 4 pi^2 / (N_c * F(M/Lambda))  ****

  so the quartic depends on nothing but the colour count and the cutoff-to-
  constituent-mass ratio -- and that ratio is fixed by g through the gap equation.

THE CHAIN, ALL BOOKED INPUTS:
    tau = T_c/Lambda = (1/2)ln2      (cosmological_constant.md:98)
      -> g = 1/I(tau)                (de_value_gap_equation.py, g_c = 2)
      -> y = M/Lambda from 1 = g J(y)
      -> lambda = 4 pi^2 / (N_c F(y)),  N_c = 2 (dark SU(2), str[k1] = 0)

VALIDATION: the same f^2 formula run on QCD (N_c = 3, M = 336, Lambda = 631 MeV)
returns f = 93.1 MeV against the physical 92.4 -- 0.7%. The map is not a guess.

Run: python3 scripts/de_value_g_to_lambda.py
"""
import math

ALPHA = 1 / 137.035999084
AC    = 3 * ALPHA
ME    = 511.0e3          # eV, the portal: sqrt(sigma_dark) = m_e
TAU   = 0.5 * math.log(2)          # T_c/m_e, cosmological_constant.md:98
NC_DARK = 2                        # dark SU(2), N_f = 3


def I_tc(tau, n=200000):
    """T_c gap kernel, int_0^1 x tanh(x/2 tau) dx  (de_value_gap_equation.py)."""
    h = 1.0 / n
    return sum(((i + 0.5) * h) * math.tanh(((i + 0.5) * h) / (2 * tau))
               for i in range(n)) * h


def J(y):
    """T = 0 gap kernel, int_0^1 x^2 dx / sqrt(x^2+y^2).  J(0) = 1/2 -> g_c = 2."""
    s = math.sqrt(1 + y * y)
    return 0.5 * s - 0.5 * y * y * math.log((1 + s) / y)


def F(y):
    """f^2 loop, int_0^1 x^2 dx / (x^2+y^2)^{3/2}."""
    s = math.sqrt(1 + y * y)
    return math.log((1 + s) / y) - 1 / s


def y_of_g(g):
    """Solve 1 = g J(y) for y = M/Lambda by bisection."""
    lo, hi = 1e-9, 50.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if g * J(mid) > 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def lam_of(y, nc):
    return 4 * math.pi ** 2 / (nc * F(y))


def main():
    print("=" * 72)
    print("#169  the g -> lambda map: the composite quartic from the NJL sector")
    print("=" * 72)

    # --- validation on QCD -------------------------------------------------
    M_q, L_q, fq_obs = 336.0, 631.0, 92.4      # MeV, standard NJL parameter set
    y_q = M_q / L_q
    f_q = math.sqrt(3 * M_q ** 2 * F(y_q) / (2 * math.pi ** 2))
    print("\n(0) VALIDATION — the same one-loop f^2 on QCD")
    print(f"  N_c=3, M={M_q:.0f} MeV, Lambda={L_q:.0f} MeV -> y={y_q:.4f}, F={F(y_q):.5f}")
    print(f"  f_pi predicted = {f_q:.2f} MeV   vs physical {fq_obs:.1f} MeV "
          f"({100*(f_q/fq_obs-1):+.1f}%)")
    print(f"  lambda_QCD = 4pi^2/(3 F) = {lam_of(y_q,3):.2f}"
          f"   [corpus quotes 'QCD calibration 22.8'; M=312 MeV gives"
          f" {lam_of(312/L_q,3):.1f}]")

    # --- the dark chain ----------------------------------------------------
    I0 = I_tc(TAU)
    g = 1 / I0
    y = y_of_g(g)
    lam = lam_of(y, NC_DARK)
    f_over_root_sigma = math.sqrt(NC_DARK * y ** 2 * F(y) / (2 * math.pi ** 2))
    print("\n(1) THE DARK CHAIN — every input already booked")
    print(f"  tau = T_c/Lambda = (1/2)ln2       = {TAU:.6f}")
    print(f"  I(tau)                            = {I0:.6f}")
    print(f"  g = 1/I(tau)                      = {g:.4f}   (g_c = 2; corpus quotes ~2.8)")
    print(f"  y = M/Lambda   from 1 = g J(y)    = {y:.5f}")
    print(f"  M = y * m_e                       = {y*ME/1e3:.1f} keV "
          f"  [de_value_derive_Lambda_g.py's BCS check: {TAU*ME/0.567/1e3:.0f} keV]")
    print(f"  M/T_c                             = {y/TAU:.3f}   (BCS weak-coupling 1.764)")
    print(f"  F(y)                              = {F(y):.5f}")
    print(f"  f/sqrt(sigma) predicted           = {f_over_root_sigma:.4f}"
          f"   [corpus's QCD-transfer band 0.19-0.25]")
    print(f"\n  ****  lambda = 4 pi^2 / (N_c F) = {lam:.2f}   (N_c = 2)  ****")
    print(f"  the naive identification lambda <- g = {g:.1f} is low by "
          f"{lam/g:.0f}x — it equates a four-fermion coupling with a bosonic quartic")

    # --- systematics, calibrated on QCD ------------------------------------
    # The scheme cancels in the RATIO: lambda_dark/lambda_QCD = (3/2)(F_QCD/F_dark),
    # so anchor on QCD, where lambda is known from measured m_sigma and f_pi. The
    # dominant systematic is the NJL sigma mass: leading order gives m_sigma = 2M,
    # but the physical scalar (f_0(500)) sits well below 2M -- a known NJL failing.
    transfer = (3 / NC_DARK) * (F(y_q) / F(y))
    print("\n(2) SYSTEMATICS — the scheme cancels in the QCD-calibrated ratio")
    print(f"  lambda_dark/lambda_QCD = (3/N_c)(F_QCD/F_dark) = {transfer:.4f}")
    print(f"  {'QCD anchor for m_sigma':34s} {'lambda_QCD':>11s} {'-> lambda_dark':>15s}")
    band = []
    for lbl, msig in [("physical f_0(500), 500 MeV", 500.0),
                      ("600 MeV", 600.0),
                      ("NJL leading order 2M = 672 MeV", 2 * M_q)]:
        lq = msig ** 2 / (2 * fq_obs ** 2)
        band.append(lq * transfer)
        print(f"  {lbl:34s} {lq:11.1f} {lq*transfer:15.1f}")
    band = (min(band), max(band))
    print(f"\n  ****  lambda_dark = {band[0]:.0f} - {band[1]:.0f}, central "
          f"{0.5*(band[0]+band[1]):.0f}  ****")
    print(f"  (the direct 3D-cutoff evaluation, {lam:.1f}, sits at the band's top —")
    print(f"   it is the m_sigma = 2M reading, the same one QCD says runs high)")

    # --- the control edge --------------------------------------------------
    print("\n(3) AGAINST THE CONTROL EDGE lambda* (Thermal_O1_Discussions.md:487-498)")
    rt = math.sqrt(AC / (256 * math.pi ** 3))
    def ratio(l):
        na3 = (rt * l) ** 2
        lhy = (128 / (15 * math.sqrt(math.pi))) * math.sqrt(na3)
        wu = 8 * (4 * math.pi / 3 - math.sqrt(3)) * na3 * math.log(na3)
        return abs(wu) / lhy
    lo, hi = 1.0, 200.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if ratio(mid) < 1.0:
            lo = mid
        else:
            hi = mid
    lstar = 0.5 * (lo + hi)
    print(f"  lambda* (|Wu| = LHY) = {lstar:.2f}   [booked 22.41]")
    print(f"  {'lambda':>10s} {'sqrt(na^3)':>12s} {'|Wu|/LHY':>10s}  verdict")
    for l in (band[0], 0.5 * (band[0] + band[1]), band[1]):
        print(f"  {l:10.1f} {rt*l:12.4f} {ratio(l):10.2f}"
              f"  {'UNCONTROLLED' if l > lstar else 'controlled'}")
    print(f"  -> the WHOLE band is above lambda* = {lstar:.1f}"
          f" ({band[0]/lstar:.1f}x to {band[1]/lstar:.1f}x). No reading lands controlled.")

    # --- the numbers the size would have had -------------------------------
    print("\n(4) THE SIZE THE SERIES WOULD GIVE (formal — the series is past control)")
    for l in (band[0], 0.5 * (band[0] + band[1]), band[1]):
        print(f"  lambda = {l:6.1f}:  Delta E/E_MF = {0.0084*l*100:6.2f} %"
              f"   Delta rho^1/4/rho^1/4 = {0.0021*l*100:5.2f} %")
    print("  (the flagship's own gap over the observation is +0.44%, so a band this")
    print("   wide swamps it — the precision claim, not the existence claim, is what dies)")
    print("=" * 72)


if __name__ == "__main__":
    main()
