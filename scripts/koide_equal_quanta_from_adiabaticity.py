"""Can the equal-quanta premise (P4) be derived, or must it be postulated?

koide_democratic_graph_null.py derived Q = 2/3 from four premises and named (P4) -- the modes carry
EQUAL QUANTA rather than equal energy -- as the load-bearing one. This asks whether (P4) is a
postulate about occupation numbers or a consequence of how the ring is assembled.

THE OBSERVATION. "Equal quanta" is equal ACTION per mode: J_q = E_q/w_q = (n_q + 1/2) hbar. Action
is the adiabatic invariant of a harmonic degree of freedom. So equal quanta at the end is equal
quanta at the beginning, PROVIDED the spectrum splits slowly -- and at the beginning the modes may
be degenerate, in which case equal occupation is automatic for any common preparation.

THE ASSEMBLY ORDER THAT DOES IT. A face is an excitation OF the condensate, so its bond to the
medium is primary; the face-face bonds are what the medium then mediates. Turn them on in that
order:

    stage 1   medium bond only     eps_q = a for every q        -- ALL THREE MODES DEGENERATE
    stage 2   face-face bonds ramp eps_q = a + b(t) lambda_q    -- the spectrum splits

At stage 1 the three modes have identical frequencies, so any equilibrium, any thermal state, any
common preparation gives them the same occupation number. Through stage 2 each mode conserves its
own action if the ramp is adiabatic. Equal quanta at the end follows.

This integrates the ramp explicitly and checks the invariant rather than asserting it, including
the failure mode: a fast ramp must BREAK it, or the check proves nothing.

Run: python3 scripts/koide_equal_quanta_from_adiabaticity.py
"""
import math

LAM = (0.0, 3.0, 3.0)          # ring Laplacian spectrum at N = 3: neutral, charged, charged
A_ON = 1.0                     # the medium bond, on from the start (stage 1)
B_END = 1.0                    # the face-face bond's final value -> a = b


def eps(q, b):
    return A_ON + b * LAM[q]


def omega(q, b):
    return math.sqrt(eps(q, b))


def ramp(t, T):
    """Smooth 0 -> B_END over [0, T], with vanishing derivatives at both ends."""
    if t <= 0.0:
        return 0.0
    if t >= T:
        return B_END
    s = t / T
    return B_END * s * s * s * (10 - 15 * s + 6 * s * s)


def integrate(q, T, J0=1.0, steps_per_period=400):
    """Evolve mode q through the ramp; return (J_initial, J_final, <x^2>_final)."""
    w0 = omega(q, 0.0)
    # start at a turning point with action J0:  E = J0 * w0,  x = sqrt(2E)/w0,  v = 0
    E0 = J0 * w0
    x, v = math.sqrt(2 * E0) / w0, 0.0
    wmax = omega(q, B_END)
    dt = (2 * math.pi / wmax) / steps_per_period
    n = int(math.ceil((T + 40 * 2 * math.pi / wmax) / dt))
    # velocity-Verlet with time-dependent omega
    w2 = eps(q, ramp(0.0, T))
    a_acc = -w2 * x
    Esum, xsum, cnt = 0.0, 0.0, 0
    tail = n - int((30 * 2 * math.pi / wmax) / dt)
    for k in range(n):
        t = k * dt
        x += v * dt + 0.5 * a_acc * dt * dt
        w2n = eps(q, ramp(t + dt, T))
        a_new = -w2n * x
        v += 0.5 * (a_acc + a_new) * dt
        a_acc = a_new
        if k >= tail:                      # average over the last ~30 periods, after the ramp
            E = 0.5 * v * v + 0.5 * w2n * x * x
            Esum += E; xsum += x * x; cnt += 1
    wf = omega(q, B_END)
    return J0, (Esum / cnt) / wf, xsum / cnt


print("=" * 78)
print("(1) STAGE 1 — THE MODES START DEGENERATE")
print("=" * 78)
print(f"  With only the medium bond on (b = 0), eps_q = a for every q:")
print(f"    {'mode':>10} {'lambda_q':>10} {'eps_q':>9} {'w_q':>9}")
print("  " + "-" * 42)
for q, name in ((0, "neutral"), (1, "charged"), (2, "charged")):
    print(f"  {name:>10} {LAM[q]:10.1f} {eps(q, 0.0):9.5f} {omega(q, 0.0):9.5f}")
print()
print("  Exactly degenerate — the medium bond is blind to which face it holds. So a common")
print("  occupation number across the three modes is not an assumption at this stage; it is")
print("  what any equilibrium or common preparation gives when the frequencies coincide.")

print()
print("=" * 78)
print("(2) STAGE 2 — RAMP THE FACE-FACE BONDS AND WATCH THE ACTION")
print("=" * 78)
print("  Each mode is integrated through the ramp with velocity-Verlet, starting from a common")
print("  action J = 1. If the action is the invariant, every mode ends at J = 1 whatever its")
print("  frequency did.")
print()
w_slow = omega(1, B_END)
T_slow = 400.0 * (2 * math.pi / w_slow)          # ramp over ~400 charged-mode periods
print(f"  ramp duration = {T_slow:.1f} = 400 charged-mode periods (adiabatic)")
print()
print(f"  {'mode':>10} {'w_initial':>11} {'w_final':>10} {'J_initial':>11} {'J_final':>11} {'drift':>10}")
print("  " + "-" * 68)
Jf = {}
for q, name in ((0, "neutral"), (1, "charged")):
    J0, J1, x2 = integrate(q, T_slow)
    Jf[q] = (J1, x2)
    print(f"  {name:>10} {omega(q,0.0):11.5f} {omega(q,B_END):10.5f} {J0:11.6f} {J1:11.6f}"
          f" {abs(J1/J0-1)*100:9.4f}%")
print()
print("  The charged mode's frequency doubles and its action does not move. That is adiabatic")
print("  invariance, computed rather than quoted.")

print()
print("=" * 78)
print("(3) THE CONTROL — A FAST RAMP MUST BREAK IT")
print("=" * 78)
print("  A check that cannot fail is not a check. If the action were conserved for ANY ramp the")
print("  result would be trivial, so the sudden limit has to break it.")
print()
print(f"  {'ramp (charged-mode periods)':>30} {'J_final (charged)':>19} {'drift':>10}")
print("  " + "-" * 62)
for periods in (0.02, 0.2, 2.0, 20.0, 200.0):
    T = periods * (2 * math.pi / w_slow)
    _, J1, _ = integrate(1, T)
    print(f"  {periods:>30.2f} {J1:19.6f} {abs(J1-1)*100:9.3f}%")
print()
print("  It breaks in the sudden limit and converges in the slow one, monotonically. So the")
print("  invariance is doing real work here, and the premise it replaces is ADIABATICITY --")
print("  a statement about the assembly rate, not about occupation numbers.")

print()
print("=" * 78)
print("(4) WHAT THE RAMP DELIVERS AT THE END")
print("=" * 78)
x2_0, x2_1 = Jf[0][1], Jf[1][1]
print(f"    <x^2> neutral (from the integration) = {x2_0:.8f}")
print(f"    <x^2> charged (from the integration) = {x2_1:.8f}")
print(f"    ratio                                 = {x2_1/x2_0:.8f}   (expect w_0/w_1 = 1/2)")
print()
R2_over_f02 = 2.0 * (x2_1 / x2_0)          # two charged modes
Q = (1.0 + R2_over_f02) / 3.0
print(f"    R^2/f_0^2 = 2 x ratio = {R2_over_f02:.8f}   (the null needs 1)")
print(f"    Q = (1 + R^2/f_0^2)/3 = {Q:.8f}   (2/3 = {2/3:.8f})")
print(f"    miss = {abs(Q/(2/3)-1)*1e6:.1f} ppm  (integration error, not physics)")
print()
print("  The null comes out of the integrated dynamics, not out of the premise it was used to")
print("  justify. The residual is claimed to be numerical, so it has to be shown to converge:")
print()
print(f"  {'steps/period':>14} {'Q':>14} {'ppm from 2/3':>14} {'ratio to previous':>18}")
print("  " + "-" * 64)
prev = None
for spp in (100, 200, 400, 800):
    _, _, a0 = integrate(0, T_slow, steps_per_period=spp)
    _, _, a1 = integrate(1, T_slow, steps_per_period=spp)
    Qs = (1.0 + 2.0 * a1 / a0) / 3.0
    ppm = abs(Qs / (2 / 3) - 1) * 1e6
    rel = f"{prev/ppm:18.2f}" if prev else f"{'--':>18}"
    print(f"  {spp:>14} {Qs:14.9f} {ppm:14.2f} {rel}")
    prev = ppm
print()
print("  The error falls with the timestep, so it is the integrator and not the physics. The")
print("  exact statement remains the algebraic one: <x^2> ~ J/w with J common gives R = f_0.")

print()
print("=" * 78)
print("(5) WHAT (P4) HAS BECOME")
print("=" * 78)
print("  BEFORE: 'the modes carry equal quanta' — a postulate about occupation numbers, with")
print("  nothing behind it, carrying the whole derivation of Q = 2/3.")
print()
print("  AFTER: two physical statements, both attackable:")
print("    (P4a) ASSEMBLY ORDER — the medium bond precedes the face-face bonds, because a face")
print("          is an excitation of the condensate. At that stage the three modes are exactly")
print("          degenerate, so equal occupation is automatic rather than assumed.")
print("    (P4b) ADIABATICITY — the face-face bonds turn on slowly compared with the mode")
print("          frequencies, so each mode conserves its action through the splitting.")
print()
print("  This is a real reduction and not a rename: (P4a) is a claim about what the faces ARE,")
print("  and (P4b) is a claim about a rate, and both can be checked against the corpus's own")
print("  freeze dynamics. Neither is a statement about quantum numbers.")
print()
print("  WHAT IS STILL OWED. The corpus must supply the ramp rate at freeze and confirm it is")
print("  slow against w ~ 39 keV. That is the same fork the delivery-law discriminator opened —")
print("  the freeze's timescale — now demanded from the other side. One number closes both.")
