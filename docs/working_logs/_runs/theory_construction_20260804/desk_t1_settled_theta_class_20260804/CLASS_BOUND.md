# CLASS_BOUND — settled ⟨Θ⟩ vs Θ_lock under stocked continuity

**Package:** `desk_t1_settled_theta_class_20260804`  
**Partial grade:** **CLASS-BOUND** (not S1 land; COMPLETE remains 0)  
**Script:** `scripts/bounce_desk_t1_class_bound.py`  
**Log:** [`logs/desk_t1_class_bound.log`](./logs/desk_t1_class_bound.log) · [`logs/summary.json`](./logs/summary.json)

---

## 1. Stocked 0D form

\[
\dot n = -n\,\Theta,\qquad
\dot\Theta = -\Theta^2 + \kappa(n-1) - \gamma\,\Theta,\quad \gamma>0.
\]

Unique physical fixed point: \((n,\Theta)=(1,0)\).  
Local linearization (κ,γ>0): \(\lambda^2+\gamma\lambda+\kappa=0\); underdamped branch on the legal grid has \(\mathrm{Re}(\lambda)=-\gamma/2\).

---

## 2. Exact identity (any κ, γ, any IC)

From \(\dot n=-n\Theta\) alone:

\[
\Theta = -\frac{\mathrm{d}}{\mathrm{d}t}\ln n
\quad\Rightarrow\quad
\langle\Theta\rangle_{[t_1,t_2]}
=
\frac{\ln n(t_1)-\ln n(t_2)}{t_2-t_1}.
\]

**Window-mean Θ is exactly the log-density drop per unit time.**  
No linearization. No grid. Holds on and off the 710-row scan.

---

## 3. Bound: settled mean = Θ_lock requires ~10⁵⁰ density drop

Target: \(\Theta_\mathrm{lock}=1/\sqrt\alpha\approx 11.70623765\) (d=3).

Required density ratio over a window of length \(\Delta t\):

\[
\frac{n(t_1)}{n(t_2)}
=
\exp\!\big(\Theta_\mathrm{lock}\,\Delta t\big).
\]

| Δt | Θ_lock · Δt | n(t₁)/n(t₂) | log₁₀(ratio) |
|---:|---:|---:|---:|
| 1 | 11.71 | 1.21×10⁵ | 5.08 |
| 5 | 58.53 | 2.63×10²⁵ | 25.42 |
| 8 | 93.65 | 4.70×10⁴⁰ | 40.67 |
| **9.7** | **113.55** | **2.06×10⁴⁹** | **49.31** |
| **10** | **117.06** | **6.91×10⁵⁰** | **50.84** |
| 20 | 234.12 | 4.78×10¹⁰¹ | 101.68 |

**Headline:** for S1_settled last-20% windows of length \(\Delta t\sim 10\) (se≈40 runs), reaching \(\langle\Theta\rangle=\Theta_\mathrm{lock}\) requires an **in-window density drop of order \(10^{50}\)**.

Free κ, γ and grid densification **cannot** evade the identity. Peak Θ ≥ lock is irrelevant to this window-mean bound.

---

## 4. Numeric check (stocked Euler dt=10⁻³)

Identity checked on prior headline rows (se=40, last 20% of full history):

| row | ⟨Θ⟩ settled | Θ from ln n | rel err | Δt | n₁/n₂ actual | log₁₀ needed for lock |
|---|---:|---:|---:|---:|---:|---:|
| argmax quality | **+0.043582** | +0.043620 | 8.7×10⁻⁴ | 9.691 | **1.526** | **49.27** |
| stocked default | −0.003680 | −0.003682 | 6.8×10⁻⁴ | 9.650 | 0.965 | 49.06 |
| prior F5 best-late | −0.058221 | −0.057748 | 8.1×10⁻³ | 9.606 | 0.574 | 48.84 |
| argmax all-phys | +0.105600 | +0.105761 | 1.5×10⁻³ | 9.675 | 2.782 | 49.19 |

Settled means reproduce `settled_late_theta` stamps to machine precision.  
Identity holds at ≲1% (F5 worst: large |Θ| + first-order Euler).

**Quality residual is density drift:** +0.0436 over Δt≈9.69 means n falls by **~34.5%** across the “settled” window — leftover drift toward FP (1,0), not a late attractor near lock.

---

## 5. GPE 1D / spherical — class conclusion for settled mean

Stocked Madelung/continuum:

\[
\partial_t n + \nabla\cdot(n\mathbf{v})=0,\qquad \Theta=\nabla\cdot\mathbf{v}.
\]

On mass-conserving domains:

\[
\frac{\mathrm{d}}{\mathrm{d}t}\int n\ln n
=
-\int n\,\Theta
\quad\Rightarrow\quad
\langle\Theta\rangle_n
=
-\frac{1}{M}\frac{\mathrm{d}}{\mathrm{d}t}\int n\ln n.
\]

Window-mean **mass-weighted** expansion is a mass-weighted log-density drop. Large positive settled ⟨Θ⟩ still prices as an enormous log-n reorganization.

**Prior stamps** (`n3_gpe_late_theta_20260804`; not re-run here):

| layer | late ⟨Θ⟩ **scan max** | settled ⟨Θ⟩ **scan max** | vs lock |
|---|---:|---:|---|
| 1D clean (**indep. argmax**) | +0.0265 (own settled **−0.0027**) | +0.0015 | ≪ |
| 2D Θ_xx (**one run**) | +0.0346 | +0.0391 | ≪ |
| spherical light | O(−0.02) | O(−0.01) | unclean; not S1 |
| 0D (**indep. argmax rows**) | +2.870 (own settled **+0.1085**) | +0.114 (own late **+2.650**) | ≪ |

**Red V2:** late/settled columns are scan maxima from **independent argmax rows** (2D is one pancake block). Not one configuration.

**Verdict:** stocked GPE 1D / 2D / spherical forms **do not change** the class conclusion for settled mean.  
`production_3d = false` (full 3D still not stocked). Continuity-bound survives any future 3D instrument that keeps \(\partial_t n+\nabla\cdot(nv)=0\).

---

## 6. What NEW instrument would break the class (not free dial)

| candidate | breaks class? | note |
|---|---|---|
| Free κ, γ dial | **NO** | identity independent of stress coeffs |
| Grid densification / settle_extra | **NO** | identity is form-level |
| Peak / Madelung spikes | **NO** | not S1 window-mean |
| **Continuity source/sink** \(\dot n\neq -n\Theta\) | **YES if stocked & named** | must be legal medium form, not dial |
| **N2 match-book** (S1 ≠ window-mean Θ) | **YES if lock metric changes** | orthogonal survivor |
| Multi-component law: lock Θ ≠ expanding medium’s own Θ | **YES if named** | not invented here |
| Production 3D GPE still conserving | **NO** | class bound survives |
| Production 3D with non-conserving medium | only after form is stocked | not present |

**This package invents no new instrument.** CLASS-BOUND is the partial; S1 remains MISSING_INPUT.

---

## 7. Scope of CLASS-BOUND

- **In:** stocked FA3 0D under \(\dot n=-n\Theta\); mass-weighted continuum/GPE under continuity.  
- **Out:** claim that every conceivable stress law is impossible; claim bounce closed; claim Θ_lock Derived; claim production 3D COMPLETE.

*NO FABRICATIONS. CLASS-BOUND ≠ S1 land. exit0 ≠ PASS. COMPLETE = 0.*
