import os
import subprocess
import re
import numpy as np

def update_coupling(coupling):
    filepath = '/home/themilkmanj/prtoe_class/source/thermodynamics.c'
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace the coupling line
    new_line = f'      double dcdf_cmb_coupling = {coupling}; /* Phenomenological coupling to offset Silk damping */'
    content = re.sub(r'      double dcdf_cmb_coupling = [^;]+; /\* Phenomenological coupling to offset Silk damping \*/', new_line, content)
    
    with open(filepath, 'w') as f:
        f.write(content)

def recompile():
    print("Recompiling...")
    subprocess.run(['make', 'clean'], cwd='/home/themilkmanj/prtoe_class', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['make', '-j4'], cwd='/home/themilkmanj/prtoe_class', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Recompiled.")

def run_cobaya():
    print("Running cobaya...")
    result = subprocess.run(
        ['cobaya-run', 'eval_triad.updated.yaml'],
        cwd='/home/themilkmanj/prtoe_class',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    chi2_cmb = None
    chi2_total = None
    for line in result.stdout.split('\n'):
        if 'chi2__CMB' in line:
            match = re.search(r'chi2__CMB\s*=\s*([0-9\.]+)', line)
            if match:
                chi2_cmb = float(match.group(1))
        if 'log-likelihood' in line:
            match = re.search(r'log-likelihood\s*=\s*([0-9\.\-]+)', line)
            if match:
                chi2_total = -2 * float(match.group(1))
    
    return chi2_cmb, chi2_total

def main():
    test_values = [0.0, 0.01, -0.01, 0.1, -0.1, 0.5, -0.5]
    
    results = []
    
    for val in test_values:
        print(f"Testing coupling = {val}")
        update_coupling(val)
        recompile()
        chi2_cmb, chi2_total = run_cobaya()
        print(f"Result for {val}: CMB chi2 = {chi2_cmb}, Total chi2 = {chi2_total}")
        results.append((val, chi2_cmb, chi2_total))
        
    print("\n\n--- Final Results ---")
    for r in results:
        print(f"Coupling {r[0]}: CMB chi2 = {r[1]}, Total chi2 = {r[2]}")

if __name__ == '__main__':
    main()
