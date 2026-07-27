"""bounce_averaging_decomposition — task #13's gate (c): the averaging bookkeeping, computed (2026-07-28).

THE CLAIM TO EXHIBIT (RP log §20's reconciliation)
  The averaged turn is powered by the terms homogeneous averaging kills.
  In the medium's own 1D equation this is an exact identity: with mass-
  weighted averages ⟨·⟩ ≡ ∫ρ(·)dx/∫ρdx and Θ = ∂ₓv, continuity plus the
  Madelung–Euler equation give
      d⟨Θ⟩/dt = −⟨Θ⟩² − Var_ρ(Θ) − ⟨∂ₓₓ(ρ + Q_qp)⟩_ρ ,
  Q_qp = −½(∂ₓₓ√ρ)/√ρ (the quantum potential).  The first two terms are
  non-positive contributions at the turn (−⟨Θ⟩² always; −Var always), so
  ⟨Θ⟩ can only rise through zero if the STRESS term ⟨∂ₓₓ(ρ+Q_qp)⟩_ρ is
  sufficiently negative — mass concentrated where the total pressure
  (interaction + quantum) peaks, i.e. at the rebounding cores.  Under a
  homogeneous density that term is identically zero: it IS the
  homogeneity-killed channel, named by the reconciliation.

WHAT THIS RUN DOES
  Reruns the sequencing race's graded configuration (V = 2, V₂ = 0.6 — the
  clock-stagger run of §21) and logs, per frame: ⟨Θ⟩, its measured time
  derivative, and the three right-hand terms.  Two verdicts:
    (a) the IDENTITY CHECK — the measured d⟨Θ⟩/dt must match the sum of
        the three terms (a strong numerical self-test of the whole
        decomposition; tolerance 10% RMS over the active window);
    (b) the ATTRIBUTION — at the turn epoch (⟨Θ⟩ crossing zero) the
        stress term must be the positive driver (its contribution
        −⟨∂ₓₓ(ρ+Q_qp)⟩ > 0) and must exceed the opposing variance term.

GRADE RULE
  Gate (c) of the white-hole task closes at candidate grade if (a) and (b)
  both land: the averaged re-expansion's funding is then exhibited, term
  by term, as the gradient stress of the inhomogeneous regime — the
  bookkeeping the fixed-box run could not perform.  Failure of (a) is a
  harness bug (fix before grading); failure of (b) with (a) passing would
  be a REAL adverse result for the reconciliation's mechanism and goes to
  the ledger.
"""
from __future__ import annotations

import math

import numpy as np

L = 160.0
N = 1280
DT = 2.0e-3
T_MAX = 20.0
FRAME = 0.05
X_A = 40.0
V, V2 = 2.0, 0.6
W_SEED, D_SEED = 5.0, 0.25

x = np.arange(N) * (L / N)
dx = L / N
k = 2.0 * np.pi * np.fft.fftfreq(N, dx)


def wrap(d):
    return (d + L / 2.0) % L - L / 2.0


def initial():
    theta = (V * L / (4 * math.pi)) * np.cos(4 * math.pi * (x - X_A) / L) \
        + (V2 * L / (2 * math.pi)) * np.cos(2 * math.pi * (x - X_A) / L)
    rho = 1.0 + D_SEED * np.exp(-(wrap(x - X_A) / W_SEED) ** 2) \
        + D_SEED * np.exp(-(wrap(x - (X_A + L / 2)) / W_SEED) ** 2)
    return np.sqrt(rho) * np.exp(1j * theta)


def d1(f):
    return (np.roll(f, -1) - np.roll(f, 1)) / (2 * dx)


def d2(f):
    return (np.roll(f, -1) - 2 * f + np.roll(f, 1)) / dx ** 2


# v2 NOTE (the run's own identity check caught v1): the bare Madelung
# decomposition is singular at near-zero-density cores — v1's ±25-scale terms
# were core spikes and the identity failed at 100% residual, refusing the
# grading exactly as designed.  v2 works at the COARSE-GRAINED level, where
# the identity is exact by construction: coarse continuity and momentum
# conservation are linear (commute with the kernel), the momentum flux
# computes regularly from ψ itself (no divisions), and the closure Π carries
# every sub-kernel term.  The physical question is coarse-grained anyway —
# this is the Buchert-type bookkeeping's own level.
SIG_CG = 2.0
KERNEL = np.exp(-0.5 * (SIG_CG * k) ** 2)


def smooth(f):
    return np.real(np.fft.ifft(KERNEL * np.fft.fft(f)))


def diagnostics(psi):
    rho = np.abs(psi) ** 2
    px = np.fft.ifft(1j * k * np.fft.fft(psi))
    J = np.imag(np.conj(psi) * px)
    sq = np.abs(psi)
    dsq = d1(sq)
    kin_flow = np.abs(px) ** 2 - dsq ** 2          # = ρv², regular in ψ
    T_int = 0.5 * rho ** 2
    T_qu = dsq ** 2 - 0.25 * d2(rho)
    rho_c = smooth(rho)
    J_c = smooth(J)
    v_c = J_c / np.maximum(rho_c, 1e-6)
    th = d1(v_c)
    w = rho_c / rho_c.sum()
    mean_th = float((w * th).sum())
    var_th = float((w * (th - mean_th) ** 2).sum())

    def drive_of(Pi):
        return -float((w * d1(d1(Pi) / np.maximum(rho_c, 1e-6))).sum())

    Pi_reyn = smooth(kin_flow) - rho_c * v_c ** 2
    dr_int = drive_of(smooth(T_int))
    dr_qu = drive_of(smooth(T_qu))
    dr_rey = drive_of(Pi_reyn)
    return mean_th, var_th, dr_int, dr_qu, dr_rey


def main() -> None:
    print("=" * 78)
    print("The averaging bookkeeping: d⟨Θ⟩/dt decomposed in the medium's own run")
    print("=" * 78)
    psi = initial()
    kin = np.exp(-1j * (k ** 2 / 2.0) * (DT / 2.0))
    steps = int(T_MAX / DT)
    per = int(FRAME / DT)
    ts, ths, vars_, di, dq, dr = [], [], [], [], [], []
    for s in range(steps + 1):
        if s % per == 0:
            m, va, a, b, c = diagnostics(psi)
            ts.append(s * DT)
            ths.append(m)
            vars_.append(va)
            di.append(a)
            dq.append(b)
            dr.append(c)
        if s == steps:
            break
        psi = np.fft.ifft(kin * np.fft.fft(psi))
        psi *= np.exp(-1j * DT * (np.abs(psi) ** 2 - 1.0))
        psi = np.fft.ifft(kin * np.fft.fft(psi))
    ts = np.array(ts)
    ths = np.array(ths)
    vars_ = np.array(vars_)
    di, dq, dr = np.array(di), np.array(dq), np.array(dr)
    strs = -(di + dq + dr)          # total drive with the sign of the identity

    # measured derivative vs the identity's RHS, over the active window
    dth = np.gradient(ths, ts)
    rhs = -ths ** 2 - vars_ - strs
    win = (ts > 2.0) & (ts < 16.0)
    resid = dth[win] - rhs[win]
    scale = np.sqrt(np.mean(np.abs(dth[win]) ** 2)) + np.sqrt(np.mean(rhs[win] ** 2))
    ident = float(np.sqrt(np.mean(resid ** 2)) / max(scale, 1e-12))
    print(f"\n(a) identity check over t ∈ [2, 16]: RMS residual / RMS scale = "
          f"{ident:.3f}  ({'PASS ≤ 0.10' if ident <= 0.10 else 'FAIL — harness'})")

    # the crossing and the attribution there
    cross = None
    for i in range(1, len(ts)):
        if ths[i - 1] < 0 <= ths[i] and ts[i] > 2.0:
            cross = i
            break
    if cross is None:
        print("(b) ⟨Θ⟩ never crossed zero in the window — report as-is.")
        return
    i0, i1 = max(cross - 10, 0), min(cross + 10, len(ts) - 1)
    drive_stress = float(np.mean(-strs[i0:i1]))
    c_int = float(np.mean(di[i0:i1]))
    c_qu = float(np.mean(dq[i0:i1]))
    c_rey = float(np.mean(dr[i0:i1]))
    oppose_var = float(np.mean(vars_[i0:i1]))
    oppose_mean = float(np.mean(ths[i0:i1] ** 2))
    print(f"\n(b) at the turn (⟨Θ_c⟩ crosses zero, t = {ts[cross]:.2f}), the terms"
          f" of d⟨Θ_c⟩/dt (window mean):")
    print(f"    total stress drive           = {drive_stress:+.4f}"
          f"   {'(POSITIVE — the driver)' if drive_stress > 0 else '(not driving!)'}")
    print(f"      · interaction pressure     = {c_int:+.4f}")
    print(f"      · quantum (gradient) part  = {c_qu:+.4f}")
    print(f"      · sub-kernel Reynolds part = {c_rey:+.4f}")
    print(f"    variance      −Var(Θ_c)      = {-oppose_var:+.4f}   (opposes)")
    print(f"    mean-square   −⟨Θ_c⟩²        = {-oppose_mean:+.4f}   (opposes)")
    net = drive_stress - oppose_var - oppose_mean
    print(f"    net d⟨Θ_c⟩/dt                = {net:+.4f}"
          f"   ({'rising through zero ✓' if net > 0 else 'not rising'})")

    print("\nVERDICT:")
    if ident <= 0.10 and drive_stress > 0 and net > 0:
        print("   GATE (c) CLOSES at candidate grade: the identity verifies, and")
        print("   the averaged turn is funded by the gradient-stress term — the")
        print("   channel that vanishes identically under homogeneous averaging,")
        print("   exactly as the reconciliation claimed. The bookkeeping the")
        print("   fixed box could not perform is performed.")
    elif ident > 0.10:
        print("   The identity fails — harness diagnosis before any grading.")
    else:
        print("   The identity holds but the stress term does not drive the")
        print("   turn — a REAL adverse result for the reconciliation's")
        print("   mechanism. Ledger row required.")
    print("=" * 78)


if __name__ == "__main__":
    main()
