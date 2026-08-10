# Non-MCMC validation suite hygiene — EDITS (2026-08-04)

**Rule:** Fix only real bugs (import errors, broken paths, wrong labels). Do not invent physics.  
**Parent:** [`REPORT.md`](REPORT.md)

---

## Code / script fixes

| locus | change |
|---|---|
| *(none)* | No import errors, broken paths, or wrong labels found in arithmetic/desk scripts. |

---

## LEGACY_ST classy FAIL — diagnosis (not fixed)

| locus | observation | action |
|---|---|---|
| `scripts/test_local_gravity.py --classy` | EXIT 1 — `Class did not read input parameter(s): use_prtoe, xi_prtoe, …` | **No code patch.** CURRENT_CORE classy; `use_prtoe` is compile dummy (`include/background.h`), not live input. |
| `scripts/test_bbn_activation.py --classy` | same unread-parameter set | **No code patch.** |
| `scripts/test_legacy_st_null_limit.py --fast --null-only` | ΛCDM OK; LEGACY_ST null FAIL same root | **No code patch.** |
| `scripts/run_prtoe_validation.py` | would hit same path | **SKIP** (documented) |
| `scripts/run_validation_suite_1_9.sh` | needs `./class` + use_prtoe inis; CLASS-heavy | **SKIP** (documented) |

Re-wiring LEGACY_ST into `input.c` / rebuilding CLASS is **out of scope** for this hygiene pass and would change core-lane surface without an owner ask.

---

## Side effects of runs (script-owned, not invented)

| path | cause |
|---|---|
| `docs/working_logs/_PACKAGE_AUDIT.md` | rewritten by `scripts/arxiv_package_audit.py` (normal script output) |
| `docs/working_logs/_runs/quantum_null_hardening_20260803/AREA_LAW_QUARTER.md` | rewritten by `scripts/quantum_area_law_quarter.py` (normal script output) |

No manual prose edits to those files by this worker.

---

## Package artifacts created

| path | role |
|---|---|
| `docs/working_logs/_runs/validation_suite_20260804/REPORT.md` | grades + non-claims |
| `docs/working_logs/_runs/validation_suite_20260804/EDITS.md` | this file |
| `docs/working_logs/_runs/validation_suite_20260804/logs/*.log` | captured stdout |

---

## Counts

| metric | n |
|---|---:|
| Source files patched | **0** |
| Physics claims added | **0** |
| Status tags promoted | **0** |
