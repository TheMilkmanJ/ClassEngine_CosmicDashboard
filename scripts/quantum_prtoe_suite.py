import numpy as np
import os

def run_quantum_suite():
    print("=== RUNNING PHENOMENOLOGICAL QUANTUM PRTOE SUITE ===")
    
    # 1. Proton Charge Radius Puzzle Solver
    # Constants
    alpha = 1.0 / 137.036
    m_e = 1.0
    m_mu = 206.768
    
    # Bohr radii in femtometers (fm)
    a_e = 52917.7
    a_mu = a_e / m_mu
    
    # Density-dependent screening function S(r) = 1 / (1 + (beta * rho)^2)
    # We model the lepton probability density rho(r) = |R_2S(r)|^2
    def R_2S(r, a):
        return (1.0 / (2.0 * np.sqrt(2.0))) * (a**(-1.5)) * (2.0 - r / a) * np.exp(-r / (2.0 * a))
    
    r_grid = np.linspace(0.01, 1000.0, 10000)
    
    # Evaluate densities
    rho_e = (R_2S(r_grid, a_e))**2
    rho_mu = (R_2S(r_grid, a_mu))**2
    
    # PRTOE parameters
    xi = 1.25e-7
    beta_atomic = 1.0e12  # Atomic-scale density coupling (distinct from cosmological beta_prtoe)

    S_e  = 1.0 / (1.0 + (beta_atomic * rho_e)**2)
    S_mu = 1.0 / (1.0 + (beta_atomic * rho_mu)**2)
    
    # Calculate expectation value of the potential shift: Delta V = <V_eff - V_std>
    # Delta V = xi * (alpha/r) * S(r)
    # We use numpy.trapezoid (or trapezoid from numpy) for integration over the radial probability density r^2 * R^2
    P_e = r_grid**2 * rho_e
    P_mu = r_grid**2 * rho_mu
    
    # Normalize densities on grid
    P_e /= np.trapezoid(P_e, r_grid)
    P_mu /= np.trapezoid(P_mu, r_grid)
    
    V_shift_e = (alpha / r_grid) * S_e
    V_shift_mu = (alpha / r_grid) * S_mu
    
    shift_e = xi * np.trapezoid(P_e * V_shift_e, r_grid)
    shift_mu = xi * np.trapezoid(P_mu * V_shift_mu, r_grid)
    
    print("\n1. Proton Radius Puzzle Lamb Shift Corrections:")
    print(f"   Electronic Hydrogen energy shift: {shift_e * 197327.0:.6e} meV")
    print(f"   Muonic Hydrogen energy shift:     {shift_mu * 197327.0:.6e} meV")
    if shift_e < 1e-20:
        print("   WARNING: shift_e ~ 0 — anomalous ratio is unphysical at this coupling.")
    print(f"   Anomalous Ratio (Muon / Electron): {shift_mu / (shift_e + 1e-30):.3f}")

    # 2. Lindblad Macroscopic Decoherence Saturation Solver
    Gamma_0 = 10.0
    beta_dec = 0.5
    xi_dec = 0.1
    S_dec = 0.5
    
    # Distances in meters
    d_atomic = 1e-10
    d_macro = 1.0
    
    def calculate_dephasing(d):
        return Gamma_0 * (d**2 / (1.0 + (beta_dec * d)**2)) * (1.0 - xi_dec * S_dec)
    
    gamma_atomic = calculate_dephasing(d_atomic)
    gamma_macro = calculate_dephasing(d_macro)
    
    print("\n2. Macroscopic Decoherence Saturation:")
    print(f"   Decoherence rate at atomic scale (d = 1e-10 m): {gamma_atomic:.6e} s^-1")
    print(f"   Decoherence rate at macro scale  (d = 1.0 m):   {gamma_macro:.6e} s^-1")
    print(f"   Standard DP divergence at macro scale:           {Gamma_0 * (d_macro**2) * (1.0 - xi_dec * S_dec):.6f} s^-1")

    # 3. Anomalous Quantum Tunneling (WKB approximation)
    # Barrier width L = 2.0 fm, Barrier height V0 = 40 MeV, Particle Energy E = 10 MeV
    m_p = 938.272 # Proton mass in MeV
    V0 = 40.0
    E = 10.0
    L = 2.0
    hbar_c = 197.327 # MeV * fm
    
    # Standard WKB Transmission
    k_std = np.sqrt(2.0 * m_p * (V0 - E)) / hbar_c
    T_std = np.exp(-2.0 * k_std * L)
    
    # PRTOE Softened Barrier
    xi_tun = 0.1
    beta_tun = 0.5
    V0_eff = V0 * (1.0 - (xi_tun / (1.0 + beta_tun**2)))
    k_prtoe = np.sqrt(2.0 * m_p * (V0_eff - E)) / hbar_c
    T_prtoe = np.exp(-2.0 * k_prtoe * L)
    
    print("\n3. WKB Barrier Transmission Probabilities:")
    print(f"   Standard Transmission coefficient: {T_std:.6e}")
    print(f"   PRTOE Transmission coefficient:    {T_prtoe:.6e}")
    print(f"   Transmission enhancement factor:   {T_prtoe / T_std:.3f}")
    print("\n======================================================")

if __name__ == '__main__':
    run_quantum_suite()
