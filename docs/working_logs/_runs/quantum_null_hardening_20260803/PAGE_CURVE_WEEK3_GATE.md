# Page curve week3 — gate status

**Status:** A4 TC parked (machine done). Week1–2 instruments **PASS**.  
**S_rad(v) / Page turn:** still **OPEN**.  
**May start:** design + finite-core skeleton only — **no fake Page close**.

## Prerequisites
| Item | Status |
|---|---|
| A4 four-branch on disk | **DONE** |
| Week1 sonic κ/T_H | **PASS** |
| Week2 Bogoliubov \|β\|² | **PASS** |
| Owner/red order week3 | soft-unblocked by plan (after A4 parked); hard order optional |

## Week3 goal (from IMPLEMENTATION_PLAN)
Evaporation schedule and first full \(S_{\mathrm{rad}}(v)\) **attempt** (Milestone C).  
First honest success may still fail to show a Page turn.

## Forbidden
- Drawing Page curve from A/4G alone  
- Shipping toy 4v(1−v) as PRTOE result  
- Reading week1–2 PASS as S_rad close  

## Next blue step (when starting)
1. Finite-core Hilbert / covariance skeleton (week2 residual)  
2. Couple exterior modes at κ from week1  
3. Track E_rad → v; compute S_rad(v) only if state is honest  
4. Report PASS/FAIL on instrument — never invent turn

Artifacts to create when started: `PAGE_CURVE_WEEK3.md` + script under `scripts/quantum_page_*_week3.py`

## Skeleton landed (15:20)

- Script: `scripts/quantum_page_core_skeleton_week3.py`
- Report: `PAGE_CURVE_WEEK3.md`
- JSON: `page_curve/week3_core_skeleton.json`
- **Page curve still NOT claimed**
