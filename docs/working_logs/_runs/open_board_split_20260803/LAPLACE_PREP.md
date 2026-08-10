# Laplace / Δχ² booking prep (no PolyChord)

**Stamp:** 2026-08-04 (hardened by `laplace_prep_harden_20260804`)  
**Scope:** audit only — what exists for Step C of `_POSTERIOR_BOOKING_CHECKLIST.md` when the bbnfix pair grades.  
**Hard rules:** no PolyChord / nested sampling on this box. No booking until pair gate (both R−1 < 0.05 **and** self-stop). **booking ≠ publishing.** Never quote pre-bbnfix ΔlnZ ≈ +2.6 as final bbnfix evidence without fence.

---

## Gate (must clear before any Laplace booking)

| leg | requirement |
|-----|-------------|
| R−1 | both `dyad_mnu_bbnfix` and `cmp_lcdm_mnu_bbnfix` last progress field 4 **< 0.05** |
| Self-stop | both `.checkpoint` have `converged: true`; chains idle |
| Stack | BBN-fixed production pair only — do not substitute pre-bbnfix ΔlnZ ≈ +2.6 |

Live stamp (prep harden 2026-08-04): lcdm **0.059** / dyad **0.189** / both **not-stopped** → **gate CLOSED**.

---

## Publish split — Stage A vs Stage B (post-gate)

| stage | what | command | writes forward shelf? |
|-------|------|---------|:---------------------:|
| **Stage A** (default) | book + finalize H₀ letter (stdout) + optional Δχ² proxy | `bash scripts/bbnfix_when_ready_all.sh` | **NO** — private `_runs/bbnfix_booking_*` only |
| **Red audit** | Claude audits booking package | write `bbnfix_booking_<id>/RED_AUDIT.md` with `red: AGREE` or `red: AGREE-IF` | no |
| **Stage B** | GetDist tables → `PRTOE_CHAIN_TABLES.md` | `bash scripts/bbnfix_when_ready_all.sh --write-tables` | **YES** — only with red stamp |
| Owner emergency | tables without red | `--force-tables` | YES — logged; **not** default |

`WRITE_TABLES` defaults to **0**. `--write-tables` without `RED_AUDIT` → refuse (exit 1).  
`--force-bbnfix` on `make_getdist_tables.py` is **UNBOOKABLE-only** (working_logs artifact; never living shelf).

---

## What Laplace ΔlnZ prep exists vs what waits for bbnfix book

| item | status | waits for bbnfix book? |
|------|--------|:------------------------:|
| Gate + refuse path on all booking entrypoints | **READY** | n/a (active while closed) |
| Three-rank GetDist booking card (`book_bbnfix_when_ready.py`) | **READY** (refuses now) | **YES** — card only after gate |
| H₀ letter sentence (`finalize_h0_at_convergence.py`) | **READY** (NOT YET now) | **YES** |
| Forward `PRTOE_CHAIN_TABLES.md` rows | instrument READY; **Stage B blocked** until red | **YES** + RED_AUDIT |
| Δχ² proxy (`bbnfix_delta_chi2_proxy.py`) | **READY (gate-hard)** | **YES** — still not Laplace |
| CosmicForge Laplace (Hessian) CLI path | **READY (generic)** | **YES** — only after stop; BBN-fixed yamls |
| Bookable ΔlnZ number under BBN-fixed stack | **DOES NOT EXIST** | **YES** — do not invent |
| Standalone `scripts/laplace_bbnfix.py` | **MISSING** (honest) | n/a — do not invent |
| Pre-bbnfix ΔlnZ ≈ +2.6 | **historical only** (wrong stack; SH0ES-conditional) | must not replace / rebrand as bbnfix |
| Nested / PolyChord | **OUT OF SCOPE** | do not open |

---

## Checklist Step C — inventory (READY vs MISSING)

Source of truth: `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md` § Step C.  
Full one-shot: `docs/working_logs/_runs/laplace_booking_full_20260804/`.

| piece | path | READY? | notes |
|-------|------|:------:|-------|
| Runbook Step C text | `_POSTERIOR_BOOKING_CHECKLIST.md` | **READY** | Laplace-from-MCMC; PolyChord deferred |
| H₀ letter gate (refuse until pair grades) | `scripts/finalize_h0_at_convergence.py` | **READY** | both R−1 + self-stop; stdout only; exit 2 when closed |
| GetDist booking entrypoint | `scripts/book_bbnfix_when_ready.py` | **READY** | three-rank GetDist; self-stop enforced; exit 2 refuse |
| One-shot Stage A pipeline | `scripts/bbnfix_when_ready_all.sh` | **READY** | tables OFF by default (`WRITE_TABLES=0`) |
| GetDist tables instrument | `scripts/make_getdist_tables.py` | **READY** | `--include-bbnfix` after gate; force → UNBOOKABLE only |
| CosmicForge Laplace (Hessian) | `run_cosmicforge.py` ~L2083–2095 | **READY** (generic) | `log_z_laplace = -0.5 χ² + 0.5 n log(4π) - 0.5 logdet` |
| Bridge sampling | `forge/evidence.py` | **READY** (library) | Meng–Wong; non-default |
| Standalone cobaya-pair **full** Laplace CLI | `scripts/laplace_*.py` Hessian | **MISSING** | CosmicForge path remains for ΔlnZ |
| One-shot min −logpost Δχ² helper | `scripts/bbnfix_delta_chi2_proxy.py` | **READY (gate-hard)** | not bookable Laplace |
| Bookable ΔlnZ under **BBN-fixed** stack | — | **MISSING** (blocked) | needs graded pair + Hessian/CosmicForge |
| Pre-bbnfix standing ΔlnZ ≈ +2.6 | docs / historical CosmicForge | **READY as historical only** | **fence required** — never as final bbnfix evidence |

---

## Practical booking order (when gate opens — do not run early)

### Stage A (book / finalize — default)

1. Confirm both progress R−1 < 0.05 **and** both `converged: true`; processes idle.  
2. Prefer: `bash scripts/bbnfix_when_ready_all.sh` (book → finalize → **tables blocked** → delta proxy).  
   Or manual: `book_bbnfix_when_ready.py` then `finalize_h0_at_convergence.py`.  
3. Capture private booking card under `_runs/bbnfix_booking_<stamp>/`.  
4. **Δχ² proxy** (if not via all.sh): label **proxy only** — not Laplace ΔlnZ.

### Red → Stage B (tables / publish)

5. Claude red: write `RED_AUDIT.md` with `red: AGREE` or `red: AGREE-IF`.  
6. `bash scripts/bbnfix_when_ready_all.sh --write-tables` (or gated `make_getdist_tables.py --include-bbnfix` only after intentional publish decision). Restore live banner if clobbered.

### Step C — evidence (after Stage A; not nested)

7. **Laplace ΔlnZ:** CosmicForge Hessian path only if capacity after chains stopped; book `log_z_laplace` model − ΛCDM; label **Laplace (Hessian)** + BBN-fixed stack. Confirm CLI before launch.  
8. Bridge sampling only if Laplace disputed / clearly non-Gaussian.  
9. **Never** PolyChord for this booking session.  
10. **Never** rebrand pre-bbnfix ΔlnZ ≈ +2.6 as the bbnfix-pair result.

---

## Explicit kill criteria

| # | kill if… |
|---|----------|
| K1 | Book while either R−1 ≥ 0.05 |
| K2 | Book before both `converged: true` (self-stop) |
| K3 | Quote H₀ / Σm_ν / S8 / 68% from peeks or force paths as results |
| K4 | Write living `PRTOE_CHAIN_TABLES.md` from `--force-bbnfix` (must be UNBOOKABLE path only) |
| K5 | Stage B tables without `RED_AUDIT` (`red: AGREE` / `AGREE-IF`) except owner `--force-tables` |
| K6 | PolyChord / nested sampling for this booking session |
| K7 | Kill live MCMCs to free CPU without owner order |
| K8 | Promote pre-bbnfix ΔlnZ ≈ +2.6 as bbnfix / final evidence without fence |
| K9 | Substitute RouteD for the letter H₀ pair |
| K10 | Invent `scripts/laplace_bbnfix.py` or invent a ΔlnZ number |

---

## Explicit non-actions

- Do not invent a `scripts/laplace_bbnfix.py` (MISSING is the honest state).  
- Do not invent a Laplace number. Do not run nested sampling.  
- Do not run CosmicForge / bridge while live ranks need CPU.  
- Do not quote ΔlnZ under the bbnfix stack until Stage A book lands and C.2 (or C.1 with explicit “not Laplace”) lands.  
- Do not kill chains to free Laplace compute without owner order.

*NO FABRICATIONS. NO EARLY BOOK. NO POLYCHORD. booking ≠ publishing.*
