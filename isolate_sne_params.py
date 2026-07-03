import subprocess
import sys
import time
import os

base_prtoe = {
    'omega_b': 0.02275,
    'omega_cdm': 0.12,
    'H0': 67.4,
    'A_s': 2.111534442254061e-09,
    'n_s': 0.965,
    'z_reio': 8.0,
    'xi_prtoe': 1.0119e-07,
    'zeta_prtoe': 0.1,
    'V0_prtoe': 0.6857,
    'lambda_prtoe': 0.05,
    'm_prtoe': 0.05,
    'beta_prtoe': 1.0e-6,
    'use_prtoe': 'yes',
    'output': 'mPk',
    'modes': 's'
}

lcdm_pars = {
    'omega_b': 0.02275,
    'omega_cdm': 0.12,
    'H0': 67.4,
    'A_s': 2.111534442254061e-09,
    'n_s': 0.965,
    'z_reio': 8.0,
    'output': 'mPk',
    'modes': 's'
}

def run_isolated(pars):
    script = f"""
from classy import Class
c = Class()
c.set({repr(pars)})
c.compute()
print(c.luminosity_distance(0.5))
"""
    with open("temp_run.py", "w") as f:
        f.write(script)
    
    res = subprocess.run([sys.executable, "temp_run.py"], capture_output=True, text=True)
    if res.returncode != 0:
        raise Exception(f"Failed: {res.stderr}")
    
    # Extract the last line of output which should be the float
    lines = res.stdout.strip().split('\n')
    for line in reversed(lines):
        try:
            return float(line)
        except ValueError:
            continue
    raise Exception(f"No float found in output: {res.stdout}")

print("Computing LCDM baseline...")
dm_lcdm_05 = run_isolated(lcdm_pars)

print("LCDM DM reference:")
print(f"  z=0.5: DM={dm_lcdm_05:.1f} Mpc")

print("\n" + "="*80)
print("SNe CHI2 ISOLATION TEST (Isolated subprocesses)")
print("="*80)

tests = [
    ("XI_PRTOE", "xi_prtoe", [1e-8, 1e-7, 5e-7, 1e-6]),
    ("ZETA_PRTOE", "zeta_prtoe", [0.01, 0.05, 0.1, 0.5]),
    ("V0_PRTOE", "V0_prtoe", [0.4, 0.5, 0.6857, 0.8, 1.0]),
    ("BETA_PRTOE", "beta_prtoe", [1e-7, 1e-6, 1e-5, 1e-4]),
    ("M_PRTOE", "m_prtoe", [0.01, 0.05, 0.1, 0.2]),
    ("LAMBDA_PRTOE", "lambda_prtoe", [0.02, 0.05, 0.1, 0.2]),
]

for test_name, param, values in tests:
    print(f"\n--- {test_name} ---")
    start = time.time()
    
    for val in values:
        print(f"  Testing {param} = {val}...", flush=True)
        pars = base_prtoe.copy()
        pars[param] = val
        
        try:
            dm_05 = run_isolated(pars)
            
            dm_delta = 100.0 * (dm_05 - dm_lcdm_05) / dm_lcdm_05
            chi2_sne_est = (dm_delta / 1.0) ** 2 * 100
            
            marker = "↑ HIGH" if abs(dm_delta) > 5 else "→ MED" if abs(dm_delta) > 2 else "✓ LOW"
            print(f"    Done. {param}={val:<12} | ΔDM(z=0.5)={dm_delta:+6.2f}% | χ²_est~{chi2_sne_est:6.0f} {marker}")
        except Exception as e:
            print(f"  {param}={val:<12} | ERROR: {e}")
            
    elapsed = time.time() - start
    print(f"(completed in {elapsed:.1f}s)")
