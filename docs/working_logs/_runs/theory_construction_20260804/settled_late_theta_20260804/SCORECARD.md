# Settled late-Θ scorecard (F5 deepen)

**Θ_lock (d=3)** = 11.70623765 = 1/√α  
**|H_kin|/H_door** = |Θ| · c_s/√3 = |Θ| · 0.08542454  
At lock: |H_kin|/H_door = 1.

**S1 pays only on S1_settled** = mean(last 20% of Θ after settle_extra), preferably with settled_std &lt; 0.2.

Form: FA3 0D only. dt=1e-3. Script sha256 `950d68ac…271fe380`.

---

## 1. Primary metrics

| metric | value | / Θ_lock | lock? | quotable? |
|---|---:|---:|---|---|
| **max quality S1_settled (se=40)** | **+0.043582** | **0.00372** | **NO** | YES (toy 0D) |
| max all-phys S1_settled (se=40) | +0.105600 | 0.00902 | NO | YES but quality FAIL (std=0.47) |
| max quality S1_settled (se=20) | +0.041952 | 0.00358 | NO | YES |
| stocked default se=40 settled | −0.003680 | — | NO | YES |
| stocked default se=0 tail10 | +0.061225 | 0.00523 | NO | YES (prior-comparable) |
| prior F5 best-late se=0 tail10 | **+2.8701** | 0.245 | NO | diagnostic only (F5) |
| prior F5 best-late se=0 tail20 | **−0.1364** | — | NO | F5 stamp |
| prior F5 best-late se=40 settled | −0.05822 | — | NO | quality FAIL |
| re-entry late_tail10 scan max | +2.8701 | 0.245 | NO | not S1_settled |
| Θ_lock | 11.706 | 1 | target | — |

---

## 2. Argmax coordinates (every headline)

| headline | (n0, Θ0, κ, γ) | settled | std | quality | tail10 | tail20 |
|---|---|---:|---:|---|---:|---:|
| **quality S1_settled se=40** | **(3, −1, 1.0, 0.05)** | **+0.04358** | 0.184 | OK | +0.717 | +0.643 |
| quality S1_settled se=20 | (20, −8, 2.0, 0.15) | +0.04195 | 0.157 | OK | −0.643 | −0.359 |
| all-phys S1_settled se=40 | (6, −2, 1.0, 0.02) | +0.1056 | 0.472 | FAIL | +1.056 | +1.176 |
| re-entry late_tail10 (F5) | (80, −8, 3.0, 0.02) | −0.0582 @se40 | 1.099 | FAIL | **+2.870** | **−0.136** |
| stocked default | (6, −2, 1.5, 0.15) | −0.00368 @se40 | 0.0315 | OK | +0.0612 | +0.281 |

Wall note: quality argmax is **not** the high-compression wall that produced +2.87; mild (3,−1) with moderate γ. Peak≠settled explicit.

---

## 3. |H_kin|/H_door ladder (d=3)

| Θ | \|H_kin\|/H_door | note |
|---:|---:|---|
| 1 | 0.0854 | unit reference |
| stocked se=40 settled −0.0037 | ~0.00031 | near FP |
| **quality max settled 0.0436** | **0.00372** | this package S1 |
| all-phys max settled 0.106 | 0.00902 | quality fail |
| prior late_tail10 2.87 | 0.245 | F5 window, not settled |
| Θ_lock 11.71 | **1.000** | required for door match |

Best legal **settled** leaves |H_kin| at **~0.37%** of H_door.

---

## 4. Ring-down ladder (stocked default)

| se | settled_mean | settled_std | quality |
|---:|---:|---:|---|
| 0 | +0.2813 | 0.254 | FAIL |
| 20 | +0.00203 | 0.114 | OK |
| 40 | −0.00368 | 0.0315 | OK |
| 80 | −0.00017 | 0.00248 | OK |
| 160 | +8.6e−7 | 1.6e−5 | OK |

## 5. Ring-down ladder (prior F5 best-late)

| se | settled_mean | settled_std | quality |
|---:|---:|---:|---|
| 0 | −0.1364 | 3.226 | FAIL |
| 20 | +0.1085 | 1.250 | FAIL |
| 40 | −0.0582 | 1.099 | FAIL |
| 80 | −0.0199 | 0.690 | FAIL |
| 160 | +0.0132 | 0.350 | FAIL |

All |settled| ≤ O(0.1); never lock. Slow γ=0.02 (rate 0.01) keeps std elevated at se=160.

---

## 6. Grade line

| question | answer |
|---|---|
| Max quality S1_settled | **+0.04358** |
| Lock reached (settled)? | **NO** |
| Ring-down → O(0.1) or below under stocked form? | **YES** (analytic FP + scan) |
| Production 3D COMPLETE? | **False** |
| S1 | **MISSING_INPUT** |
| Package grade | **OPEN-BLOCKED** |
| COMPLETE | **0** |
