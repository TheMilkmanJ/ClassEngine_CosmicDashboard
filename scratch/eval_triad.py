import yaml
from cobaya.model import get_model
from cobaya.run import run
import sys

with open("triad_config.yaml", "r") as f:
    info = yaml.safe_load(f)

# Fix parameters to the matched point
info['params']['H0']['ref'] = 74.8
info['params']['varying_alpha']['ref'] = 1.05
info['params']['dcdf_beta']['ref'] = 3.3e-5
info['params']['xi_Neff']['ref'] = 0.3
info['params']['dcdf_rho_inf']['ref'] = 0.7

for p, pinfo in info['params'].items():
    if isinstance(pinfo, dict) and 'ref' in pinfo:
        pinfo['value'] = pinfo.pop('ref')
        if 'prior' in pinfo:
            del pinfo['prior']
        if 'proposal' in pinfo:
            del pinfo['proposal']

info['sampler'] = {'evaluate': {}}
if 'output' in info:
    del info['output']
if 'debug' in info:
    info['debug'] = False

try:
    model = get_model(info)
    loglike, derived = model.loglike({})
    print("\n--- RESULTS ---")
    print(f"Total Chi2: {-2 * loglike}")
    if isinstance(derived, dict):
        for k, v in derived.items():
            print(f"{k}: {v}")
    else:
        print(f"Derived: {derived}")
except Exception as e:
    print(f"Error evaluating chi2: {e}")
