#!/usr/bin/env python3
"""Score four-branch progress from console alone (no summary required).

NO FABRICATIONS. Not a production booking. Prints partial mirror when pairs exist.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


VERDICT_RE = re.compile(
    r"VERDICT\s+(?P<tag>\S+):\s*t=(?P<t>[\d.]+)\s+H=(?P<H>[+\-eE\d.]+)\s+"
    r"spread=(?P<spread>[\d.]+)\s+margin_ok=(?P<mok>\w+)\s+drift_phys=(?P<drift>[\d.]+)%"
)
SELECTED_RE = re.compile(r"from\s+(?P<n>\d+)\s+candidates")
BRANCH_RE = re.compile(r"BRANCH\s+(\S+)")


def parse(text: str) -> dict[str, dict]:
    current = None
    pending_n = None
    out: dict[str, dict] = {}
    for line in text.splitlines():
        m = BRANCH_RE.search(line)
        if m:
            current = m.group(1)
            pending_n = None
            continue
        m = SELECTED_RE.search(line)
        if m:
            pending_n = int(m.group("n"))
            continue
        m = VERDICT_RE.search(line)
        if m:
            tag = m.group("tag")
            out[tag] = {
                "t": float(m.group("t")),
                "H": float(m.group("H")),
                "spread": float(m.group("spread")),
                "margin_ok": m.group("mok") == "True",
                "drift_phys_pct": float(m.group("drift")),
                "n_cand": pending_n,
                "censored": pending_n is not None and pending_n <= 2,
            }
            pending_n = None
    return out


def mirror_pct(a: float | None, b: float | None) -> float | None:
    if a is None or b is None:
        return None
    denom = 0.5 * (abs(a) + abs(b))
    if denom == 0:
        return abs(a + b) * 100.0
    return abs(a + b) / denom * 100.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--log",
        default="docs/working_logs/_runs/t14_hkin_i6_prod_20260803_090317/four_branch_console.log",
    )
    ap.add_argument(
        "--out",
        default="docs/working_logs/_runs/t14_i6_partial_grade_20260803/FOUR_BRANCH_LIVE.md",
    )
    args = ap.parse_args()
    log = Path(args.log)
    if not log.exists():
        print("missing log", log, file=sys.stderr)
        return 2
    rows = parse(log.read_text(errors="ignore"))
    order = ["n+1_f+1", "n+1_f-1", "n-1_f+1", "n-1_f-1"]
    lines = [
        "# Four-branch LIVE (console scrape — not TC)\n\n",
        "**NO FABRICATIONS.** Scrape only; **no production booking.**\n\n",
        "## Progress\n\n",
        "| branch | status | t | H | n_cand | margin_ok | disclosure |\n",
        "|---|---|---:|---:|---:|---|---|\n",
    ]
    for b in order:
        if b not in rows:
            lines.append(f"| {b} | pending/running | — | — | — | — | — |\n")
            continue
        r = rows[b]
        disc = "**instrument-censored**" if r.get("censored") else "ok pool"
        lines.append(
            f"| {b} | VERDICT | {r['t']:.2f} | {r['H']:+.4f} | {r.get('n_cand')} | "
            f"{r['margin_ok']} | {disc} |\n"
        )

    h = {b: rows[b]["H"] if b in rows else None for b in order}
    m11 = mirror_pct(h["n+1_f+1"], h["n-1_f-1"])
    m1m = mirror_pct(h["n+1_f-1"], h["n-1_f+1"])
    lines += [
        "\n## Partial mirror (only when both arms present)\n\n",
        f"- (1,1)↔(−1,−1): {m11 if m11 is not None else 'TBD'}%\n",
        f"- (1,−1)↔(−1,1): {m1m if m1m is not None else 'TBD'}%\n",
        f"- target production: **&lt;5%** both pairs\n",
        "\n## Booking\n\n**None.** Full TC only from `four_branch/summary.json` + conditions 1–6.\n",
    ]
    Path(args.out).write_text("".join(lines))
    print("".join(lines))
    print(f"wrote {args.out} verdicts={list(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
