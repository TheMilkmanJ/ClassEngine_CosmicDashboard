# Page-curve Week 2 — Bogoliubov / greybody on sonic horizon (2026-08-03)

**Status:** WEEK2 ONLY — honest instrument progress after week1 PASS.  
**Page curve:** **NOT computed.**  
**\(S_{\mathrm{rad}}(v)\):** **STILL NOT claimed.**  
**Script:** [`scripts/quantum_page_bogoliubov_week2.py`](../../../../scripts/quantum_page_bogoliubov_week2.py)  
**JSON artifact:** [`page_curve/week2_bogoliubov.json`](page_curve/week2_bogoliubov.json)  
**Week1:** [`PAGE_CURVE_WEEK1.md`](PAGE_CURVE_WEEK1.md) · `scripts/quantum_page_sonic_horizon_week1.py`  
**Plan:** [`PAGE_CURVE_IMPLEMENTATION_PLAN.md`](PAGE_CURVE_IMPLEMENTATION_PLAN.md)

---

## 1. What was done

Level A + light Level B on the **same prescribed stationary 1D tanh acoustic metric** as week1:

1. **Near-horizon Bogoliubov connection** — identify
   \[
   |\beta_\omega|^2 = \frac{1}{e^{2\pi\omega/\kappa}-1} = n_B(\omega;T_H),\qquad T_H=\kappa/(2\pi)
   \]
   as the mode-mixing result (not mere thermal bookkeeping).
2. **Numerical exterior mode matching** for mid-band \(\omega/\kappa\in[0.05,2]\):
   - Mode ODE on the Painlevé–Gullstrand acoustic metric (\(c_s=1\)):
     \[
     (1-v^2)\psi'' + 2(i\omega v - v v')\psi' + (\omega^2 + i\omega v')\psi = 0
     \]
   - Purely ingoing near-horizon IC \(\psi\sim x^{-i\omega/\kappa}\); integrate to \(x_{\mathrm{out}}\); Doppler decompose into in/out waves; flux-weighted greybody \(\Gamma(\omega)=1-|R|^2_{\mathrm{flux}}\).
3. **Occupation** \(n_{\mathrm{mode}}(\omega)=\Gamma(\omega)\,n_B(\omega)\); **\(T_{\mathrm{fit}}\)** from \(\ln(1+1/n)\approx\omega/T\); mid-band **energy-flux proxy**.
4. Nulls: \(\omega/\kappa\) universality of \(|\beta|^2\); subsonic (no horizon) \(\Rightarrow\) no Hawking \(\beta\).

**Still not done (correct fence):** finite-core Hilbert space, early \(S_{\mathrm{rad}}(t)\) rise, evaporation schedule, Page turn.

---

## 2. Results (computed)

### 2.1 Reused week1 metric

| quantity | value |
|---|---:|
| \(x_h\) | \(0\) |
| \(\kappa\) | \(0.125000\) |
| \(T_H=\kappa/2\pi\) | \(0.019894\) |

### 2.2 Near-horizon \(|\beta_\omega|^2 = n_B(\omega;T_H)\)

| \(\omega/\kappa\) | \(\omega\) | \(|\beta|^2=n_B\) |
|---:|---:|---:|
| 0.05 | 0.006250 | \(2.709\times 10^{0}\) |
| 0.10 | 0.012500 | \(1.144\times 10^{0}\) |
| 0.25 | 0.031250 | \(2.624\times 10^{-1}\) |
| 0.50 | 0.062500 | \(4.517\times 10^{-2}\) |
| 0.75 | 0.093750 | \(9.065\times 10^{-3}\) |
| 1.00 | 0.125000 | \(1.871\times 10^{-3}\) |
| 1.25 | 0.156250 | \(3.884\times 10^{-4}\) |
| 1.50 | 0.187500 | \(8.071\times 10^{-5}\) |
| 2.00 | 0.250000 | \(3.487\times 10^{-6}\) |

Same numbers as week1 thermal table; **meaning upgraded**: week1 = bookkeeping reference; week2 = near-horizon Bogoliubov occupation from mode connection.

### 2.3 Exterior mode matching (greybody)

All 9 mid-band bins: mode match **ok**.

| \(\omega/\kappa\) | \(\Gamma\) | \(\lvert R\rvert^2_{\mathrm{flux}}\) | \(n_{\mathrm{mode}}=\Gamma n_B\) |
|---:|---:|---:|---:|
| 0.05–2.00 | \(\approx 0.7516\) (flat) | \(\approx 0.2484\) | \(\Gamma\times n_B\) |

- Mean \(\Gamma \approx 0.752\).
- \(\Gamma(\omega)\) is nearly **frequency-independent** for this constant-density tanh flow under the present IC/matching scheme. Physical mild barrier vs residual near-horizon IC systematics at the \(\sim 25\%\) level is **not settled** here; reported as computed instrument output, not a precision greybody claim.
- Sensitivity check: \(\Gamma\) stable under \(x_\varepsilon\in[0.02,0.2]\), \(x_{\mathrm{out}}\in[20,40]\) (varies only \(\sim 0.75\to 0.76\)).

### 2.4 Thermal comparison

| quantity | value |
|---|---:|
| \(T_H\) (from \(\kappa\)) | \(0.019894\) |
| \(T_{\mathrm{fit}}\) from \(n_{\mathrm{mode}}=\Gamma n_B\) | \(0.019241\) |
| \(T_{\mathrm{fit}}/T_H\) | **0.967** |
| Plan band \([0.7,1.3]\) | **PASS** |
| \(T_{\mathrm{fit}}\) pure \(n_B\) control | \(0.019894\) (ratio \(1.000\)) |

### 2.5 Energy flux proxy (mid-band only)

| proxy | value |
|---|---:|
| \(F[\Gamma n_B]\) mid-band | \(\approx 5.05\times 10^{-5}\) |
| \(F[n_B]\) mid-band | \(\approx 8.93\times 10^{-5}\) |

**Not** a full \(\int_0^\infty\) Stefan check; quadrature over plan mid-band only.

### 2.6 Nulls

| null | result |
|---|---|
| \(\lvert\beta\rvert^2\) depends only on \(\omega/\kappa\) | PASS |
| Subsonic \(v\equiv -0.3\): no horizon / no Hawking \(\beta\) | PASS |

---

## 3. Acceptance vs plan

| test | Week 2 status |
|---|---|
| Horizon + \(\kappa\), \(T_H\) (week1) | **PASS** (reused) |
| \(\langle n_\omega\rangle\) from mode/Bogoliubov layer | **PASS** — \(\lvert\beta\rvert^2\) near-horizon + \(\Gamma\) from exterior ODE |
| \(T_{\mathrm{fit}}/T_H\in[0.7,1.3]\) | **PASS** (\(0.967\)) |
| Greybody \(\Gamma(\omega)\) | **Computed** (flat \(\sim 0.75\); not precision-claimed) |
| Energy flux instrument | **Partial** — mid-band proxy only |
| Finite-core + early \(S_{\mathrm{rad}}(t)\) | **NOT DONE** (plan Week 2 days 2–3 still owed) |
| \(S_{\mathrm{rad}}(v)\) / Page turn | **NOT computed** (correct) |

**Honest grade:** Milestone A **thermal-modes instrument PASS** (horizon + Bogoliubov \(\lvert\beta\rvert^2\) + greybody match + \(T_{\mathrm{fit}}\)). Full plan Week-2 (finite core, unitary early entropy) still open. Curve dynamics remain **OPEN**.

---

## 4. Explicit non-claims

1. No \(S_{\mathrm{rad}}(v)\) from dynamics.  
2. No Page time, no Page turn.  
3. No finite-core density-matrix evolution / entanglement partner proof.  
4. No self-consistent GP mass loss.  
5. No claim that \(\Gamma\approx 0.75\) is the final continuum greybody of the analog system (possible IC/barrier systematics).  
6. Toy \(4v(1-v)\) **not** used.

---

## 5. What Week 3+ still needs

| Week | Still owed |
|---|---|
| **2 residual** | Finite-core \(N_c\) oscillators + pair-creation Hamiltonian; early \(S_{\mathrm{rad}}(t)\) rise; unitarity null on total pure state |
| **3** | Evaporation schedule \(v=E_{\mathrm{rad}}/E_{\mathrm{tot}}\); first honest \(S_{\mathrm{rad}}(v)\); Page-turn detector (may FAIL) |
| **4** | Null suite; dispersive \(k\xi\sim 1\) fence; grade DYNAMICS-PASS / FAIL / INCONCLUSIVE |

---

## 6. Reproduce

```bash
python3 scripts/quantum_page_sonic_horizon_week1.py
python3 scripts/quantum_page_bogoliubov_week2.py
```

---

*Week-2 grade: Bogoliubov / greybody instrument PASS on week1 sonic horizon. \(T_{\mathrm{fit}}/T_H\approx 0.97\). Page curve still OPEN. No fake Page turn. STILL NOT \(S_{\mathrm{rad}}(v)\).*
