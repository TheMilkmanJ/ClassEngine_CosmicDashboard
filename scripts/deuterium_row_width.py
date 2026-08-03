#!/usr/bin/env python3
"""
The deuterium row's width: replacing a booking with a rule   (docket #57)

GRADE AND DECISION RULE STATED BEFORE COMPUTING (protocol check 33)
-------------------------------------------------------------------
PRTOE_deuterium_row.md records four defensible widths giving -2.94, -3.64, -3.13 and
-1.96 sigma, and says outright: "Which construction the corpus stands on is a booking,
not a desk computation, and it is owed." The standing -2.94 sits mid-range "by the
accident of having borrowed another code's error rather than computed one."

The hazard is obvious and it is the whole reason to write the rule down first: with a
1.7 sigma spread available, ANY answer can be reached by choosing a construction. So
the rule is fixed here, before any number is produced, and it is the one the file
itself already states without executing:

    A CENTRAL VALUE AND ITS ERROR MUST COME FROM THE SAME PLACE.

    (A) Stand on one compilation -> use that compilation's central value AND its own
        error bar. Self-consistent.
    (B) Treat the compilation spread as a systematic -> then the central value must be
        the compilation average too, not one compilation's. Self-consistent.
    (X) One compilation's central value, with an error inflated by the spread between
        compilations. NOT self-consistent -- it takes the disagreement as uncertainty
        while ignoring what the disagreement says about where the centre is.

The result is whatever it is. It is allowed to make the tension larger. Marking the
direction now, before computing: option (B) moves the predicted D/H UP toward Cooke
(NACRE's lower d(d,n)3He rate burns less deuterium), so (B) will REDUCE the tension.
That is stated in advance precisely so that arriving there cannot be dressed as a
discovery.

Evidence class: this re-books an error bar. It cannot make the model fit better; it can
only make the quoted number honest.
"""

import math

CHECKS = []
def chk(name, got, booked, tol, unit=""):
    ok = abs(got) <= tol if booked == 0 else abs(got - booked) / abs(booked) <= tol
    CHECKS.append((ok, name, booked, got, unit))

# ---------------------------------------------------------------- inputs (all recorded)
DH_MODEL   = 2.387      # x1e-5, the model's prediction
DH_LCDM    = 2.420      # x1e-5, LCDM control, same code same data
DH_OBS     = 2.527      # x1e-5, Cooke quasar-optical
SIG_OBS    = 0.030      # Cooke's measurement error
SIG_PRIMAT = 0.037      # PRIMAT post-LUNA theory error, BORROWED
DDN_RATIO  = 0.9569     # NACRE II / PRIMAT on d(d,n)3He
DDN_DDH    = 0.0524     # D/H shift from moving that reaction PRIMAT -> NACRE
SIG_PRYM   = 0.0384     # PRyM's own rates, quadrature total quoted in the file

print("=" * 76)
print("THE DEUTERIUM ROW: PICKING THE WIDTH BY RULE, NOT BY ACCIDENT")
print("=" * 76)

print(f"\n  model prediction   D/H = {DH_MODEL:.3f} e-5")
print(f"  LCDM control       D/H = {DH_LCDM:.3f} e-5")
print(f"  Cooke observation  D/H = {DH_OBS:.3f} +/- {SIG_OBS:.3f} e-5")

# ---------------------------------------------------------------- the standing row
print("\n[1] The standing row, reproduced")
w_standing = math.hypot(SIG_OBS, SIG_PRIMAT)
t_standing = (DH_MODEL - DH_OBS) / w_standing
print(f"    width  = sqrt(0.030^2 + 0.037^2) = {w_standing:.4f}")
print(f"    tension= ({DH_MODEL} - {DH_OBS})/{w_standing:.4f} = {t_standing:.2f} sigma")
chk("standing width", w_standing, 0.0476, 1e-2)
chk("standing tension", t_standing, -2.94, 1e-2, "sigma")

t_lcdm = (DH_LCDM - DH_OBS) / w_standing
print(f"    LCDM control on the same width          = {t_lcdm:.2f} sigma")
chk("LCDM control tension", t_lcdm, -2.25, 1e-2, "sigma")

# ---------------------------------------------------------------- option A
print("\n[2] Option (A): stand on PRIMAT, centre and error both")
print("    This IS the standing row. Its defence is that PRIMAT's central value and")
print("    PRIMAT's 1.10% band on d(d,n)3He are one self-consistent package. Its cost")
print("    is that it ignores a compilation disagreement that is real and measured.")
print(f"    -> {t_standing:.2f} sigma")

# ---------------------------------------------------------------- option B
print("\n[3] Option (B): treat the compilation spread as a systematic -- BOTH ends")
print("    If the PRIMAT/NACRE disagreement is uncertainty, then the best estimate of")
print("    the rate is the compilation average, and the central D/H must move with it.")
print("    Half the full PRIMAT->NACRE shift, applied to both model and control:\n")

shift_half = DDN_DDH / 2.0
DH_MODEL_B = DH_MODEL + shift_half
DH_LCDM_B  = DH_LCDM + shift_half
print(f"    d(d,n)3He NACRE/PRIMAT = {DDN_RATIO:.4f}, full D/H shift = +{DDN_DDH:.4f}")
print(f"    half-shift to the average          = +{shift_half:.4f}")
print(f"    model  D/H {DH_MODEL:.3f} -> {DH_MODEL_B:.3f}")
print(f"    LCDM   D/H {DH_LCDM:.3f} -> {DH_LCDM_B:.3f}")

# the systematic is half the spread, added in quadrature with PRyM's own rate errors
sys_compilation = DDN_DDH / 2.0
w_B = math.hypot(math.hypot(SIG_OBS, SIG_PRYM), sys_compilation)
t_B = (DH_MODEL_B - DH_OBS) / w_B
t_B_lcdm = (DH_LCDM_B - DH_OBS) / w_B
print(f"\n    width = sqrt(0.030^2 + {SIG_PRYM}^2 + {sys_compilation:.4f}^2) = {w_B:.4f}")
print(f"    model tension  = {t_B:.2f} sigma")
print(f"    LCDM  tension  = {t_B_lcdm:.2f} sigma")
chk("option B width", w_B, 0.0554, 2e-2)

# ---------------------------------------------------------------- option X
print("\n[4] Option (X): the one that must be rejected")
w_X = 0.0713
t_X = (DH_MODEL - DH_OBS) / w_X
print(f"    PRIMAT's central value with the spread folded into the error:")
print(f"      width {w_X:.4f} -> {t_X:.2f} sigma")
print("    This is the widest and most flattering construction available, and it is")
print("    the one the rule excludes: it counts the compilation disagreement as")
print("    uncertainty while still standing on one compilation's centre. Taking the")
print("    disagreement seriously means moving the centre too, which is option (B).")
chk("option X tension", t_X, -1.96, 1e-2, "sigma")

# ---------------------------------------------------------------- the comparison
print("\n[5] What the rule selects")
print(f"""
      construction                                    model     LCDM    self-consistent
      (A) PRIMAT centre + PRIMAT error               {t_standing:6.2f}   {t_lcdm:6.2f}      yes
      (B) compilation average, centre and error      {t_B:6.2f}   {t_B_lcdm:6.2f}      yes
      (X) PRIMAT centre + compilation-spread error   {t_X:6.2f}      n/a      NO
""")

delta = abs(t_B - t_standing)
print(f"    (A) and (B) differ by {delta:.2f} sigma. Both are legitimate; they answer")
print("    different questions. (A) asks how the model does against the best single")
print("    compilation. (B) asks how it does given that the compilations disagree.")
print("    (X) answers neither and is the only one the rule kills outright.")

# ---------------------------------------------------------------- the invariant
print("\n[6] The part that does not move")
print("    The excess deficit -- model minus control -- is width-independent:\n")
excess = DH_LCDM - DH_MODEL
print(f"      D/H(LCDM) - D/H(model) = {DH_LCDM:.3f} - {DH_MODEL:.3f} = {excess:.3f}")
for lab, w in [("(A)", w_standing), ("(B)", w_B), ("(X)", w_X)]:
    print(f"      in {lab} units: {excess/w:.2f} sigma")
chk("excess deficit, absolute", excess, 0.033, 1e-2)

print("\n    The model burns 0.033e-5 more deuterium than the control on identical data,")
print("    and no width choice touches that. Every construction above agrees the model")
print("    sits FURTHER from Cooke than LCDM does. The width debate changes how bad the")
print("    row looks; it does not change the sign or the size of the model's own cost.")

# ---------------------------------------------------------------- verdict
print("\n" + "=" * 76)
print("VERDICT on #57")
print("=" * 76)
print(f"""
    The booking is replaced by a rule: a central value and its error must come from
    the same place. That rule was written before the numbers and it kills exactly one
    construction -- (X), the widest and most flattering, at {t_X:.2f} sigma -- because it
    inflates the error with a disagreement whose implication for the centre it then
    ignores.

    Two self-consistent options survive and the corpus should quote BOTH, because they
    answer different questions:
      (A) against the best single compilation:   {t_standing:.2f} sigma
      (B) allowing that compilations disagree:   {t_B:.2f} sigma

    The standing row is (A). It should keep standing, now for a reason rather than by
    the accident of a borrowed error bar, with (B) quoted beside it.

    THE ROW REMAINS ADVERSE EITHER WAY. And the quantity that is width-independent --
    the model burning {excess:.3f}e-5 more deuterium than its own control on identical data
    -- is untouched by any of this. Re-booking an error bar does not improve a fit.
""")

print("=" * 76)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 76)
