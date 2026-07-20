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

**Update 2026-07-19:** conv_desi WAS relaunched (2026-07-18, per T4's superseding banner) and is
past burn-in — first progress row landed (N = 384, R−1 = NaN → numeric expected soon); its
relaunch debt above is PAID. dyad_mnu_omk remains down. The two armed flags stand unchanged:
routeD at R−1 = 16.80 today (improving from ~21, still far from the bar; the thaw-floor flag
untestable until convergence), zon_disp at 23.31 (the z_on drift flag likewise). Nothing here
is a result; the R−1 < 0.05 bar governs.

## Why they are not converging — the acceptance rate, read across all five (2026-07-20)

**The `.progress` columns are `N, timestamp, acceptance_rate, Rminus1, Rminus1_cl`.** Column 3 is the
acceptance rate, not R−1; reading it as R−1 gives a spuriously converged-looking number and that
mistake was made once in this session before the header was checked.

Read correctly, the acceptance rate is the more informative column right now, and it says the same
thing three independent ways.

**Within each chain, acceptance climbs monotonically toward 1.** routeD has risen every single row of
its history — 0.897 → 0.991 across thirteen rows and six days — while R−1 oscillated between 8 and 25
with no downward trend after N ≈ 2900. conv_desi, only fifteen hours old, is already at 0.973 and
climbing (0.937 → 0.954 → 0.973) with R−1 *rising*, 19.16 → 27.55.

**Across chains, acceptance orders them by how badly they fail.**

| chain | acceptance | R−1 | state |
|---|---|---|---|
| dyad_mnu | **0.921** | **0.176** | the only one near convergence |
| zon_disp | 0.954 | 23.3 | parked, unconverged |
| conv_desi | 0.973 | 27.6 (rising) | live |
| zon | 0.988 | 40.4 | **died** |
| routeD | **0.991** | 24.9 | live, six days |

The single inversion is routeD against zon, and routeD has 5408 samples to zon's 832 — more grinding,
not better health.

**What that supports, and what it does not.** Optimal acceptance for a chain of this dimensionality is
≈ 0.23; every chain here runs at three to four times that. Acceptance approaching 1 with R−1 flat or
rising is the standard signature of **a proposal too small to explore** — the chain accepts nearly
every step because every step is tiny. conv_desi's *first* recorded point is already 0.937, which
points at the proposal being small from initialisation rather than only shrinking later under
`learn_proposal: True`. **It does not establish the mechanism**: seeded covmat, proposal scaling, or
block structure all remain candidates, and five chains with different data and parameters are not a
controlled experiment.

**The consequence for the two flags above is sharper than "unconverged".** A chain that never explores
does not merely lack precision — its posterior is a record of where it started. **routeD's thaw floor
at 0.129, ~16σ off zero, should be read as an artefact of a chain that has not moved**, not as a
marginal result awaiting confirmation. The same caution applies to zon_disp's log₁₀z_on drift toward
the 7.8 failure line. Neither is evidence against the model, and neither would become evidence by
running longer under this configuration.

**Owner's call, and it is a configuration decision rather than a wait.** Nothing here was touched.
