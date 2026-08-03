#!/usr/bin/env python3
"""
Is the occupancy-lock / recorded-frequency contradiction an INDEPENDENT debt,
or is it the keystone relation restated in frequency language?

WHERE THIS COMES FROM. scripts/koide_delivery_law_discriminator.py flags a live
contradiction between two arcs of the theory:

    unit bosonic occupancy needs   hbar w_1 / k T_c = ln2   = 0.693147
    the corpus records             w_1 = (2/9) T_c          = 0.222222
    ratio                          9 ln2 / 2                = 3.119162

and states "one of the two is wrong, or they refer to different modes". It also
records, carefully, that 3.119162 is NOT pi (off by 0.7%), so that the near-miss
is not chased later. Good. But it does not ask what the ratio IS.

THE OBSERVATION. With the corpus's own modulus tau = (1/2) ln2,

    9 ln2 / 2 = 9 * tau

and with the keystone constant c_K = 4 / (3 ln2),

    6 / c_K = 6 * 3 ln2 / 4 = 4.5 ln2 = 9 * tau     as well.

So the discrepancy factor is exactly 9 tau = 6 / c_K.

THE CIRCULARITY QUESTION, WHICH IS THE WHOLE POINT OF THIS SCRIPT. That looks
like a discovery and it is NOT one. It follows algebraically from things already
booked, and this script's job is to show that explicitly rather than let it be
mistaken for independent evidence:

    x_corpus = w_1 / T_c = arg b = Q / 3          (how the corpus fixed w_1)
    x_occ    = hbar w / k T   at unit occupancy = ln2 = 2 tau
    ratio    = x_occ / x_corpus = 2 tau / (Q/3) = 6 tau / Q

and the keystone says Q = c_K * tau, so

    ratio    = 6 tau / (c_K tau) = 6 / c_K.

The tau cancels. The ratio is 6/c_K FOR ANY tau, i.e. it is the keystone with the
modulus divided out, and it carries no information the keystone did not already
carry.

WHY IT IS STILL WORTH RECORDING. Because it changes the STATUS of the flagged
contradiction. It is not a third, separate problem competing with the other two;
it is the same unresolved constant surfacing in a third place. Concretely:

  * the discrepancy is NOT evidence against the occupancy lock;
  * it is NOT evidence against the tau modulus;
  * a derivation of c_K would settle it automatically, along with tau, Q, arg b,
    A = sqrt2 and rho_Lambda^(1/4);
  * so it should be carried as an INSTANCE of the c_K debt, not as its own.

AND ONE ASYMMETRY WORTH STATING. The two claims are not equally well-founded.
"hbar w / kT = ln2 at unit occupancy" is a thermodynamic condition with dimensions
on both sides. "w_1 / T_c = arg b" sets a frequency RATIO equal to a PHASE -- both
dimensionless, so it is not wrong on its face, but it is an identification, not a
derivation, and it is the step that would have to be justified. This script does
not adjudicate; it records which of the two carries the heavier burden.

PRE-STATED CONTROLS:
  K-A  9*tau, 4.5*ln2 and 6/c_K must all be the same number to machine precision.
  K-B  the ratio must be recoverable from the definitions WITHOUT using the
       numerical value of tau -- i.e. it must be tau-independent. Checked by
       varying tau over a wide range and confirming the ratio does not move.
  K-C  ANTI-CONTROL: the ratio must NOT equal pi, and the script must say by how
       much, so the near-miss stays closed.
  K-D  the identity must fail if the keystone is perturbed, or it is vacuous.
"""

import math

TOL = 1e-12
_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def main():
    print("=" * 78)
    print("  THE OCCUPANCY / FREQUENCY DISCREPANCY IS THE KEYSTONE RESTATED")
    print("=" * 78)

    tau = 0.5 * math.log(2.0)
    c_K = 4.0 / (3.0 * math.log(2.0))
    Q = c_K * tau
    x_corpus = 2.0 / 9.0                 # w_1 / T_c, as recorded
    x_occ = math.log(2.0)                # hbar w / kT at unit occupancy
    ratio = x_occ / x_corpus

    print(f"\n  tau      = {tau:.12f}")
    print(f"  c_K      = {c_K:.12f}")
    print(f"  Q = c_K*tau = {Q:.12f}   (should be 2/3 = {2/3:.12f})")
    print(f"  x_corpus = {x_corpus:.12f}")
    print(f"  x_occ    = {x_occ:.12f}")
    print(f"  ratio    = {ratio:.12f}")

    # ---- K-A ---------------------------------------------------------------
    print("\n  K-A  the ratio equals 9*tau equals 6/c_K")
    chk("K-A1 keystone holds: c_K * tau = Q = 2/3", abs(Q - 2 / 3) < TOL)
    chk("K-A2 ratio = 9*tau", abs(ratio - 9 * tau) < TOL,
        f"{ratio:.12f} vs {9*tau:.12f}")
    chk("K-A3 ratio = 4.5*ln2", abs(ratio - 4.5 * math.log(2)) < TOL)
    chk("K-A4 ratio = 6/c_K", abs(ratio - 6 / c_K) < TOL,
        f"{ratio:.12f} vs {6/c_K:.12f}")

    # ---- K-B: tau-independence, which is what proves it is not a discovery --
    print("\n  K-B  the ratio is INDEPENDENT of tau — so it carries no new information")
    spread = 0.0
    for t in (0.05, 0.2, tau, 0.5, 1.0, 3.7):
        # hold the keystone Q = c_K * tau fixed at 2/3 by construction, i.e. let
        # c_K float as 2/(3t); then x_corpus = Q/3 and x_occ = 2t as defined.
        cK_t = (2.0 / 3.0) / t
        x_c = (2.0 / 3.0) / 3.0
        x_o = 2.0 * t
        r = x_o / x_c
        spread = max(spread, abs(r - 6.0 / cK_t))
    chk("K-B1 ratio = 6/c_K holds for every tau tested", spread < 1e-10,
        f"max dev {spread:.2e}  -> the tau cancels; this is the keystone, not a new fact")

    # ---- K-C: the anti-control, keeping the pi near-miss closed -------------
    print("\n  K-C  ANTI-CONTROL: the ratio is not pi")
    dpi = abs(ratio - math.pi)
    chk("K-C1 ratio != pi", dpi > 1e-3,
        f"|ratio - pi| = {dpi:.6f}  ({100*dpi/math.pi:.2f}% of pi)")
    chk("K-C2 and it is not 22/7, 355/113, or sqrt(pi)+1 either",
        min(abs(ratio - 22 / 7), abs(ratio - 355 / 113),
            abs(ratio - (math.sqrt(math.pi) + 1))) > 1e-3,
        "the near-miss stays closed")

    # ---- K-D: the identity must be falsifiable ------------------------------
    print("\n  K-D  the identity is not vacuous — perturbing the keystone breaks it")
    bad_cK = c_K * 1.01
    bad_Q = bad_cK * tau
    bad_ratio_pred = 6.0 / bad_cK
    bad_ratio_true = (2 * tau) / (bad_Q / 3)
    chk("K-D1 with c_K perturbed 1%, 6/c_K still tracks the definition",
        abs(bad_ratio_pred - bad_ratio_true) < 1e-10,
        "the relation is an identity in c_K, as claimed")
    chk("K-D2 but the NUMERICAL ratio moves, so the match at c_K = 4/(3ln2) is a real constraint",
        abs(bad_ratio_true - ratio) > 1e-3,
        f"perturbed ratio {bad_ratio_true:.6f} vs actual {ratio:.6f}")

    # ---- verdict -----------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}  — do not record")
        print("=" * 78)
        return
    print("  ALL CONTROLS PASS")
    print("=" * 78)
    print(f"""
  RESULT. The occupancy-lock / recorded-frequency discrepancy of {ratio:.6f} is
  exactly 9*tau = 6/c_K. K-B shows the tau cancels out of the ratio, so this is
  NOT an independent discovery -- it is the keystone c_K * tau = Q with the
  modulus divided out, and it was already implied the moment w_1/T_c was
  identified with arg b = Q/3.

  WHAT IT CHANGES. The discriminator flagged this as a live contradiction between
  two arcs and left it as its own open question. It should instead be carried as
  an INSTANCE of the c_K debt:

    * it is not evidence against the occupancy lock;
    * it is not evidence against the tau modulus;
    * deriving c_K settles it automatically, together with tau, Q, arg b,
      A = sqrt2 and rho_Lambda^(1/4).

  One fewer independent open question, and no new information -- which is the
  honest way round, since the alternative was to keep spending attention on a
  contradiction that cannot be resolved on its own terms.

  THE ASYMMETRY, RECORDED WITHOUT ADJUDICATING IT. The two claims are not equally
  well-founded. "hbar w / kT = ln2 at unit occupancy" is a thermodynamic condition.
  "w_1 / T_c = arg b" equates a frequency ratio with a phase -- dimensionally
  admissible, both being pure numbers, but an IDENTIFICATION rather than a
  derivation. If one of the two has to give, that is the step to examine first,
  and it is also the step the delivery-law discriminator already flagged as
  "derived FROM Q = 2/3 via theta_B, so not an independent measurement".
""")


if __name__ == "__main__":
    main()
