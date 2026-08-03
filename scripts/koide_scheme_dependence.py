"""Which masses does the Koide sector's arithmetic refer to, and how much does it matter?

Every number in the sector -- Q, A = sqrt(6Q-2), the Brannen phase theta_B -- is read off
the POLE masses. The corpus records that ("verified on the pole masses to 1e-5") but has
never asked what the alternative would give, and two live commitments depend on the answer:

  * the joint claim (A = sqrt2 AND theta_B = 2/9) over-determines the spectrum, so it is
    testable on m_mu/m_e alone -- a ratio known to 2.2e-8, six orders better than m_tau;
  * the referee calendar stakes a discrimination between the two watches on measuring
    m_tau to 1.4 ppm.

Both are ppm-level claims. If the sector's arithmetic moves by more than that under an
equally defensible choice of mass definition, neither is supportable without an account
of why the pole masses are the right variables -- which is the standing Sumino problem
for Koide's relation and which the corpus does not currently address.

One-loop QED, on-shell to MS-bar:  mbar(mu) = m_pole * [1 - (alpha/pi)(3/4 * ln(mu^2/m^2) + 1)]

Run: python3 scripts/koide_scheme_dependence.py
"""
import math

ME, MMU, MTAU = 0.51099895000, 105.6583755, 1776.86
DME, DMMU, DMTAU = 0.00000000015, 0.0000023, 0.12
ALPHA = 1 / 137.035999084
TWOPI3 = 2 * math.pi / 3
SEAT = {"tau": 0, "e": 1, "mu": 2}


def koide(me, mmu, mtau):
    """(Q, A, theta_B) of the Z3 ring from three masses."""
    s = [math.sqrt(me), math.sqrt(mmu), math.sqrt(mtau)]
    M = sum(s) / 3
    Q = (me + mmu + mtau) / sum(s) ** 2
    d = [x / M - 1 for x in s]
    c1 = (2 / 3) * sum(d[k] * math.cos(TWOPI3 * k) for k in range(3))
    s1 = -(2 / 3) * sum(d[k] * math.sin(TWOPI3 * k) for k in range(3))
    return Q, math.sqrt(6 * Q - 2), math.atan2(s1, c1) - TWOPI3


def msbar(m_pole, mu):
    """One-loop QED on-shell -> MS-bar at scale mu."""
    return m_pole * (1 - (ALPHA / math.pi) * (0.75 * math.log(mu**2 / m_pole**2) + 1))


print("=" * 76)
print("PART 1 -- THE JOINT CLAIM IS OVER-DETERMINED, AND m_mu/m_e ALONE TESTS IT")
print("=" * 76)
print("  A = sqrt2 fixes the amplitude and says nothing about the phase; the closure")
print("  fixes the phase and says nothing about Q. Neither alone constrains m_mu/m_e.")
print("  Together they leave only an overall scale, so BOTH mass ratios are predicted.")
print()
A0, p0 = math.sqrt(2.0), 2.0 / 9
r = {n: 1 + A0 * math.cos(p0 + TWOPI3 * k) for n, k in SEAT.items()}
ratio_pred = (r["mu"] / r["e"]) ** 2
ratio_meas = MMU / ME
d_ratio = ratio_meas * math.sqrt((DME / ME) ** 2 + (DMMU / MMU) ** 2)
print(f"    predicted m_mu/m_e   {ratio_pred:.6f}")
print(f"    measured  m_mu/m_e   {ratio_meas:.6f} +- {d_ratio:.2e}"
      f"   ({d_ratio/ratio_meas*1e9:.1f} ppb)")
print(f"    miss                 {abs(ratio_pred/ratio_meas-1)*1e6:.1f} ppm"
      f"  = {abs(ratio_pred-ratio_meas)/d_ratio:.0f} sigma on the measurement")
print()
print("  So on pole masses AT MOST ONE of the two watches can be exact. This does not")
print("  need m_tau and no future m_tau measurement can change it.")

print()
print("=" * 76)
print("PART 2 -- HOW MUCH OF THAT IS THE CHOICE OF MASS DEFINITION?")
print("=" * 76)
Qp, Ap, thp = koide(ME, MMU, MTAU)
print(f"  pole masses:   Q = {Qp:.9f}   A - sqrt2 = {Ap-A0:+.3e}   theta_B - 2/9 = {thp-p0:+.3e}")
print()
print(f"  {'scale mu':>12} | {'Q':>12} | {'Q - 2/3':>11} | {'A - sqrt2':>11} | {'th_B - 2/9':>11}")
print("  " + "-" * 70)
rows = []
for label, mu in (("m_tau", MTAU), ("2 GeV", 2000.0), ("m_W", 80379.0), ("M_Z", 91187.6)):
    mm = [msbar(x, mu) for x in (ME, MMU, MTAU)]
    Qb, Ab, thb = koide(*mm)
    rows.append((label, Qb, Ab, thb))
    print(f"  {label:>12} | {Qb:12.9f} | {Qb-2/3:+11.3e} | {Ab-A0:+11.3e} | {thb-p0:+11.3e}")
print()
worst = max(rows, key=lambda t: abs(t[1] - 2 / 3))
shift = abs(worst[1] - Qp)
print(f"  Q moves by {shift:.3e} between the pole masses and MS-bar at {worst[0]},")
print(f"  i.e. {shift/(2/3)*1e6:.0f} ppm, against a pole-mass residual of {abs(Qp-2/3)/(2/3)*1e6:.1f} ppm.")
print(f"  The scheme choice is worth {shift/abs(Qp-2/3):.0f} times the deviation being measured.")

print()
print("=" * 76)
print("PART 3 -- WHAT THIS DOES TO THE PREREGISTERED m_tau DISCRIMINATION")
print("=" * 76)


def solve(g, lo=1770.0, hi=1785.0):
    for _ in range(200):
        mid = (lo + hi) / 2
        if g(lo) * g(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


mQ = solve(lambda m: koide(ME, MMU, m)[0] - 2 / 3)
mTH = solve(lambda m: koide(ME, MMU, m)[2] - 2 / 9)
print(f"  m_tau demanded by Q = 2/3        {mQ:.5f} MeV")
print(f"  m_tau demanded by theta_B = 2/9  {mTH:.5f} MeV")
print(f"  separation                       {(mQ-mTH)*1e3:.3f} keV = {(mQ-mTH)/MTAU*1e6:.3f} ppm")
print()
# Put the scheme shift and the separation in the same units. Q's lever on m_tau is
# analytic-grade central difference; no root solve, so nothing can rail on a bracket.
_h = 1e-4
dQ_dmtau = (koide(ME, MMU, MTAU + _h)[0] - koide(ME, MMU, MTAU - _h)[0]) / (2 * _h)
dQ_sep = abs(koide(ME, MMU, mQ)[0] - koide(ME, MMU, mTH)[0])
Q_scheme = abs(rows[-1][1] - Qp)
print(f"  the separation in Q:            {dQ_sep:.3e}")
print(f"  the scheme shift in Q:          {Q_scheme:.3e}   (pole -> MS-bar at M_Z)")
print(f"  ratio                           {Q_scheme/dQ_sep:.0f}x")
print()
print(f"  dQ/dm_tau = {dQ_dmtau:.3e} /MeV, so the scheme shift is worth")
print(f"    {Q_scheme/abs(dQ_dmtau):.1f} MeV of m_tau  --  against a separation of {(mQ-mTH)*1e3:.2f} keV.")
print()
print("  What this does NOT show: that the registered test fails to execute. Both watches")
print("  are stated on pole masses and the pole m_tau is measurable, so a 1.4 ppm")
print("  determination does separate them exactly as the calendar says. The test is sound.")
print()
print("  What it does show is a limit on what a win would buy. The two watches differ by")
print(f"  {dQ_sep:.2e} in Q while the choice of mass variable moves Q by {Q_scheme:.2e} -- {Q_scheme/dQ_sep:.0f} times more.")
print("  A framework that does not say why the pole masses are its variables cannot claim")
print("  its mechanism resolves structure at the smaller scale while the larger one is")
print("  unaccounted. So the m_tau measurement can decide WHICH watch matches the data;")
print("  it cannot, on its own, promote the winner's mechanism, because the same framework")
print("  silently fixes a much larger number by convention. Closing that is the same debt")
print("  that leaves Koide's relation unexplained, and it is now stated in the sector's")
print("  own units rather than left as a general worry about radiative corrections.")
print()
print("  Note which way this cuts on the sector's headline. It does not weaken the")
print(f"  pole-mass agreement, which stands at {abs(Qp-2/3)/(2/3)*1e6:.1f} ppm on Q and is the whole reason the")
print("  relation is interesting. It says the sector's claim is 'the POLE masses satisfy")
print("  this', that the mass definition is load-bearing at the 1e-3 level, and that it")
print("  therefore belongs in the statement of every watch rather than in a footnote.")
