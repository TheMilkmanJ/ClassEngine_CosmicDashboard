"""Does the corpus's PINNED SUDDEN pour contradict the adiabatic split (P4b)? Order decides it.

THE APPARENT CONFLICT. koide_equal_quanta_from_adiabaticity.py reduced the equal-quanta premise to
(P4a) assembly order + (P4b) adiabaticity. But T6's pass-4 verdict pins the genesis injection the
other way:

    "(pin 2) 'THE SNAP / THE POUR (genesis, one instant)' => the sudden (1/w^2) transfer weight --
     impulsive by the books ... the weight is pinned sudden"

Sudden and adiabatic are opposites, so on the face of it the corpus's own pin kills (P4b).

THE RESOLUTION, IF THERE IS ONE. The two statements are about DIFFERENT processes:

    the POUR   -- energy injected into the modes, at fixed Hamiltonian.   Pinned SUDDEN.
    the SPLIT  -- the Hamiltonian's stiffnesses separating.               (P4b) needs SLOW.

They are logically independent, and the question is which comes first. The key fact is that at
stage 1 the three modes are DEGENERATE, and at degeneracy every transfer weight is the same number
for every mode -- 1/w^2, flat, thermal, anything -- because there is only one w. A sudden pour into
degenerate modes therefore deposits EQUAL energy per mode, and equal energy at equal frequency IS
equal quanta.

So the order pour-then-split makes the two pins agree. The order split-then-pour does not. This
computes both and shows they are not close.

Run: python3 scripts/koide_pour_before_split.py
"""
import math

LAM = (0.0, 3.0, 3.0)
A, B = 1.0, 1.0                       # a = b, the democratic graph's couplings
EPS = tuple(A + B * l for l in LAM)   # (1, 4, 4)
W = tuple(math.sqrt(e) for e in EPS)  # (1, 2, 2)

print("=" * 78)
print("(1) AT DEGENERACY EVERY DELIVERY LAW AGREES — THAT IS THE WHOLE POINT")
print("=" * 78)
print("  Stage 1 has eps_q = a for every q, so w_q = w for every q. Any transfer weight is a")
print("  function of w alone, so it returns the SAME number for all three modes:")
print()
WEIGHTS = (
    ("sudden, 1/w^2 per mode   (the corpus's pin)", lambda w: 1.0 / w**2),
    ("flat per log", lambda w: 1.0),
    ("thermal / equipartition", lambda w: 1.0),
    ("resonant, 1/w", lambda w: 1.0 / w),
    ("anything else f(w)", lambda w: math.exp(-w) + w**3),
)
w_deg = 1.0
print(f"  {'transfer weight':<44} {'E_neutral':>11} {'E_charged':>11} {'equal?':>8}")
print("  " + "-" * 78)
for name, f in WEIGHTS:
    e0, e1 = f(w_deg), f(w_deg)
    print(f"  {name:<44} {e0:11.6f} {e1:11.6f} {'YES' if abs(e0-e1) < 1e-15 else 'no':>8}")
print()
print("  Trivially true and load-bearing: the delivery-law ambiguity that has cost this arc")
print("  three cycles simply does not exist while the modes are degenerate. Equal energy at a")
print("  common frequency is equal quanta, so the pour hands over a common occupation number")
print("  no matter how impulsive it is.")

print()
print("=" * 78)
print("(2) ORDER A — POUR FIRST, THEN SPLIT ADIABATICALLY")
print("=" * 78)
print("  The pour lands on degenerate modes (common n), then the face-face bonds ramp on and")
print("  each mode conserves its action, so n is carried through unchanged. At the end")
print("  <x^2> = (2n+1) hbar / (2 M w) with a COMMON n:")
print()
x2_A = tuple((1.0) / w for w in W)             # common (2n+1), so <x^2> ~ 1/w
R2_A = x2_A[1] + x2_A[2]
QA = (1.0 + R2_A / x2_A[0]) / 3.0
print(f"    <x^2>_neutral ~ 1/w_0 = {x2_A[0]:.8f}")
print(f"    <x^2>_charged ~ 1/w_1 = {x2_A[1]:.8f}")
print(f"    R^2/f_0^2 = {R2_A/x2_A[0]:.8f}      (the null needs 1)")
print(f"    Q = {QA:.10f}      (2/3 = {2/3:.10f})")
print(f"    miss = {abs(QA/(2/3)-1)*1e6:.3f} ppm")

print()
print("=" * 78)
print("(3) ORDER B — SPLIT FIRST, THEN THE SUDDEN POUR")
print("=" * 78)
print("  Now the pour arrives on an already-split spectrum and its w-dependence bites. With the")
print("  pinned sudden weight E_q ~ 1/w_q^2, and <x^2> = E/(M w^2), the amplitude goes as 1/w^4:")
print()
x2_B = tuple(1.0 / w**4 for w in W)
R2_B = x2_B[1] + x2_B[2]
QB = (1.0 + R2_B / x2_B[0]) / 3.0
print(f"    <x^2>_neutral ~ 1/w_0^4 = {x2_B[0]:.8f}")
print(f"    <x^2>_charged ~ 1/w_1^4 = {x2_B[1]:.8f}")
print(f"    R^2/f_0^2 = {R2_B/x2_B[0]:.8f}      (the null needs 1)")
print(f"    Q = {QB:.10f}      (2/3 = {2/3:.10f})")
print(f"    miss = {abs(QB/(2/3)-1)*100:.1f}%")
print()
print("  and the stiffness ratio that WOULD make order B work is not 4:")
print("    R^2/f_0^2 = 2 (w_0/w_1)^4 = 2 (eps_0/eps_1)^2 = 1  ->  eps_1/eps_0 = sqrt2")
print(f"    check: 2*(1/math.sqrt(2))**2 = {2*(1/math.sqrt(2))**2:.10f}")
print("  which is neither the graph's 4 nor the thermal 2 nor the ring-on-ring 1/2.")

print()
print("=" * 78)
print("(4) THE TWO ORDERS ARE NOT CLOSE, SO THIS IS A REAL PREDICTION")
print("=" * 78)
print(f"  {'order':<34} {'Q':>14} {'from 2/3':>14}")
print("  " + "-" * 66)
print(f"  {'A: pour while degenerate, then split':<34} {QA:14.10f} {abs(QA/(2/3)-1)*1e6:11.3f} ppm")
print(f"  {'B: split first, then sudden pour':<34} {QB:14.10f} {abs(QB/(2/3)-1)*100:12.1f} %")
print()
print(f"  Order B misses by {abs(QB/(2/3)-1)*100:.0f}% -- it is not a near-miss to be fixed by a")
print("  correction. The mechanism therefore does not merely tolerate an ordering, it REQUIRES")
print("  one, and says which.")

print()
print("=" * 78)
print("(5) IS ORDER A THE ONE THE CORPUS ALREADY PINS?")
print("=" * 78)
print("  It is what the corpus's own words describe, though the corpus has not drawn the")
print("  consequence. Pin 2 calls the pour 'genesis, one instant' -- an injection event. The")
print("  face-face couplings are what the medium MEDIATES between faces, so they cannot precede")
print("  the faces' existence as excitations of that medium (P4a). Injection into the newborn,")
print("  still-degenerate ring, followed by the ring's own structure developing, is order A.")
print()
print("  WHAT WOULD REFUTE IT. If the corpus's freeze dynamics place the face-face coupling as")
print("  present from the first instant -- i.e. the ring is born already split -- then order B")
print("  applies, the mechanism predicts Q = 0.375, and it is dead. That is a clean kill")
print("  condition on a structural question, not on a measurement.")
print()
print("  WHAT IS NO LONGER OWED. The 'delivery law at freeze' fork does not need settling in")
print("  the form it was posed. It only mattered because the sectors were assumed split when")
print("  the energy arrived. Under order A every law gives the same answer, so the question")
print("  collapses from 'which weight' to 'which order' -- and the second is answerable from")
print("  structure rather than from a rate nobody has measured.")
print()
print("  STILL OWED, and smaller than before: (P4b)'s adiabaticity is now needed only for the")
print("  SPLIT, not for the pour. The pour may be as impulsive as the corpus pins it.")
