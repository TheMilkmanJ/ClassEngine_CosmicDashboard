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

## 3. Where it lands

- **Same data, same pipeline**: ΛCDM's best fit gives H₀ = 68.2; the model gives
 **69.9**, with the Bayesian evidence favoring the model at ΔlnZ ≈ +2.6 (Laplace
 approximation; past the pre-registered win threshold; graded internally as marginal
 and calibration-conditional — the nested-sampling confirmer is deferred to cluster
 time, so this estimate stands on the converging chains rather than awaiting a run).
- **The residual is owned**: 69.9 is not 73.0. The model closes roughly half the
 gap and *refuses* the rest — offered spatial curvature as an escape, the fit declined
 it. The claim is not "SH0ES is fully explained"; it is "the sky prefers a universe
 with this mechanism in it, and the remaining gap is real information about the
 measurements."
- **The reach computation**: an exhaustive audit of every lever the
 model owns — the supernova-standardization channels (computed through synthetic
 photometry; the sign came out *opposite* to the tension, robustly, across 162
 template configurations), the survey-geometry leakage (+0.1–0.3%), and the
 reionization coupling (±0.3) — caps the model's account of the *ladder* reading at
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
graded, and consistent with the screening threshold inferred independently from
cosmic-web scales: *subdominant at central
values* (~0.02 mag of the observed 0.05–0.08 mag step, environment-tagged), with the
full-step reading surviving only in one corner of the threshold's allowed window — a corner
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
**And the gap widened, not closed, when the card below was checked against its source on 2026-07-28:**
the table's 2.51σ is the fixed-methodology comparison, but under the newest stack EDE's residual
tension falls to ~2σ while this model's mechanism class stays where it is. Every conclusion this
section drew at the old number survives the correction in the same direction, more strongly.

**The side-by-side, with each column's strongest card face-up:**

| | what it is | where it lands | cost | **where it beats this model** |
|---|---|---|---|---|
| **Early dark energy** | a scalar that *"behaves like a cosmological constant at early times (redshifts z ≳ 3000) and then dilutes away like radiation or faster"*, shrinking the sound horizon [Poulin et al. 2019, arXiv:1811.04083] | best-in-class on residual tension (2.51σ); H₀ toward 70 without local priors. **2025–26 status (fairness refresh, corrected 2026-07-28 after verifying the source — the earlier card understated the competitor):** ACT DR6 does not favor EDE over ΛCDM but allows a significantly larger pre-recombination fraction than Planck NPIPE despite finer small-scale precision, and EDE's raised H₀r_s improves CMB–DESI DR2 consistency. Under the newest stack (Planck ℓ<1000 + ACT DR6 + lensing + Pantheon+ + DESI DR2) the residual SH0ES tension **falls to ~2σ, from 3.7σ**; a profile likelihood gives f_EDE = 0.09 ± 0.03, H₀ = 71.0 ± 1.1. **With DESI, EDE at H₀ = 73 fits better than ΛCDM at H₀ = 68.4**, and adding SH0ES raises the preference above **5σ (Δχ² = −35.4)** [Poulin et al. 2025, arXiv:2505.08051] | ΛCDM **+3** sampled parameters, with the potential's exponent *n* fixed by hand rather than sampled | **it relieves more of the tension than this model can.** Its ceiling is genuinely higher |
| **Varying m_e (as others run it)** | m_e free at recombination | H₀ = 69.1 ± 1.2 (CMB+BAO), 71.24 ± 0.96 (+SNe) [Hart–Chluba 2020, arXiv:1912.03986]; 72.3 ⁺²·⁷₋₂.₈ but **only in Ω_kΛCDM** [Sekiguchi–Takahashi 2021, arXiv:2007.03381] | **+1** (or **+2** with the curvature the higher number needs) | **it can chase the data.** Where this model is pinned at 1.2543%, a free m_e re-fits — and reached 71.24 by doing so |
| **Local systematics / the ladder** | the 73 is mis-calibrated | CCHP JWST-only TRGB 68.81 ± 1.79 ± 1.32, JAGB 67.80 ± 2.17 ± 1.64, read by its authors as needing **no new physics** [Freedman et al. 2025]. **The steelman's counterweight (fairness refresh):** SH0ES holds the other side with JWST-extended calibrators — 72.6 ± 2.0 [Riess et al. 2024], ~73.0 as of late 2025 — attributing the gap to calibrator-host selection; the two JWST programs' distances agree at the ~1% level while their H₀ readings do not, so the dispute is live in the anchors, not the photometry | **zero** new physics | **it is the cheapest explanation on the board**, and it has not been excluded |
| **Interacting dark energy** | energy exchange between the dark components (Q ∝ Hρ-class coupling, the vacuum or quintessence variant) | Planck-alone fits reach H₀ ≈ 72–73 with the coupling free [Di Valentino et al. 2020, arXiv:1908.04281] — but the preference is a relaxed constraint rather than a detection, and adding BAO pulls the fit back toward ΛCDM values | **+1 to +2** sampled parameters (the coupling, and w where freed), plus the stability conditions the coupling must dodge | **its Planck-alone reach is higher.** Where this model converts between dark components by a derived channel that is OFF in the headline chains, IDE buys its reach by letting the data choose the exchange — the same freedom-versus-economy trade as the free-m_e row |
| **this model** | the same m_e shift, amplitude fixed before the fit at ε = 27α/5π = 1.2543% | H₀ = 69.9; reach audited to ~70.9–71.3 and **cannot reach 73** | **zero** extra parameters vs ΛCDM (`varying_me = 1.012543`, fixed) | — |

**Where this model is genuinely stronger, stated narrowly:** parameter cost (zero against EDE's
three and the literature's one-to-two), and falsifiability — the amplitude cannot be re-fitted, and
the same 1.2543% is simultaneously on the hook across BBN, the CMB, 21-cm physics and neutrino
cosmology. **Cheaper and more falsifiable, not better-fitting**, and those are different virtues.

**Where the S₈ argument stands.** The standard charge against EDE is real and
quantified: σ₈ rises, giving *"10% more power at k = 1 h/Mpc"*, and the EDE detection *"drops below
2σ"* once large-scale-structure data are added [Hill et al. 2020, arXiv:2003.07355]. But the mirror
claim — that varying-m_e is clean here — is not this model's to bank either: the most recent
recombination-modification study finds a solution that *"also eases the S₈ tension"* yet concludes
that *"once DESI DR2 BAO data are added… perturbative modifications to m_e(z) cannot fully resolve
the Hubble tension"*, because *"raising H₀ by modifying recombination generically lowers Ω_m, being
inconsistent with late-time cosmological observations"* [Lee–Zhou 2026, arXiv:2606.06495]. **That is
a named structural obstruction pointing at this model's own mechanism class, and DESI is the
instrument holding it.**

**On the direction's independent support, sized honestly.** The data do lean the model's way.
Hart–Chluba's SNe-included fit gives m_e = 1.0190 ± 0.0055,
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
[Freedman et al. 2025] (arXiv:2408.06153, CCHP JWST). The 2026-07-27 fairness refresh adds:
[arXiv:2505.08051] (EDE under ACT DR6 + DESI DR2 — §5's EDE status card);
[Di Valentino et al. 2020] (arXiv:1908.04281, interacting dark energy — the table's fifth row);
[Riess et al. 2024b] (the JWST-extended-calibrator 72.6 ± 2.0 — the ladder row's counterweight).
Full entries: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

## Where the dead ends live

The abandoned H₀ routes for this sector are recorded in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md). They matter: they are why the model's
honest H₀ is 69.9 and the gap to SH0ES's 73 is owned and open, not closed by a knob.

