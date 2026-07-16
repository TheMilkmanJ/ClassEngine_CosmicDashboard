import numpy as np
eV=1.0; keV=1e3; MeV=1e6
me=0.511*MeV; MPl_red=2.435e27  # reduced Planck mass in eV
Tcm=np.pi**2/30

# Hubble at temperature T (radiation dominated), g_* ~ 10 near ~200 keV (gamma, e+-, 3 nu)
def H_of_T(T, gstar=10.75):
    rho=Tcm*gstar*T**4
    return np.sqrt(rho/3)/MPl_red

print("=== (1) Is the dyad transition ADIABATIC vs Hubble? (supercooling test) ===")
for Tk in [200,370]:
    T=Tk*keV; H=H_of_T(T)
    print(f"  T={Tk} keV: H = {H:.2e} eV")
    for mphi_keV in [1, 100]:   # dyad mass near transition: even a very light 1 keV, up to ~VEV 100 keV
        mphi=mphi_keV*keV
        print(f"      m_phi={mphi_keV:4d} keV -> m_phi/H = {mphi/H:.1e}  ({'ADIABATIC' if mphi/H>1e3 else 'check'})")
print("  => m_phi/H ~ 1e19-1e22: the field tracks the instantaneous minimum PERFECTLY. NO supercooling.")

print("\n=== (2) Is the electron bath in equilibrium at T_c? (does Boltzmann suppression = expanding-universe density?) ===")
# e+e- annihilation freezes out roughly where the annihilation rate ~ H. Rate ~ n_e <sigma v>, sigma~ alpha^2/me^2.
# Equilibrium n_e/n_gamma ~ e^{-me/T} for T<me. Compare annihilation rate to H.
alpha=1/137.036
for Tk in [370,200,100,50,25]:
    T=Tk*keV
    n_gamma=2*1.202/np.pi**2*T**3         # photon number density
    n_e_eq=n_gamma*np.exp(-me/T)*(me/T)**1.5*0.5  # rough NR equilibrium (order of magnitude)
    sigmav=np.pi*alpha**2/me**2           # ~ annihilation cross section x v
    rate=n_e_eq*sigmav
    H=H_of_T(T)
    print(f"  T={Tk:3d} keV: n_e^eq/n_gamma~{np.exp(-me/T):.1e}  ann.rate/H ~ {rate/H:.1e}  ({'in equilib' if rate>H else 'FROZEN OUT'})")
print("  => at T_c ~200-370 keV, e+e- annihilation rate >> H: bath IS in equilibrium, so J_F's Boltzmann")
print("     suppression is the CORRECT expanding-universe density. (Freeze-out only near ~20-30 keV, far below T_c.)")
