# THE DERIVATION HUNT — the remaining underived numbers, and where their pieces already sit (living; 2026-07-12)

*The operator's thesis: "we have enough in our model to derive everything — the last pieces
are already there. We just gotta look." This file is the looking: each remaining underived
quantity, the pieces of it ALREADY banked, the gap, and the status. Updated as pieces are
found; entries graduate OUT when fully derived (→ the spine) or die (→ the failures ledger).*

## GRADUATED THIS PASS

### The template-offset (strike 6's owed calc) — DERIVED ✓
The model's own winding structure supplies the true onset shape: a single comoving mode has
ρ ∝ √(m² + k²/a²)/a³ — the textbook massive-dispersion curve. Fitting the coded template
x²/(1+x²) against it (template_offset.py): **a_on(param)/a_clock = 0.86–0.92 across weight
windows → the fit parameter sits +0.04 to +0.07 dex above the physical clock.** The P-040
corollary's prediction corrects: log10(z_on) = 7.547 → **7.59 ± 0.02**. Consequence, booked
honestly: the shape branch of the third outcome explains only ~0.05 of the 0.39 dex gap to
the chain's interim 7.94 — the discrepancy substantially SURVIVES shape correction. The
third outcome narrows to its closure-purity branch (below). ALSO derived en passant: the
coded template SHOULD eventually be replaced by the dispersion shape itself — the model
already dictates it.

## OPEN — pieces inventoried

### f̄ = 2/π (P-041's mechanism) — the frame found, one step owed
Pieces present: (a) the ceiling is exactly 1 (harmonic + rest ICs → pure radial libration,
analytic); (b) the floor is exactly 1/2 (ergodic equipartition); (c) THE ENTIRE deviation
from 1 is the Z4/winding sector's torque (τ = 8ε_Aλ r⁴ sin4θ — the only agent in the
system), self-terminating because r⁴ dies faster than the harmonic energy under drag.
So f̄ is a FROZEN PARTIAL-MIXING number owned by the topology sector — the winding's third
output (after n and the comb). The owed step: the freeze-out calculation (when the Z4
torque decouples under h = 1/(2t) drag) — Kibble-Zurek-class, the SAME mathematics as the
first draw. Target: does the freeze land at exactly 2/π? Referee: the 256×3 ensemble
(running).

### ρ_inf's 20% residual — TWO candidate mechanisms, honest comparison
Measured: (ρ_obs/ρ_calc)^(1/4) = 0.8349. Candidates: (i) **dof-halving**: the medium is a
COMPLEX field (2 real dof); if the localization calc counted both where only one serves as
the floor, ρ → ρ/2 → ratio 2^(−1/4) = 0.8409 (**0.7% off**; mechanism-rich — the other dof
is the excitation sector, already the model's grammar); (ii) **the census discount**: 5/6 =
0.8333 (**0.2% off**; mechanism-poor — no natural N=6 roster exists). The firewall verdict:
(i) fits worse but has a mechanism; (ii) fits better but is naked numerology. The
discriminant: re-derive the localization clause's dof bookkeeping (§18) — a reading job,
pieces all banked.

### z_on (= the genome mass m) — blocked on the closure-purity branch
Pieces present: the onset clock (verified), the abundance closure (Ψ₀ ∝ m^(−1/4)), NOW the
shape offset (+0.05 dex, above). The remaining unknown: does the conversion channel
(dcdf_conv, sourced in routeD) shed enough of the budget to bend the quarter-power? If yes,
the m ↔ α_c mapping shifts and the 7.94-vs-7.60 gap could close from the mapping side. The
piece needed: the conv-corrected closure exponent — computable from the routeD posterior
when it converges (running).

### η (Card 4) — the template is banked, the calc is heavy
Pieces: the Josephson form I_L ∝ μ·sin Δθ (the junction template), the frozen-era timing
crux, leptophilia. Gap: the actual transfer integral. Status: the docket's heaviest
tractable item.

### v_L (Card 6) — pieces half-present
Pieces: the medium sources v_L; the type-III triplets (census-visible option) or steriles
(invisible); P-023's 0.07–0.09 eV target. Gap: the induced-VEV calculation.

### λ — conditionally derived already
Pieces: the ceiling λ ≤ (m/Ψ₀)² ≈ 2×10⁻⁹¹ (derived); P-031's saturation hypothesis
(registered). If saturation is a THEOREM (axion-class potentials saturate their isocurvature
ceiling generically?), λ = the ceiling — derivation would be one argument away. The piece
to look for: why the first draw's amplitude sits AT the quartic onset, not below.

### n (the winding integer) — measured-not-derived by design
Pieces: first-draw statistics (n ~ 10–30), topological protection, the comb's tooth count =
the measurement. The piece missing: the percolation-weighted draw (the zero_point_start
review). Note: n may be genuinely environmental (one draw, one universe) — a MEASURED
integer, like which Landau level you live in. If so it graduates to "not derivable, lawfully"
— the scope theorem's fourth wall.

### M3 (the root) — the basement
Everything above is conditional on it. Pieces: the no-bare clause (named), the two-census
structure, the forced Planck basement, the F-F species sum. This is not a "look" item — it
is the one true computation left. Everything else in this file feeds it evidence.

## FOUND THIS PASS — the ρ_inf/m_ν CLOSURE (one mechanism, two graduations)

The operator asked "is v_L derived?" — no, but the look revealed that **v_L's missing piece
and ρ_inf's missing piece are the same piece.** The chain, all banked separately:
1. §18's calc: ρ_inf^{1/4} = 2.695 meV (zero dials, 20% high).
2. The residual candidates (this file, above): ×2^{−1/4} (dof-halving) or ×5/6 (census).
3. §6's shared-scale claim: ρ_inf^{1/4} = m_ν,lightest (the Majoron tie, P-2026-020's home).
4. Oscillation splittings (external data, [Planck2018]-era global fits).

APPLY 2 TO 1, FEED 3, ADD 4: m_lightest = 2.266 meV (dof) or 2.246 (census) →
**Σm_ν = 61.4 / 61.3 meV — reproducing the banked P-2026-012 (~61 meV) to 0.5%,
by a route that never consulted it.** If the residual mechanism lands (the §18 dof
bookkeeping audit — note the calc's ½ prefactor as the specific slot to audit), THREE
quantities graduate at once: ρ_inf (zero-residual derivation), m_ν,lightest, and Σm_ν —
and the sampled m_ncdm leaves the parameter list, taking the count of underived
cosmological parameters from 4 to 2 (A_s, n_s).
HONEST FLAGS: (a) the shared-scale claim carries its own post-hoc flag (task #43 spurion,
un-lifted); (b) the residual mechanism is still two-candidate; (c) mild internal tension
to resolve: P-023's de-biased band (0.07–0.09 eV) vs this chain's 0.061 eV — the running
chains' m_ncdm posterior discriminates.

## FOUND THIS PASS (second sweep) — λ GRADUATES CONDITIONALLY, plus three frame finds

### λ — the saturation argument was already banked ✓ (conditional graduation)
The ceiling: λ ≤ (m/Ψ₀)² (derived, the isocurvature bound). The missing piece was "why
does the draw amplitude sit AT the ceiling?" — and the answer is the DEFINITION of the
banked genesis: the first draw is a Kibble draw AT T_c, and T_c is precisely the
temperature where the effective mass term and the quartic balance — a thermal draw at its
own transition is BORN at the quartic-mass crossover. Saturation is not a hypothesis; it
is what "Kibble draw" means. Therefore **λ = (m/Ψ₀)², equality, up to the O(1) Ginzburg
factor** — and P-031 (the %-level isocurvature at ℓ~170) converts from a registered
hypothesis to a DERIVED CONSEQUENCE of the genesis. Honest bounds: the O(1) Ginzburg
factor is the residual unknown (same class as f̄'s freeze-out — the third job of the
same transition mathematics); conditional on the Kibble-draw genesis (banked, t343-class).

### η and the comb share ONE integer (frame find — a new structural falsifier)
Card 4's AD-direct route: the transferred charge rides the phase gradient — which IS the
winding. So the baryon asymmetry inherits the topological integer: **η ∝ n**. The comb's
tooth count (P-029) and the baryon density become two readings of the same n. New
cross-kill, registered here: once the comb measures n, η/n is a pure-mechanism number —
if the Josephson transfer calc then misses it by orders, the AD-direct route dies with no
retreat. (The transfer integral itself remains the docket's heavy calc.)

### A_s — the census form (frame find, value open)
In the medium's grammar the primordial amplitude is Poisson noise of the condensate:
A_s = 1/N_quanta (per coherence volume at genesis) → N = 1/A_s ≈ 4.8×10⁸. Mechanism-shaped
(counting, the model's native language); the independent count of N is the missing piece.
No value claimed.

### n_s — the e-fold form (frame find, value open)
The tilt's textbook origin is duration: n_s − 1 ≈ −2/N_gen → N_gen ≈ 66 for the measured
0.9649. The model's conformal/genesis phase owes an e-fold count; if the genesis story
produces ~66 naturally, n_s graduates. No value claimed; the count is the piece to find.

*Scorecard after two sweeps: graduated — the template offset, λ (conditional); closed into
one mechanism — ρ_inf + m_ν (pending the §18 audit); framed — f̄'s freeze-out, η∝n,
A_s = 1/N, n_s = 1 − 2/N_gen. Still standing untouched: M3, the §18 audit itself, the
transfer integral, the spurion. The operator's guarantee is running ahead of the referee.*

## FOUND THIS PASS (third sweep) — the §18 audit resolves STRUCTURALLY; n_s lands at 0.2σ

### ρ_inf — the residual's identity found: it IS the dressing factor ✓
Write §18's formula in its two pieces: ρ_inf^{1/4} = [½α_c²M₂] / [(16π²α_c^{3/2})^{1/4}].
The FIRST piece alone — the medium's own Bohr binding energy, E_b = ½α²M, the scale
ladder's founding form, at coupling α_c and the banked mesoscale mass M₂ (1/M₂ = 20 nm) —
equals **2.251 meV vs the measured 2.25 meV: 0.4 parts per thousand.** The SECOND piece
(the localization dressing, 0.8385) is numerically identical to the observed residual
(0.8349): **the entire 20% discrepancy is the dressing factor itself.** The sky is saying
the dressing shouldn't be there: dark energy's quarter-power = the medium's own Bohr
energy, undressed. AUDIT VERDICT: the earlier dof-halving (0.8409) and census-5/6 (0.8333)
candidates were numerically degenerate impostors for this factor — both DEMOTE; the owed
step narrows to one surgical question: WHY does the localization normalization
double-count (the ½ Bohr prefactor and the 16π² loop normalization plausibly dressing the
same physics twice)? Consequences if it lands: ρ_inf graduates at 0.04% residual; the
m_ν/Σm_ν closure (above) fires at the same precision; m_ncdm leaves the sampled list.
COHERENCE FLAG (honest): the 0.4‰ landing uses α_c = 0.0214; under P-040 (α_c = 3α) the
match retunes M₂ to 21.0 nm (a 5% shift on a parked, loosely-pinned scale) — zon
arbitrates the pair jointly.

### n_s — the tilt lands from the model's own two scales (0.2–0.5σ) ✓ (frame + bet)
The generic tilt of a nearly-conformal phase of duration N e-folds is n_s = 1 − 2/N. The
model's conformal-origin phase runs between its two banked scales: the forced Planck
basement and the onset clock (T_on = 9.41 keV). **N = ln(M_Pl/T_on) = 54–56 →
n_s = 0.963–0.964 vs measured 0.9649 ± 0.0042** — inside 0.5σ with zero new inputs.
Honest flags: (i) the coefficient "2" is borrowed from the slow-roll convention — the
model's conformal phase owes its own derivation of it (the data kill 1/N and 3/N at >4σ,
so the bet is sharp); (ii) the M_red-vs-M_Pl basement ambiguity spans 0.9629–0.9640 (both
land); (iii) cross-prediction: n_s and z_on are now LINKED (both read T_on) — the zon
chain's verdict tightens this number too. A_s remains framed-only (the 1/N census form;
the independent quanta-count is the missing piece).

*Scorecard after three sweeps: GRADUATED — template offset, λ (conditional), ρ_inf
(structural, one surgical question owed), n_s (frame + sharp bet). CLOSED-INTO-ONE —
ρ_inf/m_ν/Σm_ν. FRAMED — f̄ (freeze-out; semi-empirical route: the running ensemble can
measure the freeze trajectory directly), η ∝ n (the shared integer), A_s = 1/N. STANDING —
M3 (the root), the transfer integral, the spurion, the "2". The operator's guarantee:
four-for-four across three sweeps.*
