"""as_coincidence_price — task #8: the amplitude closed form, priced not vibed (2026-07-27).

THE CLAIM (recorded, deliberately exposed)
  A_s = (α_c/4πk)³ = 2.081×10⁻⁹ against the measured 2.100×10⁻⁹ (−0.92%,
  −0.66σ), with k = ln(1 + π/2α_c)/π = 1.36461 determined independently of
  the amplitude (gap equation 1.360; closed form 1.36461; the A_s-implied
  value 1.3602 ± 0.0064 — three determinations of one number).

WHAT "PROMOTE OR KILL" HONESTLY RESOLVES TO
  Promotion needs the shot-noise normalization derived (C = 1 — currently an
  identification, with a factor-250 convention spread recorded) and the host
  mismatch resolved (the k-integral reconstructs on a cold Fermi surface; the
  recorded basement is a hot Fermi point).  Neither is desk work tonight.
  The desk CAN price the coincidence: pre-declare a grammar of comparable
  zero-parameter forms, count how many land as close, and state what the
  scan cannot cheapen.

THE GRAMMAR (declared before counting; no post-hoc widening)
  F = s · (α^p_choice · k^q / (4π)^r)^d  with
    coupling choice ∈ {α, α_c = 3α}, p ∈ {1, 2}, q ∈ {−1, 0, 1},
    r ∈ {0, 1, 2}, d ∈ {1, 2, 3, 4}, s ∈ {1/3, 1/2, 1, 2, 3, π, 1/π}.
  Hit ≡ |F/A_s^meas − 1| < 0.01.  The recorded form is the member
  (α_c, p=1, q=−1, r=1, d=3, s=1).

GRADE RULE
  A pricing, not an adjudication.  The claim stays candidate/exposed; the
  outputs are the hit rate, the load-bearing facts a scan cannot touch, and
  the named promotion path and kill conditions.
"""
from __future__ import annotations

import itertools
import math

ALPHA = 1.0 / 137.036
ALPHA_C = 3.0 * ALPHA
K = math.log(1.0 + math.pi / (2.0 * ALPHA_C)) / math.pi
AS_MEAS = 2.100e-9
AS_TOL = 0.01


def main() -> None:
    print("=" * 78)
    print("The amplitude closed form, priced: the declared-grammar scan")
    print("=" * 78)
    print(f"\n   k = ln(1 + π/2α_c)/π = {K:.5f};  recorded form value: "
          f"{(ALPHA_C / (4 * math.pi * K)) ** 3:.4e}")

    hits = []
    total = 0
    for coup_name, coup in (("α", ALPHA), ("α_c", ALPHA_C)):
        for p, q, r, d in itertools.product((1, 2), (-1, 0, 1), (0, 1, 2), (1, 2, 3, 4)):
            base = (coup ** p) * (K ** q) / ((4 * math.pi) ** r)
            for s_name, s in (("1/3", 1 / 3), ("1/2", 0.5), ("1", 1.0),
                              ("2", 2.0), ("3", 3.0), ("π", math.pi),
                              ("1/π", 1 / math.pi)):
                total += 1
                F = s * base ** d
                if abs(F / AS_MEAS - 1.0) < AS_TOL:
                    hits.append((coup_name, p, q, r, d, s_name, F))
    print(f"\n   grammar size: {total} forms;  hits within ±1%: {len(hits)}")
    for h in hits:
        print(f"   {h[5]}·({h[0]}^{h[1]}·k^{h[2]}/(4π)^{h[3]})^{h[4]} = {h[6]:.4e}"
              f"   ({100*(h[6]/AS_MEAS - 1):+.2f}%)")
    rate = len(hits) / total

    print(f"\n   hit rate: {100*rate:.2f}% — the chance a random grammar member")
    print("   lands this close. For comparison, landing anywhere within ±1% of a")
    print("   nine-orders-deep target from O(1)–O(10) ingredients requires the")
    print("   exponent structure to be right before the percent-level test begins.")

    print("\nWHAT THE SCAN CANNOT CHEAPEN (the claim's real load)")
    print("   * k is not a dial: three independent determinations agree —")
    print("     gap equation 1.360, closed form 1.36461, amplitude-implied")
    print("     1.3602 ± 0.0064. The concordance is 0.2–0.5%-level and predates")
    print("     any scan; a lucky form does not explain a triple agreement.")
    print("   * the cube is the spatial dimension and 4π the loop factor — the")
    print("     exponents were structural claims before they were fits.")

    print("\nTHE NAMED PATHS (unchanged by the pricing)")
    print("   promote: derive the shot-noise normalization C = 1 (the factor-250")
    print("   convention spread is the obstacle) and resolve the host mismatch")
    print("   (cold Fermi surface reconstruction vs hot Fermi point basement).")
    print("   kill: the k-concordance breaking (any determination leaving the")
    print("   Eliashberg window), or the C-derivation landing ≠ 1.")

    print("\nVERDICT: neither promoted nor killed — PRICED AND HELD. The form's")
    print(f"   grammar-mate hit rate is {100*rate:.2f}%; its load-bearing content is the")
    print("   k triple-concordance and the structural exponents; its residual is")
    print("   the C = 1 identification, owed by the basement. Candidate, exposed,")
    print("   now with its coincidence cost on the record.")
    print("=" * 78)

    assert any(h[0] == "α_c" and h[1] == 1 and h[2] == -1 and h[3] == 1
               and h[4] == 3 and h[5] == "1" for h in hits)
    assert rate < 0.02


if __name__ == "__main__":
    main()
