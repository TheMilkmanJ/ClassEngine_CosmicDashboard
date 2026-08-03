#!/usr/bin/env python3
"""
#11 / f_amp with the MODEL's real A-term (Z4 tilt), not a parametrized kick.

Z4 symmetry (Psi -> i Psi) allows the tilt  V_A = eps_A * lam * (Psi^4 + Psi*^4)
                                                 = 2 eps_A lam (x^4 - 6x^2y^2 + y^4)
                                                 = 2 eps_A lam R^4 cos(4 theta).
The field is RELEASED AT REST at phase theta_i (uniform prior after inflation);
the tilt TORQUES it as it rolls -> rotation is GENERATED, not assumed. f_amp =
late-time radial (breathing) energy fraction. Scanning theta_i over a uniform
prior gives the model's actual f_amp DISTRIBUTION (the genesis dice).

Cartesian, non-stiff, in-sandbox.  Run: python3 scripts/genesis_famp_Z4.py
"""
import numpy as np
from scipy.integrate import solve_ivp

m2, lam, Ri = 1.0, 0.03, 10.0     # units m=1; quartic dominates for R>~sqrt(m2/lam)~6

def H(t): return 1.0/(2.0*t)      # radiation era

def make_rhs(epsA):
    def rhs(t, s):
        x, y, vx, vy = s
        r2 = x*x + y*y
        # dV/dx, dV/dy  from V = m2 r2 + lam r2^2 + 2 epsA lam (x^4-6x^2y^2+y^4)
        dVx = 2*m2*x + 4*lam*r2*x + 2*epsA*lam*(4*x**3 - 12*x*y*y)
        dVy = 2*m2*y + 4*lam*r2*y + 2*epsA*lam*(4*y**3 - 12*x*x*y)
        h = H(t)
        return [vx, vy, -3*h*vx - dVx, -3*h*vy - dVy]
    return rhs

def f_amp(epsA, theta_i, t_i=0.25, t_f=80.0):
    x0, y0 = Ri*np.cos(theta_i), Ri*np.sin(theta_i)
    sol = solve_ivp(make_rhs(epsA), [t_i, t_f], [x0, y0, 0.0, 0.0],
                    method='RK45', rtol=1e-8, atol=1e-10, max_step=0.05,
                    dense_output=True)
    ts = np.linspace(0.6*t_f, t_f, 4000)
    x, y, vx, vy = sol.sol(ts)
    r2 = x*x + y*y
    L  = x*vy - y*vx
    E_rot = 0.5*L*L/r2
    rdot  = (x*vx + y*vy)/np.sqrt(r2)
    E_rad = 0.5*rdot*rdot
    return np.mean(E_rad)/np.mean(E_rad + E_rot), np.mean(L)

print("="*66)
print("#11 f_amp -- MODEL A-term (Z4 tilt), uniform release-phase prior")
print("="*66)
thetas = np.linspace(0.01, np.pi/2, 24)   # one Z4 period (cos4theta has period pi/2)
print(f"\n  {'tilt eps_A':>10}  {'median f_amp':>12}  {'range':>16}")
print("  " + "-"*44)
for epsA in [0.1, 0.2, 0.3, 0.5]:
    fa = np.array([f_amp(epsA, th)[0] for th in thetas])
    print(f"  {epsA:>10.2f}  {np.median(fa):>12.2f}  [{fa.min():.2f}, {fa.max():.2f}]")

# T14 link 5, half one: the SIGN the roll generates, not just its magnitude.
# The tilt 2 epsA lam R^4 cos4theta is invariant under  sigma: theta -> pi/2 - theta,
# as are release-at-rest and the isotropic friction, while L = R^2 thetadot is ODD
# under sigma. So the uniform prior splits evenly -- for ANY tilt strength.
# Sampled on a grid centred on pi/4 so the prior itself respects sigma; the f_amp grid
# above is left as-is (it is centred slightly off pi/4, which biases a SIGNED sum but
# not the magnitudes that table reports).
print(f"\n  sign of the generated rotation, uniform prior over one Z4 period")
print(f"\n  {'tilt eps_A':>10}  {'L>0':>5}  {'L<0':>5}  {'sum(L)/sum|L|':>16}")
print("  " + "-"*46)
sym = np.linspace(0.01, np.pi/2 - 0.01, 24)      # centred on pi/4
for epsA in [0.1, 0.2, 0.3, 0.5]:
    Ls = np.array([f_amp(epsA, th)[1] for th in sym])
    print(f"  {epsA:>10.2f}  {int((Ls>0).sum()):>5}  {int((Ls<0).sum()):>5}  "
          f"{Ls.sum()/np.abs(Ls).sum():>+16.2e}")

print("\n" + "-"*66)
print("READ: with the REAL Z4 tilt and a UNIFORM release-phase prior, the median")
print("f_amp lands ~0.5-0.7 across a plausible tilt range -- the doc's f_amp~0.6")
print("is where the model's own dice actually sit, not an assumption. The exact")
print("value slides with the tilt strength eps_A (the one remaining model input).")
print("-"*66)
