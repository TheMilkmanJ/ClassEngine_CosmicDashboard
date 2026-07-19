import sys, os
# Vendored PRyMordial is gitignored (third-party); this runner lives in scripts/ and
# points at it. Run from the repo root:  python3 scripts/prym_elasticity_runner.py LT 1.0124
_PRYM = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools", "PRyMordial")
os.chdir(_PRYM)
sys.path.insert(0, _PRYM)
# THE eps ELASTICITY SCAN - T13 item 3's blocking input. RESULTS ARE RECORDED IN
# docs/working_logs/T13_fingerprint_owed.md (the scan data itself is gitignored).
# Identical splice machinery to run_windowed.py (the production windowed runner);
# the ONLY change is that `shift` is an argument instead of hardcoded 1.0124, so the
# lattice's rows can be turned from values-at-a-point into FUNCTIONS of eps.
#   usage: run_elasticity.py <LT|MTLT> <shift>      e.g. run_elasticity.py LT 1.0124
# Output (one line, parseable):
#   ELAST <mode> <shift> <eps%> <Neff> <YPCMB> <YPBBN> <DoHx1e5> <He3oHx1e5> <Li7oHx1e10>
mode = sys.argv[1]                 # "LT" or "MTLT"
shift = float(sys.argv[2])         # 1 + eps
import PRyM.PRyM_init as pri
pri.me = 0.51099895                # STANDARD at import (thermo + HT rates standard)
for f in ['compute_nTOp_flag','compute_pTOn_flag']:
    if hasattr(pri, f): setattr(pri, f, True)
if hasattr(pri,'verbose_flag'): pri.verbose_flag = False
import numpy as np
import PRyM.PRyM_nTOp as nTOp_mod
def spliced(Tvec):
    import PRyM.PRyM_eval_nTOp as ev
    import importlib
    from scipy.interpolate import interp1d
    pri.me = 0.51099895
    importlib.reload(ev)
    std = ev.ComputeWeakRates(Tvec)
    pri.me = 0.51099895*shift
    importlib.reload(ev)
    shf = ev.ComputeWeakRates(Tvec)
    pri.me = 0.51099895
    take = {"LT": (std[0],std[1],std[2], std[3],std[4],std[5], shf[6],shf[7],shf[8]),
            "MTLT":(std[0],std[1],std[2], shf[3],shf[4],shf[5], shf[6],shf[7],shf[8])}[mode]
    T_HT,fHT,bHT,T_MT,fMT,bMT,T_LT,fLT,bLT = take
    mk = lambda x,y: interp1d(x,y,bounds_error=False,fill_value="extrapolate",kind='quadratic')
    return [mk(T_HT,fHT),mk(T_HT,bHT),mk(T_MT,fMT),mk(T_MT,bMT),mk(T_LT,fLT),mk(T_LT,bLT)]
nTOp_mod.RecomputeWeakRates = spliced
import PRyM.PRyM_main as prm
r = prm.PRyMclass().PRyMresults()
# res = [Neff, Omeganurel*1e6, 1/Omeganunr, YPCMB, YPBBN, DoHx1e5, He3oHx1e5, Li7oHx1e10]
print("ELAST %s %.6f %.4f %.6f %.6f %.6f %.6f %.6f %.6f" %
      (mode, shift, (shift-1.0)*100, r[0], r[3], r[4], r[5], r[6], r[7]), flush=True)
