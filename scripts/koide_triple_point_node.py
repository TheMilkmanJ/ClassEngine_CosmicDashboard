#!/usr/bin/env python3
"""
Does a C3-protected triple-point node DELIVER the Koide graded null, or only permit it?

The candidate mechanism (basement_build_program.md part 4): the three charged-lepton
generations are three branches of one C3 (= Z3) protected node -- a triple-point
fermion. This script builds that node's actual effective Hamiltonian, seats the three
generations on its branches, and works out the irrep splitting to test the claim that
the node forces Q = 2/3 (A = sqrt2) and the phase 2/9.

THE NODE'S HAMILTONIAN. The most general C3-symmetric (circulant) Hermitian 3x3
family Hamiltonian is
    H = a*I + b*P + conj(b)*P^2 ,   P = cyclic permutation (P^3 = I),
with a real (the diagonal / node offset) and b one COMPLEX hopping amplitude. Its
eigenvalues are the C3 harmonics
    sqrt(m_k) = a + 2|b| cos(2 pi k/3 + phi) ,  phi = arg(b),  k = 0,1,2,
which is exactly the Brannen parametrization. So "one node, three branches" is literal:
the node is b = 0 (threefold degenerate), and the three branches are split by the
single complex hopping b. The C3 irreps are the singlet f0 (~ a) and the charged
doublet f1,f2 (~ b, conj(b)).

WHAT THE TEST DECIDES. In the C3-Fourier basis |f0|^2 = 3a^2, |f1|^2 = |f2|^2 = 3|b|^2,
so the graded null f0^2 = |f1|^2 + |f2|^2 reads a^2 = 2|b|^2, i.e. |b|/a = 1/sqrt2,
equivalently A = 2|b|/a = sqrt2. The question is whether the NODE fixes |b|/a and phi,
or leaves them free. Answer computed below, honestly.
"""
import cmath, math

# ---- the C3 (circulant) family Hamiltonian -----------------------------------
W = cmath.exp(2j * math.pi / 3)                       # omega
def P_matrix():
    return [[0, 0, 1], [1, 0, 0], [0, 1, 0]]          # cyclic permutation P

def H_circulant(a, b):
    """H = a I + b P + conj(b) P^2, a 3x3 Hermitian circulant."""
    bc = b.conjugate()
    # rows of a I + b P + conj(b) P^2 ; P has 1 at (i, i-1 mod 3), P^2 at (i, i-2)
    return [[a,      b,      bc],
            [bc,     a,      b ],
            [b,      bc,     a ]]

def eig_circulant(a, b):
    """Analytic eigenvalues of the Hermitian circulant: a + b w^k + conj(b) w^2k."""
    return [ (a + b * W**k + b.conjugate() * W**(2*k)).real for k in range(3) ]

def koide_Q(sqrt_m):
    m = [s*s for s in sqrt_m]
    return sum(m) / (sum(sqrt_m))**2

print("=" * 72)
print("(1) THE NODE IS LITERAL: Koide masses ARE eigenvalues of a C3 hopping H")
print("=" * 72)
# seat the real leptons: fix a = mu (mean), |b| and phi from the measured A, delta.
me, mmu, mtau = 0.51099895, 105.6583755, 1776.86
sm = [math.sqrt(me), math.sqrt(mmu), math.sqrt(mtau)]
mu = sum(sm) / 3.0                                    # the C3 singlet mean = a
# Brannen: sqrt(m_k) = mu(1 + A cos(theta_k)); A = 2|b|/mu (from Q via A=sqrt(6(Q-1/3)))
A_val = math.sqrt(6 * (koide_Q(sm) - 1/3))            # Brannen amplitude = sqrt2
print(f"  a = mu (C3 singlet mean sqrt-mass) = {mu:.4f}")
print(f"  Brannen amplitude A = 2|b|/a = {A_val:.5f}   (sqrt2 = {math.sqrt(2):.5f})")
print(f"  => |b|/a = A/2 = {A_val/2:.5f}   (1/sqrt2 = {1/math.sqrt(2):.5f})")
# verify the circulant with these params reproduces the sqrt-masses (as a SORTED set)
b_mag = A_val * mu / 2.0
# find phi that reproduces the seating (scan; the three eigenvalues are a set)
best = None
for i in range(360000):
    phi = 2 * math.pi * i / 360000
    ev = sorted(eig_circulant(mu, cmath.rect(b_mag, phi)))
    err = sum((e - t)**2 for e, t in zip(ev, sorted(sm)))
    if best is None or err < best[0]:
        best = (err, phi, ev)
err, phi_fit, ev_fit = best
print(f"  best-fit hopping phase phi = {phi_fit:.5f} rad  (Brannen 2/9 lands at a")
print(f"    C3 image of this; the seating is a set, so phi is mod the 120 deg relabel)")
print(f"  eigenvalues {[f'{e:.4f}' for e in ev_fit]}  vs  sqrt-masses"
      f" {[f'{t:.4f}' for t in sorted(sm)]}  (sq-err {err:.2e})")
print("  => the three generations sit on the three branches of ONE C3 node exactly.")

print()
print("=" * 72)
print("(2) THE NODE (b=0) IS THE DEMOCRATIC POINT Q=1/3, NOT THE NULL Q=2/3")
print("=" * 72)
for ratio in [0.0, 0.25, 0.5, 1/math.sqrt(2), 0.9]:
    b = cmath.rect(ratio * mu, phi_fit)
    ev = eig_circulant(mu, b)
    Q = koide_Q(ev) if min(ev) > 0 else float('nan')
    Aval = 2 * ratio
    tag = "  <- NODE (3-fold degenerate)" if ratio == 0 else (
          "  <- the null, Q=2/3, A=sqrt2" if abs(ratio - 1/math.sqrt(2)) < 1e-9 else "")
    posn = "all>0" if min(ev) > 0 else "NEGATIVE sqrt-m (unphysical)"
    print(f"  |b|/a={ratio:.4f} (A={Aval:.4f}): Q={Q:.4f}, min eig={min(ev):+.4f}"
          f" [{posn}]{tag}")
print("  Q = 1/3 + (2/3)(|b|/a)^2 : b=0 gives 1/3, and the null Q=2/3 is a SPECIFIC")
print("  distance off the node, |b|/a = 1/sqrt2. The node permits it; it is not b=0.")

print()
print("=" * 72)
print("(3) DOES THE NODE FORCE |b|/a = 1/sqrt2 ?  (the honest verdict)")
print("=" * 72)
# candidate selector: the positivity wall. sqrt(m) >= 0 for all branches requires
# 1 + A cos(theta_min) >= 0 -> A <= A_max = -1/cos(theta_min).
thetas = [phi_fit + 2*math.pi*k/3 for k in range(3)]
cos_min = min(math.cos(t) for t in thetas)
A_max = -1.0 / cos_min
print(f"  positivity wall: A_max = -1/cos(theta_min) = {A_max:.4f}"
      f"  (A=sqrt2={math.sqrt(2):.4f} is {math.sqrt(2)/A_max*100:.1f}% of it)")
print(f"  so A = sqrt2 sits JUST BELOW the wall where the lightest branch (electron,")
print(f"    sqrt-m = {min(ev_fit):.4f}) nears zero -- near-maximal splitting, not exact.")
print()
print("  VERDICT: the C3 node delivers the STRUCTURE and the PARAMETER COUNT, not the")
print("  values. It forces: (i) three branches of one node (the circulant), (ii) that")
print("  the whole sector is ONE complex hopping b on an offset a -- exactly TWO")
print("  dimensionless numbers, |b|/a and arg(b). Koide's two facts then FIX them:")
print("    Q = 2/3   <=>  |b|/a = 1/sqrt2   (the amplitude/null)")
print("    phase 2/9 <=>  arg(b) = 2/9      (the holonomy)")
print("  The node explains why there are exactly these two knobs; it does NOT predict")
print("  their values. 'Why sqrt2' is now 'why |b| = a/sqrt2' (candidate: the electron")
print("  branch saturating the positivity wall); 'why 2/9' is 'why arg(b) = 2/9'.")
print("  Both need what sets the family hopping in the medium -- the basement, not the")
print("  node's symmetry alone.")

# ---- self-check --------------------------------------------------------------
_c = []
def _chk(name, got, exp, tol):
    ok = abs(got - exp) <= tol; _c.append(ok)
    print(f"  [{'ok' if ok else 'FAIL'}] {name}: got {got:.6f}, expect {exp:.6f}")
print()
print("self-check:")
# Q at the null ratio is exactly 2/3, any phase
_evn = eig_circulant(1.0, cmath.rect(1/math.sqrt(2), 0.3))
_chk("null ratio |b|/a=1/sqrt2 gives Q=2/3", koide_Q(_evn), 2/3, 1e-9)
# Q = 1/3 + (2/3)(|b|/a)^2 identity at a test ratio
_r = 0.4; _evr = eig_circulant(1.0, cmath.rect(_r, 0.3))
_chk("Q = 1/3 + (2/3)(|b|/a)^2", koide_Q(_evr), 1/3 + (2/3)*_r**2, 1e-9)
# node b=0 is threefold degenerate -> Q = 1/3
_chk("node b=0 gives Q=1/3", koide_Q(eig_circulant(1.0, 0j)), 1/3, 1e-12)
# the circulant reproduces the real sqrt-masses
_chk("circulant fits real sqrt-masses (sq-err)", err, 0.0, 1e-3)
print(f"\n{'ALL CHECKS PASS' if all(_c) else 'SOME CHECKS FAILED'}")
