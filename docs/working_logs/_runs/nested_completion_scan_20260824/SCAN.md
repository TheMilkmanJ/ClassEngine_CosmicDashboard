# Nested completion scan — 2026-08-24 18:00 UTC

OPS_HEALTH only. Harvested finished UltraNest summaries; did **not** book ΔlnZ.

## Finished (JSON on disk, `done iterating`)

| Anchor | Model | Engine | Host | logZ | Notes |
|---|---|---|---|---|---|
| SH0ES | LCDM | UltraNest | `i-0e353f38544397a6d` | −1413.4857 ± 0.5842 | Already stored `un_lcdm_shoes_finished_20260824/` |
| TRGB | LCDM | UltraNest | `i-0c8df2e18ea719094` | −1374.3615 ± 0.3982 | **New harvest** `un_lcdm_trgb_finished_20260824/` |

## Still running (not harvested)

| Role | Host | State | Snapshot |
|---|---|---|---|
| SH0ES dyad UN | `i-04ead482af737e7bf` | LIVE 98 UN | logZ −1411.31 rem **21.1%** |
| TRGB dyad UN | `i-0907059ca35aaedb4` | LIVE 98 UN | logZ −1378.37 rem **71.5%** |
| noH0 dyad UN | `i-050dd009197af1978` | LIVE 98 UN | logZ −1379.09 rem **79.6%** |
| noH0 LCDM UN | `i-02eb4dcbd633819bc` | LIVE 98 UN | logZ −1374.45 rem **1.86%** (close, not done) |
| SH0ES dyad PC | `i-0c65cc61a575bdfa7` | LIVE 98 PC | ndead 13625 still_active logZ −1420.1 ± 0.22 |
| SH0ES LCDM PC | `i-0941e936fd100c309` | LIVE 98 PC | ndead 15309 still_active logZ −1416.4 ± 0.23 |
| TRGB dyad PC | `i-06847ebdfd55bac11` | LIVE 98 PC | ndead 12598 still_active logZ −1392.4 ± 0.21 |
| TRGB LCDM PC | `i-0d1915a2ac2d5c5af` | LIVE 98 PC | ndead 14806 still_active logZ −1377.9 ± 0.22 |
| noH0 dyad PC | `i-0ada8e723c9564ee8` | LIVE 98 PC | ndead 6552 still_active logZ −1527.3 ± 0.24 |
| noH0 LCDM PC | `i-088a37359608bcabb` | LIVE 98 PC | ndead 8167 still_active logZ −1432.1 ± 0.20 |

No PolyChord production `.stats` was finished (`Still Active` on every live prod tree). Isolation/toy PC stats were ignored.

Do not mix SH0ES vs TRGB logZ. Do not compute ΔlnZ until the matching dyad summary exists.
