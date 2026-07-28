"""nested_run_cluster_sizing — what hardware actually makes the evidence run finish (2026-07-28).

WHY THIS EXISTS
  The nested run was ended on cost (#99): 66 s per likelihood evaluation
  against 534 slice steps per iteration is 9.8 h per nested iteration, so
  the 1809-iteration reference run is 736 days and the LCDM twin doubles
  it.  The corpus records that cost.  It does not record the inverse —
  what hardware makes it affordable — which is the number needed before
  any cluster is bought.

  This script computes that from the recorded numbers plus the recorded
  sampler configuration, and reports the two free levers that should be
  pulled BEFORE hardware, because either is worth more than a modest
  cluster.

THE RECORDED INPUTS
  * 66 s per likelihood evaluation, 534 slice steps per iteration, 1809
    iterations for the reference run, LCDM twin doubling the total
    (REFEREE_CALENDAR, the evidence-route block).
  * nlive = 200, num_repeats = 24, ndim = 12 (cmp_prtoe_fixed_*.yaml).

THE CEILING THAT MATTERS FOR PROCUREMENT
  PolyChord parallelises over its live points: slaves generate candidate
  replacements while the master maintains the live set.  Useful scaling
  is therefore bounded by nlive, and degrades well before reaching it.
  With nlive = 200, cores beyond ~200 buy nothing.  Raising nlive raises
  the ceiling but raises total work in proportion, so it does not help
  wall-clock at fixed budget.  **The configuration, not the wallet, sets
  the maximum useful machine.**
"""
from __future__ import annotations

SEC_PER_LIKE = 66.0
SLICE_STEPS = 534
ITERS_REF = 1809
NLIVE, NUM_REPEATS, NDIM = 200, 24, 12
YEAR_S = 365.25 * 24 * 3600


def core_years(sec_per_like=SEC_PER_LIKE, iters=ITERS_REF, both=True):
    evals = iters * SLICE_STEPS * (2 if both else 1)
    return evals * sec_per_like / YEAR_S, evals


def main() -> None:
    print("=" * 78)
    print("Sizing the machine for the nested evidence run")
    print("=" * 78)

    cy, evals = core_years()
    print(f"\n   reference run + LCDM twin: {evals:,} likelihood evaluations")
    print(f"   at the recorded {SEC_PER_LIKE:.0f} s each  ->  {cy:.2f} CORE-YEARS")

    print("\n   wall clock vs machine size (eta = parallel efficiency):")
    print("     cores   eta    effective   wall clock for the PAIR")
    for n, eta in ((16, 0.85), (32, 0.80), (64, 0.75), (128, 0.70), (200, 0.60)):
        eff = n * eta
        days = cy * 365.25 / eff
        print(f"     {n:5d}  {eta:.2f}     {eff:6.1f}      {days:6.1f} days")

    print(f"\n   THE CEILING: nlive = {NLIVE}, so PolyChord cannot usefully employ")
    print(f"   more than ~{NLIVE} cores. Beyond that, spending buys nothing unless")
    print("   nlive rises — and raising nlive raises total work proportionally,")
    print("   so it does not shorten wall clock at fixed budget. A ~64-core")
    print("   workstation sits in the right place; a large cluster does not.")

    print("\n   THE TWO FREE LEVERS, both worth more than a modest machine:")
    print(f"\n   (1) THE LIKELIHOOD AT {SEC_PER_LIKE:.0f} s IS THE DOMINANT COST and is")
    print("       slow for a CLASS-class evaluation. Every factor pulled out of")
    print("       it multiplies straight through:")
    for s in (66.0, 30.0, 10.0, 5.0):
        c, _ = core_years(sec_per_like=s)
        print(f"         {s:5.1f} s/like  ->  {c:5.2f} core-years"
              f"   ({66.0/s:4.1f}x cheaper)")
    print("       Profiling it before buying hardware is the highest-return")
    print("       hour available: 66 -> 10 s is worth more than 6x the cores,")
    print("       and costs nothing.")

    print(f"\n   (2) num_repeats = {NUM_REPEATS} is {NUM_REPEATS/NDIM:.0f}x ndim, a deliberately")
    print("       conservative setting. PolyChord's own guidance is that")
    print("       num_repeats ~ 2*ndim is adequate for evidence and ~5*ndim for")
    print("       well-sampled posteriors; the cost is linear in it, so the")
    print("       setting is already near the economical end and there is")
    print("       little to reclaim here. Recorded so it is not mistaken for")
    print("       slack.")

    print("\nVERDICT:")
    print("   The evidence pair is a ~4 core-year job, not a supercomputer job.")
    print("   At 64 cores it is about a month; at 128, about two weeks; and")
    print("   past ~200 cores the live-point count caps the return. So the")
    print("   purchase that matches this problem is a single many-core node,")
    print("   not a cluster.")
    print()
    print("   But the ordering matters more than the size: the likelihood's")
    print("   66 s is the dominant term and is the one input here that has not")
    print("   been optimised. Profile it first. A 6x speedup there costs")
    print("   nothing and beats the machine this calculation would otherwise")
    print("   justify buying.")
    print("=" * 78)


if __name__ == "__main__":
    main()
