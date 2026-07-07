#!/usr/bin/env python3
"""
dCDF Pre-PolyChord Validation Suite
Runs all Tier 1 (blocking) and Tier 2 (sanity) tests before MCMC submission.
"""
import numpy as np
import time
from classy import Class

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"
WARN = "\033[93mWARN\033[0m"

results = {}

def make_dcdf(extra={}):
    c = Class()
    params = {
        'use_dcdf': 'yes',
        'dcdf_rho_inf': 0.7,
        'dcdf_beta': 1e-7,
        'xi_Neff': 0.2,
        'omega_b': 0.0224,
        'Omega_cdm': 0.0,
        'Omega_Lambda': 0.0,
        'Omega0_dcdf': 1.0 - 0.0224 / (0.674**2),
        'H0': 67.4,
        'A_s': 2.1e-9,
        'n_s': 0.965,
        'output': 'tCl,lCl,mPk',
        'P_k_max_1/Mpc': 1.0,
        'z_max_pk': 0.0,
        'l_max_scalars': 2500,
        'lensing': 'yes',
    }
    params.update(extra)
    c.set(params)
    return c

def make_lcdm():
    c = Class()
    c.set({
        'omega_b': 0.0224,
        'omega_cdm': 0.12,
        'H0': 67.4,
        'A_s': 2.1e-9,
        'n_s': 0.965,
        'output': 'tCl,lCl,mPk',
        'P_k_max_1/Mpc': 1.0,
        'z_max_pk': 0.0,
        'l_max_scalars': 2500,
        'lensing': 'yes',
    })
    return c

# ─────────────────────────────────────────────────────────
# TIER 1 TEST 1: Null Limit (beta -> 0 should recover LCDM-like)
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("TIER 1 TEST 1: NULL LIMIT (beta=0)")
print("="*60)
try:
    lcdm = make_lcdm()
    lcdm.compute()
    s8_lcdm = lcdm.sigma8()
    pk_lcdm = lcdm.pk(0.1, 0.0)
    cl_lcdm = lcdm.raw_cl(2500)['tt']

    # beta=0: w = -exp(-s), cs2 = 0 => behaves as pressureless cold fluid at early times
    # Use tiny beta to approach limit
    null = make_dcdf({'dcdf_beta': 1e-12})
    null.compute()
    s8_null = null.sigma8()
    pk_null = null.pk(0.1, 0.0)
    cl_null = null.raw_cl(2500)['tt']

    ds8 = abs(s8_null - s8_lcdm) / s8_lcdm
    dpk = abs(pk_null - pk_lcdm) / pk_lcdm
    # compare TT spectrum at l=200 (first peak)
    dcl = abs(cl_null[200] - cl_lcdm[200]) / cl_lcdm[200]

    print(f"  sigma8 LCDM: {s8_lcdm:.4f}   Null: {s8_null:.4f}   Frac diff: {ds8:.3e}")
    print(f"  P(k=0.1) LCDM: {pk_lcdm:.3e}   Null: {pk_null:.3e}   Frac diff: {dpk:.3e}")
    print(f"  C_l(TT,l=200) Frac diff: {dcl:.3e}")

    # dCDF is fundamentally different from LCDM in background even at beta=0,
    # so we expect O(few%) differences. The key test is it's NOT wildly wrong.
    if ds8 < 0.10 and dpk < 0.10:
        status = PASS
        results['null_limit'] = 'PASS'
        print(f"  Result: {PASS} — dCDF with beta~0 produces physically reasonable clustering")
    else:
        status = FAIL
        results['null_limit'] = 'FAIL'
        print(f"  Result: {FAIL} — dCDF null limit diverges too far from LCDM")
except Exception as e:
    print(f"  Result: {FAIL} — Exception: {e}")
    results['null_limit'] = f'FAIL: {e}'

# ─────────────────────────────────────────────────────────
# TIER 1 TEST 2: Timing Benchmark
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("TIER 1 TEST 2: TIMING BENCHMARK")
print("="*60)
try:
    # Full CMB+lensing+P(k) computation, similar to what cobaya calls
    times = []
    for i in range(3):
        c = make_dcdf()
        t0 = time.time()
        c.compute()
        t1 = time.time()
        times.append(t1 - t0)
        c.struct_cleanup()

    mean_t = np.mean(times)
    polychord_evals = 500 * 30  # nlive * num_repeats
    total_hours = mean_t * polychord_evals / 3600

    print(f"  Single CLASS call: {mean_t:.2f}s  (min={min(times):.2f}s, max={max(times):.2f}s)")
    print(f"  PolyChord estimate: {polychord_evals} evals × {mean_t:.1f}s = {total_hours:.1f} CPU-hours")

    if mean_t < 10:
        results['timing'] = f'PASS ({mean_t:.1f}s/eval, ~{total_hours:.0f} CPU-hrs for PolyChord)'
        print(f"  Result: {PASS}")
    elif mean_t < 30:
        results['timing'] = f'WARN ({mean_t:.1f}s/eval, ~{total_hours:.0f} CPU-hrs — slow but feasible)'
        print(f"  Result: {WARN} — Slow. Consider reducing l_max or using evaluate sampler first.")
    else:
        results['timing'] = f'FAIL ({mean_t:.1f}s/eval — too slow for PolyChord)'
        print(f"  Result: {FAIL} — Too slow for PolyChord run.")
except Exception as e:
    print(f"  Result: {FAIL} — Exception: {e}")
    results['timing'] = f'FAIL: {e}'

# ─────────────────────────────────────────────────────────
# TIER 1 TEST 3: Parameter Boundary Robustness
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("TIER 1 TEST 3: PARAMETER BOUNDARY SWEEP")
print("="*60)
test_points = [
    ('rho_inf=0.01 (min)', {'dcdf_rho_inf': 0.01}),
    ('rho_inf=0.95 (max)', {'dcdf_rho_inf': 0.95}),
    ('beta=1e-10 (tiny)',  {'dcdf_beta': 1e-10}),
    ('beta=0.5 (large)',   {'dcdf_beta': 0.5}),
    ('xi_Neff=0.0 (min)',  {'xi_Neff': 0.0}),
    ('xi_Neff=1.0 (max)',  {'xi_Neff': 1.0}),
]

boundary_results = []
for label, extra in test_points:
    try:
        c = make_dcdf(extra)
        c.compute()
        s8 = c.sigma8()
        c.struct_cleanup()
        ok = 0.0 < s8 < 2.0
        boundary_results.append(ok)
        status = PASS if ok else FAIL
        print(f"  {label:30s}: sigma8={s8:.4f}  {status}")
    except Exception as e:
        boundary_results.append(False)
        print(f"  {label:30s}: {FAIL} — {str(e)[:80]}")

if all(boundary_results):
    results['boundary'] = 'PASS'
    print(f"  Result: {PASS} — All boundary points stable")
else:
    n_fail = sum(1 for x in boundary_results if not x)
    results['boundary'] = f'FAIL ({n_fail}/{len(boundary_results)} boundary points crashed)'
    print(f"  Result: {FAIL} — {n_fail} boundary points unstable")

# ─────────────────────────────────────────────────────────
# TIER 2 TEST 4: BAO Feature Intact
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("TIER 2 TEST 4: BAO FEATURE")
print("="*60)
try:
    c = make_dcdf({'output': 'mPk', 'z_max_pk': 0.0,
                   'z_pk': '0.38 0.51 0.61', 'P_k_max_1/Mpc': 0.5})
    c.compute()

    # Check sound horizon (BAO scale)
    bg = c.get_background()
    rs_drag = c.rs_drag()

    print(f"  Sound horizon at drag epoch: {rs_drag:.2f} Mpc")
    if 140 < rs_drag < 160:
        print(f"  Result: {PASS} — BAO scale {rs_drag:.1f} Mpc is within expected 140-160 Mpc")
        results['bao'] = f'PASS (rs_drag={rs_drag:.2f} Mpc)'
    else:
        print(f"  Result: {FAIL} — BAO scale {rs_drag:.1f} Mpc is outside expected range!")
        results['bao'] = f'FAIL (rs_drag={rs_drag:.2f} Mpc, expected 140-160)'
    c.struct_cleanup()
except Exception as e:
    print(f"  Result: {FAIL} — Exception: {e}")
    results['bao'] = f'FAIL: {e}'

# ─────────────────────────────────────────────────────────
# TIER 2 TEST 5: CMB Peaks in Right Position
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("TIER 2 TEST 5: CMB ACOUSTIC PEAKS")
print("="*60)
try:
    c = make_dcdf()
    c.compute()
    cl = c.raw_cl(2500)['tt']
    ls = np.arange(len(cl))

    # Find first peak in l*(l+1)Cl around l=200
    window = cl[100:400] * ls[100:400] * (ls[100:400]+1)
    l1_dcdf = ls[100:400][np.argmax(window)]

    lcdm = make_lcdm()
    lcdm.compute()
    cl_l = lcdm.raw_cl(2500)['tt']
    window_l = cl_l[100:400] * ls[100:400] * (ls[100:400]+1)
    l1_lcdm = ls[100:400][np.argmax(window_l)]

    shift = abs(l1_dcdf - l1_lcdm)
    print(f"  First CMB peak: dCDF l={l1_dcdf}, LCDM l={l1_lcdm}, shift={shift}")
    if shift <= 10:
        print(f"  Result: {PASS} — First acoustic peak matches LCDM position to within Δl={shift}")
        results['cmb_peaks'] = f'PASS (l1_dcdf={l1_dcdf}, Δl={shift})'
    else:
        print(f"  Result: {FAIL} — First acoustic peak shifted by Δl={shift} (>10 is pathological)")
        results['cmb_peaks'] = f'FAIL (Δl={shift})'
    c.struct_cleanup()
    lcdm.struct_cleanup()
except Exception as e:
    print(f"  Result: {FAIL} — Exception: {e}")
    results['cmb_peaks'] = f'FAIL: {e}'

# ─────────────────────────────────────────────────────────
# TIER 2 TEST 6: Growth Rate f*sigma8 at RSD Redshifts
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("TIER 2 TEST 6: GROWTH RATE f*sigma8")
print("="*60)
try:
    c = make_dcdf({'z_pk': '0.38 0.51 0.61', 'z_max_pk': 1.0})
    c.compute()
    bg = c.get_background()

    # Get f = dlnD/dlna from background
    z_bg = bg['z']
    f_bg = bg['gr.fac. f']
    sigma8_z = []
    f_vals = []
    for z_target in [0.38, 0.51, 0.61]:
        idx = np.argmin(np.abs(z_bg - z_target))
        f = f_bg[idx]
        s8z = c.sigma(8.0, z_target)
        fsig8 = f * s8z
        sigma8_z.append(fsig8)
        f_vals.append(f)
        print(f"  z={z_target}: f={f:.3f}, sigma8(z)={s8z:.4f}, f*sigma8={fsig8:.4f}")

    # BOSS RSD measurements (Alam+2017)
    boss_fsig8 = {0.38: 0.497, 0.51: 0.458, 0.61: 0.436}
    all_ok = True
    for z_target, fsig8 in zip([0.38, 0.51, 0.61], sigma8_z):
        obs = boss_fsig8[z_target]
        frac = abs(fsig8 - obs) / obs
        ok = frac < 0.20   # within 20% of BOSS measurement
        all_ok = all_ok and ok
        print(f"    vs BOSS: {obs:.3f}  frac diff: {frac:.2f}  {'OK' if ok else 'LARGE'}")

    if all_ok:
        print(f"  Result: {PASS} — f*sigma8 within 20% of BOSS RSD at all 3 redshifts")
        results['fsigma8'] = 'PASS'
    else:
        print(f"  Result: {WARN} — f*sigma8 deviates >20% from BOSS (not fatal, PolyChord will handle)")
        results['fsigma8'] = 'WARN'
    c.struct_cleanup()
except Exception as e:
    print(f"  Result: {FAIL} — Exception: {e}")
    results['fsigma8'] = f'FAIL: {e}'

# ─────────────────────────────────────────────────────────
# FINAL SUMMARY
# ─────────────────────────────────────────────────────────
print("\n" + "="*60)
print("VALIDATION SUMMARY")
print("="*60)
blocking_pass = True
for test, result in results.items():
    tier = "T1" if test in ('null_limit', 'timing', 'boundary') else "T2"
    status_char = "✓" if result.startswith('PASS') else ("⚠" if result.startswith('WARN') else "✗")
    print(f"  [{tier}] {status_char} {test:15s}: {result}")
    if tier == "T1" and not result.startswith('PASS'):
        blocking_pass = False

print()
if blocking_pass:
    print("  ✓ ALL TIER 1 TESTS PASS — Ready to submit to PolyChord!")
else:
    print("  ✗ TIER 1 FAILURES DETECTED — Fix before running PolyChord!")
print("="*60)
