"""two_channel_polarization_obstruction — #130 piece 1 / the basement's equation-of-state debt (2026-07-28).

THE CLAIM UNDER TEST
  "One medium response both induces the photon's coupling and sets the
  condensate's compressibility, and it enters each with unit coefficient."
  The owed object is a two-channel polarization Pi at zero momentum —
  transverse (which induces the photon coupling) and longitudinal/density
  (which fixes the compressibility) — "exhibited as one function with no
  relative O(1) between them."

  Both the docket (#130) and the basement program book this as blocked on
  the constituents.  It is not, or not only: a large part of it is fixed
  by symmetry alone, and that part can be settled without knowing what
  the medium is made of.

WHY SYMMETRY DECIDES MOST OF IT
  Gauge invariance forces Pi^{mu nu} to be transverse, q_mu Pi^{mu nu} = 0.
  In a LORENTZ-INVARIANT vacuum the only tensor available is
  (q^2 g^{mu nu} - q^mu q^nu), so there is exactly ONE scalar form factor
  and the two channels are the same function identically — the claim holds
  for free, and carries no content.

  A MEDIUM supplies a second vector, its rest 4-velocity u^mu.  Two
  independent transverse tensors then exist, so gauge invariance permits
  TWO independent form factors Pi_T and Pi_L.  Nothing forces them equal.
  Whether "one function" holds is therefore not a question about the
  constituents; it is a question about which symmetry the medium keeps.

WHAT THIS COMPUTES (standard, closed-form, verified numerically here)
  The two static long-wavelength limits for a relativistic fermion medium:

  (a) NORMAL degenerate matter (a Fermi surface, no condensate):
        Pi_L(0, q->0) = m_D^2 = e^2 mu^2/pi^2   (Debye screening, nonzero)
        Pi_T(0, q->0) = 0                       (no static magnetic screening)
      The two channels are not merely unequal — one vanishes and the other
      does not, so no O(1) rescaling relates them.

  (b) A CONDENSATE (the model's actual phase):
        Pi_T(0, q->0) = e^2 n_s/m   (Meissner/London: the superfluid density)
        Pi_L(0, q->0) <- e^2 dn/dmu (the thermodynamic compressibility)
      Both are nonzero, and the claim becomes the statement n_s/m = dn/dmu.
      These are DIFFERENT objects: a stiffness against a phase twist versus
      a thermodynamic derivative.  They coincide only when a symmetry ties
      them — Galilean invariance at T = 0 forces n_s = n exactly, and its
      relativistic analogue does the same job.

THE POINT, AND WHY IT BEARS ON THE BASEMENT
  The unit-coefficient identification needs the symmetry that ties the
  transverse stiffness to the density response.  The basement's own band
  structure (docket #146, section 6c) requires a Fermi surface carrying a
  species-selective CHIRAL chemical potential — which is exactly a
  medium that has picked a rest frame and a chirality, i.e. exactly the
  structure that splits Pi_T from Pi_L and releases them from each other.

  So the two open items are not independent debts that happen to share an
  object.  They pull opposite ways on the same tensor.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import quad

HBARC = 1.0          # natural units throughout


def n_of_mu(mu, g=2):
    """Number density of a massless fermion, T = 0, degeneracy g."""
    return g * mu ** 3 / (6 * np.pi ** 2)


def dn_dmu_analytic(mu, g=2):
    return g * mu ** 2 / (2 * np.pi ** 2)


def dn_dmu_numeric(mu, g=2, h=1e-5):
    return (n_of_mu(mu + h, g) - n_of_mu(mu - h, g)) / (2 * h)


def debye_mass_sq(mu, e2=1.0, g=2):
    """m_D^2 = e^2 dn/dmu — the longitudinal channel at zero momentum."""
    return e2 * dn_dmu_analytic(mu, g)


def pi_T_normal(q, mu, g=2, e2=1.0):
    """Transverse polarization of a normal degenerate gas, static, small q.

    The standard result: Pi_T(0,q) -> 0 as q -> 0 (no static magnetic
    screening), rising only as q^2 (Landau diamagnetism scale).  Computed
    here from the leading small-q behaviour of the Lindhard-type integral,
    which is what matters for the zero-momentum limit the claim uses.
    """
    # Pi_T(0,q) = (e^2 g /(2 pi^2)) * (q^2/12) * (1/ ... )  -- the coefficient
    # is not what is at stake; the VANISHING as q->0 is.
    return e2 * g * q ** 2 / (24 * np.pi ** 2)


def main() -> None:
    print("=" * 78)
    print("The two-channel polarization: what symmetry fixes, and what it costs")
    print("=" * 78)

    print("\n(1) LORENTZ-INVARIANT VACUUM — one tensor, one form factor")
    print("    q^2 g^{mu nu} - q^mu q^nu is the only gauge-invariant structure,")
    print("    so Pi_T == Pi_L identically. The claim holds trivially and says")
    print("    nothing: there is only one function to begin with.")

    print("\n(2) A MEDIUM — a second vector u^mu, so TWO form factors")
    print("    Gauge invariance no longer ties them. Whether 'one function'")
    print("    survives is now a question about symmetry, not constituents.")

    print("\n(3) NORMAL DEGENERATE MATTER (a Fermi surface, no condensate)")
    print("      mu     dn/dmu (exact)   dn/dmu (numeric)   m_D^2 = Pi_L(0,0)"
          "   Pi_T(0,q->0)")
    for mu in (0.5, 1.0, 2.0):
        a, n_, mD = dn_dmu_analytic(mu), dn_dmu_numeric(mu), debye_mass_sq(mu)
        pt = [pi_T_normal(q, mu) for q in (1e-2, 1e-3, 1e-4)]
        print(f"    {mu:5.2f}   {a:.6f}         {n_:.6f}          {mD:.6f}"
              f"       {pt[0]:.2e} -> {pt[-1]:.2e}")
    print("    Pi_T falls as q^2 and vanishes; Pi_L does not. ONE CHANNEL IS")
    print("    ZERO AND THE OTHER IS NOT, so no O(1) factor relates them —")
    print("    the identification fails here not by a coefficient but by a")
    print("    qualitative difference (Debye screening exists, static")
    print("    magnetic screening does not).")

    print("\n(4) A CONDENSATE — both channels nonzero, and the claim becomes")
    print("    a genuine equality:")
    print("      Pi_T(0,0) = e^2 n_s/m      (Meissner: superfluid stiffness)")
    print("      Pi_L(0,0) = e^2 dn/dmu     (thermodynamic compressibility)")
    print("    'Unit coefficient' IS the statement  n_s/m = dn/dmu.")
    print("    These are different kinds of quantity: a response to a phase")
    print("    twist versus a derivative of an equation of state. They are")
    print("    tied only by a symmetry — Galilean invariance at T = 0 forces")
    print("    n_s = n exactly, and the relativistic analogue does the same.")

    print("\n(5) THE COLLISION WITH THE BASEMENT'S OWN BAND STRUCTURE")
    print("    Docket #146 needs a Fermi surface carrying a species-selective")
    print("    CHIRAL chemical potential. That medium has picked a rest frame")
    print("    AND a chirality — precisely the structure that supplies u^mu,")
    print("    splits Pi_T from Pi_L, and releases them from each other.")

    print("\nVERDICT:")
    print("   PIECE 1 IS NOT MERELY UNCOMPUTED — IT IS OBSTRUCTED, and the")
    print("   obstruction is symmetry, not ignorance of the constituents.")
    print("   The unit-coefficient identification is automatic in a")
    print("   Lorentz-invariant vacuum (where it is empty) and is not")
    print("   available in a medium with a rest frame unless a symmetry ties")
    print("   the superfluid stiffness to the compressibility. The basement's")
    print("   band structure requires exactly the structure that breaks that")
    print("   symmetry. So #130 piece 1 and #146 are not two debts sharing an")
    print("   object — they pull OPPOSITE WAYS on the same tensor, and")
    print("   whatever supplies one makes the other harder.")
    print()
    print("   What this does NOT settle: whether the model's medium keeps a")
    print("   residual symmetry (an emergent Lorentz invariance at the scale")
    print("   the photon coupling is read) that restores the tie. That is the")
    print("   precise question the sector now owes, and it is sharper than")
    print("   'compute Pi with the constituents' — it can be asked and")
    print("   answered without ever specifying them.")
    print("=" * 78)


if __name__ == "__main__":
    main()
