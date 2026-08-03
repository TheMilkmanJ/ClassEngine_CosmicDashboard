import numpy as np
from scipy import integrate, optimize
alpha=1/137.035999; me=510998.95; pi=np.pi
alpha_c=3*alpha; obs=2.25e-3
def DE(Tc): return 4.5*alpha**4*Tc

# EXACT fermionic thermal function derivative: J_F'(y) = -y * int_0^inf x^2/(E (e^E+1)) dx, E=sqrt(x^2+y^2)
def absJFprime(y):
    f=lambda x:(x*x/(np.sqrt(x*x+y*y)*(np.exp(np.sqrt(x*x+y*y))+1)))
    val,_=integrate.quad(f,0,60,limit=200)
    return y*val   # |J_F'| (positive)

# high-T check: |J_F'(y)| -> (pi^2/12) y for y<<1
for y in [0.05,0.2]:
    print(f"  |J_F'({y})| exact={absJFprime(y):.5f}  high-T (pi^2/12)y={pi**2/12*y:.5f}")

# Balance (kappa cancels):  (L-1)/8 = (Tc/me)^3 * |J_F'(me/Tc)|   [EXACT thermal]  vs  high-T gives (pi^2/12) t^2
def solve_Tc_exact(Lm1):
    def g(t):  # t=Tc/me
        return t**3*absJFprime(1.0/t) - Lm1/8.0
    return me*optimize.brentq(g, 1e-3, 0.99)
def Tc_highT(Lm1):  # (pi^2/12) t^2 = (L-1)/8 -> t=sqrt(3(L-1)/2pi^2)  (the model's formula)
    return me*np.sqrt(3*Lm1/(2*pi**2))

print("\n=== EXACT thermal function vs the model's high-T formula, RAMP over the zero-T scale mu ===")
print(f"{'mu (keV)':>9} {'L-1':>6} {'Tc_highT':>9} {'Tc_exact':>9} {'DE_exact':>9} {'DE/obs':>7}")
for mu in [60e3,100e3,150e3,241e3]:
    Lm1=np.log(me**2/mu**2)-1.5
    if Lm1<=0: 
        print(f"{mu/1e3:9.0f} {Lm1:6.2f}  (no SSB)"); continue
    Thi=Tc_highT(Lm1); Tex=solve_Tc_exact(Lm1)
    print(f"{mu/1e3:9.0f} {Lm1:6.2f} {Thi/1e3:9.1f} {Tex/1e3:9.1f} {DE(Tex)*1e3:9.3f} {DE(Tex)/obs:7.2f}")

print("\n  (mu = physical VEV scale v ~ 100 keV is the RG-improved zero-T choice)")
mu=100e3; Lm1=np.log(me**2/mu**2)-1.5; Tex=solve_Tc_exact(Lm1); Thi=Tc_highT(Lm1)
print(f"  at mu=v=100keV: high-T formula T_c={Thi/1e3:.0f} keV (DE={DE(Thi)/obs:.2f}x); EXACT T_c={Tex/1e3:.0f} keV (DE={DE(Tex)/obs:.2f}x)")
print(f"  => the Boltzmann suppression (T_c < m_e) pushes T_c {'UP' if Tex>Thi else 'DOWN'} by {Tex/Thi:.2f}x vs the high-T formula.")
