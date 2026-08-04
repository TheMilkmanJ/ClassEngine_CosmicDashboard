# R-PAGE — pre-registered Page-turn acceptance protocol

**Status:** **BINDING** (Claude RED VERIFY AGREE unconditional 2026-08-03). REGISTERED before any claim-capable continuum run.  
**Rule:** write the fence **before** the run that could show a turn. Same discipline as T14.  
**Today:** all instruments keep `page_curve_claimed: false`. This protocol is what would
unlock a future claim — it does **not** unlock it now.

---

## 1. Object under test

\[
S_{\mathrm{rad}}(v),\quad v\in[0,1]=\frac{E_{\mathrm{rad}}}{E_{\mathrm{rad}}+E_{\mathrm{core}}}
\]
(or an equivalently pre-registered energy-fraction definition, frozen in the script header).

Units: healing (\(\xi\), \(t_{\mathrm{heal}}\)), \(\hbar=k_B=1\), unless a different convention is
frozen in the same header.

---

## 2. Required physical ingredients (all must be present)

| # | Ingredient | Min bar |
|---|---|---|
| P1 | Sonic / acoustic horizon with measured \(\kappa\), \(T_H=\kappa/2\pi\) | week1-class |
| P2 | Continuum exterior modes (mode ODE or equivalent), not only toy oscillators | week2-class or better |
| P3 | Finite unitary core (or proven unitary dilation) | Gaussian/exact DM |
| P4 | Evaporation schedule or self-consistent mass loss | prescribed OK if frozen |
| P5 | \(S_{\mathrm{rad}}(v)\) from reduced radiation state (von Neumann / Gaussian) | arrays on disk |

**Fails the protocol:** coefficient \(S=A/4G\) alone; toy \(4v(1-v)\) ansatz; page-like shape
on Gaussian-only hybrid **without** P2 continuum modes in the dynamics.

---

## 3. Null suite (must PASS before reading a turn)

| Null | Setup | Pass criterion |
|---|---|---|
| N1 | \(g=0\) / no pair creation / no emission | no spurious \(S_{\mathrm{rad}}\) growth (\(\max S_{\mathrm{rad}} < \varepsilon_S\)) |
| N2 | Thermal-only cumulative bookkeeping (info-loss class) | **no** purification turn; \(S\) not driven to ~0 at \(v\to 1\) |
| N3 | Pure vacuum seed, no drive | \(S_{\mathrm{rad}}\) stays ~0 |
| N4 | Unitarity (if pure global state) | \(\max\|S_{\mathrm{total}}\| < \varepsilon_U\) |

**Pre-registered defaults (freeze in claim run header):**  
\(\varepsilon_S = 10^{-4}\), \(\varepsilon_U = 0.05\) (healing units / nat), unless tightened in header.

---

## 4. Page-turn positive criteria (all required)

A **candidate Page turn** is booked only if **all** hold:

| # | Criterion |
|---|---|
| T1 | \(S_{\mathrm{rad}}(v)\) has an interior maximum: \(v_* \in (v_{\min}, v_{\max})\) with \(0.05 \le v_* \le 0.95\) |
| T2 | Late drop (see **§4.1 pins**): \(S_{\mathrm{rad}}(v_*)-S_{\mathrm{rad}}(v_{\mathrm{late}}) \ge \max\!\big(f_{\mathrm{drop}}\, S_{\mathrm{rad}}(v_*),\; 5\,\sigma_{\mathrm{jit}}\big)\) with \(f_{\mathrm{drop}}=0.10\) |
| T3 | Early rise: \(S_{\mathrm{rad}}(v_*) > S_{\mathrm{rad}}(v_{\mathrm{early}}) + \delta\) with \(v_{\mathrm{early}}\le 0.1\), \(\delta = 0.05\,S_{\mathrm{rad}}(v_*)\) |
| T4 | Nulls N1–N4 **PASS** on the **same** code path / parameters |
| T5 | Continuum ingredient P2 is **dynamical** in that run (not Γ-weight only on toy modes) |
| T6 | Artifact on disk: JSON with `v[]`, `S_rad[]`, `S_core[]`, null table, `v_late`, \(\sigma_{\mathrm{jit}}\), git-described script path |
| T7 | Script header sets `page_curve_claimed` only after T1–T6; default remains **false** |

**Not sufficient alone:** “looks Page-like” on unitary hybrid curiosity curves (batch1–2).

### 4.1 Pre-registration pins on T2 (Claude red AGREE-IF, 2026-08-03)

Frozen **in this protocol** (not chosen after seeing the curve):

| Pin | Definition |
|---|---|
| **\(v_{\mathrm{late}}\)** | The **final frame** of the claiming run. Not an argmin over a late window. |
| **Run reach** | T2 is **not evaluable** unless the run reaches \(v \ge 0.9\) at that final frame. If \(\max v < 0.9\), grade = **FAIL / incomplete**, not “no turn.” |
| **Noise floor \(\sigma_{\mathrm{jit}}\)** | Entropy jitter from the **same** run’s N1 and N3 null executions (T4 already requires them on the same code path). Define \(\sigma_{\mathrm{jit}} = \max(\sigma_{S}^{(N1)}, \sigma_{S}^{(N3)})\) where each \(\sigma_S\) is the stddev of \(S_{\mathrm{rad}}(t)\) over the null time series (or \(\max|S_{\mathrm{rad}}|\) if nearly flat and stddev is numerical zero — use \(\max( \mathrm{std},\; \max|S|,\; 10^{-8})\)). |
| **Absolute drop** | In addition to the fractional \(f_{\mathrm{drop}}=0.10\) cut, require \(S_{\mathrm{rad}}(v_*)-S_{\mathrm{rad}}(v_{\mathrm{late}}) > 5\,\sigma_{\mathrm{jit}}\). |

These two pins close post-hoc choice of the deepest late point and “10% of a noise wiggle.”

### 4.2 Monotone evaporation coordinate (batch8 stall treatment)

**Status:** **RATIFIED as a scoring aid only** once paired with active T8 and claim-decoupling.

Raw dynamical \(v(t)=E_{\mathrm{rad}}/(E_{\mathrm{rad}}+E_{\mathrm{core}})\) may **stall or
wobble** slightly while \(S_{\mathrm{rad}}\) continues to evolve. For T1–T2 scoring only,
define the registered monotone envelope
\[
u(t) := \max_{s\le t} v(s).
\]
- Report both \(v\) and \(u\) in the artifact.
- T1 uses \(u_*=u(t_*)\) at the \(S_{\mathrm{rad}}\) argmax; require \(0.05\le u_*\le 0.95\).
- T2 uses \(u_{\mathrm{late}}=u(t_{\mathrm{final}})\) and requires \(u_{\mathrm{late}}\ge 0.9\).
- This does **not** license blending a schedule into \(v\); \(v\) remains pure energy fraction.
- Scorecard must be computed by fixed code from **full** history arrays stored in the JSON
  (no hand-transcribed numbers; no downsampled-only scorecard).

### 4.3 T8 — single-valued \(S(u)\) requirement

**Status:** **ACTIVE / BINDING** (referee ratified after batch9 denial).

**Problem (batch9 denial):** if \(u\) freezes while \(S_{\mathrm{rad}}\) still rises, \(S(u)\) is
multivalued at that abscissa — “interior max at \(u_*\)” is sequencing, not a Page curve.

**T8:**
- At every fixed \(u\), the range of \(S_{\mathrm{rad}}\) values attained while \(u(t)=u\)
  (within bin width \(\Delta u=0.01\)) must satisfy
  \(\max S - \min S \le 0.1\,S_*\) where \(S_*=\max_t S_{\mathrm{rad}}(t)\).
- Entropy rise at frozen \(u\) earns **no T3 credit**.
- T1 requires a single-valued \(S(u)\) peak under this rule.

### 4.4 Claim-decoupling rule

**Status:** **ACTIVE / BINDING** (referee ratified after batch9 denial).

A CANDIDATE claim packet may be filed **only after**:
1. the run JSON is already on disk, and  
2. the scoring script is git-committed **or** owner-gated commit is impossible and the seats accept a frozen content-hash + path as provenance,  

never in the same packet as the first write of that run.

---

## 5. Grades

| Grade | Meaning |
|---|---|
| **INSTRUMENT PASS** | Run completes; nulls defined; no claim |
| **CANDIDATE TURN** | T1–T8 hold (incl. single-valued \(S(u)\)); still needs red AGREE; claim-decoupling satisfied |
| **PAGE CLAIM / Q6** | CANDIDATE TURN + **Claude red AGREE** + no fabrication of continuum |
| **FAIL** | Null fail, or turn without P2, or unitarity broken, or T8 multivalued \(S(u)\) |

---

## 6. Explicit non-claims (permanent until Q6)

- Does not close information paradox by coefficient payment  
- Does not use \(4v(1-v)\) as physics  
- Does not treat thermal-only cumulative \(dE/T\) as Page  
- Does not claim continuum GP self-consistency until that run exists  

### 6.1 Citation guard (Claude batch5)

Runs whose primary \(S_{\mathrm{rad}}\) is cumulative \(dE/T\) (or any monotone-by-construction
bookkeeping) **must not** be cited as “model failed to show a Page turn.” Failure of T1/T2
there is expected class behavior, not adverse physics. Only pure-state reduced radiation
entropy on a unitary global state can support a purification turn under T1–T2.  

---

## 7. Current instruments vs this protocol (2026-08-03)

Full index: `INSTRUMENT_INDEX.md` (same run dir). Standing claim: **none**.

| Instrument | P2 dynamical? | Nulls | Turn criteria | Claim |
|---|---|---|---|---|
| week1 sonic | no | partial | n/a | false |
| week2 Bogoliubov | stationary modes | thermal/subsonic | n/a | false |
| continuum_coupled_mvp | **no** (Γ weight only) | g=0 yes | curiosity only | false |
| continuum_evaporating | **no** (Γ weight + thermal bookkeeping) | thermal control yes | hybrid curiosity | false |
| continuum_dynamical_p2 | adiabatic re-solve only | yes | machine False | false |
| continuum_field_td | TD 1D field; \(S\) often \(dE/T\) class | yes | machine False | false |
| purestate_continuum | continuum ω/Γ weights (not full field QFT) | yes | machine True → **red DENIED** | false |
| candidate_rebuild | TD field + pure Gaussian + §4.2 | yes | machine True → **red DENIED** | false |

**Standing CANDIDATE:** none (denied ×3).  
**T8 + claim-decoupling:** **ACTIVE / BINDING** (ChatGPT REFEREE batch9-T8-claim-decoupling).  
**Next physics (not a claim unlock):** co-evolve \(S\) with advancing \(u\), not edge-tuning.  
`page_curve_claimed` remains **false** until T1–T8 + claim-decoupling + red.

---

## 8. Resource fence

- This box: OMP=1 / nice when cobaya load high; no PolyChord  
- Cluster (later): optional heavier mode grids / GP  

---

*Registered 2026-08-03 for R-PAGE. §4.1 pins added same day (Claude AGREE-IF cure). NO FABRICATIONS.*
