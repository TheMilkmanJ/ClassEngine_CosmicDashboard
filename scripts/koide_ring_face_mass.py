"""koide_ring_face_mass — what IS the face mass? The survivor becomes a fork referee (2026-07-27).

QUESTION
  The zero-point stabilizer holds the ring phase only for m_face ≤ 1.6·√σ
  (with breathing zero-point; 2.0·√σ without) — koide_ring_shape_qm.py.
  The face-mass identification was left open.  The corpus records TWO
  candidate identities for the ring's faces (the carrier fork):
    Branch A — ADJOINT lumps of the dark SU(2) sector (the gluonic branch);
    Branch B — the medium's own vortex structures (the phononic branch).
  Each carries a priceable mass class.  Where does each land against the
  ring window?

PRICING CLASSES (every transfer fenced; nothing invented)
  * Branch A, adjoint-lump class: in the QCD analog, states built on an
    adjoint source (gluelump class) sit well ABOVE the string scale —
    dressed masses of order 2–4·√σ (lattice SU(3) class values; the exact
    SU(2), N_f = 3 numbers do not exist — the same missing campaign as
    everything else in this sector).  Scheme caveat: static-source
    self-energy subtraction makes the absolute normalization convention-
    dependent; the CLASS statement (well above √σ) is robust.
  * Branch A, constituent-quark analog (if the faces are fundamental-class
    dressed constituents): QCD constituent mass ≈ 0.8·√σ (350 MeV vs
    √σ = 440 MeV).  Recorded corpus fact against this reading: three
    fundamentals of SU(2) admit no color singlet — the faces cannot be
    fundamentals (the forced-combination file), so this row is priced only
    to show it would have landed inside.
  * Branch B, vortex class: the face as a vortex structure of the medium
    carries energy set by the vortex stiffness — the recorded
    q̃² = c₂/√3 = 1.1106·√σ is the sector's own number for exactly that
    stiffness.  A vortex-structure face mass is q̃²-class times an O(1)
    geometry factor.
  * Portal dark states (~MeV band, recorded falsifiable prediction of
    √σ_dark = m_e): if the faces are these states, m_face ≈ 2–6·√σ.

GRADE RULE
  Class pricing with stated fences.  The output is a DISCRIMINATION map,
  not a verdict: which branch of the recorded carrier fork survives the
  ring window, given that the ring premise is load-bearing for c₂.
"""
from __future__ import annotations

ETA_C_CLASSICAL = 0.3457
ETA_C_WITH_ZP = 0.3864
ETA_COEFF = 0.4934          # eta = 0.4934 / sqrt(m_face/sqrt_sigma)

WINDOW_NO_ZP = (ETA_COEFF / ETA_C_CLASSICAL) ** 2
WINDOW_ZP = (ETA_COEFF / ETA_C_WITH_ZP) ** 2

CLASSES = [
    ("A: adjoint lump (gluelump class)", 2.0, 4.0,
     "SU(3)-class transfer; scheme-dependent normalization; robust: well above √σ"),
    ("A: constituent analog (excluded rep)", 0.7, 0.9,
     "three SU(2) fundamentals admit no singlet — priced for contrast only"),
    ("B: vortex structure (q̃²-class)", 0.8, 1.6,
     "q̃²/√σ = 1.11 recorded; O(1) geometry factor either side"),
    ("portal dark states (~MeV band)", 2.0, 6.0,
     "the recorded falsifiable band of √σ_dark = m_e"),
]


def verdict(lo: float, hi: float, window: float) -> str:
    if hi <= window:
        return "RING"
    if lo >= window:
        return "chain"
    return "straddles"


def main() -> None:
    print("=" * 78)
    print("Face-mass pricing: the zero-point survivor as a carrier-fork referee")
    print("=" * 78)
    print(f"\n   ring window: m_face ≤ {WINDOW_NO_ZP:.2f}·√σ (classical V), "
          f"≤ {WINDOW_ZP:.2f}·√σ (with breathing ZP)")
    print()
    print("   candidate face identity                  m/√σ        vs window (ZP)")
    for name, lo, hi, fence in CLASSES:
        v = verdict(lo, hi, WINDOW_ZP)
        print(f"   {name:40s} {lo:.1f}–{hi:.1f}       {v}")
        print(f"      fence: {fence}")
    print()
    print("READ — the stability question discriminates the carrier fork:")
    print("  * Branch A's honest mass class (adjoint lumps, 2–4·√σ) lands in the")
    print("    CHAIN phase: if the faces are gluonic lumps, the zero-point")
    print("    stabilizer fails and the equal-spacing ring premise has no payer.")
    print("  * Branch B's mass class (vortex structures, q̃²-class ≈ 0.8–1.6·√σ)")
    print("    lands INSIDE the ring window — the only identity that keeps the")
    print("    ring a ring with the recorded stabilizer.")
    print("  * The forced-combination theorem already said the ring must be a")
    print("    gauge–medium HYBRID (pure-gauge collapses, pure-medium has no")
    print("    scale). The stability program now adds: the INERTIA had better be")
    print("    medium-dominated — a hybrid whose mass is gluonic-dominated sits")
    print("    on the chain side of the window.")
    print()
    print("  Falsification structure this creates (recorded, not promoted):")
    print("  the SU(2) N_f = 3 lattice campaign's three-source geometry verdict")
    print("  and its adjoint-sector spectrum now cross-check each other — a")
    print("  Y-shaped ground state found WITH heavy gluonic faces would break")
    print("  the zero-point account and demand a different stabilizer; a")
    print("  collinear ground state would kill the ring premise directly.")
    print("=" * 78)

    assert 1.5 < WINDOW_NO_ZP < 2.5
    assert 1.2 < WINDOW_ZP < 2.0
    assert verdict(2.0, 4.0, WINDOW_ZP) == "chain"
    assert verdict(0.8, 1.6, WINDOW_ZP) in ("RING", "straddles")


if __name__ == "__main__":
    main()
