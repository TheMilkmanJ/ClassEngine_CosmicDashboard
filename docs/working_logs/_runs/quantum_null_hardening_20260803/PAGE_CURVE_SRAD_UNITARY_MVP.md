# Page S_rad(v) unitary MVP — instrument only

**Script:** `scripts/quantum_page_srad_unitary_mvp.py`  
**JSON:** `page_curve/srad_unitary_mvp.json`  
**page_curve_claimed:** **false**  
**Resource:** single-thread; no PolyChord; niced vs cobaya MCMCs.

## Numbers

| quantity | value |
|---|---:|
| N_c, N_r | 3, 6 |
| S_rad peak | 0.505012 |
| S_rad late | 0.276273 |
| late_drop | 0.228739 |
| v at peak | 0.1786 |
| max\|S_total\| | 7.080e-14 |
| unitarity (S_total~0) | PASS |
| page-like shape (curiosity) | YES |

## Grade

**Instrument PASS** if the run completes and unitarity holds.  
**Page curve / Q6:** still **OPEN** — continuum modes + red required before any claim.

## Forbidden readings

- Do not book page-like shape as PRTOE Page turn  
- Do not replace continuum Hawking with this toy TMS coupling  

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_srad_unitary_mvp.py
```
