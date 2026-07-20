#!/usr/bin/env python3
"""Task #170 (M7's remaining half) — the winding-modulation full C_l, forward.

THE QUESTION. P-2026-029 registers a comb in C_l at l_1 = n(2 pi chi_*/L) ~ 3.1n with
teeth at its harmonics, and bounds its amplitude OBSERVATIONALLY to A = dC_l/C_l in
[0.7%, 1.4%] across l = 100-600. The forward number -- the winding power fraction
f_wind that sets A -- was never computed. This computes it.

WHAT ACTUALLY PRODUCES A DIAGONAL COMB. A multiplicative winding modulation
zeta -> zeta(1+W) puts its signal in the OFF-diagonal <a_lm a*_l'm'> (docket #151);
its diagonal effect is second order and non-periodic. A periodic ripple in C_l itself
requires a COHERENT CORRELATION FEATURE in the primordial two-point function at the
winding's own separation d = L/n along the winding axis -- which is exactly what a
winding array supplies, since points a winding-wavelength apart sit in the same phase.
Then

    P(k_vec) = P_0(k) [ 1 + A_prim cos(k_par d) ]

THE GEOMETRIC COST, WHICH IS THE WHOLE RESULT. The diagonal C_l sees only the
k-hat MONOPOLE of P(k_vec) (sum_m |Y_lm|^2 = (2l+1)/4pi kills every higher multipole),
and the monopole of cos(k_par d) is j_0(kd) ~ 1/(kd). A single-axis modulation is
therefore diluted by 1/(kd) = l_1/(2 pi l) before any projection. The exact radial
projection costs another factor 2.5-9:

    T_proj(l) = 2 l(l+1) * int_0^inf j_l(x)^2 j_0(beta x) dx/x ,   beta = d/chi_*

and A_observed(l) = T_proj(l) * A_prim.

TWO CONSEQUENCES:
 (1) A(l) falls as ~1/l across the band. It is NOT the flat comb the fence was
     inverted for (S/N = A*sqrt(N/2) with N = 2.5e5 modes over l = 100-600 assumes A
     constant). The matched-filter flat-equivalent is A_eff = 0.32 * A(l=100).
 (2) Reaching the fence floor needs A_prim of order unity -- 36-72% at n = 30, and
     more than 100% (i.e. impossible) for n <~ 15. Against the model's own
     weak-modulation ceiling (winding roughness Delta^2 <~ 2e-6 per log,
     DERIVATION_HUNT), A_prim <~ 0.14%, giving f_wind <~ 1e-4.

VERDICT: f_wind lands far BELOW the fence's 0.7% floor, on geometry the comb picture
cannot avoid. Booked T_proj values are from the Bessel integrals below (--full).

Run: python3 scripts/winding_comb_cl.py            (fast: geometry + inversion)
     python3 scripts/winding_comb_cl.py --full     (re-runs the Bessel projections)
"""
import math
import sys

CHI = 13.76          # Gpc, comoving distance to last scattering (PREREGISTERED:1844)
L_TORUS = 27.6       # Gpc, matched-circles floor (PREREGISTERED:1845)
LMIN, LMAX = 100, 600            # the pre-Silk band the fence is defined over
FENCE = (0.007, 0.014)           # PREREGISTERED_PREDICTIONS.md:1873-1876
ROUGHNESS_D2 = 2e-6              # DERIVATION_HUNT: winding roughness, per log

# T_proj envelopes from the Bessel integrals (reproduce with --full)
T_PROJ = {10: {100: 0.01205, 300: 0.00262, 600: 0.00091},
          20: {100: 0.03639, 300: 0.00680, 600: 0.00259},
          30: {100: 0.06062, 300: 0.01279, 600: 0.00464}}


def beta_of(n):
    """d/chi_* with d = L/n the winding wavelength."""
    return (L_TORUS / n) / CHI


def l1_of(n):
    return 2 * math.pi / beta_of(n)


def flat_equivalent():
    """Matched-filter flat-equivalent of a 1/l comb, normalised at l = 100."""
    num = sum((2 * l + 1) * (100.0 / l) ** 2 for l in range(LMIN, LMAX + 1))
    den = sum((2 * l + 1) for l in range(LMIN, LMAX + 1))
    return math.sqrt(num / den)


def full_projection():
    import numpy as np
    from scipy.special import spherical_jn

    def T(l, beta, npts=150000):
        x = np.linspace(max(1e-3, 0.3 * l), 40.0 * max(l, 20), npts)
        jl2 = spherical_jn(l, x) ** 2
        return (np.trapezoid(jl2 * spherical_jn(0, beta * x) / x, x)
                / np.trapezoid(jl2 / x, x))

    print("\n  re-running the Bessel projections (envelope over one tooth period)")
    for n in (10, 20, 30):
        b = beta_of(n)
        for lc in (100, 300, 600):
            ls = sorted({int(round(v)) for v in
                         [lc + i * l1_of(n) / 12 for i in range(13)]})
            env = max(abs(T(l, b)) for l in ls)
            print(f"    n={n:2d} l~{lc:3d}: {env:.5f}  (booked {T_PROJ[n][lc]:.5f})")


def main():
    print("=" * 72)
    print("#170  f_wind — the winding comb's forward amplitude")
    print("=" * 72)
    print(f"  {'n':>4s} {'d = L/n [Gpc]':>14s} {'beta = d/chi':>13s} {'l_1 = 2pi/beta':>15s}")
    for n in (10, 20, 30):
        print(f"  {n:4d} {L_TORUS/n:14.3f} {beta_of(n):13.5f} {l1_of(n):15.2f}")
    print(f"  (l_1 = 2 pi n chi/L = {2*math.pi*CHI/L_TORUS:.4f} n — the registered 3.1n)")

    print("\n(1) THE TRANSFER  A_obs(l) = T_proj(l) * A_prim")
    print(f"  {'n':>4s} {'l':>6s} {'T_proj':>10s} {'Limber l_1/(2 pi l)':>21s} {'exact/Limber':>13s}")
    for n in (10, 20, 30):
        for l in (100, 300, 600):
            lim = l1_of(n) / (2 * math.pi * l)
            print(f"  {n:4d} {l:6d} {T_PROJ[n][l]:10.5f} {lim:21.5f}"
                  f" {T_PROJ[n][l]/lim:13.3f}")
    print("  -> the single-axis monopole dilution 1/(kd) is the dominant cost;")
    print("     the radial projection costs a further 2.5-9x.")

    print("\n(2) THE SHAPE — the comb is NOT flat across the band")
    for n in (10, 20, 30):
        print(f"  n={n:2d}: A(600)/A(100) = {T_PROJ[n][600]/T_PROJ[n][100]:.4f}"
              f"   (a fall of {T_PROJ[n][100]/T_PROJ[n][600]:.0f}x)")
    fe = flat_equivalent()
    print(f"  matched-filter flat-equivalent of a 1/l comb: A_eff = {fe:.4f} * A(100)")
    print("  (the fence was inverted for a FLAT A over l = 100-600; this template is not)")

    print("\n(3) INVERTING THE FENCE — what A_prim the comb would need")
    print(f"  {'n':>4s} {'A_prim for 0.7%':>17s} {'A_prim for 1.4%':>17s}  verdict")
    for n in (10, 20, 30):
        need = [f / (fe * T_PROJ[n][100]) for f in FENCE]
        ok = "reachable" if need[0] <= 1.0 else "IMPOSSIBLE (>100% modulation)"
        print(f"  {n:4d} {need[0]*100:16.1f}% {need[1]*100:16.1f}%  {ok}")

    print("\n(4) THE MODEL'S OWN CEILING")
    a_max = math.sqrt(ROUGHNESS_D2)
    print(f"  winding roughness Delta^2 <= {ROUGHNESS_D2:.0e} per log"
          f"  ->  A_prim <= {a_max*100:.3f}%")
    best = max(T_PROJ[n][100] for n in T_PROJ)
    f_wind = fe * best * a_max
    print(f"  best transfer in the band (n=30, l~100): {best:.5f}")
    print(f"  ****  f_wind <= {f_wind:.2e}  =  {f_wind*100:.4f}%  ****")
    print(f"  against the fence floor {FENCE[0]*100:.1f}%: low by {FENCE[0]/f_wind:.0f}x")
    print("\n  VERDICT: OUTSIDE the fence, on the low side. The comb picture breaks")
    print("  unless the winding's primordial imprint is an O(1) single-axis modulation,")
    print("  which the model's own weak-modulation regime forbids.")
    print("=" * 72)

    if "--full" in sys.argv:
        full_projection()


if __name__ == "__main__":
    main()
