"""kapitza_junction_response — #39 stage 8: the second-order averaging done, and what it puts in front (2026-07-28).

THE OBJECT
  Stage 7 selected class B by elimination — the Kapitza-rectified pinned
  phase — and recorded its efficiency as

        R_B  ~  (m1/thetadot) * F ,    F an O(1) junction response,

  with m1/thetadot = 3.77e-5 sitting at 0.75 of the needed 5e-5, and F
  named as the one owed factor.  Four consumers ride on it.  This script
  performs the owed averaging.

THE MODEL (each ingredient is stage 7's own, in its own words)
  * the visible-side phase phi is OVERDAMPED by the thermal bath:
    Gamma_phi ~ G_F^2 T^5 = 5.4e9 eV at T_sph, against thetadot = 59.7 eV
    (stage 7's premise check: overdamped by 9e7);
  * PINNED by the Majorana term, whose mass m1 = 2.25 meV sets the
    pinning frequency;
  * SHAKEN by the seat coupling, J*sin(phi - theta(t)), with the dark
    phase winding uniformly, theta(t) = thetadot * t.

  An overdamped phase in a potential U obeys  chi*Gamma_phi*phidot = -U'(phi).
  Writing the pinning as U_pin = -chi*m1^2*cos(phi) and the junction as
  U_J = -chi*omega_J^2*cos(phi - theta), chi cancels and the equation of
  motion is a competition of three RATES:

        phidot = -p*sin(phi) - j*sin(phi - thetadot*t)
        p = m1^2 / Gamma_phi      (the pinning relaxation rate)
        j = omega_J^2 / Gamma_phi (the junction relaxation rate)

  THIS IS THE STEP THAT MATTERS.  For an overdamped coordinate the
  pinning does not enter as the frequency m1; it enters as the RELAXATION
  RATE m1^2/Gamma_phi.  The bath that makes the class work also converts
  the pinning's energy scale into a rate, and divides it by 5.4e9 eV.

THE AVERAGING (analytic, second order in the junction)
  Expand phi = 0 + delta about the pinned minimum, linearise, solve the
  driven response, and correlate it back against the drive:

        delta(t)  = j*[p*sin(wt) - w*cos(wt)] / (p^2 + w^2),   w = thetadot
        R = <sin(phi - wt)> = <delta*cos(wt)> = - j*w / (2*(p^2 + w^2))

  Two limits, and only one of them is ours:
        p >> w  (stiff pinning) :  R -> -j*w/(2p^2)   -- pinning matters
        p << w  (fast drive)    :  R -> -j/(2w)       -- pinning is ABSENT

  The physical point is p/w = 1.6e-17.  We are seventeen orders into the
  second limit, and there the answer does not contain m1 at all.

THE DECISIVE CONTROL
  Set m1 = 0 exactly.  If m1 were the leading factor, the rectification
  must vanish.  It does not: at p = 0 the equation is the textbook
  overdamped running junction, whose own back-action rectifies at
  -j/(2w).  The transfer survives the removal of the thing it was
  credited to.

WHAT THIS RUN DOES
  (1) verifies R = -j*w/(2*(p^2+w^2)) by direct integration of the
      nonlinear equation across p/w in [0, 10], for both the cos(phi) and
      the cos(2*phi) pinning harmonic (a Majorana insertion violates L by
      two units, so its harmonic is checked, not assumed);
  (2) runs the m1 = 0 control;
  (3) evaluates the physical point from recorded inputs;
  (4) states what the needed efficiency actually demands, and grades the
      result against stage 7's pre-committed kill.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp

# ---- recorded inputs (stage 4/5/7 of the transfer-integral spec) -----------
M1_EV = 2.25e-3          # Majorana insertion, the pinning scale
THETA_DOT_EV = 59.7      # winding rate at T_sph, from charge conservation
GAMMA_PHI_EV = 5.4e9     # nu-sector damping ~ G_F^2 T^5 at T_sph
NEED = 5.0e-5            # the transmission the recorded eta_B requires


def rectified_numeric(p: float, j: float, w: float, harmonic: int = 1,
                      n_burn: int = 40, n_avg: int = 240) -> float:
    """<sin(phi - w t)> by direct integration of the overdamped equation.

    The averaging window is an EXACT integer number of drive periods, so the
    oscillating part of sin(phi - wt) cancels by construction and only the
    rectified part survives.  Without that the O(1) oscillation leaks into a
    mean of order 1e-3 and swamps it.
    """
    def rhs(t, y):
        phi = y[0]
        return [-p * np.sin(harmonic * phi) / harmonic - j * np.sin(phi - w * t)]

    T = 2 * np.pi / w
    t_burn = n_burn * T                    # let the transient die
    t_end = t_burn + n_avg * T
    t_eval = np.linspace(t_burn, t_end, 40 * n_avg + 1)
    sol = solve_ivp(rhs, (0.0, t_end), [0.0], method="DOP853",
                    rtol=1e-10, atol=1e-13, t_eval=t_eval)
    phi = sol.y[0]
    s = np.sin(phi - w * sol.t)
    return float(np.trapezoid(s, sol.t) / (t_end - t_burn))


def rectified_analytic(p: float, j: float, w: float) -> float:
    return -j * w / (2.0 * (p * p + w * w))


def main() -> None:
    print("=" * 78)
    print("The Kapitza averaging, performed — what actually sits in front")
    print("=" * 78)

    w, j = 1.0, 0.01
    print(f"\n(1) VERIFICATION of R = -j*w/(2(p^2+w^2))   [w = {w}, j = {j}]")
    print("     p/w      numeric cos(phi)   numeric cos(2phi)     analytic")
    worst = 0.0
    for p in (0.0, 0.1, 0.5, 1.0, 3.0, 10.0):
        n1 = rectified_numeric(p, j, w, harmonic=1)
        n2 = rectified_numeric(p, j, w, harmonic=2)
        a = rectified_analytic(p, j, w)
        worst = max(worst, abs(n1 - a) / abs(a))
        print(f"   {p/w:6.2f}    {n1:+.6e}     {n2:+.6e}    {a:+.6e}")
    print(f"\n     worst deviation of the cos(phi) branch from the formula: "
          f"{100*worst:.2f}%")
    print("     (the cos(2phi) column tracks it once p/w << 1 — where the")
    print("      pinning has dropped out, its harmonic cannot matter either)")

    print("\n(2) THE CONTROL — the pinning removed entirely (m1 = 0):")
    r_pinned = rectified_numeric(1e-3, j, w)
    r_unpinned = rectified_numeric(0.0, j, w)
    print(f"     with pinning p/w = 1e-3 : R = {r_pinned:+.6e}")
    print(f"     with m1 = 0 exactly     : R = {r_unpinned:+.6e}")
    print(f"     difference: {100*abs(r_pinned-r_unpinned)/abs(r_unpinned):.3f}%"
          "  -- the transfer does not need the Majorana term")

    print("\n(3) THE PHYSICAL POINT, from recorded inputs:")
    p_phys = M1_EV ** 2 / GAMMA_PHI_EV
    print(f"     pinning relaxation rate p = m1^2/Gamma_phi = {p_phys:.3e} eV")
    print(f"     drive rate              w = thetadot       = {THETA_DOT_EV:.3g} eV")
    print(f"     p/w = {p_phys/THETA_DOT_EV:.2e}")
    print("     => the fast-drive limit, by seventeen orders. R = -j/(2w),")
    print("        and m1 has left the expression.")

    print("\n(4) WHAT THE NEEDED TRANSMISSION ACTUALLY DEMANDS:")
    omega_J_sq = 2.0 * NEED * GAMMA_PHI_EV * THETA_DOT_EV
    omega_J = np.sqrt(omega_J_sq)
    j_phys = omega_J_sq / GAMMA_PHI_EV
    print(f"     R = omega_J^2/(2*Gamma_phi*thetadot) = {NEED:.1e} requires")
    print(f"        omega_J = {omega_J:.3e} eV = {omega_J/1e3:.2f} keV")
    print(f"     (perturbative validity: j/w = {j_phys/THETA_DOT_EV:.2e} << 1, ok)")
    print(f"     that is {omega_J/M1_EV:.2e} times the Majorana scale the class")
    print("     was priced on -- a junction plasma frequency, not a mass.")

    print("\nVERDICT:")
    print("   THE m1/thetadot FACTORISATION DOES NOT SURVIVE THE AVERAGING.")
    print("   Second-order averaging of the overdamped, pinned, fast-driven")
    print("   junction returns R = omega_J^2/(2*Gamma_phi*thetadot). The")
    print("   Majorana pinning is absent from it -- not small, absent: the")
    print("   m1 = 0 control rectifies identically. The bath that supplies")
    print("   the class's overdamping is what removes the pinning, by")
    print("   converting m1 into the rate m1^2/Gamma_phi = 9.4e-16 eV,")
    print("   seventeen orders under the winding rate it had to compete with.")
    print("   So m1/thetadot = 3.8e-5 landing at 0.75 of the need is a")
    print("   numerical coincidence and nothing more; the quantity that")
    print("   governs the transfer never contained m1.")
    print()
    print("   The pre-committed kill does not fire as written -- it was")
    print("   written on F, and F is not the free parameter. What replaces")
    print("   it is sharper and testable: the junction transfers what the")
    print("   need requires if and only if the seat term supplies a junction")
    print(f"   plasma frequency omega_J = {omega_J/1e3:.1f} keV. That is now the")
    print("   single number the sector owes, and it is a property of the seat")
    print("   coupling at T_sph, not of the neutrino mass.")
    print("=" * 78)


if __name__ == "__main__":
    main()
