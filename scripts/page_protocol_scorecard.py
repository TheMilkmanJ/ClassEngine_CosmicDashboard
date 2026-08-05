#!/usr/bin/env python3
"""Recompute R-PAGE protocol scorecard T1–T8 from JSON arrays only.

Loads candidate_rebuild-style JSON (history_full / n1|n2|n3 histories) or
coevolve-style JSON with equivalent history keys. Recomputes tests from the
stored arrays — no hand numbers, no re-simulation.

T1–T7 logic mirrors scripts/quantum_page_candidate_rebuild.py::eval_protocol
(and PAGE_TURN_ACCEPTANCE_PROTOCOL.md §4 / §4.2).

T8 (PAGE_TURN_ACCEPTANCE_PROTOCOL.md §4.3) — ACTIVE / BINDING:
  For bins of u = max-envelope v with width Δu = 0.01, S range within each
  occupied bin must satisfy max S − min S ≤ 0.1 · S★; report worst bin.
  CANDIDATE_TURN_binding requires T1–T6 and T8_pass (T7 claim flag always false).

DC3 weight-invariant reach (Claude open-board-split):
  When histories + schedule_pins (or per-frame w_c / e_c_raw) allow it, recompute
  v with core frequency weight frozen at initial value. If frozen envelope
  v < 0.9 while dynamic reach claimed ≥ 0.9, FAIL and gate CANDIDATE_TURN_binding.
  If not computable → weight_invariant_reach: NOT_COMPUTABLE (no invented numbers).
  design.no_v_blend is STRUCTURAL_PURE_ENERGY_FRACTION (DC2), not a DC3 pass.

Claim-decoupling (§4.4): run this only after the producing run JSON is on disk;
never file a CANDIDATE packet in the same step as the first write of that JSON.

This script NEVER sets page_curve_claimed true (always false in output).

Resource: OMP=1. No PolyChord. No MCMC.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any

import numpy as np

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

# T8 pins — ACTIVE / BINDING (ChatGPT REFEREE batch9-T8-claim-decoupling)
T8_BIN_WIDTH = 0.01
T8_RANGE_FRAC = 0.10
T8_STATUS = "ACTIVE_BINDING"


def monotone_envelope(vlist: list[float]) -> list[float]:
    """Registered stall treatment (protocol §4.2): u(t)=max_{s≤t} v(s)."""
    u: list[float] = []
    m = 0.0
    for v in vlist:
        m = max(m, float(v))
        u.append(m)
    return u


def _frame_S_rad(frame: Any) -> float:
    if isinstance(frame, dict):
        for k in ("S_rad", "S", "s_rad"):
            if k in frame:
                return float(frame[k])
        raise KeyError(f"frame missing S_rad; keys={list(frame.keys())[:12]}")
    return float(frame)


def _frame_v(frame: Any) -> float:
    if isinstance(frame, dict):
        if "v" in frame:
            return float(frame["v"])
        if "E_rad" in frame and "E_core" in frame:
            er = float(frame["E_rad"])
            ec = float(frame["E_core"])
            return er / (er + ec + 1e-30) if (er + ec) > 1e-14 else 0.0
        raise KeyError(f"frame missing v; keys={list(frame.keys())[:12]}")
    raise TypeError("v requires dict frames with v or E_rad/E_core")


def _frame_S_total(frame: Any) -> float:
    if isinstance(frame, dict) and "S_total" in frame:
        return float(frame["S_total"])
    return 0.0


def _pick_hist(data: dict, *keys: str) -> list | None:
    for k in keys:
        if k in data and data[k] is not None:
            h = data[k]
            if isinstance(h, list) and len(h) > 0:
                return h
    return None


def load_histories(data: dict) -> tuple[list, list, list, list, dict]:
    """Extract main + null histories from candidate_rebuild or coevolve JSON."""
    meta: dict[str, Any] = {"loader": "page_protocol_scorecard"}

    # Coevolve nested package
    if "coevolve" in data and isinstance(data["coevolve"], dict):
        data = {**data, **data["coevolve"]}
        meta["source"] = "coevolve_nested"

    hist = _pick_hist(
        data,
        "history_full",
        "history",
        "unitary_hist",
        "hist",
        "main_history",
        "coevolve_history",
    )
    if hist is None and "snapshots" in data and isinstance(data["snapshots"], list):
        hist = data["snapshots"]
        meta["hist_key"] = "snapshots"
    if hist is None:
        raise ValueError(
            "No main history found. Expected one of: history_full, history, "
            "unitary_hist, hist, main_history, coevolve_history, snapshots"
        )
    meta.setdefault("hist_key", "history_full" if "history_full" in data else "history")

    h_n1 = _pick_hist(
        data,
        "n1_history_full",
        "n1_history",
        "null_n1_history",
        "hist_n1",
        "null_g0_history",
    )
    h_n2 = _pick_hist(
        data,
        "n2_history_full",
        "n2_history",
        "null_n2_history",
        "hist_n2",
        "thermal_hist",
    )
    h_n3 = _pick_hist(
        data,
        "n3_history_full",
        "n3_history",
        "null_n3_history",
        "hist_n3",
        "null_vacuum_history",
    )

    # Scalar null series fallbacks (S-only arrays)
    if h_n1 is None and "null_g0_S_series" in data:
        h_n1 = [{"S_rad": float(s), "v": 0.0, "S_total": 0.0} for s in data["null_g0_S_series"]]
        meta["n1_from"] = "null_g0_S_series"
    if h_n3 is None and "null_vacuum_S_series" in data:
        h_n3 = [{"S_rad": float(s), "v": 0.0, "S_total": 0.0} for s in data["null_vacuum_S_series"]]
        meta["n3_from"] = "null_vacuum_S_series"

    missing = [name for name, h in (("n1", h_n1), ("n2", h_n2), ("n3", h_n3)) if h is None]
    if missing:
        meta["nulls_missing"] = missing
        # Provide empty-safe placeholders so T4 fails cleanly rather than crashing
        empty = [{"S_rad": 1.0, "v": 0.0, "S_total": 0.0}]  # max S=1 → N1/N3 fail
        if h_n1 is None:
            h_n1 = empty
        if h_n2 is None:
            # second-half drop large → N2 fails open (conservative)
            h_n2 = [{"S_rad": 1.0, "v": 0.0, "S_total": 0.0} for _ in range(4)] + [
                {"S_rad": 0.0, "v": 1.0, "S_total": 0.0}
            ]
        if h_n3 is None:
            h_n3 = empty

    return hist, h_n1, h_n2, h_n3, meta


def eval_protocol_t1_t7(hist: list, h_n1: list, h_n2: list, h_n3: list) -> dict:
    """Scorecard T1–T7 from full history arrays only (copy of rebuild eval_protocol).

    Claude open-board-split R-A cure (2026-08-03): T3 credits only entropy rise
    that co-occurs with advancing u (du > 0). Rise at frozen u earns no T3 credit
    (protocol §4.3 T8 companion).
    """
    S = [_frame_S_rad(h) for h in hist]
    v_raw = [_frame_v(h) for h in hist]
    vlist = monotone_envelope(v_raw)
    i_pk = int(np.argmax(S))
    S_peak, S_late = S[i_pk], S[-1]
    v_star, v_late = vlist[i_pk], vlist[-1]
    drop = S_peak - S_late
    S_early = S[0]
    S_n1 = np.array([_frame_S_rad(h) for h in h_n1], dtype=float)
    S_n2 = np.array([_frame_S_rad(h) for h in h_n2], dtype=float)
    S_n3 = np.array([_frame_S_rad(h) for h in h_n3], dtype=float)
    sig1 = max(float(np.std(S_n1)), float(np.max(np.abs(S_n1))), 1e-8)
    sig3 = max(float(np.std(S_n3)), float(np.max(np.abs(S_n3))), 1e-8)
    sigma_jit = max(sig1, sig3)

    # --- co-evolution diagnostics from arrays (Claude R-C gates) ---
    S_arr = np.array(S, dtype=float)
    u_arr = np.array(vlist, dtype=float)
    v_arr = np.array(v_raw, dtype=float)
    dS = np.diff(S_arr)
    du = np.diff(u_arr)
    DU_GATE = 1e-9
    rise = np.maximum(dS, 0.0)
    rise_total = float(np.sum(rise))
    rise_with_du = float(np.sum(rise[du > DU_GATE])) if len(rise) else 0.0
    frac_rise_du = (rise_with_du / rise_total) if rise_total > 1e-30 else float("nan")
    # longest consecutive stall with any positive dS
    stall_len = 0
    cur = 0
    for i in range(len(du)):
        if du[i] <= DU_GATE:
            cur += 1
            stall_len = max(stall_len, cur)
        else:
            cur = 0
    # peak-in-motion: du > 0 within ±5 frames of argmax S
    lo = max(0, i_pk - 5)
    hi = min(len(du), i_pk + 5)
    peak_in_motion = bool(np.any(du[lo:hi] > DU_GATE)) if hi > lo else False
    # swap-back: max(u - v_raw) before peak
    if i_pk > 0:
        swap_back = float(np.max(u_arr[: i_pk + 1] - v_arr[: i_pk + 1]))
    else:
        swap_back = 0.0
    # S rise credited only on advancing-u frames (T3 cure)
    # Integrate positive dS where du>0 up to peak; compare to early
    if i_pk > 0:
        rise_to_peak = rise[:i_pk]
        du_to_peak = du[:i_pk]
        S_rise_credited = float(np.sum(rise_to_peak[du_to_peak > DU_GATE]))
    else:
        S_rise_credited = 0.0
    # also allow path where S itself increases while u advances continuously
    # T3: credited rise must exceed 0.05 * S_peak
    T3 = S_rise_credited > 0.05 * max(S_peak, 1e-15)
    T3_raw_any_rise = S_peak > S_early + 0.05 * max(S_peak, 1e-15)

    T1 = 0.05 <= v_star <= 0.95 and 0 < i_pk < len(S) - 1
    T2_reach = v_late >= 0.9
    T2_frac = drop >= 0.10 * S_peak if S_peak > 0 else False
    T2_noise = drop > 5.0 * sigma_jit
    T2 = bool(T2_reach and T2_frac and T2_noise)
    N1 = float(np.max(S_n1)) < 1e-4
    second = S_n2[len(S_n2) // 2 :]
    drop2 = float(np.max(second) - second[-1]) if len(second) else 0.0
    N2 = drop2 < 0.10 * max(float(np.max(second)), 1e-15)
    N3 = float(np.max(S_n3)) < 1e-4
    max_abs_Stot = max(abs(_frame_S_total(h)) for h in hist)
    N4 = max_abs_Stot < 0.05
    T4 = bool(N1 and N2 and N3 and N4)
    # T5/T6 are structural: arrays-only recompute cannot re-prove continuum dynamics.
    # Match rebuild eval_protocol defaults; artifact presence is T6 evidence here.
    T5 = True
    T5_caveat = (
        "arrays-only recompute: T5 not re-proven from S/v series; "
        "inherits structural True as in candidate_rebuild.eval_protocol "
        "(field + continuum modes must be present in producing run)"
    )
    T6 = True  # we are reading full histories from disk
    T7 = False  # claim flag never auto-set
    # Run-validity (Claude R-C): stall >10 consecutive frames voids candidate path
    stall_cap_ok = stall_len <= 10
    co_frac_ok = (frac_rise_du >= 0.70) if frac_rise_du == frac_rise_du else False
    swap_ok = swap_back <= 0.05
    candidate = bool(
        T1 and T2 and T3 and T4 and T5 and T6 and stall_cap_ok and co_frac_ok and swap_ok and peak_in_motion
    )

    return {
        "T1_interior_max": bool(T1),
        "T2_reach_v_ge_0.9": bool(T2_reach),
        "T2_frac_drop": bool(T2_frac),
        "T2_noise_floor": bool(T2_noise),
        "T2_all": T2,
        "T3_early_rise": bool(T3),
        "T3_raw_any_rise_not_used": bool(T3_raw_any_rise),
        "T3_definition": (
            "credited S rise only on frames with du>1e-9 (Claude R-A cure); "
            f"S_rise_credited={S_rise_credited:.6g}"
        ),
        "T4_nulls": T4,
        "N1": bool(N1),
        "N2_thermal_no_turn": bool(N2),
        "N2_drop": float(drop2),
        "N3": bool(N3),
        "N4_unitarity": bool(N4),
        "T5_strict_dynamical_continuum": bool(T5),
        "T5_caveat": T5_caveat,
        "T6_artifacts": bool(T6),
        "T7_claim_flag": bool(T7),
        "CANDIDATE_TURN": candidate,
        "page_curve_claimed": False,  # NEVER true from this tool
        "v_star": float(v_star),
        "v_late": float(v_late),
        "v_raw_at_peak": float(v_raw[i_pk]),
        "v_raw_late": float(v_raw[-1]),
        "v_definition": (
            "pure E_rad/(E_rad+E_core) or stored v; scorecard uses monotone "
            "envelope u=max_{s<=t} v(s) per protocol §4.2"
        ),
        "S_peak": float(S_peak),
        "S_late": float(S_late),
        "drop": float(drop),
        "sigma_jit": float(sigma_jit),
        "i_peak": i_pk,
        "n_frames": len(hist),
        "max_abs_S_total": float(max_abs_Stot),
        "coevolution_gates": {
            "stall_cap_ok": bool(stall_cap_ok),
            "longest_stall_frames": int(stall_len),
            "stall_cap": 10,
            "frac_S_rise_while_u_advances": float(frac_rise_du),
            "co_frac_ok_ge_0.70": bool(co_frac_ok),
            "swap_back_max_u_minus_v": float(swap_back),
            "swap_ok_le_0.05": bool(swap_ok),
            "peak_in_motion": bool(peak_in_motion),
            "S_rise_credited_du_gt0": float(S_rise_credited),
        },
        "scorecard_source": "page_protocol_scorecard.eval_protocol_t1_t7(full history arrays only)",
        "u_envelope": vlist,  # for T8; stripped from slim print if huge
    }


def eval_t8(hist: list, u_envelope: list[float] | None = None) -> dict:
    """T8 ACTIVE/BINDING: single-valued S(u) in Δu=0.01 bins.

    For each bin of u=max-envelope v, range(S) ≤ 0.1 * S★.
    """
    S = np.array([_frame_S_rad(h) for h in hist], dtype=float)
    if u_envelope is None:
        v_raw = [_frame_v(h) for h in hist]
        u = np.array(monotone_envelope(v_raw), dtype=float)
    else:
        u = np.array(u_envelope, dtype=float)

    S_star = float(np.max(S)) if len(S) else 0.0
    thr = T8_RANGE_FRAC * S_star if S_star > 0 else 0.0

    # Bin by floor(u / Δu); include edge u=1 in last bin
    bin_idx = np.floor(u / T8_BIN_WIDTH).astype(int)
    # Cap so u exactly 1.0 stays in a finite bin
    max_bin = int(np.floor(1.0 / T8_BIN_WIDTH))
    bin_idx = np.clip(bin_idx, 0, max_bin)

    worst = {
        "bin_lo": None,
        "bin_hi": None,
        "n_points": 0,
        "S_min": None,
        "S_max": None,
        "S_range": -1.0,
        "S_range_over_S_star": None,
        "pass": True,
    }
    bins_out: list[dict] = []
    all_pass = True
    n_occupied = 0

    for b in sorted(set(bin_idx.tolist())):
        mask = bin_idx == b
        n_pts = int(np.sum(mask))
        if n_pts == 0:
            continue
        n_occupied += 1
        Ss = S[mask]
        smin = float(np.min(Ss))
        smax = float(np.max(Ss))
        srange = smax - smin
        ratio = (srange / S_star) if S_star > 0 else 0.0
        ok = srange <= thr + 1e-15
        if not ok:
            all_pass = False
        rec = {
            "bin_lo": float(b * T8_BIN_WIDTH),
            "bin_hi": float((b + 1) * T8_BIN_WIDTH),
            "n_points": n_pts,
            "S_min": smin,
            "S_max": smax,
            "S_range": float(srange),
            "S_range_over_S_star": float(ratio),
            "pass": bool(ok),
        }
        bins_out.append(rec)
        if srange > float(worst["S_range"]):
            worst = dict(rec)

    return {
        "T8_status": T8_STATUS,
        "T8_binding": True,
        "T8_definition": (
            f"for bins of u=max-envelope v with width {T8_BIN_WIDTH}, "
            f"S range within bin <= {T8_RANGE_FRAC} * S_star; report worst bin"
        ),
        "T8_bin_width": T8_BIN_WIDTH,
        "T8_range_frac": T8_RANGE_FRAC,
        "S_star": S_star,
        "threshold": float(thr),
        "n_occupied_bins": n_occupied,
        "T8_pass": bool(all_pass and n_occupied > 0),
        "worst_bin": worst,
        # keep only failing bins + summary to avoid huge dumps; full on request
        "failing_bins": [b for b in bins_out if not b["pass"]],
        "note": (
            "ACTIVE/BINDING — CANDIDATE_TURN_binding requires T8_pass. "
            "page_curve_claimed stays false until red AGREE + claim-decoupling."
        ),
    }


# backward-compatible alias
eval_proposed_t8 = eval_t8


# DC3 (Claude open-board-split): reach must be quanta-borne, not weight-borne.
# energy_cov uses f-dependent core free frequency w_c(f); decaying w_c shrinks
# E_core and can inflate v without transferring quanta. Frozen-weight recompute
# holds w_c at its initial value (1.0) when inverting stored energies.
W_C_FLOOR = 0.005  # matches quantum_page_coevolve / candidate_rebuild
WEIGHT_INVARIANT_V_THRESH = 0.9


def _schedule_w_c(f: float, hold: float, decay: float, floor: float = W_C_FLOOR) -> float:
    if f <= hold:
        return 1.0
    return max(float(np.exp(-decay * (f - hold))), floor)


def _frame_energy_pair(frame: dict) -> tuple[float, float] | None:
    if not isinstance(frame, dict):
        return None
    if "E_rad" in frame and "E_core" in frame:
        return float(frame["E_core"]), float(frame["E_rad"])
    return None


def eval_weight_invariant_reach(hist: list, data: dict) -> dict:
    """Claude DC3: v ≥ 0.9 must survive frozen frequency-weight recompute.

    Honest sources of audit data (first match wins):
      1. Per-frame e_c_raw (or E_core_raw) + E_rad — direct quanta-borne energies
         with w_c frozen at 1; optional per-frame w_c for diagnostics.
      2. Per-frame E_core/E_rad + w_c (stored) — invert E_core/w_c → excess,
         then E_core_frozen = excess * w_c0 with w_c0=1.
      3. Per-frame E_core/E_rad/f + top-level schedule_pins W_C_HOLD/W_C_DECAY
         — reconstruct w_c(f) and invert (assumes coevolve energy_cov formula).

    If none of the above is available → status NOT_COMPUTABLE (no invented numbers).

    Structural note (not a pass of DC3): design.no_v_blend / pure energy v_definition
    only certifies DC2 (no schedule blend *into the v line*); absolute energy may
    still use time-dependent free frequencies.
    """
    design = data.get("design") if isinstance(data.get("design"), dict) else {}
    pins = data.get("schedule_pins") if isinstance(data.get("schedule_pins"), dict) else {}
    v_def = str(design.get("v_definition") or data.get("v_definition") or "")
    no_v_blend = bool(design.get("no_v_blend", False))
    pure_energy_claim = no_v_blend or (
        "E_rad" in v_def and "E_core" in v_def and "blend" not in v_def.lower()
    )

    structural = {
        "design_no_v_blend": no_v_blend,
        "v_definition": v_def or None,
        "structural_tag": (
            "STRUCTURAL_PURE_ENERGY_FRACTION" if pure_energy_claim else "NO_STRUCTURAL_CLAIM"
        ),
        "structural_caveat": (
            "no_v_blend / pure E_rad/(E_rad+E_core) is DC2 (coordinate hygiene): v is not "
            "a schedule blend. Absolute E_core may still weight gamma diagonals by a "
            "time-dependent free frequency w_c(f); that is the DC3 weight-borne reach risk. "
            "STRUCTURAL_PURE_ENERGY_FRACTION is NOT a pass of weight-invariant reach."
        ),
    }

    if not hist or not isinstance(hist[0], dict):
        return {
            "weight_invariant_reach": "NOT_COMPUTABLE",
            "weight_invariant_ok": None,
            "computable": False,
            "reason": "history frames are not dicts with energy fields",
            "gates_binding_when_available": True,
            **structural,
        }

    n = len(hist)
    has_ec_raw = sum(
        1 for h in hist if isinstance(h, dict) and ("e_c_raw" in h or "E_core_raw" in h)
    )
    has_w_c = sum(1 for h in hist if isinstance(h, dict) and "w_c" in h)
    has_E = sum(1 for h in hist if _frame_energy_pair(h) is not None)
    has_f = sum(1 for h in hist if isinstance(h, dict) and "f" in h)

    method = None
    method_detail = None
    hold = pins.get("W_C_HOLD")
    decay = pins.get("W_C_DECAY")

    if has_ec_raw == n and has_E == n:
        method = "e_c_raw_stored"
        method_detail = (
            "per-frame e_c_raw/E_core_raw (occupation excess at unit weight) + E_rad"
        )
    elif has_w_c == n and has_E == n:
        method = "w_c_stored_invert"
        method_detail = "per-frame w_c + invert E_core/w_c → excess at w_c0=1"
    elif (
        has_E == n
        and has_f == n
        and hold is not None
        and decay is not None
    ):
        method = "schedule_pins_reconstruct"
        method_detail = (
            f"reconstruct w_c(f) from schedule_pins "
            f"W_C_HOLD={hold}, W_C_DECAY={decay}, floor={W_C_FLOOR}; "
            "invert E_core/w_c (assumes energy_cov linear in w_c)"
        )
    else:
        missing = []
        if has_ec_raw < n:
            missing.append(
                f"e_c_raw/E_core_raw present on {has_ec_raw}/{n} frames"
            )
        if has_w_c < n:
            missing.append(f"w_c present on {has_w_c}/{n} frames")
        if has_E < n:
            missing.append(f"E_core/E_rad present on {has_E}/{n} frames")
        if has_f < n:
            missing.append(f"f present on {has_f}/{n} frames")
        if hold is None or decay is None:
            missing.append(
                "schedule_pins missing W_C_HOLD and/or W_C_DECAY "
                f"(hold={hold!r}, decay={decay!r})"
            )
        return {
            "weight_invariant_reach": "NOT_COMPUTABLE",
            "weight_invariant_ok": None,
            "computable": False,
            "reason": (
                "cannot recompute frozen-weight v from stored arrays alone; "
                "need per-frame e_c_raw (preferred), or w_c+E_*, or E_*+f+"
                "schedule_pins W_C_HOLD/W_C_DECAY. Gamma diagonals are not stored."
            ),
            "missing": missing,
            "gates_binding_when_available": True,
            "note": (
                "Producing scripts should store e_c_raw and w_c per frame for DC3 audit "
                "(see quantum_page_coevolve energy_cov). Do not invent frozen v numbers."
            ),
            **structural,
        }

    v_frozen: list[float] = []
    w_series: list[float] = []
    e_c_frozen_series: list[float] = []
    for h in hist:
        assert isinstance(h, dict)
        ec_er = _frame_energy_pair(h)
        assert ec_er is not None
        e_c, e_r = ec_er

        if method == "e_c_raw_stored":
            e_c_raw = float(h["e_c_raw"] if "e_c_raw" in h else h["E_core_raw"])
            w = float(h["w_c"]) if "w_c" in h else float("nan")
            e_c_fr = max(e_c_raw, 0.0)  # unit weight
        elif method == "w_c_stored_invert":
            w = float(h["w_c"])
            if w > 1e-30:
                e_c_raw = e_c / w
            else:
                e_c_raw = 0.0
            e_c_fr = max(e_c_raw, 0.0)
        else:  # schedule_pins_reconstruct
            f = float(h["f"])
            w = _schedule_w_c(f, float(hold), float(decay))
            if w > 1e-30:
                e_c_raw = e_c / w
            else:
                e_c_raw = 0.0
            e_c_fr = max(e_c_raw, 0.0)

        w_series.append(float(w) if w == w else float("nan"))
        e_c_frozen_series.append(float(e_c_fr))
        if (e_r + e_c_fr) > 1e-14:
            v_frozen.append(float(e_r / (e_r + e_c_fr + 1e-30)))
        else:
            v_frozen.append(0.0)

    u_frozen = monotone_envelope(v_frozen)
    v_fr_late = float(v_frozen[-1])
    u_fr_late = float(u_frozen[-1])
    v_dyn_raw_late = float(_frame_v(hist[-1]))
    # T2 uses envelope of dynamic v; DC3 apples-to-apples uses envelope of frozen v
    ok = bool(u_fr_late >= WEIGHT_INVARIANT_V_THRESH)
    status = "PASS" if ok else "FAIL"

    # collapse diagnostic (red's "0.9 → 0.12" class)
    dyn_env = monotone_envelope([_frame_v(h) for h in hist])
    collapse = float(dyn_env[-1] - u_fr_late)

    return {
        "weight_invariant_reach": status,
        "weight_invariant_ok": ok,
        "computable": True,
        "method": method,
        "method_detail": method_detail,
        "v_threshold": WEIGHT_INVARIANT_V_THRESH,
        "v_frozen_raw_late": v_fr_late,
        "v_frozen_envelope_late": u_fr_late,
        "v_dynamic_raw_late": v_dyn_raw_late,
        "v_dynamic_envelope_late": float(dyn_env[-1]),
        "reach_collapse_dyn_env_minus_frozen_env": collapse,
        "w_c_late": float(w_series[-1]) if w_series else None,
        "w_c_min": float(np.nanmin(w_series)) if w_series else None,
        "e_c_frozen_late": float(e_c_frozen_series[-1]) if e_c_frozen_series else None,
        "gates_binding_when_available": True,
        "definition": (
            "Recompute v with core frequency weight frozen at initial w_c0=1.0. "
            "PASS iff monotone envelope of frozen-weight v reaches ≥ 0.9 "
            "(quanta-borne reach; Claude DC3). FAIL is the v-blend-one-level-down "
            "deny-on-sight class when dynamic envelope ≥ 0.9 but frozen does not."
        ),
        "honesty_limits": (
            "Radiation weights use stored E_rad as-is (omega_r fixed in coevolve). "
            "Invert path assumes E_core = w_c * e_c_raw and max(·,0) clamp; "
            "if E_core was floored at 0 while raw excess was negative, excess is "
            "under-reported as 0. Gamma diagonals themselves are not in the artifact. "
            "Preferred future store: per-frame w_c and e_c_raw (no invert)."
        ),
        **structural,
    }


def build_scorecard(data: dict, input_path: Path | None = None) -> dict:
    hist, h1, h2, h3, load_meta = load_histories(data)
    pe = eval_protocol_t1_t7(hist, h1, h2, h3)
    u_env = pe.pop("u_envelope")
    t8 = eval_t8(hist, u_env)
    dc3 = eval_weight_invariant_reach(hist, data)

    script_path = Path(__file__).resolve()
    script_sha = hashlib.sha256(script_path.read_bytes()).hexdigest()
    # Claude red theory-construction AGREE finding (2026-08-04): write-once must
    # evidence the input artifact bytes, not only tool/script sha256.
    input_sha = None
    if input_path is not None:
        try:
            input_sha = hashlib.sha256(Path(input_path).read_bytes()).hexdigest()
        except OSError:
            input_sha = None

    # Provenance of producing run if present
    run_prov = data.get("provenance") if isinstance(data.get("provenance"), dict) else {}

    t1_t6 = bool(pe["CANDIDATE_TURN"])  # pe flag is T1–T6 machine score
    t8_pass = bool(t8["T8_pass"])
    # DC3 gates binding when computable; NOT_COMPUTABLE does not invent a pass
    # and does not auto-fail older artifacts that lack audit fields.
    dc3_ok = dc3.get("weight_invariant_ok")
    dc3_blocks = bool(dc3.get("computable") and dc3_ok is False)
    binding_candidate = bool(t1_t6 and t8_pass and not dc3_blocks)

    scorecard = {
        "tool": "scripts/page_protocol_scorecard.py",
        "tool_sha256": script_sha,
        "input_path": str(input_path) if input_path else None,
        "input_sha256": input_sha,
        "input_milestone": data.get("milestone"),
        "load_meta": load_meta,
        "page_curve_claimed": False,  # hard fence — never true
        "protocol_binding_T1_T7": pe,
        "protocol_binding_T8": t8,
        "protocol_proposed_T8": t8,  # alias for older readers
        "weight_invariant_reach": dc3,  # Claude DC3 diagnostic
        "CANDIDATE_TURN_T1_T6_only": t1_t6,
        "CANDIDATE_TURN_binding": binding_candidate,  # T1–T6 + T8 + DC3 if computable
        "CANDIDATE_TURN_if_T8_were_binding": binding_candidate,  # alias
        "DC3_weight_invariant_gated_binding": bool(dc3.get("computable")),
        "run_provenance": run_prov,
        "resource": "OMP=1; no PolyChord; no MCMC; arrays-only recompute",
        "claim_decoupling": (
            "CANDIDATE packet only after: run complete → JSON on disk → "
            "scorecard from arrays → input_sha256 + script sha256 → "
            "(git commit when owner allows). "
            "This scorecard is not itself a CANDIDATE filing."
        ),
    }
    return scorecard


def _print_scorecard(sc: dict) -> None:
    pe = sc["protocol_binding_T1_T7"]
    t8 = sc.get("protocol_binding_T8") or sc["protocol_proposed_T8"]
    wb = t8.get("worst_bin") or {}
    print("=" * 60)
    print("R-PAGE protocol scorecard (arrays-only recompute)")
    print("=" * 60)
    print(f"input: {sc.get('input_path')}")
    print(f"milestone: {sc.get('input_milestone')}")
    isha = sc.get("input_sha256") or ""
    print(f"input_sha256: {(isha[:16] + '…') if isha else 'None'}")
    print(f"tool_sha256: {sc['tool_sha256'][:16]}…")
    print(f"page_curve_claimed: {sc['page_curve_claimed']}  (never set true by this tool)")
    print()
    print("--- BINDING T1–T7 ---")
    print(f"  T1 interior max:     {pe['T1_interior_max']}  (u*={pe['v_star']:.4f})")
    print(f"  T2 reach u>=0.9:     {pe['T2_reach_v_ge_0.9']}  (u_late={pe['v_late']:.4f})")
    print(f"  T2 frac/noise:       {pe['T2_frac_drop']}/{pe['T2_noise_floor']}  → T2_all={pe['T2_all']}")
    print(f"  T3 early rise:       {pe['T3_early_rise']}")
    print(
        f"  T4 nulls:            {pe['T4_nulls']}  "
        f"(N1={pe['N1']} N2={pe['N2_thermal_no_turn']} N3={pe['N3']} N4={pe['N4_unitarity']})"
    )
    print(f"  T5 continuum:        {pe['T5_strict_dynamical_continuum']}")
    print(f"  T6 artifacts:        {pe['T6_artifacts']}")
    print(f"  T7 claim flag:       {pe['T7_claim_flag']}")
    print(f"  T1–T6 machine:       {pe['CANDIDATE_TURN']}")
    print(f"  drop={pe['drop']:.6f}  S*={pe['S_peak']:.6f}  sigma_jit={pe['sigma_jit']:.3e}")
    print()
    print(f"--- BINDING T8 ({t8['T8_status']}; binding={t8['T8_binding']}) ---")
    print(f"  T8_pass:             {t8['T8_pass']}")
    print(f"  S_star:              {t8['S_star']:.6f}")
    print(f"  threshold 0.1*S*:    {t8['threshold']:.6f}")
    print(f"  occupied bins:       {t8['n_occupied_bins']}")
    print(
        f"  worst bin:           [{wb.get('bin_lo')}, {wb.get('bin_hi')})  "
        f"range={wb.get('S_range')}  range/S*={wb.get('S_range_over_S_star')}  "
        f"n={wb.get('n_points')}  pass={wb.get('pass')}"
    )
    print(f"  failing bins:        {len(t8.get('failing_bins') or [])}")
    print()
    dc3 = sc.get("weight_invariant_reach") or {}
    print("--- DC3 weight-invariant reach (Claude) ---")
    print(f"  status:              {dc3.get('weight_invariant_reach')}")
    print(f"  computable:          {dc3.get('computable')}")
    if dc3.get("computable"):
        print(
            f"  v_frozen env/raw:    {dc3.get('v_frozen_envelope_late'):.4f} / "
            f"{dc3.get('v_frozen_raw_late'):.4f}  "
            f"(dyn env={dc3.get('v_dynamic_envelope_late'):.4f})"
        )
        print(f"  method:              {dc3.get('method')}")
        print(f"  weight_invariant_ok: {dc3.get('weight_invariant_ok')}")
    else:
        print(f"  reason:              {dc3.get('reason', '')[:90]}")
    print(f"  structural_tag:      {dc3.get('structural_tag')}")
    print()
    print(f"CANDIDATE_TURN_T1_T6_only:        {sc.get('CANDIDATE_TURN_T1_T6_only')}")
    print(
        f"CANDIDATE_TURN_binding (T1–T8+DC3): {sc['CANDIDATE_TURN_binding']}  "
        f"(DC3 gates when computable={sc.get('DC3_weight_invariant_gated_binding')})"
    )
    print("page_curve_claimed remains false — this is not a CANDIDATE filing.")
    print("=" * 60)


def default_out_path(input_path: Path) -> Path:
    """Write scorecard next to input: <stem>_scorecard_recompute.json"""
    return input_path.with_name(input_path.stem + "_scorecard_recompute.json")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Recompute R-PAGE T1–T8 (binding) from JSON history arrays"
    )
    p.add_argument(
        "input_json",
        type=Path,
        help="candidate_rebuild.json or coevolve-style page-curve artifact",
    )
    p.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="output scorecard JSON (default: <input>_scorecard_recompute.json next to input)",
    )
    p.add_argument(
        "--no-write",
        action="store_true",
        help="print only; do not write scorecard JSON",
    )
    p.add_argument(
        "--include-all-bins",
        action="store_true",
        help="include every occupied T8 bin in the JSON (default: worst + failing only)",
    )
    args = p.parse_args(argv)

    inp = args.input_json
    if not inp.is_file():
        print(f"ERROR: input not found: {inp}", file=sys.stderr)
        return 2

    data = json.loads(inp.read_text())
    sc = build_scorecard(data, input_path=inp.resolve())

    # Hard fence: never allow claimed true
    sc["page_curve_claimed"] = False
    sc["protocol_binding_T1_T7"]["page_curve_claimed"] = False
    sc["protocol_binding_T1_T7"]["T7_claim_flag"] = False

    if args.include_all_bins:
        # recompute with full bin list attached
        hist, h1, h2, h3, _ = load_histories(data)
        pe = eval_protocol_t1_t7(hist, h1, h2, h3)
        u_env = pe.pop("u_envelope")
        t8_full = eval_proposed_t8(hist, u_env)
        # attach all bins by re-deriving quickly
        S = np.array([_frame_S_rad(h) for h in hist], dtype=float)
        u = np.array(u_env, dtype=float)
        bin_idx = np.clip(np.floor(u / T8_BIN_WIDTH).astype(int), 0, int(np.floor(1.0 / T8_BIN_WIDTH)))
        all_bins = []
        for b in sorted(set(bin_idx.tolist())):
            mask = bin_idx == b
            Ss = S[mask]
            smin, smax = float(Ss.min()), float(Ss.max())
            srange = smax - smin
            S_star = t8_full["S_star"]
            all_bins.append(
                {
                    "bin_lo": float(b * T8_BIN_WIDTH),
                    "bin_hi": float((b + 1) * T8_BIN_WIDTH),
                    "n_points": int(mask.sum()),
                    "S_min": smin,
                    "S_max": smax,
                    "S_range": float(srange),
                    "S_range_over_S_star": float(srange / S_star) if S_star > 0 else 0.0,
                    "pass": bool(srange <= t8_full["threshold"] + 1e-15),
                }
            )
        sc["protocol_proposed_T8"]["all_bins"] = all_bins

    _print_scorecard(sc)

    if not args.no_write:
        out = args.output if args.output is not None else default_out_path(inp)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(sc, indent=2) + "\n")
        print(f"wrote {out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
