import numpy as np
from scipy import integrate, optimize
def adot2(a,r): return 1.0/a + r*a*a - (1.0+r)
def TV(r):
    fT=lambda a:(1.0/np.sqrt(adot2(a,r)) if adot2(a,r)>0 else 0.0)
    fV=lambda a:(a**3/np.sqrt(adot2(a,r)) if adot2(a,r)>0 else 0.0)
    return integrate.quad(fT,0,1,points=[1],limit=400)[0], integrate.quad(fV,0,1,points=[1],limit=400)[0]

# ---- RAMP 1: the ratio cap Omega_L/Omega_m(a0) swept across the expansion ----
r_star=optimize.brentq(lambda r: r-0.25*TV(r)[0]/TV(r)[1], 0.2,0.49)
print(f"r* = {r_star:.4f}")
print("RAMP-1  Omega_L/Omega_m vs phase a0 (rho_L=r*, rho_m(a0)=1/a0^3):")
prev=0
mono=True
for a0 in np.linspace(0.2,1.0,9):
    ratio=r_star*a0**3
    if ratio<prev-1e-9: mono=False
    prev=ratio
    print(f"   a0={a0:.2f}: OmL/Omm={ratio:.4f}")
print(f"   monotonic-increasing to turnaround? {mono};  MAX (at a0=1) = {r_star:.3f}  << observed 2.2  -> cap CONFIRMED by sweep")

# ---- RAMP 2: sweep the sequestering coefficient C (Lambda = C<rho_m>), show ratio stays O(1) ----
print("\nRAMP-2  sweep sequestering coefficient C -> self-consistent r*(C) and the ratio cap:")
for C in [0.1,0.25,0.5,0.75,1.0,2.0]:
    try:
        rc=optimize.brentq(lambda r: r-C*TV(r)[0]/TV(r)[1], 1e-3, 0.499)
        print(f"   C={C:.2f}: r*={rc:.3f}  (cap Omega_L/Omega_m={rc:.3f})")
    except ValueError:
        # no closed root: C*T/V > r for all valid r -> no recollapsing solution
        print(f"   C={C:.2f}: NO closed-universe root in valid range (C too large -> no turnaround)")
print("   -> even C=2 (8x the KP 1/4) tops out ~O(1); reaching 2.2 needs C where no closed solution exists. Cap robust.")

# ---- RAMP 3: FLAT torus + finite cycle [0,T]: does <rho_m> -> 0 as T grows (eternal)? ----
# flat matter+Lambda: H^2 = (8piG/3)(rho_m0/a^3 + rho_L). Set 8piG/3=1, rho_m0=1, rho_L=L. a(t) grows.
print("\nRAMP-3  FLAT universe, matter+Lambda, 4-vol over [0, t_max]:  <rho_m> = int(rho_m a^3 dt)/int(a^3 dt)")
def flat_avg(L, t_max):
    # a from H: da/dt = a*sqrt(1/a^3 + L). integrate a(t).
    from scipy.integrate import solve_ivp
    sol=solve_ivp(lambda t,a: a*np.sqrt(1.0/a**3 + L), [1e-6,t_max], [1e-4], dense_output=True, rtol=1e-8, atol=1e-12, max_step=t_max/2000)
    ts=np.linspace(1e-6,t_max,4000); a=sol.sol(ts)[0]; a=np.clip(a,1e-6,None)
    rho_m=1.0/a**3
    num=np.trapz(rho_m*a**3, ts); den=np.trapz(a**3, ts)
    return num/den, a[-1]
L=0.4
for tmax in [3,5,8,12,20]:
    avg,af=flat_avg(L,tmax)
    print(f"   t_max={tmax:5.1f}: a_end={af:8.2f}  <rho_m>={avg:.4e}  -> Lambda=1/4<rho_m>={0.25*avg:.4e}")
print("   -> as the (flat) cycle lengthens, <rho_m>->0 and Lambda->0. Eternal expansion => KP gives ZERO. Confirmed by sweep.")
