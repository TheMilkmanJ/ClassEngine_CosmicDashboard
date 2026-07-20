#!/usr/bin/env python3
"""
Build a CORRELATION-PRESERVING proposal seed for a Cobaya chain.

The failure this fixes (2026-07-20, routeD / conv_desi / zon_disp):
Cobaya's default `learn_proposal_Rminus1_max_early = 30` lets a chain learn its
proposal covariance while R-1 still sits at 8-27 -- i.e. from a chain that has not
converged at all. The learned sigmas came back 10-45x SMALLER than the configured
widths, the chain stopped exploring, and acceptance ran ~97% with the trace not
moving.

Two repairs are possible and they are not equivalent:

  DIAGONAL rebuild   -- take the configs' physical proposal widths, zero correlations.
                        Fixes the step SIZE. Cannot orient a proposal along a
                        degeneracy, so a thin curved ridge still defeats it.
  CORRELATION-PRESERVING (this script) -- take the ridge's ORIENTATION from the
                        chain's own archived covariance, which was learned on its
                        real parameter set, and the MAGNITUDES from the config.
                            C_new = D_phys . R_archived . D_phys
                        Correlations kept, scale corrected. This is the standard
                        bootstrap and it is what repaired routeD and conv_desi
                        (acceptance 97% -> 20.4% / 19.8%).

Caveat, stated because it matters: the archived covariance comes from a chain that
did NOT converge. Its correlations are an estimate, not a measurement. What
justifies using them is that an approximately-right orientation beats no
orientation, which is what the two repaired chains demonstrated -- not a proof that
the ridge is correctly mapped.

Usage:
    python3 scripts/build_chain_seed.py zon_disp
    python3 scripts/build_chain_seed.py zon_disp --from-samples --write

Without --write it prints a report and touches nothing.
"""
import sys
import os
import re
import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_covmat(path):
    with open(path) as fh:
        header = fh.readline()
    names = header.lstrip("#").split()
    C = np.loadtxt(path, skiprows=1)
    if C.shape[0] != len(names):
        raise SystemExit(f"{path}: {C.shape[0]} rows vs {len(names)} names in header")
    return names, C


def read_proposal_widths(yaml_path):
    """Pull `proposal:` values keyed by the parameter block they sit under.

    Deliberately a small hand parser rather than a yaml load: the configs carry
    `lambda` derived-parameter strings that a strict loader chokes on, and we only
    need param -> proposal.
    """
    widths = {}
    current = None
    param_re = re.compile(r"^  ([A-Za-z_][A-Za-z0-9_]*):\s*$")
    prop_re = re.compile(r"^\s+proposal:\s*([0-9.eE+-]+)\s*$")
    for line in open(yaml_path):
        m = param_re.match(line)
        if m:
            current = m.group(1)
            continue
        m = prop_re.match(line)
        if m and current:
            widths[current] = float(m.group(1))
    return widths


def empirical_cov(chain, names):
    """Weighted covariance computed from the chain's SAMPLES.

    Why this exists (zon_disp, 2026-07-20): Cobaya's `.covmat` is what the sampler
    LEARNED, and it only updates a parameter once the learn criterion fires. For
    zon_disp that never happened for `log10_zon` -- the very parameter the chain
    exists to measure -- so its row in the learned covmat is the configured
    proposal width (0.08 exactly) with every off-diagonal exactly zero, while every
    other parameter carries real correlations. Bootstrapping from that file
    reproduces the blindness.

    The SAMPLES know better: 217 distinct log10_zon values were explored, and their
    empirical correlations are substantial (omega_b -0.743, A_planck +0.515). This
    reads the orientation off the samples instead.

    Drops the first half as transient. That is crude, and it is appropriate here
    precisely because the chain never converged -- there is no principled burn-in
    point to use, and the goal is an orientation estimate rather than a posterior.
    """
    path = os.path.join(REPO, "chains", f"cmp_prtoe_{chain}.1.txt")
    if not os.path.exists(path):
        raise SystemExit(f"missing samples: {path}")
    hdr = [l for l in open(path) if l.startswith("#")][0].lstrip("#").split()
    d = np.loadtxt(path)
    missing = [n for n in names if n not in hdr]
    if missing:
        raise SystemExit(f"samples lack columns: {missing}")
    idx = [hdr.index(n) for n in names]
    half = d.shape[0] // 2
    return np.cov(d[half:, idx], rowvar=False, aweights=d[half:, 0]), d.shape[0] - half


def build(chain, write=False, from_samples=False):
    cov_path = os.path.join(REPO, "chains", f"cmp_prtoe_{chain}.covmat")
    yaml_path = os.path.join(REPO, f"cmp_prtoe_{chain}.yaml")
    out_path = os.path.join(REPO, "chains", f"{chain}_seed.covmat")

    for p in (cov_path, yaml_path):
        if not os.path.exists(p):
            raise SystemExit(f"missing: {p}")

    names, C = read_covmat(cov_path)
    widths = read_proposal_widths(yaml_path)

    # Flag any parameter the learned covmat never touched -- these are the ones a
    # naive bootstrap silently fails to help.
    Dl = np.sqrt(np.diag(C))
    Rl = C / np.outer(Dl, Dl)
    offl = Rl.copy()
    np.fill_diagonal(offl, 0)
    never = [n for j, n in enumerate(names) if np.abs(offl[j]).max() < 1e-12]
    if never:
        print(f"!! learned covmat never updated: {', '.join(never)}")
        print("   (zero off-diagonal = configured width passed through, no orientation)")
        if not from_samples:
            print("   -> consider --from-samples, which reads orientation off the chain itself\n")

    if from_samples:
        C, nused = empirical_cov(chain, names)
        print(f"orientation source: EMPIRICAL covariance from {nused} samples "
              f"(second half of the chain)")

    D_arch = np.sqrt(np.diag(C))
    R = C / np.outer(D_arch, D_arch)

    missing = [n for n in names if n not in widths]
    D_phys = np.array([widths.get(n, D_arch[i]) for i, n in enumerate(names)])

    C_new = D_phys[:, None] * R * D_phys[None, :]

    # A correlation matrix from a real covariance is PSD by construction, and
    # rescaling by a positive diagonal preserves that -- but check, because a
    # non-PD seed is silently disastrous inside the sampler.
    eig = np.linalg.eigvalsh(C_new)
    pd = eig.min() > 0

    off = np.abs(R[~np.eye(len(R), dtype=bool)])
    print(f"chain            : {chain}")
    print(f"archived covmat  : {C.shape[0]}x{C.shape[0]}, max|corr| {off.max():.3f}, mean {off.mean():.3f}")
    print(f"proposal widths  : {len(widths) - len(missing)}/{len(names)} matched from the yaml")
    if missing:
        print(f"  NOT in yaml (archived sigma kept): {', '.join(missing)}")
    print(f"scale correction : ratio D_phys/D_archived per parameter")
    ratios = D_phys / D_arch
    for n, r in sorted(zip(names, ratios), key=lambda t: -t[1])[:6]:
        print(f"    {n:<16} {r:8.2f}x")
    print(f"positive-definite: {'YES' if pd else 'NO -- DO NOT USE'} (min eig {eig.min():.3g})")

    if not pd:
        raise SystemExit("refusing to write a non-positive-definite seed")

    if write:
        with open(out_path, "w") as fh:
            fh.write("# " + " ".join(names) + "\n")
            np.savetxt(fh, C_new)
        print(f"\nwritten          : {out_path}")
        print("  Point the chain's yaml at it with  covmat: chains/"
              f"{chain}_seed.covmat")
        print("  and set  learn_proposal_Rminus1_max_early: 2.0  (default 30 is the bug).")
    else:
        print("\n(dry run -- pass --write to save)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    build(sys.argv[1], write="--write" in sys.argv,
          from_samples="--from-samples" in sys.argv)
