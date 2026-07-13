#!/usr/bin/env python3
"""Card 6: the seesaw duty scan — what v_L do the joint duties FORCE?

Inverse-seesaw / Majoron assembly (the model's recorded structure):
  light mass:      m3 = mu * (y*v/sqrt(2))^2 / M^2        (mu << M regime)
  heavy width:     Gamma_N = y^2 * M / (8*pi)
  resonance duty:  mu / Gamma_N ~ O(1)                     (Card 4's eta route)
  Majoron:         g = m3 / v_L ; CMB-S4 reaches v_L < ~20 MeV (P-2026-025 band)
  spurion source:  mu = lambda' * v_L, lambda' in [1e-3, 1] (natural band)
  triplet mass:    M ~ 1 TeV (P-2026-039); scanned continuously 0.3-30 TeV
  double-duty:     y_junction in [0.7, 3]e-5 (the transfer integral's landing)

RAMP DISCIPLINE (the depth law): continuous log-grids, margins reported as
smooth curves, conclusions quoted as bands with their edges shown — no binary
corner checks, no point verdicts.
"""
import numpy as np

v = 246e9          # EW vev, eV
m3 = 50.2e-3       # heaviest light nu, eV (m1 = 2.25 meV, normal-ordering stack)
TeV = 1e12

def mu_from_mass(y, M):          # D1: light-mass duty inverted
    return m3 * M**2 / (y * v / np.sqrt(2))**2

def gamma_N(y, M):
    return y**2 * M / (8 * np.pi)

# ---- CORNER 1: the resonance ramp -----------------------------------------
# D1 = D5 with r = mu/Gamma treated as a CONTINUOUS variable, not a switch.
# y(M, r) = [16 pi m3 M / (r v^2)]^{1/4}; mu follows; v_L = mu/lambda'.
print("=" * 76)
print("CORNER 1 — the resonance ramp: y, mu, v_L as continuous functions of (M, r)")
print("=" * 76)
M_grid = np.logspace(np.log10(0.3), np.log10(30), 13) * TeV
r_grid = np.logspace(-1, 1, 9)          # mu/Gamma from 0.1 to 10 — the ramp
print(f"{'M [TeV]':>8} | y(r=1) | mu(r=1) [MeV] | v_L band [MeV] (lam' 1..1e-3, r 0.1..10) | S4 overlap frac")
for M in M_grid:
    y1 = (16 * np.pi * m3 * M / (1.0 * v**2))**0.25
    mu1 = mu_from_mass(y1, M)
    mus = np.array([mu_from_mass((16*np.pi*m3*M/(r*v**2))**0.25, M) for r in r_grid])
    vL_all = np.outer(mus, 1/np.logspace(-3, 0, 25)).ravel()   # mu/lambda'
    lo, hi = vL_all.min(), vL_all.max()
    frac_s4 = (vL_all < 20e6).mean()     # fraction of the natural band S4 reaches
    print(f"{M/TeV:8.2f} | {y1:.2e} | {mu1/1e6:11.4f} | [{lo/1e6:9.4f}, {hi/1e6:12.1f}] | {frac_s4:5.2f}")

# ---- CORNER 2: the double-duty ramp ----------------------------------------
print()
print("=" * 76)
print("CORNER 2 — the junction-vertex ramp: mu, mu/Gamma, v_L floor vs y (M = 1 TeV)")
print("=" * 76)
y_grid = np.logspace(np.log10(0.7e-5) - 1.3, np.log10(3e-5) + 1.3, 15)  # wide ramp around the junction band
print(f"{'y':>10} | {'mu':>12} | {'mu/Gamma':>10} | {'v_L floor (lam<=1)':>18} | {'g ceiling':>10} | in junction band?")
for y in y_grid:
    M = 1 * TeV
    mu = mu_from_mass(y, M)
    res = mu / gamma_N(y, M)
    vL_floor = mu
    g_ceil = m3 / vL_floor
    inb = 0.7e-5 <= y <= 3e-5
    print(f"{y:10.2e} | {mu:12.4e} | {res:10.2e} | {vL_floor:14.4e} eV | {g_ceil:10.2e} | {'YES' if inb else '—'}")

# ---- THE BRIDGE: continuous M(y) demanded by resonance ----------------------
print()
print("=" * 76)
print("THE BRIDGE — M forced by (resonance + mass duty) as a continuous curve in y")
print("=" * 76)
print(f"{'y':>10} | M forced (r=1)      | distance to the 1-TeV triplet duty")
for y in np.logspace(-6, -2.5, 15):
    M_forced = 1.0 * v**2 * y**4 / (16 * np.pi * m3)
    print(f"{y:10.2e} | {M_forced:12.4e} eV | {np.log10(1*TeV/max(M_forced,1e-30)):6.1f} decades")

print()
print(f"Benchmark A cross-check (v_L = 5 MeV): g = m3/v_L = {m3/5e6:.2e} (recorded: 1.2e-8)")
