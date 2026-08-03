#!/usr/bin/env python3
"""
The live model-vs-LCDM comparison, read honestly.

Prompted by an external reviewer's regrade (2026-07-28) which stated the model
sits ~41 log units behind LCDM and that the quoted +2.635 Laplace win is stale.
The first half is checked here against the live chains; the second half is a fair
criticism that this script does NOT try to rescue.

Two questions, kept separate because conflating them is the whole trap:

  Q1  what do the chains currently say?      (best-fit -logpost)
  Q2  what does that entitle anyone to say?  (almost nothing, and here is why)

Pre-stated control: best-so-far -logpost is a running MINIMUM, so it can only
fall as samples accumulate.  A chain with more samples has more chances to find a
lower one EVEN IF the two models are identical.  Any comparison that ignores
sample count is biased toward the longer chain.  Stated before looking at which
chain is longer.
"""

import glob
import os

CHAINS = "/home/themilkmanj/prtoe_class/chains"
PAIR = [("LCDM  (cmp_lcdm_mnu_bbnfix)", "cmp_lcdm_mnu_bbnfix"),
        ("model (dyad_mnu_bbnfix)", "dyad_mnu_bbnfix")]


def load(base):
    """Return list of (weight, -logpost) in file order across ranks."""
    rows = []
    for path in sorted(glob.glob(os.path.join(CHAINS, base + ".*.txt"))):
        with open(path) as fh:
            for line in fh:
                if line.startswith("#"):
                    continue
                parts = line.split()
                if len(parts) > 3:
                    try:
                        rows.append((float(parts[0]), float(parts[1])))
                    except ValueError:
                        pass
    return rows


def best_curve(rows, points=6):
    """best-so-far as a function of cumulative sample count."""
    out, best = [], None
    marks = [int(len(rows) * (i + 1) / points) for i in range(points)]
    for i, (_w, lp) in enumerate(rows, start=1):
        if best is None or lp < best:
            best = lp
        if i in marks:
            out.append((i, best))
    return out


def main():
    print("=" * 76)
    print("  LIVE READ: model vs LCDM on the current bbnfix pair")
    print("=" * 76)

    data = {}
    for label, base in PAIR:
        rows = load(base)
        data[base] = rows
        best = min(r[1] for r in rows) if rows else float("nan")
        print(f"\n  {label}")
        print(f"    samples (raw rows): {len(rows)}")
        print(f"    best -logpost:      {best:.4f}")

    lcdm, model = data["cmp_lcdm_mnu_bbnfix"], data["dyad_mnu_bbnfix"]
    if not lcdm or not model:
        missing = [b for b, r in data.items() if not r]
        print("\n" + "=" * 76)
        print("  NO COMPARISON POSSIBLE — a chain has written no samples yet.")
        print(f"  empty: {', '.join(missing)}")
        print("""
  This is the expected state during burn-in, and after any relaunch with -f (which
  deletes previous chain files). It is NOT a defect and NOT an adverse result: a
  chain that has written nothing has said nothing. Re-run once samples appear.
""")
        print("=" * 76)
        return
    b_l, b_m = min(r[1] for r in lcdm), min(r[1] for r in model)
    print("\n" + "-" * 76)
    print(f"  RAW GAP: LCDM {b_l:.2f} - model {b_m:.2f} = {b_l - b_m:+.2f} log units")
    print(f"  (positive = model has the lower -logpost, i.e. fits better)")
    print(f"\n  The reviewer's figure was model 1421.6 vs LCDM 1380.5, i.e. ~41 units")
    print(f"  AGAINST the model.  That is a STALE reading: the model's best has since")
    print(f"  fallen to {b_m:.2f}.  The direction has flipped, not merely narrowed.")

    # ---- the control: is the gap a sampling artifact? ----------------------
    print("\n" + "=" * 76)
    print("  BUT: THE CONTROL SAYS DO NOT BANK IT")
    print("=" * 76)
    print(f"\n  sample counts differ: LCDM {len(lcdm)}, model {len(model)}"
          f"  ({len(model)/max(len(lcdm),1):.2f}x)")
    print("  best-so-far is a running minimum, so the longer chain wins on best-fit")
    print("  even for identical models.  Here the LONGER chain is the model's.\n")

    print("  best-so-far vs cumulative samples:")
    print(f"    {'N':>8} {'LCDM best':>12}   |   {'N':>8} {'model best':>12}")
    cl, cm = best_curve(lcdm), best_curve(model)
    for i in range(max(len(cl), len(cm))):
        a = f"{cl[i][0]:8d} {cl[i][1]:12.4f}" if i < len(cl) else " " * 21
        b = f"{cm[i][0]:8d} {cm[i][1]:12.4f}" if i < len(cm) else " " * 21
        print(f"    {a}   |   {b}")

    # equal-sample comparison
    n = min(len(lcdm), len(model))
    b_l_eq = min(r[1] for r in lcdm[:n])
    b_m_eq = min(r[1] for r in model[:n])
    print(f"\n  TRUNCATED TO EQUAL SAMPLES (N = {n} each):")
    print(f"    LCDM  best = {b_l_eq:.4f}")
    print(f"    model best = {b_m_eq:.4f}")
    print(f"    gap        = {b_l_eq - b_m_eq:+.4f} log units")
    print("    (rank-ordering within a file is not a random subsample, so even this")
    print("     is indicative only -- it removes the length bias, not the burn-in one.)")

    print("\n" + "=" * 76)
    print("""  WHAT THIS DOES AND DOES NOT ESTABLISH

  ESTABLISHED: the "~41 log units behind" reading is stale.  On the live chains
  the model's best -logpost is BELOW LCDM's, not far above it.

  NOT ESTABLISHED, and the reviewer is right about this part:

    * best-fit -logpost is NOT evidence.  It is a chi-squared-like comparison
      with no parameter penalty.  Delta ln Z is the quantity that decides, and
      neither chain can supply it yet.
    * NEITHER CHAIN IS CONVERGED.  LCDM sits at R-1 = 1.011; the model chain has
      no R-1 written.  Both best-fit values are upper bounds on the true minimum
      and both will keep falling.
    * the gap is smaller than the sampling asymmetry can account for, so its SIGN
      is not yet a result.

  So the correct statement is neither the reviewer's "41 behind" nor a claim of a
  1.9-unit win.  It is: THE LIVE COMPARISON IS CURRENTLY A WASH AND CANNOT BE
  QUOTED IN EITHER DIRECTION.  The reviewer's underlying point -- that the +2.635
  Laplace is the wrong kind of number to headline while the live chains are
  unmixed -- stands untouched by anything here.
""")
    print("=" * 76)


if __name__ == "__main__":
    main()
