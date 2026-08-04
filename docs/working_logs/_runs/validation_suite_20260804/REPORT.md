# Non-MCMC validation suite hygiene — REPORT (2026-08-04)

**Worker:** Grok Build  
**Package:** `docs/working_logs/_runs/validation_suite_20260804/`  
**Rule:** NO FABRICATIONS · exit 0 ≠ automatic PASS for physics claims · no PolyChord · leave live MCMCs alone  
**Live MCMCs left alone:** `dyad_mnu_bbnfix`, `cmp_lcdm_mnu_bbnfix`, `cmp_prtoe_routeD` (confirmed running; not touched)

Artifacts:

| file | role |
|---|---|
| this `REPORT.md` | run table + grades + non-claims |
| [`EDITS.md`](EDITS.md) | fixes applied (none this pass) |
| [`logs/`](logs/) | captured stdout/stderr per run |

**Env:** `OMP_NUM_THREADS=1`, `nice -n 15`, `python3` = system 3.12.3; classy from `python/classy.cpython-312-*.so`.

---

## 1. Grade rule (this package)

| class | meaning |
|---|---|
| **PASS verdict** | Explicit match/arithmetic token on a formulable card (BBN ε 2σ ceiling; area-law 1/4; τ = ½ ln 2 at Q=2/3) |
| **desk audit** | Script ran clean (exit 0); controls/hygiene hold — **not** a physics COMPLETE / parent win |
| **FAIL** | Nonzero exit or explicit claim mismatch |
| **SKIP** | Not run; reason documented (CLASS/MCMC/PolyChord fence or LEGACY_ST offline) |

Canonical formulable split (from prior pass-label hygiene): BBN ε + area-law + τ Parseval = **PASS verdict**; supertrace k1 = **desk audit** even when all controls `ok` and RESULT CONFIRMED.

**BBN ε fence:** ARITHMETIC VERIFIED (internal). EXTERNAL WIN PENDING (no DOI). Not booked as external win.

---

## 2. Run table

| # | command | log | EXIT | grade | notes |
|---:|---|---|---:|---|---|
| 1 | `python3 papers/bbn-eps-bound/recompute_eps_bound.py` | [`logs/recompute_eps_bound.log`](logs/recompute_eps_bound.log) | **0** | **PASS verdict** | ε 2σ ceiling = **3.196%**; paper 3.20%; `match = PASS` (\|Δ\| < 0.05). Arithmetic only. |
| 2 | `python3 scripts/supertrace_k1_verify.py` | [`logs/supertrace_k1_verify.log`](logs/supertrace_k1_verify.log) | **0** | **desk audit** | All S-A…S-I controls `ok`; RESULT CONFIRMED + unit correction note. No literal `PASS` token; not a parent COMPLETE. |
| 3 | `python3 scripts/quantum_area_law_quarter.py` | [`logs/quantum_area_law_quarter.log`](logs/quantum_area_law_quarter.log) | **0** | **PASS verdict** | 12π/48π = 0.25 **PASS**; numerical cancel **PASS**. Page curve remains OPEN. |
| 4 | `python3 scripts/tau_parseval_recompute.py` | [`logs/tau_parseval_recompute.log`](logs/tau_parseval_recompute.log) | **0** | **PASS verdict** | `PASS exact tau=1/2 ln2 at Q=2/3`. `locking_without_Q: OPEN`. |
| 5 | `python3 scripts/arxiv_package_audit.py` | [`logs/arxiv_package_audit.log`](logs/arxiv_package_audit.log) | **0** | **desk audit** | 6/6 TeX packages clean (PRTOE/note-field/tarball). Instrument hygiene; not physics. Side-wrote `docs/working_logs/_PACKAGE_AUDIT.md`. |
| 6 | `python3 scripts/test_local_gravity.py` (analytic) | [`logs/test_local_gravity_analytic.log`](logs/test_local_gravity_analytic.log) | **0** | **desk audit** | LEGACY_ST analytic map; OVERALL PASS. Comparison lane only. |
| 7 | `python3 scripts/test_bbn_activation.py` (analytic) | [`logs/test_bbn_activation_analytic.log`](logs/test_bbn_activation_analytic.log) | **0** | **desk audit** | Analytic ρ_φ/ρ_r ≪ threshold **[PASS]**. LEGACY_ST comparison only. |
| 8 | `python3 scripts/test_local_gravity.py --classy` | [`logs/test_local_gravity_classy.log`](logs/test_local_gravity_classy.log) | **1** | **FAIL** | `CosmoSevereError`: Class did not read `use_prtoe, xi_prtoe, …`. LEGACY_ST input offline in CURRENT_CORE classy. |
| 9 | `python3 scripts/test_bbn_activation.py --classy` | [`logs/test_bbn_activation_classy.log`](logs/test_bbn_activation_classy.log) | **1** | **FAIL** | Same unread `use_prtoe` input set. |
| 10 | `python3 scripts/test_legacy_st_null_limit.py --fast --null-only` | [`logs/test_legacy_st_null_limit_fast.log`](logs/test_legacy_st_null_limit_fast.log) | **1** | **FAIL** | ΛCDM leg OK; LEGACY_ST null fails unread `use_prtoe` params. |
| 11 | `python3 -c "import scripts"` | [`logs/smoke_import_scripts.log`](logs/smoke_import_scripts.log) | **0** | **desk audit** | Trivial package import smoke. |
| 12 | `scripts/run_prtoe_validation.py` | [`logs/SKIP_reasons.log`](logs/SKIP_reasons.log) | — | **SKIP** | LEGACY_ST runner needs classy `use_prtoe` compute; would FAIL same as #8–10. Not CURRENT_CORE. |
| 13 | `scripts/run_validation_suite_1_9.sh` | [`logs/SKIP_reasons.log`](logs/SKIP_reasons.log) | — | **SKIP** | Requires `./class` + use_prtoe inis (tests 2–9); CLASS-heavy; LEGACY_ST offline; risk of CPU contention with live MCMCs. Job fence: no CLASS/MCMC suite. |
| — | PolyChord / live MCMC | — | — | **SKIP** | Absolute fence. Untouched. |

**Capability probe:** [`logs/classy_capability_probe.log`](logs/classy_capability_probe.log) — `use_dcdf` is the live public path; `use_prtoe` is a struct dummy for compile (`include/background.h`), not registered as live input → unread-parameter on compute.

---

## 3. Scorecard

| metric | n |
|---|---:|
| Runs attempted | **11** (incl. smoke) |
| EXIT 0 | **8** |
| EXIT 1 (LEGACY_ST classy) | **3** |
| **PASS verdict** | **3** (BBN ε, area-law, τ Parseval) |
| **desk audit** | **5** (supertrace, arxiv audit, local-gravity analytic, bbn-activation analytic, import smoke) |
| **FAIL** | **3** (classy LEGACY_ST path) |
| **SKIP** | **2** suites + PolyChord/MCMC fence |
| Code fixes applied | **0** |
| Physics claims invented | **0** |

**Formulable arithmetic set (3):** all **PASS verdict**, EXIT 0.

**exit 0 ≠ PASS:** 8 clean exits → only **3** true PASS verdicts; remaining 5 are desk audits.

---

## 4. Fixes applied

**None.**

- Arithmetic/desk scripts: no import errors, no broken paths, no wrong labels.
- LEGACY_ST classy FAILs are **architectural** (CURRENT_CORE build does not accept `use_prtoe` as live input), not script typos. Re-enabling ST input is out of scope and would invent a core-lane change.
- No rebuild of CLASS; no MCMC surgery.

See [`EDITS.md`](EDITS.md).

---

## 5. Non-claims (explicit)

This package does **not** claim:

1. **BBN ε EXTERNAL WIN** — arithmetic only; **EXTERNAL WIN PENDING (no DOI)**.
2. **H₀ / posterior booking** — not opened; live bbnfix/routeD chains left alone.
3. **CURRENT_CORE CLASS null** — did not run `validate_dcdf.py` as a full core book (out of listed job); LEGACY_ST classy FAIL ≠ CURRENT_CORE FAIL.
4. **LEGACY_ST numerical suite PASS** — classy path **FAIL** / suites **SKIP**.
5. **Supertrace paper COMPLETE** — desk audit + unit-correction note only.
6. **Page curve / dynamical QG** — area-law pays ratio 1/4 only; Page OPEN.
7. **τ locking without Q** — remains OPEN per script JSON.
8. **PolyChord evidence** — not run.
9. **exit 0 batch = all physics PASS** — rejected by grade rule.

---

## 6. BBN ε arithmetic detail (internal)

From [`logs/recompute_eps_bound.log`](logs/recompute_eps_bound.log):

| quantity | value |
|---|---|
| Y_p0 (ε=0) | 0.246891 |
| dY_p/dε | 0.00163 per %ε |
| Aver Y_p | 0.2453 ± 0.0034 |
| ε 1σ ceiling | 1.110% |
| **ε 2σ ceiling** | **3.196%** |
| paper claim 2σ | 3.20% |
| match | **PASS** |

Status: **ARITHMETIC VERIFIED (internal)** · **EXTERNAL WIN PENDING (no DOI)**.

---

## 7. Return path

**REPORT:** `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/validation_suite_20260804/REPORT.md`

*NO FABRICATIONS. Live MCMCs untouched. No PolyChord. No premature H₀ book.*
