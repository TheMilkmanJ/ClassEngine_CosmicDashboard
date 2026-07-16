import numpy as np
from scipy import integrate, optimize
# a_ta=1, rho_m,ta=1, 8piG/3=1, r=rho_L/rho_m,ta ; adot^2 = 1/a + r a^2 - (1+r)
def adot2(a,r): return 1.0/a + r*a*a - (1.0+r)
def TV(r):
    fT=lambda a:(1.0/np.sqrt(adot2(a,r)) if adot2(a,r)>0 else 0.0)
    fV=lambda a:(a**3/np.sqrt(adot2(a,r)) if adot2(a,r)>0 else 0.0)
    T=integrate.quad(fT,0,1,points=[1],limit=400)[0]
    V=integrate.quad(fV,0,1,points=[1],limit=400)[0]
    return T,V
# self-consistency r = 1/4 * T/V ; valid r range: adot2>0 on (0,1) -> interior min at a=(2r)^-1/3 must be >=1 => r<=0.5
res=lambda r: r - 0.25*TV(r)[0]/TV(r)[1]
print("scan:")
for r in [0.05,0.1,0.2,0.3,0.4,0.45]:
    T,V=TV(r); print(f"  r={r:.2f}: T/V={T/V:.4f}  1/4 T/V={0.25*T/V:.4f}  resid={res(r):+.4f}")
r_star=optimize.brentq(res,0.2,0.49)
T,V=TV(r_star)
print(f"\nSELF-CONSISTENT: r* = rho_L/rho_m,turnaround = {r_star:.4f}  (<rho_m>/rho_ta={T/V:.4f})")
print(f"KP coefficient Lambda/rho_m,ta = 1/4 <rho_m>/rho_ta = {0.25*T/V:.4f}  (cf toy 3/4=0.75 in cosmo_const 7a)")

# --- THE CAP: Omega_L/Omega_m during expansion is <= r* (peaks at turnaround, smaller earlier) ---
print(f"\n*** Omega_L/Omega_m is CAPPED at r* = {r_star:.3f} during the whole expansion (max at turnaround) ***")
print(f"    OBSERVED Omega_L/Omega_m = 2.2  ->  KP under-predicts the ratio by {2.2/r_star:.1f}x")

# --- the value, IF turnaround ~ now (rho_m,ta ~ rho_m0) ---
H0=67.0; rho_crit_q = 2.481e-3*(H0/67.0)**0.5  # rho_crit^1/4 ~ 2.48 meV at H0=67
Om=0.315; rho_m0_q = Om**0.25*rho_crit_q
Lam_q = (0.25*T/V)**0.25 * rho_m0_q   # Lambda^1/4 = (coeff)^1/4 * rho_m,ta^1/4, turnaround~now
print(f"\nvalue if turnaround~now: rho_m0^1/4={rho_m0_q*1e3:.2f} meV -> Lambda^1/4={Lam_q*1e3:.2f} meV  ({Lam_q/2.25e-3:.2f}x obs 2.25)")
print("(cosmo_const 7a quoted 1.71 meV=0.76x using the toy 3/4 coeff; the PROPER coeff 0.46 gives ~1.5 meV=0.68x)")
print("\n=> BUT the value is moot: the RATIO cap (0.46 vs 2.2) means the mechanism can't seat DE where observed.")
