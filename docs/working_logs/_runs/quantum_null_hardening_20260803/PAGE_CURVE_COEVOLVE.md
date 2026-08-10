# PAGE co-evolution instrument result

**Milestone:** `R_PAGE_coevolve_T8_era`  
**page_curve_claimed:** **false**  
**Standing CANDIDATE:** **no** (claim-decoupling: scorecard is a separate step)

## Design
Co-evolve S_rad with advancing evaporation coordinate u = max envelope of pure
energy fraction v. Beam-splitter dump is scheduled to keep u climbing through
the entropy-rise window (batch9 denial mode = S multivalued at stalled u).

## Machine numbers (from this run only — not a CANDIDATE filing)
| quantity | value |
|---|---:|
| pre-T8 self-score (T1–T6) | False |
| CANDIDATE_TURN (this script) | **false** (never self-claims) |
| u* at S peak | 0.4048 |
| u_late | 0.8694 |
| S_peak | 0.012327 |
| S_late | 0.001077 |
| drop | 0.011250 |
| N2 thermal no-turn | True |
| N4 unitarity | True |
| frac S-rise while u advances | 0.04530307968349011 |
| longest stall steps with S rise | 66 |

## Next (claim-decoupling)
```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v38.json
```
Binding gate is **T1–T8** + coevolution gates. Do not file CANDIDATE until scorecard exists.

## Explicit non-claims
- Not a Page curve claim; Q6 remains OPEN  
- Not medium-licensed r or pair H  
- Instrument class only  
- Write-once versioned artifact (Claude R-C.6) — do not overwrite  

Artifact: `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v38.json`  
Script sha256: `72946ddd4d98d1c8…`  

*NO FABRICATIONS.*
