# R1 caustic-bit — the precision test (the Θ_loc plateau's universality) — working log

*Reasoning record. Interim/relative results are legitimate here; the standing books
carry the hardened numbers. Sim: `scripts/r1_caustic_sim.py` (tiny-grid, single-thread,
sub-minute; production written and deferred). Closed-form anchors added to
`scripts/audit_math_pass.py`.*

## The owed test

V5 built the local caustic-bit operator

 **Θ_loc = Q/(Q+K)**, Q = |∇√ρ|², K = ρ|∇S|²

(Madelung amplitude-gradient energy vs phase-gradient energy) and passed its existence
test: a ≈0.5 plateau in granulated speckle against ≈10⁻⁶ in laminar flow, on a coarse
grid. The operator exists to carry a coupling m_e(Θ_loc): every lab and every quasar
absorber sits at the plateau, so m_e reads the same everywhere granulated — **provided
the plateau is universal**. The existence grid saw a few-percent spread between two
speckle realisations (0.496 vs 0.459). A few-percent spread in the plateau is a
few×10⁻⁴ spread in m_e, which overruns the ≈10⁻⁷ molecular bound on m_e variation. So
V5 owed a **precision test**: is the plateau universal between halo environments at the
≈10⁻⁵ level? The coarse grid could not resolve it.

## What a caustic is here, and the tool that fits

A classical caustic is a fold in the phase-space flow — a density catastrophe. In this
medium the critical velocity is zero (cert 1): every infall is supercritical, so
classical caustics never form. They regularise into de Broglie interference — a
fully-developed speckle field threaded by a quantised-vortex tangle (the nodal lines).
The caustic bit is therefore a **statistics** question about the wave-regularised
caustic = an isotropic Gaussian random wave, not a catastrophe-integrator job.

**Tool: a dedicated developed-speckle generator + an accurate Madelung-gradient
estimator**, cross-validated in the caustic (vortex-tangle) regime and under real
Schrödinger–Poisson gravity. The validated speckle and split-step machinery from the
two-field granule solver is reused (imported, not modified) and re-validated here, where
the object is a fold-tangle rather than a soliton. A classical caustic ray-tracer would
be the wrong tool — it would integrate a singularity the medium never forms.

## The analytic spine — why the plateau is exactly ½

Pointwise algebra, for any differentiable ψ = √ρ · exp(iS):

 ∇ψ = (∇√ρ + i√ρ ∇S) · exp(iS) ⟹ **|∇ψ|² = Q + K**.

Estimator without the √ρ cusp: with w_i = ψ* ∂_i ψ,

 Q = Σ_i Re(w_i)²/ρ, K = Σ_i Im(w_i)²/ρ, **Θ_loc = Σ Re(w_i)² / Σ |w_i|²** (ρ cancels).

For a developed speckle field ψ is a **circular** complex Gaussian random field (uniform
random phases). Then ∇ψ is independent of ψ and circularly symmetric, so
u = exp(−iS)·∇ψ has real and imaginary parts — a ≡ ∇√ρ and b ≡ √ρ ∇S — that are
**identically distributed and independent**. Hence

 **Θ_loc = |a|² / (|a|² + |b|²) ~ Beta(d/2, d/2)** (d = dimension).

Beta(d/2, d/2) is symmetric about ½, so its **mean is exactly ½ in every dimension**,
with variance 1/(4(d+1)). And because the a↔b exchange symmetry (Θ ↔ 1−Θ) survives any
covariance, the mean stays ½ even for an **anisotropic** spectrum. The plateau is
therefore pinned to ½ with **zero dependence** on the power spectrum, σ_v, density,
epoch, or dimension — sharper than "O(1) universal." The only thing that moves it off ½
is loss of circularity: a field that is not fully phase-randomised (a residual
laminar/coherent-flow component). That is the real, quantifiable content of the
precision test.

 2D: Beta(1,1) = Uniform[0,1], mean ½, variance 1/12.
 3D: Beta(3/2,3/2), mean ½, variance 1/16.

## Validations (numbers from the sim; cross-checked against the analytic law)

- **Partition identity** Q + K = |∇ψ|² holds pointwise to max relative error 8.9×10⁻¹⁶
 (median 1.8×10⁻¹⁶), zero masked points — Q and K exactly split the gradient energy;
 the estimator carries no cusp artefact.
- **Generator re-validation**: the dimension-general speckle reproduces the plateau of
 the already-validated granule-solver field (⟨Θ⟩ 0.494 vs 0.499 at 3D tiny grid).
- **Distribution vs Beta(d/2, d/2)**: 3D variance 0.06253 vs 1/16 = 0.06250 (four
 figures), KS 0.005; 2D matches Uniform[0,1] (mean 0.496, variance 0.0825 vs 1/12,
 KS 0.009). The pointwise law is confirmed.
- **Caustic content (resolve the fold, not a soliton)**: the vortex-tangle density
 Θ_glob ≡ n_vortex·l_dB² = 0.082 vs the Berry–Dennis isotropic value 1/4π = 0.0796 —
 the field genuinely carries the quantised-vortex tangle at the predicted universal
 density. Laminar controls: a plane wave gives Θ_loc = 5×10⁻²⁹ (ρ constant ⟹ Q = 0
 exactly); a smooth wavepacket 3×10⁻³. Both sit orders below the plateau — the binary.

## The precision result

- **Environment sweep** (spectrum shape: Maxwellian / shell / power-law / top-hat; σ_v
 spanning l_dB, i.e. halo mass and epoch; 2D and 3D): every environment returns
 ⟨Θ_loc⟩ = ½ to sampling precision. The best-sampled environments land on ½ within
 their error bars (3D Maxwellian 0.4995 ± 0.0008; 2D power-law 0.5002 ± 0.0006). The
 grand spread at tiny grid (≈1.5×10⁻²) tracks the per-environment sampling errors, not
 a physical offset.
- **Anisotropy** (3:1 spectrum): ⟨Θ_loc⟩ stays at ½ (isotropic 0.491, anisotropic
 0.504 — both within sampling) — the exchange-symmetry claim holds.
- **The developed↔laminar knob**: mixing a fraction f of laminar flow (a tilted plane
 wave) into the speckle pulls the plateau down monotonically,
 ⟨Θ_loc⟩ ≈ ½ − 0.155·f near f = 0, reaching exactly 0 at f = 1 (the binary's laminar
 pole). This is the physical variable behind any environment-dependence: the plateau
 moves only with residual-laminar (undeveloped) fraction, at a measured slope ≈0.16 per
 unit fraction.
- **The existence-grid "spread" identified**: narrowing the spectrum (fewer independent
 speckle cells per box) pulls ⟨Θ_loc⟩ below ½ — 0.481 at ≈4 cells, climbing to ½ by
 ≈50–100 cells. The coarse grid's 0.496 vs 0.459 was this finite-developedness bias
 (its second run cut the mode count), not an environmental spread.
- **Gravity**: real Schrödinger–Poisson evolution (shared self-gravity) leaves the
 plateau at ½ (0.501 → 0.508 over the run, within sampling) — gravitational
 non-Gaussianity does not move the mean, and the imported integrator is re-validated in
 the caustic regime.

## R1's grade against its precision claim: **PASS** (with two structural conditions named)

The plateau's mean is ½ for developed isotropic (or anisotropic) circular-Gaussian
speckle — analytically exact and numerically confirmed — so the environment-to-
environment universality the coupling needs holds **by theorem, not by resolution**. The
≈10⁻⁵ requirement on the mean is met exactly in the developed limit; the coarse-grid
spread was a finite-developedness artefact. This is stronger than the existence-test
reading of "O(1), few-percent."

Two structural conditions carry the pass, and are where any real residual kill-test now
lives:

1. **The coupling must respond to a volume- / line-of-sight-averaged Θ over many de
 Broglie cells, not the pointwise Θ.** Pointwise Θ_loc has O(1) variance (Beta: 1/12 in
 2D, 1/16 in 3D), so a strictly local m_e(Θ_loc) would scatter m_e by order unity
 within a single absorber — unphysical. The many-cell average concentrates on ½ as
 1/√N_cells. For a realistic absorber column (l_dB ~ pc, path ~ kpc gives
 N_cells ~ 10⁹ in 3D) the averaged Θ sits at ½ to well below 10⁻⁵; longer columns do
 better. The precision requirement is met with orders of margin — **once the coupling
 is defined as an average.** This averaging requirement should be stated explicitly as
 part of the mechanism.
2. **Every m_e-measurement environment must be deep-developed** — not a soliton
 core / coherence-patch (too few cells) and not a strongly anisotropic laminar flow.
 Generically satisfied for quasar absorbers and lab regions, both of which span vast
 numbers of granule cells; the departure would show only in genuinely undeveloped or
 near-coherent regions, at the measured slope ≈0.16 per unit laminar fraction.

Honest limitation: the tiny grid does not brute-force-measure the mean to 10⁻⁵ directly
(that needs ~variance/(10⁻⁵)² ≈ 6×10⁸ independent cells — the production domain). It
instead validates the **law** (Beta, mean ½ exact) whose analytic exactness delivers the
10⁻⁵, plus the finite-cell convergence toward ½ and the developed↔laminar slope. The
direct central-limit narrowing demonstration (averaging Θ over long many-cell columns
down to 10⁻⁵) is written into `run_production()` and deferred until the chains are off
the machine.

## What the verdict document should record (not edited here)

- §2.5 Step 2 / Step 3 caveat (iii): the plateau value is ½, and its universality is the
 analytic Beta(d/2, d/2) exactness (mean ½ for any developed isotropic/anisotropic
 speckle, spectrum/σ_v/epoch-independent), not a numerical few-percent coincidence. The
 "few-percent spread (0.46–0.50)" is a finite-developedness (finite-cell) artefact; the
 physical spread of the mean is zero in the developed limit.
- The owed precision test is discharged: the plateau universality is a proven property
 of random-wave statistics. The two conditions that carry it — the coupling as a
 many-cell average, and developedness of measured environments — replace the earlier
 "≈10⁻⁵, beyond this document's tools" framing. The non-polynomial coupling's UV story
 remains the standing external debt.

## Reproduce

`python3 scripts/r1_caustic_sim.py` (tiny grids, single-thread, ≈13 s). Production sweep
(from the scripts directory): `python3 -c 'import r1_caustic_sim as m; m.run_production()'`
— run only when the MCMC chains are off the machine. Closed-form plateau anchors (mean ½,
variance 1/(4(d+1)),
Berry–Dennis 1/4π) are in `scripts/audit_math_pass.py`; verified by
`bash scripts/check_before_commit.sh`.
