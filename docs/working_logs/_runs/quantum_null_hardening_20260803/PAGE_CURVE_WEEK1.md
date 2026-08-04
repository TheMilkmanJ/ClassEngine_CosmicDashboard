# Page-curve Week 1 — sonic horizon + thermal bookkeeping (2026-08-03)

**Status:** WEEK1 ONLY — honest instrument progress.  
**Page curve:** **NOT computed.**  
**\(S_{\mathrm{rad}}(v)\):** **NOT claimed.**  
**Script:** [`scripts/quantum_page_sonic_horizon_week1.py`](../../../../scripts/quantum_page_sonic_horizon_week1.py)  
**JSON artifact:** [`page_curve/week1_sonic_horizon.json`](page_curve/week1_sonic_horizon.json)  
**Plan:** [`PAGE_CURVE_IMPLEMENTATION_PLAN.md`](PAGE_CURVE_IMPLEMENTATION_PLAN.md)  
**Scaffold (toy only):** [`PAGE_CURVE_SCAFFOLD.md`](PAGE_CURVE_SCAFFOLD.md)

---

## 1. What was done

Milestone A first half: place a **prescribed stationary 1D acoustic** black-hole profile, locate the sonic horizon, measure surface gravity \(\kappa\), report Unruh/analog-Hawking temperature \(T_H=\kappa/(2\pi)\), and tabulate the ideal Bose occupation \(n_B(\omega)=1/(e^{\omega/T_H}-1)\) on the plan mid-band \(\omega\in[0.05,2]\,\kappa\).

This is **thermal bookkeeping**, not a Page curve and not a dynamical \(S_{\mathrm{rad}}(v)\).

### Profile (healing units)

- Domain \(x\in[-40,40]\,\xi\), \(n=1\Rightarrow c_s=1\).
- Flow: \(v(x)=\tfrac12(v_{\mathrm{in}}+v_{\mathrm{out}})+\tfrac12(v_{\mathrm{out}}-v_{\mathrm{in}})\tanh(x/\ell)\) with \(v_{\mathrm{in}}=-1.5\), \(v_{\mathrm{out}}=-0.5\), \(\ell=4\,\xi\).
- Interior (\(x<0\)): supersonic \(|v|>c_s\); exterior: subsonic. Horizon at \(x_h=0\), \(v_h=-1\).

Surface gravity (1D acoustic):
\[
\kappa=\frac12\partial_x\bigl(c_s^2-v^2\bigr)\Big|_{x_h}
\quad\Rightarrow\quad
T_H=\frac{\kappa}{2\pi}.
\]

Analytic for this tanh: \(\mathrm{d}v/\mathrm{d}x|_{x_h}=\mathrm{amp}/\ell=0.125\), \(\kappa=c_s\cdot(\mathrm{d}v/\mathrm{d}x)=0.125\), \(T_H=\kappa/(2\pi)\approx 0.019894\).

---

## 2. Results (computed)

### 2.1 Analytic target

| quantity | value |
|---|---:|
| \(x_h\) | \(0\) |
| \(v_h\), \(c_s\) | \(-1\), \(1\) |
| \(\kappa\) | \(0.125000\) \(t_{\mathrm{heal}}^{-1}\) |
| \(T_H=\kappa/2\pi\) | \(0.019894\) |

### 2.2 Grid convergence of \(\kappa\) (finite difference)

| \(N\) | \(\mathrm{d}x\) | \(\kappa\) | \(T_H\) | \(\lvert\kappa-\kappa_{\mathrm{an}}\rvert/\kappa_{\mathrm{an}}\) |
|---:|---:|---:|---:|---:|
| 512 | 0.15625 | 0.124936 | 0.019884 | 0.0508% |
| 1024 | 0.07812 | 0.124984 | 0.019892 | 0.0127% |
| 2048 | 0.03906 | 0.124996 | 0.019894 | 0.0032% |
| 4096 | 0.01953 | 0.124999 | 0.019894 | 0.0008% |

Refinement \(|\kappa_N-\kappa_{N/2}|/\kappa_N \approx 0.0024\%\) — **PASS** (plan exit: \(<5\%\)).

### 2.3 Null control

Subsonic profile \(v\equiv -0.3\), \(\max|v|/c_s=0.3\): **no horizon** — PASS.

### 2.4 Mode frequency vs thermal occupation (reference Bose)

Ideal \(n_B(\omega)\) at \(T_H=\kappa/2\pi\) (not a Bogoliubov scattering solve):

| \(\omega/\kappa\) | \(\omega\) | \(\omega/T_H\) | \(n_B(\omega)\) |
|---:|---:|---:|---:|
| 0.05 | 0.006250 | 0.3142 | \(2.709\times 10^{0}\) |
| 0.10 | 0.012500 | 0.6283 | \(1.144\times 10^{0}\) |
| 0.25 | 0.031250 | 1.5708 | \(2.624\times 10^{-1}\) |
| 0.50 | 0.062500 | 3.1416 | \(4.517\times 10^{-2}\) |
| 1.00 | 0.125000 | 6.2832 | \(1.871\times 10^{-3}\) |
| 1.50 | 0.187500 | 9.4248 | \(8.071\times 10^{-5}\) |
| 2.00 | 0.250000 | 12.5664 | \(3.487\times 10^{-6}\) |

---

## 3. Acceptance vs plan Milestone A

| test | Week 1 status |
|---|---|
| Horizon \(\lvert v(x_h)\rvert=c_s(x_h)\), \(\kappa>0\) | **PASS** |
| \(T_H=\kappa/(2\pi)\) with FD error bar | **PASS** (\(\ll 5\%\)) |
| Spectrum \(\langle n_\omega\rangle\) from mode solve; \(T_{\mathrm{fit}}/T_H\) | **NOT DONE** — table is pure thermal *reference*, not extracted \(\beta_\omega\) |
| Dispersion fence \(k\xi\gtrsim 1\) | deferred (needs mode basis) |
| Null \(\kappa\to 0\) / no horizon \(\Rightarrow\) no flux | horizon null **PASS**; flux null needs Week 2 flux script |

**Honest grade:** instrument **partial PASS** — horizon + \(\kappa\) + \(T_H\) bookkeeping solid; full Milestone A (thermal flux from modes / \(T_{\mathrm{fit}}\)) still open.

---

## 4. Explicit non-claims

1. No \(S_{\mathrm{rad}}(v)\) array or plot from dynamics.  
2. No Page time, no Page turn.  
3. No greybody \(\Gamma(\omega)\); \(n_B\) is ideal Bose at \(T_H\).  
4. No finite-core Hilbert-space evolution.  
5. No self-consistent GP mass loss.  
6. Toy ansatz \(4v(1-v)\) was **not** used (scaffold remains illustration only).

---

## 5. What Week 2+ still needs

| Week | Still owed |
|---|---|
| **2** | Mode problem on fixed background: scattering / Bogoliubov \(\beta_\omega\); energy flux \(F\); compare \(\langle n_\omega\rangle\) to \(n_B\) with optional greybody; finite-core skeleton (\(N_c\) oscillators) + early \(S_{\mathrm{rad}}(t)\) rise only |
| **3** | Evaporation schedule \(v=E_{\mathrm{rad}}/E_{\mathrm{tot}}\); first honest \(S_{\mathrm{rad}}(v)\) from dynamics; Page-turn detector (may FAIL) |
| **4** | Null suite (infinite bath vs finite core); dispersion/healing fence; grade DYNAMICS-PASS / FAIL / INCONCLUSIVE |

Immediate next script targets (from plan naming): mode/flux layer → `page_curve_thermal_flux.py` (or equivalent), then `page_curve_core_hilbert.py`.

---

## 6. Reproduce

```bash
python3 scripts/quantum_page_sonic_horizon_week1.py
# scaffold remains non-result illustration:
python3 scripts/quantum_page_curve_scaffold.py
```

---

*Week-1 grade: sonic-horizon instrument + Unruh \(T_H\) bookkeeping PASS. Curve dynamics still OPEN. No fake Page turn.*
