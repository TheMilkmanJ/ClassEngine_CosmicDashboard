"""#146's residue, measured: how precisely must the basement dope exactly one node pair?

Hierarchy section 6c derives k = ln(1 + 1/b)/pi from Thomas-Fermi screening, and lists four
conditions on the host. Two of them concern the screening constant:

  condition 4   N_screen = 2 N_0 -- exactly two of the 48 Weyl species carry finite density
  condition 3   v = 1            -- the band velocity equals the medium's gauge-field speed

The file writes b = 2 alpha_c/(pi v) under one and b = N alpha_c/(pi v) under the other, and
counts them as two separate unmet asks. They are not separable: b depends on N and v ONLY
through their ratio, so the two conditions are one relation, N = 2v.

This script (1) checks that degeneracy on the corpus's own formulas, (2) calibrates the anchor
response against the three sensitivity numbers section 6c already records, and (3) puts a fence
on N/v -- the tolerance the docket has never carried.

Run: python3 scripts/basement_screening_fence.py
"""
import math

# alpha_c is fixed by the booked screening constant itself: b = 2 alpha_c/pi at v = 1.
B_BOOKED = 0.0139369
K_BOOKED = 1.36461191
ALPHA_C = B_BOOKED * math.pi / 2


def b_of(N, v):
    """The screening constant. m_D^2 = e^2 N N_0, N_0 = k_F^2/(pi^2 v), e^2 = 4 pi alpha_c,
    b = m_D^2/(4 k_F^2)  ->  b = N alpha_c/(pi v)."""
    return N * ALPHA_C / (math.pi * v)


def k_of(N, v):
    return math.log(1 + 1 / b_of(N, v)) / math.pi


def dlnM(N, v):
    """Log shift of the anchor relative to the booked point. The anchor is exponential in
    the pairing coupling, lambda = k alpha_c, so ln M carries -1/(k alpha_c)."""
    return 1 / (K_BOOKED * ALPHA_C) - 1 / (k_of(N, v) * ALPHA_C)


print("=" * 76)
print("CALIBRATION -- reproduce what section 6c already records")
print("=" * 76)
print(f"  alpha_c from the booked b        {ALPHA_C:.6f}")
print(f"  k at (N, v) = (2, 1)             {k_of(2,1):.8f}   booked {K_BOOKED:.8f}")
print(f"  d lnM / d lnk = 1/(k alpha_c)    {1/(K_BOOKED*ALPHA_C):.2f}        booked 33.47")
print(f"  k at N = 1 (one band screening)  {k_of(1,1):.5f}      booked 1.58305")
print(f"    -> anchor moves by             x{math.exp(dlnM(1,1)):.1f}"
      f"       booked 1.6e5 GeV against a ~1.57 TeV anchor, i.e. x102")
print(f"  k at N = 24 (roster as Dirac)    {k_of(24,1):.5f}      booked 0.618")
print(f"    -> anchor moves by             x{math.exp(dlnM(24,1)):.1e}     booked ~1e-18")
print(f"  v = 0.9 at N = 2                 k = {k_of(2,0.9):.4f}     booked 1.3316")
print(f"    -> anchor moves by             x{math.exp(dlnM(2,0.9)):.2f}       booked 'about a factor two'")

print()
print("=" * 76)
print("(1) THE TWO CONDITIONS ARE ONE: b DEPENDS ONLY ON N/v")
print("=" * 76)
print(f"  {'N':>6} {'v':>6} {'N/v':>7} | {'b':>12} {'k':>12}")
print("  " + "-" * 50)
for N, v in ((2, 1.0), (4, 2.0), (1, 0.5), (6, 3.0), (3, 1.5)):
    print(f"  {N:6} {v:6.2f} {N/v:7.3f} | {b_of(N,v):12.8f} {k_of(N,v):12.8f}")
print()
print("  Every row is the booked point. So 'exactly two species doped' and 'v = 1' are not")
print("  two facts about the host -- they are one relation, N = 2v, and supplying either")
print("  alone reduces the debt by nothing. Section 6c counts them separately (three unmet,")
print("  one supplied); on its own formulas the screening pair is a single condition.")

print()
print("=" * 76)
print("(2) THE FENCE ON N/v")
print("=" * 76)


def solve_ratio(target_dlnM, lo, hi):
    """Find N/v giving the stated anchor shift, by bisection on the ratio."""
    f = lambda x: dlnM(x, 1.0) - target_dlnM
    flo = f(lo)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if flo * f(mid) <= 0:
            hi = mid
        else:
            lo, flo = mid, f(mid)
    return 0.5 * (lo + hi)


for name, tol in (("a factor 2", math.log(2)), ("a factor 10", math.log(10)),
                  ("a factor 100", math.log(100))):
    hi = solve_ratio(-tol, 2.0, 6.0)      # larger N/v -> smaller k -> smaller anchor
    lo = solve_ratio(+tol, 0.5, 2.0)
    print(f"  anchor within {name:<12}  N/v in [{lo:.4f}, {hi:.4f}]"
          f"   = 2 {(lo/2-1)*100:+.1f}% / {(hi/2-1)*100:+.1f}%")

print()
print("  So the ratio is fenced at roughly +-9% for factor-2 accuracy on the anchor. Among")
print("  INTEGER species counts at v = 1 there is no room at all:")
print()
print(f"  {'N':>4} | {'k':>10} | {'anchor vs booked':>18}")
print("  " + "-" * 40)
for N in (1, 2, 3, 4, 6):
    print(f"  {N:4} | {k_of(N,1):10.5f} | {'x%.3g' % math.exp(dlnM(N,1)):>18}")
print()
print("  N = 1 overshoots by two orders and N = 3 undershoots by one and a half, so the")
print("  count is not merely favoured, it is isolated. The tolerance the fence allows is")
print("  continuous room, and the only continuous variable in the ratio is v.")

print()
print("=" * 76)
print("(3) WHAT THIS DOES TO THE DOCKET")
print("=" * 76)
v_lo = 2 / solve_ratio(-math.log(2), 2.0, 6.0)
v_hi = 2 / solve_ratio(+math.log(2), 0.5, 2.0)
print(f"  Hold N = 2 and the fence reads v in [{v_lo:.4f}, {v_hi:.4f}] for factor-2 accuracy,")
print(f"  i.e. the band velocity must sit within {(1-v_lo)*100:.1f}% of the medium's gauge-field speed.")
print("  Section 6c argues that comes free -- a linear node IS a cone whose slope defines the")
print("  emergent light speed -- and on the degeneracy above that argument is doing more work")
print("  than it was credited with: it is what stops N and v trading off against each other.")
print()
print("  So the residue is one number and not two. If the cone argument holds, v = 1 is fixed")
print("  and the whole of #146 is 'why exactly one node pair is doped'. If it ever weakens,")
print("  N and v move together exactly, and a host with N = 4 would need v = 2 -- fermions")
print("  outrunning the medium's own gauge field, which is its own refutation. That is worth")
print("  recording: the degeneracy is not a loophole, because its far end is unphysical.")
