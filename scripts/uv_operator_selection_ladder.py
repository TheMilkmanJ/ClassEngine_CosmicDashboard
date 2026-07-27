"""uv_operator_selection_ladder — task #18: the assumption shrinks, then reduces (2026-07-27).

THE SELECTION LADDER, WITH DATA DOING MAXIMAL WORK
  Layer 1 (which bilinear class) — DATA + STRUCTURE, recorded: the Higgs
    portal H†H shifts every mass including quarks (deuterium kills it at
    12σ; bounded to λ_p ≲ 10⁻⁹); the neutrino bilinear (LH)(LH) cannot
    deliver an electron-mass shift at any coefficient.  The Yukawa class
    survives by exclusion.
  Layer 2 (quarks vs leptons) — DATA, recorded: a universal quark-mass
    shift moves the deuteron binding at 12–18σ.  Leptophilic by data.
  Layer 3 (which lepton) — THE RESIDUAL ASSUMPTION, analyzed here.

THE LAYER-3 ANALYSIS (new)
  Two surviving structures: electron-only (the standing choice) and
  flavor-universal fractional coupling (one coefficient across the lepton
  Yukawas — the minimal-flavor-violation-class structure, natural for a
  singlet coupling through a lepton-partnered sector).  The question:
  does ANY recorded observable distinguish them?
    * Muon channel: a fractional shift δm_μ/m_μ = ε ≈ 1.25% moves the muon
      annihilation epoch (T ~ m_μ/3 ≈ 35 MeV) by 1.25% — but annihilation
      completes long before neutrino decoupling (~2–3 MeV) and BBN's n/p
      freeze-out (~0.7 MeV): the entropy fully equilibrates into the one
      bath either way.  No trace in N_eff, η, or any abundance.
    * Tau channel: annihilates earlier still (~600 MeV).  Same conclusion,
      stronger.
    * Recombination and all later atomic physics see only m_e.
  ⟹ THE TWO STRUCTURES ARE OBSERVATIONALLY IDENTICAL across every recorded
  window.  The layer-3 "assumption" carries no empirical content: what is
  actually assumed is only the overall coefficient — the flavor structure
  is invisible.  Reclassification: from "assumption with physical content"
  to "representation choice."

THE REDUCTION (candidate grade, no new referee)
  The kernel program's own claim is that the charged-lepton mass matrix is
  the dark condensate's OUTPUT (the portal √σ_dark = m_e; the string-bound
  family structure).  Under that claim the operator selection is not a
  choice at all: the singlet multiplies the lepton Yukawas because they are
  its own condensate outputs, and the electron's dominance in observables
  is automatic (atomic physics reads m_e).  #125 thereby REDUCES INTO the
  kernel program — settled exactly when it is, judged by the same referees
  (the SU(2) N_f = 3 lattice campaign, the deviation lock, m_τ).  No new
  judge needed; the task gates onto the existing τ program.

GRADE RULE
  Layer-3 invisibility: computed timing hierarchy, asserted below.  The
  reduction: candidate, inheriting the kernel program's grade.  The loop
  stability of the standing choice (H†H induced ~500× under bound) is
  recorded and unchanged.  Nothing promoted.
"""
from __future__ import annotations

M_MU_MEV = 105.66
M_TAU_MEV = 1776.9
T_NU_DEC_MEV = 2.5
T_NP_FREEZE_MEV = 0.7
EPS = 0.012543


def main() -> None:
    t_mu_ann = M_MU_MEV / 3.0
    t_tau_ann = M_TAU_MEV / 3.0
    print("=" * 78)
    print("The operator selection: the ladder, the invisibility, the reduction")
    print("=" * 78)
    print("\n   layer 1 (bilinear class): Higgs portal dead by deuterium (12σ);")
    print("   neutrino bilinear structurally unable — Yukawa class by exclusion.")
    print("   layer 2 (quarks vs leptons): leptophilic by data (12–18σ).")
    print("\n   layer 3 — the timing hierarchy that makes flavor invisible:")
    print(f"   τ annihilation epoch   ~ {t_tau_ann:6.0f} MeV")
    print(f"   μ annihilation epoch   ~ {t_mu_ann:6.1f} MeV   (a {100*EPS:.2f}% m_μ shift")
    print(f"                                        moves this by {100*EPS:.2f}% — of an epoch")
    print(f"                                        whose entropy fully re-equilibrates)")
    print(f"   neutrino decoupling    ~ {T_NU_DEC_MEV:6.1f} MeV   ← everything above this")
    print(f"   n/p freeze-out         ~ {T_NP_FREEZE_MEV:6.1f} MeV      merges into one bath")
    print("   ⟹ muon- and tau-channel shifts leave NO trace in N_eff, η, any")
    print("   abundance, or any atomic observable. Electron-only and flavor-")
    print("   universal couplings are observationally identical everywhere the")
    print("   corpus looks.")
    print("\n   RECLASSIFICATION: the layer-3 assumption carries no empirical")
    print("   content — it is a representation choice, not a physical one.")
    print("\n   THE REDUCTION: under the kernel program's own claim (the lepton")
    print("   mass matrix is the condensate's output; the portal √σ_dark = m_e),")
    print("   the selection is automatic — the singlet multiplies the lepton")
    print("   Yukawas because they are its outputs. #125 reduces into the kernel")
    print("   program: settled when it is, by the same referees. No new judge.")
    print("=" * 78)

    assert t_mu_ann > 10 * T_NU_DEC_MEV
    assert t_tau_ann > 100 * T_NU_DEC_MEV
    assert T_NU_DEC_MEV > 3 * T_NP_FREEZE_MEV


if __name__ == "__main__":
    main()
