# Note for Prof. W. Fairbank — what a unified dark-fluid cosmology predicts for 0νββ

*2026-07-19. Plain physics throughout; self-contained.*

## The result in three sentences

In a unified dark-sector cosmology — one superfluid scalar replacing dark matter and dark energy,
plus a single derived 1.2543% early-universe shift of the electron mass (ε = 27α/5π) — the neutrino
sector is an output rather than an input: the model's dark-energy scale ties to the lightest
neutrino mass, giving **Σm_ν = 61.4 meV with normal ordering**. Because the mass mechanism violates
lepton number, **neutrinos must be Majorana, and the 0νββ process is structurally required.** The
corresponding effective mass, with measured splittings and free Majorana phases, is
**m_ββ ∈ [0.04, 5.3] meV, typically ~3.3 meV.**

## What this means for your program

**The mechanism is guaranteed; the rate is small.** The model cannot exist without 0νββ, but it
puts the effective mass below current ton-scale reach, in the normal-ordering meV regime. We are
not promising your experiment a signal — we are describing the universe it is searching in if this
model class is right. A null at any given sensitivity does not kill the model. A demonstrated Dirac
nature kills it cleanly and permanently.

**The mass scale is a two-sided target.** A confirmed detection well above ~5.3 meV falsifies the
model outright; no claimed detection exists there, so this is a forward bet rather than a
retrodiction. From the other side, DESI-era cosmology is already brushing the prediction — a robust
Σm_ν > ~70 meV, or inverted ordering from oscillations, ends it.

**The claim was registered before the deciding data**, as a numbered, git-timestamped entry with a
named killing observation. The timestamps are the provenance and the audit trail is in the
repository.

## The cancellation floor, and how thin it is

The three contributions to m_ββ, on the model's anchor m₁ = ρ_Λ¼ = 2.25 meV with NuFIT-class
mixings:

| term | value |
|---|---|
| \|U_e1\|² m₁ | 1.52 meV |
| \|U_e2\|² m₂ | 2.67 meV |
| \|U_e3\|² m₃ | 1.10 meV |

The middle term exceeds the other two combined — 2.67 against 2.62 — and that inequality is the
only reason a floor exists. The three phasors cannot close a triangle, so complete cancellation is
impossible and m_ββ ≥ 0.04 meV whatever the Majorana phases do.

The margin is 0.05 meV on terms of order 2. The floor disappears entirely, and exact cancellation
becomes allowed, once m₁ exceeds **2.324 meV** — 3.3% above the anchor. The model carries three
recorded values for the dark-energy scale depending on which closure supplies it (2.25, 2.2599,
2.284 meV); all three sit below that threshold, the highest by 1.7%. So the floor holds on every
number the model uses, and it is one modest revision from vanishing.

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
PREREGISTERED_PREDICTIONS (40+ numbered bets), FAILURES_LEDGER.

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

The joint is decided by a nuclear-code systematic outside our control: PRIMAT gives D/H = 2.439
where PArthENoPE gives 2.51–2.54, a 3.5% spread that is 2.3× the quoted nuclear error. Carrying
none of it, the joint is p = 0.02–0.08, rejected to marginal at 5%; carrying half, p = 0.07–0.11;
carrying all of it, p = 0.12–0.21. The model sits on the low side of the deuterium fork — a
self-adverse position, registered before its referee (P-2026-027, a dark-ages radio measurement of
primordial D/H at 327 MHz, free of astration and quasar optics).

## Where the deuterium deficit comes from

Taking that column apart changes what it is a statement about. The prediction is built in two steps
from an in-house ΛCDM control run, same code and same data:

| step | D/H ×10⁻⁵ | vs Cooke |
|---|---|---|
| ΛCDM control | 2.420 | −1.90σ |
| the model's baryon density, 1.1% higher | 2.372 | −2.75σ |
| the dyad's nucleosynthesis window, +0.645% | 2.387 | −2.49σ |

**The new physics acting during nucleosynthesis helps.** The electron-mass ramp switches on at
T_c ≈ 179 keV and raises D/H by 0.645%, worth +0.27σ toward the measurement. Grafted onto the ΛCDM
control alone it gives −1.63σ, better than the control's −1.90σ.

**The deficit is imported from the CMB fit.** Fitting the microwave background with a varying
electron mass returns a baryon density 1.1% above the control, and deuterium is the most
baryon-sensitive abundance in the network — the production run gives d ln(D/H)/d ln ω_b = −1.83 — so
that 1.1% becomes a 2.0% deuterium loss: three times the window's help, and opposite in sign.

**That baryon shift is the same one that buys the Hubble result.** The two arrive together along one
degeneracy direction, which fixes an exchange rate of **0.50σ of deuterium per km/s/Mpc of H₀**.
Reaching parity with the ΛCDM control would cost 1.17 of the 1.7 km/s/Mpc; centring deuterium on
Cooke would cost all of it and land H₀ at 64.9.

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

**A scale coincidence, carried as a coincidence.** The model's dark-energy floor has
ρ_∞^(1/4) ≈ 2.25 meV, the expected mass of the lightest neutrino under normal ordering. Known
attempts to mechanize the dark-energy–neutrino coincidence (MaVaN) failed to instabilities; we log
the coincidence, use the tie that produces the 61.4, and claim nothing further.

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
