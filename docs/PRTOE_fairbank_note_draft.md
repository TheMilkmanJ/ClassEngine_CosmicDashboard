# Note for Prof. W. Fairbank — what a unified dark-fluid cosmology predicts for 0νββ

*2026-07-19. Plain physics throughout; self-contained.*

## The result in three sentences

In a unified dark-sector cosmology — one superfluid scalar replacing dark matter and dark energy,
plus a single derived 1.2543% early-universe shift of the electron mass (ε = 27α/5π) — the neutrino
sector is an output rather than an input: the model's dark-energy scale ties to the lightest
neutrino mass, giving **Σm_ν = 61.4 meV with normal ordering**. Because the mass mechanism violates
lepton number, **neutrinos must be Majorana, and the 0νββ process is structurally required.** The
corresponding effective mass, with measured splittings and free Majorana phases, is
**m_ββ ∈ [0.02, 5.3] meV, typically ~3.3 meV.**

## What this means for your program

**Your program's entire target range is a kill zone for this model.** That is the blunt version and
it is the reason for writing. The model's ceiling is m_ββ = 5.3 meV; nEXO, LEGEND-1000 and CUPID are
aiming at roughly 5–20 meV; current limits sit at 28–180 meV depending on the matrix elements. So
**any confirmed detection by the current or next generation falsifies this model outright** — there
is no corner of your accessible parameter space where a signal and this model coexist. No claimed
detection exists there now, so it is a forward bet rather than a retrodiction.

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

**The claim was registered before the deciding data**, as a numbered, git-timestamped entry with a
named killing observation. The timestamps are the provenance and the audit trail is in the
repository.

## The cancellation floor, and how thin it is

The lightest mass is the model's dark-energy scale, m₁ = ρ_Λ¼, and that scale is not pinned tighter
than about 1.5%: three closures in the model supply 2.25, 2.2599, and 2.284 meV. The sum is
insensitive to the choice — Σm_ν = 61.35 to 61.40 meV, which is why it is quoted as 61.4. The
effective mass is not, and the floor is where the difference shows.

The three contributions, with NuFIT-class mixings, at the two ends of that range:

| term | m₁ = 2.25 meV | m₁ = 2.284 meV |
|---|---|---|
| \|U_e1\|² m₁ | 1.52 meV | 1.55 meV |
| \|U_e2\|² m₂ | 2.67 meV | 2.68 meV |
| \|U_e3\|² m₃ | 1.10 meV | 1.10 meV |
| **floor** | **0.044 meV** | **0.023 meV** |
| ceiling | 5.30 meV | 5.33 meV |

A floor exists at all only because the middle term exceeds the other two combined — 2.67 against
2.62 at the low anchor. That margin is 0.05 meV on terms of order 2, so the three phasors barely
fail to close a triangle, and complete cancellation is barely impossible. **Moving m₁ by 1.5%
across the model's own range halves the floor.** Above m₁ = **2.324 meV** the triangle closes, the
floor is exactly zero, and complete cancellation becomes allowed — that threshold is 1.7% above the
highest anchor the model carries.

So the honest statement is that the floor is 0.02–0.04 meV, and that it is a coincidence of scales
rather than a protected feature.

The consequence may be the most distinctive thing this model says to your field: because the
near-cancellation amplifies small changes in m₁, **m_ββ here is an unusually sharp probe of the
dark-energy scale.**

## Why the cosmological squeeze relaxes

ΛCDM-conditional analyses increasingly squeeze Σm_ν toward and below the 59 meV oscillation floor —
the "negative neutrino mass" tension. This model replaces CDM+Λ with one fluid, ΛCDM-degenerate at
background and linear level and verified numerically to five decimals, plus the electron-mass shift
at recombination in the Hart–Chluba implementation. Varying-m_e is independently preferred at
2–3.6σ by other groups on Planck+ACT+DESI stacks.

The shifted calibration frees the damping-tail budget that ΛCDM fits spend against the neutrino
mass, so model-conditional fits leave Σm_ν near its physical value: the same data, room instead of
squeeze. If this model class is right, the meV-scale m_ββ frontier is physically meaningful rather
than cosmologically foreclosed.

## Status

**Fits.** The model matches or modestly outperforms ΛCDM on Planck 2018 + ACT DR6 + SPT-3G + BAO +
Pantheon+SH0ES, at H₀ ≈ 69.9 — sound-horizon-driven, and holding with the SH0ES calibration
included and pulling the other way. That figure is provisional: a refined likelihood treatment is
running now and the value may shift.

**The current test.** A zero-parameter evidence run is in progress, with the model's amplitude,
tilt, coupling, and transition epoch all stated in advance — derived or profiled, statuses public —
against ΛCDM at full freedom. Any stated number wrong collapses the model's own evidence.

**Validation.** Exact ΛCDM null test at five decimals, gauge invariance, precision-stability
battery. The deepest structural claim, the medium's reality, is carried as an open assumption
rather than asserted. Entry points for a technical reader: THREE_EQUATIONS, DEPENDENCY_TREE,
PREREGISTERED_PREDICTIONS (50+ numbered bets), FAILURES_LEDGER.

**Context.** Vacuum condensates setting matter's parameters is not exotic — roughly 99% of ordinary
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

| step | D/H ×10⁻⁵ | vs Cooke |
|---|---|---|
| ΛCDM control | 2.420 | −1.90σ |
| the model's baryon density, 1.1% higher | 2.372 | −2.75σ |
| the dyad's nucleosynthesis window, +0.645% | 2.387 | −2.49σ |

**The new physics acting during nucleosynthesis helps.** The electron-mass ramp switches on at
T_c ≈ 179 keV and raises D/H by 0.645%, worth +0.27σ toward the measurement. Grafted onto the ΛCDM
control alone it would give −1.63σ, better than the control's −1.90σ — though that is a
decomposition rather than an available configuration, since the window and the baryon shift are the
same ε acting at two epochs and the model cannot have one without the other. The point it
establishes is only that **the deficit is not manufactured in the nuclear sector.**

**The deficit is imported from the CMB fit.** Fitting the microwave background with a varying
electron mass returns a baryon density 1.1% above the control, and deuterium is the most
baryon-sensitive abundance in the network — the production run gives d ln(D/H)/d ln ω_b = −1.83 — so
that 1.1% becomes a 2.0% deuterium loss: three times the window's help, and opposite in sign.

**That baryon shift is the same one that buys the Hubble result.** The two arrive together along one
degeneracy direction, which fixes an exchange rate of **0.50σ of deuterium per km/s/Mpc of H₀**.
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
it requires a state of mass ≳ 20 MeV, lifetime 10⁶–10⁸ s, and abundance carrying ~30 eV per
hydrogen, which the model's field content does not contain, for specific reasons rather than
accidental ones.

## Two smaller items

**Where the lightest mass actually comes from.** Oscillations fix the two splittings but not the
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

**A framing you may enjoy.** In this model's internal language, 0νββ decides whether lepton number
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

**(c)** Any interest in the model-vs-ΛCDM comparison rerun with the nEXO/LEGEND/CUPID sensitivity
bands overlaid on the m_ββ window.

---

*Claims trace to documented computations: PRTOE_neutrino_sector.md for this sector,
PRTOE_deuterium_scar.md for the decomposition, PRTOE_PREREGISTERED_PREDICTIONS.md for the
registered bets, BIBLIOGRAPHY.md for citations.*
