"""Do the charged and neutrino rings' amplitudes stand in a simple ratio, and is it robust?

The charged ring has A^2 = 6Q - 2 = 2 at Q = 2/3. The neutrino triple has its own Q, fixed once
the lightest mass is -- and the corpus fixes it, at m1 = 2.25 meV, the dark-energy scale
rho_Lambda^(1/4). So A_nu is not free either, and the ratio of the two amplitudes is a number the
corpus already determines without having looked at it.

The lead: A^2/A_nu^2 appears to land on 8/3. That would make A_nu^2 = 3/4 against the charged
ring's 2. Before believing it, the question is whether Q_nu is stable enough for the coincidence
to mean anything -- the splittings carry ~1-2% errors and Q_nu may be steep in them.

This script computes the ratio and, more importantly, its error budget.

Run: python3 scripts/two_ring_amplitude_ratio.py
"""
import math

# PDG/NuFIT normal ordering, with 1-sigma
DM21, DM21_E = 7.53e-5, 0.18e-5
DM31, DM31_E = 2.53e-3, 0.03e-3
M1 = 2.25e-3            # the corpus's lightest mass = rho_Lambda^(1/4)
RHO_E = 0.01e-3         # a generous 0.5% on the DE scale


def Q_nu(m1, d21=DM21, d31=DM31):
    m2, m3 = math.sqrt(m1*m1 + d21), math.sqrt(m1*m1 + d31)
    return (m1 + m2 + m3) / (math.sqrt(m1) + math.sqrt(m2) + math.sqrt(m3))**2


def A2(Q):
    return 6*Q - 2


q = Q_nu(M1)
print("=" * 74)
print("THE TWO RINGS")
print("=" * 74)
print(f"  charged:  Q = 2/3          A^2 = {A2(2/3):.6f}")
print(f"  neutrino: Q = {q:.6f}   A^2 = {A2(q):.6f}   (at m1 = {M1*1e3:.2f} meV)")
print()
print(f"  ratio A^2/A_nu^2 = {A2(2/3)/A2(q):.6f}")
print(f"  8/3              = {8/3:.6f}")
print(f"  miss             = {abs(A2(2/3)/A2(q)/(8/3) - 1)*1e6:.1f} ppm")
print()
print(f"  equivalently A_nu^2 = {A2(q):.6f} against 3/4 = 0.750000"
      f"   ({abs(A2(q)/0.75 - 1)*1e6:.1f} ppm)")
print(f"  equivalently Q_nu   = {q:.7f} against 11/24 = {11/24:.7f}"
      f"   ({abs(q/(11/24) - 1)*1e6:.1f} ppm)")

print()
print("=" * 74)
print("IS IT ROBUST? THE ERROR BUDGET")
print("=" * 74)


def dQ(par, val, err):
    kw = {"d21": DM21, "d31": DM31}
    if par == "m1":
        return (Q_nu(M1 + err) - Q_nu(M1 - err)) / 2
    kw[par] = val + err
    hi = Q_nu(M1, **kw)
    kw[par] = val - err
    lo = Q_nu(M1, **kw)
    return (hi - lo) / 2


parts = (("m1 (= rho_Lambda^1/4)", M1, RHO_E),
         ("Dm21^2", DM21, DM21_E),
         ("Dm31^2", DM31, DM31_E))
tot = 0.0
print(f"  {'input':<24} {'1-sigma':>12} {'-> dQ_nu':>12} {'in ppm of Q':>13}")
print("  " + "-" * 66)
for name, val, err in parts:
    d = dQ("m1" if name.startswith("m1") else ("d21" if "21" in name else "d31"), val, err)
    tot += d*d
    print(f"  {name:<24} {err:12.3e} {d:12.3e} {abs(d)/q*1e6:12.0f}")
tot = math.sqrt(tot)
print("  " + "-" * 66)
print(f"  {'combined':<24} {'':>12} {tot:12.3e} {tot/q*1e6:12.0f}")

print()
print(f"  the 11/24 miss is {abs(q - 11/24):.3e}; the input error is {tot:.3e}")
print(f"  ratio: the coincidence sits {abs(q - 11/24)/tot:.3f} sigma from exact")

print()
print("=" * 74)
print("VERDICT")
print("=" * 74)
if tot/q*1e6 > 1000:
    print(f"  Q_nu carries {tot/q*1e6:.0f} ppm of input error. Landing within"
          f" {abs(q/(11/24)-1)*1e6:.0f} ppm of 11/24")
    print("  is therefore NOT a precision coincidence -- the target is wider than the miss by")
    print(f"  a factor {tot/abs(q - 11/24):.0f}, so any nearby simple fraction would also 'fit'.")
    print()
    print("  What survives is weaker and still worth stating: A_nu^2 is near 3/4 and A^2 is 2,")
    print("  so the two rings' amplitudes are near a 8:3 ratio. That is a target for a")
    print("  mechanism, not evidence of one, and it cannot be sharpened without the splittings")
    print("  and the lightest mass to a part in 1e5 -- which no experiment offers.")
else:
    print("  the coincidence is tighter than the input error and deserves a mechanism hunt")
