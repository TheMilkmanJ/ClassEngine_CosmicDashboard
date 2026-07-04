import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import json

# Paths to the respective python wrappers
PRTOE_CLASSY_DIR = "SYSTEM"
HI_CLASS_CLASSY_DIR = "/home/themilkmanj/hi_class/python/build"

def run_class_in_subprocess(class_dir, params, output_file):
    """
    Runs a specific CLASS version in an isolated subprocess to prevent
    'classy' namespace collisions in Python.
    """
    script_content = f"""
import sys
import os
import json

# Find the specific lib.linux directory for the classy module
build_dir = "{class_dir}"
if build_dir != "SYSTEM":
    try:
        lib_dir = next(os.path.join(build_dir, d) for d in os.listdir(build_dir) if d.startswith('lib.'))
        sys.path.insert(0, lib_dir)
    except StopIteration:
        print("Could not find classy lib in " + build_dir)
        sys.exit(1)
    except FileNotFoundError:
        print("Could not find build directory " + build_dir)
        sys.exit(1)

from classy import Class

params = {repr(params)}

cosmo = Class()
cosmo.set(params)
cosmo.compute()

# Extract unlensed Cls
cls = cosmo.raw_cl(2500)
l = cls['ell']
tt = cls['tt']
ee = cls['ee']
te = cls['te']

with open("{output_file}", 'w') as f:
    json.dump({{'l': l.tolist(), 'tt': tt.tolist(), 'ee': ee.tolist(), 'te': te.tolist()}}, f)

cosmo.struct_cleanup()
cosmo.empty()
"""
    script_path = f"/tmp/run_class_{os.path.basename(os.path.dirname(class_dir))}.py"
    with open(script_path, 'w') as f:
        f.write(script_content)
        
    res = subprocess.run(["python", script_path], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error running CLASS in {class_dir}:")
        print(res.stderr)
    return res.returncode == 0


def main():
    print("Setting up PRTOE vs hi_class cross-validation...")
    
    # 1. Define the baseline LCDM or Dark Energy parameters
    shared_params = {
        'output': 'tCl, pCl, lCl',
        'l_max_scalars': 2500,
        'lensing': 'yes',
        'A_s': 2.1e-9,
        'n_s': 0.965,
        'h': 0.7,
        'Omega_b': 0.05,
        'Omega_cdm': 0.25,
        'Omega_k': 0.0,
    }
    
    # 2. Add PRTOE specific params
    prtoe_params = shared_params.copy()
    prtoe_params.update({
        'use_prtoe': 'yes',
        'Omega0_prtoe': 0.7,  # Exact remainder
        'xi_prtoe': 1e-7,     # Small but active dark sector
        'Omega_Lambda': 0.0,
    })
    
    # 3. Add hi_class specific params for the equivalent model
    # We will use hi_class's default LCDM / Smg configuration
    hi_class_params = shared_params.copy()
    hi_class_params.update({
        'Omega_smg': 0.7,
        'gravity_model': 'propto_omega',
        'parameters_smg': '1., 0., 0., 0., 1.',
        'expansion_model': 'lcdm',
        'expansion_smg': 0.5,
    })
    
    prtoe_out = "/tmp/prtoe_cls.json"
    hiclass_out = "/tmp/hiclass_cls.json"
    
    print("Running PRTOE...")
    if not run_class_in_subprocess(PRTOE_CLASSY_DIR, prtoe_params, prtoe_out):
        print("PRTOE failed.")
        return
        
    print("Running hi_class...")
    if not run_class_in_subprocess(HI_CLASS_CLASSY_DIR, hi_class_params, hiclass_out):
        print("hi_class failed.")
        return
        
    print("Comparing results...")
    with open(prtoe_out, 'r') as f:
        prtoe_data = json.load(f)
    with open(hiclass_out, 'r') as f:
        hi_data = json.load(f)
        
    l = np.array(prtoe_data['l'])
    tt_prtoe = np.array(prtoe_data['tt'])
    tt_hi = np.array(hi_data['tt'])
    
    # Calculate fractional difference
    diff = (tt_prtoe - tt_hi) / tt_hi
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(l[2:], diff[2:], label="(PRTOE - hi_class)/hi_class (TT)")
    plt.axhline(0, color='k', linestyle='--', alpha=0.5)
    plt.xlabel('Multipole $\ell$')
    plt.ylabel('Fractional Difference')
    plt.title('PRTOE vs hi_class Cross-Validation')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('cross_validation_results.png', dpi=300)
    print("Plot saved to cross_validation_results.png")
    
if __name__ == "__main__":
    main()
