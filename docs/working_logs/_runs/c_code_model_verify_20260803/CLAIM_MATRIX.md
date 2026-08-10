# Claim → C-code matrix (verified by source + classy spot-checks)

| # | Model claim | C location | Match? | Notes |
|---|---|---|---|---|
| 1 | \(w=-\rho_\infty/\rho\), \(p=-\rho_\infty\) | `include/background.h` `w_dcdf()`; `source/background.c` ~615–629 | **YES** | Spot-check T1–T2 |
| 2 | \(c_s^2\equiv 0\) | `cs2_dcdf()` | **YES** | β removed 2026-07-05 |
| 3 | Continuity fixed point at floor | `background.c` ~3044–3056 | **YES** | |
| 4 | Conversion: matter-part → free-streaming DR | `dcdf_conv_rate`, ODE, `perturbations.c` multipoles | **YES** | Linear hierarchy when g>0 |
| 5 | #17 rad-like onset | `dcdf_rho_rad` / `dcdf_z_rad_onset` | **YES** | **Not** in `(.)w_dcdf` column |
| 6 | Route-D thaw floor | `dcdf_floor_thaw` E_th,P_E ~658–668 | **YES** | Does **not** change `w_dcdf` column (by design) |
| 7 | Dyad / \(m_e(z)\) | `background_varconst_*` + thermo | **YES** | Path present |
| 8 | No modified gravity | standard GR + fluid | **YES** | |
| 9 | P-018 \(w_{DE}=-1\) rigid | requires thaw=0, no free wiggle | **CONDITIONAL** | RouteD thaw **on** breaks P-018 |
| 10 | T14 / BBN PRyM / Koide | outside CLASS | **N/A** | Different codes |

## Known diagnostic traps

1. **`(.)w_dcdf` ≠ full dark-sector w** — omit conversion, #17 rad, thaw from that column.
2. **Thaw instrument test:** Δw_dcdf ~ 0 but age and p_tot change (confirmed).
3. **Pre-onset w=1/3** lives in #17 + SM radiation budget, not `w_dcdf`.

## Verdict

**Production CLASS C implements the as-built dCDF cosmology model.**  
Branches (thaw, conversion) are explicit and documented. Full theory stack is larger than this C tree.
