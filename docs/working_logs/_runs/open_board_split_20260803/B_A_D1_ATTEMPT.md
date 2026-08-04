# Page construction D1 attempt — two-phase BS→TMS (2026-08-04)

**NO FABRICATIONS.** Write-once artifacts. No CANDIDATE. claimed false.

---

## What was tried

| ver | idea | early T8 ratio | u_late | result |
|---|---|---:|---:|---|
| v40 | pure-zero TMS until u≥0.12 | n/a | 0.29 | vacuum dump dead |
| v41–42 | soft seed TMS (6–8%) then full | ~0 / flat | 0.86–0.88 | early T8 better; T2 fail |
| v43–44 | stronger dump after soft phase | 0.04–0.07 | 0.87–0.89 | early T8 would pass; **T2 still short of 0.9** |

Artifacts: `page_curve/coevolve_v28`–`v33` class (D1 family).

## Learning

1. Pure BS from vacuum does not seed enough occupation to dump.  
2. Soft two-phase **does** flatten early \(S(u)\) (early ratio ≪ 0.10).  
3. Recovering unit-weight \(u\ge 0.9\) under soft early TMS is harder than under v13 continuous TMS — dump boosts reintroduce late multivalued \(S\) before freeze.

## Standing champion

**`coevolve_v13`** still best joint near-miss (T8 early 0.113 only). Script header restored to **v23_champion_locked**.

## Next (if continue Page)

- D2: \(w_c\equiv 1\) in free \(A\) as well as Page \(v\)  
- Or accept instrument near-miss and prioritize bbnfix booking when machine gates fire  

*NO FABRICATIONS.*
