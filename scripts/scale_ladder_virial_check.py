#!/usr/bin/env python3
"""
Is there an energy cascade to derive?   (docket #11, the dynamical half)

GRADE STATED BEFORE COMPUTING (protocol check 33)
-------------------------------------------------
MATH_SPINE records the scale ladder's static half as built and its dynamical half --
"the energy cascade" -- as still open. Before attempting the dynamical half, ask what
the static half actually contains, because a cascade needs something to cascade
BETWEEN.

What would count as the task being live: the rungs carry content beyond a single
identity, so a dynamical law connecting them could say something.
What would count as the task having no object: the rungs are all one identity applied
repeatedly, in which case there is nothing for a cascade to be the dynamics OF, and
#11 should be closed as malformed rather than worked.

This script cannot support the ladder. It can only find out whether the ladder is
a claim or a restatement.
"""

import math

G      = 6.67430e-11
C      = 299792458.0
M_SUN  = 1.98892e30
AU     = 1.495978707e11
ALPHA  = 1.0 / 137.035999084

CHECKS = []
def chk(name, got, booked, tol, unit=""):
    ok = abs(got) <= tol if booked == 0 else abs(got - booked) / abs(booked) <= tol
    CHECKS.append((ok, name, booked, got, unit))

print("=" * 76)
print("THE SCALE LADDER: CLAIM OR RESTATEMENT?")
print("=" * 76)

print("""
  The ladder's column is  E_bind/(m c^2) = (1/2) alpha_eff^2,  with alpha_eff defined
  as "the rung's own coupling -- ORBITAL VELOCITY IN c UNITS for gravity, the gauge
  coupling for atoms, the cosmic coupling for the universe".
""")

# ---------------------------------------------------------------- gravity rungs
print("[1] The gravitational rungs")
print("    For a circular orbit, E_bind = (1/2) m v^2 exactly (virial theorem).")
print("    The ladder defines alpha_eff = v/c. Substituting:\n")
print("        E_bind/(m c^2) = (1/2) v^2/c^2 = (1/2) alpha_eff^2\n")
print("    That is not a result. It is the definition of alpha_eff substituted into")
print("    the virial theorem. It holds for ANY gravitationally bound circular orbit")
print("    in ANY universe, with or without this model.\n")

print("      rung                 r            v (m/s)    alpha_eff    (1/2)a^2     E_b/mc^2")
rungs = [
    ("solar system, 40 AU", 40 * AU,          M_SUN),
    ("planet orbit, 1 AU",  1 * AU,           M_SUN),
    ("Earth orbit check",   1 * AU,           M_SUN),
]
for lab, r, M in rungs:
    v      = math.sqrt(G * M / r)
    a_eff  = v / C
    half_a = 0.5 * a_eff ** 2
    # independently: E_bind/(m c^2) for a circular orbit = GM/(2 r c^2)
    eb     = G * M / (2.0 * r * C ** 2)
    print(f"      {lab:20s} {r:.3e}  {v:9.1f}   {a_eff:.4e}   {half_a:.4e}  {eb:.4e}")
    chk(f"virial identity, {lab}", half_a, eb, 1e-12)

print("\n    The last two columns agree to machine precision at every rung, because")
print("    they are the same expression. No physics passed between them.")

# ---------------------------------------------------------------- the atom
print("\n[2] The atomic rung")
print("    Hydrogen's binding energy is E_b = (1/2) alpha^2 m_e c^2 -- the Rydberg,")
print("    which is how the Bohr radius is DERIVED. Dividing by m_e c^2:\n")
print("        E_b/(m_e c^2) = (1/2) alpha^2\n")
ryd_over_mec2 = 0.5 * ALPHA ** 2
print(f"    (1/2) alpha^2 = {ryd_over_mec2:.6e}")
print(f"    13.6057 eV / 510999 eV = {13.605693 / 510998.95:.6e}")
chk("atom rung is the Rydberg", ryd_over_mec2, 13.605693 / 510998.95, 1e-4)
print("\n    Same structure: the rung restates the definition of the Rydberg.")

# ---------------------------------------------------------------- the universe
print("\n[3] The universe rung -- the file already concedes this one")
print("    PRTOE_scale_ladder.md says outright: 'this is an identity, not a check:")
print("    the model's dark-energy relation IS rho_Lambda^(1/4) = (1/2) alpha_c^2 M_2,")
print("    so dividing it by M_2 returns (1/2) alpha_c^2 by construction.'\n")
a_c = 3 * ALPHA
print(f"    (1/2) alpha_c^2 = {0.5 * a_c**2:.4e}   (table: 2.40e-4)")
chk("universe rung", 0.5 * a_c ** 2, 2.3963e-4, 1e-3)

# ---------------------------------------------------------------- verdict
print("\n" + "=" * 76)
print("VERDICT on #11")
print("=" * 76)
print("""
    THE TASK HAS NO OBJECT, and should be closed as malformed rather than worked.

    Every rung of the ladder is the same identity:

      * gravitational rungs -- alpha_eff is DEFINED as v/c, so (1/2)alpha_eff^2 is
        the virial theorem with a symbol renamed. Verified to machine precision.
      * the atomic rung -- (1/2)alpha^2 is the Rydberg, i.e. how the Bohr radius is
        derived in the first place.
      * the universe rung -- definitional by the model's own dark-energy relation,
        as the ladder file already states.

    So "every bound structure obeys the Bohr skeleton" reduces to "every bound
    structure obeys the virial theorem", which is true, old, and carries no
    model-dependent content. The five rungs are one statement written five times.

    An ENERGY CASCADE would be the dynamics connecting the rungs -- energy actually
    flowing between them. But the rungs are not coupled: a hydrogen atom's binding is
    not dynamically connected to a galaxy cluster's. They merely both satisfy a
    relation that all bound systems satisfy. There is no cascade to derive because
    there is no ladder in the physical sense, only a table of systems each obeying
    the same textbook theorem.

    WHAT SURVIVES, and it is worth keeping separately: the HINGE. xi = 402 AU falling
    between the planetary system and the Oort cloud is a real statement about where
    the medium's coherence length sits relative to structures, and it does carry
    model-dependent content. That is a fact about xi, not about a ladder, and it
    should be filed with the medium's properties rather than propping up a column
    that turns out to be the virial theorem.

    Recommendation: close #11 as having no object; keep the hinge; drop the ladder's
    claim to be "one grammar spanning everything", since the grammar is Newton's.
""")

print("=" * 76)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 76)
