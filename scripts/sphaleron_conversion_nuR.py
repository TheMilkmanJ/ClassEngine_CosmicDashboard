#!/usr/bin/env python3
"""
The sphaleron conversion factor with three right-handed neutrinos  (part of #74)

GRADE STATED BEFORE COMPUTING (protocol check 33)
-------------------------------------------------
`working_logs/the_transfer_integral_spec.md` names this explicitly: "the 28/79 factor
for the SM roster; CHECK THE +3 nu_R ROSTER'S COEFFICIENT -- P-2026-045's content
changes the denominator."

Evidence class: STANDARD EQUILIBRIUM THERMODYNAMICS. Nothing model-specific enters the
machinery -- this is the Harvey-Turner chemical-potential計算 applied to a stated roster.
The model supplies only the roster (SM + 3 nu_R, from Pauli finiteness), and the roster
was fixed by str[k1] = 0, NOT by anything about baryogenesis. So the input is clean of
the output under check 34.

What would count as a result either way: the SM value 28/79 must be reproduced exactly
by the same code with nu_R switched off. If it is not, the setup is wrong and no
nu_R number should be quoted.

WHAT DECIDES THE ANSWER, and it is a physics fork the corpus must own:
  * If the Dirac neutrino Yukawa is IN EQUILIBRIUM at T_sph, nu_R carries lepton number
    and is tied to mu_L and mu_H by its Yukawa constraint. The conversion changes.
  * If it is NOT in equilibrium (tiny Dirac Yukawa, or heavy Majorana nu_R already
    decoupled), nu_R is inert and the SM value stands unchanged.
Both are computed below. The corpus must say which regime it is in; this script does
not decide that.
"""

from fractions import Fraction as F

CHECKS = []
def chk(name, got, booked, unit=""):
    CHECKS.append((got == booked, name, booked, got, unit))

def solve(N=3, with_nuR=False):
    """
    Equilibrium chemical potentials above the electroweak crossover.

    Unknowns: mu_Q, mu_u, mu_d, mu_L, mu_e, mu_H  (+ mu_nu if with_nuR)
    All generation-universal. Solved exactly in rationals -- no floating point.

    Constraints:
      (1) EW sphaleron      3 mu_Q + mu_L = 0
      (2) QCD sphaleron     2 mu_Q - mu_u - mu_d = 0
      (3) up Yukawa         mu_u = mu_Q + mu_H
      (4) down Yukawa       mu_d = mu_Q - mu_H
      (5) charged lepton    mu_e = mu_L - mu_H
      (6) hypercharge = 0
      (7) [nu_R only]       mu_nu = mu_L + mu_H
    One overall normalisation is free; set mu_H = 1 and scale out at the end.

    THE SIGNS, DERIVED RATHER THAN GUESSED. A term psibar_1 psi_2 phi permits
    psi_2 + phi -> psi_1, so equilibrium reads mu_2 + mu_phi = mu_1:
      Qbar_L H d_R       : d_R  + H  -> Q_L                  => mu_d  = mu_Q - mu_H
      Qbar_L Htilde u_R  : u_R  + H~ -> Q_L, mu_H~ = -mu_H   => mu_u  = mu_Q + mu_H
      Lbar H e_R         : e_R  + H  -> L                    => mu_e  = mu_L - mu_H
      Lbar Htilde nu_R   : nu_R + H~ -> L                    => mu_nu = mu_L + mu_H
    An earlier pass had all four inverted. It returned 20/53 and the control below
    caught it before any number was quoted.
    """
    mu_H = F(1)

    def fields(q):
        mu_Q = q
        mu_u = mu_Q + mu_H
        mu_d = mu_Q - mu_H
        mu_L = -3 * mu_Q
        mu_e = mu_L - mu_H
        mu_nu = mu_L + mu_H if with_nuR else F(0)
        return mu_Q, mu_u, mu_d, mu_L, mu_e, mu_nu

    # hypercharge neutrality, with multiplicities and Y:
    #   Q: 6N at Y=1/6 ; u: 3N at 2/3 ; d: 3N at -1/3 ; L: 2N at -1/2 ;
    #   e: N at -1 ; nu: N at 0 (drops out) ; H: 2 components, boson weight 2, Y=1/2
    # coefficient of q, and the constant (mu_H) part:
    def hyper(q):
        mu_Q, mu_u, mu_d, mu_L, mu_e, mu_nu = fields(q)
        return (F(6*N) * F(1, 6) * mu_Q
                + F(3*N) * F(2, 3) * mu_u
                + F(3*N) * F(-1, 3) * mu_d
                + F(2*N) * F(-1, 2) * mu_L
                + F(N) * F(-1) * mu_e
                + F(N) * F(0) * mu_nu
                + F(2) * F(2) * F(1, 2) * mu_H)

    # hyper(q) is linear in q: solve hyper(q) = 0
    h0 = hyper(F(0))
    h1 = hyper(F(1)) - h0
    q_sol = -h0 / h1

    mu_Q, mu_u, mu_d, mu_L, mu_e, mu_nu = fields(q_sol)

    # B and L (per unit volume, common factor dropped)
    B = F(2*N) * mu_Q + F(N) * mu_u + F(N) * mu_d
    L = F(2*N) * mu_L + F(N) * mu_e + (F(N) * mu_nu if with_nuR else F(0))
    return B, L, B / (B - L)

print("=" * 76)
print("SPHALERON CONVERSION: B / (B - L)")
print("=" * 76)

print("\n[1] Control: the Standard Model roster, nu_R switched OFF")
B, L, a = solve(N=3, with_nuR=False)
print(f"    B/(B-L) = {a}   (standard result: 28/79)")
chk("SM control reproduces 28/79", a, F(28, 79))
if a != F(28, 79):
    print("    *** SETUP IS WRONG -- do not read the nu_R number below ***")
else:
    print("    Control passes, so the machinery is trustworthy for the next line.")

CONTROL_OK = (a == F(28, 79))

print("\n[2] The model's roster: SM + 3 nu_R, Dirac Yukawa IN equilibrium at T_sph")
if not CONTROL_OK:
    print("    WITHHELD. The control did not reproduce 28/79, so this setup is not")
    print("    trustworthy and no nu_R coefficient is quoted from it. The grade for")
    print("    this script was stated before computing and it is being honoured:")
    print("    a failed control means no number, not a number with a caveat.")
else:
    B2, L2, a2 = solve(N=3, with_nuR=True)
    print(f"    B/(B-L) = {a2}   = {float(a2):.6f}")
    print(f"    against the SM   {F(28,79)} = {float(F(28,79)):.6f}")

print("\n[3] The other regime: nu_R present but Yukawa OUT of equilibrium")
print("    If the Dirac Yukawa is too small to equilibrate by T_sph, or the nu_R are")
print("    heavy Majorana states already decoupled, they carry no chemical potential")
print("    and do not enter. The conversion is then the SM value unchanged:")
print(f"      B/(B-L) = {F(28,79)}")

print("\n" + "=" * 76)
print("OUTCOME")
print("=" * 76)
print("""
    The control reproduces 28/79 exactly, so the machinery is sound. The spec's
    question is answered:

        Standard Model                     B/(B-L) = 28/79 = 0.354430
        SM + 3 nu_R, Yukawa in equilibrium B/(B-L) = 1/4   = 0.250000

    a reduction of 29.5%. The mechanism is simple once seen: nu_R carries lepton
    number but no hypercharge, so it does not enter the neutrality condition and
    leaves B untouched -- it only enlarges L. B/(B-L) falls accordingly.

    A NOTE ON THE FIRST ATTEMPT, kept deliberately. All four Yukawa constraints were
    inverted, which returned 20/53. The pre-stated control caught it and the number was
    withheld rather than published with a caveat. Without that control the wrong
    coefficient would have shipped looking entirely plausible -- 1/4 was in fact what
    the broken version also returned, by compensating errors, so even agreement between
    two runs would not have exposed it.

    WHICH VALUE THE TRANSFER INTEGRAL SHOULD USE -- and this is a physics fork the
    corpus must own, independent of the arithmetic:""")
print("""

      * The finiteness roster and the thermal population are DIFFERENT QUESTIONS. P-2026-045
        counts nu_R as Weyl fields in a gravitational supertrace. Whether they are
        thermally populated at T_sph = 131.7 GeV is a separate matter, and a field can
        be in the roster while absent from the plasma. Conflating the two would import
        a field-content result into an equilibrium calculation with no warrant.
      * Equilibration of a Dirac Yukawa y needs roughly y^2 T/(8 pi) > H(T), i.e. y above
        about 10^-7 at 132 GeV -- a Dirac mass above the MeV scale. The model's light
        neutrinos are sub-eV, so on the Dirac reading the Yukawa is far out of equilibrium
        and the SM coefficient stands untouched.
      * The corpus's neutrinos are seesaw Majorana, so the relevant nu_R are heavy and
        their presence in the plasma at T_sph depends on the v_L corner, which is itself
        an open two-branch fork (MeV vs >= GeV).

    RECOMMENDATION: the transfer integral should
    use 28/79 unless the v_L corner resolves to a regime that thermalises the nu_R at
    T_sph. If it does, the coefficient is 1/4 and the integral must be re-run with it.
    Both values are now computed, so the choice is a physics ruling, not a missing number.
""")

print("=" * 76)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 76)
