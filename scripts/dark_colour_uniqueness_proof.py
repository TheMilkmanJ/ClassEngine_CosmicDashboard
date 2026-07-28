"""dark_colour_uniqueness_proof — the dark colour group's uniqueness, closed for ALL N_c (2026-07-28).

WHAT IS RECORDED
  Requiring the dark sector to self-cancel in the finiteness sum gives

      str[k1]_dark = 2*N_f*N_c - 4*(N_c^2 - 1) = 0   =>   N_f = 2(N_c^2 - 1)/N_c

  and the hunt tabulates N_c = 2..6, finds N_f integer only at N_c = 2
  (where it is exactly 3), and concludes "N_c = 2 is the unique colour
  group admitting an integer flavour count."

  A five-row table does not establish uniqueness.  It rules out four
  alternatives.  Nothing in it forbids some larger N_c from landing on an
  integer again, and the claim as written is doing more work than the
  evidence behind it.

THE CLOSURE (elementary, and it makes the table unnecessary)
  Split the expression instead of tabulating it:

      N_f = 2(N_c^2 - 1)/N_c = 2*N_c - 2/N_c

  The first term is an integer for every integer N_c.  So N_f is an
  integer IF AND ONLY IF N_c divides 2 — that is, N_c is 1 or 2.

      N_c = 1 -> N_f = 0 : no gluons, no quarks, the empty theory
      N_c = 2 -> N_f = 3 : the standing assignment

  So SU(2) with three flavours is the unique NONTRIVIAL solution over the
  whole infinite range, not merely the winner of a five-row scan.  The
  same one-liner also shows why the near-misses are near: 2/N_c shrinks,
  so large-N_c values crowd just under the even integer 2*N_c without
  ever reaching it.

WHAT THIS RUN DOES
  states the identity, verifies it symbolically against the original
  form, scans a large range to confirm no further integer solutions
  exist (a check on the argument, not the argument itself), and confirms
  the tabulated row values.
"""
from __future__ import annotations

from fractions import Fraction


def n_f_original(n_c: int) -> Fraction:
    """N_f from the self-cancellation condition, as written in the hunt."""
    return Fraction(2 * (n_c * n_c - 1), n_c)


def n_f_split(n_c: int) -> Fraction:
    """The same quantity, split: 2*N_c - 2/N_c."""
    return Fraction(2 * n_c) - Fraction(2, n_c)


def main() -> None:
    print("=" * 78)
    print("The dark colour group: uniqueness closed for every N_c")
    print("=" * 78)

    print("\n(1) THE IDENTITY  2(N_c^2-1)/N_c = 2*N_c - 2/N_c")
    bad = [n for n in range(1, 2001) if n_f_original(n) != n_f_split(n)]
    print(f"    verified exactly (Fraction arithmetic) for N_c = 1..2000: "
          f"{'identical throughout' if not bad else f'FAILS at {bad[:5]}'}")

    print("\n(2) THE RECORDED TABLE, reproduced")
    print("    N_c :  " + "  ".join(f"{n:>7d}" for n in range(2, 7)))
    print("    N_f :  " + "  ".join(f"{float(n_f_original(n)):>7.4g}"
                                    for n in range(2, 7)))

    print("\n(3) THE ARGUMENT: 2*N_c is always an integer, so N_f is an integer")
    print("    exactly when N_c divides 2.")
    sols = [n for n in range(1, 100001) if n_f_original(n).denominator == 1]
    print(f"    scan N_c = 1..100000 for integer N_f -> {sols}")
    print("    (the scan CONFIRMS the argument; the argument is what proves it,")
    print("     since a scan of any finite range never could)")

    for n in sols:
        nf = n_f_original(n)
        note = ("no gluons (N_c^2-1 = 0), no quarks: the empty theory"
                if n == 1 else "the standing assignment")
        print(f"      N_c = {n} -> N_f = {int(nf)}   [{note}]")

    print("\n(4) WHY THE NEAR-MISSES ARE NEAR")
    print("    N_f = 2*N_c - 2/N_c sits just under the even integer 2*N_c, by")
    print("    2/N_c, which shrinks as N_c grows:")
    for n in (3, 6, 12, 100):
        print(f"      N_c = {n:>3d}: 2*N_c = {2*n:>3d}, short by "
              f"{float(Fraction(2,n)):.4f}")
    print("    so large-N_c values approach an integer without attaining one —")
    print("    the deficit is never zero for N_c > 2.")

    print("\nVERDICT:")
    print("   THE UNIQUENESS IS PROVABLE, NOT MERELY TABULATED. N_f is an")
    print("   integer iff N_c | 2, so the only candidates in the entire")
    print("   infinite range are N_c = 1 (the empty theory, N_f = 0) and")
    print("   N_c = 2 (N_f = 3). SU(2) with three light flavours is the unique")
    print("   nontrivial solution of the self-cancellation condition, and the")
    print("   five-row table can be replaced by one line of divisibility.")
    print("   This STRENGTHENS the recorded claim rather than altering it: the")
    print("   conclusion was right, the warrant behind it was a finite scan.")
    print("=" * 78)


if __name__ == "__main__":
    main()
