import sys, os, re, subprocess, shutil

# THE DEUTERIUM-ONLY LEVER — does an expansion boost confined BELOW T_c heal D/H
# without costing Y_p?
#
# WHY THIS IS THE RIGHT QUESTION. Helium is decided at n/p freeze-out (~800 keV);
# deuterium at the bottleneck (~70 keV); the dyad's T_c = 179 keV sits BETWEEN them.
# A constant dark-radiation residual acts at both epochs, which is why it cannot heal
# BBN (both rows rise, they need opposite moves). A component that switches on at T_c
# is absent when helium is set and present when deuterium is set -- so it is, by the
# model's own epoch structure, a deuterium-only lever. This measures its leverage.
#
# WHERE IT IS INSERTED. The dark sector couples to the SM gravitationally and nothing
# else, so the extra density belongs in the Friedmann equation ONLY -- not in the
# photon or neutrino temperature ODEs. PRyM's Hubble() is a closure inside
# PRyMclass.PRyMresults, so this script patches that one line in the vendored source,
# runs, and restores. tools/PRyMordial is untracked, so nothing is left modified.
#
#   usage: prym_below_Tc_boost.py            (runs the full grid)
# Output rows: MODE dNeff Tc_MeV Neff YpBBN DoHx1e5

HERE  = os.path.dirname(os.path.abspath(__file__))
PRYM  = os.path.join(os.path.dirname(HERE), "tools", "PRyMordial")
MAIN  = os.path.join(PRYM, "PRyM", "PRyM_main.py")

# read once at import (PRyM_main does not import os, and Hubble is called inside the ODE loop)
HEAD_ANCHOR = """import time
import numpy as np
"""
HEAD_PATCH = """import time
import os as _prtoe_os
import numpy as np
# --- PRTOE deuterium-only lever, read once ---
_PRTOE_DN   = float(_prtoe_os.environ.get('PRTOE_DNEFF', '0.0'))
_PRTOE_TC   = float(_prtoe_os.environ.get('PRTOE_TC_MEV', '0.179'))
_PRTOE_ALLT = _prtoe_os.environ.get('PRTOE_ALL_T', '0') == '1'
# --- end ---
"""
ANCHOR = """            rho_tot = rho_pl+rho_3nu
"""
PATCH = """            rho_tot = rho_pl+rho_3nu
            # --- PRTOE deuterium-only lever (gravitational insertion only) ---
            if _PRTOE_DN != 0.0 and (_PRTOE_ALLT or Tg < _PRTOE_TC):
                rho_tot += _PRTOE_DN*PRyMthermo.rho_nu(Tnumu)
            # --- end PRTOE insertion ---
"""

RUNNER = r'''
import os, sys
PRYM = sys.argv[1]
os.chdir(PRYM); sys.path.insert(0, PRYM)
import PRyM.PRyM_init as pri
pri.numba_flag = False          # numba/numpy pair is broken in this env; PRyM runs pure-python
if hasattr(pri,'verbose_flag'): pri.verbose_flag = False
import PRyM.PRyM_main as prm
r = prm.PRyMclass().PRyMresults()
# PRyMresults: [0]=Neff [3]=Yp(CMB) [4]=Yp(BBN) [5]=D/H x1e5 [6]=He3 [7]=Li7
print("RESULT %.6f %.6f %.6f" % (r[0], r[4], r[5]), flush=True)
'''

def run(dN, all_T=False, Tc=0.179):
    env = dict(os.environ, PRTOE_DNEFF=repr(dN), PRTOE_TC_MEV=repr(Tc),
               PRTOE_ALL_T='1' if all_T else '0')
    p = subprocess.run([sys.executable, "-c", RUNNER, PRYM],
                       capture_output=True, text=True, env=env)
    for line in p.stdout.splitlines():
        if line.startswith("RESULT"):
            _, neff, yp, doh = line.split()
            return float(neff), float(yp), float(doh)
    sys.stderr.write(p.stdout[-3000:] + "\n" + p.stderr[-3000:] + "\n")
    raise RuntimeError("PRyM run failed for dN=%s all_T=%s" % (dN, all_T))

src = open(MAIN).read()
if "PRTOE deuterium-only lever" in src:
    raise SystemExit("PRyM_main.py already patched -- restore it first")
for a in (HEAD_ANCHOR, ANCHOR):
    if src.count(a) != 1:
        raise SystemExit("anchor not unique in PRyM_main.py (found %d)" % src.count(a))
shutil.copy(MAIN, MAIN + ".prtoe_bak")
open(MAIN, "w").write(src.replace(HEAD_ANCHOR, HEAD_PATCH).replace(ANCHOR, PATCH))

try:
    print("# MODE dNeff Tc_MeV Neff YpBBN DoHx1e5", flush=True)
    base = run(0.0)
    print("BASELINE 0.000 -     %.5f %.6f %.5f" % base, flush=True)
    for dN in (0.06, 0.24, 0.42, 0.84):
        r = run(dN, all_T=False)
        print("BELOW_TC %.3f 0.179 %.5f %.6f %.5f" % ((dN,) + r), flush=True)
    for dN in (0.24, 0.42):
        r = run(dN, all_T=True)
        print("ALL_T    %.3f -     %.5f %.6f %.5f" % ((dN,) + r), flush=True)
finally:
    shutil.move(MAIN + ".prtoe_bak", MAIN)
    assert "PRTOE deuterium-only lever" not in open(MAIN).read()
    print("# PRyM_main.py restored", flush=True)
