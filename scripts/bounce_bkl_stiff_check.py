#!/usr/bin/env python3
"""
#117 — can the model's own rotating condensate supply the stiff (w >= 1) phase
that a BKL-safe contraction requires?

MATH_SPINE records the objection as "the recorded regimes do not supply w >= 1".
That is a survey statement. This is the calculation.

The model's founding identity is a charged ROTATING superfluid: a complex scalar
Psi = (r/sqrt2) e^{i theta} carrying a conserved charge Q = a^3 r^2 thetadot.
Eliminating thetadot at fixed Q turns the rotation into a centrifugal term in an
effective radial potential:

    V_eff(r) = V(r) + Q^2 / (2 a^6 r^2)

Two regimes are possible on approach:

  (A) TRACKING - r sits at the minimum of V_eff and slides as a shrinks.
  (B) FROZEN   - Hubble friction beats the restoring curvature, r stays put and
                 rho_rot = Q^2/(2 a^6 r^2) goes as a^-6, i.e. exactly kination.

(B) is the only way to get w = 1 out of this sector. So the question is entirely
"which regime holds on approach to the bounce", and that is decided by comparing
V_eff'' against H^2 at the tracking solution.

Result, both analytic and integrated below:
  * tracking in V ~ r^n gives  w = (n-2)/(n+2)  exactly -- strictly BELOW 1 for
    every polynomial n, approaching 1 only as n -> infinity.
  * the tracking solution is stable (so (B) never takes over) whenever the
    amplitude is sub-Planckian: V_eff''/H^2 = O(10) * (M_Pl/r)^2.

So the rotating sector cannot supply the stiff phase at any sub-Planckian
amplitude, for any polynomial potential. The BKL objection is not merely
unanswered by the recorded regimes -- it is unanswerable from this sector.
"""
import numpy as np
from scipy.integrate import solve_ivp

MPL = 1.0  # reduced Planck units throughout


def w_tracking_analytic(n):
    """Tracking equation of state for V ~ r^n. Derivation:
       V'(r) = Q^2/(a^6 r^3)  =>  r^(n+2) ~ a^-6  =>  r ~ a^(-6/(n+2))
       rho_rot = Q^2/(2 a^6 r^2) ~ a^(-6n/(n+2)) = a^(-3(1+w))
       => w = (n-2)/(n+2)
    """
    return (n - 2.0) / (n + 2.0)


def curvature_over_H2(n):
    """V_eff''/H^2 at the tracking minimum, in units of (M_Pl/r)^2.

    At the minimum, V'(r) = Q^2/(a^6 r^3), so Q^2/(a^6 r^4) = V'(r)/r.
      V_eff'' = V'' + 3 Q^2/(a^6 r^4) = V'' + 3 V'/r
    For V = c r^n:  V'' = n(n-1) c r^(n-2),  V'/r = n c r^(n-2)
      => V_eff'' = n(n+2) c r^(n-2) = n(n+2) V / r^2

    Energy density at tracking:
      rho = V + Q^2/(2 a^6 r^2) = V + (1/2) V'/r * r^... -> V(1 + n/2)
    since Q^2/(2 a^6 r^2) = (1/2) r V'(r) = (n/2) V.
      => rho = V (1 + n/2) = V (n+2)/2
      => H^2 = rho/(3 M_Pl^2) = V (n+2)/(6 M_Pl^2)

    Ratio:
      V_eff''/H^2 = [n(n+2) V/r^2] / [V (n+2)/(6 M_Pl^2)] = 6 n (M_Pl/r)^2
    """
    return 6.0 * n


def integrate_contraction(n, r0, Q, a0=1.0, a_end=1e-3, c=1.0):
    """Integrate the radial field equation through a contracting phase and
    measure the realised w from rho(a). Independent of the analytic algebra:
    solves the ODE and fits the slope of ln rho vs ln a.

    Field equation in e-folds N = ln a (dN < 0 for contraction), with
    H^2 = rho/(3 M_Pl^2) and rho = (1/2) rdot^2 + Q^2/(2 a^6 r^2) + V(r):

      r'' + (3 + H'/H) r' + (1/H^2)[V'(r) - Q^2/(a^6 r^3)] = 0

    where ' = d/dN. We integrate the first-order system in (r, u = dr/dN),
    recomputing H each step from the constraint (so no separate Friedmann ODE).
    """
    def V(r):
        return c * r**n

    def dV(r):
        return c * n * r**(n - 1)

    def rhs(N, y):
        r, u = y
        a = np.exp(N)
        cent = Q**2 / (a**6 * r**2)          # 2 * rotational KE
        # constraint: rho = (1/2) H^2 u^2 + (1/2) cent + V  (since rdot = H u)
        # => H^2 (3 M_Pl^2 - (1/2) u^2) = (1/2) cent + V
        denom = 3.0 * MPL**2 - 0.5 * u**2
        if denom <= 0:
            return [0.0, 0.0]
        H2 = (0.5 * cent + V(r)) / denom
        if H2 <= 0:
            return [0.0, 0.0]
        # dH/dN / H  from  dot(rho) = -3H(rho + p)
        rho = 0.5 * H2 * u**2 + 0.5 * cent + V(r)
        p = 0.5 * H2 * u**2 + 0.5 * cent - V(r)
        dlnH = -1.5 * (1.0 + p / rho)
        acc = -(3.0 + dlnH) * u - (dV(r) - Q**2 / (a**6 * r**3)) / H2
        return [u, acc]

    N0, N1 = np.log(a0), np.log(a_end)
    # start ON the tracking solution: V'(r) = Q^2/(a^6 r^3)
    r_track = (Q**2 / (c * n * a0**6))**(1.0 / (n + 2))
    sol = solve_ivp(rhs, [N0, N1], [r_track, 0.0], rtol=1e-10, atol=1e-14,
                    dense_output=True, max_step=0.05)
    Ns = np.linspace(N0, N1, 2000)
    rs = sol.sol(Ns)[0]
    us = sol.sol(Ns)[1]
    a = np.exp(Ns)
    cent = Q**2 / (a**6 * rs**2)
    denom = 3.0 * MPL**2 - 0.5 * us**2
    H2 = (0.5 * cent + V(rs)) / denom
    rho = 0.5 * H2 * us**2 + 0.5 * cent + V(rs)

    def fit_w(mask):
        """local w from the slope of ln rho vs ln a over a selected window"""
        if mask.sum() < 20:
            return np.nan
        s = np.polyfit(Ns[mask], np.log(rho[mask]), 1)[0]
        return -s / 3.0 - 1.0

    # THE POINT: r grows during contraction (r ~ a^(-6/(n+2))), so a single run
    # crosses from sub-Planckian tracking into the trans-Planckian regime where
    # Hubble friction wins and the field freezes. Measure w in each separately.
    sub = rs < 0.05 * MPL          # deep in tracking
    trans = rs > 5.0 * MPL         # past the predicted freeze threshold
    return fit_w(sub), fit_w(trans), rs, a


if __name__ == "__main__":
    print(__doc__)
    print("=" * 74)
    print("TRACKING EQUATION OF STATE, V ~ r^n")
    print("=" * 74)
    print(f"{'n':>4} {'w analytic':>11} {'w sub-Planck':>13} {'w trans-Planck':>15}   note")
    # Only n <= 6 is integrated. Placing the tracking amplitude at a chosen
    # sub-Planckian r0 needs c = Q^2/(n r0^(n+2)), which for large n demands an
    # absurd potential normalisation (n=100, r0=1e-3 wants c ~ 1e292) and makes
    # the ODE stiff. That is a parametrisation artefact, not physics -- the
    # analytic w = (n-2)/(n+2) is exact for every n and needs no integration.
    for n, note in [(2, "quadratic - the mass era"),
                    (4, "quartic - the recorded w=1/3 youth"),
                    (6, "")]:
        wa = w_tracking_analytic(n)
        # c = 1, Q = 1e-6 already places the tracking amplitude
        # r = (Q^2/n)^(1/(n+2)) at 8e-4, 8e-3, 2.5e-2 M_Pl for n = 2, 4, 6 --
        # deep sub-Planckian. Contracting to a = 1e-4 then carries r past the
        # 5 M_Pl freeze threshold, so one run measures both regimes.
        w_sub, w_tr, rs, a = integrate_contraction(n, r0=1e-3, Q=1e-6, a_end=1e-4)
        ok = "OK" if abs(w_sub - wa) < 5e-3 else "MISMATCH"
        tr = f"{w_tr:>15.4f}" if np.isfinite(w_tr) else f"{'(never gets there)':>15}"
        print(f"{n:>4} {wa:>11.6f} {w_sub:>13.6f} {tr}   {ok}  {note}")

    print()
    print("  w = (n-2)/(n+2) -> 1 only as n -> infinity.")
    print("  No polynomial potential reaches w = 1. Kination is out of reach")
    print("  of the tracking rotating condensate, for every n.")

    print()
    print("=" * 74)
    print("IS TRACKING ACTUALLY WHAT HAPPENS? (freeze would give w=1 instead)")
    print("=" * 74)
    print("  Freezing needs Hubble friction to beat the restoring curvature,")
    print("  i.e. V_eff'' < H^2 (a few). At the tracking minimum:")
    print()
    print(f"{'n':>6} {'V_eff\"/H^2':>18}   amplitude needed for r to freeze")
    for n in (2, 4, 6, 10):
        k = curvature_over_H2(n)
        r_freeze = np.sqrt(k)          # r/M_Pl at which V_eff''/H^2 = 1
        print(f"{n:>6} {f'{k:.0f} (M_Pl/r)^2':>18}   r > {r_freeze:.1f} M_Pl")
    print()
    print("  The ratio is (M_Pl/r)^2 up to O(10). For any SUB-PLANCKIAN")
    print("  amplitude the curvature dominates by orders of magnitude, the")
    print("  field tracks, and w is pinned at (n-2)/(n+2) < 1.")
    print()
    print("  VERDICT: the rotating sector cannot supply a BKL-safe stiff phase")
    print("  below the Planck scale. The objection is unanswerable from here,")
    print("  not merely unanswered.")

    print()
    print("=" * 74)
    print("THE CONTRACTING BRANCH ON THE MODEL'S OWN (m, lambda) -- what eos it hits")
    print("=" * 74)
    m, lam = 2.24e-20, 2e-91          # recorded values (eV; lambda = (m/Psi0)^2)
    Psi0 = m / np.sqrt(lam)
    MPL = 1.22e28                     # eV
    print(f"  Psi0 = m/sqrt(lambda) = {Psi0:.2e} eV = {Psi0/MPL:.1e} M_Pl (quartic=mass point)")
    print(f"  {'R/Psi0':>9} {'h=lam R^2/m^2':>14} {'local n':>8} {'w':>8}")
    for logr in (3, 1, 0, -1, -3):
        R = Psi0 * 10.0**logr
        h = lam * R**2 / m**2
        n_local = (2 * m**2 * R**2 + 4 * lam * R**4) / (m**2 * R**2 + lam * R**4)
        w = (n_local - 2) / (n_local + 2)
        print(f"  {10.0**logr:>9.0e} {h:>14.2e} {n_local:>8.3f} {w:>8.4f}")
    print()
    print("  The contracting branch passes through w = 1/3 (quartic youth) into")
    print("  w = 0 (mass era) -- the same sequence as expansion, reversed -- and")
    print("  never stiffens: the quartic=mass point Psi0 is itself sub-Planckian,")
    print("  and kination needs ~M_Pl amplitude that contraction does not reach")
    print("  before the bounce. So solving the field equation in time returns the")
    print("  SAME adverse BKL verdict; it does not rescue the bounce.")
