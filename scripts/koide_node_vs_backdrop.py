#!/usr/bin/env python3
"""
Is the condensate a NODE of the family graph, or a BACKDROP?   (docket #1)

GRADE STATED BEFORE COMPUTING (protocol check 33)
-------------------------------------------------
Evidence class: STRUCTURAL. Nothing here confirms the model against data.

T6 reduced the democratic mechanism's two premises to one. (P2), cross-type coupling
equality, follows from (P1) plus an ordering: if the condensate is a node of the same
graph then the structure is K_4, K_4 is edge-transitive, so one coupling is FORCED
rather than chosen, and the medium's distinguished role enters through the STATE (it
is pinned) rather than through the couplings. Symmetric dynamics, symmetry-broken state.

So everything rests on (P1). This script does not decide (P1) -- that is a structural
choice about the constituent level, not a desk computation. What it does is make (P1)
CONCRETE by asking: are the two options even distinguishable, and by what?

What would count as success: a clean discriminant separating node from backdrop.
What would count as a null: the two give identical spectra, in which case (P1) is
undecidable from this direction and the risk cannot be reduced here.
What is NOT claimed: that the condensate IS a node. That remains open and is the
single premise the Q = 2/3 mechanism rests on.
"""

import math
import itertools

CHECKS = []
def chk(name, got, booked, tol, unit=""):
    ok = abs(got) <= tol if booked == 0 else abs(got - booked) / abs(booked) <= tol
    CHECKS.append((ok, name, booked, got, unit))

def eigenvalues(M):
    """Symmetric 4x4 eigenvalues by Jacobi rotation -- no numpy dependency."""
    A = [row[:] for row in M]
    n = len(A)
    for _ in range(200):
        off = max(((abs(A[i][j]), i, j) for i in range(n) for j in range(n) if i != j))
        if off[0] < 1e-14:
            break
        _, p, q = off
        if abs(A[p][p] - A[q][q]) < 1e-30:
            theta = math.pi / 4
        else:
            theta = 0.5 * math.atan2(2 * A[p][q], A[p][p] - A[q][q])
        c, s = math.cos(theta), math.sin(theta)
        B = [row[:] for row in A]
        for k in range(n):
            B[p][k] = c * A[p][k] + s * A[q][k]
            B[q][k] = -s * A[p][k] + c * A[q][k]
        A2 = [row[:] for row in B]
        for k in range(n):
            A2[k][p] = c * B[k][p] + s * B[k][q]
            A2[k][q] = -s * B[k][p] + c * B[k][q]
        A = A2
    return sorted(A[i][i] for i in range(n))

def hessian(a, b):
    """Graph Hessian (Laplacian) for 3 faces + 1 medium.
       a = face-face bond, b = face-medium bond.  a = b is the K_4 democratic case."""
    W = [[0.0] * 4 for _ in range(4)]
    for i, j in itertools.combinations(range(3), 2):
        W[i][j] = W[j][i] = a
    for i in range(3):
        W[i][3] = W[3][i] = b
    L = [[0.0] * 4 for _ in range(4)]
    for i in range(4):
        L[i][i] = sum(W[i])
        for j in range(4):
            if i != j:
                L[i][j] = -W[i][j]
    return L

print("=" * 76)
print("NODE OR BACKDROP: IS THERE A DISCRIMINANT?")
print("=" * 76)

# ---------------------------------------------------------------- 1. the two spectra
print("\n[1] The spectrum, both ways")
print("    Nodes: three faces + the medium. Two bond types:")
print("      a = face-face,  b = face-medium.  The democratic case is a = b (K_4).\n")

print("    Analytic result (derived below, verified numerically):")
print("      eigenvalues = { 0,  3a+b (x2),  4b (x1) }\n")

print("      case                     a      b        spectrum")
for lab, a, b in [("democratic (K_4)", 1.0, 1.0),
                  ("backdrop, weak bond", 1.0, 0.4),
                  ("backdrop, strong bond", 1.0, 2.5),
                  ("backdrop, b -> 0", 1.0, 1e-9)]:
    ev = eigenvalues(hessian(a, b))
    print(f"      {lab:24s} {a:4.1f}  {b:5.2f}    "
          + "  ".join(f"{e:7.3f}" for e in ev))

# verify the analytic form
for a, b in [(1.0, 1.0), (1.0, 0.4), (2.0, 3.0), (0.7, 1.9)]:
    ev = eigenvalues(hessian(a, b))
    pred = sorted([0.0, 3 * a + b, 3 * a + b, 4 * b])
    for got, want in zip(ev, pred):
        chk(f"eigenvalue a={a} b={b}", got, want, 1e-8) if want != 0 else \
            chk(f"zero mode a={a} b={b}", got, 0.0, 1e-8)

print("\n    The zero mode is the uniform shift and is present either way -- it is the")
print("    overall scale direction, not a discriminant.")

# ---------------------------------------------------------------- 2. the discriminant
print("\n[2] The discriminant")
print("    The nonzero spectrum is {3a+b, 3a+b, 4b}. It is THREEFOLD DEGENERATE iff")
print("\n        3a + b = 4b   <=>   3a = 3b   <=>   a = b\n")
print("    So the democratic case is exactly the degenerate case, and any backdrop")
print("    reading (a != b) splits the triple into a 2+1. The degeneracy is not an")
print("    extra assumption riding alongside K_4 -- it IS K_4, read spectrally.")

for a, b in [(1.0, 1.0), (1.0, 1.1), (1.0, 1.5)]:
    ev = eigenvalues(hessian(a, b))
    nz = [e for e in ev if e > 1e-8]
    split = (max(nz) - min(nz)) / max(nz) if nz else 0.0
    print(f"      a={a:.1f} b={b:.1f}:  nonzero {[f'{e:.3f}' for e in nz]}"
          f"   fractional split {split*100:5.1f}%")

chk("degeneracy exactly at a=b", max(eigenvalues(hessian(1.0, 1.0)))
    - sorted(eigenvalues(hessian(1.0, 1.0)))[1], 0.0, 1e-9)
# a 10% coupling mismatch already splits the triple by 7.7%
_ev = [e for e in eigenvalues(hessian(1.0, 1.1)) if e > 1e-8]
chk("10% bond mismatch splits the triple", (max(_ev) - min(_ev)) / max(_ev), 0.068182, 1e-4)

# ---------------------------------------------------------------- 3. what it buys
print("\n[3] What this does and does not buy")
print("""
    It buys a sharp statement of the premise. (P1) is not a vague preference for one
    picture over another: it is the claim that the family sector's stiffness matrix has
    a threefold-degenerate nonzero spectrum. That is a definite structural property, it
    is what edge-transitivity delivers, and any backdrop reading breaks it into 2+1 at
    first order in the coupling mismatch -- a 10% mismatch already splits the triple by
    6.8%, so the property is not fragile-in-principle and hard-to-check; it is rigid.

    It does NOT buy a decision. Nothing here says the condensate IS a node. And the
    degeneracy is a property of the COUPLINGS, which is exactly the ordering claim: the
    physical charged-lepton masses are famously non-degenerate, so whatever degeneracy
    the stiffness matrix has must be broken by the pinned state rather than by the
    couplings. That ordering -- couplings set first, state pinned second -- is the
    other half of (P1) and this script does not touch it either.

    The honest position: (P1) is a single structural premise, now stated as a spectral
    property rather than a picture, and it remains the one thing the Q = 2/3 mechanism
    rests on.
""")

# ---------------------------------------------------------------- verdict
print("=" * 76)
print("VERDICT on #1")
print("=" * 76)
print("""
    A discriminant EXISTS and it is clean: nonzero spectrum {3a+b, 3a+b, 4b}, threefold
    degenerate if and only if a = b. Node and backdrop are therefore not two ways of
    describing the same physics -- they differ in the stiffness spectrum at first order
    in the mismatch.

    #1 stays OPEN. What changes is its shape: the premise is no longer "is the medium
    really part of the same structure", which is unanswerable as posed, but "is the
    family stiffness matrix threefold degenerate before pinning", which is a property
    a constituent-level model either has or does not. That is a model-building question
    and belongs in the same waiting room as the seat constant -- not a desk computation.

    Filed accordingly: sharpened, not closed, and explicitly NOT counted as progress
    toward Q = 2/3.
""")

print("=" * 76)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 76)
