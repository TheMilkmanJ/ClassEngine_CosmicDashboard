"""Which phase is the basement's medium in? The screening weights depend on the answer.

Section 6c puts the pairing shell at Lambda_shell, fixed by Delta = 2 Lambda_shell exp(-1/lambda)
= 3152 GeV with 1/lambda = 33.474. That is fifteen orders above the electroweak scale, so the
medium sits in the UNBROKEN phase -- and two things that a broken-phase reading takes for granted
are not available there:

  * there is no electric charge. The screened abelian charge is hypercharge, and the roster's
    Y assignments are not its Q assignments;
  * no Standard-Model species is vector-like. Every left-handed field is an SU(2) doublet and
    every right-handed one a singlet, so no pair of opposite-chirality Weyl nodes shares a
    representation -- there is no Dirac cone anywhere in the 48.

The second is the sharper. A chiral chemical potential needs a cone with two chiralities of the
same gauge charge to dope oppositely. In the unbroken phase there is no such object, so the
mechanism has nothing to sit on, whatever selects it.

Run: python3 scripts/basement_phase_check.py
"""
import math

# Per generation: (name, n_Weyl, Y, Q_list, SU2 rep dim, colour)
GEN = (
    ("Q_L  (3,2,1/6)", 6, 1 / 6, (2 / 3, -1 / 3), 2, 3),
    ("u_R  (3,1,2/3)", 3, 2 / 3, (2 / 3,), 1, 3),
    ("d_R  (3,1,-1/3)", 3, -1 / 3, (-1 / 3,), 1, 3),
    ("L    (1,2,-1/2)", 2, -1 / 2, (0.0, -1.0), 2, 1),
    ("e_R  (1,1,-1)", 1, -1.0, (-1.0,), 1, 1),
    ("nu_R (1,1,0)", 1, 0.0, (0.0,), 1, 1),
)
NGEN = 3
LAMBDA_INV = 33.474
DELTA_GEV = 3152.0
V_EW = 246.0

print("=" * 78)
print("WHERE THE SHELL SITS")
print("=" * 78)
lam_shell = DELTA_GEV / (2 * math.exp(-LAMBDA_INV))
print(f"  Delta = 2 Lambda_shell exp(-1/lambda),  1/lambda = {LAMBDA_INV}, Delta = {DELTA_GEV} GeV")
print(f"  -> Lambda_shell = {lam_shell:.3e} GeV")
print(f"  electroweak scale v = {V_EW} GeV")
print(f"  the shell sits {math.log10(lam_shell/V_EW):.1f} orders above it -- deep in the UNBROKEN phase")

print()
print("=" * 78)
print("THE ROSTER, WITH BOTH CHARGE ASSIGNMENTS")
print("=" * 78)
print(f"  {'field':<18} {'n':>3} {'Y':>7} {'n*Y^2':>9} {'sum Q^2':>9}")
print("  " + "-" * 50)
sy2 = sq2 = 0.0
for name, n, Y, Qs, _w, nc in GEN:
    # each SU(2)/colour state carries the same Y; Q varies within the doublet.
    y_part = n * Y * Y
    q_part = nc * sum(q * q for q in Qs) if nc > 1 else sum(q * q for q in Qs)
    sy2 += y_part
    sq2 += q_part
    print(f"  {name:<18} {n:3} {Y:7.4f} {y_part:9.4f} {q_part:9.4f}")
print("  " + "-" * 50)
print(f"  {'per generation':<18} {sum(g[1] for g in GEN):3} {'':7} {sy2:9.4f} {sq2:9.4f}")
print(f"  {'x 3 generations':<18} {NGEN*sum(g[1] for g in GEN):3} {'':7} {NGEN*sy2:9.4f} {NGEN*sq2:9.4f}")
print()
print("  Cross-check on the hypercharge sum, which is what the unbroken phase screens with:")
b_Y = (2 / 3) * NGEN * sy2 + (1 / 3) * (2 * 0.25)      # fermions + the Higgs doublet
print(f"    b_Y = (2/3) sum_Weyl Y^2 + (1/3) sum_scalar Y^2 = {b_Y:.5f}   = 41/6 = {41/6:.5f}")
print("    the Standard Model's own hypercharge beta coefficient, so sum Y^2 = 10 is right.")
print(f"  And sum Q^2 = {NGEN*sq2:.0f}, the value the finiteness table records.")

print()
print("=" * 78)
print("IS ANY SPECIES VECTOR-LIKE? (does a Dirac cone exist for mu_5 to sit on?)")
print("=" * 78)
left = [(n, Y, w, nc) for n, cnt, Y, Qs, w, nc in GEN if w == 2]
right = [(n, Y, w, nc) for n, cnt, Y, Qs, w, nc in GEN if w == 1]
print(f"  left-handed  (SU(2) doublets): {', '.join(n for n,_,_,_ in left)}")
print(f"  right-handed (SU(2) singlets): {', '.join(n for n,_,_,_ in right)}")
pairs = [(a[0], b[0]) for a in left for b in right
         if abs(a[1] - b[1]) < 1e-12 and a[2] == b[2] and a[3] == b[3]]
print()
print(f"  pairs sharing (Y, SU(2) rep, colour): {len(pairs)}")
print("  Every left-handed field is a doublet and every right-handed one a singlet, so the SU(2)")
print("  representation alone forbids a vector-like pair -- the hypercharges never even get a")
print("  chance to match. That is what 'the Standard Model is a chiral gauge theory' means, and")
print("  it is exactly the obstruction: there is no Dirac cone in the unbroken phase.")

print()
print("=" * 78)
print("WHAT THIS DOES TO THE SELECTION ARGUMENT")
print("=" * 78)
print("  The charge-weighted selection -- one doped cone worth 2 N_c q^2, hence a charged lepton")
print("  -- is a BROKEN-phase computation. It uses electric charge, and it uses the electron's")
print("  two chiralities as one cone. Both become available only below the electroweak scale,")
print(f"  {math.log10(lam_shell/V_EW):.0f} orders below where section 6c puts the shell. Held at the shell it does not apply;")
print("  held in the broken phase it applies but the shell is in the wrong place.")
print()
print("  So the selection result stands as a CONDITIONAL: if the medium's screening happens in")
print("  the broken phase, the doped pair must be a charged lepton. Whether it does is section")
print("  6f's open fork, and this is a third horn of it -- sharper than the coupling-running")
print("  horn, because it is not about what value alpha takes but about whether the objects the")
print("  kernel refers to exist at that scale at all.")
print()
print("  The unbroken-phase reading of the same requirement is worth stating: the screened")
print(f"  charge is hypercharge, the whole roster doped is sum Y^2 = {NGEN*sy2:.0f} rather than {NGEN*sq2:.0f}, and")
print("  N_screen = 2 N_0 would have to be met by hypercharge multiplets rather than by a cone.")
