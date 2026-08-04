# RECHECK 2026-08-03 (continue) — hard_win3 BBN ε recompute
Status: **PASS** — still disk-backed; no script edit; MCMC untouched.
Sources read: `numbers.json`, `REPORT.md` (this run dir only).
Recompute: REPORT recipe `(Aver+2*sig-Yp0)/dY` with 0.2453, 0.0034, 0.246891, 0.00163.
Live result: eps_2sig_pct = **3.1957055214723873** (3.196%).
Disk numbers.json: eps_2sig_pct = 3.1957055214723873; paper_claims_2sig = 3.2.
pass_2sig_matches_paper: **true** (disk) — live match to disk exact.
3.196% ≈ 3.20%: **YES** (abs error 0.0043 pp < 0.01).
Audit slope recompute: (0.248995−0.246891)/1.2543 = 0.0016774296420314079 = disk.
No dedicated scripts/*bbn*/*eps* recompute driver for this card; inline recipe used.
Key inputs (disk): Yp0=0.246891, dYp_deps_paper=0.00163, Aver=0.2453±0.0034.
eps_1sig_pct disk+live: 1.1098159509202314.
EMPRESS_pull_at_eps0 disk: 2.9091176470588267 (not used as upper limit).
Kill criteria not tripped; science claim shelf files not edited.
Verdict: **PASS** — hard-win BBN ε recompute remains disk-backed and paper-matched.

**Promotion (2026-08-03 night; cured 2026-08-04 red):** arithmetic stamped **ARITHMETIC VERIFIED (internal)** on improvement/promotion boards;
**EXTERNAL WIN PENDING (no DOI)** — public record (Zenodo one record) still required. `papers/bbn-eps-bound/README.md` carries reverify line. Not an arXiv post (endorsement/Fairbank still owner).
