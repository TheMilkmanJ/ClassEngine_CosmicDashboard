# Track A2 closure: Route T f into the n_s / r triangle (2026-07-31)

Code: `scripts/ns_routeT_closure.py`.  
Depends on: Route T γ* from `census_alpha_B_first_principles.py` (A1),  
normalization triangle `as_normalization_triangle.py`,  
envelope mechanism `ns_envelope_mechanism.py` / `tilt_envelope_derivation.md`.

## Headline

| object | before (A1 open) | after Route T f |
|---|---|---|
| f = k·ξ imprint | pinned *given* r; target ~2×10⁻⁴ | **f = γ\* = ε²√2 = 2.225×10⁻⁴** (medium) |
| r conversion rate | band **[0.81, 3.23]** from iso residual | **r = 0.992** (meas A_s) / **0.987** (closed A_s) |
| S/ζ = 1/(r L\*) | 0.7–2.0% over surviving r band | **1.63%** (point) |
| n_s envelope | 0.9677 (+0.66σ) | unchanged; **still +0.66σ** |
| approach-to-scaling | OOM open | OOM open (sub-σ gap −0.0028) |

**Grade: CANDIDATE CLOSED** — r determined, isocurvature residual inside P-2026-031, envelope within data. Named residual: approach-to-scaling amplitude uncomputed; A1's d_⊥=2.

## 1. Does r become determined?

Yes. The triangle is

> A_s = r² L\*² f³ / 2π²

With f supplied by Route T (no A_s in the inputs) the inversion is a point:

> r = √(2π² A_s) / (L\* f^{3/2})

| A_s channel | f (Route T) | **r** |
|---|---|---|
| measured 2.100×10⁻⁹ | 2.225×10⁻⁴ | **0.9917** |
| closed (α_c/4πk)³ = 2.081×10⁻⁹ | 2.225×10⁻⁴ | **0.9871** |

Self-consistency check: A1 graded Route T against the **r = 1** triangle target (f_ref = 2.206×10⁻⁴ closed / 2.213×10⁻⁴ meas). Solved r ≈ 0.99 returns that referee as honest, not a silent fit — f_T / f(r=1) = 1.009 (meas), 1.009 (closed).

The former two-sided iso band r ∈ [0.81, 3.23] is now a **consistency window** the determined point sits inside, not the best the construction can say.

## 2. Isocurvature residual vs P-2026-031

Conversion residual at horizon entry:

> S/ζ = 1/(r L\*)

| r | S/ζ |
|---|---|
| 0.9917 (meas) | **1.630%** |
| 0.9871 (closed) | **1.638%** |
| 1.0 (fiducial) | 1.617% |

Registered triangle band (sub-%–% class, P-2026-031): **[0.5%, 2.0%]**.  
Broader envelope-doc class: [0.2%, 2.0%].

**PASS** — residual is the percent-class registered line: mechanism residual and P-2026-031 amplitude class are one object read twice. External referee unchanged: a future CMB bound at ℓ ≈ 170.

## 3. Does envelope + approach fully account for n_s − 1 ≈ −0.035?

### Envelope (derived at candidate grade)

Coherent conserved-charge conversion forces

> n_s = 1 − 2/L\* = **0.9677**, n_s − 1 = **−0.0323**

against measured 0.9649 ± 0.0042 → **+0.66σ**. Signature α_s = −(1−n_s)²/2 = −5.23×10⁻⁴ forced.

Envelope supplies **92%** of the measured |n_s−1| ≈ 0.0351; the post-envelope gap is

> Δ = (n_s−1)_meas − (n_s−1)_env = **−0.0028** (< 1σ)

### Approach-to-scaling (exponent only)

Route T VOS: v\* = 1.11×10⁻⁴ ⇒

> a = β(1+v\*²) ≈ ½, **a − 1 = −0.500**

Transient δγ/γ ∝ t^{a−1} is red in sign. OOM map (not a derivation): if residual fraction δ at the pivot sources tilt via n_s−1 ≈ 3δ, then

| goal | \|δ\|_pivot needed |
|---|---|
| full −0.035 from approach alone | ~0.012 |
| close the post-envelope −0.0028 | ~0.0009 |

**Neither is derived** — both need formation epoch + initial mismatch. Approach-to-scaling remains **OOM-OPEN**.

### Honest read

- Envelope **does** account for n_s within current data (no tension).
- Envelope + approach do **not** jointly claim a first-principles exact −0.035: the last ~0.003 is uncomputed, sub-σ, and not a kill.
- Do **not** promote “n_s − 1 derived to the milli level.”

## Grade and gates

**CANDIDATE CLOSED** on Track A2 promotion path:

1. **r determined** (was banded) by medium f + A_s.
2. **S/ζ determined and inside** the registered isocurvature band.
3. **Envelope n_s consistent** with measurement at +0.66σ.

### Named residuals (not hidden)

| residual | status | kill if |
|---|---|---|
| d_⊥ = 2 (A1) | named O(1) | reconnection microphysics returns c_chop far from 2 with no replacement |
| approach-to-scaling \|δ\| | OOM open | only matters if future data force n_s away from 0.9677 *and* the gap cannot be filled |
| P-2026-031 CMB bound | external referee | correlated iso bound tightens below ~1% at residual's scale class |

### Kill conditions (armed)

1. Medium reconnection returns c_chop ≪ 2 (or ≫ 2) with no O(1) replacement that restores f without fitting A_s.
2. CMB bound on *correlated* isocurvature drops below the 1.6% residual while r held near 1.
3. Envelope form 1 − 2/L\* excluded by future running precision (α_s referee).

### Not claimed

- Derived (theorem) grade for r or n_s.
- n_s − 1 = −0.035 from approach transient alone.
- Zero free parameters of the whole model (Track B inputs remain).

## Cross-links

- A1 Route T: `census_alpha_B_first_principles.md`, `scripts/census_alpha_B_first_principles.py`
- Triangle: `scripts/as_normalization_triangle.py`, tilt envelope addenda
- Envelope mechanism: `tilt_envelope_derivation.md`, `scripts/ns_envelope_mechanism.py`
- Residual gate (pre-Route-T band check): `scripts/ns_residual_gate_check.py`
- E2E board: `_E2E_DERIVATION_BOARD.md` Track A2
