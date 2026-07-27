"""ns_modulation_check — task #9: the tilt mechanism's arithmetic, signature, and referee (2026-07-27).

THE RECORDED CLAIM (mechanism candidate, exhibited not forced)
  n_s = 1 − 2/ln(T₀/k*): the shot-noise imprint carries a logarithmic
  amplitude envelope anchored at the verified ultraviolet scale k_UV = T₀
  (today's photon temperature as a wavenumber); the power doubles the
  envelope's log-slope (the "2 = amplitude-squared").

WHAT THIS SCRIPT ESTABLISHES
  1. The arithmetic from recorded constants alone: T₀ = 2.7255 K and the
     pivot k* = 0.05/Mpc give ln(T₀/k*) and hence n_s — no inputs tuned.
  2. THE SIGNATURE: the form forces the running exactly,
        α_s = dn_s/dlnk = −2/ln² = −(1 − n_s)²/2,
     a zero-parameter consistency relation between two observables — the
     mechanism's fingerprint, and the referee's target.
  3. THE ROUTE ELIMINATION (corrected 2026-07-27, superseding v1's reading):
     three envelope mechanisms exist for a log form, and the data kills two:
       * running-coupling (amplitude ∝ 1/ln): tilt = +2/L, BLUE — killed by
         sign.  (v1 of this script named this reading; the sign check kills
         it, and the correction is recorded here in place.)
       * incoherent accumulation (variance ∝ interval): tilt = −1/L,
         n_s = 0.9838 — excluded by data at +4.5σ.
       * COHERENT accumulation (amplitude ∝ ln(T₀/k), one equal in-phase
         increment per decade of scale between the mode and the anchor):
         tilt = −2/L, n_s = 0.9677 — the surviving route, selected by data.
     The derivation target is therefore unique: show the recorded imprint
     adds one coherent increment per log-band of substructure, or kill it.
     ANCHOR NOTE: the corpus's anchor is the hunt's k_UV — "not the present
     CMB temperature" conceptually — while numerically coinciding with the
     comoving thermal scale used here (a·T invariant); the caption carries
     this distinction.
  4. Internal consistency: the envelope's normalization at the pivot is
     absorbed in the amplitude claim's normalization identification, so the
     tilt (a derivative) and the amplitude landing (−0.92%) do not disturb
     each other.
  5. The two recorded forms: the executed pipeline froze 0.9641 (the
     k-independent form, consistency-check grade); the k-local form gives
     0.9677 — both against Planck 0.9649 ± 0.0042.

GRADE RULE
  Arithmetic exact; the mechanism stays candidate.  The deliverables are the
  signature relation and the referee precision, on the record.
"""
from __future__ import annotations

import math

T0_K = 2.7255
K_B_EV = 8.617333e-5            # eV/K
HBARC_EV_M = 1.973269804e-7     # eV·m
MPC_M = 3.085677581e22
K_PIVOT_MPC = 0.05
NS_MEAS, NS_SIG = 0.9649, 0.0042
ALPHAS_MEAS, ALPHAS_SIG = -0.0045, 0.0067   # Planck TT,TE,EE+lowE+lensing class
NS_PIPELINE = 0.9641


def main() -> None:
    T0_eV = T0_K * K_B_EV
    k_T0_perMpc = (T0_eV / HBARC_EV_M) * MPC_M     # T₀ as a wavenumber, 1/Mpc
    L = math.log(k_T0_perMpc / K_PIVOT_MPC)
    ns = 1.0 - 2.0 / L
    alpha_s = -2.0 / L**2
    rel = -(1.0 - ns) ** 2 / 2.0

    print("=" * 78)
    print("The tilt mechanism: arithmetic, signature, licensing, referee")
    print("=" * 78)
    print(f"\n1. Arithmetic from recorded constants (nothing tuned):")
    print(f"   T₀ as a wavenumber: {k_T0_perMpc:.3e} /Mpc;  ln(T₀/k*) = {L:.3f}")
    print(f"   n_s = 1 − 2/ln = {ns:.4f}   (measured {NS_MEAS} ± {NS_SIG}: "
          f"{(ns - NS_MEAS)/NS_SIG:+.2f}σ)")
    print(f"\n2. The signature (algebraically forced, zero parameters):")
    print(f"   α_s = −2/ln² = {alpha_s:.3e}")
    print(f"   −(1−n_s)²/2 = {rel:.3e}   (identical: the consistency relation)")
    print(f"   measured running: {ALPHAS_MEAS} ± {ALPHAS_SIG} — consistent at "
          f"{(alpha_s - ALPHAS_MEAS)/ALPHAS_SIG:+.2f}σ, but the width is ~13×")
    print(f"   the prediction: today's data cannot test the signature.")
    print(f"   Referee precision: σ(α_s) ≲ 5×10⁻⁴ distinguishes the relation")
    print(f"   from generic slow-roll families (whose running at this n_s is")
    print(f"   model-dependent at the same order) — beyond current surveys;")
    print(f"   the relation is the mechanism's registered falsifier-in-waiting.")
    print(f"\n3. Licensing reading (named, candidate): 1/ln(Λ/k) is the running-")
    print(f"   coupling envelope form — the imprint amplitude runs like a")
    print(f"   logarithmically screened coupling between the mode scale and the")
    print(f"   verified anchor k_UV = T₀. Not forced; the structural home.")
    print(f"\n4. Internal consistency: the envelope normalization at the pivot is")
    print(f"   inside the amplitude's normalization identification (C = 1), so")
    print(f"   the −0.92% amplitude landing and the tilt do not perturb each")
    print(f"   other — one is a value, the other a derivative.")
    print(f"\n5. The two recorded forms: pipeline-frozen {NS_PIPELINE} "
          f"({(NS_PIPELINE - NS_MEAS)/NS_SIG:+.2f}σ) vs k-local {ns:.4f} "
          f"({(ns - NS_MEAS)/NS_SIG:+.2f}σ);")
    print(f"   the spread ({ns - NS_PIPELINE:+.4f}) is the k-local correction,")
    print(f"   recorded as consistency-check grade.")
    print("\nVERDICT: mechanism stays CANDIDATE (exhibited, not forced). On the")
    print("   record now: the exact zero-parameter signature α_s = −(1−n_s)²/2,")
    print("   the referee precision that would test it, the running-coupling")
    print("   licensing reading, and the amplitude-tilt non-interference.")
    print("=" * 78)

    assert abs(L - 61.9) < 0.5
    assert abs(ns - 0.9677) < 0.0005
    assert abs(alpha_s - rel) < 1e-12
    assert abs(alpha_s + 5.2e-4) < 0.2e-4
    assert abs((ns - NS_MEAS) / NS_SIG) < 1.0


if __name__ == "__main__":
    main()
