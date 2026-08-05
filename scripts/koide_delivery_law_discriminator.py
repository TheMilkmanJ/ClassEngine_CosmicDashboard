"""Which energy-delivery law can carry the null at the exactness the corpus claims for it?

koide_frame_bridge.py established that R_c = M_c is an AMPLITUDE statement, and that turning it
into a stiffness statement requires a delivery law -- with four in use across the corpus giving
eps_D/eps_S in {2, sqrt2, 1, 1/2}. That left the law unfixed. This narrows it, using a constraint
the corpus already insists on everywhere else: Q = 2/3 holds to ~6e-6.

THE INSTRUMENT. Exactness is a much sharper probe than a central value. T6's reduction reads the
sector powers off equipartition, <|f_q|^2> = T/eps_q -- but equipartition is the CLASSICAL limit
of the exact harmonic result

    <|f_q|^2> = (hbar / 2 M w_q) coth(hbar w_q / 2 k T),

and the two sectors sit at DIFFERENT frequencies (eps_1 = 2 eps_0 means w_1 = sqrt2 w_0). So the
quantum correction does not cancel from the ratio. Its size is set by x = hbar w / kT, and the
corpus fixes that number itself: w_1 = (2/9) T_c.

Part 1 asks how exact the thermal law can be at the corpus's own x.
Part 2 asks what x the claimed 6e-6 would require.
Part 3 turns the same lens on the occupancy lock, which is a QUANTUM law and belongs in the table.

Run: python3 scripts/koide_delivery_law_discriminator.py
"""
import math

Q_TARGET = 2.0 / 3.0
EXACTNESS = 6e-6                    # the agreement the corpus claims for Q = 2/3
TAU = 0.5 * math.log(2)
M_E_KEV = 0.51099895e6 / 1e3
T_C = TAU * M_E_KEV                 # 177.099 keV
X1_CORPUS = 2.0 / 9.0               # hbar w_1 / k T_c, from w_1 = (2/9) T_c


def g(x):
    """(x/2) coth(x/2) -- the quantum enhancement of <x^2> over its classical value."""
    if x < 1e-8:
        return 1.0 + x * x / 12.0
    z = 0.5 * x
    return z / math.tanh(z)


def Q_of(x1, eps_ratio=2.0):
    """Q under the thermal law at charged-sector x1, with eps_D/eps_S = eps_ratio."""
    x0 = x1 * math.sqrt(1.0 / eps_ratio)          # w ~ sqrt(eps), so x0 = x1/sqrt(ratio)
    rho2 = (1.0 / eps_ratio) * g(x1) / g(x0)
    return 1.0 / 3.0 + (2.0 / 3.0) * rho2


print("=" * 78)
print("(1) THE THERMAL LAW AT THE CORPUS'S OWN FREQUENCY")
print("=" * 78)
print(f"  T_c = tau m_e            = {T_C:.3f} keV      (tau = ln2/2)")
print(f"  w_1 = (2/9) T_c          = {(2/9)*T_C:.3f} keV")
print(f"  x_1 = hbar w_1 / k T_c   = {X1_CORPUS:.6f}")
print(f"  x_0 = x_1 / sqrt2        = {X1_CORPUS/math.sqrt(2):.6f}")
print()
print("  Bose occupancy of the charged mode at that x:")
nbar = 1.0 / (math.exp(X1_CORPUS) - 1.0)
print(f"    n_bar = 1/(e^x - 1)    = {nbar:.4f}")
print("  Equipartition is the n_bar >> 1 limit. At n_bar ~ 4 the classical form is an")
print("  approximation, not an identity -- and the null is quoted as an identity.")
print()
q_corpus = Q_of(X1_CORPUS)
print(f"  Q under the exact thermal law, with eps_D = 2 eps_S held exactly:")
print(f"    rho^2 = (1/2) g(x_1)/g(x_0) = {0.5*g(X1_CORPUS)/g(X1_CORPUS/math.sqrt(2)):.9f}")
print(f"    Q     = {q_corpus:.9f}")
print(f"    2/3   = {Q_TARGET:.9f}")
print(f"    miss  = {abs(q_corpus/Q_TARGET - 1)*1e6:.1f} ppm,"
      f" against a claimed exactness of {EXACTNESS*1e6:.0f} ppm")
print(f"    -> the correction is {abs(q_corpus/Q_TARGET - 1)/EXACTNESS:.0f}x LARGER than the"
      " agreement it must not disturb")

print()
print("=" * 78)
print("(2) HOW CLASSICAL WOULD THE MODES HAVE TO BE?")
print("=" * 78)
lo, hi = 1e-6, 10.0
for _ in range(200):
    mid = math.sqrt(lo * hi)
    if abs(Q_of(mid) / Q_TARGET - 1) > EXACTNESS:
        hi = mid
    else:
        lo = mid
x_max = math.sqrt(lo * hi)
print(f"  Q stays within {EXACTNESS*1e6:.0f} ppm of 2/3 only for x_1 <= {x_max:.6f}")
print(f"  the corpus's x_1 is                                  {X1_CORPUS:.6f}")
print(f"  so w_1 would have to be smaller by a factor          {X1_CORPUS/x_max:.1f}")
print(f"  i.e. w_1 <= {x_max*T_C:.3f} keV against the recorded {(2/9)*T_C:.3f} keV")
print()
print(f"  {'x_1':>10} {'n_bar':>10} {'Q':>14} {'ppm from 2/3':>14}")
print("  " + "-" * 54)
for x in (1e-3, 0.01, x_max, 0.05, 0.1, X1_CORPUS, 0.5, math.log(2)):
    lbl = f"{x:10.6f}"
    nb = 1.0 / (math.exp(x) - 1.0)
    qq = Q_of(x)
    print(f"  {lbl} {nb:10.3f} {qq:14.9f} {abs(qq/Q_TARGET-1)*1e6:14.1f}")
print()
print("  The classical limit is EXACT and every finite x breaks it in the same direction --")
print("  Q rises above 2/3, monotonically. There is no cancellation to hope for: the charged")
print("  sector sits at the higher frequency, so it is always the more quantum of the two, and")
print("  its power is always suppressed less than the classical formula says.")
print()
print("  Equivalently, holding Q = 2/3 exactly at the corpus's x_1 requires")
lo, hi = 1.5, 2.5
for _ in range(200):
    mid = 0.5 * (lo + hi)
    if Q_of(X1_CORPUS, mid) > Q_TARGET:
        lo = mid
    else:
        hi = mid
r_needed = 0.5 * (lo + hi)
print(f"    eps_D/eps_S = {r_needed:.6f}  rather than 2 exactly,")
a_over_b = 3.0 / (r_needed - 1.0)
print(f"    i.e. a = {a_over_b:.4f} b  rather than a = 3b.")
print("  So 'a = 3b' is the CLASSICAL statement of the null, not its exact statement, and the")
print("  clean integer 3 is an artifact of the limit rather than a structural fact.")

print()
print("=" * 78)
print("(3) THE OCCUPANCY LOCK IS A FIFTH LAW -- AND IT IS NOT THERMAL")
print("=" * 78)
print("  The lock does not use equipartition at all. Its argument is quantum and cold:")
print("    N_0 = M w f_0^2 / hbar = 1        (the neutral mode carries one quantum)")
print("    E_c = M w^2 R_c^2 = hbar w        (the charged PAIR sits in its ground state,")
print("                                       2 dof x (1/2) hbar w)")
print("  from which f_0^2 = R_c^2 = hbar/(M w) and the null follows with M and w cancelling.")
print()
print("  That cancellation is the lock's whole strength -- and it needs ONE w. The argument")
print("  as recorded writes the same symbol in both lines. But the null it is explaining says")
print("  the two sectors do NOT share a frequency:")
print()
print("    eps_1 = 2 eps_0   =>   w_1 = sqrt2 w_0")
print()
w0, w1 = 1.0, math.sqrt(2.0)
f0sq = 1.0 / w0                     # hbar/(M w_0), one quantum in the neutral mode
Rcsq = 1.0 / w1                     # hbar/(M w_1), ground state of the charged pair
print(f"    neutral, one quantum at w_0 :  f_0^2 = hbar/(M w_0)  -> {f0sq:.6f}  (hbar/M = 1)")
print(f"    charged pair ground state    :  R_c^2 = hbar/(M w_1)  -> {Rcsq:.6f}")
print(f"    R_c / M_c = (w_0/w_1)^(1/2)  = {math.sqrt(f0sq and Rcsq/f0sq):.6f}"
      f"   = 2^(-1/4)")
print(f"    the null needs                 1.000000")
print(f"    miss                           {abs(math.sqrt(Rcsq/f0sq) - 1)*100:.1f}%")
print()
print("  So the lock's derivation is frequency-degenerate: it delivers the null only if the")
print("  neutral and charged sectors share w, and the stiffness reduction it is supposed to")
print("  explain says they differ by sqrt2. Written with distinct frequencies the same three")
print("  lines give 2^(-1/4) = 0.841, not 1.")
print()
print("  This is not fatal to the lock and it is not cosmetic. It is a NAMED condition the")
print("  lock now owes: either the two sectors are degenerate at the moment the quanta are")
print("  counted -- which is a statement about the freeze, before the stiffnesses split --")
print("  or the lock's cancellation does not happen. The lock's own filter score (2 for 2,")
print("  against 0 for 22 for the retired mechanisms) is untouched by this; what changes is")
print("  that it has a specific, checkable debt instead of an unexamined step.")

print()
print("=" * 78)
print("(4) tau AND UNIT OCCUPANCY — AN EXACT IDENTITY, AND THE FORK IT OPENS")
print("=" * 78)
print("  Sitting in the table above, at the last row: n_bar = 1 falls at x = ln2 exactly.")
print("  The corpus's central constant is tau = ln2/2. So, as an identity in nothing but the")
print("  Bose factor:")
print()
print("      n_bar = 1  <=>  e^x = 2  <=>  x = ln2  <=>  hbar w / kT = 2 tau")
print()
x_unit = math.log(2.0)
print(f"    check: n_bar(ln2) = {1.0/(math.exp(x_unit)-1.0):.12f}")
print(f"           2 tau      = {2*TAU:.12f}      ln2 = {x_unit:.12f}")
print()
print("  This is worth stating precisely because it is easy to over-read. It does NOT derive")
print("  tau. It says that the SAME number the corpus reaches from -ln(rho) is the value of")
print("  hbar w / 2kT at which a bosonic mode holds exactly one quantum -- which is the")
print("  occupancy lock's premise, reached from the opposite side of the theory.")
print()
print("  It also sharpens the fork, because the two cannot both hold:")
print(f"    unit occupancy needs   hbar w / kT_c = ln2      = {x_unit:.6f}")
print(f"    the corpus records     w_1 = (2/9) T_c         = {X1_CORPUS:.6f}")
print(f"    ratio                  (ln2)/(2/9) = 9 ln2 / 2 = {x_unit/X1_CORPUS:.6f}")
print()
print(f"    (That ratio is 9ln2/2 = {9*math.log(2)/2:.6f}. It is NOT pi"
      f" -- pi = {math.pi:.6f}, off by {abs(x_unit/X1_CORPUS/math.pi-1)*100:.1f}%."
      " Recorded so")
print("     the near-miss is not chased later.)")
print()
print(f"  In frequency: unit occupancy puts w at {x_unit*T_C:.2f} keV, the recorded w_1 is"
      f" {X1_CORPUS*T_C:.2f} keV.")
print("  One of the two is wrong, or they refer to different modes. That is a bounded,")
print("  answerable question, and it is the first time the two live arcs -- the tau modulus")
print("  and the occupancy lock -- have been made to contradict each other on a number.")
print()
print("  AMENDED 2026-07-29 -- the ratio is NOT an independent contradiction.")
print("  scripts/occupancy_frequency_keystone_identity.py shows 9ln2/2 = 9*tau = 6/c_K")
print("  exactly, and that the tau CANCELS out of it (verified over a wide range of tau,")
print("  max deviation 0.00e+00). So this ratio is the keystone c_K*tau = Q with the")
print("  modulus divided out -- it was already implied the moment w_1/T_c was identified")
print("  with arg b = Q/3, and it carries no information the keystone did not carry.")
print("  Carry it as an INSTANCE of the c_K debt, not as its own open question: it is")
print("  evidence against neither arc, and deriving c_K settles it automatically.")
print("  The asymmetry still stands, though -- 'hbar w/kT = ln2' is a thermodynamic")
print("  condition, while 'w_1/T_c = arg b' equates a frequency ratio with a phase, which")
print("  is an identification rather than a derivation and is the step to examine first.")

print()
print("=" * 78)
print("VERDICT — THE LAW IS NARROWED, NOT YET FIXED")
print("=" * 78)
print("  The thermal law cannot carry the null at the claimed exactness at the corpus's own")
print(f"  frequency: it distorts Q by {abs(q_corpus/Q_TARGET-1)*1e6:.0f} ppm against a"
      f" {EXACTNESS*1e6:.0f} ppm budget. Two ways out,")
print("  and they are both real statements rather than escapes:")
print()
print(f"    (a) the modes are far more classical than w_1 = (2/9) T_c implies (x_1 <=")
print(f"        {x_max:.4f}, a factor {X1_CORPUS/x_max:.0f} smaller). Note that w_1 = (2/9)T_c is")
print("        itself derived FROM Q = 2/3 via theta_B, so it is not an independent")
print("        measurement and this route is not circular to take -- but it does mean the")
print("        corpus currently has no independent handle on x_1 at all.")
print()
print("    (b) the delivery law is not thermal. Occupancy lock was a *cold-law class*")
print("        candidate, but it is NOT a live escape: integer occupancy cannot produce")
print("        ω₁/ω₀ = √2 (killed 2026-07-29; see occupancy_lock_cannot_deliver / T6).")
print("        Residual exactness research is freeze-time stiffness / Wilson bins only —")
print("        not a restored 'candidate mechanism' (tribunal R2-koide lane (c)).")
print()
print("  Either way the classical equipartition reading of the null is the one under pressure,")
print("  and 'a = 3b' should be carried as its classical limit rather than as an exact")
print("  structural relation.")
