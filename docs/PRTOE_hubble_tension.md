# Hubble tension — mechanism, residual, calibration

Glossary: [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md). Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Amplitude: [PRTOE_THE_AMPLITUDE.md](PRTOE_THE_AMPLITUDE.md). Risk: [PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md). Chains: [PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md).

> ## Residual freeze — 2026-08-10 (old-BAO Stage B + DESI Stage A; nested still open)
>
> **Document job:** COMPLETE-CONDITIONAL — mechanism, owned residual, ladder ceiling, and
> literature scoreboard are written. **Booked H₀ exists on two stacks; decisive nested evidence does not.**
>
> **Old-BAO pair — BOOKED Stage A + Stage B** (authority
> `bbnfix_booking_20260808_005626/REPORT.md` · Grok red `RED_AUDIT.md` · living
> [PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md)):
>
> | leg | N | R−1 | t | converged |
> |---|---:|---:|---|---|
> | `dyad_mnu_bbnfix` | 37605 | **0.048118** | 2026-08-07T04:08:52 | **true** |
> | `cmp_lcdm_mnu_bbnfix` | 26294 | **0.049324** | 2026-08-05T11:52:10 | **true** |
>
> Three-rank GetDist (`ignore_rows=0.3`, SH0ES-conditional): dyad **H₀ = 70.052 ± 0.716**,
> `m_ncdm = 0.0671 ± 0.0583`, **S₈ = 0.821 ± 0.0097**; lcdm **H₀ = 68.345 ± 0.343**,
> `m_ncdm = 0.0192 ± 0.0174`, **S₈ = 0.824 ± 0.0081**. Triangles: `docs/plots/*_bbnfix_triangle.png`.
>
> **Evidence honesty (old-BAO):** sample-cov Laplace **ΔlnZ ≈ +0.21** (cond(Σ)~10⁸). Historical
> **ΔlnZ ≈ +2.6** is pre-bbnfix only. Hessian v2 finite but soft-mode diagnostic (not nested).
>
> **DESI-DR2 pair — BOOKED Stage A (separate instrument; do not mix)** — authority
> `desidr2_bbnfix_booking_20260810_053127` · peel `docs/chains/*_desidr2.*` · Grok red for citation:
>
> | leg | N | R−1 | converged | H₀ (GetDist 30% burn) |
> |---|---:|---:|---|---|
> | `dyad_mnu_bbnfix_desidr2` | 53482 | **0.03321** | **true** | **70.30 ± 0.54** |
> | `cmp_lcdm_mnu_bbnfix_desidr2` | 52031 | **0.041377** | **true** | **68.73 ± 0.25** |
>
> DESI sample-cov Laplace **ΔlnZ ≈ +1.31** (CHAIN_TABLES 1.305; still soft modes; **not nested**). Nested referee: UltraNest + PolyChord live on SH0ES, TRGB, and noH0. LCDM UltraNest one-legs are **finished**; dyad legs are not. **No nested ΔlnZ yet.** TRGB Stage A MCMC is **booked** (do not mix with SH0ES).
>
> **What remains open:** nested-quality comparison on DESI-DR2; do **not** use intermediate log(Z)
> or MAP peeks as evidence.
>
> **Forbidden claims:** decisive win from Laplace; mixing old-BAO with DESI posteriors; historical +2.6
> as current authority; inventing nested verdict.

**Status.** Core empirical claim of the program — built against data, not extended to it after the
fact. Two SH0ES-conditional dual-gate pairs are **booked** (old-BAO Stage B published; DESI Stage A
with peel). On both stacks the dyad sits ~1.6–1.7 above the matched ΛCDM+m_ν twin in H₀, but
evidence is only soft-mode Laplace (old-BAO **+0.21** / DESI **+1.31**), not nested. Nested twins remain open (LCDM UltraNest one-legs finished; dyad unfinished). **Do not lead with a win.**
