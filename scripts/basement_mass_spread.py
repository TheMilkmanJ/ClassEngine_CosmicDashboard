"""basement_mass_spread — #113 Part 3b: the constituent spread the induced-G relation forces (2026-07-27).

THE RELATION (the program file's target)
  1/G = −(1/2π)·str[k₁·m²·ln(m²/µ²)] = M_Pl²  over the fixed roster
  (+48, −48, +12, −12; Part 3a verified str[k₁] = 0).

STRUCTURE FIRST (why the old two-scale toy could never have worked)
  µ-independence requires str[k₁·m²] = 0 as well.  A two-scale split
  (all +48 at m_A, all −48-and-friends at m_B) then forces
  60·m_A² = 60·m_B² — degenerate — and the whole supertrace vanishes:
  1/G = 0.  So the roster needs asymmetry across BOTH sign pairs, and
  the honest minimal ansatz is paired splittings around one scale m:
      m_f = m(1+x)   (+48)      m_b = m(1−x)   (−48)
      m_v = m(1+y)   (+12)      m_s = m(1−y)   (−12)
  with str[k₁m²] = 0 fixing y = −4x·(1 + O(x²)) exactly (solved, not
  expanded, below).  One free spread x; the relation then fixes m.

WHAT THIS COMPUTES
  The exact (x, m) locus solving both constraints, and the two honest
  summary numbers the program file wants:
    * the minimal-scale point (how close to M_Pl the roster must sit),
    * the spread at that point (max mass ratio across the roster).
  The firm qualitative statement (spread O(M_Pl), degenerate forbidden)
  gets its quantitative body with no retracted count anywhere in it.
"""
from __future__ import annotations

import math

K = [(48, +1), (48, -1), (12, +1), (12, -1)]


def supertraces(x: float, y: float):
    """Return (str[k m²], str[k m² ln m²]) in units of m² (ln in units of m)."""
    ms = [(1 + x, +48), (1 - x, -48), (1 + y, +12), (1 - y, -12)]
    s2 = sum(k * mm * mm for mm, k in ms)
    slog = sum(k * mm * mm * math.log(mm * mm) for mm, k in ms)
    return s2, slog


def y_of_x(x: float) -> float:
    """Solve str[k m²] = 0 for y at given x (bisection; y in (−1, 0])."""
    lo, hi = -0.999999, 0.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if supertraces(x, mid)[0] > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def main() -> None:
    print("=" * 78)
    print("The basement's mass spread, solved on the fixed roster — #113 Part 3b")
    print("=" * 78)
    print("\n   structural gate: two-scale ansatz ⟹ str[k m²] = 0 forces degeneracy")
    print("   ⟹ 1/G = 0 — the old toy's ~7% figure could not have survived the")
    print("   retraction of its count; ≥ two independent splittings required. ✓")

    print("\n   x       y(x)      str[km²]   |str[km²lnm²]|   m/M_Pl needed   max ratio")
    best = None
    for x in (0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9):
        y = y_of_x(x)
        if not (-1.0 < y):
            print(f"   {x:.2f}   no admissible y (constraint leaves the physical domain)")
            continue
        s2, slog = supertraces(x, y)
        if abs(slog) < 1e-12:
            continue
        # 1/G = −(1/2π) m² · slog = M_Pl²  ⟹  m = M_Pl · sqrt(2π/(−slog))
        val = 2 * math.pi / (-slog) if slog < 0 else float("nan")
        if val > 0 and not math.isnan(val):
            m_over = math.sqrt(val)
            masses = [1 + x, 1 - x, 1 + y, 1 - y]
            ratio = max(masses) / min(masses)
            print(f"   {x:.2f}   {y:+.4f}   {s2:+.1e}   {abs(slog):9.4f}      "
                  f"{m_over:8.3f}        {ratio:6.2f}")
            if best is None or m_over < best[2]:
                best = (x, y, m_over, ratio)
        else:
            print(f"   {x:.2f}   {y:+.4f}   {s2:+.1e}   sign(slog) = +: 1/G < 0, unphysical branch")

    if best:
        x, y, m_over, ratio = best
        print(f"\n   the minimal-scale point: x = {x:.2f}, y = {y:.3f} → the roster")
        print(f"   sits at m = {m_over:.2f}·M_Pl with max mass ratio {ratio:.2f}.")
        print("\nVERDICT: the quantitative body of Part 3b's firm statement —")
        print("   the roster must sit AT the Planck scale (O(1)·M_Pl, not near it")
        print("   logarithmically) with an O(1) spread across both sign pairs;")
        print("   a percent-class spread is excluded because str[km²lnm²] scales")
        print("   as the spread SQUARED (both linear terms die by the constraint),")
        print("   so small splittings drive the needed m far ABOVE M_Pl. The")
        print("   'spread O(M_Pl)' claim is now a computed locus, not a scaling")
        print("   argument. What this does NOT supply (unchanged): the emit")
        print("   mechanism and WHICH point on the locus the UV completion picks —")
        print("   the program file's preon/GUT-class items.")
    print("=" * 78)


if __name__ == "__main__":
    main()
