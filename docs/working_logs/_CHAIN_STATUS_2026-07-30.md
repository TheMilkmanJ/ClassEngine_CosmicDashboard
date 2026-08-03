# Live chain status — 2026-07-30 ~23:57 MDT

*Subagent snapshot. Production classy: `/home/themilkmanj/prtoe_class/python/classy.cpython-312-x86_64-linux-gnu.so` (mtime 2026-07-23). Worktree Jul 30 rebuild is **not** loaded by live MPI.*

| Chain | Verdict | MH accept | R−1 (latest) | Action |
|---|---|---|---|---|
| **dyad_mnu_bbnfix** | healthy | ~6.2% | **0.185** @ N≈7211 | Keep running |
| **cmp_lcdm_mnu_bbnfix** | healthy | ~8.0% | **0.711** @ N≈4492 | Keep running |
| **cmp_prtoe_routeD** | watch | ~5% / ~3.7% | none yet | Keep; rank1 lag (~469 vs 868) until first Learn @560 |

**Do not** restart or hot-swap classy under these processes. RouteD can finish on the old conversion (background-only) physics; new linear conversion hierarchy is for a future relaunch after deploy.
