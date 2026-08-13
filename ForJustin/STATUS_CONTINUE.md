# Status — residual integrate (currency 2026-08-12)

## Outsider path (historical packages still on disk)

| Doc | Role |
|---|---|
| [`docs/working_logs/_runs/master_integrate_20260804/BOARD_DASHBOARD.md`](../docs/working_logs/_runs/master_integrate_20260804/BOARD_DASHBOARD.md) | Owner one-pager |
| [`docs/working_logs/_runs/improve_loop_20260804/BOARD_STATUS.md`](../docs/working_logs/_runs/improve_loop_20260804/BOARD_STATUS.md) | Living delivery + red column |
| [`docs/PRTOE_honest_status.md`](../docs/PRTOE_honest_status.md) | **Living** machine + honesty stamp (**2026-08-12**) |

## Machine (currency 2026-08-12)

### MCMC dual-gates — BOOKED

| pair | status | H₀ dyad / lcdm | receipt |
|---|---|---|---|
| old-BAO bbnfix SH0ES | BOOKED Stage A+B | 70.05 / 68.35 | `bbnfix_booking_20260808_005626` |
| DESI-DR2 SH0ES | BOOKED Stage A | **70.30 / 68.73** | `bbnfix_booking_desidr2_sh0es_20260811_094254` |
| DESI-DR2 **TRGB** | **BOOKED Stage A** | **68.90 / 68.39** | `trgb_booking_desidr2_20260812` |
| RouteD | BOOKED Stage A | 69.63 | `routed_booking_20260810` |

**Ladder takeaway:** SH0ES pulls dyad H₀ high (~70.3); TRGB does not (~68.9). Do not mix stacks.

### Nested evidence — LIVE (not bookable mid-run)

| engine | host | status |
|---|---|---|
| UltraNest dyad ×96 | `i-04ead482af737e7bf` | **RUNNING** |
| UltraNest lcdm ×96 | `i-0e353f38544397a6d` | **RUNNING** |
| PolyChord dyad ×96 native GIL | `i-0c65cc61a575bdfa7` | **RUNNING** |
| PolyChord lcdm ×48 native GIL | `i-096d08d2dc9d8f42c` | relaunched after logL tuple fix (1.20.x) |

**Hang fix:** `Cobaya/pypolychord_GIL_callbacks.patch` — multi-rank isolation PASS.  
**Nested ΔlnZ:** only after both engines finish. Mid-run logZ forbidden.

### Fleet / cost

- Quota **512** vCPU.
- Idle `i-090c0275d8198ae14` (c7i.12xlarge) **stopped** 2026-08-12.

### BBN ε

**ARITHMETIC VERIFIED (internal)** (3.196% ≈ 3.20%). **EXTERNAL WIN PENDING (no DOI)**.

### Theory residual (unchanged)

Page Q6 OPEN (T8); Bounce OPEN-BLOCKED; Koide MISSING_INPUT; Strong CP COMPLETE-ABSTENTION.
See honest_status residual board.

## Owner next (when free)

1. Leave nested fleet alone for days; do not quote mid-run logZ.
2. Optional: send Catherine email (`catherine_triage_20260811/EMAIL_TO_CATHERINE_20260811.md`).
3. Optional: tribunal `red: AGREE` on TRGB Stage A if Stage B publish required.
4. After UN/PC finish: book nested ΔlnZ package only.
