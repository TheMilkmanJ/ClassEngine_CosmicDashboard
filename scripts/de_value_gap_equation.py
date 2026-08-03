import numpy as np
from scipy import integrate, optimize
alpha=1/137.035999; me=510998.95; keV=1e3
alpha_c=3*alpha
obs=2.25e-3
def DE(Tc): return 4.5*alpha**4*Tc

# NON-PERTURBATIVE GAP EQUATION (NJL/BCS for the composite dyad).
# Dyad = fermion bilinear condensate; 4-fermion coupling G, cutoff Lambda (compositeness scale).
# Critical temperature (M->0, 2nd order): 1 = g * I(tau),  g = N G Lambda^2/pi^2 (dimensionless),
#   tau = T_c/Lambda,  I(tau) = integral_0^1 x tanh(x/2tau) dx.
def I(tau):
    return integrate.quad(lambda x: x*np.tanh(x/(2*tau)), 0, 1, limit=200)[0]
def tau_of_g(g):
    # solve 1 = g I(tau) for tau
    if g<=2.0+1e-9: return 0.0   # g_c=2 is the critical coupling (I(0)=1/2)
    return optimize.brentq(lambda t: g*I(t)-1.0, 1e-4, 5.0)

print("=== (A) The gap equation gives a WELL-DEFINED T_c (no log ambiguity). RAMP over coupling g ===")
print(f"  critical coupling g_c = 2 (I(0)=1/2). Above it, T_c/Lambda = tau(g):")
print(f"  {'g':>5} {'tau=Tc/Lam':>11}")
for g in [2.1,2.5,2.86,3.5,5,8]:
    print(f"  {g:5.2f} {tau_of_g(g):11.4f}")
print("  -> monotonic, finite, unique. The NJL gap equation RESOLVES the perturbative log-ambiguity.")

print("\n=== (B) Set the compositeness scale Lambda = m_e (electron-pair composite): what g gives the DE value? ===")
Lam=me
# DE-preferred T_c and the model's ~193 keV
for label,Tc_target in [("DE-exact (176 keV)",176*keV),("model central (193 keV)",193*keV)]:
    tau=Tc_target/Lam
    g=1.0/I(tau)
    print(f"  {label}: tau={tau:.3f} -> g={g:.3f}  -> DE=(9/2)a^4 T_c = {DE(Tc_target)*1e3:.3f} meV ({DE(Tc_target)/obs:.2f}x)")

print("\n=== (C) RAMP the compositeness scale Lambda (is m_e special?) at fixed strong g=3 ===")
g=3.0; tau=tau_of_g(g)
print(f"  at g=3: tau=T_c/Lambda={tau:.3f}")
for Lam_keV in [100,300,511,900]:
    Tc=tau*Lam_keV*keV
    print(f"  Lambda={Lam_keV:4d} keV -> T_c={Tc/keV:6.1f} keV -> DE={DE(Tc)/obs:.2f}x")
print("\nVERDICT: the gap equation gives a WELL-DEFINED T_c = Lambda*tau(g) -- the perturbative log-ambiguity")
print("is GONE. The DE value becomes rho_L^1/4 = (9/2)a^4 Lambda tau(g). For Lambda=m_e and g~2.6-2.9")
print("(moderately above the critical g_c=2), T_c ~ 176-193 keV -> DE ~ 1.0-1.1x. The residual is now TWO")
print("PHYSICAL medium-compositeness inputs (Lambda, g), not a scheme choice. Progress: ill-defined -> well-")
print("defined-given-(Lambda,g). NOT a closure: Lambda=m_e and g~2.8 are natural but not yet DERIVED.")
