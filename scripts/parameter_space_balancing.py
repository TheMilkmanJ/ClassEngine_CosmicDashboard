import numpy as np
import matplotlib.pyplot as plt
import os

def run_parameter_balancing():
    # Setup professional astrophysics design (Dark Theme)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Inter', 'DejaVu Sans', 'Arial']

    # Standard constants
    c_std = 299792458.0          # m/s
    hbar_std = 1.0545718e-34     # J s
    
    # Under G_eff = G_std * 10^38, we require:
    # hbar_eff / c_eff^3 = (hbar_std / c_std^3) * 10^-38
    
    # We define a grid of relative Planck's constant scaling: hbar_eff / hbar_std
    # from 10^-38 (Option B) to 1.0 (Option A)
    hbar_scale = np.logspace(-38, 0, 100)
    
    # Calculate corresponding required speed of light scaling: c_eff / c_std
    # c_scale^3 = hbar_scale * 10^38  => c_scale = (hbar_scale * 10^38)^(1/3)
    c_scale = (hbar_scale * 1e38)**(1.0 / 3.0)
    
    ax.loglog(hbar_scale, c_scale, color='#39ff14', lw=3.5, label='Required Balancing Profile')
    
    # Mark Option A (c_scale maximum, hbar_scale = 1)
    ax.scatter([1.0], [c_scale[-1]], color='#00d2ff', s=100, zorder=5, label='Option A: Faster Light (c_eff ~ 4.6e12 c_std)')
    
    # Mark Option B (hbar_scale minimum, c_scale = 1)
    ax.scatter([1e-38], [1.0], color='#ff007f', s=100, zorder=5, label='Option B: Smaller Planck (hbar_eff ~ 10^-38 hbar_std)')
    
    ax.set_title('Physical Constant Balancing under subatomic Strong Gravity', fontsize=14, pad=15)
    ax.set_xlabel(r'Planck Constant Scaling Factor ($\hbar_{\mathrm{eff}} / \hbar_{\mathrm{std}}$)', fontsize=12)
    ax.set_ylabel(r'Speed of Light Scaling Factor ($c_{\mathrm{eff}} / c_{\mathrm{std}}$)', fontsize=12)
    ax.grid(True, which="both", linestyle='--', alpha=0.3)
    ax.legend(frameon=True, facecolor='#111111', edgecolor='#333333', fontsize=10)
    
    plt.tight_layout()
    os.makedirs('output', exist_ok=True)
    plt.savefig('output/parameter_balancing.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("=== PARAMETER SPACE BALANCING COMPLETE ===")
    print(f"Option A: c_eff = {c_scale[-1] * c_std:.6e} m/s (c_eff/c_std = {c_scale[-1]:.6e})")
    print(f"Option B: hbar_eff = {1e-38 * hbar_std:.6e} J s (hbar_eff/hbar_std = 1.000000e-38)")

if __name__ == '__main__':
    run_parameter_balancing()
