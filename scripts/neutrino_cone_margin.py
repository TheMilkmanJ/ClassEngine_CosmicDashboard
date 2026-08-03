"""Can the neutrino triple ever sit on the cone, and what does the answer say about the selector?

Two questions in one computation.

(1) The emergent-Z3 reading needs a fourth mass governed by the same node, and the neutrinos are
    the only candidate. T6 records that the forward test fails -- Q_nu = 0.458 at m1 = 2.25 meV,
    and "no m1 brings it to 2/3". That is a proof if the maximum over m1 falls short, so compute
    the maximum.

(2) If it does fall short, the corpus's own conclusion is that "whatever pins the cone acts in the
    charged sector specifically". That is the same selector the basement's screening picks out for
    an unrelated reason -- Thomas-Fermi weights by charge squared, so neutrinos contribute nothing.
    Two sectors, arrived at independently, naming electric charge.

Run: python3 scripts/neutrino_cone_margin.py
"""
import math

DM21 = 7.53e-5      # eV^2, solar
DM31 = 2.53e-3      # eV^2, atmospheric (normal ordering)


def Q_of(m1):
    m2 = math.sqrt(m1 * m1 + DM21)
    m3 = math.sqrt(m1 * m1 + DM31)
    s = [math.sqrt(m) for m in (m1, m2, m3)]
    return (m1 + m2 + m3) / sum(s) ** 2, (m1, m2, m3)


print("=" * 74)
print("THE NEUTRINO KOIDE RATIO AGAINST THE LIGHTEST MASS")
print("=" * 74)
print(f"  {'m1 [eV]':>12}  {'m2 [eV]':>10}  {'m3 [eV]':>10}  {'sum m [eV]':>11}  {'Q_nu':>9}")
print("  " + "-" * 62)
for m1 in (0.0, 1e-3, 2.25e-3, 5e-3, 1e-2, 3e-2, 1e-1):
    q, (a, b, c) = Q_of(m1)
    print(f"  {m1:12.4g}  {b:10.6f}  {c:10.6f}  {a+b+c:11.6f}  {q:9.5f}")

print()
q_ref, _ = Q_of(2.25e-3)
print(f"  at the recorded m1 = 2.25 meV:  Q_nu = {q_ref:.5f}   (T6 records 0.458)")

print()
print("=" * 74)
print("THE MAXIMUM, WHICH IS WHAT MAKES IT A PROOF")
print("=" * 74)
best_m1, best_q = 0.0, Q_of(0.0)[0]
m = 0.0
while m < 0.5:
    q, _ = Q_of(m)
    if q > best_q:
        best_q, best_m1 = q, m
    m += 1e-5
print(f"  Q_nu is largest at m1 = {best_m1:.5g} eV, where it reaches {best_q:.5f}")
print(f"  the cone requires                                        {2/3:.5f}")
print(f"  shortfall                                                {(1-best_q/(2/3))*100:.1f}%")
print()
print("  Q_nu falls monotonically from its m1 = 0 value toward 1/3 as the spectrum degenerates,")
print("  so the maximum is the massless-lightest limit and NO m1 reaches 2/3. The corpus's")
print("  statement is a proof, not an observation, and the margin is not marginal.")

print()
print("=" * 74)
print("WHAT THAT DOES TO THE TWO OPEN THREADS")
print("=" * 74)
print("  (1) The fourth handle does not exist. The emergent-Z3 reading needed a further mass")
print("      governed by the same node; the neutrino triple cannot be on that node for any")
print("      lightest mass, so the reading stays untestable inside the corpus's structure.")
print()
print("  (2) But the same result confirms the selector from a second direction. T6 concludes")
print("      from the neutrino failure that 'whatever pins the cone acts in the charged sector")
print("      specifically'. The basement reaches the same place for an unrelated reason: screening")
print("      weights carriers by charge squared, so a neutrino cone contributes 2.N_c.q^2 = 0 and")
print("      cannot be the doped pair. Two sectors, two arguments, one selector -- electric charge.")
print()
print("      That is worth more than it looks. The charge-weighted selection was derived in the")
print("      basement from Thomas-Fermi and the roster; the charged-sector restriction was derived")
print("      in the Koide sector from a failed forward test. Neither used the other.")
