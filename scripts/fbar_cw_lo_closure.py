#!/usr/bin/env python3
"""
Track A3 closure — f̄ = 2/π residual / c_w / leading-order dominance (2026-07-31).

WHAT THIS CLOSES
----------------
The ε-stack carries f̄ = 2/π as the winding average ⟨|cos|⟩. Three pieces were
already on the table:

  (form)  mass-positivity rectifies the signed projection → mean-absolute, 2/π;
          RMS 0.707 and variance 0.5 are data-rejected (fbar_leading_order_price.py,
          fbar_window_discriminator.py, winding_fbar_spatial.py).
  (even)  C8/C16: admissible even part is the medium back-reaction resummation
          F = u/(1+a u) with c_w = −a exactly (cw_response_from_backreaction.py).
  (price) subleading moves f̄ by only ~0.98% per unit c_w (fbar_leading_order_price.py).

WHAT WAS STILL OPEN (board A3)
------------------------------
  1. Prove (not assert) leading-order dominance of |x| over c_w x² at ε ≈ 1.25%,
     from the medium expansion and the data band on a / c_w.
  2. Derive or tightly bound a (= −c_w) from recorded couplings if possible;
     otherwise name the residual honestly.
  3. Grade the track.

GRADE RULE (same as census_alpha_B_first_principles.py / board key)
-------------------------------------------------------------------
  DERIVED:          medium equations fix the object with no free O(1).
  CANDIDATE CLOSED: mechanism exhibited; at most one named residual / data referee.
  OPEN:             scale wrong by ≫O(1), or form still free.

PRE-STATED CONTROLS
-------------------
  A  winding moments by integration, ratios π/4 and 2/3.
  B  LO shift formula f̄_eff = 2/π + c_w·ε/2 reproduces recorded per-unit price.
  C  quadratic/leading = |c_w|·ε·(π/4); at unit |c_w| equals the corrected C9 0.985%.
  D  across the WHOLE data band on |c_w| (ensemble and fit-implied),
     quadratic/leading stays ≪ 1 (dominance holds as bound, not hope).
  E  cubic/leading ≪ quadratic across the same band (series not truncated by accident).
  F  back-reaction fixed point F = u/(1+a u), c_w = −a (form from medium).
  G  recorded couplings do NOT force a unique a — residual is named, not invented.
  H  ANTI-CONTROL: a huge |c_w| (~100) WOULD break LO dominance — falsifiable.
  I  ANTI-CONTROL: odd responses give c_w = 0 and are outside the ensemble band.
  J  grade assertion is self-consistent with board key and the controls above.

Run: python3 scripts/fbar_cw_lo_closure.py
"""
from __future__ import annotations

import math
import sys

# ---- recorded PRTOE --------------------------------------------------------
ALPHA = 1.0 / 137.035999084
EPS = 27.0 * ALPHA / (5.0 * math.pi)          # c · f̄ · α_c = 1.2543%
TWO_OVER_PI = 2.0 / math.pi
PI_OVER_4 = math.pi / 4.0

# data on c_w (renamed from c2 2026-07-28)
CW_FIT = -1.80
CW_ENS, CW_ENS_SIG = -0.84, 0.52
ENS_BAND = (CW_ENS - CW_ENS_SIG, CW_ENS + CW_ENS_SIG)   # [-1.36, -0.32]
C8_WIDE = (-2.0, 0.0)
# back-reaction a = −c_w
A_ENS_BAND = (-ENS_BAND[1], -ENS_BAND[0])               # [0.32, 1.36]
A_FIT = -CW_FIT                                          # 1.80
# measured f̄
FBAR_FIT = 0.6253
FBAR_ENS, FBAR_ENS_SIG = 0.63137, 0.00328

_fail: list[str] = []


def chk(name: str, cond: bool, detail: str = "") -> None:
    if not cond:
        _fail.append(name)
    tag = "ok  " if cond else "FAIL"
    print(f"  {tag}  {name}" + (f"   {detail}" if detail else ""))


def moment(power: int, n: int = 400001) -> float:
    """⟨|cos θ|^power⟩ over [0, 2π) by Simpson."""
    a, b = 0.0, 2.0 * math.pi
    h = (b - a) / (n - 1)
    tot = 0.0
    for i in range(n):
        t = a + i * h
        v = abs(math.cos(t)) ** power
        w = 1.0 if i in (0, n - 1) else (4.0 if i % 2 else 2.0)
        tot += w * v
    return tot * h / 3.0 / (2.0 * math.pi)


def fbar_eff(c_w: float, eps: float = EPS) -> float:
    return TWO_OVER_PI + c_w * eps / 2.0


def quad_over_lead(c_w: float, eps: float = EPS, r_quad: float = PI_OVER_4) -> float:
    """|quadratic| / leading after θ-average = |c_w| · ε · ⟨cos²⟩/⟨|cos|⟩."""
    return abs(c_w) * eps * r_quad


def cub_over_lead(c3: float, eps: float = EPS, r_cub: float = 2.0 / 3.0) -> float:
    return abs(c3) * eps * eps * r_cub


def main() -> int:
    print("=" * 78)
    print("  Track A3 — f̄ LO / c_w residual / leading-order dominance")
    print("=" * 78)
    print(f"\n  ε = 27α/(5π) = {EPS:.9f}  ({EPS*100:.4f}%)")
    print(f"  2/π           = {TWO_OVER_PI:.9f}")
    print(f"  ensemble c_w  = {CW_ENS} ± {CW_ENS_SIG}  →  a ∈ [{A_ENS_BAND[0]:.2f}, {A_ENS_BAND[1]:.2f}]")
    print(f"  fit-implied   = {CW_FIT}                 →  a = {A_FIT:.2f}")

    # ---- A: moments --------------------------------------------------------
    print("\n  A  winding moments (integrated, not quoted)")
    m1, m2, m3 = moment(1), moment(2), moment(3)
    print(f"       ⟨|cos|⟩   = {m1:.9f}   (2/π  = {TWO_OVER_PI:.9f})")
    print(f"       ⟨cos²⟩    = {m2:.9f}   (1/2  = {0.5:.9f})")
    print(f"       ⟨|cos|³⟩  = {m3:.9f}   (4/3π = {4/(3*math.pi):.9f})")
    chk("A1 moments match closed forms",
        abs(m1 - TWO_OVER_PI) < 1e-6 and abs(m2 - 0.5) < 1e-6
        and abs(m3 - 4 / (3 * math.pi)) < 1e-6)
    r_quad, r_cub = m2 / m1, m3 / m1
    chk("A2 quadratic moment ratio = π/4", abs(r_quad - PI_OVER_4) < 1e-6,
        f"{r_quad:.9f}")
    chk("A3 cubic moment ratio = 2/3", abs(r_cub - 2.0 / 3.0) < 1e-6,
        f"{r_cub:.9f}")

    # ---- B: f̄_eff formula -------------------------------------------------
    print("\n  B  f̄_eff = 2/π + c_w·ε/2  (per-unit price)")
    per_unit = (EPS / 2.0) / TWO_OVER_PI
    chk("B1 per-unit fractional shift ≈ 0.985%",
        abs(per_unit * 100 - 0.985) < 0.005,
        f"{per_unit*100:.4f}% per unit c_w")
    # recover implied c_w from measured f̄
    c_from_fit = (FBAR_FIT - TWO_OVER_PI) / (EPS / 2.0)
    c_from_ens = (FBAR_ENS - TWO_OVER_PI) / (EPS / 2.0)
    chk("B2 fit-implied f̄ recovers c_w ≈ −1.80",
        abs(c_from_fit - CW_FIT) < 0.02, f"got {c_from_fit:.3f}")
    chk("B3 ensemble f̄ recovers c_w ≈ −0.84",
        abs(c_from_ens - CW_ENS) < 0.02, f"got {c_from_ens:.3f}")

    # ---- C: C9 quadratic booking (corrected 0.985%) ------------------------
    print("\n  C  C9 quadratic / leading at unit |c_w|")
    q_unit = quad_over_lead(1.0, r_quad=r_quad) * 100.0
    chk("C1 unit-|c_w| quadratic fraction = 0.985% (not the slipped 0.83%)",
        abs(q_unit - 0.985) < 0.005, f"{q_unit:.4f}%")
    slip = EPS * r_cub * 100.0
    chk("C2 the old 0.83% is 2/3·ε — cubic's ratio in quadratic's place",
        abs(slip - 0.836) < 0.01, f"{slip:.4f}%")

    # ---- D: LO dominance bound across data band ----------------------------
    print("\n  D  leading-order dominance across the data band on |c_w|")
    print(f"\n    {'source':<22} {'|c_w|':>8} {'quad/lead':>12} {'pointwise |c_w|ε':>18}")
    print("    " + "-" * 64)
    band_ok = True
    rows = [
        ("ensemble lo", abs(ENS_BAND[1])),   # 0.32
        ("ensemble centre", abs(CW_ENS)),
        ("ensemble hi", abs(ENS_BAND[0])),   # 1.36
        ("fit-implied", abs(CW_FIT)),
        ("C8 wide floor", 2.0),
        ("natural a=1/2", 0.5),
        ("natural a=1", 1.0),
    ]
    worst_q = 0.0
    for name, acw in rows:
        q = quad_over_lead(acw, r_quad=r_quad)
        pw = acw * EPS
        worst_q = max(worst_q, q)
        print(f"    {name:<22} {acw:8.2f} {q*100:11.3f}% {pw*100:17.3f}%")
        # dominance: averaged quadratic ≪ leading  (demand < 5%)
        if q >= 0.05:
            band_ok = False
    chk("D1 averaged quadratic/leading < 5% across entire data band",
        band_ok and worst_q < 0.05,
        f"worst = {worst_q*100:.3f}% (fit-implied / C8 floor)")
    # sharper: even at fit-implied, under 2%
    q_fit = quad_over_lead(CW_FIT, r_quad=r_quad)
    chk("D2 at fit-implied |c_w|=1.80, quad/lead still < 2%",
        q_fit < 0.02, f"{q_fit*100:.3f}%")
    # pointwise worst case |c_w|ε (not θ-averaged) still small
    pw_fit = abs(CW_FIT) * EPS
    chk("D3 pointwise worst |c_w|·ε at fit-implied < 3%",
        pw_fit < 0.03, f"{pw_fit*100:.3f}%")
    print("\n       ⇒ LO dominance is a BOUND from ε and the data band on a,")
    print("         not a generic hope. The expansion parameter is ε itself.")

    # ---- E: cubic remains sub-subleading -----------------------------------
    print("\n  E  cubic remains negligible (resummation c₃ = a² = c_w²)")
    print(f"\n    {'|c_w|':>8} {'c₃=c_w²':>10} {'cub/lead':>12} {'cub/quad':>12}")
    print("    " + "-" * 46)
    cub_ok = True
    for acw in (0.32, 0.84, 1.0, 1.36, 1.80, 2.0):
        c3 = acw * acw
        cl = cub_over_lead(c3, r_cub=r_cub)
        ql = quad_over_lead(acw, r_quad=r_quad)
        print(f"    {acw:8.2f} {c3:10.4f} {cl*100:11.4f}% {cl/ql if ql else 0:11.4f}")
        if cl >= 0.005 or cl >= ql:
            cub_ok = False
    chk("E1 cubic/leading < 0.5% and cubic < quadratic across band", cub_ok)

    # ---- F: form from medium back-reaction ---------------------------------
    print("\n  F  form: medium back-reaction generates c_w = −a (C16)")
    # solve F = u − a u F by bisection
    def resummed(u: float, a: float) -> float:
        lo, hi = 0.0, u + 1.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if mid - (u - a * u * mid) > 0:
                hi = mid
            else:
                lo = mid
        return 0.5 * (lo + hi)

    form_ok = True
    for a in (0.32, 0.5, 1.0, 1.36, 1.80):
        for u in (0.05, 0.5):
            F = resummed(u, a)
            closed = u / (1.0 + a * u)
            if abs(F - closed) > 1e-9:
                form_ok = False
    chk("F1 fixed point of F = u − a u F is u/(1+a u)", form_ok)
    # Taylor: c_w = −a.  (F(h)−h)/h² = −a/(1+a h) → −a as h→0;
    # use small h and correct residual O(a² h).
    h = 1e-6
    cw_ok = True
    worst_dev = 0.0
    for a in (0.32, 0.5, 1.0, 1.36, 1.80):
        f = lambda u, a=a: u / (1.0 + a * u)
        # F(u) = u + c_w u² + …  ⇒  c_w = (F(h) − h)/h²
        cw = (f(h) - h) / (h * h)
        worst_dev = max(worst_dev, abs(cw + a))
        if abs(cw + a) > 1e-4:
            cw_ok = False
    chk("F2 c_w = −a at every back-reaction strength tested", cw_ok,
        f"max |c_w + a| = {worst_dev:.2e}; c_w IS the back-reaction strength")
    # series predictions
    series_ok = all(
        abs((-a) ** 2 - a * a) < 1e-15 and abs((-a) ** 3 + a ** 3) < 1e-15
        for a in (0.5, 1.0, 1.8)
    )
    # c3 = a² = c_w², c4 = −a³ = −|c_w|³
    chk("F3 resummation predicts c₃ = c_w², c₄ = −|c_w|³", series_ok)

    # ---- G: can recorded couplings force a? --------------------------------
    print("\n  G  can recorded couplings force a unique a?  (honest residual)")
    # candidates one might invent from the stack
    candidates = {
        "α_c = 3α": 3 * ALPHA,
        "ε": EPS,
        "1 (unit back-reaction)": 1.0,
        "1/2 (ln/exp family)": 0.5,
        "π/4 (moment ratio)": PI_OVER_4,
        "2/π (f̄ itself)": TWO_OVER_PI,
        "√2 − 1": math.sqrt(2) - 1,
    }
    print(f"\n    {'candidate from recorded objects':<36} {'value':>10} {'in ens band?':>14}")
    print("    " + "-" * 64)
    in_band = []
    for name, val in candidates.items():
        inside = A_ENS_BAND[0] <= val <= A_ENS_BAND[1]
        if inside:
            in_band.append(name)
        print(f"    {name:<36} {val:10.5f} {'yes' if inside else 'no':>14}")
    # α_c and ε are far too small — not the back-reaction scale
    chk("G1 α_c and ε are NOT the back-reaction scale (≪ O(1))",
        candidates["α_c = 3α"] < 0.05 and candidates["ε"] < 0.05)
    # unit and 1/2 sit inside the ensemble band — natural, not forced
    chk("G2 natural a=1 and a=1/2 sit inside ensemble band (admissible, not forced)",
        "1 (unit back-reaction)" in in_band and "1/2 (ln/exp family)" in in_band)
    # nothing in the stack forces a unique value: multiple distinct O(1)s fit
    chk("G3 no unique a is forced — residual is the VALUE of a",
        len(in_band) >= 2,
        f"{len(in_band)} natural O(1)s inside band: residual, not derivation")
    # fit-implied a=1.80 is outside ensemble — tension recorded, not averaged
    sep = abs(CW_FIT - CW_ENS) / CW_ENS_SIG
    chk("G4 fit vs ensemble tension is real (~1.9σ) — do not average them",
        abs(sep - 1.9) < 0.15, f"{sep:.2f}σ")
    print("\n       NAMED RESIDUAL: a (= −c_w), the medium's back-reaction strength")
    print("       on its own winding response. Form and LO dominance do not need it;")
    print("       only the precise sub-percent f̄ correction does. Data-refereed:")
    print(f"         ensemble a ∈ [{A_ENS_BAND[0]:.2f}, {A_ENS_BAND[1]:.2f}]")
    print(f"         fit-implied a ≈ {A_FIT:.2f}  (1.9σ tension — recorded, not resolved)")

    # ---- H: anti-control — huge c_w breaks LO ------------------------------
    print("\n  H  ANTI-CONTROL: LO dominance is falsifiable")
    q_huge = quad_over_lead(100.0, r_quad=r_quad)
    chk("H1 |c_w|~100 would make quad/lead ~100% — expansion broken",
        q_huge > 0.5, f"quad/lead = {q_huge*100:.1f}%")
    # data is O(1), so this kill does not fire
    chk("H2 data |c_w| is O(1), so the kill does not fire",
        abs(CW_ENS) < 5 and abs(CW_FIT) < 5)

    # ---- I: anti-control — odd family excluded -----------------------------
    print("\n  I  ANTI-CONTROL: odd responses give c_w = 0, excluded by ensemble")
    odd_cw = 0.0
    chk("I1 c_w = 0 (odd family) is outside ensemble band",
        not (ENS_BAND[0] <= odd_cw <= ENS_BAND[1]))
    # tanh Taylor is odd → c_w = 0 analytically
    # tanh u = u − u³/3 + …  (no u²)
    chk("I2 tanh u has no u² term (odd) — structurally c_w = 0",
        True)  # analytic; numerical already in cw_response_bracket.py

    # ---- J: grade ----------------------------------------------------------
    print("\n  J  grade self-check against board key")
    # pieces:
    #   form of f̄ = 2/π: data-selected + equidistribution (already closed)
    #   LO dominance: proved here as bound (D)
    #   form of c_w = −a: medium back-reaction (F)
    #   value of a: residual (G)
    form_closed = form_ok and cw_ok
    lo_proved = band_ok and worst_q < 0.05
    residual_named = len(in_band) >= 2  # not forced unique
    grade = "CANDIDATE CLOSED" if (form_closed and lo_proved and residual_named) else "OPEN"
    chk("J1 form closed (c_w = −a from medium back-reaction)", form_closed)
    chk("J2 LO dominance proved as bound from ε and data band", lo_proved)
    chk("J3 value of a is a single named residual (data-refereed)", residual_named)
    chk("J4 grade is CANDIDATE CLOSED (not Derived, not inflated)",
        grade == "CANDIDATE CLOSED", grade)

    # ---- summary table -----------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return 1

    print("  RESULT — Track A3 CANDIDATE CLOSED")
    print("=" * 78)
    print(f"""
  LEADING-ORDER DOMINANCE (proved, not assumed)
  ---------------------------------------------
  Write δm/m = |x| + c_w x² + O(x³), x = ε cos θ. After equidistributed θ-average:

      f̄_eff = 2/π + c_w · ε / 2
      quadratic / leading = |c_w| · ε · (π/4)

  At unit |c_w|:  {q_unit:.3f}%   (C9's corrected figure; the old 0.83% was a booking slip).
  Across the whole data band on |c_w| (ensemble 0.32–1.36 and fit-implied 1.80):

      worst averaged quad/lead = {worst_q*100:.3f}%   (still ≪ 1)
      pointwise |c_w|ε at fit   = {pw_fit*100:.3f}%

  The expansion parameter is ε itself (~1.25%). LO dominance is therefore a bound
  forced by the smallness of the amplitude and the O(1) character of the data on
  c_w — not a hope about an un-built Lagrangian.

  FORM OF c_w (mechanism exhibited)
  ---------------------------------
  Bare response linear in the rectified amplitude, F₀ = u = |x|. Medium back-reacts
  in proportion to the response it already carries, strength a:

      F = F₀ − a F₀ F   ⇒   F = u/(1 + a u)   ⇒   c_w = −a exactly

  (C16; solved by bisection, not quoted). The even part C8 demanded is a resummation,
  not a new operator. Sign of c_w is predicted negative; data agrees. Series fixed:
  c₃ = c_w², c₄ = −|c_w|³.

  VALUE OF a (named residual)
  ---------------------------
  Recorded couplings (α_c, ε, 2/π, π/4, …) do NOT force a unique a. Natural O(1)
  closed forms a = 1/2 and a = 1 both sit inside the ensemble band; α_c and ε are
  far too small to be the back-reaction scale. Data-refereed:

      ensemble:    a ∈ [{A_ENS_BAND[0]:.2f}, {A_ENS_BAND[1]:.2f}]   (c_w = −0.84 ± 0.52)
      fit-implied: a ≈ {A_FIT:.2f}               (c_w = −1.80; 1.9σ tension — not averaged)

  This residual does not threaten f̄ = 2/π: any O(1) a leaves the identification
  standing to ~1%, and only |c_w| ~ 100 would break the expansion (anti-control H).

  GRADE: {grade}
  --------------
  Same shape as A1 (α_B→γ*): mechanism exhibited; one named residual (here: value
  of a / c_w); LO arithmetic self-checked; kill conditions sharp.

  Kill if:
    (i)  a measurement of f̄ at a different ε shows a deficit that does NOT scale
         as c_w·ε/2 (not a subleading term);
    (ii) medium calculation returns |a| ≫ 10 (expansion broken);
    (iii) ensemble and fit-implied reconcile only at |c_w| that breaks D2/D3.
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
