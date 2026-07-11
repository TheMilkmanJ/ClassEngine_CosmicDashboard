#!/usr/bin/env python3
"""
Sakharov / Affleck-Dine twist-sign test (gate: does HEAT set the arrow?).

Question: with a CP-violating A-term V_A = 2 eps_A lam R^4 cos(4 theta + delta),
does the cooling/expansion (Hubble friction) give a UNIVERSAL-SIGN twist across
patches with different release phases theta_i -> closing the domain problem?

Field: Psi = x + i y, released AT REST at phase theta_i in a radiation background
(H = 1/(2t), a ~ t^1/2). We integrate and record the sign of the comoving dark
charge Q = a^3 * 2 (x ydot - y xdot) as a function of theta_i, for several CP
phases delta, and with Hubble friction ON vs OFF.

Honest test: if sign(Q) is the SAME for all theta_i -> universal arrow (domain
problem closed by the dynamics). If sign(Q) flips with theta_i -> the sign tracks
the random release phase (domain problem persists; only inflation-homogenization
of theta_i can save it, NOT the A-term/CP/cooling).
"""
import numpy as np
from scipy.integrate import solve_ivp

m2   = 1.0      # m^2
lam  = 0.10     # quartic
epsA = 0.30     # A-term strength (U(1)-violating)
Ri   = 3.0      # release radius |Psi|

def dVdx_dVdy(x, y, delta):
    # V = m2 (x^2+y^2) + lam (x^2+y^2)^2 + 2 eps_A lam Re[e^{i delta} (x+iy)^4]
    R2 = x*x + y*y
    # base (U(1)-symmetric) part
    dVx = 2*m2*x + 4*lam*R2*x
    dVy = 2*m2*y + 4*lam*R2*y
    # A-term: 2 eps_A lam Re[e^{i delta} Psi^4]; d/dPsi* handled via components
    Psi = x + 1j*y
    # dV_A/dx = 2 eps_A lam * Re[e^{i delta} * 4 Psi^3 * dPsi/dx], dPsi/dx = 1
    # dV_A/dy = 2 eps_A lam * Re[e^{i delta} * 4 Psi^3 * dPsi/dy], dPsi/dy = i
    c = 2*epsA*lam*4*np.exp(1j*delta)*Psi**3
    dVx += np.real(c*1.0)
    dVy += np.real(c*1j)
    return dVx, dVy

def rhs(t, s, delta, friction):
    x, y, vx, vy = s
    H = 1.0/(2.0*t) if friction else 0.0
    dVx, dVy = dVdx_dVdy(x, y, delta)
    ax = -3*H*vx - dVx
    ay = -3*H*vy - dVy
    return [vx, vy, ax, ay]

def final_charge(theta_i, delta, friction, t0=0.05, t1=60.0):
    x0, y0 = Ri*np.cos(theta_i), Ri*np.sin(theta_i)
    sol = solve_ivp(rhs, [t0, t1], [x0, y0, 0.0, 0.0],
                    args=(delta, friction), rtol=1e-8, atol=1e-10, dense_output=False)
    x, y, vx, vy = sol.y[:, -1]
    a3 = (t1/t0)**1.5 if friction else 1.0   # a ~ t^1/2 -> a^3 ~ t^1.5
    Q = a3 * 2.0*(x*vy - y*vx)
    return Q

def scan(delta, friction, n=24):
    thetas = np.linspace(0, 2*np.pi, n, endpoint=False)
    Qs = np.array([final_charge(th, delta, friction) for th in thetas])
    signs = np.sign(Qs)
    frac_pos = np.mean(signs > 0)
    return thetas, Qs, signs, frac_pos

print("="*72)
print("SAKHAROV TWIST-SIGN TEST — does the cooling arrow give a universal sign?")
print(f"  m^2={m2}, lam={lam}, eps_A={epsA}, R_i={Ri}")
print("="*72)
for delta in [0.0, np.pi/4, np.pi/2, 1.0]:
    for friction in [True, False]:
        thetas, Qs, signs, fpos = scan(delta, friction)
        tag = "cooling ON " if friction else "cooling OFF"
        # pattern string
        pat = "".join("+" if s > 0 else "-" for s in signs)
        net = np.sign(np.sum(Qs))
        print(f"delta={delta:5.2f} {tag} | frac(+)={fpos:4.2f} | "
              f"net={'+' if net>0 else '-'} | sign vs theta_i: {pat}")
    print("-"*72)
print()
print("READING: if the +/- pattern is ALL '+' (or all '-'), the twist sign is")
print("universal (domain problem closed by dynamics). If it MIXES +/-, the sign")
print("tracks the random release phase theta_i -> domain problem persists; only")
print("inflation homogenizing theta_i (one value across the sky) can fix it.")
