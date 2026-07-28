"""#146's residue: which node pair can be the doped one? The charge weighting decides.

Section 6c asks the host for N_screen = 2 N_0 and records that "exactly two of forty-eight"
species must carry finite density, with nothing selecting the pair. That reading treats
N_screen as a COUNT. It is not one. Thomas-Fermi screening of a gauge field weights each
carrier band by its charge squared,

    m_D^2 = sum_bands (g q_b)^2 N_0,b        ->     N_screen/N_0 = sum_bands q_b^2

and section 6g fixes which gauge field: alpha_c = 3 alpha, "the kernel is not borrowed from
electromagnetism -- it IS electromagnetism, because electromagnetism is the medium." So the
weights are electric charges, the roster's charges are fractional, and quarks carry colour
multiplicity on top. The requirement N_screen = 2 N_0 is therefore a Diophantine condition on
the roster, not a free choice of two species out of forty-eight.

Run: python3 scripts/basement_species_selection.py
"""
import math
from itertools import product

ALPHA_C = 0.0139369 * math.pi / 2

# One generation of the Planck-floor roster, as Dirac species: (name, |q|, colour).
SPECIES = (("charged lepton", 1.0, 1),
           ("neutrino",       0.0, 1),
           ("up-type quark",  2.0 / 3, 3),
           ("down-type quark", 1.0 / 3, 3))
NGEN = 3


def weight(q, nc):
    """N_screen/N_0 contributed by ONE doped Dirac species: two bands, colour, charge^2."""
    return 2 * nc * q * q


print("=" * 76)
print("WHAT ONE DOPED NODE PAIR IS WORTH, SPECIES BY SPECIES")
print("=" * 76)
print(f"  {'species':<18} {'|q|':>7} {'colour':>7} {'N_screen/N_0':>14}")
print("  " + "-" * 50)
for name, q, nc in SPECIES:
    print(f"  {name:<18} {q:7.4f} {nc:7} {weight(q,nc):14.4f}")
print()
print("  A chiral chemical potential on ONE Dirac cone dopes its two chiralities oppositely,")
print("  giving an electron pocket and a hole pocket at the same Fermi level. That is why a")
print("  single cone contributes TWO screening bands while the pair it forms has ONE density")
print("  of states -- section 6c's '2-for-screening, 1-for-pairing' asymmetry, delivered by")
print("  the mechanism rather than assumed. The pockets are the same cone's two halves, so")
print("  they share a velocity: r = v_e/v_h = 1 is automatic, not a further condition.")

print()
print("=" * 76)
print("WHICH COMBINATIONS HIT N_screen = 2 N_0 EXACTLY?")
print("=" * 76)
sols = []
for counts in product(range(NGEN + 1), repeat=len(SPECIES)):
    tot = sum(n * weight(q, nc) for n, (_, q, nc) in zip(counts, SPECIES))
    if abs(tot - 2.0) < 1e-12:
        sols.append(counts)
print(f"  searching all species counts 0..{NGEN} per type ({(NGEN+1)**len(SPECIES)} combinations)")
print()
for counts in sols:
    parts = [f"{n} x {name}" for n, (name, _, _) in zip(counts, SPECIES) if n]
    print(f"    {' + '.join(parts)}")
print()
charged = sorted({(c[0], c[2], c[3]) for c in sols})
print(f"  {len(sols)} solutions, but the neutrino is invisible to the screening (q = 0), so it")
print("  rides free: doped or not, it changes nothing. Collapsing that column leaves")
print(f"  {len(charged)} distinct configurations of the CHARGED sector:")
print()
for nl, nu, nd in charged:
    parts = [f"{n} x {nm}" for n, nm in ((nl, "charged lepton"), (nu, "up-type quark"),
                                         (nd, "down-type quark")) if n]
    print(f"    {' + '.join(parts)}")
print()
print("  Up-type quarks are excluded outright: one costs 8/3, already past 2.")

print()
print("=" * 76)
print("THE TWO SURVIVORS, WEIGHED")
print("=" * 76)
print("  (a) ONE charged lepton. A single cone, one coincidence, no colour.")
print("  (b) ALL THREE down-type quarks. Three cones doped to a common Fermi level -- three")
print("      coincidences rather than one -- and all three carry colour, so the medium would")
print("      acquire a gluon Debye mass alongside the photon's. The kernel section 6c uses is")
print("      the medium's own 1/q^2 Goldstone exchange and carries no colour screening, so (b)")
print("      is not merely less economical: it changes the exchange the derivation runs on.")
print()
print("  So the charge weighting takes '2 of 48, nothing selects them' down to one viable")
print("  configuration: the doped node pair is a CHARGED LEPTON. Which of the three the")
print("  corpus already answers elsewhere -- the electron is the portal, sqrt(sigma_dark) = m_e.")

print()
print("=" * 76)
print("AND IT CORRECTS THE FULL-ROSTER READING OF THE FAILED KILL")
print("=" * 76)
full = NGEN * sum(weight(q, nc) for _, q, nc in SPECIES)
print(f"  Section 6c prices 'the whole roster doped' as N = 24, the 48 Weyl as Dirac")
print(f"  equivalents. Charge-weighted it is not 24 but  sum over the roster = {full:.4f}")
print(f"  which is the recorded sum of squared charges over the 48-Weyl roster, SumQ^2 = 16.")
print("  The screening count and that invariant are the same quantity, which is a check on")
print("  both: one generation contributes 16/3, three give 16.")
print()
k = lambda N: math.log(1 + math.pi / (N * ALPHA_C)) / math.pi
print(f"    k at N = 24 (the counted reading)          {k(24):.5f}")
print(f"    k at N = 16 (the charge-weighted reading)  {k(16):.5f}")
print(f"    k at N = 2  (the booked point)             {k(2):.8f}")
print()
dlnM = lambda N: 1 / (k(2) * ALPHA_C) - 1 / (k(N) * ALPHA_C)
print(f"  anchor at N = 24  x{math.exp(dlnM(24)):.1e}      at N = 16  x{math.exp(dlnM(16)):.1e}")
print("  Both destroy the anchor, so the failed kill stays failed and the verdict is")
print("  unchanged -- but 16 is the right number for it, and it is one the corpus already")
print("  carries for another reason entirely.")
