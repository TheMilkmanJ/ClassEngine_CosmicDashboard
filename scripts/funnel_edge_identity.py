#!/usr/bin/env python3
"""
THE FUNNEL-EDGE IDENTITY: the registered lightest-neutrino mass m_1 = rho_Lambda^(1/4)
(P-2026-012) coincides with the 0vbb funnel's lower edge -- the smallest m_1 at which
the effective Majorana mass m_bb can vanish -- to half a percent at current oscillation
centrals. Verified by a 5-agent workflow 2026-08-02 (adversarial verifier: 5/5 CONFIRMED).

--------------------------------------------------------------------------------------
THE OBJECT

m_bb = | t1 + t2 e^{i a21} + t3 e^{i a31} | with free Majorana phases a21, a31, where
  t1 = c12^2 c13^2 m1,   t2 = s12^2 c13^2 m2,   t3 = s13^2 m3,
  m2 = sqrt(m1^2 + dm21), m3 = sqrt(m1^2 + dm31).
The MARGIN M(m1) = t2 - t1 - t3 decides the geometry: M > 0 -> the three phasors cannot
close and m_bb has a floor; M <= 0 -> m_bb = 0 is reachable (the "funnel", normal
ordering only). The funnel's lower edge m1* solves M(m1*) = 0.

The paper (papers/neutrino-mbb) sits at M(2.25 meV) = +0.045 meV on its own stated
parameters -- a floor of 0.04 meV -- while NuFIT 5.0 centrals give M = -0.0002 meV.
The sign of M is a 50/50 coin on today's oscillation errors. THIS SCRIPT establishes
what the coin toss actually is: the question of whether m_1 sits above or below m1*,
and the fact that m1*(NuFIT central) - rho_Lambda^(1/4) = 0.010 meV (0.5%, 0.04 sigma).
No literature statement of this coincidence was found (3 searches, null; the dedicated
funnel papers arXiv:2308.09737 and 2603.06787 never mention the dark-energy scale).

PRE-STATED CONTROLS (workflow-verified targets; each must reproduce or the run FAILS):
  F-A  margin at the paper's parameters      = +0.0448 meV
  F-B  margin at NuFIT 5.0 NO centrals       = -0.00022 meV  (the sign FLIPS)
  F-C  funnel edge m1*: NuFIT 2.2496 meV, paper-parameters 2.3245 meV
  F-D  sigma(m1*) today = 0.239 meV, s12^2 dominant (0.225 of it)
  F-E  rho_Lambda^(1/4) = 2.2395 +/- 0.0108 meV (Planck 2018, reduced Planck mass)
  F-F  the identity gap m1* - rho_L^(1/4) = +0.0102 meV = 0.043 sigma(m1*)
  F-G  JUNO era (s12^2, dm21 -> 0.5%/0.3%; dm31 -> 0.2%; theta13 unchanged):
       sigma(m1*) = 0.063 meV with THETA13 the bottleneck (0.055 of it) -- and no
       experiment improves theta13 this decade (Daya Bay final stands), so the
       identity test floors at ~3% and the coin, if the true |M| < ~0.04 meV,
       stays uncalled even post-JUNO.
  F-H  closure phases: on the edge, m_bb = 0 forces (a21, a31) = (pi, 0) exactly --
       BOTH Majorana phases at CP-conserving values (grid minimum at 180deg, 0deg).
  F-I  ANTI-CONTROL: at the paper's own (rounded) parameters the edge sits 0.085 meV
       ABOVE rho_L^(1/4) -- the identity is a statement at measured centrals and is
       parameter-sensitive; it must NOT be reported as parameter-independent.
"""

import numpy as np
from scipy.optimize import brentq

_fail = []
def chk(name, cond, detail=""):
    if not cond: _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))

# parameter sets: (s12sq, s13sq, dm21 [eV^2], dm31 [eV^2])
PAPER = (0.307, 0.022, 7.42e-5, 2.51e-3)
NUFIT = (0.304, 0.02221, 7.42e-5, 2.517e-3)
SIG   = (0.0125, 0.00065, 0.21e-5, 0.027e-3)          # NuFIT 5.0 1-sigma
M1 = 2.25e-3                                           # eV, the hypothesis

def terms(m1, p):
    s12, s13, d21, d31 = p
    m2, m3 = np.sqrt(m1**2 + d21), np.sqrt(m1**2 + d31)
    c13 = 1 - s13
    return (1 - s12) * c13 * m1, s12 * c13 * m2, s13 * m3

def margin(m1, p):
    t1, t2, t3 = terms(m1, p)
    return t2 - t1 - t3

def edge(p):
    return brentq(lambda m: margin(m, p), 0.5e-3, 8e-3)

def sigma_edge(p, sig):
    base = edge(p); parts = {}
    names = ('s12sq', 's13sq', 'dm21', 'dm31')
    for i, (n, s) in enumerate(zip(names, sig)):
        q = list(p); q[i] += s
        parts[n] = abs(edge(tuple(q)) - base)
    return np.sqrt(sum(v * v for v in parts.values())), parts

def main():
    print("=" * 78)
    print("  THE FUNNEL-EDGE IDENTITY")
    print("=" * 78)

    mp, mn = margin(M1, PAPER) * 1e3, margin(M1, NUFIT) * 1e3
    print(f"\n  margin M(2.25 meV): paper {mp:+.4f} meV   NuFIT {mn:+.5f} meV")
    chk("F-A  paper margin +0.0448", abs(mp - 0.0448) < 0.001)
    chk("F-B  NuFIT margin -0.00022, sign flipped", abs(mn + 0.00022) < 0.0005 and mp * mn < 0)

    ep, en = edge(PAPER) * 1e3, edge(NUFIT) * 1e3
    print(f"  funnel edge m1*:    paper {ep:.4f} meV    NuFIT {en:.4f} meV")
    chk("F-C  edges 2.3245 / 2.2496", abs(ep - 2.3245) < 0.002 and abs(en - 2.2496) < 0.002)

    s_now, parts = sigma_edge(NUFIT, SIG)
    s_now *= 1e3
    print(f"  sigma(m1*) today = {s_now:.4f} meV   parts: " +
          ", ".join(f"{k} {v*1e3:.4f}" for k, v in parts.items()))
    chk("F-D  0.239 meV, s12sq dominant", abs(s_now - 0.239) < 0.012
        and parts['s12sq'] == max(parts.values()))

    # rho_Lambda^(1/4), Planck 2018: Omega_L = 0.6847(73), H0 = 67.36(54)
    OL, sOL, H0, sH0 = 0.6847, 0.0073, 67.36, 0.54
    Mpl = 1.220890e19 / np.sqrt(8 * np.pi) * 1e9          # reduced Planck mass, eV
    h_ev = lambda H: H * 1e3 / 3.0856776e22 * 6.5821196e-16   # km/s/Mpc -> eV
    rL4 = lambda O, H: (O * 3 * h_ev(H)**2 * Mpl**2) ** 0.25 * 1e3   # meV
    r = rL4(OL, H0)
    sr = np.sqrt((rL4(OL + sOL, H0) - r)**2 + (rL4(OL, H0 + sH0) - r)**2)
    print(f"\n  rho_Lambda^(1/4) = {r:.4f} +/- {sr:.4f} meV")
    chk("F-E  2.2395 +/- 0.0108", abs(r - 2.2395) < 0.002 and abs(sr - 0.0108) < 0.001)

    gap = en - r
    print(f"  IDENTITY GAP m1* - rho_L^(1/4) = {gap:+.4f} meV = {100*gap/r:.2f}% = {gap/s_now:.3f} sigma")
    chk("F-F  +0.0102 meV, 0.04 sigma", abs(gap - 0.0102) < 0.002 and abs(gap / s_now) < 0.1)

    JUNO = (0.005 * 0.304, SIG[1], 0.003 * 7.42e-5, 0.002 * 2.517e-3)
    s_j, pj = sigma_edge(NUFIT, JUNO)
    s_j *= 1e3
    print(f"\n  JUNO-era sigma(m1*) = {s_j:.4f} meV   parts: " +
          ", ".join(f"{k} {v*1e3:.4f}" for k, v in pj.items()))
    chk("F-G  0.063 meV, theta13 bottleneck", abs(s_j - 0.0625) < 0.004
        and pj['s13sq'] == max(pj.values()))

    # closure phases on the edge
    t1, t2, t3 = terms(edge(NUFIT), NUFIT)
    a = np.linspace(0, 2 * np.pi, 721)
    A21, A31 = np.meshgrid(a, a, indexing='ij')
    mbb = np.abs(t1 + t2 * np.exp(1j * A21) + t3 * np.exp(1j * A31))
    i, j = np.unravel_index(np.argmin(mbb), mbb.shape)
    print(f"\n  phase-grid minimum at (a21, a31) = ({np.degrees(a[i]):.1f}, {np.degrees(a[j]):.1f}) deg,"
          f"  m_bb = {mbb[i, j]*1e3:.2e} meV")
    chk("F-H  minimum exactly at (180, 0), CP-conserving, m_bb = 0",
        abs(np.degrees(a[i]) - 180) < 0.5 and min(np.degrees(a[j]), 360 - np.degrees(a[j])) < 0.5
        and mbb[i, j] * 1e3 < 1e-6)

    chk("F-I  ANTI-CONTROL: paper-parameter edge sits well off rho_L^(1/4)",
        abs(ep - r) > 5 * sr, f"gap {ep - r:+.4f} meV -- the identity lives at measured centrals only")

    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
    else:
        print("  ALL CONTROLS PASS")
        print("=" * 78)
        print(f"""
  WHAT THIS ESTABLISHES. The coin toss on the m_bb floor's existence is the question
  "does m_1 sit above or below the funnel edge m1*?", and the registered m_1 lands ON
  the edge: m1* = {en:.4f} meV against rho_Lambda^(1/4) = {r:.4f} meV -- {100*gap/r:.2f}%, with no
  published statement of the coincidence found. Three ways the coin stops:
    1. DATA -- JUNO (<0.5% on theta12/dm21 by ~2031-32) shrinks sigma(m1*) to
       {s_j:.3f} meV, but theta13 then gates it and nothing improves theta13 this
       decade; if the true |M| < ~0.04 meV the coin stays uncalled.
    2. CLOSURE MECHANISM (m_ee = 0: FGM texture classes A1/A2, symmetry-protected,
       normal-ordering-only, m_lightest pinned to the funnel) -- marries the corpus's
       "the floor SETS m_1" operator to make the identity exact, pins BOTH Majorana
       phases CP-conserving at (pi, 0), and predicts m_bb = |M| <~ 0.05 meV: NO
       observable signal, INVERTING the paper's discriminating band into a falsifier.
       Cost: the corpus's own constitution calls flavor structure "not writable".
    3. FLOOR MECHANISM (minimal seesaw m1 = 0; most mass sum rules) -- protects the
       floor but requires m1 = 0, contradicting P-2026-012 outright.
""")

if __name__ == '__main__':
    main()
