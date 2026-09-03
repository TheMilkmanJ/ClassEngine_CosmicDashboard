> **Status.** Stage A posteriors are **booked** (old-BAO SH0ES + DESI-DR2 SH0ES + DESI-DR2 TRGB). Nested sampling is **launched**; LCDM UltraNest one-legs finished; dyad unfinished; mid-run log-evidence is **not bookable**. The α_c instrument **stopped**; GetDist **inconclusive** on `log10_zon`. `conv_desi` retune **stopped**; GetDist **inconclusive** on `dcdf_conv_g`. Route-D thaw is **finished** Stage A (idle; separate instrument).

# The code manifest — what is in the pipeline, what is armed, what is banned (2026-07-12)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*The inclusion law: everything proven beneficial enters the pipeline; nothing killed ever does. This
file is the single source of truth for implementation status — so every row states where a thing
lives and whether it is actually running, checked against `ps` and the file timestamps rather than
against intent.*

*Homes are named, not lettered: **CLASS source** (background.c/input.c), **yaml** (the cobaya
configs), **comparison layer** (scripts/), **doc-only** (laws and grammar with no pipeline
expression).*

## 1. IN — running now (the referee's own physics)

> ### Production instruments
>
> Authority: `docs/PRTOE_CHAIN_TABLES.md` and booking/ops packages under `working_logs/_runs/`.
>
> | stack | Stage A | Nested ΔlnZ / other machine |
> |---|---|---|
> | old-BAO SH0ES `bbnfix` | **BOOKED** | separate lane |
> | DESI-DR2 SH0ES twins | **BOOKED** | LCDM UN **FINISHED**; dyad UN + PC still live; no twin ΔlnZ |
> | DESI-DR2 TRGB twins | **BOOKED** | LCDM UN **FINISHED**; dyad UN + PC still live; no twin ΔlnZ |
> | no-local-H0 twins | — | LCDM UN **FINISHED**; dyad UN still live; no twin ΔlnZ |
> | zon_disp / α_c onset | **STOPPED** | GetDist **INCONCLUSIVE** (`log10_zon` 7.57±0.51) |
> | conv_desi | — | **STOPPED** retune; `g` **INCONCLUSIVE** (`conv_desi_retune_grade_20260824`) |
> | Nested mid-run logZ | — | **not bookable** until final summary JSON |
>
> Do **not** mix Stage A posteriors across ladder anchors. Do **not** quote mid-run nested logZ.
> Bounce theory grades live in the bounce freeze packages (path/sign partial derived; magnitude permanent non-claim; E9 honesty) — not this pipeline table.

| item | home | status |
|---|---|---|
| The dispersion shape: ρ_rad = dust·(√(1+x²)−1), exact p and dp/dloga | CLASS source: background.c | IN — the live .so, direct-eval verified (2798.7) |
| The ramped window edges: varying_transition_width (tanh fades in ln(1+z); 0 = legacy step) | CLASS source: background.c/input.c/background.h | IN — pipeline .so rebuilt clean-PATH, width=0 backward-compat verified |
| The electron-coupled scalar (varying m_e, the ramp through T_c) | CLASS source | IN |
| The dcdf unified sector (rad→CDM crossover at z_on) | CLASS source | IN |
| **BBN-fixed production pair — model** | yaml: `dyad_mnu_bbnfix.yaml` → `chains/dyad_mnu_bbnfix.*` | **BOOKED old-BAO receipt** — three-rank GetDist now exists via `bbnfix_booking_20260808_005626`; dyad **H₀ = 70.052 ± 0.716**, `m_ncdm = 0.0671 ± 0.0583`, **S₈ = 0.821 ± 0.0097** |
| **BBN-fixed production pair — ΛCDM+mν twin** | yaml: `cmp_lcdm_mnu_bbnfix.yaml` → `chains/cmp_lcdm_mnu_bbnfix.*` | **BOOKED old-BAO receipt** — lcdm **H₀ = 68.345 ± 0.343**, `m_ncdm = 0.0192 ± 0.0174`, **S₈ = 0.824 ± 0.0081** |
| **DESI-DR2 bbnfix pair — model** | yaml: `dyad_mnu_bbnfix_desidr2.yaml` | **Stage A BOOKED** (SH0ES); nested launched (LCDM UN finished; dyad live; mid-run nested logZ forbidden until finish) |
| **DESI-DR2 bbnfix pair — ΛCDM+mν twin** | yaml: `cmp_lcdm_mnu_bbnfix_desidr2.yaml` | **Stage A BOOKED** (SH0ES); nested launched (LCDM UN finished; dyad live; mid-run nested logZ forbidden until finish) |
| **Route-D thaw chain** | yaml: `cmp_prtoe_routeD.yaml` → `chains/cmp_prtoe_routeD.*` | **FINISHED / Stage A booked** (R−1≈0.054). Idle. Separate instrument — **not** dual-gate H₀ twins. |
| **The PolyChord evidence run — sampled-ε** (varying_me, A_s via logA, n_s, dcdf_rho_inf, m_ncdm all sampled) — tests whether the data prefers varying-m_e at all (Occam-penalized) and whether the ε-posterior lands on the derived 1.2543% | yaml: pc_prtoe.yaml (PolyChord) | **not running** — this specific sampled-ε config is still off. Current nested work is launched (LCDM UltraNest one-legs **finished**; dyad UN + PC still live on SH0ES, TRGB, no-H0 EV yamls; mid-run nested logZ forbidden until finish; no twin ΔlnZ) |
| **The zero-parameter run — ε/A_s/n_s fixed** (varying_me = 1.012543, A_s = 2.088058×10⁻⁹, n_s = 0.9641; only dcdf_rho_inf, z_reio, m_ncdm + nuisances sampled) — the actual *zero-extra-parameter rival to ΛCDM* test | yaml: cmp_prtoe_fixed.yaml | **not running — ended 2026-07-20 by owner decision, archived to `chains/_archive_polychord_ended_20260720_0915/`.** Current blocker is not laptop economics alone; it is the absence of a finished matching nested comparison on the current stack |
| Gold DESI-DR2 nested evidence pair-set | yaml: `*_desidr2_ev.yaml` / `*_desidr2_trgb_ev.yaml` / `*_noh0_ev.yaml` | Nested **launched**; LCDM UltraNest one-legs **FINISHED**; dyad UN + PolyChord still live; **no nested ΔlnZ bookable** (`dual_nested_runbook_20260812`; ETA stamps `nested_pc_eta_20260815`) |
| The freeze-sentinel launch guards | comparison layer: both wrappers | IN — verified quoted+unquoted |
| **zon_disp production / retune MCMC** | yaml: `cmp_prtoe_zon_disp.yaml` (archive) / `cmp_prtoe_zon_disp_retune.yaml` | **STOPPED** R−1=0.036, `converged: true`, 48 ranks harvested. GetDist **INCONCLUSIVE** on `log10_zon` (7.57±0.51; all lineup rungs inside 68%). Package: `zon_disp_retune_grade_20260821`. Not a Stage A H₀ twin |
| **conv_desi production MCMC** | yaml: `cmp_prtoe_conv_desi_retune.yaml` (Jul-22 `cmp_prtoe_conv_desi` is archive) | **STOPPED** 2026-08-24, R−1=0.0447, `converged: true`, 192 ranks. GetDist **INCONCLUSIVE** on `dcdf_conv_g` (0.080±0.072). Not Stage A; not a KiDS shear fit. Package `conv_desi_retune_grade_20260824` |

## 2. Armed — enters on its named trigger

| item | value | trigger | lands in |
|---|---|---|---|
| A_s frozen | 2.088058×10⁻⁹ = (α_c/4πk)³, concordance joint k | **IN — executed in the fixed-ε configs** (nested zero-parameter run itself is not live; nested is launched — LCDM UN one-legs finished; dyad unfinished; mid-run nested logZ forbidden until finish) | yaml |
| z_on frozen | 3.5619×10⁷ (log 7.5517 — the BOBYQA frozen-stack profile; the 3α mark hit to 0.005 dex) | **IN — fast-profiled estimate; the α_c instrument (zon_disp retune) is STOPPED** (R−1=0.036, `converged: true`); GetDist **INCONCLUSIVE** `log10_zon = 7.571 ± 0.511`. Not α_c = 3α | yaml |
| n_s stated | 0.9641 = 1 − 2/ln(M_Pl/T_on) at the profiled z_on (the value the fixed-ε configs execute; the exhibited mechanism's k-local number is 0.9677 — the delta is 0.86σ at Planck width, noted for the next config, no mid-run change) | **IN — frozen into the fixed-ε configs** | yaml |
| ρ_inf stated | the occupancy value | the α_c instrument + the triangle confirmed | yaml |
| m_ncdm stated | ≈61.35 meV | the spurion identification lifted (done — neutrino_sector §2) + P-023 resolved | yaml |
| The flow ladder correction | ω₀ = 0.77 km/s/Mpc; 73.0 → 72.2 at full coherence | genesis sizing fixes the coherent fraction | comparison layer: flow_ladder_correction.py (built) |
