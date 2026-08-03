"""How badly do the two Koide watches actually disagree? The 452-sigma, in its own units.

The conjunction (A = sqrt2) AND (arg f1 = 2/9) is refuted by m_mu/m_e at 452 sigma. That
number is a statement about how well the muon-electron ratio is MEASURED (22 parts per
billion), not about how far apart the hypotheses are. Reported alone it reads as a sector
in ruins, which is not what the arithmetic says.

This script puts the disagreement in the sector's own variables. Each of the three
constraints is a curve in the (A, phi) plane:

    the data      m_mu/m_e = 206.768283, known to 2.2e-8   -- a razor-thin curve
    watch 1       A = sqrt2                                -- a horizontal line
    watch 2       phi = (1 + A^2/2)/9, the closure         -- a shallow parabola

If everything were exact all three would meet at one point. They do not; they bound a
small triangle, and the triangle's size is the honest measure of the disagreement.

Run: python3 scripts/koide_watch_triangle.py
"""
import math

ME, MMU, MTAU = 0.51099895000, 105.6583755, 1776.86
DME, DMMU = 0.00000000015, 0.0000023
TWOPI3 = 2 * math.pi / 3
A0, P0 = math.sqrt(2.0), 2.0 / 9
SEAT = {"tau": 0, "e": 1, "mu": 2}

RATIO = MMU / ME
DRATIO = RATIO * math.sqrt((DME / ME) ** 2 + (DMMU / MMU) ** 2)


def ratio_of(A, phi):
    """m_mu/m_e for the ring at (A, phi)."""
    r = {n: 1 + A * math.cos(phi + TWOPI3 * k) for n, k in SEAT.items()}
    return (r["mu"] / r["e"]) ** 2


def bisect(f, lo, hi, n=300):
    flo = f(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        if flo * f(mid) <= 0:
            hi = mid
        else:
            lo, flo = mid, f(mid)
    return 0.5 * (lo + hi)


def closure_phi(A):
    return (1.0 + A * A / 2.0) / 9.0


print("=" * 78)
print("THE THREE CONSTRAINTS AS CURVES IN THE (A, phi) PLANE")
print("=" * 78)
print(f"  measured m_mu/m_e      {RATIO:.9f} +- {DRATIO:.2e}   ({DRATIO/RATIO*1e9:.1f} ppb)")
print(f"  booked point (sqrt2, 2/9) gives  {ratio_of(A0, P0):.9f}")
print(f"  -> miss {abs(ratio_of(A0,P0)-RATIO)/RATIO*1e6:.2f} ppm ="
      f" {abs(ratio_of(A0,P0)-RATIO)/DRATIO:.0f} sigma  (cycle 8's headline)")
print()

# Vertex 1: the data curve meets the horizontal line A = sqrt2. Q is exact here; phi is not.
p1 = bisect(lambda p: ratio_of(A0, p) - RATIO, P0 - 1e-4, P0 + 1e-4)
# Vertex 2: the data curve meets the closure parabola. The closure is exact; Q is not.
a2 = bisect(lambda a: ratio_of(a, closure_phi(a)) - RATIO, A0 - 1e-4, A0 + 1e-4)
p2 = closure_phi(a2)
# Vertex 3: the two watches meet each other -- the corpus's booked point, off the data.
a3, p3 = A0, P0

print("=" * 78)
print("THE TRIANGLE: WHERE EACH PAIR OF CONSTRAINTS MEETS")
print("=" * 78)
print(f"  {'vertex':<34} {'A':>15} {'phi':>15}")
print("  " + "-" * 66)
print(f"  {'data x (A = sqrt2)':<34} {A0:15.10f} {p1:15.10f}")
print(f"  {'data x closure':<34} {a2:15.10f} {p2:15.10f}")
print(f"  {'(A = sqrt2) x closure  [booked]':<34} {a3:15.10f} {p3:15.10f}")
print()
print(f"  spread in A     {max(A0,a2,a3)-min(A0,a2,a3):.3e}   ({(max(A0,a2,a3)-min(A0,a2,a3))/A0*1e6:.3f} ppm)")
print(f"  spread in phi   {max(p1,p2,p3)-min(p1,p2,p3):.3e}   ({(max(p1,p2,p3)-min(p1,p2,p3))/P0*1e6:.3f} ppm)")

print()
print("=" * 78)
print("THE SAME DISAGREEMENT, ONE VARIABLE AT A TIME")
print("=" * 78)
Q2 = 1 / 3 + a2 * a2 / 6
print("  Grant the closure exactly, and let the light masses fix everything else:")
print(f"    Q      = {Q2:.12f}      Q - 2/3 = {Q2-2/3:+.3e}  ({abs(Q2-2/3)/(2/3)*1e6:.3f} ppm)")
print(f"    A      = {a2:.12f}      A - sqrt2 = {a2-A0:+.3e}")
print()
print("  Grant Q = 2/3 exactly instead, and do the same:")
print(f"    phi    = {p1:.12f}      phi - 2/9 = {p1-P0:+.3e}  ({abs(p1-P0)/P0*1e6:.3f} ppm)")
print()
print("  So the conjunction fails, and this is the size of the failure. Whichever watch")
print("  is granted, the other misses by well under one part per million. The 452 sigma")
print("  measures how sharply m_mu/m_e is known, not how badly the sector is broken --")
print(f"  a {abs(ratio_of(A0,P0)-RATIO)/RATIO*1e6:.1f} ppm discrepancy on a {DRATIO/RATIO*1e9:.0f} ppb measurement is unavoidably hundreds of sigma.")
print("  Both readings are correct and neither alone is the whole statement.")

print()
print("=" * 78)
print("WHY THE TAU CANNOT SEE ANY OF THIS")
print("=" * 78)


def koide(me, mmu, mt):
    s = [math.sqrt(me), math.sqrt(mmu), math.sqrt(mt)]
    M = sum(s) / 3
    Q = (me + mmu + mt) / sum(s) ** 2
    d = [x / M - 1 for x in s]
    c1 = (2 / 3) * sum(d[k] * math.cos(TWOPI3 * k) for k in range(3))
    s1 = -(2 / 3) * sum(d[k] * math.sin(TWOPI3 * k) for k in range(3))
    return Q, math.sqrt(6 * Q - 2), math.atan2(s1, c1) - TWOPI3


Qm, Am, phim = koide(ME, MMU, MTAU)
print(f"  the full three-mass point   A = {Am:.10f}   phi = {phim:.10f}")
print(f"  its distance from the triangle:  dA = {Am-A0:+.3e}   dphi = {phim-P0:+.3e}")
print(f"  the triangle's own size:         {max(A0,a2,a3)-min(A0,a2,a3):.3e} in A,"
      f" {max(p1,p2,p3)-min(p1,p2,p3):.3e} in phi")
print()
print(f"  The tau's +-0.12 MeV displaces the fitted point by {abs(Am-A0)/(max(A0,a2,a3)-min(A0,a2,a3)):.0f}x the triangle's width")
print("  in A. That is the whole reason both watches sit under 1 sigma on a three-mass")
print("  fit while their conjunction is dead on two: the tau's error bar is far larger")
print("  than the structure being argued about, so it hides the disagreement rather")
print("  than resolving it. Only the light masses can see the triangle at all.")
