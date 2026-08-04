# Page construction D3 attempt — mode-count / continuum band (2026-08-04)

**NO FABRICATIONS.** Write-once artifacts. No CANDIDATE. `page_curve_claimed: false`.

---

## What D3 is

Change radiation mode band (count / continuum sample) so \(dS/du\) shape can clear early T8 without small-header thrash.  
Champion residual was **only** T8 early bin ratio **0.113** on `coevolve_v13` (stall+DC3+T2 pass).

---

## What was tried

| family | artifact class | n_modes | schedule | early/worst T8 | u_late | stall | DC3 | joint |
|---|---|---:|---|---:|---:|---|---|---|
| densify full-20 | v35 | 20 | denser default | late fail (stall class) | **0.899** | **fail** (~554) | **FAIL** | no |
| densify + dump thrash | v36 | 20 | denser | late fail | 0.899 | fail (~556) | FAIL | no |
| densify + T2 notch (`v61_D3_dense_T2_notch`) | **v37** | 20 | G_BS 4.65, BS_MILD 0.210, EXTRA 13 | late fail ratio ~1.0 at [0.89,0.9) | **0.899** | fail (~556) | FAIL | no |
| midband-12 + champion pins (`v62_D3_mid12_champ_sched`) | **v38** | 12 (mid of 20) | v13 pins | late fail | **0.869** | fail | FAIL | no |

Week2 densify: `quantum_page_bogoliubov_week2.midband_omegas` temporarily 20 fracs; archive
`page_curve/week2_bogoliubov_20mode_D3.json`. Live week2 restored to **9-mode** champion band.

---

## Learning

1. Full densify **does** change \(S(u)\) shape (early-bin stickiness can ease in intermediate self-scores) but **breaks** unit-weight reach: envelope freezes short of \(u=0.9\) with massive late stalls.
2. Dump notches on densified band (v37) **do not** cross the T2 bar — still \(u_{\mathrm{late}}\approx 0.899\).
3. Midband-12 with champion couplings (v38) is **worse** reach than full-20, not a sweet spot.
4. Mode-count change is **not free**: co-evolution schedule was calibrated to the 9-mode greybody set; densify without a new microphysical dump law is thrash-adjacent.

## Standing champion

**`coevolve_v13.json`** still best joint near-miss:

| gate | result |
|---|---|
| T1–T6 + coevo (stall≤10, co_frac, swap, peak_in_motion) | **PASS** |
| T2 / DC3 | **PASS** |
| **T8** | **FAIL** — early [0.10,0.11) range/S* = **0.113** |
| CANDIDATE_TURN_binding | **False** |
| page_curve_claimed | **false** |

Script header restored: **`v23_champion_locked`**. Live week2 = 9-mode.

## Deeper construction board status

| ID | Status |
|---|---|
| **D1** two-phase BS→TMS | Tried — early T8 better; T2 not joint (`B_A_D1_ATTEMPT.md`) |
| **D2** free \(w_c\equiv 1\) | Tried — **no-op** on champion path (`B_A_D2_ATTEMPT.md`) |
| **D3** mode band densify | Tried — **not joint** (this note) |
| **D4** accept instrument near-miss | **Active default** until new microphysics |

## Explicit non-actions

- No further densify / G_BS / BS_MILD thrash on this construction  
- No T8 threshold loosen / bin subsample  
- No CANDIDATE packet / `page_curve_claimed`  
- Q6 remains **OPEN**

*NO FABRICATIONS.*
