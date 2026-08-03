"""What does the null become under the COLD law -- both sectors in definite quantum states?

koide_delivery_law_discriminator.py showed the thermal law cannot carry Q = 2/3 at the 6e-6 the
corpus quotes: at the corpus's own w_1 = (2/9)T_c the quantum correction distorts Q by 1025 ppm.
It also showed the occupancy lock is a cold law and therefore the right exactness CLASS. This
works the cold law out properly instead of trusting the lock's three recorded lines, because those
lines write one frequency where the null says there are two, and their N_0 = 1 is
convention-dependent.

THE ONE RELATION EVERYTHING RESTS ON. For a harmonic degree of freedom of mass M and frequency w
in a state of n quanta -- Fock, or coherent with n quanta, whose TIME-AVERAGED second moment is
the same --

    <x^2> = (2n + 1) hbar / (2 M w).

That is the whole input. The singlet is one degree of freedom, the doublet is two, and
R_c^2 = |f_1|^2 + |f_2|^2 sums both of them. So:

    M_c^2 = (2 n_0 + 1) hbar / (2 M w_0)
    R_c^2 = 2 * (2 n_1 + 1) hbar / (2 M w_1)      [two degrees of freedom]

Everything below is that pair, divided.

Run: python3 scripts/koide_quantum_law_null.py
"""
import math
from fractions import Fraction

HBAR = M = 1.0                       # cancel from every ratio; set to 1 and checked below


def moment(n, w, dof=1):
    """Sum of <x^2> over `dof` degenerate degrees of freedom, each holding n quanta."""
    return dof * (2 * n + 1) * HBAR / (2 * M * w)


print("=" * 78)
print("(1) THE LOCK'S RECORDED ARGUMENT, WITH ITS CONVENTION MADE EXPLICIT")
print("=" * 78)
print("  As recorded:  N_0 = M w f_0^2 / hbar = 1,  and the charged pair in its ground state.")
print("  Read against <x^2> = (2n+1) hbar / (2 M w), the neutral line says")
print()
print("      M w <x^2> / hbar = (2 n_0 + 1)/2 = n_0 + 1/2 = 1   ->   n_0 = 1/2")
print()
print("  which is not a state. The lock's 'integer that cannot drift' is an integer only under")
print("  the PEAK-amplitude reading (x = A cos wt, <x^2> = A^2/2), where M w A^2 / hbar = 2n+1")
print("  and N_0 = 1 means n_0 = 0 -- the ground state. That is the reading the lock's second")
print("  line already uses for the charged pair, so it is the consistent one, and it is what is")
print("  used below. Recorded because the two readings differ by exactly the factor 2 that the")
print("  null is sensitive to, and the corpus does not say which is meant.")

print()
print("=" * 78)
print("(2) THE NULL UNDER THE COLD LAW — WHAT IT ACTUALLY REQUIRES")
print("=" * 78)
print("  R_c = M_c  <=>  2 (2n_1 + 1) / w_1 = (2n_0 + 1) / w_0")
print("             <=>  w_1 / w_0 = 2 (2n_1 + 1) / (2n_0 + 1)")
print("  and since w ~ sqrt(eps), the stiffness ratio the null demands is")
print()
print("      eps_1/eps_0 = 4 (2n_1 + 1)^2 / (2n_0 + 1)^2")
print()
print(f"  {'n_0':>4} {'n_1':>4} {'w_1/w_0':>10} {'eps_1/eps_0':>13} {'a/b':>10}  {'reading'}")
print("  " + "-" * 74)
rows = []
for n0 in range(4):
    for n1 in range(3):
        wr = 2.0 * (2 * n1 + 1) / (2 * n0 + 1)
        er = wr * wr
        # eps_0 = a, eps_1 = a + 3b  =>  a/b = 3/(er - 1)
        ab = 3.0 / (er - 1.0) if abs(er - 1.0) > 1e-12 else float("inf")
        # verify by construction rather than by the algebra above
        w0, w1 = 1.0, wr
        ok = abs(moment(n1, w1, dof=2) / moment(n0, w0, dof=1) - 1.0) < 1e-12
        note = ""
        if n0 == 0 and n1 == 0:
            note = "both sectors in their GROUND STATE"
        elif abs(ab - 3.0) < 1e-9:
            note = "the recorded a = 3b"
        rows.append((n0, n1, wr, er, ab, ok, note))
        print(f"  {n0:>4} {n1:>4} {wr:10.5f} {er:13.5f} {ab:10.5f}  {note}"
              f"{'' if ok else '   [CONSTRUCTION CHECK FAILED]'}")

print()
print("  Every row is verified by building the two moments and dividing, not by the algebra.")

print()
print("=" * 78)
print("(2b) THE GROUND STATE IS NOT NEEDED — ONLY EQUAL OCCUPANCY")
print("=" * 78)
print("  Read the table down its diagonal: n_0 = n_1 = 0, 1, 2 all return eps_1/eps_0 = 4 and")
print("  a = b. That is not three coincidences. Setting n_0 = n_1 = n,")
print()
print("      w_1/w_0 = 2 (2n + 1)/(2n + 1) = 2      for EVERY n,")
print()
print("  because the occupancy factor (2n+1) is common to both sectors and cancels. So the")
print("  cold result does not rest on the sectors being cold at all — only on their holding")
print("  the SAME number of quanta.")
print()
print(f"  {'n':>4} {'w_1/w_0':>10} {'eps_1/eps_0':>13} {'a/b':>8} {'R_c/M_c':>12}")
print("  " + "-" * 52)
for n in (0, 1, 2, 5, 17, 1000):
    wr = 2.0 * (2 * n + 1) / (2 * n + 1)
    rc = math.sqrt(moment(n, wr, dof=2) / moment(n, 1.0, dof=1))
    print(f"  {n:>4} {wr:10.6f} {wr*wr:13.6f} {3.0/(wr*wr-1.0):8.4f} {rc:12.10f}")
print()
print("  THE WHOLE FORK COLLAPSES TO ONE PHYSICAL QUESTION. Both laws say <x^2> = (2n+1)/(2Mw)")
print("  hbar; they differ only in what is held equal across the two sectors:")
print()
print(f"    {'law':<34} {'what is equal':<22} {'<x^2> scaling':<16} {'null gives'}")
print("    " + "-" * 74)
print(f"    {'equal quanta per mode':<34} {'(2n+1)':<22} {'~ 1/w':<16} {'eps_1/eps_0 = 4  -> a = b'}")
print(f"    {'equal energy per mode (thermal)':<34} {'(2n+1) w':<22} {'~ 1/w^2':<16} {'eps_1/eps_0 = 2  -> a = 3b'}")
print()
# verify the thermal branch by the same construction, to be sure the framing is right
_w0 = 1.0
_w1 = math.sqrt(2.0)                       # eps ratio 2
_E = 1.0                                   # equal energy per mode
_x2 = lambda w, dof: dof * _E / (M * w * w)   # <x^2> at fixed energy per dof
print(f"    thermal check by construction: R_c^2/M_c^2 ="
      f" {_x2(_w1, 2)/_x2(_w0, 1):.12f} at eps_1/eps_0 = 2")
print(f"    cold    check by construction: R_c^2/M_c^2 ="
      f" {moment(0, 2.0, dof=2)/moment(0, 1.0, dof=1):.12f} at eps_1/eps_0 = 4")
print()
print("  Equal energy is the equipartition theorem and needs a bath. Equal quanta is a")
print("  democratic occupancy statement and does not — and the corpus's whole idiom for this")
print("  ring is democratic. Neither is derived here; what is derived is that the corpus's two")
print("  incompatible stiffness targets are these two laws and nothing else.")

print()
print("=" * 78)
print("(3) THE GROUND-STATE ROW IS THE ONE THE LOCK MEANS")
print("=" * 78)
n0 = n1 = 0
w0 = 1.0
w1 = 2.0 * (2 * n1 + 1) / (2 * n0 + 1)
Mc2 = moment(n0, w0, dof=1)
Rc2 = moment(n1, w1, dof=2)
print("  Both sectors cold, in their ground states — the cleanest cold statement there is,")
print("  and the one the lock's second line already assumes for the charged pair.")
print()
print(f"    M_c^2 = hbar/(2 M w_0)          = {Mc2:.10f}   (hbar = M = 1, w_0 = 1)")
print(f"    R_c^2 = 2 x hbar/(2 M w_1)      = {Rc2:.10f}")
print(f"    R_c/M_c                          = {math.sqrt(Rc2/Mc2):.10f}")
print()
print(f"    requires  w_1/w_0 = {w1:.6f} exactly, i.e. eps_1/eps_0 = {w1*w1:.6f}")
er = w1 * w1
ab = 3.0 / (er - 1.0)
print()
print("  Pushed through the ring's own Fourier stiffnesses eps_0 = a, eps_1 = a + 3b:")
print(f"      a + 3b = {er:.0f} a    ->    3b = {er-1:.0f} a    ->    a = {Fraction(ab).limit_denominator(100)} b")
print()
print("  " + "=" * 70)
print(f"      THE COLD NULL IS  a = b,  NOT  a = 3b.")
print("  " + "=" * 70)
print()
print("  On-site coupling equal to bond coupling — ONE constant appearing in both places, which")
print("  is what a single microscopic coupling would give. Against a = 3b, which requires the")
print("  on-site term to be tuned to three times the bond term with nothing setting the 3.")

print()
print("=" * 78)
print("(4) CROSS-CHECKS")
print("=" * 78)
# (a) hbar and M really do cancel
for _h, _m in ((1.0, 1.0), (7.3, 0.11), (1e-34, 9.1e-31)):
    HBAR, M = _h, _m
    r = moment(0, 2.0, dof=2) / moment(0, 1.0, dof=1)
    print(f"    hbar = {_h:<9.3g} M = {_m:<9.3g}  ->  R_c^2/M_c^2 = {r:.12f}")
HBAR = M = 1.0
print("    (so the result carries no hidden scale, which was the lock's whole claim)")
print()
# (b) the Q the cold null produces, by construction
rho2 = 0.5 * (Rc2 / Mc2)             # rho^2 = |f_1|^2/f_0^2 = (R_c^2/2)/M_c^2
Q = 1 / 3 + (2 / 3) * rho2
print(f"    rho^2 = (R_c^2/2)/M_c^2 = {rho2:.12f}")
print(f"    Q     = 1/3 + (2/3) rho^2 = {Q:.12f}   (2/3 = {2/3:.12f})")
print(f"    A     = sqrt(6Q - 2)      = {math.sqrt(6*Q-2):.12f}   (sqrt2 = {math.sqrt(2):.12f})")
print(f"    tau   = -ln(A/2)          = {-math.log(math.sqrt(6*Q-2)/2):.12f}"
      f"   (ln2/2 = {math.log(2)/2:.12f})")
print("    Exact, with no limit taken and no temperature anywhere. This is the exactness class")
print("    the 6e-6 agreement needs: a ground state does not drift.")
print()
# (c) the thermal law's target, for contrast, and the factor between them
print(f"    cold law needs   eps_1/eps_0 = {er:.4f}   ->  a = b")
print(f"    thermal law needs eps_1/eps_0 = 2.0000   ->  a = 3b")
print(f"    ratio between the two targets = {er/2:.4f}")
print("    The two laws differ by exactly 2 in the stiffness ratio, which is the doublet's")
print("    degree-of-freedom count -- the thermal law gives the doublet twice the energy for")
print("    having twice the modes, the cold law gives it twice the zero-point for the same")
print("    reason. That is where the whole disagreement lives.")

print()
print("=" * 78)
print("(5) WHAT THIS DOES AND DOES NOT SETTLE")
print("=" * 78)
print("  SETTLED: under a cold law with both sectors in their ground states, R_c = M_c is exact,")
print("  scale-free, and equivalent to a = b. No tuning, no limit, no temperature. The frequency")
print("  degeneracy the lock's recorded argument silently assumed is NOT needed -- what is needed")
print("  is the opposite, w_1 = 2 w_0, and that is now a stated, checkable requirement rather")
print("  than an accident.")
print()
print("  NOT SETTLED, and it is the next object: nothing here says WHY a = b. It is a far more")
print("  natural target than a = 3b -- one coupling rather than a tuned 3:1 -- but it is still")
print("  a relation to be sourced from the kernel/hop dynamics, and that is board task #1's")
print("  object, now restated.")
print()
print("  ALSO OWED: the cold law needs the sectors cold at freeze. The corpus's w_1 = (2/9)T_c")
print("  puts hbar w_1 / kT_c = 0.22, which is the classical end, not the cold one. Either that")
print("  frequency is not the one the null cares about, or the freeze is not cold, and the two")
print("  cannot both stand. Same fork the discriminator opened, now with a second thing riding")
print("  on it.")
