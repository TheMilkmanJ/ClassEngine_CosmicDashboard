# Chain snapshot — preliminary, NONE booked (2026-07-17)

*A convergence + posterior read of the standing MCMC chains, taken while the PolyChord evidence pair
(cmp_prtoe_fixed + pc_lcdm) runs. **Everything here is PRELIMINARY: no chain except dyad_mnu is near
R−1 < 0.05, so nothing is a result** — this file exists only so the two live flags aren't lost. The
REFEREE_CALENDAR's R−1 < 0.05 bar must be met before any of these grades count.*

| chain | R−1 (latest) | state | preliminary read |
|---|---|---|---|
| dyad_mnu_mcmc | 0.176 | MARGINAL | Σm_ν mean **59.6 meV** — lands on the 61.4 meV normal-ordering prediction; but inverted ordering **not yet excluded** (95% UL 155 meV). Encouraging, not final. |
| cmp_prtoe_zon_disp | ~23 | NOT converged | log₁₀z_on ≈ 7.72, **drifting above** the 3α-compatible band [7.4, 7.7] toward the 7.8 failure line — unfavourable trend for P-040 (α_c = 3α), unconverged. |
| cmp_prtoe_routeD | ~21 | NOT converged | dcdf_floor_thaw ≈ **0.129, ~16σ off 0** at face value → would be evidence *against* w = −1. But an unconverged chain piling up off a prior boundary is the classic false-exclusion trap — **a flag to re-run, not a conclusion.** |
| cmp_prtoe_zon | ~40 | NOT converged | superseded by zon_disp. |
| cmp_prtoe_conv_desi | — | NO DATA | died mid-restart; needs relaunch. |
| cmp_prtoe_twist | ∞ | unstarted | w0waCDM extension (the separate twist-floor thread, not the main w = −1 claim). |
| dyad_mnu_omk | ∞ | NO DATA | never produced accepted samples; needs relaunch. |

**The two flags to re-check the moment a chain converges** (both currently untrustworthy from
non-convergence, both would matter if they hold):
1. **routeD's thaw floor ≠ 0** — if it survives convergence, it threatens the w = −1 prediction.
2. **zon_disp's z_on above the 3α band** — if it survives, it's tension for α_c = 3α (P-040).

**Also owed:** conv_desi and dyad_mnu_omk produced no usable samples — relaunch needed (not done; the
cores are on the evidence pair).
