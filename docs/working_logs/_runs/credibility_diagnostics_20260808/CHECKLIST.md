# Credibility diagnostics checklist — PRTOE bbnfix program

**Purpose.** What a skeptical physicist would demand before treating this as more than a careful side project.  
**Rule.** No claim of COMPLETE or “win” until the gate + evidence rows below are green with methods labeled.

---

## A. Statistical gates (already partly done)

| # | Item | Status target | How |
|---|---|---|---|
| A1 | Dual-gate book | both legs R−1 < 0.05 **and** `converged: true` | `python3 scripts/book_bbnfix_when_ready.py` |
| A2 | GetDist posteriors | 3 ranks, ignore_rows=0.3, means±σ | booking REPORT |
| A3 | MAP / min −logpost | reported per leg + Δ proxy | `bbnfix_delta_chi2_proxy.py` |
| A4 | Sample-cov Laplace | ΔlnZ + cond(Σ) | `laplace_from_bbnfix_chains.py` |
| A5 | Soft-mode flag | cond(Σ) ≫ 10⁶ → **do not headline ΔlnZ** | auto in Laplace script |

**Old-BAO bbnfix (docs/chains):** A1–A4 done; A5 **failed soft** (cond ~ 1e8; ΔlnZ ≈ +0.21).

---

## B. Posterior health (required for credibility)

| # | Item | Pass criterion |
|---|---|---|
| B1 | Trace / rank agreement | all 3 ranks overlap in 1D marginals for H0, Σmν, key model params |
| B2 | ESS | GetDist effective samples ≳ 200 (prefer ≳ 500) on key params |
| B3 | Gelman–Rubin | max R−1 (GetDist) consistent with progress R−1 < 0.05 |
| B4 | Corner / 2D | no obvious multi-basin on (H0, ρ∞), (varying_me, ωb), etc. |
| B5 | Prior–posterior | prior not wholly driving; plot prior vs posterior for free params |

Script: `python3 scripts/bbnfix_posterior_diagnostics.py --chain-dir docs/chains`

---

## C. Evidence (the bar that moves “side project” → “interesting paper”)

| # | Method | Pass for *interest* | Pass for *strong claim* |
|---|---|---|---|
| C1 | Nested sampling (PolyChord), **matched** dyad vs ΛCDM | ΔlnZ ≳ +2.5 with error bar | ≳ +5, both legs finished |
| C2 | Hessian Laplace at MAP (finite-diff −ln Lπ) | agrees with nested within ~1–2 | same |
| C3 | Sample-cov Laplace | diagnostics only if cond OK | never sole headline if cond ≫ 10⁶ |
| C4 | Prior sensitivity | ΔlnZ stable under reasonable prior widen/narrow | required for claims |
| C5 | Stack sensitivity | DESI-DR2 twin pair converges; same qualitative story | required for modern BAO |

**Do not** rebrand historical pre-bbnfix ΔlnZ ≈ +2.6 as this stack’s result.

---

## D. Theory / honesty packaging

| # | Item |
|---|---|
| D1 | Fixed stack statement (likelihoods, BBN prior, YHe, classy flags) |
| D2 | Parameter count and which are “extra” vs ΛCDM twin |
| D3 | Explicit exposures (e.g. w=−1 floor vs DESI DE preference) |
| D4 | Preregistered predictions vs post-hoc |
| D5 | What would **kill** the model (named) |

---

## E. Reproducibility

| # | Item |
|---|---|
| E1 | Public or archived yamls + packages_path hashes |
| E2 | Chain files + progress + checkpoint |
| E3 | One-command book + diagnostics scripts |
| E4 | AWS/on-demand launch notes with instance id + AMI |

---

## Priority order (do this, not everything at once)

1. **B1–B3** on booked old-BAO pair (cheap, local)  
2. **C2** Hessian Laplace at MAP (medium cost; CLASS calls)  
3. Keep **DESI-DR2** MCMCs to dual-gate  
4. **C1** PolyChord matched pair only after Fortran/stats bugs fixed  
5. **C4–C5** before any public “evidence” language  

---

## Honest bar for an external physicist

| They would say | If… |
|---|---|
| “Interesting null / pilot” | A done, B mostly clean, C still soft |
| “Worth a methods + results note” | C1 or solid C2 with ΔlnZ ≳ 2.5, B clean |
| “Competitive cosmology paper” | C1+C2 agree, C4–C5, D–E tight |
| “Side project / not ready” | Headline ΔlnZ from soft sample-cov alone |
