"""bounce_m6_rebound_1d_hypersonic — closing the J1 delivery-envelope gap (2026-07-27).

WHY THIS EXISTS
  The handoff joints (bounce_task4_handoff_joints.py) found the directional
  squeeze delivers inflow at Mach 14–16 at the door, while the verified 1D
  rebound runs only reached Mach 3.  Extrapolating would be fabrication;
  testing is not.  Same verified split-step scheme as bounce_m6_rebound_1d.py,
  with resolution scaled to the steeper flow: N = 8192 over L = 120 (phase
  winding ~0.2 rad/cell at Mach 15), DT = 1e-4.

RUNS
  (A, v₀) = (5, 8), (5, 15), (20, 15) — the delivered window's high end.

GRADE RULE
  Numbers quoted only with energy conserved to ≤2%.  A rebound at Mach 15 is
  a computed toy result; a failure to rebound is equally reportable.
"""
from __future__ import annotations

import math

import numpy as np

L, N, DT, T_MAX = 120.0, 8192, 1.0e-4, 12.0
DX = L / N
X = np.linspace(-L / 2, L / 2, N, endpoint=False)
K = 0.5 * (2.0 * math.pi * np.fft.fftfreq(N, d=DX)) ** 2
XI_SEC = 402.0 * 1.496e11 / (math.sqrt(3.0 / 137.036) * 2.99792458e8)


def run(A: float, v0: float, R: float = 8.0) -> dict:
    n0 = 1.0 + A * np.exp(-((X / R) ** 2))
    v = -v0 * (X / R) * np.exp(-0.5 * (X / R) ** 2)
    phase = np.cumsum(v) * DX
    psi = np.sqrt(n0) * np.exp(1j * phase)

    def energy(psi_):
        n = np.abs(psi_) ** 2
        dpsi = np.gradient(psi_, DX)
        return float(0.5 * np.sum(np.abs(dpsi) ** 2) * DX
                     + 0.5 * np.sum((n - 1.0) ** 2) * DX)

    e0 = energy(psi)
    steps = int(T_MAX / DT)
    sample = max(1, int(0.1 / DT))
    nmax, times, outward_hist = [], [], []
    mask = np.abs(X) > 2.0 * R
    for s in range(steps):
        n = np.abs(psi) ** 2
        psi *= np.exp(-0.5j * DT * (n - 1.0))
        psi = np.fft.ifft(np.exp(-1j * DT * K) * np.fft.fft(psi))
        n = np.abs(psi) ** 2
        psi *= np.exp(-0.5j * DT * (n - 1.0))
        if s % sample == 0:
            n = np.abs(psi) ** 2
            nmax.append(float(n.max()))
            times.append(s * DT)
            dpsi = np.gradient(psi, DX)
            j = np.imag(np.conj(psi) * dpsi)
            vf = j / np.maximum(n, 1e-12)
            outward_hist.append(float(np.mean(vf[mask] * np.sign(X[mask]))))
    nmax_a = np.asarray(nmax)
    kpk = int(np.argmax(nmax_a))
    e1 = energy(psi)
    return {
        "A": A, "v0": v0, "n_init": 1.0 + A,
        "n_peak": float(nmax_a[kpk]), "t_turn": float(times[kpk]),
        "n_final": float(nmax_a[-1]),
        "outward_late": float(np.mean(outward_hist[len(outward_hist) // 2:])),
        "dE_frac": abs(e1 - e0) / max(e0, 1e-12),
        "turned": float(nmax_a[-1]) < 0.7 * float(nmax_a[kpk]),
    }


def main() -> None:
    print("=" * 78)
    print("Hypersonic 1D rebound — the delivered-Mach window, tested not extrapolated")
    print("=" * 78)
    print(f"  {'A':>4} {'v0':>5} {'n_i':>6} {'n_pk':>8} {'×':>6} {'t_turn':>7} "
          f"{'n_f':>8} {'out':>7} {'turn?':>6} {'dE%':>6}")
    rows = []
    for A, v0 in ((5.0, 8.0), (5.0, 15.0), (20.0, 15.0)):
        r = run(A, v0)
        rows.append(r)
        print(f"  {A:4.0f} {v0:5.1f} {r['n_init']:6.1f} {r['n_peak']:8.2f} "
              f"{r['n_peak']/r['n_init']:6.2f} {r['t_turn']:7.2f} {r['n_final']:8.2f} "
              f"{r['outward_late']:7.3f} {'YES' if r['turned'] else 'no':>6} "
              f"{100*r['dE_frac']:6.2f}")
    print()
    ok = all(r["dE_frac"] < 0.02 for r in rows)
    if ok and all(r["turned"] for r in rows) and all(r["outward_late"] > 0 for r in rows):
        print("VERDICT: the medium turns hypersonic compression too — the rebound")
        print("  mechanism holds through the full delivered-Mach window (J1 gap")
        print("  CLOSED by test). Compression amplification and turn times in the")
        print("  table; energy conserved in every run.")
    else:
        print("VERDICT: NOT clean — see the table; do not quote uncorroborated rows.")
    print("=" * 78)

    assert ok, "energy guard failed — do not quote"
    assert all(r["turned"] for r in rows)
    assert all(r["outward_late"] > 0 for r in rows)


if __name__ == "__main__":
    main()
