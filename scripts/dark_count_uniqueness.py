"""dark_count_uniqueness — task #7: the colour/flavour count, checked and licensed (2026-07-27).

THE RECORDED CANDIDATE
  Pauli finiteness for the dark sector: str[k₁] = 2·N_f·N_c − 4(N_c² − 1) = 0,
  claimed to force SU(2) with N_f = 3 as the unique integer solution.

THREE CHECKS
  1. UNIQUENESS, made exact.  N_f = 2(N_c² − 1)/N_c = 2N_c − 2/N_c is an
     integer iff N_c divides 2.  N_c = 1 is trivial (no gauge bosons, N_f = 0);
     N_c = 2 gives N_f = 3.  Unique for ALL N_c, not just a scanned range —
     a divisibility fact, verified by scan below anyway.
  2. THE REPRESENTATION CONDITION, named.  The arithmetic assumes fundamental
     flavours.  With adjoint flavours the condition reads
     2·N_f·(N_c²−1) − 4(N_c²−1) = 0 ⟹ N_f = 2 for EVERY N_c — a degenerate
     alternative family.  So uniqueness is CONDITIONAL on the fundamental
     assignment, which the corpus's own structure supports twice over: the
     flavours are lepton-partnered (the electron-mass field's chiral
     condensate), and the recorded diquark consilience (SU(2) baryons are
     diquarks) is a fundamental-rep statement.  Condition named, not hidden.
  3. THE DEMAND ITSELF, licensed.  With a physical cutoff, divergence
     cancellation is not automatic — it needs a reason.  The corpus records
     one: the vacuum-energy budget is capped at the pairing gap by a
     no-double-counting constraint (the cosmological-constant accounting).
     An uncancelled quadratic supertrace in the dark sector would contribute
     cutoff-scale zero-point energy and break that cap.  So str[k₁] = 0 is
     not an aesthetic naturalness wish — it is REQUIRED by the recorded
     vacuum accounting, at the same argument grade as the cap itself.

GRADE RULE
  Arithmetic exact; the rep condition and the cap-licensing are argument
  grade with conditions named.  The external referee is unchanged: the
  SU(2), N_f = 3 lattice campaign.  Nothing promoted.
"""
from __future__ import annotations


def str_fund(nc: int, nf: int) -> int:
    return 2 * nf * nc - 4 * (nc * nc - 1)


def main() -> None:
    print("=" * 78)
    print("The dark colour/flavour count: uniqueness exact, demand licensed")
    print("=" * 78)

    print("\n1. Fundamental flavours: integer solutions of 2·N_f·N_c = 4(N_c²−1)")
    sols = []
    for nc in range(2, 51):
        num = 2 * (nc * nc - 1)
        if num % nc == 0:
            sols.append((nc, num // nc))
    for nc, nf in sols:
        print(f"   N_c = {nc}:  N_f = {nf}   (str = {str_fund(nc, nf)})")
    print("   divisibility proof: N_f = 2N_c − 2/N_c ∈ ℤ ⟺ N_c | 2 — unique for")
    print("   all N_c, not just the scan.")

    print("\n2. The representation condition (named):")
    print("   adjoint flavours give N_f = 2 for EVERY N_c — a degenerate family.")
    print("   Uniqueness is conditional on fundamental flavours, supported by the")
    print("   lepton-partnering of the flavours and the recorded diquark")
    print("   consilience. A future adjoint-flavour reading would void the count.")

    print("\n3. The demand licensed by the recorded vacuum cap:")
    print("   an uncancelled quadratic supertrace contributes cutoff-scale")
    print("   zero-point energy; the corpus's cosmological-constant accounting")
    print("   caps the vacuum at the pairing gap by no-double-counting. The")
    print("   finiteness condition is therefore required by recorded bookkeeping,")
    print("   not wished for by naturalness.")

    print("\n4. The consistency web (recorded, cross-checked):")
    print("   τ needs N_f ≥ 2                      — satisfied (3)")
    print("   SU(2) baryons are diquarks           — fundamental-rep consilience")
    print("   ΔN_eff re-priced at N_c = 2          — recorded (sign changed)")
    print("   ring stability favors medium-inertia — carrier fork, compatible")
    print("   lattice referee                      — SU(2) N_f = 3 campaign, unchanged")

    print("\nVERDICT: the count SU(2), N_f = 3 is now (i) exactly unique given the")
    print("   named fundamental-rep condition, and (ii) demanded by the recorded")
    print("   vacuum accounting rather than by taste. Grade: candidate → licensed")
    print("   candidate with two named conditions (rep assignment; cap scope).")
    print("   The lattice campaign remains the referee. Not derived.")
    print("=" * 78)

    assert sols == [(2, 3)]
    assert str_fund(2, 3) == 0
    assert all((2 * (nc * nc - 1)) % nc != 0 for nc in range(3, 51))


if __name__ == "__main__":
    main()
