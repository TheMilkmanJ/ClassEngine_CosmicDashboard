# T7 REPORT — Koide Wilson inputs hunt

**Date:** 2026-08-04  
**Package:** `docs/working_logs/_runs/theory_construction_20260804/desk_t7_koide_wilson_20260804/`  
**Worker:** Grok Build subagent (T7)  
**Prior:** `koide_residual` — Wilson 5/5 MISSING_INPUTS; packaging (c) LOCKED; thermal dead  

## Fences (binding)

| Fence | Status |
|---|---|
| NO FABRICATIONS | enforced |
| Do not invent gauge fields / holonomy numbers to get exit 0 | enforced |
| Do not restore thermal delivery as land | enforced (dead) |
| Packaging lane (c) | **LOCKED** (untouched) |
| Leave MCMCs | observed |
| exit0 ≠ PASS; inventory exit 2 expected | observed |

---

## 1. Mission and result

**Mission:** Corpus-hunt each of five Wilson MISSING_INPUTS with file:line status PRESENT / PARTIAL / MISSING; update status honestly; list licensed fills without free dials; reconfirm desk audits ≠ mechanism close.

**Result:**

| metric | value |
|---|---:|
| **n_filled** | **0** |
| **n_still_missing** | **5** |
| **grade** | **OPEN-BLOCKED · MISSING_INPUTS 5/5** |
| θ_W scored | 0 |
| bins scored | 0 |
| inventory exit | **2** |

**No change** relative to `debt_koide_wilson_20260803` and `koide_residual` reconfirm. Hunt found **zero** new PRESENT inputs.

---

## 2. Hunt summary (detail in WILSON_HUNT.md)

| # | Requirement | Status | One-line proof |
|---|---|---|---|
| 1 | `dark_SU2_A_mu` | **MISSING** | No data/output A archive; T14 ψ = H_kin condensate; CLASS tests = metric gauge |
| 2 | `family_cycle_path_C` | **PARTIAL** | Equilateral topology yes; √3 ≠ phase c_K; phase spacing circular for 2/9 test |
| 3 | `winding_background_n` | **MISSING** | n ≳ 1.65 bound; L_gen unassigned; Widnall ≠ family dark-gauge n |
| 4 | `alpha_d_or_electric_projection` | **PARTIAL** | α_d ≲ 2.2 window; pure-gauge collapses; hybrid connection unbuilt as field |
| 5 | `holonomy_evaluator` | **MISSING** | Only inventory gate; evaluator scripts absent |

PARTIAL and MISSING both **block** zero-knob scoring → **5/5 still missing** for fill count.

Instrument re-run:

```
nice -n 19 python3 scripts/koide_wilson_holonomy_inventory.py
→ exit 2; logs/koide_wilson_holonomy_inventory.log
```

Filesystem reconfirm of named candidates: **all ABSENT**  
(`data/dark_su2_gauge_config.npy`, `data/wilson_Amu.npy`, `data/family_triangle_connection.json`, `output/dark_su2_gauge.dat`, `scripts/koide_wilson_holonomy.py`, `scripts/wilson_family_cycle.py`, `scripts/branch_a_holonomy.py`).

---

## 3. What would fill each without free dial

| Input | Licensed fill | Forbidden |
|---|---|---|
| A_μ | Lattice SU(2) N_f=3 configs **or** derived hybrid connection with **fixed** dual-SC parameters | Toy A_μ; ψ as A_μ; fit to θ_B |
| Path C | Independent face spacing (screened correlator / lattice), not Q/τ | Phase-derived c_K to test 2/9 |
| n | L_gen determination → fixed (n, orientation) **or** n-independence proof | Widnall pick; bound as fixed |
| α_d / projection | Fixed coupling + constructed hybrid at same scale as A_μ | Bound edge dial; pure-gauge-only |
| Evaluator | After 1–4: path-ordered / electric holonomy angle; score bins once | Embed 2/9; score before A_μ |

HIT_PRIMARY would crown Branch A as **#102 candidate only**; **#101 remains open**.

---

## 4. Optional: tau_parseval / koide_lock

| Script | Role | Residual impact |
|---|---|---|
| `tau_parseval_recompute.py` | Desk: τ=½ln2 exact at Q=2/3; `locking_without_Q: OPEN` | **Not** mechanism close |
| `koide_lock_algebra_verification.py` | Desk: a=3b ⇔ ρ²=1/2 algebra | **Not** mechanism close |

Both are **desk audits / identities**, already stamped as such in `PRTOE_koide_relation.md` and theory-walls queue. T7 does not re-promote them.

---

## 5. Packaging / residual freeze (unchanged)

```
LOCKED packaging (c) — relation = unexplained regularity; protection paid
KILLED thermal/flat — 1025.4 ppm vs 6 ppm (~171×)
OPEN #101 / #102 — one node
OPEN-BLOCKED Wilson Branch A — MISSING_INPUTS 5/5
PAID bins pre-registration — unscored
NO invent A_μ · NO fake Wilson close · NO thermal restore
```

---

## 6. Deliverables

| File | Role |
|---|---|
| [`REPORT.md`](./REPORT.md) | this executive write-up |
| [`WILSON_HUNT.md`](./WILSON_HUNT.md) | file:line hunt per input + licensed fills |
| [`STATUS_TABLE.md`](./STATUS_TABLE.md) | honest status table + counts |
| [`SURVIVORS.md`](./SURVIVORS.md) | what remains / next work |
| [`NON_CLAIMS.md`](./NON_CLAIMS.md) | absolute non-claims |
| [`MASTER.md`](./MASTER.md) | stamp |
| [`logs/koide_wilson_holonomy_inventory.log`](./logs/koide_wilson_holonomy_inventory.log) | re-run capture |
| [`logs/EXIT_CODE.txt`](./logs/EXIT_CODE.txt) | `2` |

---

## 7. One-liner

> **T7 Wilson hunt: n_filled=0, n_still_missing=5, grade=OPEN-BLOCKED MISSING_INPUTS 5/5. No θ_W. No invent. Thermal still dead. Packaging (c) still LOCKED.**

*NO FABRICATIONS. exit0≠PASS. Leave MCMCs. No fake Wilson close. No restore thermal delivery as land.*
