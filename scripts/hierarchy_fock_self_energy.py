"""Docket #183 — the Fock (exchange) self-energy insertion: the crossed box's companion.

#141 (scripts/hierarchy_vertex_crossed_box.py) computed the CROSSED BOX on §6c's host and got
c = 0.789262.  That is the vertex half of the O(lambda) correction.  The fermion self-energy
insertion sits at the SAME order and is computed here, on the same host and with the same
machinery, which this module imports rather than re-derives.

THE HOST (identical to #141, docs/PRTOE_hierarchy_problem.md §6c/§6e):

    V(q) = e^2/(q^2 + m_D^2),   e^2 = 4 pi alpha_c,   b = m_D^2/(4 k_F^2) = 2 alpha_c/(pi v),

one band's Fermi surface at k_F inside a linear cone, T = 0, units k_F = v = 1 (so m_D^2 = 4b).

WHY IT IS A VELOCITY RENORMALISATION AND NOT A Z FACTOR.  With an INSTANTANEOUS V the Matsubara
sum in Sigma(k, i w) = -T sum_w' int d3p/(2pi)^3 V(k-p) G(p, i w') collapses to the occupation,
int dw'/2pi G(p, i w') = n_p, so Sigma is frequency-INDEPENDENT:

    Sigma(k) = - int d3p/(2pi)^3 V(k-p) n_p,      n_p = theta(k_F - p) at T = 0.

Frequency-independent means Z = 1 exactly — there is no Eliashberg mass enhancement here.  The
entire effect is the MOMENTUM dependence, i.e. a renormalised Fermi velocity

    v* = v + dSigma/dk |_{k_F},        delta_v = dSigma/dk |_{k_F},

and hence a renormalised pairing density of states N0* = k_F^2/(pi^2 v*) = N0/(1 + delta_v).
(Only the occupations enter Sigma, so the linear-vs-parabolic dispersion choice does not.)

HOW IT COMBINES WITH THE CROSSED BOX.  Gap equation Delta = int d3k'/(2pi)^3 W Delta/(2|xi|)
with W = V - C and xi = v*(k' - k_F):

    lambda_eff = N0* <V - C> = N0 <V> (1 - c lambda)/(1 + delta_v) = lambda (1 - c lambda - a lambda)

writing delta_v = a lambda.  So, to O(lambda), the two insertions simply ADD in the exponent:

    1/lambda_eff = 1/lambda + c + a,      anchor multiplier exp(-(c + a)).

THE SIGN, NOT ARGUED.  Differentiating under the integral with k along z-hat,

    delta_v = 2 e^2 int_{p<1} d3p/(2pi)^3 (1 - p_z)/(|k_hat - p|^2 + m_D^2)^2,

and p < 1 forces p_z <= |p| < 1, so the integrand is pointwise POSITIVE on the Fermi sea.
delta_v > 0, a > 0, with no argument required: exchange STIFFENS the band, the density of
states falls, and the coupling falls with it.  Same sign as the crossed box — the two ADD, they
do not cancel.  (This is the #141 sign statement's exact analogue: there the Lindhard weight was
pointwise >= 0, here 1 - p_z is.)

THE CLOSED FORM.  The angular integral is elementary and the radial one collapses:

    Sigma(k) = -(e^2/(8 pi^2 k)) I(k),   I(k) = int_0^1 dp p ln[((k+p)^2 + m^2)/((k-p)^2 + m^2)]

with, at k = k_F = 1 (m^2 = 4b),

    I(1)  = 2 - 2 m arctan(2/m) + (m^2/2) ln(1 + 4/m^2)
    I'(1) = 4 - 2 m arctan(2/m) -           ln(1 + 4/m^2)

so the arctangents cancel in the derivative and

    delta_v = -(e^2/(8 pi^2)) [I'(1) - I(1)] = (e^2/(8 pi^2)) [(1 + 2b) ln(1 + 1/b) - 2],

    a(b) = delta_v/lambda = (1 + 2b)/2 - 1/ln(1 + 1/b).          <-- e^2 drops out, as it must

VALIDATIONS (all in main()):
  1. Sigma(k) at m -> 0 must be the textbook Hartree-Fock exchange self-energy (Slater form)
     Sigma_x(k) = -(e^2/4 pi^2)[1 + ((1-x^2)/2x) ln|(1+x)/(1-x)|].  Exact, analytic.
  2. Large b: a -> 1/(12 b), derived independently by expanding V = e^2/(q^2+4b) to O(q^2/4b)
     (the constant piece of a contact V renormalises no velocity at all, so a -> 0).
  3. The closed form vs mpmath quadrature of I(1), I'(1) at 40 digits.
  4. The closed form vs a finite-difference derivative of Sigma(k).
  5. The closed form vs BRUTE-FORCE cartesian 3D integration of delta_v — shares nothing with
     the angular reduction except the physics.
  6. The identity T1 = -I'(1), where T1 is the extra radial term thrown off by the direct
     (differentiate-first) reduction: an internal consistency check between two orderings.
  7. e^2-independence of a.

Run: python3 scripts/hierarchy_fock_self_energy.py
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# reuse #141's validated host constants and Fermi-surface average
from hierarchy_vertex_crossed_box import (  # noqa: E402
    ALPHA_C, B_TF, E2, K_SCREEN, LAMBDA, V_avg_fs, c_coefficient, _gl,
)

try:
    import mpmath as mp
    HAVE_MP = True
except ImportError:                                          # pragma: no cover
    HAVE_MP = False


# ---- the closed forms ------------------------------------------------------
def I_1(b):
    """I(1) = 2 - 2 m arctan(2/m) + (m^2/2) ln(1 + 4/m^2),  m^2 = 4b."""
    m = 2.0 * math.sqrt(b)
    return 2.0 - 2.0 * m * math.atan(2.0 / m) + 0.5 * m * m * math.log1p(4.0 / (m * m))


def Ip_1(b):
    """I'(1) = 4 - 2 m arctan(2/m) - ln(1 + 4/m^2)."""
    m = 2.0 * math.sqrt(b)
    return 4.0 - 2.0 * m * math.atan(2.0 / m) - math.log1p(4.0 / (m * m))


def delta_v(b, e2=E2):
    """dSigma/dk at the Fermi surface = (e^2/8 pi^2)[(1+2b) ln(1+1/b) - 2]."""
    return e2 / (8.0 * math.pi ** 2) * ((1.0 + 2.0 * b) * math.log1p(1.0 / b) - 2.0)


def a_coefficient(b=B_TF):
    """a = delta_v/lambda = (1+2b)/2 - 1/ln(1+1/b).  Function of b alone."""
    return (1.0 + 2.0 * b) / 2.0 - 1.0 / math.log1p(1.0 / b)


def a_self_consistent(b=B_TF):
    """a with the screening constant b = 2 alpha_c/(pi v) allowed to follow v -> v*.

    NOT the primary number: #141 computed c on a FIXED host and consistency demands the same
    host here.  Reported as a named residual.  d ln <V>/d ln b = -1/[(1+b) ln(1+1/b)], and
    delta b/b = -delta_v/v, so a -> a (1 + d ln <V>/d ln b)."""
    dlnV_dlnb = -1.0 / ((1.0 + b) * math.log1p(1.0 / b))
    return a_coefficient(b) * (1.0 + dlnV_dlnb)


# ---- Sigma(k) itself, for the textbook check and finite differences --------
def sigma(k, b=B_TF, e2=E2, n=400):
    """Sigma(k) = -(e^2/(8 pi^2 k)) int_0^1 dp p ln[((k+p)^2+m^2)/((k-p)^2+m^2)].

    Panelled Gauss-Legendre around p = k, where the log is nearly singular for small m."""
    m2 = 4.0 * b
    edges = sorted(set([0.0] + [min(max(k + s * 2.0 * math.sqrt(b), 0.0), 1.0)
                                for s in (-4, -1, 0, 1, 4)] + [1.0]))
    x, w = _gl(n)
    tot = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        if hi <= lo:
            continue
        p = 0.5 * (hi - lo) * x + 0.5 * (lo + hi)
        ww = 0.5 * (hi - lo) * w
        tot += float(np.dot(ww, p * np.log(((k + p) ** 2 + m2) / ((k - p) ** 2 + m2))))
    return -e2 / (8.0 * math.pi ** 2 * k) * tot


def sigma_hf_exact(k, e2=E2):
    """Textbook unscreened Hartree-Fock exchange (Slater), m -> 0 limit of sigma()."""
    return -e2 / (4.0 * math.pi ** 2) * (
        1.0 + (1.0 - k * k) / (2.0 * k) * math.log(abs((1.0 + k) / (1.0 - k))))


def delta_v_brute(b=B_TF, e2=E2, n=900, half=1.0):
    """delta_v straight from the cartesian definition, no angular reduction:

        delta_v = 2 e^2 int_{p<1} d3p/(2pi)^3 (1 - p_z)/(|k_hat - p|^2 + m_D^2)^2, k_hat = z_hat.

    Midpoint rule on a cube covering the unit Fermi sphere.  Integrand is smooth and bounded
    (the denominator's minimum is m_D^2 at p = k_hat, which is ON the sphere's surface, so the
    sphere-boundary staircase is the accuracy limit: ~3 digits)."""
    m2 = 4.0 * b
    g = np.linspace(-half, half, n, endpoint=False) + half / n
    h = 2.0 * half / n
    tot = 0.0
    for pz in g:                                    # slab by slab, to stay inside memory
        X, Y = np.meshgrid(g, g, indexing="ij")
        r2 = X * X + Y * Y + pz * pz
        inside = r2 < 1.0
        den = X * X + Y * Y + (pz - 1.0) ** 2 + m2
        tot += float(np.sum(np.where(inside, (1.0 - pz) / den ** 2, 0.0)))
    return 2.0 * e2 * tot * h ** 3 / (2.0 * math.pi) ** 3


def T1(b=B_TF, n=400):
    """The extra radial term from the differentiate-first reduction; must equal -I'(1).

        T1 = int_0^1 dp 4 p^2 (1 - p^2 - m^2) / ([(1-p)^2+m^2][(1+p)^2+m^2])
    """
    m2 = 4.0 * b
    edges = sorted(set([0.0] + [min(1.0, 1.0 - s * 2.0 * math.sqrt(b)) for s in (4, 1, 0)]))
    x, w = _gl(n)
    tot = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        if hi <= lo:
            continue
        p = 0.5 * (hi - lo) * x + 0.5 * (lo + hi)
        ww = 0.5 * (hi - lo) * w
        f = 4.0 * p * p * (1.0 - p * p - m2) / (((1 - p) ** 2 + m2) * ((1 + p) ** 2 + m2))
        tot += float(np.dot(ww, f))
    return tot


def main():
    b, m = B_TF, 2.0 * math.sqrt(B_TF)
    print("docket #183 — the Fock self-energy insertion on §6c's host\n")
    print(f"  alpha_c = {ALPHA_C:.8f}   k = {K_SCREEN}   lambda = {LAMBDA:.8f}")
    print(f"  b = 2 alpha_c/pi = {b:.8f}   m_D/2k_F = sqrt(b) = {math.sqrt(b):.6f}")
    print(f"  <V>_FS = {V_avg_fs(b, E2):.8f}   lambda = <V>/pi^2 = {V_avg_fs(b, E2)/math.pi**2:.8f}\n")

    # --- 1. textbook Hartree-Fock limit --------------------------------------
    print("  [1] m -> 0 must reproduce the textbook (Slater) HF exchange self-energy:")
    for k in (0.3, 0.7, 1.3, 2.0):
        got, want = sigma(k, b=1e-14), sigma_hf_exact(k)
        print(f"      k = {k:.1f}   got {got:+.10f}   want {want:+.10f}   rel {abs(got/want-1):.2e}")

    # --- 3. closed form vs mpmath quadrature ---------------------------------
    if HAVE_MP:
        mp.mp.dps = 40
        mm = mp.mpf(2) * mp.sqrt(mp.mpf(b))
        Iq = mp.quad(lambda p: p * mp.log(((1 + p) ** 2 + mm ** 2) / ((1 - p) ** 2 + mm ** 2)),
                     [0, mp.mpf(1) - mm, 1])
        Ipq = mp.quad(lambda p: 2 * p * ((1 + p) / ((1 + p) ** 2 + mm ** 2)
                                         - (1 - p) / ((1 - p) ** 2 + mm ** 2)),
                      [0, mp.mpf(1) - mm, 1])
        print(f"\n  [3] closed form vs mpmath (40 dps):")
        print(f"      I(1)   closed {I_1(b):+.14f}   quad {float(Iq):+.14f}   "
              f"rel {abs(float(Iq)/I_1(b)-1):.2e}")
        print(f"      I'(1)  closed {Ip_1(b):+.14f}   quad {float(Ipq):+.14f}   "
              f"rel {abs(float(Ipq)/Ip_1(b)-1):.2e}")
    else:
        print("\n  [3] mpmath unavailable — skipped")

    # --- 6. the two reduction orderings must agree ---------------------------
    print(f"\n  [6] differentiate-first vs integrate-first:  T1 {T1(b):+.12f}   "
          f"-I'(1) {-Ip_1(b):+.12f}   rel {abs(T1(b)/(-Ip_1(b))-1):.2e}")

    # --- 4. finite difference on Sigma(k) ------------------------------------
    dv = delta_v(b)
    print("\n  [4] closed-form delta_v vs central finite difference of Sigma(k):")
    for hh in (1e-2, 1e-3, 1e-4):
        fd = (sigma(1.0 + hh, b) - sigma(1.0 - hh, b)) / (2.0 * hh)
        print(f"      h = {hh:.0e}   fd {fd:+.10f}   closed {dv:+.10f}   rel {abs(fd/dv-1):.2e}")

    # --- 5. brute-force cartesian --------------------------------------------
    print("\n  [5] brute-force cartesian delta_v (independent of the angular reduction):")
    prev = None
    for n in (300, 600, 900):
        bf = delta_v_brute(b, n=n)
        d = "" if prev is None else f"   delta {abs(bf-prev):.2e}"
        print(f"      n = {n:4d}   brute {bf:+.8f}   closed {dv:+.8f}   "
              f"rel {abs(bf/dv-1):.2e}{d}")
        prev = bf

    # --- 2. large-b asymptote and contact limit ------------------------------
    print("\n  [2] a(b) against the independently derived large-b asymptote 1/(12b):")
    for bb in (b, 0.05, 0.2, 1.0, 5.0, 50.0, 5e3, 5e5):
        aa, asym = a_coefficient(bb), 1.0 / (12.0 * bb)
        print(f"      b = {bb:<10.5g} a = {aa:.10f}   1/(12b) = {asym:.10f}   "
              f"ratio {aa/asym:.6f}")

    # --- 7. e^2-independence --------------------------------------------------
    print("\n  [7] e^2-independence (a must be a function of b alone):")
    for e2 in (E2, 1.0, 10.0):
        print(f"      e^2 = {e2:<8.4f}  delta_v/lambda(e2) = "
              f"{delta_v(b, e2)/(V_avg_fs(b, e2)/math.pi**2):.12f}")

    # --- the answer -----------------------------------------------------------
    a = a_coefficient(b)
    c = c_coefficient(nu=96, nt=96, ns=96)
    print(f"\n  ==> delta_v = {dv:.8f}  (v* = {1+dv:.6f}, the band stiffens by {100*dv:.3f}%)")
    print(f"      a = delta_v/lambda = {a:.6f}   (POSITIVE — no cancellation)")
    print(f"      c (#141) = {c:.6f}")
    print(f"      c + a    = {c + a:.6f}")
    print(f"      screening fed back (residual, not primary): a = {a_self_consistent(b):.6f}"
          f"  ->  c + a = {c + a_self_consistent(b):.6f}")

    MRED = 1.220890e28 / math.sqrt(8 * math.pi)
    print(f"\n      1/lambda = {1/LAMBDA:.4f}")
    for tag, ex in (("booked", 1 / LAMBDA), ("+c (#141)", 1 / LAMBDA + c),
                    ("+c+a (#183)", 1 / LAMBDA + c + a)):
        print(f"        {tag:12s} exponent {ex:8.4f}   M_anchor (exact-solution conv.) "
              f"{2*MRED*math.exp(-ex-1.5)/1e9:8.1f} GeV")
    print(f"\n      anchor multiplier exp(-c)     = {math.exp(-c):.5f}")
    print(f"      anchor multiplier exp(-(c+a)) = {math.exp(-(c+a)):.5f}"
          f"   (a further x{math.exp(-a):.5f})")
    print(f"      §6d band 1.6-5.2 TeV x exp(-c)     -> "
          f"{1.6*math.exp(-c):.3f}-{5.2*math.exp(-c):.3f} TeV   [#141, currently booked]")
    print(f"      §6d band 1.6-5.2 TeV x exp(-(c+a)) -> "
          f"{1.6*math.exp(-(c+a)):.3f}-{5.2*math.exp(-(c+a)):.3f} TeV   [#183, complete O(lambda)]")
    a_sc = a_self_consistent(b)
    print(f"      with the screening residual        -> "
          f"{1.6*math.exp(-(c+a_sc)):.3f}-{5.2*math.exp(-(c+a_sc)):.3f} TeV")
    print(f"      4 pi m_H = {4*math.pi*125.25:.1f} GeV; complete-O(lambda) anchor is "
          f"{2*MRED*math.exp(-1/LAMBDA-c-a-1.5)/1e9/(4*math.pi*125.25):.4f} x it")


if __name__ == "__main__":
    main()
