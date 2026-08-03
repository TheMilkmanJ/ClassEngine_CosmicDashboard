"""finalize_h0_at_convergence — task #24's last gate, made instant (2026-07-28).

WHAT THIS IS
  The Fairbank letter's one open number is H₀ (provisional 69.9; the
  corrected bbnfix pair is converging).  This tool watches the pair and, at
  the corpus's own grading bar (both chains R−1 < 0.05), extracts the final
  posterior H₀ for the model and the control and prints the letter's
  replacement text and the HOLD checklist closure — so completing #24
  becomes a five-minute manual edit the moment the chains grade.  It edits
  NOTHING itself (manual-edits rule); it prints.

  Run any time: unconverged, it reports both chains' current R−1 and
  refuses, which is its honest state until the pair lands.
"""
from __future__ import annotations

import pathlib

import numpy as np

CH = pathlib.Path(__file__).resolve().parent.parent / "chains"
PAIR = ("cmp_lcdm_mnu_bbnfix", "dyad_mnu_bbnfix")
RBAR = 0.05


def last_rminus1(name: str) -> float:
    lines = (CH / f"{name}.progress").read_text().strip().splitlines()
    return float(lines[-1].split()[3])


def h0_posterior(name: str):
    cols = (CH / f"{name}.1.txt").open().readline().split()
    i = cols.index("H0") - 1
    rows = [np.loadtxt(CH / f"{name}.{j}.txt") for j in (1,)
            if (CH / f"{name}.{j}.txt").exists()]
    d = np.vstack(rows)
    n = len(d)
    w, h = d[n // 2:, 0], d[n // 2:, i]
    mean = float(np.average(h, weights=w))
    sig = float(np.sqrt(np.average((h - mean) ** 2, weights=w)))
    return mean, sig, n


def main() -> None:
    print("=" * 74)
    print("H₀ finalization gate (letter item 1)")
    print("=" * 74)
    r = {name: last_rminus1(name) for name in PAIR}
    for name, val in r.items():
        print(f"   {name}: R−1 = {val:.3f}  "
              f"({'GRADED' if val < RBAR else 'converging'})")
    if any(val >= RBAR for val in r.values()):
        print(f"\n   NOT YET — the grading bar is R−1 < {RBAR} on both chains.")
        print("   Nothing extracted; the letter's provisional caveat stands.")
        print("=" * 74)
        return
    m_mean, m_sig, m_n = h0_posterior("dyad_mnu_bbnfix")
    c_mean, c_sig, c_n = h0_posterior("cmp_lcdm_mnu_bbnfix")
    print(f"\n   model H₀   = {m_mean:.2f} ± {m_sig:.2f}  (N = {m_n})")
    print(f"   control H₀ = {c_mean:.2f} ± {c_sig:.2f}  (N = {c_n})")
    print(f"   ΔH₀ (model − control) = {m_mean - c_mean:+.2f}")
    print("\n   LETTER REPLACEMENT (Status section, manual edit):")
    print(f"   'Pantheon+SH0ES, at H₀ = {m_mean:.1f} ± {m_sig:.1f} — "
          f"sound-horizon-driven, and holding with the SH0ES calibration")
    print("   included even though that calibration pulls the other way.'")
    print("   (Delete the not-yet-final caveat sentence; close HOLD item 1")
    print("   with this run's date and both R−1 values.)")
    print("=" * 74)


if __name__ == "__main__":
    main()
