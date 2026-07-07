#!/usr/bin/env python3
"""Task #12: varying-alpha control scan — theta*-locked pricing, joint stack."""
import sys, subprocess, os, yaml, copy
sys.path.insert(0, "/home/themilkmanj/prtoe_class/python")
import classy, numpy as np

TARGET = 1.042150
OPT = dict(omega_b=0.022757, A_s=1e-10*np.e**3.059448, n_s=0.970999,
           z_reio=8.363414, dcdf_rho_inf=0.701221)
def theta(H0, alpha):
    p = {'output':'tCl','l_max_scalars':100,'use_dcdf':'yes','dcdf_deltam_mode':1,
         'N_ur':2.0328,'N_ncdm':1,'T_ncdm':0.71611,'m_ncdm':0.0654,'xi_Neff':0.0,
         'varying_fundamental_constants':'instantaneous','varying_me':1.010294,
         'varying_alpha':alpha,'varying_transition_redshift':50.0,
         'YHe':0.2471+0.0096*np.log(0.022757/0.02236)+0.17*0.010294}
    p.update(OPT); p['H0']=H0; p['Omega0_dcdf']=1.0-p['omega_b']/(H0/100.)**2
    M=classy.Class(); M.set(p); M.compute()
    t=M.get_current_derived_parameters(['100*theta_s'])['100*theta_s']
    M.struct_cleanup(); M.empty(); return t

base = yaml.safe_load(open('/home/themilkmanj/prtoe_class/dyad_mnu_mcmc.yaml'))
FIX = dict(omega_b=0.022757, logA=3.059448, n_s=0.970999, z_reio=8.363414,
           dcdf_rho_inf=0.701221, varying_me=1.010294, A_planck=1.000369,
           A_act=0.999315, P_act=1.002742, Tcal=0.997021, Ecal=1.002174,
           m_ncdm=0.0654)
print(f"theta* target: {TARGET}", flush=True)
for alpha in (1.0, 1.005, 1.01):
    lo,hi=64.0,78.0
    for _ in range(18):
        mid=(lo+hi)/2
        if theta(mid,alpha)<TARGET: lo=mid
        else: hi=mid
    H0=(lo+hi)/2
    print(f"alpha={alpha}: relocked H0 = {H0:.3f}", flush=True)
    cfg=copy.deepcopy(base)
    for name,val in {**FIX,'H0':H0}.items():
        if name in cfg['params']: cfg['params'][name]=float(val)
    # inject varying_alpha into the theory extra_args
    th=cfg['theory']; key=list(th.keys())[0]
    ea=th[key].setdefault('extra_args',{})
    ea['varying_alpha']=float(alpha)
    cfg['sampler']={'evaluate': None}
    cfg['output']=f'chains/alpha_scan_{int(alpha*1000)}'
    fn=f'/home/themilkmanj/prtoe_class/alpha_eval_{int(alpha*1000)}.yaml'
    yaml.safe_dump(cfg,open(fn,'w'),default_flow_style=False)
    r=subprocess.run(['/usr/bin/python3','-m','cobaya','run',fn,'--packages-path',
                      '/home/themilkmanj/cobaya_packages_clean','--force'],
                     capture_output=True,text=True,env={**os.environ,'OMP_NUM_THREADS':'4'})
    for line in (r.stdout+r.stderr).splitlines():
        L=line.lower()
        if 'chi2' in L and ('total' in L or '=' in line): print("   ",line.strip(),flush=True)
    print(f"   [alpha={alpha} eval done]",flush=True)
print("scan complete",flush=True)
