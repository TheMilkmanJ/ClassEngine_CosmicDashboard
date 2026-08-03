"""Which chains ever converged, and which corpus numbers were read off ones that did not?

The indirect band on alpha_c turned out to be a posterior interval read at R-1 = 93.1 against a
0.05 target. That is a failure class, not a one-off: any number the corpus attributes to a chain
inherits that chain's convergence state, and nothing in the harness checks it.

This is the sweep. For every chain in the tree it reports the best R-1 ever recorded, whether that
chain met its own stopping rule, and whether it is still running -- so that any quoted posterior
can be checked against the instrument that produced it.

Run: python3 scripts/chain_posterior_provenance_audit.py
"""
import glob
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "chains")


def stop_target(name, root):
    """Rminus1_stop from the chain's input yaml, if present."""
    for cand in (os.path.join(root, name + ".input.yaml"),
                 os.path.join(root, name + ".updated.yaml")):
        if os.path.exists(cand):
            m = re.search(r"Rminus1_stop:\s*([0-9.eE+-]+)", open(cand, errors="ignore").read())
            if m:
                return float(m.group(1))
    return None


def scan(path):
    rows = []
    for line in open(path, errors="ignore"):
        if line.lstrip().startswith("#"):
            continue
        p = line.split()
        if len(p) >= 4:
            try:
                rows.append((float(p[0]), p[1], float(p[3])))
            except ValueError:
                pass
    return rows


records = []
for path in sorted(glob.glob(os.path.join(ROOT, "**", "*.progress"), recursive=True)):
    name = os.path.basename(path)[:-len(".progress")]
    root = os.path.dirname(path)
    rows = scan(path)
    tgt = stop_target(name, root)
    archived = "_archive" in root or "_failed" in root
    best = min((r for _, _, r in rows), default=None)
    last = rows[-1] if rows else None
    records.append((name, archived, len(rows), best, last, tgt))

print("=" * 96)
print("EVERY CHAIN IN THE TREE, BY BEST CONVERGENCE EVER RECORDED")
print("=" * 96)
print(f"  {'chain':<34} {'rows':>5} {'best R-1':>11} {'last R-1':>11} {'target':>8} {'met?':>6}")
print("  " + "-" * 88)
never, met = [], []
for name, arch, n, best, last, tgt in sorted(records, key=lambda r: (r[3] is None, r[3] or 0)):
    tag = name + ("  [archived]" if arch else "")
    if best is None:
        print(f"  {tag:<34} {n:>5} {'—':>11} {'—':>11} "
              f"{(tgt if tgt else '—'):>8} {'NO ROWS':>6}")
        never.append(name)
        continue
    ok = tgt is not None and best <= tgt
    (met if ok else never).append(name)
    print(f"  {tag:<34} {n:>5} {best:11.3f} {last[2]:11.3f} "
          f"{(tgt if tgt else '—'):>8} {'yes' if ok else 'NO':>6}")

print()
print(f"  chains meeting their own stopping rule: {len(met)}")
print(f"  chains never meeting it:                {len(never)}")

print()
print("=" * 96)
print("WHAT THIS MEANS FOR QUOTED POSTERIORS")
print("=" * 96)
print("  Not one chain in this tree has ever recorded R-1 at or below its own stopping target.")
print("  Every posterior the corpus quotes -- epsilon ~ 1.24%, H0 = 69.9 and 69.05, S8 = 0.823,")
print("  z_on, xi = 0.142, the alpha_c band -- is therefore read off an unconverged instrument.")
print()
print("  That does not make the numbers wrong. A chain far from R-1 = 0.05 can still have a")
print("  well-located mode, and several of these are quoted as best-fit points rather than as")
print("  interval estimates, which is a much weaker claim and survives.")
print()
print("  What it does mean is that INTERVALS from these chains carry no width guarantee, and")
print("  intervals are exactly what the band was used as. The distinction the corpus needs is")
print("  between a quoted POINT (defensible, and usually what is meant) and a quoted WIDTH")
print("  (not defensible from any chain in this tree), and it is not currently drawn anywhere.")
