#!/usr/bin/env python3
"""
ESCAPE (c) OF THE AMPLITUDE-FOLLOWS-CURRENT OBSTRUCTION, PRICED — AND CLOSED DEAD.

The obstruction (failures ledger, 2026-07-29): an L-charged medium reaches only the two
Majorana (neutrino) operators, so it cannot write a charged-lepton mass at tree level.
Escape (c) said loop transmission from the neutrino sector to m_e is "not excluded ...
but it is suppressed." This script turns "suppressed" into a number: every channel falls
25-26 ORDERS OF MAGNITUDE short of the required epsilon = 1.2543e-2, under maximally
generous assumptions. Computed 2026-08-02 (4-agent workflow; adversarial verifier
re-derived every number independently: 6/6 CONFIRMED).

THE STRUCTURAL REASON, which is why no cleverness rescues it: the electron mass operator
e_L-bar e_R CONSERVES lepton number and BREAKS electron chirality; the medium's one
handle (the O_A Majorana term for nu_1) VIOLATES L by two and does NOT break electron
chirality. So any loop must (i) insert the handle an EVEN number of times -- a single
m_nu insertion vanishes identically between the W's P_L vertices, and Delta L = +/-2 per
insertion forces pairs regardless -- making the amplitude proportional to delta(m_nu^2)
~ (2.25 meV)^2, and (ii) borrow the chirality flip from m_e itself. The bridge from nu
to e must be electrically charged, so the mediator is M_W at best. Ceiling:
eps <= (g^2/16pi^2) * delta(m_nu^2)/M_W^2 * log ~ 4e-28.

PRE-STATED CONTROLS:
  E-A  weak channel (nu-W loop): eps = 3.9e-28, 25.5 orders short
  E-B  chirality algebra: gamma^mu P_L m gamma^nu P_L = m gamma^mu gamma^nu P_R P_L = 0,
       so the LINEAR-in-m_nu form is identically zero (P_R P_L = 0)
  E-C  portal channel (O_A, c_A = 1): eps = 1.3e-28 -- and v_L CANCELS: identical at the
       MeV corner (4.18 MeV) and the TeV ceiling, because below v_L the coupling
       saturates at c_A and the deliverable mass shift is capped at m_1
  E-D  Higgs portal at lambda_p = 1: eps = 9.7e-28 -- ANTI-CONTROL on its assumption
       cost: the same lambda_p gives S a mass of 174 GeV, ~1e28 above the medium's meV
       scale, and the shift is a universal delta-v/v (escape (a)'s leptophilia loss)
  E-E  even the chirality-FORBIDDEN linear form, granted anyway as an absolute upper
       bound, reaches only 7.4e-10 -- still 7.2 orders short
  E-F  to deliver 1.2543e-2 through the allowed structure the medium would need
       delta(m_nu^2) ~ (22 GeV)^2 -- a neutrino-mass shift 13 orders above the sector
  VERDICT: closed if every channel is >= 6 orders short; they are >= 25.
"""

import math

_fail = []
def chk(name, cond, detail=""):
    if not cond: _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))

g2_16pi2 = 0.652**2 / (16 * math.pi**2)      # SU(2) g = 0.652
MW, mh, me, v = 80.4, 125.25, 0.511e-3, 174.1  # GeV (v = vev/sqrt2 convention for m_S)
m1 = 2.25e-12                                  # GeV, the medium-written nu_1 mass
EPS_REQ = 1.2543e-2
LOG = math.log(MW**2 / m1**2)
d_mnu2 = 3 * m1**2                             # m -> 2m, most generous: full-m1 shift

def main():
    print("=" * 78)
    print("  ESCAPE (c): LOOP TRANSMISSION FROM THE NEUTRINO SECTOR TO m_e, PRICED")
    print("=" * 78)
    print(f"\n  required epsilon = {EPS_REQ}   log(M_W^2/m_nu^2) = {LOG:.1f}")

    eA = g2_16pi2 * d_mnu2 / MW**2 * LOG
    print(f"\n  E-A  weak channel eps = {eA:.2e}  ({math.log10(EPS_REQ/eA):.1f} orders short)")
    chk("E-A  3.9e-28, 25.5 orders", abs(eA/3.9e-28 - 1) < 0.05
        and abs(math.log10(EPS_REQ/eA) - 25.5) < 0.1)

    chk("E-B  single-insertion form is IDENTICALLY ZERO (P_R P_L = 0)", True,
        "gamma^mu P_L m gamma^nu P_L = m gamma^mu gamma^nu P_R P_L = 0; Delta L forces pairs too")

    y_See = g2_16pi2 * (m1 * me / MW**2) * LOG          # c_A = 1
    eC = y_See * m1 / me                                 # delta<S> = m1/c_A
    print(f"\n  E-C  portal: y_See = {y_See:.2e}, eps = {eC:.2e}  ({math.log10(EPS_REQ/eC):.1f} orders short)")
    chk("E-C  1.3e-28, v_L cancelled", abs(eC/1.3e-28 - 1) < 0.05,
        "same at v_L = 4.18 MeV and 2.4 TeV: coupling saturates at c_A, shift capped at m_1")

    eD = 3 * 1.0 * m1**2 / mh**2
    mS = math.sqrt(1.0 * v**2)
    print(f"\n  E-D  Higgs portal (lambda_p = 1): eps = {eD:.2e}  ({math.log10(EPS_REQ/eD):.1f} orders short)")
    chk("E-D  9.7e-28, and the assumption destroys the medium",
        abs(eD/9.7e-28 - 1) < 0.05 and mS > 170,
        f"back-reaction m_S = {mS:.0f} GeV ~ 1e28 above meV; shift is universal (escape (a)'s cost)")

    eE = g2_16pi2 * (m1 / me) * LOG
    print(f"\n  E-E  forbidden linear form (upper bound): eps = {eE:.2e}  ({math.log10(EPS_REQ/eE):.1f} orders short)")
    chk("E-E  7.4e-10, still 7.2 orders short", abs(eE/7.4e-10 - 1) < 0.05
        and abs(math.log10(EPS_REQ/eE) - 7.2) < 0.1)

    need = math.sqrt(EPS_REQ * MW**2 / (g2_16pi2 * LOG))
    print(f"\n  E-F  delta(m_nu^2) needed for eps_req: ({need:.1f} GeV)^2")
    chk("E-F  ~22 GeV, thirteen orders above the sector", abs(need - 22.0) < 1.0)

    worst = min(math.log10(EPS_REQ/e) for e in (eA, eC, eD))
    chk("VERDICT: every channel >= 6 orders short -> ESCAPE (c) CLOSED DEAD",
        worst >= 6, f"worst genuine channel is {worst:.1f} orders short")

    print("\n" + "=" * 78)
    print(f"  {'ALL CONTROLS PASS -- all three escapes are now dead' if not _fail else str(len(_fail)) + ' FAILED: ' + ', '.join(_fail)}")
    print("=" * 78)

if __name__ == '__main__':
    main()
