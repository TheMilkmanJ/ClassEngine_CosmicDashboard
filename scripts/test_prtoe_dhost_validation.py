#!/usr/bin/env python3
"""
Test Script for PRTOE DHOST Validation Module
==============================================

This script demonstrates how to use prtoe_dhost_checks_v2.py to validate
PRTOE runs against DHOST consistency conditions.

Usage:
    python test_prtoe_dhost_validation.py

Requirements:
    - numpy
    - matplotlib
    - prtoe_dhost_checks_v2.py module
"""

import sys
import os
import numpy as np

# Add cosmic_dashboard/templates to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'cosmic_dashboard', 'templates'))

try:
    from prtoe_dhost_checks_v2 import prtoe_dhost_consistency_check_v2, plot_dhost_diagnostics
    print("✓ Successfully imported prtoe_dhost_checks_v2")
except ImportError as e:
    print(f"✗ Failed to import prtoe_dhost_checks_v2: {e}")
    print("  Please ensure the file is in cosmic_dashboard/templates/")
    sys.exit(1)


def create_test_background():
    """Create a realistic test background for PRTOE with default parameters."""
    # Create a realistic cosmological evolution
    n_points = 1000
    a = np.linspace(0.01, 1.0, n_points)  # scale factor
    
    # PRTOE parameters (typical values)
    xi = 0.05
    zeta = 2.0
    phi_c = 0.1
    V0 = 0.01
    lambda_prtoe = 1.0
    m = 0.1
    
    # Background scalar field (simplified evolution)
    phi = phi_c * np.tanh(5.0 * (np.log(a) + 10.0))  # Transition around a ~ e^-10
    phi_prime = phi_c * 5.0 * (1.0 - np.tanh(5.0 * (np.log(a) + 10.0))**2) / a
    ddphi = np.zeros_like(a)  # Simplified
    
    # Compute F and its derivatives
    A_phi = 0.5 * (1.0 + np.tanh((phi - phi_c) / 0.1))
    S_phi = phi**2 / (1.0 + zeta * phi**2)
    F = 1.0 + xi * A_phi * S_phi
    F_phi = xi * (0.5 * (1.0 - np.tanh((phi - phi_c) / 0.1)**2) / 0.1 * S_phi + A_phi * 2.0 * phi / (1.0 + zeta * phi**2)**2)
    F_phiphi = xi * np.ones_like(phi)  # Simplified
    
    return {
        'a': a,
        'phi': phi,
        'phi_prime': phi_prime,
        'ddphi': ddphi,
        'F': F,
        'F_phi': F_phi,
        'F_phiphi': F_phiphi,
        'H': np.ones_like(a) * 70.0 * np.sqrt(0.3 / a**3 + 0.7),  # Simplified H(a)
    }


def test_basic_functionality():
    """Test basic functionality of the validation module."""
    print("\n" + "="*60)
    print("TEST 1: Basic Functionality")
    print("="*60)
    
    background = create_test_background()
    
    result = prtoe_dhost_consistency_check_v2(
        background=background,
        xi=0.05,
        zeta=2.0,
        phi_c=0.1,
        verbose=True
    )
    
    print(f"\nResult Summary:")
    print(f"  Healthy: {result.healthy}")
    print(f"  No Ghost: {result.no_ghost}")
    print(f"  Gradient Stable: {result.gradient_stable}")
    print(f"  Tensor Speed OK: {result.tensor_speed_ok}")
    
    return result


def test_parameter_sweep():
    """Test parameter sweep over xi and zeta."""
    print("\n" + "="*60)
    print("TEST 2: Parameter Sweep")
    print("="*60)
    
    xi_values = [0.01, 0.05, 0.1, 0.5]
    zeta_values = [1.0, 2.0, 5.0]
    
    background = create_test_background()
    
    for xi in xi_values:
        for zeta in zeta_values:
            result = prtoe_dhost_consistency_check_v2(
                background=background,
                xi=xi,
                zeta=zeta,
                verbose=False
            )
            status = "✓" if result.healthy else "✗"
            print(f"  xi={xi:.2f}, zeta={zeta:.1f}: {status} (K_min={result.min_K:.4f}, c_s²_min={result.min_c_s2:.4f})")


def test_violation_cases():
    """Test cases that should trigger violations."""
    print("\n" + "="*60)
    print("TEST 3: Violation Cases (Expected to Fail)")
    print("="*60)
    
    # Case 1: Negative F (should trigger ghost)
    background_bad_F = create_test_background()
    background_bad_F['F'] = -0.5 * np.ones_like(background_bad_F['F'])
    
    result = prtoe_dhost_consistency_check_v2(
        background=background_bad_F,
        xi=0.05,
        zeta=2.0,
        verbose=True
    )
    print(f"  Negative F case - Healthy: {result.healthy} (Expected: False)")
    
    # Case 2: Large F_phi (should trigger gradient instability)
    background_bad_G = create_test_background()
    background_bad_G['F_phi'] = 100.0 * np.ones_like(background_bad_G['F_phi'])
    
    result = prtoe_dhost_consistency_check_v2(
        background=background_bad_G,
        xi=0.05,
        zeta=2.0,
        verbose=True
    )
    print(f"  Large F_phi case - Healthy: {result.healthy} (Expected: False)")


def test_plotting():
    """Test the plotting functionality."""
    print("\n" + "="*60)
    print("TEST 4: Plotting Functionality")
    print("="*60)
    
    background = create_test_background()
    result = prtoe_dhost_consistency_check_v2(
        background=background,
        xi=0.05,
        zeta=2.0,
        verbose=False
    )
    
    try:
        plot_dhost_diagnostics(result, save_path=None)
        print("  ✓ Plotting completed successfully")
    except Exception as e:
        print(f"  ✗ Plotting failed: {e}")


def main():
    """Run all tests."""
    print("\n" + "="*60)
    print("PRTOE DHOST Validation Module Test Suite")
    print("="*60)
    
    # Run all tests
    test_basic_functionality()
    test_parameter_sweep()
    test_violation_cases()
    test_plotting()
    
    print("\n" + "="*60)
    print("All tests completed!")
    print("="*60)
    print("\nNext steps:")
    print("1. Integrate this module into your CosmicDashboard workflow")
    print("2. Replace the test background with actual CLASS output")
    print("3. Run on your PRTOE parameter scans")
    print("\nExample integration:")
    print("  from prtoe_dhost_checks_v2 import prtoe_dhost_consistency_check_v2")
    print("  result = prtoe_dhost_consistency_check_v2(background_dict, xi, zeta)")
    print("  if not result.healthy:")
    print("      print(result.warnings)")


if __name__ == "__main__":
    main()
