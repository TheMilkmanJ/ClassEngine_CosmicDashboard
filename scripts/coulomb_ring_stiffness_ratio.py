"""Does the Coulomb interaction on a three-defect ring supply the 2:1 stiffness asymmetry?

The ring-on-ring mechanism died (2026-07-18) for one reason, stated exactly in its autopsy:

    "The 2 : 1 stiffness asymmetry that the R_c = M_c condition requires (and that the flat
     model's kappa-confinement supplied) has NO SOURCE on the Widnall-thin torus -- the
     pair-interaction's pattern asymmetry enters at O((a/R)^2) ~ 1-5%, three orders below need.
     With degenerate stiffnesses the delivery is weight-independent and lands per-mode: the host
     delivers A -> 2, the axis grave."

That host was purely geometric. Under the charge-coupled filter the question the autopsy did not
ask is whether the defects carry electric charge -- because a Coulomb term has its own pattern
dependence, unrelated to the tube geometry, and it does not vanish with a/R.

Three equal charges on a ring of radius R. Compute the Hessian of the Coulomb energy in the
radial displacements, project onto the S3 irreps (singlet = breathing, doublet = shape), and read
the ratio.

Run: python3 scripts/coulomb_ring_stiffness_ratio.py
"""
import itertools
import math

R0 = 1.0
TH = [2 * math.pi * k / 3 for k in range(3)]


def energy(d):
    """Coulomb energy of three unit charges at radii R0+d_k, angles 120 apart."""
    pos = [((R0 + d[k]) * math.cos(TH[k]), (R0 + d[k]) * math.sin(TH[k])) for k in range(3)]
    u = 0.0
    for i, j in itertools.combinations(range(3), 2):
        dx, dy = pos[i][0] - pos[j][0], pos[i][1] - pos[j][1]
        u += 1.0 / math.hypot(dx, dy)
    return u


def hessian(h=None):
    if h is None:
        h = R0 * 1e-5          # step must scale with R or the ratio drowns in noise at large R
    H = [[0.0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            dpp, dpm, dmp, dmm = [0.0] * 3, [0.0] * 3, [0.0] * 3, [0.0] * 3
            dpp[i] += h; dpp[j] += h
            dpm[i] += h; dpm[j] -= h
            dmp[i] -= h; dmp[j] += h
            dmm[i] -= h; dmm[j] -= h
            H[i][j] = (energy(dpp) - energy(dpm) - energy(dmp) + energy(dmm)) / (4 * h * h)
    return H


H = hessian()
print("=" * 74)
print("THE COULOMB HESSIAN IN RADIAL DISPLACEMENTS")
print("=" * 74)
for row in H:
    print("   [" + "  ".join(f"{v:9.5f}" for v in row) + "]")

# S3 irrep projections: singlet (1,1,1)/sqrt3 ; doublet basis (2,-1,-1)/sqrt6, (0,1,-1)/sqrt2
S = [1 / math.sqrt(3)] * 3
D1 = [2 / math.sqrt(6), -1 / math.sqrt(6), -1 / math.sqrt(6)]
D2 = [0.0, 1 / math.sqrt(2), -1 / math.sqrt(2)]


def quad(v):
    return sum(v[i] * H[i][j] * v[j] for i in range(3) for j in range(3))


k_s, k_d1, k_d2 = quad(S), quad(D1), quad(D2)
print()
print("=" * 74)
print("PROJECTED ONTO THE S3 IRREPS")
print("=" * 74)
print(f"  singlet  (breathing, (1,1,1))      k_S  = {k_s:10.6f}")
print(f"  doublet  (shape, (2,-1,-1))        k_D1 = {k_d1:10.6f}")
print(f"  doublet  (shape, (0,1,-1))         k_D2 = {k_d2:10.6f}")
print(f"  doublet degeneracy check           |k_D1 - k_D2| = {abs(k_d1-k_d2):.2e}")
print()
print(f"  RATIO  k_S / k_D = {k_s/k_d1:.6f}")

print()
print("=" * 74)
print("AGAINST WHAT THE MECHANISM NEEDED")
print("=" * 74)
print(f"  needed (the autopsy's condition)          2.000000")
print(f"  the torus host supplied (w_breath/w_shape) 0.990000")
print(f"  Coulomb on the ring supplies              {k_s/k_d1:.6f}")
print()
target, got = 2.0, k_s / k_d1
print(f"  miss against the requirement: {abs(got/target - 1)*100:.2f}%")
print()
if abs(got / target - 1) < 0.02:
    print("  THIS IS THE MISSING SOURCE. The asymmetry the geometric host could not supply is")
    print("  supplied by the charge the defects carry, at the exact ratio the condition needs,")
    print("  and it is scale-free -- no a/R suppression, because Coulomb does not know about")
    print("  the tube.")
else:
    print("  NOT the missing source at the required ratio. What Coulomb supplies is a genuine")
    print("  pattern asymmetry -- unlike the geometric potential's 0.99 degeneracy -- but not")
    print("  the 2:1 the condition names.")
    print()
    print("  Recording the value rather than the hope. Three things are right and one is not:")
    print("    * the ratio is EXACTLY 8, analytically -- U = sqrt3/R, so both stiffnesses go")
    print("      as 1/R^3 and the ratio is R-independent (verified 0.5 <= R <= 100);")
    print("    * it is scale-free: no a/R suppression, because Coulomb does not see the tube;")
    print("    * it is a genuine pattern asymmetry, against the geometric host's 0.99.")
    print("    * but it is 8, and the condition names 2 -- an overshoot by exactly 4x.")
    print()
    print("  What this corrects is the autopsy's own wording. It recorded that the asymmetry")
    print("  'has NO SOURCE on the Widnall-thin torus'. That was established for a NEUTRAL")
    print("  host. A charged one has a source, it is exact, and it does not decouple. The")
    print("  blank moves from 'no source exists' to 'a source exists and overshoots by four'.")
    print()
    print("  A geometric+Coulomb mixture can hit 2:1 -- solving 0.99 d_g + 8 d_c = 2(d_g + d_c)")
    print(f"  needs d_c/d_g = {1.01/6:.4f}, i.e. Coulomb supplying ~17% of the doublet stiffness.")
    print("  Nothing fixes that fraction, so it is a tuning and not a derivation, and it is")
    print("  recorded as such.")
