#!/usr/bin/env python3
"""Distinctive-prediction hunt: scan xi across the DHOST stability wedge and
measure how far PRTOE observables deviate from LCDM, compared against the
precision of current/next-gen surveys.

Observables:
  - f*sigma8(z)  at z = 0, 0.5, 1.0, 1.5      (DESI full-shape: ~1% aggregate)
  - P(k, z=0)    at k = 0.01..0.5 h/Mpc        (scale-dependent growth signature)
  - C_l^TT/EE    l = 2..500                    (Planck: ~0.2-0.5% per-bin at high l)

Run: python scripts/forecast_scan.py  (from repo root; uses the installed classy)
"""
import json
import sys
import numpy as np
from classy import Class

XI_GRID = [1e-7, 5e-7, 1e-6, 3e-6, 6e-6, 1.2e-5]
Z_FS8 = [0.0, 0.5, 1.0, 1.5]
KVEC = np.logspace(-2, np.log10(0.5), 12)          # h/Mpc
LMAX = 500

BASE = {
    'h': 0.7, 'Omega_b': 0.05, 'Omega_cdm': 0.25, 'Omega_k': 0,
    'A_s': 2.1e-9, 'n_s': 0.965, 'z_reio': 8.0,
    'output': 'tCl,pCl,lCl,mPk', 'lensing': 'yes',
    'P_k_max_h/Mpc': 1.0, 'z_max_pk': 2.0, 'l_max_scalars': LMAX,
}

SURVEY_PRECISION = {   # rough 1-sigma fractional sensitivities
    'fsigma8': 0.01,       # DESI full-shape aggregate
    'pk': 0.01,            # BOSS/DESI broadband
    'cl': 0.003,           # Planck high-l per-bin
}


def run_model(extra):
    c = Class()
    c.set({**BASE, **extra})
    c.compute()
    out = {}
    out['fsigma8'] = [c.effective_f_sigma8(z) for z in Z_FS8]
    h = c.h()
    out['pk'] = [c.pk(k * h, 0.0) for k in KVEC]   # classy wants k in 1/Mpc
    cl = c.lensed_cl(LMAX)
    out['tt'] = cl['tt'][2:].tolist()
    out['ee'] = cl['ee'][2:].tolist()
    out['sigma8'] = c.sigma8()
    c.struct_cleanup(); c.empty()
    return out


def frac_dev(a, b):
    a, b = np.asarray(a), np.asarray(b)
    denom = np.where(np.abs(b) > 0, np.abs(b), 1e-300)
    return np.abs(a - b) / denom


def main():
    print("[scan] LCDM reference...", flush=True)
    lcdm = run_model({'Omega_Lambda': 0.7})

    results = {}
    for xi in XI_GRID:
        tag = f"xi={xi:.1e}"
        print(f"[scan] PRTOE {tag} ...", flush=True)
        try:
            m = run_model({
                'use_prtoe': 'yes', 'xi_prtoe': xi, 'Omega0_prtoe': 0.7,
                'Omega_Lambda': 0.0,
            })
        except Exception as e:
            print(f"[scan]   FAILED: {e}", flush=True)
            results[tag] = {'error': str(e)}
            continue

        d_fs8 = frac_dev(m['fsigma8'], lcdm['fsigma8'])
        d_pk = frac_dev(m['pk'], lcdm['pk'])
        d_tt = frac_dev(m['tt'], lcdm['tt'])
        d_ee = frac_dev(m['ee'], lcdm['ee'])
        res = {
            'fsigma8_dev': d_fs8.tolist(),
            'fsigma8_max': float(d_fs8.max()),
            'pk_dev_by_k': dict(zip([f"{k:.3f}" for k in KVEC], d_pk.tolist())),
            'pk_max': float(d_pk.max()),
            'pk_scale_dependence': float(d_pk.max() - d_pk.min()),
            'tt_max': float(d_tt.max()),
            'tt_argmax_l': int(np.argmax(d_tt) + 2),
            'ee_max': float(d_ee.max()),
            'sigma8_dev': float(abs(m['sigma8'] - lcdm['sigma8']) / lcdm['sigma8']),
            'snr': {
                'fsigma8': float(d_fs8.max() / SURVEY_PRECISION['fsigma8']),
                'pk': float(d_pk.max() / SURVEY_PRECISION['pk']),
                'cl_tt': float(d_tt.max() / SURVEY_PRECISION['cl']),
            },
        }
        results[tag] = res
        print(f"[scan]   fs8_max={res['fsigma8_max']:.2e}  pk_max={res['pk_max']:.2e} "
              f"(scale-dep {res['pk_scale_dependence']:.2e})  "
              f"TT_max={res['tt_max']:.2e}@l={res['tt_argmax_l']}  "
              f"SNR(fs8)={res['snr']['fsigma8']:.2f} SNR(pk)={res['snr']['pk']:.2f} "
              f"SNR(TT)={res['snr']['cl_tt']:.2f}", flush=True)

    with open('chains/forecast_scan_results.json', 'w') as f:
        json.dump({'lcdm_sigma8': lcdm['sigma8'], 'results': results}, f, indent=1)
    print("[scan] written chains/forecast_scan_results.json", flush=True)

    detectable = {t: r for t, r in results.items()
                  if 'snr' in r and max(r['snr'].values()) >= 1.0}
    if detectable:
        print("[scan] DETECTABLE at >=1 sigma:", ", ".join(detectable))
    else:
        print("[scan] No point in the wedge exceeds survey precision — "
              "constraint-paper territory.")


if __name__ == '__main__':
    main()
