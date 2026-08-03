#!/usr/bin/env python3
"""
The expansion-energy ledger: Friedmann as +kinetic / -binding = 0, and local energy
conservation as the first law dU = -p dV. (JP's "what IS the expansion energy" chase.)

READ THIS FIRST -- the honest scope, so the result is not over-read:
  * This does NOT derive Friedmann anew. The Newtonian energy-balance route to
    H^2 = (8 pi G/3) rho is textbook and holds for ANY theory with a Newton's
    constant. Reproducing it is the MINIMUM bar (consistency), not a triumph.
  * What is PRTOE-specific is INTERPRETIVE, and it splits into a claim and a cost:
      - claim  : the medium gives the +kinetic/-binding ledger a LOCALIZABLE home
                 (the medium's own energy), where GR has only a non-localizable
                 pseudotensor. A localizable energy is a *candidate* for a
                 well-defined GLOBAL total -- which GR cannot provide.
      - cost   : a real medium has a rest frame -> a PREFERRED FRAME -> Lorentz
                 violation, tightly bounded (PRTOE_LV_pricing.md, ~27 orders of
                 suppression on the one live channel). Concreteness is bought with
                 a falsification exposure GR does not carry.
  * VERIFIED here: (1) the flat-universe ledger nets to zero at the Friedmann H;
    (2) local conservation -- the continuity equation IS dU = -p dV -- component by
    component. NOT shown here (the real payoff, still open): that the medium's
    GLOBAL total energy is constant. That needs the medium's own dynamics, and it
    is the actual thing worth building. Grade at the bottom.
"""
import math

G   = 6.674e-11          # Newton's constant (in this model, the INDUCED G)
_ok = []
def chk(name, got, exp, tol):
    good = abs(got - exp) <= tol * (1 + abs(exp)); _ok.append(good)
    print(f"  [{'ok' if good else 'FAIL'}] {name}: {got:.6g} vs {exp:.6g}")

# ============================================================ (1) the flat ledger
print("=" * 70)
print("(1) FRIEDMANN AS AN ENERGY LEDGER:  +kinetic  -binding  = 0  (flat)")
print("=" * 70)
# comoving sphere, physical radius r = a*chi, mass M = (4/3) pi r^3 rho, rdot = H r
#   kinetic per test mass = +1/2 rdot^2 = +1/2 H^2 r^2
#   binding per test mass = -G M / r    = -(4/3) pi G rho r^2
#   total E = 0 (flat)  <=>  1/2 H^2 = (4/3) pi G rho  <=>  H^2 = (8 pi G/3) rho
def H2_friedmann(rho): return 8 * math.pi * G / 3 * rho
def kinetic(H, r):     return 0.5 * H * H * r * r
def binding(rho, r):   return -(4.0/3.0) * math.pi * G * rho * r * r
rho, r = 8.5e-27, 3.0e25          # ~critical density (kg/m^3), a length (m)
H = math.sqrt(H2_friedmann(rho))
K, U = kinetic(H, r), binding(rho, r)
print(f"  rho = {rho:.2e} kg/m^3,  H = {H:.3e} 1/s  (= {H*3.086e19:.1f} km/s/Mpc)")
print(f"  kinetic  = {K:+.4e}")
print(f"  binding  = {U:+.4e}")
print(f"  E = K + U = {K+U:+.4e}   -> zero to machine precision = FLAT universe")
print("  So the Friedmann equation IS the statement 'expansion kinetic energy")
print("  exactly cancels gravitational binding' -- the flat universe carries zero")
print("  net energy. In the medium reading: the medium's spreading (kinetic) is")
print("  balanced by its own induced-gravity self-attraction (binding).")
chk("flat ledger K+U = 0 at Friedmann H", (K + U) / abs(U), 0.0, 1e-12)

# ============================================================ (2) first law = continuity
print()
print("=" * 70)
print("(2) LOCAL CONSERVATION:  the continuity eqn IS the first law dU = -p dV")
print("=" * 70)
# comoving volume V = a^3 (chi=1); U = rho a^3.  First law (adiabatic): dU = -p dV.
#   d(rho a^3) = -p d(a^3)  ->  a^3 drho + 3 a^2 rho da = -3 p a^2 da
#   ->  drho/da = -3 (rho + p)/a  ->  rho_dot = -3 H (rho + p)   [continuity]
# For p = w rho:  rho ~ a^{-3(1+w)}.
print("  d(rho a^3) = -p d(a^3)  <=>  rho ~ a^(-3(1+w))   [w = p/rho]")
for label, w in [("radiation", 1.0/3.0), ("matter", 0.0), ("dark energy", -1.0)]:
    n = -3 * (1 + w)                        # rho ~ a^n
    # verify the first law numerically: dU + p dV = 0 across a small da
    a0, da = 1.0, 1e-6
    def rho_of(a, w=w): return a ** (-3 * (1 + w))
    def U_of(a, w=w):   return rho_of(a) * a**3
    dU = (U_of(a0 + da) - U_of(a0 - da)) / (2 * da)
    p  = w * rho_of(a0)
    dV = 3 * a0**2                          # d(a^3)/da
    firstlaw = dU + p * dV                  # should be 0
    print(f"    {label:11s} w={w:+.4f}: rho ~ a^{n:+.2f},  dU + p dV = {firstlaw:+.2e}"
          f"  ({'conserved (first law holds)' if abs(firstlaw)<1e-6 else 'CHECK'})")
    chk(f"first law dU=-pdV for {label}", firstlaw, 0.0, 1e-6)

# ============================================================ (3) the ledger over expansion
print()
print("=" * 70)
print("(3) WHERE THE ENERGY GOES  (why 'expansion energy' is not a new substance)")
print("=" * 70)
print("  Track comoving energy U = rho a^3 from a=1 to a=2 for each component:")
for label, w in [("radiation", 1.0/3.0), ("matter", 0.0), ("dark energy", -1.0)]:
    U1, U2 = 1.0, (2.0)**(-3*(1+w)) * 2.0**3
    verb = ("LOSES energy -> does +p dV work pushing space out" if U2 < U1 else
            "constant U (does no work)" if abs(U2-U1) < 1e-9 else
            "GAINS energy <- its negative pressure is pulled ON by expansion")
    print(f"    {label:11s}: U(a=1)={U1:.2f} -> U(a=2)={U2:.2f}   {verb}")
print("  There is no separate 'expansion energy' reservoir: the content does p dV")
print("  work on the growing volume (radiation pays, DE is paid), and locally the")
print("  books close by the first law. The medium is the SAME thing doing the")
print("  spreading (kinetic), the binding (gravity), and the sinking (dilution) --")
print("  one flow, not a new substance.")

# ============================================================ grade
print()
print("=" * 70)
print("GRADE (honest)")
print("=" * 70)
print("""  SHOWN: the medium is CONSISTENT with Friedmann -- the flat-universe ledger
  nets to zero (+kinetic/-binding), and local energy conservation is exactly the
  first law dU = -p dV, component by component. This clears the minimum bar: the
  medium reproduces the expansion without breaking known cosmology.

  NOT a new result: the Newtonian energy-balance derivation is textbook and holds
  for any G. Reproducing it proves consistency, not correctness.

  PRTOE-specific, and UNBUILT: that the medium's GLOBAL total energy is constant --
  a well-defined conserved total GR cannot provide. That is the actual payoff, and
  it needs the medium's own dynamics (Friedmann derived FROM the medium's energy
  functional, not just consistent with it). Not shown here.

  THE COST, unavoidable: a localizable energy requires the medium's rest frame -- a
  preferred frame, Lorentz violation, bounded to ~27 orders on the one live channel
  (PRTOE_LV_pricing.md). Concreteness is bought with an exposure GR does not carry.

  Net: consistent, concrete, and more falsifiable -- NOT shown correct.""")

print(f"\nself-check:  {'ALL PASS' if all(_ok) else 'SOME FAILED'}  ({sum(_ok)}/{len(_ok)})")
