#!/usr/bin/env python3
"""Inventory: can medium (ω,λ) or r be pinned from corpus? (R-MEDR + R-PAIRH P1)

Desk hunt only — does not invent. Single-thread, seconds.
Writes MISSING_INPUT or CANDIDATE_PIN list.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(".")
OUT = Path("docs/working_logs/_runs/quantum_residual_task_20260803/MEDR_PAIRH_INVENTORY.md")
OUT_JSON = Path("docs/working_logs/_runs/quantum_residual_task_20260803/medr_pairh_inventory.json")

# patterns that would license a pair pin
PATTERNS = [
    (r"pair\s+Hamiltonian", "pair_Hamiltonian_phrase"),
    (r"H\s*=\s*.*a\^?\\?dagger", "latex_pair_H"),
    (r"two-?mode\s+squeez", "tmsv_phrase"),
    (r"squeez(?:e|ing)\s+parameter", "squeeze_param"),
    (r"\\lambda\s*/\s*\\omega|lambda\s*/\s*omega", "lambda_over_omega"),
    (r"Bogoliubov\s+coherence", "bogoliubov_coherence"),
    (r"pairing\s+gap|gap\s+equation", "pairing_gap"),
    (r"Cooper\s+pair", "cooper"),
]

SEARCH_GLOBS = [
    "docs/PRTOE_*.md",
    "docs/exploratory/PRTOE_*.md",
    "scripts/*.py",
]


def main() -> int:
    hits: dict[str, list[dict]] = {name: [] for _, name in PATTERNS}
    files_scanned = 0
    for glob in SEARCH_GLOBS:
        for path in ROOT.glob(glob):
            if not path.is_file():
                continue
            # skip huge
            try:
                if path.stat().st_size > 2_000_000:
                    continue
                text = path.read_text(errors="replace")
            except Exception:
                continue
            files_scanned += 1
            for pat, name in PATTERNS:
                for m in re.finditer(pat, text, re.I):
                    # line number
                    line = text.count("\n", 0, m.start()) + 1
                    snippet = text[max(0, m.start() - 40) : m.end() + 60].replace("\n", " ")
                    hits[name].append(
                        {"file": str(path), "line": line, "snippet": snippet[:160]}
                    )

    # Cap hits per pattern
    for k in hits:
        hits[k] = hits[k][:12]

    # Decision logic: we need an explicit medium map to r or (ω,λ)
    has_pair_h_definition = len(hits["pair_Hamiltonian_phrase"]) + len(hits["latex_pair_H"]) > 0
    has_r_formula = any("r =" in h["snippet"] or "r=" in h["snippet"] for h in hits["squeeze_param"])
    has_lambda_omega = len(hits["lambda_over_omega"]) > 0

    # Known: textbook harness exists; medium pin does not from prior EN-D2
    medium_pin_found = False  # set true only if we find explicit formula with medium numbers
    # Heuristic: look for r = f(T_c or gap) style in snippets
    for h in hits["squeeze_param"] + hits["pairing_gap"]:
        if re.search(r"r\s*=\s*[^.\n]{0,40}(T_c|gap|m_e|alpha|ξ|xi)", h["snippet"], re.I):
            medium_pin_found = True

    verdict = {
        "files_scanned": files_scanned,
        "medium_r_derived": False,
        "medium_pair_H_licensed": False,
        "textbook_harness_exists": True,
        "path_harness": "scripts/quantum_pair_hamiltonian_tmsv.py",
        "medium_pin_found": medium_pin_found,
        "has_pair_h_phrase": has_pair_h_definition,
        "has_lambda_omega_phrase": has_lambda_omega,
        "hit_counts": {k: len(v) for k, v in hits.items()},
        "hits": hits,
        "EN_D2_D3": "MISSING_INPUT" if not medium_pin_found else "CANDIDATE — inspect hits",
        "next": "If medium_pin_found, hand-derive formula into script; else stay blocked",
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(verdict, indent=2))

    md = f"""# Medium r / pair H inventory (R-MEDR + R-PAIRH P1)

**Script:** `scripts/quantum_medium_r_inventory.py`  
**files_scanned:** {files_scanned}

## Verdict

| question | answer |
|---|---|
| Textbook pair H harness | **YES** (`quantum_pair_hamiltonian_tmsv.py`) |
| Medium-licensed pair H on disk | **{"CANDIDATE — inspect" if medium_pin_found else "NO"}** |
| Medium r formula on disk | **{"CANDIDATE — inspect" if medium_pin_found else "NO"}** |
| EN-D2/D3 | **{verdict["EN_D2_D3"]}** |

## Hit counts

| pattern | n |
|---|---:|
"""
    for k, n in verdict["hit_counts"].items():
        md += f"| {k} | {n} |\n"
    md += """
## Interpretation

Phrase hits for Cooper/Bogoliubov/gap are **expected** in a superfluid corpus; they do **not**
by themselves pin \\(r\\) or \\((\\omega,\\lambda)\\). Only an explicit map to numbers pays R-MEDR.

## Recompute

```bash
OMP_NUM_THREADS=1 python3 scripts/quantum_medium_r_inventory.py
```
"""
    OUT.write_text(md)
    print("MEDR/PAIRH inventory")
    print(f"  scanned={files_scanned} medium_pin_found={medium_pin_found}")
    print(f"  EN-D2/D3 → {verdict['EN_D2_D3']}")
    print(f"  wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
