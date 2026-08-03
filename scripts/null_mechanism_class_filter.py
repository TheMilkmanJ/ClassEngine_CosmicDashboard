"""Why all seven recorded mechanisms for the null failed: they share a property the answer cannot have.

Two constraints on whatever makes the Z3-graded norm vanish are now on record, and they were
derived independently of each other and of the candidate list:

  (A) CHARGE-COUPLED. The neutrino triple cannot sit on the cone for any lightest mass (Q_nu tops
      out at 0.585 against 2/3), from which T6 concludes the cone "acts in the charged sector
      specifically". The basement reaches the same place from screening: Thomas-Fermi weights
      carriers by charge squared, so a neutrino cone is worth 2.N_c.q^2 = 0.

  (B) EXACT, NOT BALANCED. Q is held to ~1e-5. Statistical and equilibrium mechanisms deliver a
      value with fluctuations around it, and the fluctuation here would need suppressing by four
      orders it has no reason to be. Exactness of that kind comes from a quantity that VANISHES.

This script applies both filters to the recorded dead list.

Run: python3 scripts/null_mechanism_class_filter.py
"""

# (name, retired-on, does the mechanism reference electric charge?, is it a vanishing or a balance?)
DEAD = (
    ("wide-seam / 2D-Potts", "2026-07-17", False, "regime width"),
    ("SOC attractor", "2026-07-17", False, "dynamical attractor"),
    ("medium-w inheritance (w = 1/3 => K = 2V)", "2026-07-17", False, "energy balance"),
    ("quartic virial", "2026-07-17", False, "energy balance"),
    ("harmonic equipartition", "2026-07-17", False, "energy balance"),
    ("CS midpoint", "2026-07-17", False, "energy balance"),
    ("GBM / 1D log gas", "2026-07-17", False, "statistical"),
    ("hand-built (R^2 - 2M^2)^2", "2026-07-17", False, "constructed"),
    ("Komar active-mass balance", "2026-07-17", False, "energy balance"),
    ("topology / lock-6", "2026-07-17", False, "invariant (none equals sqrt2)"),
    ("natural Z3 cubic -g sum(phi^3)", "2026-07-17", False, "potential minimum"),
)

print("=" * 82)
print("THE RECORDED DEAD LIST, AGAINST THE TWO SURVIVING CONSTRAINTS")
print("=" * 82)
print(f"  {'mechanism':<42} {'charge?':>8} {'kind':>26}")
print("  " + "-" * 78)
for name, _, charged, kind in DEAD:
    print(f"  {name:<42} {'yes' if charged else 'NO':>8} {kind:>26}")

n = len(DEAD)
n_charged = sum(1 for _, _, c, _ in DEAD if c)
n_vanish = sum(1 for _, _, _, k in DEAD if "vanish" in k)
print()
print(f"  {n} recorded mechanisms.")
print(f"  referencing electric charge:              {n_charged}")
print(f"  built on a vanishing rather than a balance: {n_vanish}")

print()
print("=" * 82)
print("SO THE LIST IS DEAD AS A CLASS, AND THE CLASS IS NAMEABLE")
print("=" * 82)
print("  Not one of the eleven references electric charge, and not one rests on a quantity that")
print("  vanishes identically. Every single failure was a charge-blind balance -- which is")
print("  exactly the conjunction constraints (A) and (B) forbid.")
print()
print("  That is worth more than eleven separate autopsies. The failures were not eleven bad")
print("  ideas; they were one bad class explored eleven ways, and the corpus's own later work")
print("  -- the neutrino forward test and the screening weight -- says why the class cannot work.")
print()
print("  What the constraints demand together: a CHARGE-COUPLED quantity that VANISHES")
print("  IDENTICALLY. That is the shape of an anomaly-cancellation or index condition, and the")
print("  corpus already carries two objects of exactly that shape for unrelated reasons --")
print("  str[k1] = 0 (Pauli finiteness) and sum Q^2 = 16 over the roster.")
print()
print("  Not a mechanism. A named class with two members already in the building, which is what")
print("  the sector has lacked since 2026-07-17: every attempt since then has drawn from the")
print("  class the evidence excludes.")

print()
print("=" * 82)
print("THE HONEST LIMIT")
print("=" * 82)
print("  The three charged leptons all carry Q = -1, so no charge-weighted sum over them")
print("  vanishes on its own -- sum Q = -3, sum Q^2 = 3. A working mechanism must therefore")
print("  couple charge to something else that distinguishes the seats, and the family grading")
print("  is not available for that (its Z3 charge commutes with chirality; the identification")
print("  died on Nielsen-Ninomiya). So the class is named and its first obstacle is already")
print("  visible, which is the honest state: a direction, not a derivation.")
