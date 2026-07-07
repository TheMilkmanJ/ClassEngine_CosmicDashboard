import numpy as np
from classy import Class

def run_model(name, params):
    c = Class()
    c.set(params)
    try:
        c.compute()
    except Exception as e:
        print(f"[{name}] CLASS failed to compute: {e}")
        return None
    
    # Extract background quantities
    ba = c.get_background()
    th = c.get_thermodynamics()
    
    # Get derived parameters
    h = c.h()
    
    print(f"\n=== Model: {name} ===")
    print(f"h         = {h:.5f}")
    
    # Check sound horizon at drag epoch
    rs_drag = c.rs_drag()
    print(f"rs_drag = {rs_drag:.5f} Mpc")
    
    # If PRTOE is active, check F(phi) at recombination
    z_rec = 1090.0 # Approximate
    
    # Find index in thermodynamics table closest to z_rec
    z_th = th['z']
    idx = np.argmin(np.abs(z_th - z_rec))
    
    # For background, find the corresponding F
    z_bg = ba['z']
    idx_bg = np.argmin(np.abs(z_bg - z_rec))
    
    if '(.)F_prtoe' in ba:
        F_rec = ba['(.)F_prtoe'][idx_bg]
        phi_rec = ba['(.)phi_prtoe'][idx_bg]
        print(f"F(z={z_bg[idx_bg]:.1f}) = {F_rec:.5f}")
        print(f"phi(z={z_bg[idx_bg]:.1f}) = {phi_rec:.5f}")
    
    c.struct_cleanup()
    c.empty()
    return rs_drag

base_params = {
    'h': 0.674, 
    'Omega_b': 0.05, 
    'Omega_cdm': 0.25,
    'A_s': 2.1e-9, 
    'n_s': 0.965,
    'output': '',
    'background_verbose': 1,
    'thermodynamics_verbose': 1
}

# 1. LCDM
params_lcdm = base_params.copy()
params_lcdm['use_prtoe'] = 'no'
run_model("LCDM", params_lcdm)

# 2. PRTOE xi1 > 0
params_pos = base_params.copy()
params_pos.update({
    'use_prtoe': 'yes',
    'prtoe_ablate_gates': 'no',
    'Omega0_prtoe': 0.7,
    'Omega_Lambda': 0.0,
    'xi1_prtoe': 0.3,
    'xi_prtoe': 1e-7,
    'm_prtoe': 1e-12,
    'g3_prtoe': 0.0
})
run_model("PRTOE (xi1 = +0.3)", params_pos)

# 3. PRTOE xi1 < 0
params_neg = base_params.copy()
params_neg.update({
    'use_prtoe': 'yes',
    'prtoe_ablate_gates': 'no',
    'Omega0_prtoe': 0.7,
    'Omega_Lambda': 0.0,
    'xi1_prtoe': -0.3,
    'xi_prtoe': 1e-7,
    'm_prtoe': 1e-12,
    'g3_prtoe': 0.0
})
run_model("PRTOE (xi1 = -0.3)", params_neg)
