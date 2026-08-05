#!/usr/bin/env python3
"""book_bbnfix_when_ready — single entrypoint for BBN-fixed pair GetDist booking.

Hard gate (corpus / checklist / hard-win1 / Claude R-D cure):
  Both chains must have:
    (1) last-row R−1 < 0.05 from chains/<root>.progress field 4 (Rminus1)
    (2) sampler self-stop: `converged: true` in chains/<root>.checkpoint
  If either leg fails on either chain → refuse, exit 2.
  Do not book on single-chain sub-bar R−1 or without self-stop.

When both ready:
  loadMCSamples(..., ignore_rows=0.3) for all ranks; book marginals for
  H0, m_ncdm, omega_b, S8 (if present); write REPORT.md + booking.json
  under docs/working_logs/_runs/bbnfix_booking_<stamp>/.

No new MCMC. Does not edit living docs (manual follow-up per checklist).

Usage (repo root):
  python3 scripts/book_bbnfix_when_ready.py
  python3 scripts/book_bbnfix_when_ready.py --outdir docs/working_logs/_runs/bbnfix_booking_TEST
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CH = REPO / "chains"
PAIR = ("dyad_mnu_bbnfix", "cmp_lcdm_mnu_bbnfix")
RBAR = 0.05
IGNORE_ROWS = 0.3
PARAMS = ("H0", "m_ncdm", "omega_b", "S8")


def checkpoint_meta(name: str) -> dict:
    """Parse cobaya checkpoint for self-stop + last R−1 (informational).

    Gate authority remains progress R−1 + converged:true. Checkpoint
    Rminus1_last is reported for watch honesty when progress files lag.
    """
    p = CH / f"{name}.checkpoint"
    out: dict = {
        "path": str(p),
        "present": p.is_file(),
        "converged": None,
        "Rminus1_last": None,
    }
    if not p.is_file():
        return out
    text = p.read_text()
    if "converged: true" in text:
        out["converged"] = True
    elif "converged: false" in text:
        out["converged"] = False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("Rminus1_last:"):
            try:
                out["Rminus1_last"] = float(s.split(":", 1)[1].strip())
            except ValueError:
                pass
    return out


def checkpoint_converged(name: str) -> bool | None:
    """True/False if checkpoint present; None if missing or unreadable."""
    return checkpoint_meta(name).get("converged")


def last_progress(name: str) -> dict:
    """Parse last row of chains/<name>.progress.

    Columns (cobaya): N  timestamp  acceptance_rate  Rminus1  Rminus1_cl
    Gate uses field 4 = Rminus1 (0-indexed field 3).
    """
    path = CH / f"{name}.progress"
    if not path.is_file():
        return {
            "root": name,
            "path": str(path),
            "present": False,
            "error": f"missing progress file: {path}",
        }
    lines = path.read_text().strip().splitlines()
    if not lines:
        return {
            "root": name,
            "path": str(path),
            "present": False,
            "error": f"empty progress file: {path}",
        }
    parts = lines[-1].split()
    if len(parts) < 4:
        return {
            "root": name,
            "path": str(path),
            "present": False,
            "error": f"malformed last progress row ({len(parts)} fields): {lines[-1]!r}",
        }
    try:
        n = float(parts[0])
        rminus1 = float(parts[3])
    except ValueError as e:
        return {
            "root": name,
            "path": str(path),
            "present": False,
            "error": f"cannot parse N/R−1 from last row: {e}; row={lines[-1]!r}",
        }
    if rminus1 != rminus1:  # NaN
        return {
            "root": name,
            "path": str(path),
            "present": False,
            "error": f"R−1 is NaN on last row: {lines[-1]!r}",
            "N": n,
            "timestamp": parts[1] if len(parts) > 1 else None,
            "Rminus1": None,
        }
    return {
        "root": name,
        "path": str(path),
        "present": True,
        "N": n,
        "timestamp": parts[1] if len(parts) > 1 else None,
        "acceptance_rate": float(parts[2]) if len(parts) > 2 else None,
        "Rminus1": rminus1,
        "Rminus1_cl": parts[4] if len(parts) > 4 else None,
        "ready": rminus1 < RBAR,
        "last_row": lines[-1],
    }


def ranks_present(name: str) -> list[str]:
    return [str(CH / f"{name}.{i}.txt") for i in (1, 2, 3)
            if (CH / f"{name}.{i}.txt").is_file()]


def gate_status(progress: dict[str, dict]) -> tuple[bool, list[str]]:
    """Return (both_ready, list of refuse reasons).

    Both legs required per chain (Claude R-D): R−1 < RBAR AND converged:true.
    """
    reasons: list[str] = []
    for name in PAIR:
        p = progress[name]
        if not p.get("present"):
            reasons.append(f"{name}: MISSING/unreadable progress — {p.get('error', 'unknown')}")
            continue
        r = p["Rminus1"]
        if r >= RBAR:
            reasons.append(
                f"{name}: R−1 = {r:.6f} >= {RBAR} (N={p.get('N')}, t={p.get('timestamp')}) — NOT READY"
            )
        else:
            reasons.append(
                f"{name}: R−1 = {r:.6f} < {RBAR} (N={p.get('N')}) — R−1 GRADED"
            )
        cmeta = checkpoint_meta(name)
        conv = cmeta.get("converged")
        p["converged"] = conv
        p["checkpoint_Rminus1_last"] = cmeta.get("Rminus1_last")
        if conv is True:
            reasons.append(f"{name}: checkpoint converged: true — self-stop OK")
        elif conv is False:
            reasons.append(
                f"{name}: checkpoint converged: false — NOT READY (self-stop required)"
            )
        else:
            reasons.append(
                f"{name}: checkpoint missing/unreadable — NOT READY (self-stop required)"
            )
        if cmeta.get("Rminus1_last") is not None:
            reasons.append(
                f"{name}: checkpoint Rminus1_last={cmeta['Rminus1_last']:.6f} "
                f"(informational; gate uses progress R−1)"
            )
    both = all(
        progress[n].get("present")
        and progress[n].get("Rminus1", 1.0) < RBAR
        and progress[n].get("converged") is True
        for n in PAIR
    )
    return both, reasons


def getdist_marginals(root: str) -> dict:
    """Three-rank GetDist load; marginal mean ± std for PARAMS if present."""
    # Import only when booking — refuse path must not require getdist if unused,
    # but dry-run refuse should still work without importing heavy stacks.
    from getdist import loadMCSamples

    prefix = str(CH / root)
    samples = loadMCSamples(prefix, settings={"ignore_rows": IGNORE_ROWS})
    names = samples.getParamNames().list()
    out: dict = {
        "root": root,
        "prefix": prefix,
        "ignore_rows": IGNORE_ROWS,
        "param_names_available": names,
        "n_samples_after_burn": int(samples.numrows) if hasattr(samples, "numrows") else None,
        "marginals": {},
    }
    try:
        out["n_samples_after_burn"] = int(len(samples.samples))
    except Exception:
        pass

    for p in PARAMS:
        if p not in names:
            out["marginals"][p] = {"present": False}
            continue
        mean = float(samples.mean(p))
        std = float(samples.std(p))
        entry = {
            "present": True,
            "mean": mean,
            "std": std,
            "mean_pm_std": f"{mean:.6g} ± {std:.6g}",
        }
        # Prefer 68% limits from getMargeStats when available
        try:
            marge = samples.getMargeStats()
            d = marge.parWithName(p)
            if d is not None and d.limits:
                lim = d.limits[0]
                entry["limit68_lower"] = float(lim.lower)
                entry["limit68_upper"] = float(lim.upper)
                entry["mean_pm_68"] = (
                    f"{d.mean:.6g}  [{lim.lower:.6g}, {lim.upper:.6g}]"
                )
                entry["mean"] = float(d.mean)
        except Exception as e:
            entry["marge_note"] = f"68% limits unavailable: {e}"
        out["marginals"][p] = entry
    return out


def write_report(
    outdir: Path,
    *,
    both_ready: bool,
    progress: dict,
    reasons: list[str],
    booking: dict | None,
    stamp: str,
    exit_code: int,
) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    payload = {
        "stamp": stamp,
        "gate": {
            "Rbar": RBAR,
            "rule": (
                "refuse unless BOTH chains have R−1 < Rbar AND "
                "checkpoint converged: true (self-stop); both legs required"
            ),
            "pair": list(PAIR),
            "both_ready": both_ready,
            "exit_code": exit_code,
        },
        "progress": progress,
        "reasons": reasons,
        "ranks": {n: ranks_present(n) for n in PAIR},
        "booking": booking,
        "ignore_rows": IGNORE_ROWS,
        "params_requested": list(PARAMS),
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "script": "scripts/book_bbnfix_when_ready.py",
    }
    (outdir / "booking.json").write_text(json.dumps(payload, indent=2) + "\n")

    lines = [
        f"# bbnfix GetDist booking — {stamp}",
        "",
        f"**Generated (UTC):** {payload['generated_utc']}",
        f"**Script:** `scripts/book_bbnfix_when_ready.py`",
        f"**Gate:** both of {{{', '.join(PAIR)}}} with R−1 **< {RBAR}** "
        f"**AND** `converged: true` (self-stop) — both legs required",
        f"**Result:** {'BOOKED' if both_ready and booking else 'REFUSED'}",
        f"**Exit code:** {exit_code}",
        "",
        "## Progress + self-stop gate",
        "",
        "| chain | present | N | timestamp | R−1 | converged | ready |",
        "|---|---|---:|---|---:|---|---|",
    ]
    for name in PAIR:
        p = progress[name]
        if not p.get("present"):
            lines.append(
                f"| `{name}` | NO | — | — | — | — | NO — {p.get('error', '')} |"
            )
        else:
            conv = p.get("converged")
            conv_s = "true" if conv is True else ("false" if conv is False else "missing")
            r_ok = p.get("Rminus1", 1.0) < RBAR
            ready = "YES" if (r_ok and conv is True) else "NO"
            lines.append(
                f"| `{name}` | YES | {p.get('N')} | {p.get('timestamp')} | "
                f"{p['Rminus1']:.6f} | {conv_s} | {ready} |"
            )
    lines.extend(["", "### Gate messages", ""])
    for r in reasons:
        lines.append(f"- {r}")

    lines.extend(["", "## Rank files", ""])
    for name in PAIR:
        ranks = ranks_present(name)
        lines.append(f"- `{name}`: {len(ranks)} files")
        for rp in ranks:
            lines.append(f"  - `{rp}`")

    if not both_ready:
        lines.extend(
            [
                "",
                "## Booking status",
                "",
                f"**REFUSED.** Do not quote H₀ / Σm_ν / Ω_b h² / S8 as bookable "
                f"posteriors while either chain has R−1 ≥ {RBAR}, missing progress, "
                f"or has not self-stopped (`converged: true`).",
                "",
                "Also blocked while gate closed: living `PRTOE_CHAIN_TABLES.md` writes,",
                "bookable Laplace ΔlnZ under the BBN-fixed stack, and promotion of",
                "pre-bbnfix ΔlnZ ≈ +2.6 as if it were this pair's result.",
                "",
                "Publish split (when gate later opens): **Stage A** = book + finalize only;",
                "**Stage B** = tables only after `RED_AUDIT.md` (`red: AGREE` / `AGREE-IF`).",
                "",
                "Re-run when both progress tails show R−1 < 0.05 **and** both "
                "checkpoints have `converged: true`:",
                "",
                "```bash",
                "python3 scripts/book_bbnfix_when_ready.py",
                "# preferred one-shot Stage A: bash scripts/bbnfix_when_ready_all.sh",
                "```",
                "",
                "See also: `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`,",
                "`scripts/finalize_h0_at_convergence.py`,",
                "`docs/working_logs/_runs/laplace_booking_full_20260804/`,",
                "`docs/working_logs/_runs/laplace_prep_harden_20260804/`.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "",
                f"## GetDist marginals (`ignore_rows={IGNORE_ROWS}`)",
                "",
                "Three-rank load via `getdist.loadMCSamples`. Means ± std; "
                "68% limits when GetDist MargeStats available.",
                "",
            ]
        )
        assert booking is not None
        for root, block in booking.items():
            lines.append(f"### `{root}`")
            lines.append("")
            n = block.get("n_samples_after_burn")
            lines.append(f"Post-burn samples: {n}")
            lines.append("")
            lines.append("| parameter | present | mean ± std | 68% limits |")
            lines.append("|---|---|---|---|")
            for p in PARAMS:
                m = block["marginals"].get(p, {"present": False})
                if not m.get("present"):
                    lines.append(f"| {p} | NO | — | — |")
                else:
                    lim = "—"
                    if "limit68_lower" in m:
                        lim = f"[{m['limit68_lower']:.6g}, {m['limit68_upper']:.6g}]"
                    lines.append(
                        f"| {p} | YES | {m['mean']:.6g} ± {m['std']:.6g} | {lim} |"
                    )
            lines.append("")
        lines.extend(
            [
                "## External claim (booked numbers only)",
                "",
                "Matched-likelihood dyad vs ΛCDM+m_ν posteriors under the BBN-fixed "
                "production stack (DESI+Planck+ACT+SPT+SN+BBN prior as in the yamls).",
                "",
                "**Kill:** quote while R−1 ≥ 0.05; omit burn-in statement; rank-1-only "
                "half-chain σ instead of three-rank GetDist.",
                "",
                "## Manual follow-up (not done by this script)",
                "",
                "- Paste H₀ letter sentence from `finalize_h0_at_convergence.py` if desired",
                "- Update `docs/PRTOE_CHAIN_TABLES.md`, `_chain_snapshot.md`, referee calendar",
                "- Optional Laplace ΔlnZ per checklist Step C — separate, not this entrypoint",
                "",
            ]
        )

    (outdir / "REPORT.md").write_text("\n".join(lines) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Book bbnfix GetDist marginals only when both R−1 < 0.05 "
            "AND both checkpoints show converged: true (self-stop)."
        )
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=None,
        help="Output directory (default: docs/working_logs/_runs/bbnfix_booking_<stamp>)",
    )
    parser.add_argument(
        "--stamp",
        default=None,
        help="Timestamp label for default outdir (default: UTC now YYYYmmdd_HHMMSS)",
    )
    args = parser.parse_args(argv)

    stamp = args.stamp or datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    outdir = args.outdir
    if outdir is None:
        outdir = REPO / "docs" / "working_logs" / "_runs" / f"bbnfix_booking_{stamp}"
    else:
        outdir = Path(outdir)
        if not outdir.is_absolute():
            outdir = REPO / outdir

    print("=" * 74)
    print("bbnfix GetDist booking gate")
    print(f"  pair: {PAIR}")
    print(f"  bar:  R−1 < {RBAR} on BOTH + self-stop (converged: true) on BOTH")
    print("  refuse if either R−1 >= bar, missing progress, or not self-stopped")
    print(f"  out:  {outdir}")
    print("=" * 74)

    progress = {name: last_progress(name) for name in PAIR}
    both_ready, reasons = gate_status(progress)

    for r in reasons:
        print(f"  {r}")

    if not both_ready:
        print()
        print("  REFUSED — booking blocked (gate closed).")
        print(f"  Gate requires BOTH chains with R−1 < {RBAR} AND converged: true.")
        print("  No GetDist booking; no H₀ / Σm_ν / S8 quote; living docs unchanged.")
        print("  No PRTOE_CHAIN_TABLES.md write; no bookable Laplace ΔlnZ under this stack.")
        print("  Do NOT promote pre-bbnfix ΔlnZ ≈ +2.6 as the bbnfix-pair result.")
        print("  Re-run: python3 scripts/book_bbnfix_when_ready.py")
        print("=" * 74)
        write_report(
            outdir,
            both_ready=False,
            progress=progress,
            reasons=reasons,
            booking=None,
            stamp=stamp,
            exit_code=2,
        )
        print(f"  wrote refuse card: {outdir / 'REPORT.md'}")
        print(f"  wrote: {outdir / 'booking.json'}")
        return 2

    print()
    print(f"  Both graded. Running GetDist (ignore_rows={IGNORE_ROWS}) …")
    booking: dict = {}
    try:
        for name in PAIR:
            print(f"  loading {name} …")
            booking[name] = getdist_marginals(name)
            for p in PARAMS:
                m = booking[name]["marginals"][p]
                if m.get("present"):
                    extra = ""
                    if "limit68_lower" in m:
                        extra = f"  68% [{m['limit68_lower']:.4g}, {m['limit68_upper']:.4g}]"
                    print(f"    {p}: {m['mean']:.6g} ± {m['std']:.6g}{extra}")
                else:
                    print(f"    {p}: (not in chain)")
    except Exception as e:
        print(f"  GetDist FAILED: {e}", file=sys.stderr)
        write_report(
            outdir,
            both_ready=True,
            progress=progress,
            reasons=reasons + [f"GetDist error: {e}"],
            booking=None,
            stamp=stamp,
            exit_code=1,
        )
        print(f"  partial card: {outdir / 'REPORT.md'}")
        return 1

    write_report(
        outdir,
        both_ready=True,
        progress=progress,
        reasons=reasons,
        booking=booking,
        stamp=stamp,
        exit_code=0,
    )
    print()
    print(f"  BOOKED → {outdir / 'REPORT.md'}")
    print(f"  BOOKED → {outdir / 'booking.json'}")
    print("=" * 74)
    return 0


if __name__ == "__main__":
    sys.exit(main())
