# Debt report — RM two-point / coherence formula (Kibble geometry)

**Run id:** `debt_rm_formula_20260803`  
**Date:** 2026-08-03  
**Worker:** blue-team science (desk formula; no MCMC)  
**Parent debt:** [`debt_magnetism_20260803`](../debt_magnetism_20260803/REPORT.md) §3–§4.B  
**Primary sources:**  
- [`docs/PRTOE_cosmic_magnetism.md`](../../../PRTOE_cosmic_magnetism.md) §3a, §4, §6  
- [`docs/PRTOE_cmb_anomalies.md`](../../../PRTOE_cmb_anomalies.md) (ξ_K/χ_* = 1.07°)  
- [`docs/PRTOE_READERS_GUIDE.md`](../../../PRTOE_READERS_GUIDE.md) (ξ_K, χ_*)  
- Script: [`scripts/rm_coherence_kibble.py`](../../../../scripts/rm_coherence_kibble.py)

---

## 0. Question answered

**Can a computable Faraday RM two-point / coherence formula be written from recorded corpus geometry (ξ_K = 256 Mpc) without inventing new free parameters?**

**Answer: YES for the geometric scale and unit-normalized angular shape; amplitude is an upper bound set by B_seed with external n_e labeled as assumed — not a new PRTOE knob.**

**Does this close the void-floor gap?** **NO.** Explicit non-claim below.

---

## 1. Recorded inputs (no new free parameters)

| symbol | value | role | corpus home |
|---|---|---|---|
| ξ_K | **256 Mpc** comoving | Kibble domain / vortex-network coherence length | READERS_GUIDE; cosmic_magnetism §1; cmb_anomalies |
| χ_* | **13.76 Gpc** = 13760 Mpc | comoving distance to last scattering | READERS_GUIDE; cmb_anomalies; audit_math_pass |
| B_seed | **≈ 5×10⁻¹⁸ G** | smooth Harrison seed; **inter-line CAP** under return flux | cosmic_magnetism §2–§3a |
| B_blazar | **≳ 10⁻¹⁶ G** | external TeV-halo floor (falsifier), **not** a model output | NeronovVovk2010; §0, §3a |

Already audited angular scale at last scattering (not re-derived here, only reused):

\[
\theta_\xi(\chi_*) = \frac{\xi_K}{\chi_*} = \frac{256}{13760}\,\mathrm{rad} = \mathbf{1.07°}
\]

(`scripts/audit_math_pass.py`: `XI_K, CHI_STAR = 256.0, 13760.0` → 1.07°).

**No new magnetism free parameters** are introduced. The only *shape* choice is a unit-normalized Gaussian radial correlation (standard one-scale template); its **length is fixed to ξ_K**. Replacing the Gaussian by a top-hat or exponential of the **same** ξ_K changes O(1) shape factors, not the characteristic multipole.

---

## 2. Derived vs assumed (explicit)

### Derived (from corpus geometry + standard Faraday definition)

1. **RM line-of-sight definition** (standard plasma electrodynamics; not a model knob):

   \[
   \mathrm{RM}(\hat n)
   = K \int_0^{\chi_s} n_e(\chi)\, B_\parallel(\chi\,\hat n,\chi)\,d\chi
   \]

   with \(K = e^3/(2\pi m_e^2 c^4)\) (cgs). Numerical convenience form:  
   \(\mathrm{RM}/[\mathrm{rad\,m^{-2}}] \approx 0.81 \int (n_e/\mathrm{cm^{-3}})(B_\parallel/\mu\mathrm{G})(dl/\mathrm{pc})\).

2. **Two-point function** for any structured B:

   \[
   \boxed{
   \langle\mathrm{RM}(\hat n_1)\,\mathrm{RM}(\hat n_2)\rangle
   = K^2 \int_0^{\chi_s}\!d\chi_1\int_0^{\chi_s}\!d\chi_2\;
   n_e(\chi_1)n_e(\chi_2)\;
   \langle B_\parallel(\chi_1\hat n_1)\,B_\parallel(\chi_2\hat n_2)\rangle
   }
   \]

3. **Kibble geometric transfer** (the missing multipole map named in cosmic_magnetism §3a):

   \[
   \boxed{
   \theta_\xi(\chi) = \frac{\xi_K}{\chi},\qquad
   \ell_{\mathrm{geo}}(\chi) = \frac{\chi}{\xi_K},\qquad
   \ell_\pi(\chi) = \frac{\pi\,\chi}{\xi_K}
   }
   \]

   - \(\theta_\xi\): angular size of one Kibble cell at comoving distance χ.  
   - \(\ell_{\mathrm{geo}}\): flat-sky \(k_\perp\chi\) with \(k_\perp = 1/\xi_K\).  
   - \(\ell_\pi\): conventional “feature multipole” \(\approx \pi/\theta_\xi\).

4. **Unit-normalized thin-shell angular correlation** when  
   \(\langle B_i(\mathbf x)B_j(\mathbf x+\mathbf r)\rangle
   \propto \exp\!\big(-r^2/(2\xi_K^2)\big)\) (isotropic; scale = ξ_K):

   \[
   \boxed{
   \frac{w(\theta)}{w(0)}
   = \exp\!\Bigl(-\frac{\theta^2}{2\,\theta_\xi(\chi)^2}\Bigr)
   = \exp\!\Bigl(-\tfrac12\bigl(\theta/\theta_\xi\bigr)^2\Bigr)
   }
   \]

   for a thin equal-χ shell (Limber / flat-sky). Full LOS integral is a χ-weighted
   superposition of such shells — **still only one geometric scale ξ_K**.

5. **Limber-style multipole sketch** (scale identification, not a survey pipeline):

   \[
   C_\ell^{\mathrm{RM}}
   \;\sim\;
   K^2 \int\frac{d\chi}{\chi^2}\,
   n_e(\chi)^2\,
   P_{B_\parallel}\!\Bigl(k=\frac{\ell}{\chi};\chi\Bigr)
   \]

   with \(P_{B_\parallel}(k)\) peaked / cut at \(k\sim 1/\xi_K\).  
   ⇒ **feature / break in \(C_\ell^{\mathrm{RM}}\) near \(\ell \sim \ell_{\mathrm{geo}}\)–\(\ell_\pi\)** for the effective χ of the RM-producing plasma.

### Assumed (named; not illegal free params of the magnetism claim)

| assumption | why allowed | what it is *not* |
|---|---|---|
| Gaussian (or any one-scale) radial shape of ξ_B | encodes “coherence length = ξ_K”; O(1) shape only | not a fit parameter to RM data |
| Thin-shell / Limber projection for the unit shape | standard small-angle transfer | not a new seed mechanism |
| Source-plane χ (or χ_eff of n_e-weighted plasma) | observer choice / external catalog depth | not a PRTOE free knob |
| External \(n_e(\chi)\) for **amplitude** | standard IGM/WHIM astrophysics | **not derived here**; leaves σ_RM open |
| \(B_{\mathrm{rms}}\lesssim B_{\mathrm{seed}}\) | return-flux theorem already in corpus §3a | **does not** raise void B to blazar |

### Not assumed / not claimed

- No B_void ≳ 10⁻¹⁶ G.  
- No filament boost ×3400 applied to inter-line / void RM (theorem-blocked).  
- No new seed, no MCMC, no survey fit.

---

## 3. Numbers outsiders can check (printed by script)

Run:

```bash
nice -n 19 python3 scripts/rm_coherence_kibble.py
```

### 3a. Last-scattering reference (recorded χ_*)

| quantity | value |
|---|---|
| θ_ξ(χ_*) | **1.066°** ≈ **1.07°** (matches cmb_anomalies / audit_math_pass) |
| ℓ_geo(χ_*) | **53.75** |
| ℓ_π(χ_*) | **168.9** |
| sky cells ~ 4π/θ_ξ² | **~3.6×10⁴** (fine network tiling) |

### 3b. Characteristic scales at fixed source-plane χ (comoving)

| χ [Mpc] | θ_ξ [deg] | θ_ξ [arcmin] | ℓ_geo | ℓ_π |
|---:|---:|---:|---:|---:|
| 500 | 29.3 | 1760 | 1.95 | 6.1 |
| 1000 | 14.7 | 880 | 3.91 | 12.3 |
| 2000 | 7.33 | 440 | 7.81 | 24.5 |
| 3000 | 4.89 | 293 | 11.7 | 36.8 |
| 5000 | 2.93 | 176 | 19.5 | 61.4 |
| 13760 (= χ_*) | 1.07 | 64.0 | 53.8 | 168.9 |

**Extragalactic RM depth class (χ ~ 1–3 Gpc):**  
θ_ξ ~ **5–15°**, ℓ_π ~ **12–37**.  
That is a **large-angle** RM correlation feature — the quantitative content of the qualitative “~100 Mpc-class, not micro” claim in cosmic_magnetism §4.

### 3c. Unit-normalized shell two-point

| θ/θ_ξ | w(θ)/w(0) |
|---:|---:|
| 0.0 | 1.000 |
| 0.5 | 0.882 |
| 1.0 | 0.607 |
| 1.5 | 0.325 |
| 2.0 | 0.135 |
| 3.0 | 0.011 |

**Checkable statement:** angular RM coherence half-power is near \(\theta\sim\theta_\xi(\chi_{\mathrm{eff}})\); power falls by e⁻½ at one Kibble angle and is essentially gone by ~3 θ_ξ.

### 3d. Amplitude (honest bound, not a free fit)

With \(B_{\mathrm{rms}}\lesssim B_{\mathrm{seed}}\) and a coherence patch length ~ξ_K along the LOS, an order-of-magnitude CAP is

\[
|\mathrm{RM}|
\;\lesssim\;
K\, n_e\, B_{\mathrm{seed}}\, L_{\mathrm{patch}}
\]

per coherent patch, with N_indep ~ χ_s/ξ_K patches adding in rms as √N if uncorrelated beyond ξ_K.  
**n_e is external.** Without a stated IGM n_e model, the corpus does **not** claim a numerical σ_RM. The **scale** prediction does not need n_e.

Using B_blazar instead of B_seed would illegally invent a void field the model does not have (§3a theorem). Amplitude must stay on the B_seed class for *model* predictions.

---

## 4. What this pays vs what stays open

| item | status after this pass |
|---|---|
| ⟨RM·RM⟩ expression | **WRITTEN** (LOS double integral + ξ_K-structured ⟨B B⟩) |
| ξ_K → angular / multipole transfer | **WRITTEN** (θ_ξ, ℓ_geo, ℓ_π) |
| Unit-normalized C_ℓ / w(θ) scale feature | **COMPUTABLE** (script) |
| Absolute C_ℓ amplitude / survey comparison | **OPEN** — needs external n_e, noise, galactic RM cleaning |
| Void floor vs blazar (×20 = 1.30 dex) | **STILL OPEN** — this formula does **not** touch it |
| Galactic Harrison seed ~5×10⁻¹⁸ G | unchanged, paid (P-028) |

This is exactly step **B** of debt_magnetism_20260803 §4: close the named RM formula debt **without** claiming void-floor closure.

---

## 5. Non-claims (do not promote)

1. **Does NOT close the void-floor gap.** Model inter-line B stays ≲ B_seed ≈ 5×10⁻¹⁸ G; blazar ≳ 10⁻¹⁶ G remains ×20 open (1.30 dex).  
2. **Does NOT** use ×3400 rms filament boost as a void / inter-line floor.  
3. **Does NOT** claim a measured σ_RM or a survey detection.  
4. **Does NOT** introduce free parameters (filling factor, dynamo gain, ad-hoc ξ_RM) to fit catalogs.  
5. **Does NOT** identify the cold spot with a Kibble cell (already retired: 1.07° network ≠ 5–10° spot).  
6. **Does NOT** equate RM coherence multipoles with CMB acoustic peaks; different observables, shared only the geometric transfer language.

---

## 6. If free parameters had been required

Had the **scale** needed an unrecorded length (e.g. an independent “RM coherence ξ_RM” not equal to ξ_K, or a free spectral index tuned to surveys), the correct action under the task rules would have been: **stop and declare the formula non-writable without illegal free params.**

That did **not** happen: the distinctive claim in the corpus is precisely that the seed’s coherence is the **Kibble** scale ξ_K = 256 Mpc. Transferring that single recorded length into θ and ℓ is parameter-free. Amplitude remains n_e-external and B_seed-capped.

---

## 7. Ledger snapshot

| item | before | after this run |
|---|---|---|
| RM formula missing (cosmic_magnetism §3a, §6) | **Open — formula missing** | **Geometric two-point + multipole transfer written; amplitude external** |
| Void floor shortfall | open, 1.30 dex | **unchanged open** |
| Overall magnetism debt | OPEN-THEORY | still OPEN-THEORY (void referee + amplitude/survey still owed) |

---

## 8. Sources (paths)

- `/home/themilkmanj/prtoe_class/docs/PRTOE_cosmic_magnetism.md`  
- `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/debt_magnetism_20260803/REPORT.md`  
- `/home/themilkmanj/prtoe_class/docs/PRTOE_cmb_anomalies.md`  
- `/home/themilkmanj/prtoe_class/docs/PRTOE_READERS_GUIDE.md`  
- `/home/themilkmanj/prtoe_class/scripts/audit_math_pass.py` (ξ_K/χ_* check)  
- `/home/themilkmanj/prtoe_class/scripts/rm_coherence_kibble.py` (this run)

*End of report. No MCMC. Void floor not closed. RM geometric formula now on record.*


## Claude H2 cure — source-plane (2026-08-03)

**Do not quote ℓ_π ≈ 169 as “the” RM prediction.** That number is for χ = χ_* (last scattering).
RM catalogs use polarized extragalactic sources at χ ~ 1–5 Gpc:

| χ [Mpc] | θ_ξ [deg] | ℓ_π | Survey-relevant? |
|---:|---:|---:|---|
| 1000 | 14.7 | 12 | shallow EG |
| 2000 | 7.3 | 25 | typical EG |
| 3000 | 4.9 | 37 | deep EG |
| 5000 | 2.9 | 61 | high-z tail |
| 13760 | 1.07 | 169 | **CMB frame only** |

**Prediction for real RM catalogs:** large-angle coherence **ℓ ~ 25–60** (χ 2–5 Gpc), not ℓ~169.
Script `scripts/rm_coherence_kibble.py` already prints the multi-plane table. Void-floor non-claim unchanged.
