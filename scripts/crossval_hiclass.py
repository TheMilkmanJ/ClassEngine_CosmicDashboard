import sys
import os
import argparse
import numpy as np

def run_class(class_dir, model_type):
    # Insert path to find classy
    sys.path.insert(0, os.path.join(class_dir, 'python/build/lib.linux-x86_64-cpython-313'))
    try:
        import classy
    except ImportError:
        import importlib.util
        spec = importlib.util.spec_from_file_location("classy", os.path.join(class_dir, "python/classy.cpython-313-x86_64-linux-gnu.so"))
        classy = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(classy)
        
    cosmo = classy.Class()
    
    # Common parameters
    params = {
        'omega_b': 0.02237,
        'omega_cdm': 0.12,
        'H0': 67.36,
        'A_s': 2.1e-9,
        'n_s': 0.9649,
        'tau_reio': 0.0544,
        'output': 'tCl, lCl, mPk',
        'lensing': 'yes',
        'l_max_scalars': 2500,
    }
    
    if model_type == 'prtoe':
        params.update({
            'use_prtoe': 'yes',
            'xi_prtoe': 1e-6,
            'zeta_prtoe': 1.0,
            'V0_prtoe': 0.1,
            'lambda_prtoe': 0.05,
            'm_prtoe': 0.05,
            'phi_0_prtoe': 1.0,
            # We want ungated run to compare exactly to Horndeski
            'prtoe_ablate_gates': 'yes'
        })
    elif model_type == 'hi_class':
        params.update({
            'gravity_model': 'brans dicke',
            'parameters_smg': '1e-6, 1.0, 0.1, 0.05, 0.05, 1.0',
            'Omega_Lambda': 0,
            'Omega_fld': 0,
            'Omega_smg': -1,  # Closure
        })
        
    cosmo.set(params)
    cosmo.compute()
    
    cls = cosmo.lensed_cl(2500)
    # Convert to D_l
    ll = cls['ell'][2:]
    dl_tt = cls['tt'][2:] * ll * (ll + 1) / (2 * np.pi)
    
    # Save output
    np.savez(f'crossval_{model_type}.npz', ell=ll, dl_tt=dl_tt)
    print(f"Successfully ran {model_type} and saved Cls.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--class_dir', required=True)
    parser.add_argument('--model', required=True, choices=['prtoe', 'hi_class'])
    args = parser.parse_args()
    
    run_class(args.class_dir, args.model)
