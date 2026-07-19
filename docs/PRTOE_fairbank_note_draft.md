# Note for Prof. W. Fairbank — What a unified dark-fluid cosmology predicts for 0νββ

*(DRAFT v0.3, 2026-07-17. Plain physics throughout; self-contained.)*

> **CIRCULATION GATE — three items, all open. This note does not go out until they close.**
> 1. **The running zero-parameter evidence verdict** — the run is executing (sampling since
>    2026-07-18); its completion horizon is itself under review, so this gate may hold the note
>    for a long time and that is the honest expectation, not a delay.
> 2. **Final citation check.**
> 3. **The quoted fit record must be re-earned.** The H₀ ≈ 69.9 record was obtained with a
>    likelihood that fed CLASS a **ΛCDM helium fraction** rather than the model's own: the
>    `YHe` lambda declares the electron-mass shift and never applies it, leaving n_e ∝ (1−Y_p)
>    **0.27% off** at recombination — in precisely the place this model's H₀ mechanism operates.
>    The BBN prior is blind the same way and undercharges the model by ~1 χ². **The number in
>    this letter is not defensible to a referee until the fit is re-run with the model's own Y_p.**
>    ([PRTOE_CODE_MANIFEST.md](PRTOE_CODE_MANIFEST.md), the theory↔code gap.)

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
 the SH0ES calibration included and pulling the other way). **BBN is deliberately not in
 that list — it is the model's worst column, and it is stated separately below.**
- **The BBN cost, stated plainly.** The electron-mass shift is on during nucleosynthesis, and
 the sector is rigid — every input derived or measured, so the model cannot coach its witness.
 It comes out **net adverse**: Y_p sits **+1.09σ** above Aver (**+3.53σ** vs EMPRESS — the
 helium civil war is unresolved and not ours to settle), and D/H is predicted at
 **2.387×10⁻⁵** against Cooke's 2.527 ± 0.030 — **−2.9σ** on the full budget (observational
 ±0.030 ⊕ PRIMAT post-LUNA nuclear theory ±0.037). **The joint is decided by a nuclear-code
 systematic we do not control:** PRIMAT gives D/H = 2.439 where PArthENoPE gives 2.51–2.54, a
 3.5% spread that is 2.3× the quoted nuclear error. Fold none of it and the joint is
 **χ² = 9.83, p = 0.007 — rejected at 5%**; fold half and p = 0.05; fold all of it and
 p = 0.20. **We quote the range, not the flattering end.** The dyad sits on the LOW side of the
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
to the 0νββ community — especially the two-sided kill structure; 
(b) **a critical eye on the BBN sector, which is where we are weakest** 
— specifically whether the PRIMAT/PArthENoPE deuterium spread should be carried as 
a theory error (which is the difference between this model being rejected at 5% on BBN 
and being comfortable there), and whether the dark-ages radio referee is a real path;
(c) any interest in the model-vs-ΛCDM comparison rerun with the nEXO/LEGEND/CUPID
sensitivity bands overlaid on the m_ββ window.

*(All claims traceable to documented computations: PRTOE_neutrino_sector.md for this
sector; PRTOE_PREREGISTERED_PREDICTIONS.md for the frozen bets; BIBLIOGRAPHY.md for
verified citations.)*
