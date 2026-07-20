# The Hubble Tension: Mechanism, Residual, and the Calibration Question

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*Status: the model's* ***core empirical claim*** *— the one domain built in contact with
the data rather than extended to it. The improvement is measured and evidence-priced; a
zero-free-parameter Bayesian comparison against ΛCDM is running as of this revision.*

---

## 1. The tension

Cepheid-calibrated supernovae (SH0ES): H₀ = 73.0 ± 1.0 km/s/Mpc. ΛCDM fit to the CMB:
67–68.2. The disagreement exceeds 5σ and has survived years of scrutiny on both ends.
ΛCDM's implicit position is that one of the two measurements must be wrong.

## 2. The mechanism

The model adds one number to known physics: a +1.2543% shift of the electron mass, active
in the early universe and switched off by a screening transition at late times. The
electron mass sets recombination's atomic physics; a heavier early electron gives
earlier decoupling, a smaller sound horizon, and a CMB fit that lands at *higher* H₀
without disturbing the acoustic structure (the established varying-m_e degeneracy
[Hart–Chluba 2020; Sekiguchi–Takahashi 2021], here supplied with a physical origin —
the condensate's order parameter, condensing at T_c = 177.10 keV, inactive during the
early stages of nucleosynthesis at production grade).

## 3. Where it lands — stated honestly

- **Same data, same pipeline**: ΛCDM's best fit gives H₀ = 68.2; the model gives
 **69.9**, with the Bayesian evidence favoring the model at ΔlnZ ≈ +2.6 (Laplace
 approximation; past the pre-registered win threshold; graded internally as marginal
 and calibration-conditional pending the full nested-sampling verdict now running).
- **The residual is owned**: 69.9 is not 73.0. The model closes roughly half the
 gap and *refuses* the rest — offered spatial curvature as an escape, the fit declined
 it. The claim is not "SH0ES is fully explained"; it is "the sky prefers a universe
 with this mechanism in it, and the remaining gap is real information about the
 measurements."
- **The reach computation**: an exhaustive audit of every lever the
 model owns — the supernova-standardization channels (computed through synthetic
 photometry; the sign came out *opposite* to the tension, robustly, across 162
 template configurations), the survey-geometry leakage (+0.1–0.3%), and the
 reionization tether (±0.3) — caps the model's account of the *ladder* reading at
 **~70.9–71.3. The model cannot reach 73, and says so.**

## 4. The calibration question (where the residual points)

If the model is right, the Cepheid-calibrated 73.0 carries 2–3 km/s/Mpc of systematics
— and the model was *pre-registered* on that side of the live calibration war: its
first registered prediction called H₀ ∈ [69, 71] for the tip-of-the-red-giant-branch
(TRGB) ladder, and the TRGB program indeed reads **69.8–70.4** [Freedman 2021]. The
structural asymmetry between the two ladders is the known crowding question: Cepheids
are photometered in crowded, dusty galactic disks (neighboring starlight contaminates
the measurement); TRGB uses sparse, clean halo fields. The cleanest rung agrees with
the model's band; the contamination-prone rung reads high; JWST's crowding
re-measurements are the community's own referee on exactly this point.

The model additionally *contributes* a candidate systematic from its own physics: under
its environmental screening reading, supernovae in dense versus sparse hosts carry a
small standardization offset with the observed **SN host mass step's** direction —
graded (the web-scale-gate consistency passes): *subdominant at central
values* (~0.02 mag of the observed 0.05–0.08 mag step, environment-tagged), with the
full-step reading surviving only in one corner of the gate's allowed window — a corner
that simultaneously fixes the Lyman-α forest offset, so DESI's forest cross-calibration
decides between "the mass step is the model's" and "the step is astrophysical." Either
outcome is informative; neither is free.

**Data ethics, on the record**: no dataset is dropped for disagreeing. The evidence
comparisons run in three documented tiers — Cepheid-anchored, anchor-free, and
TRGB-anchored — all published side by side, with the analysis roles declared and
timestamped *before* any evidence value existed.

## 5. Against the field's alternatives

**Against the nearest competitor — the varying-m_e literature — the difference is parameter cost,
not direction.** Hart–Chluba (2018, 2020) and Sekiguchi–Takahashi (2021) established the mechanism,
and the recent ACT DR6 + DESI DR2 analyses (arXiv:2508.09025, arXiv:2606.06495) find varying m_e
preferred at **2–3.6σ**. That is independent support for the direction this model takes, and it
should be read as such rather than as competition. **The difference is that there m_e is a free
phenomenological parameter and here it is not.** The amplitude is derived — ε = c·f̄·α_c = 27α/5π =
1.2543% — and the live evidence run **pins** it at that value (`varying_me = 1.012543`, fixed;
[PRTOE_CODE_MANIFEST.md](PRTOE_CODE_MANIFEST.md)), so the comparison against ΛCDM costs **zero extra
parameters, not +1**.

**And the honest half of that comparison: this buys no more H₀ relief than the fits do.** The same
partial-relief ceiling the literature runs into is the one this model finds. What changes is the risk
profile — a phenomenological fit that lands off 1.2543% simply reports a different best-fit value,
while this model has nowhere to go, because the amplitude is fixed by α and the census before any
data is seen. **Cheaper and more falsifiable, not better-fitting**, and it is worth being explicit
that those are different virtues.

Early-dark-energy-class solutions buy H₀ with new components tuned for the job and
generically worsen the S₈ clustering tension. This model's mechanism: (i) one parameter
with independent duties across BBN, the CMB, 21-cm physics, and neutrino cosmology —
the same 1.2543% must work everywhere or the model fails; (ii) an S₈ story that moves in
the observed direction; (iii) a nucleosynthesis sector re-posed honestly (the helium
abundance currently stands as a +1.3 to +2.0σ *counter*-lean against Aver, kept on record); (iv) named,
scheduled falsifiers it cannot dodge (DESI's w = −1 test; exact atomic-ratio locks in
future radio observations). No competitor on the H₀ market carries a comparable
kill-list — which is affordable only because the mechanism is one number, not a sector.

*The tension asked: which measurement is lying? The model answers: neither instrument —
the early universe was being read with the wrong electron mass, and the late-time
remainder points at the one rung of the ladder that everyone already agreed needed
re-measuring. Half the gap closes by mechanism; the other half is signed, owned, and
assigned to named referees.*

## References

[Riess 2022] (SH0ES); [Freedman 2021] (TRGB/CCHP); [Planck 2018];
[Hart–Chluba 2020], [Sekiguchi–Takahashi 2021] (the varying-m_e degeneracy);
[Di Valentino 2021] (the competitor landscape); [DESI 2024] (the named falsifier).
Full entries: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

## Where the dead ends live

The abandoned H₀ routes for this sector — chiefly the H0=73-via-birth-ramp attempt (extra
recombination-era dark radiation, which the model's own physics falsifies: the dCDF's
radiation phase ends at z_on ≈ 4×10⁷ and is dust by recombination, giving ΔN_eff ~ 10⁻³,
not the 0.26 that was hand-picked) — are recorded in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md). They matter: they are why the model's
honest H₀ is 69.9 and the gap to SH0ES's 73 is owned and open, not closed by a knob.

