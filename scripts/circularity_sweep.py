#!/usr/bin/env python3
"""
Circularity sweep: which headline landings recover their own inputs?

GRADE STATED BEFORE COMPUTING (protocol check 33)
-------------------------------------------------
Two claims died today by the same mechanism -- a quantity fixed by demanding X, then
reported as "landing on" X:

  * Psi_0 redshifting onto Omega_DM. Psi_0 was FIXED by demanding today's abundance
    (PHYSICS_DOMAINS row 70), so recovering it inverts its own defining relation.
  * The scale ladder. alpha_eff is DEFINED as v/c, so (1/2)alpha_eff^2 is the virial
    theorem restated, and the universe rung is definitional by the model's own
    dark-energy relation.

Both were found by accident while doing something else. That is not a method. This
script audits the remaining headline landings deliberately, asking one question of
each: WAS ANY INPUT FIXED BY DEMANDING THE OUTPUT?

Evidence class: PROVENANCE AUDIT. It cannot confirm any claim. It can only sort them
into circular, clean, or needing an owner's ruling. A clean verdict here does not make
a landing right -- it only means the landing is not empty by construction.

What would count as success: every headline landing gets a definite provenance verdict.
What would count as failure: verdicts that depend on judgement calls I cannot resolve
from the corpus, which must then be reported as unresolved rather than guessed.
"""

import math

ALPHA   = 1.0 / 137.035999084
ALPHA_C = 3.0 * ALPHA
M_E     = 510998.95            # eV

CHECKS = []
def chk(name, got, booked, tol, unit=""):
    ok = abs(got) <= tol if booked == 0 else abs(got - booked) / abs(booked) <= tol
    CHECKS.append((ok, name, booked, got, unit))

print("=" * 78)
print("CIRCULARITY SWEEP OF THE HEADLINE LANDINGS")
print("=" * 78)

# ---------------------------------------------------------------- calibration
print("\n[0] Calibration: the two known-bad cases, to confirm the test detects them")
print("""
    (a) Psi_0 -> Omega_DM.  Input Psi_0 was fixed BY DEMANDING Omega_DM.
        Test verdict: CIRCULAR. Detected -- the defining relation is stated in the
        corpus in words ("fixed by demanding today's abundance").

    (b) The scale ladder.  Input alpha_eff is DEFINED as v/c.
        Test verdict: DEFINITIONAL. Detected -- substituting the definition returns
        the virial theorem identically.

    Both are caught by reading the definition of each input. That is the whole test,
    and it is cheap. It should have been run on everything long ago.
""")

# ---------------------------------------------------------------- the flagship
print("[1] THE FLAGSHIP: rho_Lambda^(1/4) = (d^2/2) alpha^4 T_c")
print("    Recorded: 2.2599 meV against the observed 2.25 meV, +0.44%.\n")

TAU  = 0.5 * math.log(2.0)
T_C  = TAU * M_E
rho4 = (9.0 / 2.0) * ALPHA ** 4 * T_C

print(f"    tau  = (1/2)ln2         = {TAU:.7f}")
print(f"    T_c  = tau * m_e        = {T_C/1e3:.3f} keV")
print(f"    rho^(1/4) = (9/2)a^4 T_c= {rho4*1e3:.4f} meV")
print(f"    observed                = 2.25 meV")
print(f"    offset                  = {(rho4*1e3/2.25 - 1)*100:+.2f}%")
chk("T_c from tau", T_C / 1e3, 177.099, 1e-4, "keV")
chk("rho_Lambda^(1/4)", rho4 * 1e3, 2.2599, 1e-3, "meV")

print("""
    INPUT PROVENANCE, one line each:
      alpha   -- measured, external. Clean.
      m_e     -- measured, external. Clean.
      d = 3   -- the spatial dimension. Clean (and note the corpus records the
                 observed rho_Lambda giving d = 2.993, which is the +0.44% restated,
                 NOT an independent fit).
      tau     -- (1/2)ln2, from the Koide null A = sqrt(2) <=> R_c = M_c. That chain
                 runs on CHARGED LEPTON MASSES and contains no cosmological input.

    VERDICT: NOT CIRCULAR. No input was fixed by demanding rho_Lambda. The landing is
    a real arithmetic coincidence between a lepton-sector constant and a cosmological
    one, which is what makes it interesting and also what makes it fragile.
""")

# the honest precision question, separately
print("    But the PRECISION deserves the same treatment the anchor got today.")
print("    The theory side has no free parameter, so +0.44% is not a tolerance --")
print("    it is a discrepancy. Against the observational error on rho_Lambda^(1/4):")
# Omega_Lambda known to ~1%; rho^(1/4) scales as Omega^(1/4)
obs_frac = 0.01 / 4.0
print(f"      Omega_Lambda to ~1%  ->  rho^(1/4) to ~{obs_frac*100:.2f}%")
print(f"      the offset is {(rho4*1e3/2.25 - 1)*100:.2f}%, i.e. ~{((rho4*1e3/2.25 - 1))/obs_frac:.1f} sigma")
chk("offset in units of obs error", (rho4 * 1e3 / 2.25 - 1) / obs_frac, 1.77, 0.1)
print("""
    So the flagship is a ~1.8 sigma OFFSET, not an agreement. The corpus already grades
    it "an existence claim, not a precision one", which is the right call -- but the
    wording "lands on the observed scale" reads as success, and at 1.8 sigma it is
    better described as landing on the right SCALE while missing the VALUE.
""")

# ---------------------------------------------------------------- A_s
print("[2] A_s = (alpha_c/4 pi k)^3")
A_S = (ALPHA_C / (4.0 * math.pi * 1.36461191)) ** 3
print(f"    computed = {A_S:.4e}   (Planck: 2.1e-9)")
chk("A_s closed form", A_S, 2.1e-9, 0.15)
print("""
    INPUT PROVENANCE:
      alpha_c -- 3*alpha, a registered bet (P-2026-040). Not fitted to A_s.
      k       -- derived in hierarchy 6c from the screening constant. The corpus
                 records three concordant readings, 1.360 / 1.36461 / 1.3602, of which
                 ONE (1.360) is the A_s-measured value.

    VERDICT: NOT CIRCULAR, but with a caution the corpus itself carries -- if k is ever
    quoted as A_s-derived AND A_s is then quoted as a k-prediction, that is a loop.
    Hierarchy 6c is explicit that the sharp precision rides the CLOSED-FORM k, and that
    the A_s-measured k gives only 1.39 +/- 0.16 (consistent, not sharp). The fence is
    already in place. It must not be removed.
""")

# ---------------------------------------------------------------- epsilon
print("[3] epsilon = c * f_bar * alpha_c = 27 alpha / 5 pi")
eps = (9.0 / 10.0) * (2.0 / math.pi) * ALPHA_C
print(f"    (9/10)(2/pi)(3 alpha) = {eps*100:.4f}%   and 27 alpha/5 pi = "
      f"{27*ALPHA/(5*math.pi)*100:.4f}%")
chk("epsilon closed form", eps * 100, 1.2543, 1e-3, "%")
chk("epsilon equals 27a/5pi", eps, 27 * ALPHA / (5 * math.pi), 1e-12)
print("""
    INPUT PROVENANCE:
      alpha_c = 3 alpha -- registered bet. Clean of epsilon.
      f_bar = 2/pi      -- the winding average, <|cos|>. Independent geometry.
      c = 9/10          -- a COUNTING choice over the census. The external review calls
                          this "a counting choice, not forced", and the corpus's own
                          docket #6 closed it as a democratic count rather than a
                          derivation from first principles.

    VERDICT: NOT CIRCULAR -- epsilon is not used to fix any of the three -- but the
    product inherits c's status. If c = 9/10 is a choice, epsilon is a motivated ansatz
    whose agreement with the fitted epsilon is a test the model can pass or fail, not a
    derivation. That is a weaker claim than "derived" and should be worded as such.
""")

# ---------------------------------------------------------------- the mass
print("[4] The ultralight mass, 'confirmed three independent ways'")
print("""
    INPUT PROVENANCE of each leg:
      (1) xi = hbar/(m c_s)  -- DEFINED from m, and the "recorded 402 AU" is itself
          computed from m with the same c_s. Comparing 398 against 402 compares one
          computation from m with another computation from m. CIRCULAR.
      (2) the Schive core radius -- external relation goes as 1/m, the model's own
          ground-state relation as 1/m^2. Different exponents intersect at one m, so
          agreement WOULD pin m -- provided the model's normalisation was not set from
          this comparison. Provenance not established. UNRESOLVED.
      (3) the superradiance band -- priced elsewhere in the SAME dependency-tree row
          as an adverse exposure where "the model brings no defence". It cannot be
          independent support and an unmet constraint at once. NOT SUPPORT.

    VERDICT: the wording is withdrawn. What stands is the onset clock plus at most one
    unresolved consistency check.

    NOTE, against the model's interest: DOMAIN_COVERAGE used the three-way pinning to
    argue the superradiance confrontation "cannot be relieved by moving it". Weakening
    the pin weakens THAT argument too, so this correction loosens an adverse constraint
    the corpus had been taking on the chin. Both halves are recorded.
""")

# ---------------------------------------------------------------- the neutrino tie
print("[5] The neutrino/dark-energy tie, m_1 = rho_Lambda^(1/4)")
print("""
    An external review called this "a scale coincidence dressed as a lock". The corpus
    answers it directly and the answer is already in the text:

      DERIVATION_HUNT: "What the tie constrains is the COMBINATION, not either
      constant... the seat constant is not 'kappa_m ~ 1' but a ratio, kappa_m =
      kappa_V^(1/4), and neither factor is separately fixed by it... the recorded 2.2%
      tolerance leaves kappa_V free across a factor 1.09 and constrains kappa_m and
      kappa_V individually not at all. Any attempt on 'the seat constant' must target
      the ratio; computing kappa_m alone closes nothing."

    And the neutrino sector states plainly: "What the model does not do is derive the
    value 2.25 meV itself... The claim is that one un-derived number does two jobs that
    standard cosmology treats as unrelated, not that the number is explained."

    VERDICT: NOT CIRCULAR, and NOT OVERCLAIMED. The tie quotes the OBSERVED 2.25 meV
    rather than the theory chain's 2.2599, so it does not inherit the flagship's 0.44%
    offset either. This is the most carefully fenced claim examined in the sweep, and
    the criticism is answered by the corpus's own wording rather than needing a fix.
""")

# ---------------------------------------------------------------- summary
print("=" * 78)
print("SWEEP RESULT")
print("=" * 78)
print("""
      claim                          verdict            note
      ---------------------------------------------------------------------------
      Psi_0 -> Omega_DM              CIRCULAR           caught 2026-07-28, relabelled
      the scale ladder               DEFINITIONAL       caught 2026-07-28, retired
      m "confirmed three ways"        1 CIRCULAR,       xi is defined from m; Schive
                                      1 UNRESOLVED,     unresolved; superradiance is
                                      1 NOT SUPPORT     the exposure itself
      rho_Lambda = (9/2)a^4 T_c      not circular       but a ~1.8 sigma offset, not
                                                        an agreement
      A_s = (alpha_c/4 pi k)^3       not circular       fence required: never quote k
                                                        as A_s-derived and A_s as a
                                                        k-prediction together
      epsilon = c f_bar alpha_c      not circular       inherits c = 9/10's status as
                                                        a counting choice; "ansatz",
                                                        not "derived"
      m_1 = rho_Lambda^(1/4)         not circular       already correctly fenced --
                                                        constrains a ratio, and the
                                                        corpus says so itself

    Of six claims: two empty, one part-empty, three clean. Of the three clean, one
    needed weaker wording (the flagship is an offset, not a landing), one needs its
    fence kept (A_s), and one needed nothing at all (the neutrino tie, which was
    already graded better than the criticism assumed).

    The cheap lesson: this test is one line per input -- "what fixed this?" -- and it
    caught two dead claims that had stood for months. It belongs in the protocol and
    should be run on every landing before it is written up, not after.
""")

print("=" * 78)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 78)
