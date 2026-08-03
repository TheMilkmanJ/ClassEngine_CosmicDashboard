#!/usr/bin/env python3
"""
Adjudicate the 3D toroidal fork against the criterion pre-registered at t = 6.25/8.

WRITTEN BEFORE THE RUN FINISHED, deliberately. The acceptance note was recorded
in the run log at t = 6.25 on the n = -1 branch; this script mechanises it so the
verdict is read off rather than argued after the answer is visible.

THE PRE-REGISTERED CRITERION (run log, "PRE-REGISTERED ACCEPTANCE NOTE"):

  * the branch E-drift asymmetry is common-mode and measured at 0.029% worst
    case -- the drift belongs to the integrator, not the winding sign;
  * (A) shape helicity is INTEGER-VALUED, so a 0.029% common-mode asymmetry
    cannot move it. An exact pair sum of 0 is ROBUST;
  * (B) core-circuit winding is CONTINUOUS. Its pair-sum residual must be
    compared to the asymmetry: a residual >> 0.029% of the typical magnitude is
    a real feature, not numerical noise;
  * NO ABSOLUTE ENERGETIC QUANTITY may be quoted from this run at any point.

COMMITTED CONSEQUENCE: if (A) flips exactly and (B) fails its pair sum, reading
(A) survives and reading (B) is falsified on its own pair sum. If (A)'s flip
fails, neither survives and the fault is in the construction.
"""

import os
import re
import sys

LOG = ("/home/themilkmanj/prtoe_class/docs/working_logs/_runs/"
       "toroidal_fork_3d_2026-07-28.log")
ASYM_PCT = 0.0294   # worst-case relative branch asymmetry, measured over 24 frames


def parse(path):
    """Extract (A) helicity and (B) winding for each branch, plus frame coverage."""
    txt = open(path).read()
    out = {}

    # compact form:  [n=-1 FIRST RING at t = 1.00: helA +1, W +1.87]
    for m in re.finditer(r"\[n=([+-])1 FIRST RING at t = ([0-9.]+): helA ([+-]?\d+), "
                         r"W ([+-]?[0-9.]+)\]", txt):
        s = m.group(1) + "1"
        out.setdefault(s, {}).update(t=float(m.group(2)),
                                     helA=int(m.group(3)),
                                     W=float(m.group(4)))

    # verbose form: "n = +1: ring at t = ..." then (A)/(B) lines
    for m in re.finditer(r"n = ([+-])1: ring at t = ([0-9.]+).*?\(A\) shape helicity: "
                         r"([+-]?\d+).*?\(B\) core-circuit winding W = ([+-]?[0-9.]+)",
                         txt, re.S):
        s = m.group(1) + "1"
        out.setdefault(s, {}).update(t=float(m.group(2)),
                                     helA=int(m.group(3)),
                                     W=float(m.group(4)))

    frames = {}
    for m in re.finditer(r"\[n=([+-])1 t=\s*([0-9.]+)", txt):
        frames.setdefault(m.group(1) + "1", set()).add(float(m.group(2)))
    return out, frames


def main():
    if not os.path.exists(LOG):
        print("log not found"); sys.exit(1)
    r, frames = parse(LOG)

    print("=" * 74)
    print("  3D TOROIDAL FORK — verdict against the pre-registered criterion")
    print("=" * 74)

    for s in ("+1", "-1"):
        f = sorted(frames.get(s, []))
        span = f"{min(f):.2f} -> {max(f):.2f}" if f else "none"
        got = r.get(s)
        print(f"\n  branch n = {s}:  frames {len(f)} ({span})")
        if got:
            print(f"    (A) shape helicity      = {got['helA']:+d}")
            print(f"    (B) core-circuit W      = {got['W']:+.3f}   (at t = {got['t']:.2f})")
        else:
            print("    no ring readings parsed yet")

    if not ({"+1", "-1"} <= set(r)):
        print("\n  BOTH BRANCHES NOT YET READ — run still in progress; no verdict.")
        return

    p, n = r["+1"], r["-1"]

    print("\n" + "-" * 74)
    print("  READING (A) — shape helicity, INTEGER-VALUED")
    sA = p["helA"] + n["helA"]
    print(f"    {p['helA']:+d} and {n['helA']:+d}  ->  pair sum {sA:+d}")
    a_ok = (sA == 0) and (p["helA"] != n["helA"])
    print(f"    exact flip, pair sum zero: {'YES' if a_ok else 'NO'}")
    print(f"    an integer cannot be moved by a {ASYM_PCT}% common-mode asymmetry,")
    print(f"    so this outcome is robust by construction.")

    print("\n  READING (B) — core-circuit winding, CONTINUOUS")
    sB = p["W"] + n["W"]
    mag = (abs(p["W"]) + abs(n["W"])) / 2
    relB = 100 * abs(sB) / mag if mag else float("nan")
    print(f"    {p['W']:+.3f} and {n['W']:+.3f}  ->  pair sum {sB:+.3f}")
    print(f"    residual is {relB:.1f}% of typical magnitude {mag:.3f}")
    print(f"    exceeds the {ASYM_PCT}% branch asymmetry by {relB/ASYM_PCT:,.0f}x")
    b_ok = relB < 1.0

    print("\n" + "=" * 74)
    if a_ok and not b_ok:
        print("""  VERDICT — as pre-committed:

    (A) SURVIVES. The shape helicity flips exactly with the winding sign, and
        being integer-valued it is immune to the run's energy drift.
    (B) FALSIFIED ON ITS OWN PAIR SUM. The residual is orders above the
        numerical asymmetry, so it is a real property of the configuration and
        cannot be rescued by a finer integrator.

  This is the outcome the acceptance note committed to in advance.""")
    elif not a_ok:
        print("""  VERDICT — the surprise branch, also pre-committed:

    (A)'s exact flip DID NOT HOLD. Neither reading survives, and the failure is
    in the construction rather than the arithmetic. This was written down as the
    genuine-surprise case before the run completed and must be reported as such.""")
    else:
        print("""  VERDICT: both readings pair-sum cleanly. Not an outcome the note
  anticipated -- do not adjudicate from this script alone; re-open the fork.""")
    print("""
  NOT LICENSED by this run, restated: any statement about energy, action or
  stability; any comparison against a run with different integrator settings;
  and any claim that (B) would pass at higher resolution.""")
    print("=" * 74)


if __name__ == "__main__":
    main()
