# CURRENT_CORE full validation — 2026-08-04

**Run dir:** `docs/working_logs/_runs/current_core_full_20260804/`  
**Script:** `validate_dcdf.py` (CURRENT_CORE `use_dcdf` pure fluid; **not** LEGACY_ST `use_prtoe`)  
**Full log:** `validate_dcdf_full.log` (EXIT:0)  
**Companion logs:** `clustering_full.log`, `legacy_st_null_limit.log`, `legacy_st_probe.log`  
**Rules:** NO FABRICATIONS · no PolyChord · no MCMC surgery

---

## Definition of done

| item | status |
|---|---|
| `validate_dcdf_full.log` present + complete | **YES** |
| T1 blocking gates (null + boundary) | **PASS** |
| REPORT with T1/T2 gate table | **this file** |
| `CURES.md` (scratch `dcdf_beta` inventory) | **YES** |
| scratch triad YAMLs safe (no live `dcdf_beta`) | **YES** |

---

## T1 / T2 gate table (from `validate_dcdf_full.log`)

| tier | gate | result | detail |
|---|---|---|---|
| **T1** | null_limit | **PASS** | σ₈ LCDM 0.8229 vs Null 0.7959 (Δ 3.276e-02); P(k=0.1) Δ 7.110e-02; C_ℓ(TT,ℓ=200) Δ 2.265e-02 — pure dCDF clustering reasonable |
| **T1** | timing | **WARN** | Single CLASS call **47.01s** (min 43.67s, max 50.01s); PolyChord estimate 15k×47.0s ≈ **195.9 CPU-hrs** — slow for nested sampling; OK for Metropolis/evaluate (**PolyChord deferred**) |
| **T1** | boundary | **PASS** | 7/7 stable: ρ_inf=0.01 (σ₈=1.4211), ρ_inf=0.90 (0.2272), deltam_mode 0/1/2 (0.2387 / 0.7959 / 0.7925), ξ_Neff=0.0/0.5 (0.7959 / 0.7668) |
| **T2** | bao | **PASS** | r_s(drag) = **148.77 Mpc** (expected 140–160) |
| **T2** | cmb_peaks | **PASS** | First peak dCDF ℓ=222 vs LCDM ℓ=221, **Δℓ=1** |
| **T2** | fsigma8 | **WARN** | z=0.38 fσ₈=0.5942 (~OK vs BOSS 0.497); z=0.51 0.5939 / 0.458 (**LARGE**); z=0.61 0.5888 / 0.436 (**LARGE**) — advisory, not blocking |

### Blocking summary

```
✓ TIER 1 BLOCKING GATES PASS (null + boundary) — CURRENT_CORE instrument OK
  (PolyChord nested evidence still deferred on this box; MCMC Metropolis separate)
EXIT:0
```

| blocking question | answer |
|---|---|
| null_limit PASS? | **YES** |
| boundary PASS? | **YES** |
| timing FAIL (hard)? | **NO** (WARN only) |
| T1 overall | **PASS** |
| Suite exit | **0** |

---

## What T1 null_limit / boundary actually mean

T1 **PASS** is a genuine instrument gate computed by `validate_dcdf.py` — not a narrative stamp. Thresholds and author intent are disclosed here so PASS is not over-read as ΛCDM recovery or precision cosmology agreement.

### null_limit (source: `validate_dcdf.py` ~107–108)

| item | content |
|---|---|
| **Code gate** | `if ds8 < 0.10 and dpk < 0.10` — fractional \|Δσ₈\| and \|ΔP(k=0.1)\| vs ΛCDM reference |
| **Author comment in source** | *"Pure dCDF vs ΛCDM can differ at O(few%); gate is **not pathologically wrong**"* |
| **What PASS means** | Clustering stays inside a **10% band** of the ΛCDM reference — **not** recovery of ΛCDM, **not** a precision posterior match |
| **What PASS does not mean** | Booked agreement with ΛCDM growth; S₈ tension resolution; production cosmology acceptance |

**Measured this run (from table above):**

| observable | fractional Δ vs LCDM |
|---|---|
| σ₈ | ~ **3.28×10⁻²** (0.8229 → 0.7959) |
| P(k=0.1) | ~ **7.11×10⁻²** |
| C_ℓ(TT, ℓ=200) | ~ **2.27×10⁻²** (reported; **not** in the hard `ds8`/`dpk` predicate) |

All three sit inside the 10% band; the hard gate only requires σ₈ and P(k). The model does **not** recover ΛCDM — it remains close enough that the instrument author grades clustering “not pathologically wrong.”

### boundary (source: `validate_dcdf.py` ~185, 193–195)

| item | content |
|---|---|
| **Code gate** | Each of 7 parameter points: compute succeeds **and** `0.0 < sigma8 < 2.0` |
| **What PASS means** | **Stability / did-not-crash** across the named boundary sweep — finite σ₈ in (0, 2) |
| **What PASS does not mean** | Precision cosmology agreement; physical preferability of any boundary point; recovery of a fiducial σ₈ |

**Measured this run:** 7/7 stable. Disclosed σ₈ **span ≈ 0.227 – 1.421** (ρ_inf=0.90 → 0.2272; ρ_inf=0.01 → 1.4211; other points mid-range). A span that wide is consistent with a crash-or-not gate, not with a tight cosmology acceptance cut.

### Honesty keep

- T1 overall remains **PASS** (honest instrument gate as coded).
- Do **not** market null_limit PASS as “dCDF ≈ ΛCDM” or boundary PASS as “physics validated across parameter space.”
- Timing WARN and fσ₈ WARN stay advisory (unchanged).

*NO FABRICATIONS — thresholds read from `validate_dcdf.py`; measured values from this REPORT’s log table.*

---

## Companion surfaces (same run dir)

| surface | log | result |
|---|---|---|
| Clustering smoke (`test_dcdf_clustering`) | `clustering_full.log` | **SUCCESS** — P(k=0.1) ratio dCDF/LCDM **0.9289**; σ₈ 0.7962 vs 0.8232; EXIT:0 |
| LEGACY_ST null limit (`use_prtoe`) | `legacy_st_null_limit.log` | **FAILED as expected** — CLASS does not read `use_prtoe` / ST knobs (not in this build); path is comparison baggage only, not CURRENT_CORE |
| LEGACY_ST probe | `legacy_st_probe.log` | **UNAVAILABLE/FAIL expected** if CLASS not built with ST flag |

LEGACY_ST failures **do not** fail the CURRENT_CORE gate. CURRENT_CORE = `use_dcdf` + pure fluid (v5: `dcdf_beta` retired).

---

## API / hygiene notes

- **v5:** `dcdf_beta` retired 2026-07-05; CLASS **hard-errors** if present. EoS \(w=-\rho_\mathrm{inf}/\rho\), \(c_s^2\equiv 0\); conv/thaw default off.
- Prior cure of the suite itself: `docs/working_logs/_runs/open_board_split_20260803/VALIDATE_DCDF_V5_CURE_20260804.md`.
- This full run reconfirms the same T1/T2 pattern as `VALIDATE_DCDF_V5_20260804c.log` (timing ~47s here vs ~57s there; physics gates unchanged).

---

## Scratch cure (see `CURES.md`)

| file | action |
|---|---|
| `scratch/eval_triad.yaml` | commented out live `dcdf_beta` |
| `scratch/eval_triad.input.yaml` | commented out live `dcdf_beta` |
| `scratch/eval_triad.updated.yaml` | commented out `input_params` entry + params block |

Post-cure YAML parse: **no** active `params.dcdf_beta` / `input_params: dcdf_beta`. Accidental cobaya evaluate on triad YAMLs will not hard-error CLASS on the retired knob.

---

## Explicit non-claims

- No PolyChord nested evidence run or booked.
- No MCMC chain surgery; bbnfix / routeD left alone.
- fσ₈ WARN is **not** a T1 failure and is not marketed as BOSS agreement.
- LEGACY_ST unavailability is **not** a CURRENT_CORE regression.

*NO FABRICATIONS.*
