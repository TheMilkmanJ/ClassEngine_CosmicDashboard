# Gold PolyChord peel — 2026-08-10 ~05:30Z

## SH0ES ΛCDM (`i-0e353f38544397a6d`)

**Process:** **DEAD** after Fortran runtime error (known PolyChord bug).

```
At line 861 of file read_write.F90
Fortran runtime error: Missing comma between descriptors
("log(Z_",I1,")",A5,"= ",E24.15E3," +/- ",E24.15E3" (Still Active)")
```

**Peelable intermediate (NOT final, NOT bookable as nested ΔlnZ):**

| quantity | value | note |
|---|---:|---|
| Intermediate `log(Z)` | **−3798.69 ± 0.81** | written to `.stats` mid-run; “Still Active” path crashed |
| dead points | ~4595 | `_dead.txt` present |
| nlive | 500 | |
| nDims | 12 | |

**Action:** patch `read_write.F90`, rebuild pypolychord, **resume** from `.resume` (dead points should resume).

## SH0ES dyad (`i-04ead482af737e7bf`)

**Log:** live points generated, `started sampling`.  
**Files at last check:** resume + phys_live + prior (no dead yet at 04:39Z stamp).  
**Risk:** same stats-write bug when first intermediate stats flush.

## Fence

- Do **not** quote intermediate log(Z) as gold evidence.
- Do **not** form ΔlnZ until **both** legs finish cleanly after the Fortran fix.
- DESI MCMC dual-gate booking is a **separate** Stage A instrument (done 20260810_053127).

*NO FABRICATIONS.*
