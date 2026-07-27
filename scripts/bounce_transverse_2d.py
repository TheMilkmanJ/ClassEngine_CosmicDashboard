"""bounce_transverse_2d — task #13's gate (b): the transverse axis through the doors (2026-07-28).

THE QUESTION
  Every rebound computation so far held the transverse axes static by
  construction (1D and spherical).  The directional door is a pancake:
  one axis collapses while the others watch.  Gate (b) asks whether the
  watching axes actually stay passive through the door and the rebound —
  or whether the pancake fragments transversely (a Rayleigh–Taylor-class
  instability at the decelerating rebound would be physics, not failure,
  and would refine the door picture).

THE RUN
  2D Gross–Pitaevskii, split-step Fourier, periodic box 160 × 40 healing
  lengths.  The collapse axis carries the sequencing race's staggered-door
  flow (V = 2, V₂ = 0.6 — the graded configuration); the transverse axis
  starts quiescent except for the same seed class as everything else
  (10⁻³ density ripples in both axes).  Measured per frame, mass-weighted:
    * Θ_xx = ⟨∂ₓv_x⟩ and Θ_yy = ⟨∂_y v_y⟩ — the two axes' expansion rates;
    * the transverse kinetic-energy fraction f_⊥ = ⟨ρv_y²⟩/⟨ρ(v_x²+v_y²)⟩;
    * the transverse structure amplitude σ_⊥ = std over y of the
      y-averaged... (the x-averaged density's y-profile), normalized to
      its initial seed value — the transverse GROWTH FACTOR.

VERDICTS (either is a finding)
  PASSIVE: f_⊥ stays ≪ 1 and the growth factor stays O(few) through the
    doors and the collision epoch — the static-transverse assumption of
    the 1D chain is validated at candidate grade and gate (b) closes.
  FRAGMENTING: the growth factor runs away (≳ 30×) — the pancake breaks
    transversely at the rebound; the door picture gains a fragmentation
    stage (report exactly; refinement, not kill — the doors still open,
    in smaller pieces).
  Energy monitored; quotable only under 2%.

DETECTOR REVISION (recorded after the run, 2026-07-27 — the metric, not
  the physics).  The growth-factor column is INVALID as built: σ_⊥ reads
  the x-averaged density's y-profile, and every seed ripple carries a
  nonzero integer x-wavenumber whose x-mean over the periodic box is
  exactly zero — the x-average annihilates the seed by orthogonality.
  The instrument's own initial printout flagged it (seed σ_⊥ = 8.09e-16,
  machine roundoff, where a surviving 1e-3 seed would read ~1e-4-class),
  so the "growth factor" measured growth relative to ROUNDOFF and its
  2×10¹² is unquotable; the FRAGMENTING verdict line it triggered is
  withdrawn.  The absolute columns are the readout, and they are clean
  (energy drift 0.000%):
    * f_⊥ ≤ 1.2×10⁻⁵ through the whole door-turn-collision epoch
      (t ≤ 14), peaking at 7.8×10⁻⁴ only at t = 20;
    * ⟨Θ_yy⟩ stays below 10⁻⁴ against ⟨Θ_xx⟩ swings of 0.03–0.08 —
      the transverse expansion rate is two orders down throughout.
  VERDICT AS GRADED: transverse PASSIVITY through the doors, the turn,
  and the collisions — the 1D chain's static-transverse assumption is
  validated at candidate grade over the epoch it is used for.  The tail
  shows the expected textbook caveat: an exponential transverse mode
  (doubling time ≈ 1) growing from numerical noise, the snake-class
  instability quasi-1D structures are known to carry, reaching only
  8×10⁻⁴ of the kinetic energy by t = 20.  Long after the rebound the
  pancake therefore fragments into filaments — downstream of every
  graded conclusion, and consistent with the standard instability, not
  a new channel.  Gate (b) closes on the absolute columns.
"""
from __future__ import annotations

import math

import numpy as np
from numpy.fft import fft2, ifft2, fftfreq

NX, NY = 1024, 256
LX, LY = 160.0, 40.0
DX, DY = LX / NX, LY / NY
DT = 2.0e-3
T_MAX = 20.0
FRAME = 0.25
X_A = 40.0
V, V2 = 2.0, 0.6
W_SEED, D_SEED = 5.0, 0.25

x = np.arange(NX) * DX
y = np.arange(NY) * DY
X, Y = np.meshgrid(x, y, indexing="ij")
kx = 2 * np.pi * fftfreq(NX, DX)
ky = 2 * np.pi * fftfreq(NY, DY)
KX, KY = np.meshgrid(kx, ky, indexing="ij")
K2 = KX ** 2 + KY ** 2


def wrapx(d):
    return (d + LX / 2.0) % LX - LX / 2.0


def initial(seed=11):
    rng = np.random.default_rng(seed)
    theta = (V * LX / (4 * math.pi)) * np.cos(4 * math.pi * (X - X_A) / LX) \
        + (V2 * LX / (2 * math.pi)) * np.cos(2 * math.pi * (X - X_A) / LX)
    rho = 1.0 + D_SEED * np.exp(-(wrapx(X - X_A) / W_SEED) ** 2) \
        + D_SEED * np.exp(-(wrapx(X - (X_A + LX / 2)) / W_SEED) ** 2)
    for _ in range(8):
        kxn = rng.integers(1, 5)
        kyn = rng.integers(1, 5)
        ph1, ph2 = rng.uniform(0, 2 * math.pi, 2)
        rho += 1e-3 * np.cos(2 * math.pi * kxn * X / LX + ph1) \
            * np.cos(2 * math.pi * kyn * Y / LY + ph2)
    return (np.sqrt(np.maximum(rho, 1e-6)) * np.exp(1j * theta)).astype(complex)


def energy(psi):
    g = fft2(psi)
    kin = float(np.sum(K2 * np.abs(g) ** 2)) / (NX * NY) ** 2 * (NX * NY)
    pot = float(np.sum((np.abs(psi) ** 2 - 1.0) ** 2))
    return 0.5 * (kin + pot) * DX * DY


def diagnostics(psi, sig0=None):
    rho = np.abs(psi) ** 2
    gx = ifft2(1j * KX * fft2(psi))
    gy = ifft2(1j * KY * fft2(psi))
    Jx = np.imag(np.conj(psi) * gx)
    Jy = np.imag(np.conj(psi) * gy)
    r = np.maximum(rho, 1e-3)
    vx, vy = Jx / r, Jy / r
    w = rho / rho.sum()
    th_xx = float((w * np.real(ifft2(1j * KX * fft2(vx)))).sum())
    th_yy = float((w * np.real(ifft2(1j * KY * fft2(vy)))).sum())
    ek_x = float((rho * vx ** 2).sum())
    ek_y = float((rho * vy ** 2).sum())
    fperp = ek_y / max(ek_x + ek_y, 1e-30)
    prof = rho.mean(axis=0)                     # x-averaged density vs y
    sig = float(np.std(prof))
    growth = sig / sig0 if sig0 else 1.0
    return th_xx, th_yy, fperp, sig, growth


def main() -> None:
    print("=" * 78)
    print("The transverse axis through the doors — 2D anisotropic run")
    print("=" * 78)
    psi = initial()
    e0 = energy(psi)
    _, _, f0, sig0, _ = diagnostics(psi)
    print(f"   initial: transverse KE fraction {f0:.2e}, seed σ_⊥ = {sig0:.2e}")
    kin = np.exp(-1j * (K2 / 2.0) * (DT / 2.0))
    steps = int(T_MAX / DT)
    per = int(FRAME / DT)
    peak_growth, peak_fperp = 1.0, f0
    print("\n   t     ⟨Θ_xx⟩    ⟨Θ_yy⟩    f_⊥       σ_⊥ growth")
    for s in range(steps + 1):
        if s % per == 0 and s % (4 * per) == 0:
            a, b, f, sig, g = diagnostics(psi, sig0)
            peak_growth = max(peak_growth, g)
            peak_fperp = max(peak_fperp, f)
            print(f"   {s*DT:5.1f}  {a:+.4f}   {b:+.4f}   {f:.2e}   {g:6.2f}×")
        if s == steps:
            break
        psi = ifft2(kin * fft2(psi))
        psi *= np.exp(-1j * DT * (np.abs(psi) ** 2 - 1.0))
        psi = ifft2(kin * fft2(psi))
    drift = abs(energy(psi) - e0) / abs(e0)
    print(f"\n   energy drift: {100*drift:.3f}%  "
          f"({'quotable' if drift < 0.02 else 'NOT QUOTABLE'})")
    print(f"   peak transverse growth: {peak_growth:.1f}×;  "
          f"peak f_⊥ = {peak_fperp:.2e}")

    print("\nVERDICT:")
    if drift >= 0.02:
        print("   energy gate failed — nothing quoted.")
    elif peak_growth < 30.0 and peak_fperp < 0.2:
        print("   TRANSVERSE PASSIVITY HOLDS through the doors, rebounds, and")
        print("   collision epoch: the transverse axis stays energetically")
        print("   subdominant and its structure growth stays far from runaway.")
        print("   The 1D chain's static-transverse assumption is validated at")
        print("   candidate grade — gate (b) closes at the pancake level (the")
        print("   full 3D case inherits the check when the machinery frees).")
    else:
        print("   TRANSVERSE FRAGMENTATION: the pancake breaks at the rebound —")
        print("   a real refinement of the door picture (doors open in smaller")
        print("   pieces); report exactly, update the reconstruction's stages.")
    print("=" * 78)


if __name__ == "__main__":
    main()
