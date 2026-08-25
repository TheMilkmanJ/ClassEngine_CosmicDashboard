# Nested completion scan — 2026-08-25 03:53 UTC

OPS_HEALTH plus one new **finished one-leg** harvest. Did **not** book ΔlnZ.

## Finished LCDM UltraNest (JSON on disk, `done iterating`)

| Anchor | Model | Engine | Host | logZ | Notes |
|---|---|---|---|---|---|
| SH0ES | LCDM | UltraNest | `i-0e353f38544397a6d` (stopped) | −1413.4857 ± 0.5842 | Stored `un_lcdm_shoes_finished_20260824/` |
| TRGB | LCDM | UltraNest | `i-0c8df2e18ea719094` (stopped) | −1374.3615 ± 0.3982 | Stored `un_lcdm_trgb_finished_20260824/` |
| no-H0 | LCDM | UltraNest | `i-02eb4dcbd633819bc` | −1374.4346 ± 0.3765 | **New harvest** `un_lcdm_noh0_finished_20260825/` |

## Still running (not harvested)

From the 2026-08-25 ~03:30 UTC fleet peel. Mid-run logZ is health only.

| Role | Host | Snapshot |
|---|---|---|
| SH0ES dyad UN | `i-04ead482af737e7bf` | rem **15.0%** logZ −1411.24 |
| TRGB dyad UN | `i-0907059ca35aaedb4` | rem **61.1%** logZ −1378.07 |
| noH0 dyad UN | `i-050dd009197af1978` | rem **70.6%** logZ −1378.73 |
| SH0ES dyad PC | `i-0c65cc61a575bdfa7` | ndead 14178 still_active −1418.15 ± 0.22 |
| SH0ES LCDM PC | `i-0941e936fd100c309` | ndead 15863 still_active −1415.72 ± 0.23 |
| TRGB dyad PC | `i-06847ebdfd55bac11` | ndead 13133 still_active −1389.62 ± 0.22 |
| TRGB LCDM PC | `i-0d1915a2ac2d5c5af` | ndead 14806 still_active −1377.94 ± 0.22 |
| noH0 PC both | `i-0ada8e…` / `i-088a37…` | workers LIVE; peel glob missed `.stats` |

SH0ES LCDM **UltraNest** did not move: it finished at −1413.49. SH0ES LCDM **PolyChord** partial logZ went from −1416.4 (24 Aug scan, ndead 15309) to −1415.72 (ndead 15863). That is mid-run volume, not a new booked Z, and not mixable with UN.

Do not mix SH0ES vs TRGB vs no-H0 logZ. Do not compute ΔlnZ until the matching dyad summary exists.
