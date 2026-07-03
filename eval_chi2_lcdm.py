import yaml
from cobaya.model import get_model
import sys

with open("templates/lcdm_baseline.yaml", "r") as f:
    info = yaml.safe_load(f)

# Fix all parameters to their reference values so we just do one evaluation
for p, pinfo in info['params'].items():
    if isinstance(pinfo, dict) and 'ref' in pinfo:
        pinfo['value'] = pinfo.pop('ref')
        if 'prior' in pinfo:
            del pinfo['prior']
        if 'proposal' in pinfo:
            del pinfo['proposal']

# We just want to evaluate the likelihoods
info['sampler'] = {'evaluate': {}}
if 'output' in info:
    del info['output']

model = get_model(info)
loglike, derived = model.loglike({})

print("\n--- RESULTS ---")
print(f"Log-Likelihood: {loglike}")
try:
    if isinstance(derived, dict):
        for k, v in derived.items():
            print(f"{k}: {v}")
    else:
        print(f"Derived: {derived}")
        print("Chi2 components are usually printed by Cobaya in the logs above.")
except Exception as e:
    print(f"Error printing derived: {e}")
