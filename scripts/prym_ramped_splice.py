import sys, os
# THE TRUE RAMPED SPLICE — the decisive BBN computation (depth law, amendment 5).
#
# run_windowed.py brackets the ramped truth with two STEP splices:
#   LT   : full shift in the LT zone only        -> under-counts
#   MTLT : full shift in the MT+LT zones         -> over-counts
# The joint likelihood (T13 item 3) showed that bracket spans p = 0.11 to p = 0.0005 --
# i.e. the step-approximation IS the verdict. Amendment 5 (steps illegal as computational
# entries AND methods) says compute the ramp instead of bracketing it.
#
# THE RAMP the model actually derives:  eps(T) = eps * (1 - T/T_c),  zero above T_c
# ("the dyad is OFF above T_c and ramps on below"). Applied POINTWISE to the weak-rate
# grids rather than by zone:
#
#   rate_ramped(T) = std(T) + [shf(T) - std(T)] * w(T),   w(T) = max(0, 1 - T/T_c)
#
# This is exact at w=0 and w=1 and first-order-correct in between; eps = 1.24% is small
# enough that the rate's departure from linearity in the m_e shift is negligible (the
# scan's own Y_p increments are linear to <2% across 0 -> 1.86%).
#
# THE ETA-FLOW: the CMB fit with varying m_e re-infers omega_b. The witness records that
# shift as +1.1%, driving D/H by -1.8% (D/H ~ omega_b^-1.66, MEASURED by a wide omega_b scan
# through this splice -- scripts/prym_omega_b_elasticity.py; the chains' BBN prior codes -1.6,
# low by 4% and inside the numerics floor). Pass <omega_b_scale> to apply it; the RATIO of the two runs is the
# eta-flow factor, independent of PRyM's absolute omega_b default.
#
#   usage: prym_ramped_splice.py <shift> [T_c_MeV] [omega_b_scale]
#          T_c DEFAULTS to 0.179 MeV -- the DERIVED confining chiral value (tau*m_e), which is
#          what the model actually derives. 0.193 is the perturbative Coleman-Weinberg
#          cross-check (log-ambiguous) and must be passed explicitly if wanted; it is a
#          cross-check, not the model's number, and the engine should not default to it.
# Output: RAMPED <shift> <eps%> <T_c_MeV> <Neff> <YPCMB> <YPBBN> <DoHx1e5> <He3oHx1e5> <Li7oHx1e10>
_PRYM = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools", "PRyMordial")
os.chdir(_PRYM)
sys.path.insert(0, _PRYM)

shift  = float(sys.argv[1])          # 1 + eps
Tc_MeV = float(sys.argv[2]) if len(sys.argv) > 2 else 0.179   # DERIVED confining chiral T_c
wb_scale = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0    # eta-flow: omega_b scaling

import PRyM.PRyM_init as pri
pri.me = 0.51099895                  # STANDARD at import (thermo + HT rates standard)
try:                                 # numba only accelerates PRyM_thermo integrals; if the
    import numba                     # env's numpy is ahead of numba, fall back to pure numpy
except Exception:                    # (same results, slower) rather than failing to run
    pri.numba_flag = False
if wb_scale != 1.0:                  # the eta-flow, applied before anything derives from it
    pri.Omegabh2 = pri.Omegabh2*wb_scale
    pri.eta0b    = pri.Omegabh2_to_eta0b*pri.Omegabh2
for f in ['compute_nTOp_flag','compute_pTOn_flag']:
    if hasattr(pri, f): setattr(pri, f, True)
if hasattr(pri,'verbose_flag'): pri.verbose_flag = False
import numpy as np
import PRyM.PRyM_nTOp as nTOp_mod

Tc_K = Tc_MeV * pri.MeV_to_Kelvin    # the grids are in Kelvin

def ramped(Tvec):
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
    # tuples: T_HT,f_HT,b_HT, T_MT,f_MT,b_MT, T_LT,f_LT,b_LT
    def blend(T, s, f):
        w = np.clip(1.0 - np.asarray(T)/Tc_K, 0.0, 1.0)   # THE RAMP, pointwise
        return np.asarray(s) + (np.asarray(f) - np.asarray(s))*w
    T_HT, T_MT, T_LT = std[0], std[3], std[6]
    fHT, bHT = blend(T_HT, std[1], shf[1]), blend(T_HT, std[2], shf[2])
    fMT, bMT = blend(T_MT, std[4], shf[4]), blend(T_MT, std[5], shf[5])
    fLT, bLT = blend(T_LT, std[7], shf[7]), blend(T_LT, std[8], shf[8])
    mk = lambda x,y: interp1d(x,y,bounds_error=False,fill_value="extrapolate",kind='quadratic')
    return [mk(T_HT,fHT),mk(T_HT,bHT),mk(T_MT,fMT),mk(T_MT,bMT),mk(T_LT,fLT),mk(T_LT,bLT)]

nTOp_mod.RecomputeWeakRates = ramped
import PRyM.PRyM_main as prm
r = prm.PRyMclass().PRyMresults()
print("RAMPED %.6f %.4f %.4f wb=%.4f %.6f %.6f %.6f %.6f %.6f %.6f" %
      (shift, (shift-1.0)*100, Tc_MeV, wb_scale, r[0], r[3], r[4], r[5], r[6], r[7]), flush=True)
