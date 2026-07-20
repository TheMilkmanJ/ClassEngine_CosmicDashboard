# The Hubble Tension: Mechanism, Residual, and the Calibration Question

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*Status: the model's* ***core empirical claim*** *— the one domain built in contact with
the data rather than extended to it. The improvement is measured and evidence-priced by a
zero-free-parameter Bayesian comparison against ΛCDM, whose number is a Laplace estimate from
the MCMC; nested sampling is deferred to cluster time, so that estimate stands without a
confirmer and the chains' convergence is what sharpens it.*

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
the measurement); TRGB uses sparse, clean halo fields.

**That referee has reported, and it went against the crowding reading — recorded here because
the model named it in advance.** JWST re-observed >1000 Cepheids across NGC 4258 and five SN Ia
hosts and found the HST–JWST mean distance difference to be **−0.01 ± 0.03 mag**, rejecting
unrecognised distance-dependent crowding as the cause of the tension at **8.2σ**
[Riess et al. 2024, arXiv:2401.04773]. Cepheid photometry is not where the 73 comes from.
What survives is narrower and still live: the *ladders themselves* disagree. CCHP's JWST-only
rungs read **TRGB 68.81 ± 1.79 (stat) ± 1.32 (sys)** and **JAGB 67.80 ± 2.17 ± 1.64**, with the
combined HST+JWST TRGB at **70.39 ± 1.22 ± 1.33 ± 0.70**, and those authors read their result as
*"consistent with the current standard ΛCDM model, without the need for the inclusion of
additional new physics"* [Freedman et al. 2025, arXiv:2408.06153] — while SH0ES reads
**73.04 ± 1.04** [Riess 2022]. The model's registered band sits on the TRGB side of a
disagreement whose *mechanism* is now unexplained rather than identified.

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

**The field's own scoreboard first, because it is not flattering.** The most recent
common-framework comparison — fourteen models, one pipeline, current CMB + BAO + supernovae —
reports the tension at *"a nominal significance above 7σ"* and finds that *"early dark energy and
early modified gravity models perform best, shifting the H₀ inference without local measurement
priors toward 70 km s⁻¹ Mpc⁻¹ and reducing the residual discrepancy with SH0ES to approximately
2.5–3.6σ"* [Schöneberg et al. 2026, arXiv:2607.13282]. Against a ΛCDM baseline of Δ_DMAP = 5.4σ,
its Table 1 scores:

| model | −ΔAIC | ln BF | residual Δ_DMAP | verdict |
|---|---|---|---|---|
| early dark energy | 23.40 | 10.51 | **2.51σ** | qualified |
| **varying m_e** | 12.58 | 3.53 | **4.25σ** | qualified |
| ΔN_eff | 3.18 | −0.09 | 5.09σ | eliminated |

**This model's mechanism sits in the varying-m_e row, and that row is beaten by EDE on every
column.** Nothing in the derivation changes that: a derived amplitude buys parameter economy, not
extra H₀ reach. Stated plainly — **on residual tension, the leading competitor is currently ahead.**

**The side-by-side, with each column's strongest card face-up:**

| | what it is | where it lands | cost | **where it beats this model** |
|---|---|---|---|---|
| **Early dark energy** | a scalar that *"behaves like a cosmological constant at early times (redshifts z ≳ 3000) and then dilutes away like radiation or faster"*, shrinking the sound horizon [Poulin et al. 2019, arXiv:1811.04083] | best-in-class on residual tension (2.51σ); H₀ toward 70 without local priors | ΛCDM **+3** sampled parameters, with the potential's exponent *n* fixed by hand rather than sampled | **it relieves more of the tension than this model can.** Its ceiling is genuinely higher |
| **Varying m_e (as others run it)** | m_e free at recombination | H₀ = 69.1 ± 1.2 (CMB+BAO), 71.24 ± 0.96 (+SNe) [Hart–Chluba 2020, arXiv:1912.03986]; 72.3 ⁺²·⁷₋₂.₈ but **only in Ω_kΛCDM** [Sekiguchi–Takahashi 2021, arXiv:2007.03381] | **+1** (or **+2** with the curvature the higher number needs) | **it can chase the data.** Where this model is pinned at 1.2543%, a free m_e re-fits — and reached 71.24 by doing so |
| **Local systematics / the ladder** | the 73 is mis-calibrated | CCHP JWST-only TRGB 68.81 ± 1.79 ± 1.32, JAGB 67.80 ± 2.17 ± 1.64, read by its authors as needing **no new physics** [Freedman et al. 2025] | **zero** new physics | **it is the cheapest explanation on the board**, and it has not been excluded |
| **this model** | the same m_e shift, amplitude fixed before the fit at ε = 27α/5π = 1.2543% | H₀ = 69.9; reach audited to ~70.9–71.3 and **cannot reach 73** | **zero** extra parameters vs ΛCDM (`varying_me = 1.012543`, fixed) | — |

**Where this model is genuinely stronger, stated narrowly:** parameter cost (zero against EDE's
three and the literature's one-to-two), and falsifiability — the amplitude cannot be re-fitted, and
the same 1.2543% is simultaneously on the hook across BBN, the CMB, 21-cm physics and neutrino
cosmology. **Cheaper and more falsifiable, not better-fitting**, and those are different virtues.

**Where the S₈ argument stands, corrected.** The standard charge against EDE is real and
quantified: σ₈ rises, giving *"10% more power at k = 1 h/Mpc"*, and the EDE detection *"drops below
2σ"* once large-scale-structure data are added [Hill et al. 2020, arXiv:2003.07355]. But the mirror
claim — that varying-m_e is clean here — is not this model's to bank either: the most recent
recombination-modification study finds a solution that *"also eases the S₈ tension"* yet concludes
that *"once DESI DR2 BAO data are added… perturbative modifications to m_e(z) cannot fully resolve
the Hubble tension"*, because *"raising H₀ by modifying recombination generically lowers Ω_m, being
inconsistent with late-time cosmological observations"* [Lee–Zhou 2026, arXiv:2606.06495]. **That is
a named structural obstruction pointing at this model's own mechanism class, and DESI is the
instrument holding it.**

**On the direction's independent support, sized honestly.** The data do lean the model's way, but by
less than this file previously claimed. Hart–Chluba's SNe-included fit gives m_e = 1.0190 ± 0.0055,
a 3.5σ preference over unity; the newer ACT DR6 + DESI DR2 analysis gives **m_e/m_e₀ = 1.0081 ±
0.0046 — a 1.8σ preference** [Toda–Seto, arXiv:2508.09025]. The preference has shrunk as the data
improved. What has *not* shrunk is the model's own standing against those fits: 1.012543 sits
+0.7σ, −1.2σ and +1.0σ from the three respectively — consistent with every one of them, having been
fixed before any of them were run.

Finally, the kill-list: (i) one number with independent duties across BBN, the CMB, 21-cm physics
and neutrino cosmology — the same 1.2543% must work everywhere or the model fails; (ii) an S₈ story
that moves in the observed direction; (iii) a nucleosynthesis sector re-posed honestly (the helium
abundance currently stands as a +1.3 to +2.0σ *counter*-lean against Aver, kept on record); (iv)
named, scheduled falsifiers it cannot dodge (DESI's w = −1 test; exact atomic-ratio locks in future
radio observations). No competitor on the H₀ market carries a comparable kill-list — which is
affordable only because the mechanism is one number, not a sector, and which is a claim about
exposure, not about fit quality.

*The tension asked: which measurement is lying? The model answers: neither instrument —
the early universe was being read with the wrong electron mass, and the late-time
remainder points at the one rung of the ladder that everyone already agreed needed
re-measuring. Half the gap closes by mechanism; the other half is signed, owned, and
assigned to named referees.*

## References

[Riess 2022] (SH0ES, arXiv:2112.04510); [Freedman 2021] (TRGB/CCHP); [Planck 2018];
[Hart–Chluba 2020] (arXiv:1912.03986), [Sekiguchi–Takahashi 2021] (arXiv:2007.03381) — the
varying-m_e degeneracy; [Di Valentino 2021] (the competitor landscape); [DESI 2024] (the named
falsifier). The steelman pass adds: [Schöneberg et al. 2026] (arXiv:2607.13282, the
fourteen-model common-framework comparison — the scoreboard §5 is graded against);
[Poulin et al. 2019] (arXiv:1811.04083, EDE); [Hill et al. 2020] (arXiv:2003.07355, EDE's S₈
cost); [Toda–Seto 2026] (arXiv:2508.09025) and [Lee–Zhou 2026] (arXiv:2606.06495) — varying-m_e
under ACT DR6 + DESI DR2; [Riess et al. 2024] (arXiv:2401.04773, the crowding referee);
[Freedman et al. 2025] (arXiv:2408.06153, CCHP JWST).
Full entries: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

## Where the dead ends live

The abandoned H₀ routes for this sector — chiefly the H0=73-via-birth-ramp attempt (extra
recombination-era dark radiation, which the model's own physics falsifies: the dCDF's
radiation phase ends at z_on ≈ 4×10⁷ and is dust by recombination, giving ΔN_eff ~ 10⁻³,
not the 0.26 that was hand-picked) — are recorded in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md). They matter: they are why the model's
honest H₀ is 69.9 and the gap to SH0ES's 73 is owned and open, not closed by a knob.

