import numpy as np
from cobaya.yaml import yaml_load
from cobaya.model import get_model

info = yaml_load(open('/home/themilkmanj/prtoe_class/triad_config.yaml'))
info['sampler'] = {'evaluate': {}}
info['output'] = 'chains/triad_eval'

try:
    model = get_model(info)
    point = {
        'omega_b': 0.0224,
        'H0': 75.8,
        'logA': 3.05,
        'n_s': 0.965,
        'z_reio': 8.0,
        'A_planck': 1.0,
        'dcdf_rho_inf': 0.7,
        'xi_Neff': 0.3,
        'varying_alpha': 1.05,
        'dcdf_beta': 5.0e-5
    }
    
    logpost, derived = model.logposterior(point)
    print("----- EVALUATION RESULTS -----")
    print(f"Log Posterior: {logpost}")
    print(f"Chi2: {-2 * logpost}")
    for k, v in derived.items():
        if 'chi2' in k:
            print(f"{k}: {v}")
except Exception as e:
    import traceback
    traceback.print_exc()
