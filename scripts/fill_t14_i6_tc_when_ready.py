#!/usr/bin/env python3
"""Fill t14_i6 TC skeleton from four_branch/summary.json when present.

NO FABRICATIONS. Exit 2 if artifacts missing. Does not book production sign.

Schema (ring_toroidal_hkin.py):
  summary = {booking, smoke, elapsed_s, results: {
    branch: {tag, n_wind, fountain_sign, verdict: {t,H,Tw,Wr,ampA,...}|null,
             dial_spread, dial_Hs, margin_ok, psi_path}
  }}
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path
from typing import Any

BASE = Path("docs/working_logs/_runs/t14_hkin_i6_prod_20260803_090317")
FB = BASE / "four_branch" / "summary.json"
CONSOLE = BASE / "four_branch_console.log"
SKELETON = Path("docs/working_logs/_runs/t14_i6_TC_SKELETON.md")
OUT = Path("docs/working_logs/_runs/t14_i6_TC_FROM_DISK.md")
GATE_OUT = Path("docs/working_logs/_runs/t14_i6_TC_GATES.md")
CHECKLIST = Path("docs/working_logs/_runs/t14_i6_CONDITIONS_1_6_CHECKLIST.md")

BRANCH_ORDER = ["n+1_f+1", "n+1_f-1", "n-1_f+1", "n-1_f-1"]


def _fmt(x: Any, nd: int = 4) -> str:
    if x is None:
        return "—"
    if isinstance(x, float):
        if math.isnan(x):
            return "NaN"
        return f"{x:.{nd}g}"
    return str(x)


def mirror_residual(h_a: Any, h_b: Any) -> float | None:
    """Relative residual |H_a + H_b| / mean(|H|) for opposite-sign pair."""
    try:
        a = float(h_a)
        b = float(h_b)
    except (TypeError, ValueError):
        return None
    if math.isnan(a) or math.isnan(b):
        return None
    denom = 0.5 * (abs(a) + abs(b))
    if denom == 0:
        return abs(a + b)
    return abs(a + b) / denom


def parse_console_n_cand(text: str) -> dict[str, int]:
    """Map branch -> n candidates from SELECTED lines."""
    out: dict[str, int] = {}
    # VERDICT n+1_f+1: ... appears after SELECTED ... from N candidates
    # Walk by branch blocks
    current = None
    for line in text.splitlines():
        m = re.search(r"BRANCH\s+(\S+)", line)
        if m:
            current = m.group(1)
            continue
        m = re.search(r"from\s+(\d+)\s+candidates", line)
        if m and current:
            out[current] = int(m.group(1))
        m = re.search(r"VERDICT\s+(\S+):", line)
        if m:
            current = m.group(1)
    return out


def flatten_branch(name: str, row: dict[str, Any] | None, n_cand: int | None) -> dict[str, Any]:
    if not row:
        return {
            "branch": name,
            "t": None,
            "H": None,
            "Tw": None,
            "Wr": None,
            "ampA": None,
            "n_cand": n_cand,
            "margin_ok": None,
            "verdict_null": True,
            "censored": n_cand is not None and n_cand <= 2,
        }
    v = row.get("verdict")
    if v is None:
        return {
            "branch": name,
            "t": None,
            "H": None,
            "Tw": None,
            "Wr": None,
            "ampA": None,
            "n_cand": n_cand,
            "margin_ok": row.get("margin_ok"),
            "verdict_null": True,
            "censored": n_cand is not None and n_cand <= 2,
            "dial_spread": row.get("dial_spread"),
        }
    return {
        "branch": name,
        "t": v.get("t"),
        "H": v.get("H"),
        "Tw": v.get("Tw"),
        "Wr": v.get("Wr"),
        "ampA": v.get("ampA"),
        "helA": v.get("helA"),
        "nphase": v.get("nphase"),
        "n_cand": n_cand,
        "margin_ok": row.get("margin_ok"),
        "verdict_null": False,
        "censored": n_cand is not None and n_cand <= 2,
        "dial_spread": row.get("dial_spread"),
        "drift_phys": v.get("drift_phys"),
    }


def main() -> int:
    if not FB.exists():
        print("WAIT: no four_branch/summary.json yet", file=sys.stderr)
        return 2

    d = json.loads(FB.read_text())
    results = d.get("results") or {}
    n_cand_map: dict[str, int] = {}
    if CONSOLE.exists():
        n_cand_map = parse_console_n_cand(CONSOLE.read_text(errors="ignore"))

    rows = [
        flatten_branch(b, results.get(b) if isinstance(results.get(b), dict) else None, n_cand_map.get(b))
        for b in BRANCH_ORDER
    ]
    by = {r["branch"]: r for r in rows}

    OUT.write_text(
        "# R1-t14-i6 production numbers FROM DISK\n\n"
        f"**Source:** `{FB}`\n\n"
        f"**elapsed_s:** {d.get('elapsed_s')}\n"
        f"**booking string:** {d.get('booking')}\n"
        f"**console n_cand map:** {n_cand_map}\n\n"
        "## Flattened branches\n\n```json\n"
        + json.dumps(rows, indent=2, default=str)
        + "\n```\n\n## Full summary.json\n\n```json\n"
        + json.dumps(d, indent=2, default=str)[:20000]
        + "\n```\n"
    )
    print("wrote", OUT)

    table_lines = [
        "| branch | t | H | Tw | Wr | ampA | n_cand | margin_ok |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in rows:
        nc = r.get("n_cand")
        nc_s = "—" if nc is None else (f"**{nc} censored**" if r.get("censored") else str(nc))
        table_lines.append(
            f"| {r['branch']} | {_fmt(r.get('t'))} | {_fmt(r.get('H'))} | {_fmt(r.get('Tw'))} | "
            f"{_fmt(r.get('Wr'))} | {_fmt(r.get('ampA'))} | {nc_s} | {_fmt(r.get('margin_ok'))} |"
        )

    m11 = mirror_residual(by["n+1_f+1"].get("H"), by["n-1_f-1"].get("H"))
    m1m = mirror_residual(by["n+1_f-1"].get("H"), by["n-1_f+1"].get("H"))
    m11_pct = None if m11 is None else 100.0 * m11
    m1m_pct = None if m1m is None else 100.0 * m1m
    mirror_ok = (
        m11_pct is not None
        and m1m_pct is not None
        and m11_pct < 5.0
        and m1m_pct < 5.0
    )

    # mismatched-t flags for mirror pairs
    t_pairs = [
        ("(1,1)↔(−1,−1)", by["n+1_f+1"].get("t"), by["n-1_f-1"].get("t")),
        ("(1,−1)↔(−1,1)", by["n+1_f-1"].get("t"), by["n-1_f+1"].get("t")),
    ]
    t_flags = []
    for label, ta, tb in t_pairs:
        if ta is None or tb is None:
            t_flags.append(f"{label}: incomplete")
        elif ta != tb:
            t_flags.append(f"{label}: **mismatched-t** ({ta} vs {tb})")
        else:
            t_flags.append(f"{label}: matched t={ta}")

    any_censored = any(r.get("censored") for r in rows)
    all_margin = all(r.get("margin_ok") is True for r in rows if not r.get("verdict_null"))
    all_have_verdict = all(not r.get("verdict_null") for r in rows)

    eligible = (
        mirror_ok
        and all_have_verdict
        and all_margin
        and not any_censored  # cond 2: censored rows block clean production book
    )

    gate_md = [
        "# R1-t14-i6 gates FROM DISK (auto)\n",
        f"\n**Source:** `{FB}`\n",
        f"**elapsed_s:** {_fmt(d.get('elapsed_s'), 1)}\n",
        f"**booking string (instrument):** {d.get('booking')}\n",
        "\n**NO FABRICATIONS.** Production sign booking only if gates PASS + conditions 1–6 + red/ref.\n",
        "\n## four-branch selected\n\n",
        "\n".join(table_lines),
        "\n\n## Mirror residuals\n\n",
        f"- (n+1_f+1) ↔ (n-1_f-1): {_fmt(m11_pct, 4)}% (target <5%)\n",
        f"- (n+1_f-1) ↔ (n-1_f+1): {_fmt(m1m_pct, 4)}% (target <5%)\n",
        f"- **mirror_ok:** {mirror_ok}\n",
        "\n## Condition 3 — member t\n\n",
        *[f"- {x}\n" for x in t_flags],
        "\n## Condition 2 — candidate pools\n\n",
        f"- console n_cand: {n_cand_map}\n",
        f"- any instrument-censored (≤2): **{any_censored}**\n",
        "\n## Gate scorecard\n\n",
        "| Gate | Target | Result |\n|---|---|---|\n",
        "| Calibrate planar+helix | PASS | PASS (prior) |\n",
        "| nowinding | H≪0.2 + disclosure | PASS (prior) |\n",
        "| nojet no false ring | no ring | PASS (prior; red M1) |\n",
        f"| True-mirror residual <5% | <5% | {_fmt(m11_pct,3)}% / {_fmt(m1m_pct,3)}% → "
        f"{'PASS' if mirror_ok else 'FAIL/TBD'} |\n",
        f"| Margins all four | margin_ok | {all_margin and all_have_verdict} |\n",
        f"| No censored production rows | n_cand>2 | {not any_censored} |\n",
        "| Blind selector | no Tw/Wr/H | held if instrument unchanged |\n",
        "\n## Booking stance (auto)\n\n",
        "- Smoke-grade H≈sign(n)·2 remains separate.\n",
        f"- Production sign(H vs n) **auto-eligible:** **{eligible}**\n",
        "  (mirror_ok AND all verdicts AND all margin_ok AND no ≤2-cand rows).\n",
        "- Even if eligible: **do not self-book** — tribunal + conditions 1–6 + red/ref required.\n",
        f"- Checklist: `{CHECKLIST}`\n",
    ]
    GATE_OUT.write_text("".join(gate_md))
    print("wrote", GATE_OUT)

    if SKELETON.exists():
        sk = SKELETON.read_text()
        start = sk.find("## four-branch (fill when ready)")
        if start >= 0:
            new_fb = (
                "## four-branch (fill when ready)\n\n"
                + "\n".join(table_lines)
                + f"\n\nMirror residual (1,1)↔(−1,−1): {_fmt(m11_pct, 4)}%\n"
                + f"Mirror residual (1,−1)↔(−1,1): {_fmt(m1m_pct, 4)}%\n"
                + f"mirror_ok: {mirror_ok}\n"
                + f"any_instrument_censored: {any_censored}\n"
                + f"production_auto_eligible: {eligible}\n"
                + f"\n*Auto-filled from `{FB}` + console n_cand. Verify before booking.*\n"
            )
            SKELETON.write_text(sk[:start] + new_fb)
            print("updated", SKELETON)

    print(
        f"DONE fill mirror_ok={mirror_ok} censored={any_censored} eligible={eligible} (no booking filed)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
