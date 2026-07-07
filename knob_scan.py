#!/usr/bin/env python3
"""Knob-family completion: free-Y_p, Omega_k, running — theta*-locked pricing.
Pinned expectations (pre-run): Y_p small credit at best; Omega_k ~0; alpha_s <= -2.
Sign convention: positive = chi2 PENALTY."""
import sys, subprocess, os, yaml, copy
sys.path.insert(0, "/home/themilkmanj/prtoe_class/python")
import classy, numpy as np
TARGET = 1.042150
BASE_CLASSY = {'output':'','use_dcdf':'yes','dcdf_deltam_mode':1,
    'N_ur':2.0328,'N_ncdm':1,'T_ncdm':0.71611,'m_ncdm':0.0654,'xi_Neff':0.0,
    'varying_fundamental_constants':'instantaneous','varying_me':1.010294,
    'varying_alpha':1.0,'varying_transition_redshift':50.0,
    'omega_b':0.022757,'A_s':1e-10*np.e**3.059448,'n_s':0.970999,'z_reio':8.363414,
    'dcdf_rho_inf':0.701221}
YHE0 = 0.2471+0.0096*np.log(0.022757/0.02236)+0.17*0.010294
def theta(H0, extra):
    p=dict(BASE_CLASSY); p['YHe']=YHE0; p.update(extra)
    p['H0']=H0; p['Omega0_dcdf']=1.0-p['omega_b']/(H0/100.)**2 - p.get('Omega_k',0.0)
    M=classy.Class(); M.set(p); M.compute()
    t=M.get_current_derived_parameters(['100*theta_s'])['100*theta_s']
    M.struct_cleanup(); M.empty(); return t
VARIANTS = [
 ('omk_m',   {'Omega_k':-0.005}), ('omk_p', {'Omega_k':0.005}),
 ('nrun_m',  {'alpha_s':-0.01}), ('nrun_p', {'alpha_s':0.01}),
]
base=yaml.safe_load(open('/home/themilkmanj/prtoe_class/alpha_eval_1000.yaml'))
for tag, extra in VARIANTS:
    lo,hi=64.0,78.0
    for _ in range(18):
        mid=(lo+hi)/2
        if theta(mid,extra)<TARGET: lo=mid
        else: hi=mid
    H0=(lo+hi)/2
    print(f"{tag}: {extra} relocked H0 = {H0:.3f}", flush=True)
    c=copy.deepcopy(base); c['params']['H0']=float(H0)
    ea=c['theory']['classy']['extra_args']
    for k,v in extra.items():
        if k=='YHe': c['params']['YHe']=float(v)   # override the lambda
        else: ea[k]=float(v)
    if 'Omega_k' in extra:
        c['params']['Omega0_dcdf']={'value':'lambda omega_b, H0: 1.0 - (omega_b)/(H0/100.0)**2 - (%f)'%extra['Omega_k'],'derived':False}
    c['output']=f'chains/knob_{tag}'
    fn=f'/home/themilkmanj/prtoe_class/knob_{tag}.yaml'
    yaml.safe_dump(c,open(fn,'w'),default_flow_style=False)
    r=subprocess.run(['/usr/bin/python3','-m','cobaya','run',fn,'--packages-path',
        '/home/themilkmanj/cobaya_packages_clean','--force'],capture_output=True,text=True,
        env={**os.environ,'OMP_NUM_THREADS':'4'})
    got=[l for l in (r.stdout+r.stderr).splitlines() if 'chi2_planck_2018_highl' in l or 'chi2_act' in l or 'chi2_sn' in l]
    for l in got: print("   ",l.strip(),flush=True)
    if not got: print("    [EVAL FAILED — check]",flush=True)
print("knob scan complete",flush=True)
