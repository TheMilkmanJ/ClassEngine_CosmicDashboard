#!/usr/bin/env python3
"""bounce_n4_force_branch_attempt — N4 force-branch theorem kill-seek (2026-08-04).

QUESTION
  Does any stocked argument force exterior H_re > 0 without free P2
  (expanding-branch declaration)?

ANSWER (this script)
  No. FORCE_BRANCH_DERIVED = false.
  Reconfirms FA3: can_derive_H_re_without_declaration = false.

ROLE
  Honest reconfirm + stamp only. Does NOT invent Israel S_ab, K_ab, or a
  force-branch theorem. Writing prose that restates P2 is not a theorem.

FENCES
  - No invent H_re as Derived
  - No free N_med / η land
  - No continuous metric-ON H through 0 sold as exterior FRW
  - No bounce closed · no cyclic booked
  - Leave MCMCs · no PolyChord
  - exit 0 ≠ physics PASS ≠ N4 land

PARENTS
  bounce_residual_demand/CANDIDATE_NEXT.md N4
  israel_junction_content_20260804/GAP_LIST.md G1–G12
  fa3_metric_off P1+P2; scripts/bounce_fa3_hcross_attempt.py
"""
from __future__ import annotations

import json
import math
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
FA3 = REPO / "scripts" / "bounce_fa3_hcross_attempt.py"

# Recorded anchors (same seating as FA3 / M2 — not re-derived here)
ALPHA = 1.0 / 137.036
C_S = math.sqrt(3.0 * ALPHA)


def reconfirm_fa3() -> dict:
    """Run FA3 and parse SUMMARY_JSON; assert can_derive=false."""
    proc = subprocess.run(
        [sys.executable, str(FA3)],
        cwd=str(REPO),
        capture_output=True,
        text=True,
        check=False,
    )
    text = proc.stdout + "\n" + proc.stderr
    if proc.returncode != 0:
        print("FA3 subprocess FAILED")
        print(text[-4000:])
        raise SystemExit(2)

    m = re.search(r"SUMMARY_JSON_BEGIN\s*(\{.*?\})\s*SUMMARY_JSON_END", text, re.S)
    if not m:
        print("FA3 JSON block not found")
        print(text[-2000:])
        raise SystemExit(3)
    data = json.loads(m.group(1))
    assert data.get("can_derive_H_re_without_declaration") is False
    assert data.get("cyclic_cosmology") is False
    return data


def algebraic_obstruction_A_stamp() -> dict:
    """VACUOUS documentation stamp (cannot fail as a physics test).

    Hardcodes H_kin=0 and rho_finite=True then returns obstruction_A_stands=True.
    Real content is FA3 subprocess reconfirm + ARGUMENT_KILL_TABLE.md.
    Sibling israel_sab package labels this class [VACUOUS stamp].
    """
    # Pure algebra: if ρ > 0 and H² = 8πGρ/3, then H ≠ 0.
    # No need for G numbers — sign of RHS at finite ρ is enough.
    rho_finite = True
    H_at_cross_kin = 0.0
    friedmann_requires_H_nonzero = rho_finite
    continuous_exterior_path_legal = not (
        H_at_cross_kin == 0.0 and friedmann_requires_H_nonzero
    )
    return {
        "obstruction_A_stands": True,  # VACUOUS stamp; FA3 subprocess is the real check
        "continuous_metric_ON_H_cross_legal": continuous_exterior_path_legal,
        "H_kin_at_cross": H_at_cross_kin,
        "rho_finite_at_cross": rho_finite,
    }


def argument_verdicts() -> list[dict]:
    """Every candidate force-branch argument → kill or non-land status.

    Codes align with package ARGUMENT_KILL_TABLE.md. None are Derived theorems.
    """
    rows = [
        {
            "id": "FB1",
            "name": "continuous H_kin as exterior H (path A)",
            "verdict": "KILLED",
            "why": "obstruction A: H=0 at finite ρ conflicts FRW",
        },
        {
            "id": "FB2",
            "name": "metric-off then H_re = sign(Θ)|H_F(ρ)|",
            "verdict": "P2_RESTATEMENT",
            "why": "step is expanding-branch declaration, not derivation",
        },
        {
            "id": "FB3",
            "name": "Israel thin shell at re-entry (S-B)",
            "verdict": "MISSING_INPUT",
            "why": "no S_ab, no K_ab, no Israel eq (G1–G3)",
        },
        {
            "id": "FB4",
            "name": "M4 achronality forces expanding root",
            "verdict": "KILLED_AS_THEOREM",
            "why": "constrains when/where attach, not algebraic ±√ root",
        },
        {
            "id": "FB5",
            "name": "FA1 quench / acoustic stress as S_ab",
            "verdict": "KILLED",
            "why": "no surface tensor; does not select exterior H sign",
        },
        {
            "id": "FB6",
            "name": "M2 junction N_med/η dials",
            "verdict": "FORBIDDEN",
            "why": "FABRICATED compression; retired free param",
        },
        {
            "id": "FB7",
            "name": "medium ⟨Θ⟩ turn alone forces exterior root",
            "verdict": "CATEGORY_ERROR",
            "why": "fluid expansion ≠ exterior FRW square-root selection",
        },
        {
            "id": "FB8",
            "name": "H_kin∝Θ selects root in Phase II",
            "verdict": "KILLED",
            "why": "map withdrawn when metric off (G6); A if metric on",
        },
        {
            "id": "FB9",
            "name": "observer / arrow softener (P2_SETS_ARROW)",
            "verdict": "NON_DERIVATION",
            "why": "softens severity of free choice; does not force root",
        },
        {
            "id": "FB10",
            "name": "match-book Phase III dictionary",
            "verdict": "USES_P2",
            "why": "N2 RECONSTRUCTED under P2; does not promote P2",
        },
        {
            "id": "FB11",
            "name": "averaging bulk stress drive",
            "verdict": "MEDIUM_ONLY",
            "why": "PAID fluid layer; exterior H undefined in Phase II",
        },
        {
            "id": "FB12",
            "name": "modified homogeneous constraint (H=0 finite ρ)",
            "verdict": "DEAD",
            "why": "homogeneous engines dead (G12); A stands",
        },
        {
            "id": "FB13",
            "name": "S-A two-map bookkeeping forces root",
            "verdict": "KILLED_AS_THEOREM",
            "why": "two maps are inventory; force still G5",
        },
        {
            "id": "FB14",
            "name": "linguistic ⟨Θ⟩>0 ⇒ expanding exterior",
            "verdict": "P2_RESTATEMENT",
            "why": "confuses fluid gate with exterior H branch choice",
        },
        {
            "id": "FB15",
            "name": "NEC / energy conditions force H_re>0",
            "verdict": "NOT_STOCKED",
            "why": "contracting FRW at finite ρ is NEC-compatible",
        },
        {
            "id": "FB16",
            "name": "Darmois induced-metric continuity alone",
            "verdict": "INSUFFICIENT",
            "why": "h_ab continuous does not fix ± of H from H²",
        },
        {
            "id": "FB17",
            "name": "entropy / C² restoration forces H>0",
            "verdict": "NON_DERIVATION",
            "why": "arrow restored-after is interpretation; N4 still open",
        },
        {
            "id": "FB18",
            "name": "H_kin matching target at re-entry = force",
            "verdict": "CANDIDATE_REFRAME",
            "why": "R1 target ≠ square-root sign derivation",
        },
        {
            "id": "FB19",
            "name": "single-shell Israel across Phase II",
            "verdict": "ILL_POSED",
            "why": "no exterior metric hosts Σ through Phase II (G4/P1)",
        },
        {
            "id": "FB20",
            "name": "M4 white-hole / hold-time joint",
            "verdict": "CONSTRAINT_ONLY",
            "why": "task4 OPEN joint; not Israel force-branch",
        },
    ]
    # Honesty: none may claim FORCE_BRANCH_DERIVED
    for r in rows:
        r["forces_H_re_without_P2"] = False
    return rows


def main() -> None:
    print("=" * 78)
    print("N4 FORCE-BRANCH ATTEMPT — kill-seek + FA3 reconfirm")
    print("  FORCE_BRANCH_DERIVED default false unless real theorem stocked")
    print("  exit 0 = compute done; NOT physics PASS; NOT N4 land")
    print("=" * 78)

    print("\n[1] FA3 reconfirm (can_derive_H_re_without_declaration)")
    fa3 = reconfirm_fa3()
    can_derive = fa3["can_derive_H_re_without_declaration"]
    print(f"  can_derive_H_re_without_declaration = {can_derive}")
    print(f"  grade_O2                           = {fa3.get('grade_O2')}")
    print(f"  obstruction                        = {fa3.get('obstruction')}")
    print(f"  c_s                                = {fa3.get('c_s')}")
    print(
        f"  |H_kin(Θ=1,d=3)|/H_door            = "
        f"{fa3.get('H_kin_over_H_door_Theta1_d3')}"
    )
    assert can_derive is False
    print("  ASSERT OK: FA3 can_derive remains false")

    print("\n[2] Obstruction A algebraic stamp [VACUOUS — cannot fail as physics test]")
    a = algebraic_obstruction_A_stamp()
    for k, v in a.items():
        print(f"  {k} = {v}")
    assert a["obstruction_A_stands"] is True
    assert a["continuous_metric_ON_H_cross_legal"] is False
    print("  ASSERT OK: continuous exterior path illegal at H=0 finite ρ")

    print("\n[3] Argument kill-seek table (FB1–FB20)")
    rows = argument_verdicts()
    n_force = sum(1 for r in rows if r["forces_H_re_without_P2"])
    for r in rows:
        print(f"  {r['id']:4s}  {r['verdict']:20s}  {r['name']}")
    assert n_force == 0
    print(f"  ASSERT OK: {len(rows)} arguments, {n_force} force H_re without P2")

    # Named theorem not stocked — cannot flip stamp by prose
    FORCE_BRANCH_DERIVED = False
    NAMED_THEOREM_STOCKED = False
    bounce_closed = False
    cyclic = False
    p2_is_declaration = True

    print("\n[4] N4 honesty stamps")
    print(f"  FORCE_BRANCH_DERIVED              = {FORCE_BRANCH_DERIVED}")
    print(f"  NAMED_THEOREM_STOCKED             = {NAMED_THEOREM_STOCKED}")
    print(f"  P2_is_declaration                 = {p2_is_declaration}")
    print(f"  bounce_closed                     = {bounce_closed}")
    print(f"  cyclic_cosmology                  = {cyclic}")
    print(f"  c_s / √3 (mag-lock factor d=3)    = {C_S / math.sqrt(3.0):.6f}")

    assert FORCE_BRANCH_DERIVED is False
    assert NAMED_THEOREM_STOCKED is False
    assert p2_is_declaration is True
    assert bounce_closed is False
    assert cyclic is False
    # Cross-check FA3 number
    assert abs(float(fa3["H_kin_over_H_door_Theta1_d3"]) - C_S / math.sqrt(3.0)) < 1e-9

    out = {
        "package": "n4_force_branch_20260804",
        "exit_means": "compute_done_not_physics_PASS",
        "FORCE_BRANCH_DERIVED": False,
        "NAMED_THEOREM_STOCKED": False,
        "can_derive_H_re_without_declaration": False,
        "P2_is_declaration": True,
        "obstruction_A_stands": True,
        "arguments_examined": len(rows),
        "arguments_forcing_H_re_without_P2": 0,
        "argument_ids": [r["id"] for r in rows],
        "fa3_grade_O2": fa3.get("grade_O2"),
        "c_s": C_S,
        "H_kin_over_H_door_Theta1_d3": C_S / math.sqrt(3.0),
        "bounce_closed": False,
        "cyclic_cosmology": False,
        "lands": 0,
        "grade": "OPEN_MISSING_INPUT_N4_FORCE_BRANCH_false",
        "promotion_requires": (
            "named_proof_form: legal_gate + (S_ab,K_ab or acoustic axioms) "
            "=> unique H_re>0; contracting root inconsistent"
        ),
    }

    print("\nSUMMARY_JSON_BEGIN")
    print(json.dumps(out, indent=2))
    print("SUMMARY_JSON_END")
    print("\nASSERTS OK — FORCE_BRANCH_DERIVED false; FA3 can_derive false; 0 lands.")
    print("NO FABRICATIONS. exit 0 ≠ PASS.")


if __name__ == "__main__":
    main()
