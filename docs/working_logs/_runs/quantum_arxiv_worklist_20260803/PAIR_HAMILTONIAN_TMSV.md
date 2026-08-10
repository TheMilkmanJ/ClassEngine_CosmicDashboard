# Pair Hamiltonian → TMSV → CHSH harness

**Script:** `scripts/quantum_pair_hamiltonian_tmsv.py`  
**JSON:** `pair_hamiltonian_tmsv.json`

## Hamiltonian (textbook)

\[
H = \omega(a^\dagger a + b^\dagger b) + \lambda(ab + a^\dagger b^\dagger)
\]

Closed map \(|\lambda/\omega|<1 \Rightarrow r = \mathrm{artanh}(|\lambda/\omega|)\), then
literature \(B_{\max}(r)=2\sqrt{1+\tanh^2(2r)}\).

## Result

| check | status |
|---|---|
| All B ≤ Tsirelson in scan | PASS |
| Medium ω derived | **NO** |
| Medium λ derived | **NO** |
| Medium r derived | **NO** |
| EN-D2/D3 | still **MISSING_INPUT** |

## What would pay medium r

A corpus-licensed derivation of \((\omega,\lambda)\) or of \(r\) from medium numbers
(gap, density, stiffness, …) **without free dials**. That object is **not on disk**.

## Non-claims

Not CHSH discovery; not atomic QM; not Born.

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_pair_hamiltonian_tmsv.py
```
