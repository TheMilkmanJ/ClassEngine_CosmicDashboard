#!/usr/bin/env python3
import numpy as np
from classy import Class

def get_max_f_ede(xi1):
    c = Class()
    c.set({
        'h': 0.7, 'Omega_b': 0.05, 'Omega_cdm': 0.25, 'Omega_k': 0,
        'A_s': 2.1e-9, 'n_s': 0.965,
        'use_prtoe': 'yes',
        'prtoe_ablate_gates': 'no',
        'phi_c_prtoe': 0.01,
        'xi_prtoe': 1e-5,
        'xi1_prtoe': xi1,
        'g3_prtoe': 1.0,
        'Omega0_prtoe': 0.7,
        'Omega_Lambda': 0.0,
        'root': '/home/themilkmanj/prtoe_class/',
        'background_verbose': 0,
    })
    c.compute()
    
    bg = c.get_background()
    z = bg['z']
    
    try:
        rho_phi = bg['(.)rho_prtoe']
    except KeyError:
        rho_phi = bg['(.)rho_scf']
    rho_tot = bg['(.)rho_crit']
    
    f_ede = rho_phi / rho_tot
    
    # We want max f_EDE around recombination (z=1000 to z=5000)
    mask = (z > 1000) & (z < 5000)
    max_f = np.max(f_ede[mask])
    
    c.struct_cleanup()
    c.empty()
    return max_f * 100 # returned as percentage

def sweep():
    print("Targeting f_EDE = 0.440%")
    points = [0.01, 0.02, 0.05, 0.1, 0.2]
    for p in points:
        val = get_max_f_ede(p)
        print(f"xi1 = {p:e}, max f_EDE = {val:e}%")
        
sweep()
