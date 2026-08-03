import os, glob
import numpy as np
import pandas as pd

results = []
for f in sorted(glob.glob('/home/themilkmanj/prtoe_class/chains/*.1.txt')):
    try:
        with open(f, 'r') as file:
            header = file.readline().strip()
            if not header.startswith('#'):
                continue
            cols = header.split()[1:]
            
        df = pd.read_csv(f, sep='\s+', comment='#', names=cols)
        if 'minuslogpost' in df.columns and 'chi2' in df.columns:
            min_logpost = df['minuslogpost'].min()
            min_chi2 = df['chi2'].min()
            results.append((os.path.basename(f), min_logpost, min_chi2))
    except Exception as e:
        print(f"Error reading {f}: {e}")

print(f"{'Chain':<30} | {'Min -log(Post)':<15} | {'Min chi^2':<15}")
print("-" * 65)
for name, mlp, mc2 in sorted(results, key=lambda x: x[1]):
    print(f"{name:<30} | {mlp:<15.2f} | {mc2:<15.2f}")
