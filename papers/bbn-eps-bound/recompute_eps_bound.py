#!/usr/bin/env python3
"""External recompute of the Aver 2σ ε bound at T_c = 179 keV.

No framework required. Numbers match papers/bbn-eps-bound/README.md and main.tex.

Usage:
  python3 recompute_eps_bound.py

Expected: ε_2σ ≈ 3.20% (PASS if |ε_2σ − 3.20| < 0.05).
"""
from __future__ import annotations

# Stated inputs (paper / README)
Yp0 = 0.246891  # PRyM baseline ε=0
dYp_deps = 0.00163  # per %ε (paper)
Aver_Yp = 0.2453
Aver_sig = 0.0034

eps_1sig = (Aver_Yp + 1 * Aver_sig - Yp0) / dYp_deps
eps_2sig = (Aver_Yp + 2 * Aver_sig - Yp0) / dYp_deps
emp_pull = (Yp0 - 0.2370) / 0.0034  # EMPRESS non-result

print("BBN ε bound recompute (Aver et al. 2021; T_c = 179 keV)")
print(f"  Y_p0 (ε=0)           = {Yp0}")
print(f"  dY_p/dε              = {dYp_deps} per %ε")
print(f"  Aver Y_p             = {Aver_Yp} ± {Aver_sig}")
print(f"  ε 1σ ceiling         = {eps_1sig:.3f}%")
print(f"  ε 2σ ceiling         = {eps_2sig:.3f}%")
print(f"  paper claim 2σ       = 3.20%")
print(f"  match                = {'PASS' if abs(eps_2sig - 3.20) < 0.05 else 'FAIL'}")
print(f"  EMPRESS pull at ε=0  = {emp_pull:+.2f}σ (cannot bound ε)")
