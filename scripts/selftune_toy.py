#!/usr/bin/env python3
"""
TOY ghost-condensate + neutrino cosmological ODE (transparent, simplified).
Q: does c_s^2 self-tune to ~ rho_nu/rho_Lambda (the chi~1/c_s^2 amplification),
and is it an ATTRACTOR (IC-independent)?  Toy -> read STRUCTURE not exact number.

Ghost condensate: P(X) = -rho_L + 1/2 (X-X0)^2, X=1/2 v^2, condensate at v=1 (X0=1/2).
c_s^2 = (X-X0)/(2X) = (v^2-1)/(2 v^2).  Neutrino force ~ -beta rho_nu(a), rho_nu~a^-3.
Field EOM (k-essence): dv/dN = [-3H(X-X0)v - beta rho_nu] / [H(3/2 v^2 - X0)].
Units: M_Pl=1, rho_L=1, H=H_L=1/sqrt(3) (de Sitter), beta=1.
"""
import numpy as np
from scipy.integrate import solve_ivp

X0=0.5; rhoL=1.0; H=1/np.sqrt(3); beta=1.0
def cs2(v): return (v*v-1)/(2*v*v)
def rhs(N,y,eps):
    v=y[0]; X=0.5*v*v; rho_nu=eps*np.exp(-3*N)
    num=-3*H*(X-X0)*v - beta*rho_nu
    den=H*(1.5*v*v - X0)
    return [num/den]

print("="*64); print("TOY self-tuning check: c_s^2 vs rho_nu/rho_L, and attractor"); print("="*64)
print("\n(a) SCALING -- fixed-point c_s^2(now, N=0) vs eps_nu=rho_nu/rho_L:")
print(f"  {'eps_nu':>8} {'c_s^2(N=0)':>12} {'c_s^2/eps_nu':>12} {'chi=1/cs2':>10}")
for eps in [0.001,0.002,0.005,0.01]:
    sol=solve_ivp(rhs,[-3,2],[1.05],args=(eps,),rtol=1e-9,atol=1e-11,dense_output=True,max_step=0.02)
    v0=sol.sol(0.0)[0]; c=cs2(v0)
    print(f"  {eps:>8.3f} {c:>12.5f} {c/eps:>12.3f} {1/c:>10.1f}")

print("\n(b) ATTRACTOR -- start from different v, do they converge by N=0? (eps=0.002)")
print(f"  {'v_init(N=-3)':>13} {'v(N=0)':>10} {'c_s^2(N=0)':>12}")
for vi in [1.02,1.10,1.30,0.95]:
    sol=solve_ivp(rhs,[-3,2],[vi],args=(0.002,),rtol=1e-9,atol=1e-11,dense_output=True,max_step=0.02)
    v0=sol.sol(0.0)[0]
    print(f"  {vi:>13.2f} {v0:>10.5f} {cs2(v0):>12.5f}")
print("\n(needed for chi~500: c_s^2 ~ 0.002. Watch if c_s^2/eps_nu ~ const [self-tune] and")
print(" if different ICs converge [attractor]. TOY -- structure only, not the real number.)")
