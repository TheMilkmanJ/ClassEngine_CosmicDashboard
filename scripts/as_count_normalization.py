#!/usr/bin/env python3
"""Task #168 — mechanize A_s's count C: is the assembly exactly (4pi k / alpha_c)^3?

Three things this settles, in order:

(1) PROVENANCE. The pipeline's frozen A_s = 2.088058e-9 (cmp_prtoe_fixed.yaml:91) is
    NOT an independent measurement. It is the same closed form (alpha_c/4pi k)^3
    evaluated at the CONCORDANCE joint k = 1.3630 (scripts/concordance.py) instead of
    the closed-form k = 1.364612. So the booked "-0.35%" is 3*ln(k_joint/k_closed) --
    a k-determination spread -- and carries no information about the count C. The
    joint itself contains the closed form as one of its three inputs and Planck's A_s
    inverted THROUGH the closed form as another, so the comparison is self-referential.

(2) THE HONEST DATA CONFRONTATION. Against the corpus's own recorded measured value,
    Planck A_s = 2.100e-9 (_AUDIT_LEDGER.md:801) at ~1.4% (hierarchy_problem.md:609),
    the closed form lands -0.92% = -0.66 sigma, i.e. C_required = 1.0093 +/- 0.014.
    C = 1 is consistent; no present measurement can pin C better than +/-1.4%.

(3) THE MECHANIZATION ATTEMPT. Carry the recorded mechanism -- a Poisson census of
    independent cells, A_s = 1/N with N the cells across the pivot scale
    (PRTOE_THE_CHAIN.md:68-69) -- through to the dimensionless power per log k:

        Delta^2_zeta(k) = k^3 P_zeta(k) / (2 pi^2),   P_zeta = R^2 * xi^3
        =>  A_s = R^2 (k xi)^3 / (2 pi^2)
        =>  C == A_s * N = R^2 (k_* l_p)^3 / (2 pi^2)

    with xi the comoving cell size, l_p the pivot "scale" whose cell count is N, and
    R = d zeta / d(delta n / n) the transfer coefficient. C therefore hides TWO O(1)s,
    not one: the pivot-volume convention and R. Neither is derived anywhere in the
    corpus, and at the corpus's own conformal (w = 1/3) transfer R = 1/4 the three
    natural conventions return C = pi/4, 0.098, 3.2e-3 -- none of them 1.

Run: python3 scripts/as_count_normalization.py
"""
import math

ALPHA = 1 / 137.035999084          # scripts/audit_math_pass.py:8
AC    = 3 * ALPHA                  # alpha_c = 3 alpha, MATH_SPINE
FROZEN = 2.088058e-9               # cmp_prtoe_fixed.yaml:91
PLANCK = 2.100e-9                  # _AUDIT_LEDGER.md:801
PLANCK_FRAC = 0.014                # hierarchy_problem.md:609, "measured to ~1.4%"
K_JOINT = 1.3630                   # scripts/concordance.py joint, as used by the yaml


def k_of(a):
    """The closed-form screened-exchange coupling, hierarchy_problem.md:308-310."""
    return math.log(1 + math.pi / (2 * a)) / math.pi


def As_of(a, k=None):
    k = k_of(a) if k is None else k
    return (a / (4 * math.pi * k)) ** 3


def report():
    k_cf = k_of(AC)
    A_cf = As_of(AC, k_cf)
    A_joint = As_of(AC, K_JOINT)

    print("=" * 72)
    print("#168  A_s's count C — is the assembly exactly (4 pi k / alpha_c)^3?")
    print("=" * 72)
    print(f"  alpha_c = 3 alpha        = {AC:.9f}")
    print(f"  k = ln(1+pi/2a_c)/pi     = {k_cf:.9f}   (booked 1.36461191)")
    print(f"  L = 4 pi k / alpha_c     = {4*math.pi*k_cf/AC:.4f}  cells per side")
    print(f"  N = L^3                  = {(4*math.pi*k_cf/AC)**3:.5e}")
    print(f"  A_s = (alpha_c/4 pi k)^3 = {A_cf:.6e}")

    print("\n(1) WHAT THE -0.35% ACTUALLY MEASURES")
    print(f"  frozen A_s (yaml:91)             = {FROZEN:.6e}")
    print(f"  closed form at k_joint = {K_JOINT}  = {A_joint:.6e}")
    print(f"    -> the frozen value IS the closed form at the joint k, to "
          f"{abs(A_joint/FROZEN-1)*100:.4f}%")
    print(f"  k implied by the frozen value    = {AC/(4*math.pi*FROZEN**(1/3)):.7f}")
    print(f"  A_s(k_closed) / A_s(k_joint) - 1 = {100*(A_cf/A_joint-1):+.4f} %"
          f"   [booked -0.35%]")
    print(f"  pure k effect 3*ln(k_joint/k_cf) = {300*math.log(K_JOINT/k_cf):+.4f} %")
    print("  => the residual is the k-determination spread, NOT the count C.")

    print("\n(2) THE HONEST DATA CONFRONTATION")
    print(f"  Planck A_s (ledger:801)  = {PLANCK:.4e} +/- {PLANCK_FRAC*100:.1f}%")
    print(f"  closed form vs it        = {100*(A_cf/PLANCK-1):+.3f} % "
          f"= {(A_cf/PLANCK-1)/PLANCK_FRAC:+.2f} sigma")
    print(f"  C_required = A_meas/A_cf = {PLANCK/A_cf:.5f} +/- {PLANCK_FRAC:.3f}")

    print("\n(3) MECHANIZATION ATTEMPT — C = R^2 (k_* l_p)^3 / (2 pi^2)")
    R_conf = 0.25                        # zeta = d rho / (3(1+w) rho), w = 1/3
    print(f"  conformal (w = 1/3) transfer R = 1/(3(1+w)) = {R_conf}")
    print(f"  {'pivot-volume convention':30s} {'C at R=1/4':>12s} {'R needed for C=1':>18s}")
    for name, lp_k in [("l_p = 2 pi / k_*  (wavelength)", 2 * math.pi),
                       ("l_p = pi / k_*    (half-wave)", math.pi),
                       ("l_p = 1 / k_*     (inverse k)", 1.0)]:
        geo = lp_k ** 3 / (2 * math.pi ** 2)
        print(f"  {name:30s} {R_conf**2*geo:12.6f} {1/math.sqrt(geo):18.5f}")
    print("  => no convention returns C = 1 at the corpus's own transfer; the three")
    print("     readings span a factor of ~250. C hides the convention AND R.")

    print("\n(4) WHAT THE CLOSED FORM IS EQUIVALENT TO (the forward target, re-typed 2026-07-20)")
    for name, lp_k in [("wavelength", 2 * math.pi), ("inverse k", 1.0)]:
        # A_s = R^2 (k xi)^3 / 2pi^2  ->  k xi at R = 1
        kxi = (2 * math.pi ** 2 * A_cf) ** (1 / 3)
        print(f"  freeze-out ratio k_* xi required at R = 1: {kxi:.5e} "
              f"= 1/{1/kxi:.1f} of k_*^-1")
        break
    print("  i.e. the census must lock cells ~290x below the mode's own scale.")
    print("  NOT a Kibble-Zurek freeze-out ratio: P_zeta = R^2 xi^3 carries no k, so one")
    print("  frozen comoving xi is white noise (Delta^2 ~ k^3, n_s = 4). Scale invariance")
    print("  needs xi(k) ~ 1/k -- a SCALING length holding a fixed fraction of the horizon.")
    print("  The basement owes a mechanism of that type before it owes the number.")

    print("\n(5) THE 6i JOINT'S REAL REQUIREMENT")
    rows = [("3 alpha(0)", AC), ("3 alpha(M_Z) [1/127.95]", 3 / 127.95),
            ("3 alpha extrapolated [1/106]", 3 / 106.0)]
    for lbl, a in rows:
        A = As_of(a)
        print(f"  {lbl:30s} A_s = {A:.4e}   C needed = {FROZEN/A:.4f}")
    print("  => excluding the M_Z reading needs C = 1 to about +/-22%, not 'exactly 1'.")
    print("=" * 72)


if __name__ == "__main__":
    report()
