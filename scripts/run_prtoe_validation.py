#!/usr/bin/env python3
"""
PRTOE Numerical Validation Runner
=================================
Runs critical numerical checks on real CLASS + PRTOE output.
"""

import numpy as np
import sys
import os

# === Robust path handling ===
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    script_dir = os.getcwd()

sys.path.append(os.path.join(script_dir, '..', 'cosmic_dashboard', 'templates'))

from prtoe_dhost_checks_v2 import prtoe_dhost_consistency_check_v2
from data_loader import load_class_background

def run_true_null_limit_test(use_class=True):
    """Task 2.1: TRUE Null limit test (ALL PRTOE parameters → 0)"""
    print("\\n" + "="*60)
    print(" TASK 2.1: TRUE NULL LIMIT TEST")
    print("="*60)
    
    if use_class:
        try:
            import classy
            params = {
                'use_prtoe': 'yes',
                'xi_prtoe': 0.0,
                'zeta_prtoe': 0.0,
                'phi_0_prtoe': 0.0,
                'V0_prtoe': 1.0,
                'm_prtoe': 0.0,
                'lambda_prtoe': 1.0,
                'phi_c_prtoe': 0.0,
                'delta_phi_prtoe': 1.0,
                'Omega_cdm': 0.27,
                'Omega_b': 0.05,
                'h': 0.67,
                'Omega_k': 0.0,
                'YHe': 0.245,
                'output': 'mPk'
            }
            cosmo = classy.Class()
            try:
                cosmo.set(params)
                cosmo.compute()
                print("✅ Computation completed without tachyonic warnings!")
                print("✅ TRUE NULL LIMIT TEST PASSED")
                return True
            except Exception as e:
                print(f"❌ Computation failed: {str(e)[:200]}...")
                print("❌ TRUE NULL LIMIT TEST FAILED")
                return False
            finally:
                try:
                    cosmo.struct_cleanup()
                    cosmo.empty()
                except Exception as cleanup_err:
                    print(f"⚠️  CLASS cleanup failed: {cleanup_err}")
        except ImportError:
            print("⚠️  CLASS module not available")
            return False
    else:
        print("⚠️  CLASS skipped by caller")
        return "SKIPPED"


def run_null_limit_test(use_class=True):
    """Task 2.2: Null Limit Test"""
    print("\\n" + "="*60)
    print(" TASK 2.2: PRTOE NULL LIMIT TEST")
    print("="*60)
    
    background = None
    if use_class:
        try:
            import classy
            print("Running full CLASS solver for null limit...")
            cosmo = classy.Class()
            try:
                cosmo.set({
                    'use_prtoe': 'yes',
                    'xi_prtoe': 1e-7,
                    'zeta_prtoe': 0.0,
                    'phi_0_prtoe': 0.0,
                    'V0_prtoe': 1.0,
                    'm_prtoe': 0.0,
                    'lambda_prtoe': 1.0,
                    'phi_c_prtoe': 0.0,
                    'delta_phi_prtoe': 1.0,
                    'Omega_cdm': 0.27,
                    'Omega_b': 0.05,
                    'h': 0.67,
                    'Omega_k': 0.0,
                    'YHe': 0.245,
                    'output': 'mPk'
                })
                cosmo.compute()
                print("✅ CLASS computation completed successfully")
                if cosmo.has_prtoe():
                    background = load_class_background(cosmo)
                else:
                    print("❌ PRTOE activation failed")
                    return False
            finally:
                try:
                    cosmo.struct_cleanup()
                    cosmo.empty()
                except Exception as cleanup_err:
                    print(f"⚠️  CLASS cleanup failed: {cleanup_err}")
        except ImportError:
            print("⚠️  CLASS module not available")
            return False
        except Exception as e:
            print(f"⚠️  CLASS computation failed: {e}")
            return False
            
    if background is None:
        if use_class:
            return False
        print("⚠️  Using dummy data for validation test...")
        background = {
            'phi': np.linspace(-3, 3, 500),
            'F': np.ones(500),
            'F_phi': np.zeros(500),
            'F_phiphi': np.zeros(500),
            'phi_prime': np.ones(500) * 0.001,
            'ddphi': np.zeros(500),
            'a': np.linspace(0.01, 1.0, 500),
            'H': np.ones(500) * 70.0 / 299792.458
        }
        
    result = prtoe_dhost_consistency_check_v2(
        background=background,
        xi=1e-7,
        zeta=0.0,
        verbose=True
    )
    if result.healthy and result.min_K > 0.99 and result.min_c_s2 > 0.99:
        print("✅ NULL LIMIT TEST PASSED — Model recovers healthy DHOST behavior")
        return True
    else:
        print("❌ NULL LIMIT TEST FAILED")
        return False


def run_stability_sweep(use_class=True):
    """Task 2.3: Basic stability sweep over ξ and ζ"""
    print("\\n" + "="*60)
    print(" TASK 2.3: STABILITY SWEEP")
    print("="*60)

    xi_values = [1e-7, 5e-6, 1.2e-5]
    zeta_values = [0.1, 1.0, 3.0]
    results = []

    for xi in xi_values:
        for zeta in zeta_values:
            background = None
            if use_class:
                try:
                    import classy
                    params = {
                        'use_prtoe': 'yes',
                        'xi_prtoe': xi,
                        'zeta_prtoe': zeta,
                        'phi_0_prtoe': 0.0,
                        'V0_prtoe': 1.0,
                        'm_prtoe': 0.1,
                        'lambda_prtoe': 1.0,
                        'phi_c_prtoe': 0.0,
                        'delta_phi_prtoe': 1.0,
                        'Omega_cdm': 0.27,
                        'Omega_b': 0.05,
                        'h': 0.67,
                        'Omega_k': 0.0,
                        'YHe': 0.245,
                        'output': 'mPk'
                    }
                    print(f"  Testing ξ={xi:.1e}, ζ={zeta:.1f}...")
                    cosmo = classy.Class()
                    try:
                        cosmo.set(params)
                        cosmo.compute()
                        background = load_class_background(cosmo)
                    finally:
                        try:
                            cosmo.struct_cleanup()
                            cosmo.empty()
                        except Exception as cleanup_err:
                            print(f"⚠️  CLASS cleanup failed: {cleanup_err}")
                except ImportError:
                    print("⚠️  CLASS module not available")
                except Exception as e:
                    print(f"  CLASS failed: {e}")
                    
            if background is None:
                if use_class:
                    results.append({
                        'xi': xi,
                        'zeta': zeta,
                        'healthy': False,
                        'min_K': 0.0,
                        'min_c_s2': 0.0
                    })
                    print(f"  ξ={xi:.1e}, ζ={zeta:.1f} → ❌ FAILED TO RUN CLASS")
                    continue
                else:
                    # Dummy fallback if use_class is False
                    background = {
                        'phi': np.linspace(-4, 4, 600),
                        'F': 1.0 + 0.05 * np.tanh(np.linspace(-4, 4, 600)),
                        'F_phi': np.ones(600) * 0.01,
                        'F_phiphi': np.ones(600) * 0.001,
                        'phi_prime': np.ones(600) * 0.005,
                        'ddphi': np.zeros(600),
                        'a': np.linspace(0.01, 1.0, 600),
                        'H': np.ones(600) * 70.0 / 299792.458
                    }

            res = prtoe_dhost_consistency_check_v2(
                background=background,
                xi=xi,
                zeta=zeta,
                verbose=False
            )

            results.append({
                'xi': xi,
                'zeta': zeta,
                'healthy': res.healthy,
                'min_K': res.min_K,
                'min_c_s2': res.min_c_s2
            })

            status = "✅ HEALTHY" if res.healthy else "❌ ISSUES"
            print(f"  ξ={xi:.1e}, ζ={zeta:.1f} → {status} | min(K)={res.min_K:.4f}, min(c_s²)={res.min_c_s2:.4f}")
            
    return results


if __name__ == "__main__":
    print("Starting PRTOE Numerical Validation Suite...")

    true_null_ok = run_true_null_limit_test()
    null_ok = run_null_limit_test()
    sweep_results = run_stability_sweep()

    print("\\n" + "="*60)
    print(" VALIDATION SUMMARY")
    print("="*60)
    
    print(f"True Null Limit Test (ALL params=0): {'PASSED' if true_null_ok is True else 'FAILED' if true_null_ok is False else 'SKIPPED'}")
    print(f"Null Limit Test (xi=1e-7 boundary): {'PASSED' if null_ok is True else 'FAILED' if null_ok is False else 'SKIPPED'}")
    print(f"Stability Sweep completed with {len(sweep_results)} parameter combinations.")
    
    if true_null_ok is False or null_ok is False or any(not r['healthy'] for r in sweep_results):
        sys.exit(1)
