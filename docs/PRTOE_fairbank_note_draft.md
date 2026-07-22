# Note for Prof. W. Fairbank — what a unified dark-fluid cosmology predicts for 0νββ

*2026-07-19. Plain physics throughout; self-contained.*

## The result in three sentences

In a unified dark-sector cosmology — one superfluid scalar replacing dark matter and dark energy,
plus a single derived 1.2543% early-universe shift of the electron mass (ε = 27α/5π) — the neutrino
sector is an output rather than an input: the model's dark-energy scale ties to the lightest
neutrino mass, giving **Σm_ν = 61.4 meV with normal ordering**. Because the mass mechanism violates
lepton number, **neutrinos must be Majorana, and the 0νββ process is structurally required.** The
corresponding effective mass, with measured splittings and free Majorana phases, is
**m_ββ ∈ [0.04, 5.3] meV, with a phase-averaged rms of 3.3 meV** (the rms is the
rate-relevant average, since the rate goes as m_ββ²; the median over phases is 3.05 meV).

## What this means for your program

**nEXO is the only experiment in the world with a chance of seeing this, and the window is
narrow.** That is the reason for writing, and the next section works it out. The short version: the
model's ceiling is m_ββ = 5.30 meV, and nEXO's projected reach at the favourable end of the
matrix-element range is 4.7 meV — so a thin band, roughly **4.7 to 5.3 meV**, is common to both.
LEGEND-1000 (9–21 meV) and CUPID (12–34 meV) sit entirely above the model's ceiling and cannot
reach it at any matrix element. Everywhere outside that thin band, a confirmed detection falsifies
the model outright.

**The converse is weaker, and the asymmetry should be stated.** A null at any sensitivity does not
kill the model, because the phases can cancel. And while a demonstrated Dirac nature would end the
model logically — the mass mechanism violates lepton number, so Majorana is not optional — there is
no practical route to demonstrating Dirac nature. You cannot prove the absence of a process. The
experimental content of this prediction is therefore one-directional: **your program can refute this
model but cannot confirm it.**

**The near-term threat is cosmological, and it comes from below.** DESI-era CMB+BAO limits reach
Σm_ν ≲ 72 meV with some combinations pressing lower, toward the normal-ordering floor itself. The
model sits at 61.4 meV, just inside. The live risk is therefore not a detection above the prediction
but **the upper limit descending through it**. The model's defence is that those limits are
ΛCDM-conditional and the squeeze relaxes under this model's recombination physics (next section) —
which is a testable claim rather than an escape, and the fastest way to grade this whole sector.

Which half of this is distinctive? The sum is not. Σm_ν = 61.4 meV sits
only **2.6 meV above the minimum that normal ordering allows** (58.8 meV, at m₁ = 0), and planned
cosmological resolution is ~20 meV — so no experiment now planned can separate this model's sum from
the minimal-ordering case that every squeezed model lands on. Quoting Σm_ν as a success would be
quoting a number nothing can check.

**What is distinctive is m_ββ, because it is sensitive to m₁ itself and the sum is not.** At m₁ = 0
the window is [1.48, 3.69] meV; at the model's m₁ = 2.25 meV it is [0.04, 5.30] meV. The ceiling
rises 44% and the floor nearly collapses, and the observational consequence is clean: **minimal
ordering puts the entire window below nEXO's best reach, while this model puts about 11% of it
above.** That is the difference your program can actually see, and it is this sector's only claim
that earns the word distinctive.

On provenance, including the part that counts against us — the prediction was registered before the
deciding data (2026-07-07, git-timestamped). But the mechanism now offered for *why* the model picks
this branch — the tenth-channel mass relation — was worked out after DESI's preference for a low sum
was known, and our own registry carries it under a post-hoc flag for exactly that reason. It earns
no derivation credit until it produces a new falsifiable consequence beyond the registered number.
The registry entry itself is also narrower than the claim above: it does not select the ordering,
and it was written with the causal arrow pointing the other way. All of that is in the repository
under P-2026-012 and ANN-2026-025, and you should read those rather than take this paragraph's word
for it.

## The cancellation floor, and how thin it is

The lightest mass is the model's dark-energy scale, m₁ = ρ_Λ¼. The observed value is 2.25 meV, known
to **0.45%** — Planck's 1.8% on ρ_Λ, quartered by the fourth root — and the model's derived chain
lands at 2.2599, which is +0.44%, i.e. inside one standard deviation of the observation. The sum does
not notice: Σm_ν = 61.34 to 61.37 meV across that range, which is why it is quoted as 61.4. The
effective mass is less forgiving, and the floor is where the difference shows.

The three contributions, with NuFIT-class mixings, across the observation's own range:

| term | m₁ = 2.2399 meV (−1σ) | m₁ = 2.25 meV (observed) | m₁ = 2.2599 meV (derived) |
|---|---|---|---|
| \|U_e1\|² m₁ | 1.52 meV | 1.52 meV | 1.53 meV |
| \|U_e2\|² m₂ | 2.67 meV | 2.67 meV | 2.67 meV |
| \|U_e3\|² m₃ | 1.10 meV | 1.10 meV | 1.10 meV |
| **floor** | **0.050 meV** | **0.044 meV** | **0.038 meV** |
| ceiling | 5.295 meV | 5.302 meV | 5.310 meV |

The floor moves by about a quarter across that range while the ceiling moves by 0.3%. The window is
therefore quoted as [0.04, 5.3], and every conclusion below turns on the ceiling, which is stable.

A floor exists at all only because the middle term exceeds the other two combined — 2.67 against
2.62. That margin is 0.05 meV on terms of order 2, so the three phasors barely fail to close a
triangle, and complete cancellation is barely impossible. Above m₁ = **2.324 meV** the triangle
closes, the floor is exactly zero, and complete cancellation becomes allowed — a threshold the
model's own derived anchor sits 2.8% below, which is six standard deviations of the observation
away. The floor thins across the range the scale is known to, but it does not vanish inside it.

So the honest statement is that the floor is around 0.04 meV, and that it is a coincidence of
scales rather than a protected feature. Nothing observable rides on it: it is two orders below any
experiment's reach on any timeline, and every conclusion below turns on the ceiling instead, which
the anchor barely moves.

The consequence may be the most distinctive thing this model says to your field: because the
near-cancellation amplifies small changes in m₁, **m_ββ here is an unusually sharp probe of the
dark-energy scale.**

## The overlay: where this model sits against your program

Projected 10-year sensitivities, each span being the nuclear-matrix-element range rather than an
experimental uncertainty, against the model's window of [0.04, 5.30] meV:

| experiment | isotope | projected m_ββ reach | vs the model's 5.30 meV ceiling |
|---|---|---|---|
| **nEXO** | ¹³⁶Xe | **4.7 – 20.3 meV** | **overlaps at 4.7–5.3 meV** |
| LEGEND-1000 | ⁷⁶Ge | 9 – 21 meV | entirely above; cannot reach |
| CUPID | ¹⁰⁰Mo | 12 – 34 meV | entirely above; cannot reach |

nEXO is the only one of the three that can touch this model, and only if the ¹³⁶Xe matrix element
falls at the favourable end. Taking the Majorana phases flat — the usual convention, and a choice
rather than a result — the model exceeds 4.7 meV about **10.8%** of the time.

The part that concerns your own work directly: if barium tagging reaches the factor-of-four
half-life gain your group has projected, the reach improves by √4 = 2 in m_ββ, from 4.7 to roughly
**2.35 meV**. On this model that moves the probability of a signal from 10.8% to **69%** — more
than a six-fold improvement, and the difference between a long shot and a likely detection.

But it costs discrimination. Minimal
normal ordering — the m₁ = 0 case, the generic expectation — has its own window of [1.48, 3.69] meV
and exceeds 2.35 meV **63.7%** of the time. Against this model's 69%, a tagged detection near 2.35
separates almost nothing:

| reach | this model | minimal ordering | separates? |
|---|---|---|---|
| 4.7 meV (baseline nEXO) | 10.8% | **0%** | **yes, completely** |
| 2.35 meV (with Ba tagging) | 69.1% | 63.7% | no |

**The discriminating band is 3.69 to 5.30 meV** — above minimal ordering's hard ceiling, below this
model's. Minimal ordering *cannot* produce a signal there at any phases; this model lands there
**31.7%** of the time. And of the 10.8% of cases where baseline nEXO sees anything at all, **all of
it** falls in that band.

So the two capabilities do different jobs. **Barium tagging makes the test likely; the baseline
machine makes it decisive.** A tagged detection at 2 meV would be a triumph for the field and would
barely move this model's posterior. A baseline detection at 4.5 meV would be a result no
minimal-ordering scenario can accommodate. If that distinction is useful to how the upgrade gets
argued for, it is yours to use.

## Why the cosmological squeeze relaxes

ΛCDM-conditional analyses increasingly squeeze Σm_ν toward and below the 59 meV oscillation floor —
the "negative neutrino mass" tension. This model replaces CDM+Λ with one fluid, ΛCDM-degenerate at
background and linear level and verified numerically to five decimals, plus the electron-mass shift
at recombination in the Hart–Chluba implementation. Varying-m_e has independent support, and it is
worth stating at its real strength rather than its most flattering: the Planck-era analysis that
opened the line found **3.5σ** (Hart & Chluba 2020), while the recent fit on ACT DR6 + DESI DR2
returns m_e/m_e₀ = 1.0081 ± 0.0046 — a **1.8σ** preference — and a second recent analysis on those
stacks concludes that varying m_e cannot fully resolve the tension once DESI DR2 BAO is included.
**And the field's own common-framework comparison does not favour this mechanism class:** across
fourteen models in one pipeline, early dark energy scores −ΔAIC 23.40 and leaves a residual 2.51σ,
against varying m_e's 12.58 and 4.25σ (Schöneberg et al. 2026). We are not the best-performing
route to H₀ on the current scoreboard, and this letter's case does not rest on our being so.

The shifted calibration frees the damping-tail budget that ΛCDM fits spend against the neutrino
mass, so model-conditional fits leave Σm_ν near its physical value: the same data, room instead of
squeeze. If this model class is right, the meV-scale m_ββ frontier is physically meaningful rather
than cosmologically foreclosed.

## Status

The model's fits match or modestly outperform ΛCDM on Planck 2018 + ACT DR6 + SPT-3G + BAO +
Pantheon+SH0ES, at H₀ ≈ 69.9 — sound-horizon-driven, and holding with the SH0ES calibration
included and pulling the other way. That figure is provisional: the chains that underwrite it are
still being brought to convergence under a corrected sampler configuration, and the value may shift.

**The current test, with a caveat we found while checking it.** The zero-parameter evidence
comparison freezes amplitude, tilt, coupling and transition epoch in advance, against ΛCDM at full
freedom, so any stated number being wrong collapses the model's own evidence. Nested sampling was
started on that configuration and then stood down on this hardware: the schedule is hundreds of days
to a first checkpoint, so the nested number waits for cluster time. Until then the comparison is
carried by a Laplace-from-MCMC estimate, and the chains that feed it are the critical path. The
caveat is the transition epoch. It was frozen at a profiled value rather than at the model's own
onset identity, and the two differ by 0.053 dex; because the onset redshift goes as √m, that
corresponds to a dark fluid mass about 28% from the one the rest of the model uses. **So the
configuration being graded is a point near the model rather than the model's stated one**, and its
result will need reading in that light. We would rather tell you that than have it turn up later.

For validation: an exact ΛCDM null test at five decimals, gauge invariance, a precision-stability
battery. The deepest structural claim, the medium's reality, is carried as an open assumption
rather than asserted. Entry points for a technical reader: THREE_EQUATIONS, DEPENDENCY_TREE,
PREREGISTERED_PREDICTIONS (50+ numbered bets), FAILURES_LEDGER.

For context: vacuum condensates setting matter's parameters is not exotic — roughly 99% of ordinary
mass is QCD-condensate binding. This model adds one more condensate and asks whether it reads into
the remaining Yukawa percent at the 10⁻² level during one epoch.

**BBN is the model's worst column**, and it is deliberately absent from the fit list above. The
electron-mass shift is on during nucleosynthesis and the sector is rigid — every input derived or
measured — so the model cannot coach its witness. It comes out net adverse. Y_p sits +1.3 to +2.0σ
above Aver, and +3.8 to +4.4σ against EMPRESS; the helium civil war is unresolved and not ours to
settle. D/H is predicted at 2.407–2.463×10⁻⁵ against Cooke's 2.527 ± 0.030, which is −2.5 to −1.4σ
on the full budget (observational ±0.030 ⊕ PRIMAT post-LUNA nuclear theory ±0.037). Both ranges are
the span of one committed input, the genesis dilution ζ = T_dark/T_γ ∈ [0.25, 0.35], which the model
uses everywhere it appears and which CMB-S4 will measure directly through ΔN_eff = 0.06–0.24.
*(The next section decomposes the nucleosynthesis physics at ζ's own baseline, before the dilution's
dark-radiation contribution is added, where the same prediction reads 2.387×10⁻⁵. The two figures
are the same calculation at two stages, not two predictions.)*

The joint is decided by a nuclear-code systematic outside our control: PRIMAT gives D/H = 2.439
where PArthENoPE gives 2.51–2.54, a 3.5% spread that is 2.3× the quoted nuclear error. Carrying
none of it, the joint is p = 0.02–0.08, rejected to marginal at 5%; carrying half, p = 0.07–0.11;
carrying all of it, p = 0.12–0.21. The model sits on the low side of the deuterium fork — a
self-adverse position, registered before its referee (P-2026-027, a dark-ages radio measurement of
primordial D/H at 327 MHz, free of astration and quasar optics).

## Where the deuterium deficit comes from

Taking that column apart changes what it is a statement about. Below, the chain is shown at ζ's
baseline — before the dilution's dark-radiation contribution is added, which is what carries 2.387
up into the 2.407–2.463 range quoted above. The prediction is built in two steps from an in-house
ΛCDM control run, same code and same data:

| step | D/H ×10⁻⁵ | vs Cooke (standing ±0.0476) |
|---|---|---|
| ΛCDM control | 2.420 | −2.25σ |
| the model's baryon density, 1.1% higher | 2.372 | −3.25σ |
| the dyad's nucleosynthesis window, +0.645% | 2.387 | −2.94σ |

**The new physics acting during nucleosynthesis helps.** The electron-mass ramp switches on at
the derived T_c = 177.10 keV — the abundances are insensitive at the percent level, so nothing
below turns on the exact figure — and raises D/H by 0.645%, worth +0.31σ toward the measurement. Grafted onto the ΛCDM
control alone it would give −1.93σ, better than the control's −2.25σ — though that is a
decomposition rather than an available configuration, since the window and the baryon shift are the
same ε acting at two epochs and the model cannot have one without the other. The point it
establishes is only that **the deficit is not manufactured in the nuclear sector.**

**The deficit is imported from the CMB fit.** Fitting the microwave background with a varying
electron mass returns a baryon density 1.1% above the control, and deuterium is the most
baryon-sensitive abundance in the network — the production run gives d ln(D/H)/d ln ω_b = −1.66 — so
that 1.1% becomes a 1.8% deuterium loss: three times the window's help, and opposite in sign.

**That baryon shift is the same one that buys the Hubble result.** The two arrive together along one
degeneracy direction, which fixes an exchange rate of **0.59σ of deuterium per km/s/Mpc of H₀**.
That rate is a secant between two computed points — the model's fit and the control, 1.7 km/s/Mpc
apart — not a slope measured along the degeneracy, so it is trustworthy across that interval and an
extrapolation outside it. Inside it: reaching parity with the ΛCDM control costs 1.17 of the
1.7 km/s/Mpc, i.e. **69% of the H₀ relief**. Centring deuterium on Cooke would take roughly three
times the measured interval, which indicates the direction and scale of the trade rather than a
landing point.

The deuterium tension and the Hubble result are therefore one trade rather than two problems, and
any real cure has to be orthogonal to that degeneracy — it must raise D/H at fixed baryon density
and fixed electron mass. That test sorts the candidates. Expansion-rate levers all fail it, since
they move helium and deuterium the same way while the two need opposite moves. Two survive. A boost
confined below T_c is the right shape but comes out 8–33× too weak on the model's own
degree-of-freedom counting. Late photodissociation of ⁴He is the cheapest cure available — breaking
1.7×10⁻⁵ of the helium supplies enough deuterium to centre the row while moving Y_p by 0.001σ — but
an electromagnetic repair requires a state of mass ≳ 20 MeV, lifetime 10⁶–10⁸ s, and abundance carrying ~30 eV per
hydrogen, which the model's field content does not contain, for specific reasons rather than
accidental ones.

## Two smaller items

Where the lightest mass comes from: oscillations fix the two splittings but not the
absolute floor, and in this model that floor is not fitted — it is medium-sourced. The lightest
neutrino mass reads m₁ = κ_m·ρ_inf¼ with κ_m ≈ 1: the dark-energy scale does not happen to coincide
with the lightest neutrino mass, it **sets** it. Σm_ν = 61.4 meV then follows from that floor plus
the measured splittings.

Three qualifications, because this is the claim most worth attacking. **First**, the model does not
derive the value 2.25 meV. That is its own open problem — the dark-energy-value problem — so the
claim is not that the number is explained but that **one un-derived number does two jobs that
standard cosmology treats as unrelated.** What is predictive is the relation: given the measured
dark-energy density, the sum and the ordering follow with nothing further to adjust. **Second**,
κ_m ≈ 1 is where the residual freedom sits — the relation's form comes from the model's channel
counting, its O(1) coefficient is not independently pinned. **Third**, this is deliberately not a
mass-varying-neutrino (MaVaN) construction; those founder on the Afshordi–Zaldarriaga–Kohri
instability, and this model avoids it because m_ν is set by a frozen lepton-number-breaking vacuum
expectation value rather than by the rolling dark-energy field, so the rolling does not vary the
neutrino mass. A reader discounting this claim should discount it at the first two points, and
nowhere else.

A framing you may enjoy: in this model's internal language, 0νββ decides whether lepton number
is a collateralized charge — like electric charge, with a field enforcing it — or an unenforced
accounting identity, with Majorana neutrinos the mechanism by which such an identity defaults. Your
detector is auditing whether L's debt has a bank.

## The ask

**(a)** Whether the meV-window prediction is in the form most useful to the 0νββ community —
particularly the two-sided kill structure, and whether the floor's thinness is something the field
wants stated up front or regards as obvious.

**(b)** A critical eye on the BBN sector, where the model is weakest. Three questions rather than
one: whether the PRIMAT/PArthENoPE deuterium spread should be carried as a theory error, which is
the difference between rejection at 5% and comfort; whether the decomposition above is the right
reading of the deficit — that is, whether a tension living in the baryon density and trading against
H₀ at a fixed rate should be argued as a BBN problem at all, or as a statement about where on the
m_e–ω_b degeneracy the data wants to sit; and whether the dark-ages radio referee is a real path.

**(c)** Two numbers we took from the outside and you own from the inside: whether 4.7 meV is the
right baseline nEXO reach to plan against at the favourable ¹³⁶Xe matrix element, and whether the
factor-of-four barium-tagging gain should be read as half-life sensitivity (which is how we used it,
giving 2× in m_ββ) or as something else. Every probability above moves with those two, and the
discriminating-band argument in particular is only as good as the 3.69 meV minimal-ordering ceiling
sitting where we have put it.

---

*Claims trace to documented computations: PRTOE_neutrino_sector.md for this sector,
PRTOE_deuterium_row.md for the decomposition, PRTOE_PREREGISTERED_PREDICTIONS.md for the
registered bets, BIBLIOGRAPHY.md for citations.*
