"""What puts mu_5 there? #146's last residue, against the corpus's own operator and its own winding.

THE RESIDUE (docket #146, after three passes): "the residue is a species-selective chiral mu_5 on
one node pair ... Still unsupplied: what puts mu_5 there." No source for mu_5 is named anywhere in
the corpus -- a grep for one returns nothing.

THE TWO PIECES THAT ARE ALREADY THERE, IN DIFFERENT ROOMS

  (1) PRTOE_baryogenesis.md already makes the identification a rotating phase IS a chemical
      potential: "mu = theta_dot holds across the transfer window", with theta_dot/H = 2.4e6 at
      T_sph. There it is used for LEPTON NUMBER, and the census portal is explicitly disqualified
      for that job -- "the census portal is lepton-number-blind".

  (2) Docket #125 selected the portal's operator: the gauge-singlet scalar multiplies the electron
      Yukawa, S (Lbar H e_R)/Lambda.

Put them together. The operator fixes how S's phase may be removed: S -> e^{i theta} S is undone by
e_R -> e^{-i theta} e_R, and that is a rotation of the RIGHT-HANDED electron only -- a chiral
rotation. A time-dependent theta then deposits theta_dot on n_R and nothing on n_L.

That is species-selective (the operator names the electron) and chiral (only e_R turns), which is
exactly the object #146 asks for. This works the claim through, including the part that does not
survive, and the condition it inherits.

Run: python3 scripts/basement_mu5_source.py
"""
import math

M_PL = 1.22e19          # GeV
T_SPH = 131.7           # GeV
G_STAR = 106.75
RATIO = 2.4e6           # theta_dot / H at T_sph, recorded in PRTOE_baryogenesis.md

print("=" * 78)
print("(1) THE ROTATION THE OPERATOR FORCES")
print("=" * 78)
print("  The #125 operator is   (S / Lambda) (Lbar H e_R) + h.c.")
print("  S is a total gauge singlet and is lepton-number-blind, so it carries no charge of its")
print("  own to rotate. Invariance under S -> e^{i th} S therefore has ONE compensator available")
print("  in the operator: e_R -> e^{-i th} e_R.")
print()
print("  That is a rotation of the right-handed electron alone. Decomposed:")
print()
print(f"    {'field':<12} {'rotates?':<10} {'chemical potential deposited'}")
print("    " + "-" * 60)
print(f"    {'e_R':<12} {'yes':<10} mu_R = theta_dot")
print(f"    {'e_L':<12} {'no':<10} mu_L = 0")
print()
print("    vector part  mu_V = (mu_R + mu_L)/2 = theta_dot / 2")
print("    axial  part  mu_5 = (mu_R - mu_L)/2 = theta_dot / 2")
print()
print("  So a right-handed-only rotation is HALF VECTOR and half axial. It is not purely chiral,")
print("  and that matters, because DERIVATION_HUNT's requirement is explicit: the object that")
print("  keeps 'the vacuum's neutrality preserved identically' is the AXIAL one, mu_R = +mu_5,")
print("  mu_L = -mu_5. A vector piece charges the medium.")

print()
print("=" * 78)
print("(2) WHY ONLY THE AXIAL HALF SURVIVES")
print("=" * 78)
print("  The two halves have different fates in a medium, and the difference is not a")
print("  convenience -- it is the distinction between a gauged and an ungauged charge:")
print()
print(f"  {'piece':<14} {'charge':<22} {'gauged?':<10} {'fate in the medium'}")
print("  " + "-" * 74)
print(f"  {'vector':<14} {'electron number':<22} {'YES (EM)':<10} SCREENED -- the plasma compensates")
print(f"  {'axial':<14} {'chirality':<22} {'no':<10} SURVIVES -- nothing screens it")
print()
print("  A vector chemical potential for a gauged charge cannot be imposed on a neutral medium:")
print("  neutrality fixes it, and any attempt to shift it is Debye-screened. Chirality is not a")
print("  gauge charge, so nothing compensates it; it relaxes only through the mass term, at a")
print("  rate set by m_e, not by the plasma frequency.")
print()
print("  NET: a winding portal phase deposits  mu_5 = theta_dot / 2  on the electron, and the")
print("  vector half it also deposits is screened away. What is left is precisely the")
print("  neutrality-preserving axial potential the residue names.")

print()
print("=" * 78)
print("(3) THE MAGNITUDE, AT THE ONE EPOCH THE CORPUS PINS theta_dot")
print("=" * 78)
H = 1.66 * math.sqrt(G_STAR) * T_SPH**2 / M_PL
theta_dot = RATIO * H
THETA_DOT_RECORDED = 59.7          # eV, carried directly in the failures ledger
print("  The corpus fixes theta_dot at the sphaleron era twice, and the two agree to 2%:")
print(f"    (a) directly, in the ledger:  theta_dot = {THETA_DOT_RECORDED} eV")
print(f"        (its m_1/theta_dot = 2.25 meV / {THETA_DOT_RECORDED} eV ="
      f" {2.25e-3/THETA_DOT_RECORDED:.2e}, as recorded)")
print(f"    (b) via the recorded ratio theta_dot/H = {RATIO:.1e} at T_sph = {T_SPH} GeV,")
print(f"        g* = {G_STAR}:  H = {H:.4e} GeV  ->  theta_dot = {theta_dot*1e9:.2f} eV")
print(f"    difference {100*abs(theta_dot*1e9-THETA_DOT_RECORDED)/THETA_DOT_RECORDED:.1f}%,"
      f" which is the T_sph choice: (a) implies T_sph = "
      f"{math.sqrt(THETA_DOT_RECORDED/1e9/RATIO*M_PL/(1.66*math.sqrt(G_STAR))):.1f} GeV.")
print()
print(f"    Quoting the ledger's direct value:  mu_5 = theta_dot/2 ="
      f" {THETA_DOT_RECORDED/2:.1f} eV")
print()
print("  Recorded for comparison, NOT as a match: the junction plasma frequency at the same")
print("  epoch is w_J ~ 5.7 keV, about 200x larger. These are different objects and the")
print("  comparison is offered only so the scale is not mistaken.")
print()
print("  WHAT IS NOT ESTABLISHED: whether this mu_5 is the size #146's doping needs. The docket")
print("  fixes the doping through N_screen = 2 N_0 and the band structure, not through a stated")
print("  mu_5 in eV, so there is no recorded number to compare against. That comparison is owed")
print("  and it is a real way this candidate can die.")

print()
print("=" * 78)
print("(4) THE CONDITION IT INHERITS — AND IT IS NOT A NEW ONE")
print("=" * 78)
print("  A chiral chemical potential needs a Dirac cone to sit on: two opposite-chirality states")
print("  in the same representation, so that mu_R = +mu_5 and mu_L = -mu_5 seat a particle")
print("  pocket against a hole pocket. #146's own third pass established that at the shell")
print("  (Lambda_shell = 5.4e17 GeV) NO species is vector-like -- every left-handed field is an")
print("  SU(2) doublet and every right-handed one a singlet -- so 'there is no Dirac cone for")
print("  mu_5 to sit on at all'.")
print()
print("  The rotation above inherits exactly that condition, for the same reason: e_L and e_R")
print("  are only two halves of one object once the Higgs has paired them. In the unbroken phase")
print("  the compensator e_R -> e^{-i th} e_R still exists, but what it dopes is a chiral")
print("  singlet with no partner, not a cone.")
print()
print(f"  {'phase':<26} {'cone exists?':<15} {'charged-lepton selection':<26} {'mu_5 source'}")
print("  " + "-" * 78)
print(f"  {'broken (below EW)':<26} {'YES':<15} {'holds (q^2 weighting)':<26} {'AVAILABLE'}")
print(f"  {'unbroken (at the shell)':<26} {'no':<15} {'fails (Y^2, no cone)':<26} {'unavailable'}")
print()
print("  THE TWO LINE UP EXACTLY. The charged-lepton selection and the mu_5 source hold in the")
print("  same phase and fail in the same phase, for the same structural reason -- the pairing of")
print("  opposite chiralities into one Dirac object.")

print()
print("=" * 78)
print("VERDICT — THE RESIDUE IS NOT AN INDEPENDENT UNKNOWN")
print("=" * 78)
print("  #146 was carrying two open items that looked separate: (a) does the charged-lepton")
print("  selection survive the shell's phase, and (b) what puts mu_5 there. They are one item.")
print()
print("  The source for mu_5 exists and is built from objects the corpus already owns -- #125's")
print("  operator and baryogenesis's own mu = theta_dot -- with no new field, no new coupling")
print("  and no new assumption. It is species-selective because the operator names the electron,")
print("  and chiral because only e_R can absorb the phase. Its vector half is screened by the")
print("  same neutrality the residue's own statement demands.")
print()
print("  And it is conditional on the broken phase, which is the condition the selection already")
print("  carries. So #146's open count drops from two to one, and the survivor is the fork")
print("  already registered as sec.6f's third horn: does the medium screen in the broken phase?")
print()
print("  STILL OWED, and both are attackable:")
print("    * the size comparison -- mu_5 ~ 29 eV at T_sph against whatever doping the band")
print("      structure needs, a number the docket has not stated in those units;")
print("    * theta_dot at the epoch that actually matters. The 2.4e6 ratio is pinned at T_sph;")
print("      if the doping is needed elsewhere, theta_dot ~ T^3 must be carried there and the")
print("      turn budget says the winding is laid down early and saturates.")
