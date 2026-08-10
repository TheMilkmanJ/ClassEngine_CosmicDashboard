========================================================================
bbnfix MCMC watch diagnostic — UNBOOKABLE
stamp: 2026-08-04T02:01:02
gate authority: progress R−1 < 0.05 AND checkpoint converged:true
========================================================================

--- dyad_mnu_bbnfix ---
  progress: N=18837 R−1=0.189201 t=2026-08-03T17:57:59.890097 (file mtime 2026-08-03T17:57:59)
  checkpoint: converged=False Rminus1_last=0.18920075919140164 (mtime 2026-08-03T17:57:59)
  chains: ranks=3 rows=[6742, 6683, 6778] latest_mtime=2026-08-04T01:59:43
  crude param R−1 (burn 50%, max over params): 0.0339 — NOT cobaya measure; NOT bookable
/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix.1.txt
/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix.2.txt
/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix.3.txt
Removed 0.3 as burn in
  GetDist max GR (ignore_rows=0.3): 0.085838 — diagnostic only; booking still needs cobaya self-stop
  bookable_leg: False (R−1_ok=False, stop_ok=False)

--- cmp_lcdm_mnu_bbnfix ---
  progress: N=19013 R−1=0.059055 t=2026-08-03T21:05:36.968557 (file mtime 2026-08-03T21:05:37)
  checkpoint: converged=False Rminus1_last=0.05905511181721022 (mtime 2026-08-03T21:05:37)
  chains: ranks=3 rows=[6699, 6701, 6563] latest_mtime=2026-08-04T02:01:14
  crude param R−1 (burn 50%, max over params): 0.0191 — NOT cobaya measure; NOT bookable
/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix.1.txt
/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix.2.txt
/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix.3.txt
Removed 0.3 as burn in
  GetDist max GR (ignore_rows=0.3): 0.068758 — diagnostic only; booking still needs cobaya self-stop
  bookable_leg: False (R−1_ok=False, stop_ok=False)

========================================================================
REFUSE booking from this script. Use: python3 scripts/book_bbnfix_when_ready.py
========================================================================
