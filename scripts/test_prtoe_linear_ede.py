#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from classy import Class

def get_ede_fraction(xi1, xi=1e-5):
    c = Class()
    c.set({
        'h': 0.7, 'Omega_b': 0.05, 'Omega_cdm': 0.25, 'Omega_k': 0,
        'A_s': 2.1e-9, 'n_s': 0.965,
        'use_prtoe': 'yes',
        'prtoe_ablate_gates': 'no',   # keep gates to survive radiation era
        'phi_c_prtoe': 0.01,           # restore to default
        'xi_prtoe': xi,
        'xi1_prtoe': xi1,
        'g3_prtoe': 1.0,
        'Omega0_prtoe': 0.7,
        'Omega_Lambda': 0.0,
        'root': '/home/themilkmanj/prtoe_class/',
        'background_verbose': 1,
    })
    c.compute()
    
    bg = c.get_background()
    z = bg['z']
    
    # Calculate energy fractions
    # 'rho_prtoe' is the effective energy density of the scalar field
    try:
        rho_phi = bg['(.)rho_prtoe']
    except KeyError:
        rho_phi = bg['(.)rho_scf']
    rho_tot = bg['(.)rho_crit']
    
    f_ede = rho_phi / rho_tot
    
    # Print the maximum EDE fraction around recombination (z=1100 to z=3400)
    mask = (z > 100) & (z < 5000)
    max_f_ede = np.max(f_ede[mask])
    z_max = z[mask][np.argmax(f_ede[mask])]
    print(f"For xi1={xi1}, max f_EDE = {max_f_ede*100:.6e}% at z = {z_max:.0f}")
    
    c.struct_cleanup()
    c.empty()
    return z, f_ede

def main():
    plt.figure(figsize=(10, 6))
    
    # Baseline without linear coupling
    z_base, f_base = get_ede_fraction(0.0)
    plt.semilogx(z_base, f_base, 'k--', label='Base (xi1=0)')
    
    # Varying linear coupling
    for xi1 in [1e-6, 1e-5, 5e-5]:
        z, f = get_ede_fraction(xi1)
        plt.semilogx(z, f, label=f'xi1={xi1}')
        
    plt.xlim(1e4, 10)
    plt.xlabel('Redshift z')
    plt.ylabel('Fractional Energy Density $f_{\\rm EDE}(z)$')
    plt.title('PRTOE Natural EDE Activation from Trace ($R$)')
    plt.legend()
    plt.grid(True)
    plt.savefig('ede_fraction.png')
    print("Saved ede_fraction.png")

if __name__ == '__main__':
    main()
