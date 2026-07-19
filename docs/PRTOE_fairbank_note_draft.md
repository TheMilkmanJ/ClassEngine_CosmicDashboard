# Note for Prof. W. Fairbank — What a unified dark-fluid cosmology predicts for 0νββ

*(DRAFT v0.4, 2026-07-19. Plain physics throughout; self-contained.)*

> **CIRCULATION GATE — one item, open.** This note does not go out until it closes.
>
> **The zero-parameter evidence verdict.** The run has been sampling since 2026-07-18
> (PolyChord, 400 live points, matched to a ΛCDM twin so the evidence ratio is valid). Its
> completion horizon is itself under review, so this gate may hold the note for a long time, and
> that is the honest expectation rather than a delay.
>
> **This gate also covers the fit record.** The H₀ ≈ 69.9 quoted below was measured on chains that
> predate a likelihood correction: the helium fraction fed to the recombination code was ΛCDM's
> rather than the model's own, leaving the free-electron fraction n_e ∝ (1−Y_p) about 0.27% off in
> precisely the place this model's H₀ mechanism operates. **That defect is fixed** — the model's
> measured BBN response is now wired into both the `YHe` value and the BBN prior across all
> evidence configurations, and the running job carries the fix. What has not happened yet is the
> re-measurement. Until the running job reports, treat H₀ ≈ 69.9 as the pre-correction number and
> expect it to move.
>
> *(Citations were checked against the bibliography on 2026-07-19; the one gap — the PArthENoPE
> reference underwriting the deuterium theory error — is closed.)*

## The result in three sentences

In a unified dark-sector cosmology — one superfluid scalar replacing dark matter and
dark energy, plus a single **derived** 1.2543% early-universe shift of the electron mass (ε = 27α/5π) — the
neutrino sector is an output, not an input: the model's dark-energy scale ties to the
lightest neutrino mass, giving **Σm_ν = 61.4 meV with normal ordering**, and because
the mass mechanism violates lepton number, **neutrinos must be Majorana: the 0νββ
process is structurally required.** The corresponding effective mass, with measured
splittings and free Majorana phases, is
**m_ββ ∈ [0.04, 5.3] meV (typically ~3.3 meV).**

## What this means for your program — stated without varnish

1. **The mechanism is guaranteed; the rate is honestly small.** This model cannot exist
 without the 0νββ process — but it predicts the effective mass *below* current
 ton-scale reach, in the normal-ordering meV regime. We are not promising your
 experiment a signal; we are telling you what universe it is searching in if this
 model class is right. A null at any given sensitivity does not kill the model (the
 phase-cancellation floor near 0.04 meV is stated, not hidden);
 **a demonstrated Dirac nature does kill it — cleanly and permanently.**
2. **A two-sided kill on the mass scale.** A confirmed detection well ABOVE ~5.3 meV
 falsifies this model outright (checked against the record: no claimed detection
 exists there — this is a forward bet, not a retrodiction). From the other side,
 DESI-era cosmology is already brushing the prediction: a robust Σm_ν > ~70 meV, or
 inverted ordering from oscillations, kills the stack. Exposed both directions, on
 purpose.
3. **The claim is registered, not retrofit.** Normal ordering, Σm_ν = 61.4 meV — a
 numbered, git-timestamped registry entry with a named killing observation, recorded
 before the deciding data. The registry's timestamps are the provenance; the full
 audit trail is in the repository for any reader who wants it.

## The cancellation floor is real but not protected — the part we think is worth your time

The three contributions to m_ββ, on the model's anchor m₁ = ρ_Λ¼ = 2.25 meV and NuFIT-class
mixings, are

| term | value |
|---|---|
| \|U_e1\|² m₁ | 1.52 meV |
| \|U_e2\|² m₂ | 2.67 meV |
| \|U_e3\|² m₃ | 1.10 meV |

The middle term slightly exceeds the other two combined (2.67 against 2.62). That inequality is
the *only* reason a floor exists: the three phasors cannot close a triangle, so complete
cancellation is impossible and m_ββ ≥ 0.04–0.06 meV whatever the Majorana phases do.

**The margin is 0.05 meV, on terms of order 2.** We would rather you hear that from us than find
it. The floor disappears entirely — exact cancellation becomes allowed — once m₁ exceeds
**2.324 meV**, just 3.3% above the model's anchor. The model carries three recorded values for the
dark-energy scale depending on which closure supplies it (2.25, 2.2599, 2.284 meV); all three sit
below the threshold, so the floor survives on every number the model actually uses — but the
highest of them clears it by 1.7%. The floor is not structurally protected. A modest upward
revision of the dark-energy scale erases it and makes complete cancellation allowed.

The useful consequence for an experiment: in this model **m_ββ is an unusually sharp probe of the
dark-energy scale**, because the near-cancellation amplifies small changes in m₁. That is a strange
sentence to write, and it is the most distinctive thing this model says to your field.

## Why the cosmological squeeze relaxes (mechanism, not tuning)

ΛCDM-conditional analyses increasingly squeeze Σm_ν toward and below the 59 meV
oscillation floor (the "negative neutrino mass" tension). This model replaces CDM+Λ
with one fluid (ΛCDM-degenerate at background and linear level — verified numerically
to five decimals) plus the electron-mass shift at recombination (the Hart–Chluba
implementation; varying-m_e is independently preferred at 2–3.6σ by other groups on
Planck+ACT+DESI stacks). The shifted calibration frees the damping-tail budget that
ΛCDM fits spend against the neutrino mass: model-conditional fits leave Σm_ν healthy
near its physical value — the same data, room instead of squeeze. If this model class
is right, the meV-scale m_ββ frontier is physically meaningful rather than
cosmologically foreclosed.

## The honest status card

- **Fit record**: matches or modestly outperforms ΛCDM on Planck 2018 + ACT DR6 +
 SPT-3G + BAO + Pantheon+SH0ES at H₀ ≈ 69.9 (sound-horizon-driven; holds with
 the SH0ES calibration included and pulling the other way). **Read this number with the
 circulation gate above**: it predates the likelihood correction and is being re-measured now.
 **BBN is deliberately not in that list — it is the model's worst column, and it is stated
 separately below.**
- **The BBN cost, stated plainly.** The electron-mass shift is on during nucleosynthesis, and
 the sector is rigid — every input derived or measured, so the model cannot coach its witness.
 It comes out **net adverse**: Y_p sits **+1.3 to +2.0σ** above Aver (**+3.8 to +4.4σ** vs
 EMPRESS — the helium civil war is unresolved and not ours to settle), and D/H is predicted at
 **2.407–2.463×10⁻⁵** against Cooke's 2.527 ± 0.030 — **−2.5 to −1.4σ** on the full budget
 (observational ±0.030 ⊕ PRIMAT post-LUNA nuclear theory ±0.037). Both ranges are the span of
 one committed input, the genesis dilution ζ = T_dark/T_γ ∈ [0.25, 0.35], which the model uses everywhere it
 appears and which CMB-S4 will measure directly through ΔN_eff = 0.06–0.24. **The joint is
 decided by a nuclear-code systematic we do not control:** PRIMAT gives D/H = 2.439 where
 PArthENoPE gives 2.51–2.54, a 3.5% spread that is 2.3× the quoted nuclear error. Fold none of
 it and the joint is **p = 0.02–0.08 — rejected to marginal at 5%**; fold half and p = 0.07–0.11;
 fold all of it and p = 0.12–0.21. **We quote the range, not the flattering end.** The dyad sits on the LOW side of the
 deuterium fork — a self-adverse bet, registered before the referee (P-2026-027, a dark-ages
 radio measurement of primordial D/H at 327 MHz, free of astration and quasar optics).
- **The current test**: a zero-parameter evidence run is in progress — the model's
 amplitude, tilt, coupling, and transition epoch all STATED in advance (derived or
 profiled; statuses public), against ΛCDM at full freedom. Full exposure: any stated
 number wrong collapses the model's own evidence.
- **Validation**: exact ΛCDM null test (5-decimal reproduction), gauge invariance,
 precision-stability battery — committed.
- **Internal validation**: a continuous in-repo adversarial review with a maintained
 audit trail. The deepest structural claim — the medium's reality —
 is tracked as an open assumption, not asserted. Entry points for a technical reader:
 THREE_EQUATIONS, DEPENDENCY_TREE, PREREGISTERED_PREDICTIONS (40+ numbered bets),
 FAILURES_LEDGER.
- **Mainstream anchor**: vacuum condensates setting matter's parameters is not exotic —
 ~99% of ordinary mass is QCD-condensate binding. This model adds one more condensate
 and asks whether it reads into the remaining (Yukawa) percent at the 10⁻² level
 during one epoch.

## Where the deuterium deficit actually comes from

Since we are asking you to look hardest at the BBN column, here is what taking it apart shows —
the answer was not what we expected, and it changes what kind of help is useful.

The prediction is built in two steps from an in-house ΛCDM control run, same code, same data:

| step | D/H ×10⁻⁵ | vs Cooke |
|---|---|---|
| ΛCDM control | 2.420 | −1.90σ |
| the model's baryon density, 1.1% higher | 2.372 | −2.75σ |
| the dyad's nucleosynthesis window, +0.645% | 2.387 | −2.49σ |

**The new physics acting during nucleosynthesis helps.** The electron-mass ramp switches on at
T_c ≈ 179 keV and raises D/H by 0.645%, worth +0.27σ toward the measurement. Grafted onto the
ΛCDM control alone it would give −1.63σ — *better* than the control's −1.90σ.

**The deficit is imported from the CMB fit.** Fitting the microwave background with a varying
electron mass returns a baryon density 1.1% above the control, and deuterium is the most
baryon-sensitive abundance in the network — the production run gives d ln(D/H)/d ln ω_b = −1.83 —
so that 1.1% becomes a 2.0% deuterium loss: three times the window's help, opposite in sign.

**And that baryon shift is the same one that buys the Hubble result.** The two arrive together
along one degeneracy direction, which fixes an exchange rate: **0.50σ of deuterium per km/s/Mpc of
H₀**. Reaching mere parity with the ΛCDM control would cost 1.17 of the 1.7 km/s/Mpc; centring
deuterium on Cooke would cost all of it and land H₀ at 64.9.

So the deuterium tension and the Hubble result are one trade, not two problems. The consequence we
did not anticipate: **any real cure must be orthogonal to that degeneracy** — it has to raise D/H
at fixed baryon density and fixed electron mass. That test sorts the candidates. Expansion-rate
levers all fail it, because they move helium and deuterium the same way and the two need opposite
moves. Two survive: a boost confined below T_c, the right shape but 8–33× too weak on the model's
own degree-of-freedom counting; and late photodissociation of ⁴He, the cheapest cure on the books —
breaking 1.7×10⁻⁵ of the helium supplies enough deuterium to centre the row while moving Y_p by
0.001σ — which needs a state of mass ≳ 20 MeV, lifetime 10⁶–10⁸ s, and abundance carrying ~30 eV
per hydrogen. The model's current field content does not contain one, for specific reasons rather
than accidental ones.

We flag this because it changes ask (b) from "help, we are weak here" into a sharper question.

## Two smaller items that may interest you

1. **A scale coincidence, flagged at coincidence grade**: the model's dark-energy floor
 has ρ_∞^(1/4) ≈ 2.25 meV — the expected mass of the lightest neutrino under normal
 ordering. Known attempts to mechanize the DE–ν coincidence (MaVaN) failed to
 instabilities; we log the coincidence, use the tie that produces the 61.4, and
 overclaim nothing.
2. **A framing you may enjoy**: in this model's internal language, 0νββ is the
 experiment that decides whether lepton number is a *collateralized* charge (like
 electric charge, with a field enforcing it) or an unenforced accounting identity —
 Majorana neutrinos being the mechanism by which an unenforced identity defaults.
 Your detector is auditing whether L's debt has a bank.

## The ask

(a) Your read on whether the meV-window prediction is presented in the form most useful
to the 0νββ community — especially the two-sided kill structure, and whether the floor's
fragility is something the field wants stated up front or regards as obvious;

(b) **a critical eye on the BBN sector, which is where we are weakest.** Three questions rather
than one: whether the PRIMAT/PArthENoPE deuterium spread should be carried as a theory error
(the difference between this model being rejected at 5% on BBN and being comfortable there);
whether the decomposition above is the right way to read the deficit — that is, whether a tension
which lives in the baryon density and trades against H₀ at a fixed rate should be argued as a BBN
problem at all, or as a statement about where on the m_e–ω_b degeneracy the data actually wants to
sit; and whether the dark-ages radio referee is a real path;
(c) any interest in the model-vs-ΛCDM comparison rerun with the nEXO/LEGEND/CUPID
sensitivity bands overlaid on the m_ββ window.

*(All claims traceable to documented computations: PRTOE_neutrino_sector.md for this sector; PRTOE_deuterium_scar.md for the decomposition; PRTOE_PREREGISTERED_PREDICTIONS.md for the frozen bets; BIBLIOGRAPHY.md for verified citations. The closed-form numbers are recomputed on every commit by scripts/audit_math_pass.py.)*
