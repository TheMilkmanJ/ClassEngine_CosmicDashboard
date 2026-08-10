# Medium r / pair H inventory (R-MEDR + R-PAIRH P1)

**Script:** `scripts/quantum_medium_r_inventory.py`  
**files_scanned:** 490

## Verdict

| question | answer |
|---|---|
| Textbook pair H harness | **YES** (`quantum_pair_hamiltonian_tmsv.py`) |
| Medium-licensed pair H on disk | **NO** |
| Medium r formula on disk | **NO** |
| EN-D2/D3 | **MISSING_INPUT** |

## Hit counts

| pattern | n |
|---|---:|
| pair_Hamiltonian_phrase | 12 |
| latex_pair_H | 0 |
| tmsv_phrase | 8 |
| squeeze_param | 2 |
| lambda_over_omega | 1 |
| bogoliubov_coherence | 4 |
| pairing_gap | 12 |
| cooper | 2 |

## Interpretation

Phrase hits for Cooper/Bogoliubov/gap are **expected** in a superfluid corpus; they do **not**
by themselves pin \(r\) or \((\omega,\lambda)\). Only an explicit map to numbers pays R-MEDR.

## Recompute

```bash
OMP_NUM_THREADS=1 python3 scripts/quantum_medium_r_inventory.py
```
