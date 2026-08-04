# REPORT (partial) — desk_compute_full_20260804 · arithmetic

**Worker:** Grok Build (arithmetic pack grade)  
**Pack outdir:** `docs/working_logs/_runs/desk_compute_full_20260804/arithmetic/`  
**Grade artifact:** [`GRADE_arithmetic.md`](GRADE_arithmetic.md)  
**Rule:** NO FABRICATIONS · no PolyChord · no live MCMC · no H₀ book · **exit 0 ≠ PASS**  
**BBN fence:** ARITHMETIC VERIFIED (internal); **EXTERNAL WIN PENDING (no DOI)**

---

## 1. Run status

| field | value |
|---|---|
| SUMMARY | `arithmetic/SUMMARY.md` present |
| SUMMARY stamp | 2026-08-04T09:43:56.739847+00:00 |
| jobs | 9 |
| exit0 / nonzero / timeout | **9 / 0 / 0** |
| orchestrator | pack started under multi-pack orchestrator (`orchestrator.log`) |

All nine arithmetic scripts completed under `--timeout 120` without timeout or nonzero exit.

---

## 2. True grade summary (not token_PASS)

Canonical hygiene: only three objects are **PASS verdict** arithmetic cards. Everything else is **desk audit**.

| true grade | n | jobs |
|---|---:|---|
| **PASS verdict** | **3** | `bbn_eps`, `area_law_quarter`, `tau_parseval` |
| **desk audit** | **6** | `supertrace_k1`, `rho_bounce`, `fbar_lo`, `fbar_cw_lo`, `fbar_window`, `fbar_envelope` |
| **FAIL** | **0** | — |
| **timeout** | **0** | — |

**Do not write “9/9 PASS.”** Write **9/9 exit 0 · 3 PASS · 6 desk audits.**

Full row-level residual column: [`GRADE_arithmetic.md`](GRADE_arithmetic.md).

---

## 3. Headline results (desk-audited)

| job | t(s) | one-line outcome |
|---|---:|---|
| `bbn_eps` | 0.27 | ε 2σ ceiling **3.196%** ≈ paper **3.20%** — internal arithmetic PASS; external win still pending DOI |
| `supertrace_k1` | 0.57 | str[k₁]=0 (SM+3ν_R, conformal Higgs); unit wording already shelf-cured |
| `area_law_quarter` | 0.57 | S/(A/G)=**1/4** exact; Page dynamics still OPEN |
| `tau_parseval` | 1.90 | exact τ=½ln2 at Q=2/3; `locking_without_Q` OPEN |
| `rho_bounce` | 0.35 | ρ_bounce finite ~1.06 keV scale; joint bounce dynamics OPEN |
| `fbar_lo` | 1.19 | LO ~0.985%/unit c₂; c₂ underived |
| `fbar_cw_lo` | 10.94 | Track A3 CANDIDATE CLOSED; residual **a** |
| `fbar_window` | 0.14 | accumulated window preferred at modest evidence; operator form owed |
| `fbar_envelope` | 41.30 | whole-turn 2/π exact; short-N α_c escape closed only for N≲ few turns |

---

## 4. Residuals that stay OPEN (pack-level)

- BBN: **EXTERNAL WIN PENDING (no DOI)**; bbnfix not bookable from this pack  
- Page curve / dynamical S_rad(v)  
- Supertrace → absolute SI *G*  
- τ locking_without_Q  
- Bounce two-component dynamics / H_re (not paid by ρ_bounce number)  
- f̄ residuals: **c₂ / a (= −c_w)** value; operator form; α_c conflict not resolved by window/envelope alone  

No OPEN residual promoted to COMPLETE.

---

## 5. Explicit NON-PROMOTIONS (repeat for master integrate)

- No BBN external win / DOI claim  
- No bbnfix / posterior booking  
- No Page COMPLETE  
- No bounce / H_re COMPLETE  
- No f̄ Derived (CANDIDATE CLOSED max on Track A3)  
- No bulk “9/9 PASS”  
- No H₀ book · PolyChord · MCMC surgery  

See full list in [`GRADE_arithmetic.md`](GRADE_arithmetic.md).

---

## 6. Counts (return)

| metric | n |
|---|---:|
| Jobs graded | **9** |
| exit 0 | **9** |
| PASS verdict | **3** |
| desk audit | **6** |
| FAIL | **0** |
| timeout | **0** |
| OPEN residuals named (rows with residual) | **9** |
| COMPLETE promotions | **0** |
| Grade files written | **2** (`GRADE_arithmetic.md`, this REPORT) |

---

## 7. Scope note

This is a **partial** wave report for the **arithmetic** pack only. Sibling packs (`bounce`, `koide`, `baryo_rm`, `hierarchy`, `page_instrument`, `quantum_residual`, `alpha_amp`, `tests_analytic`, `current_core`, …) are out of scope here. Master integrate: `MASTER_REPORT.md` when all pack grades land.

*NO FABRICATIONS. Partial report complete.*
