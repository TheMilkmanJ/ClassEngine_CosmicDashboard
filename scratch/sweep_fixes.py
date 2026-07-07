import subprocess
import os

def run_class(phase_c, damp_c):
    # Modify perturbations.c
    with open('source/perturbations.c', 'r') as f:
        code = f.read()
    
    # We need to find the block and replace the constants
    import re
    # Match the block
    pattern = r'(double phase_boost = 1\.0 \+ )([0-9\.\-]+)( \* Omega_dcdf;\s+/\* Phase shift.*?dy\[pv->index_pt_shear_g\] )([\+\-])(= )([0-9\.\-]+)( \* Omega_dcdf)'
    
    def repl(m):
        sign = '-' if damp_c > 0 else '+'
        return f"{m.group(1)}{phase_c}{m.group(3)}{sign}{m.group(5)}{abs(damp_c)}{m.group(7)}"
        
    new_code = re.sub(pattern, repl, code, flags=re.DOTALL)
    if new_code == code:
        print("Regex failed to match!")
        return None
        
    with open('source/perturbations.c', 'w') as f:
        f.write(new_code)
        
    # Rebuild CLASS
    subprocess.run("make clean && make -j4", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Run evaluation
    res = subprocess.run("cobaya-run eval_triad.updated.yaml", shell=True, capture_output=True, text=True)
    out = res.stdout + res.stderr
    
    # Extract chi2
    chi2 = None
    for line in out.split('\n'):
        if 'chi2_planck_2018_highl_plik.TTTEEE_lite' in line:
            chi2 = float(line.split('=')[1].strip())
            break
            
    return chi2

print("Running grid search...")
for pc in [0.0, 0.01, 0.05]:
    for dc in [0.0, 1.0, 5.0]:
        chi2 = run_class(pc, dc)
        print(f"Phase={pc}, Damp={dc} -> chi2={chi2}")
