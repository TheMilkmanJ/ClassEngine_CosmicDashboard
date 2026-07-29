# radio-lattice — what this paper claims, and what it deliberately leaves out

*Draft. Not for `arxiv/` until its row in `docs/working_logs/_ARXIV_READINESS.md` reads READY.*

## The one claim

A universal fractional shift ε in m_e imprints five radio observables with **fixed relative
weights** +2 : +1 : −1 : −1 : −2. The ratios follow from atomic-physics scalings and are
independent of ε's value.

## What is deliberately NOT in this paper

This list exists to be defended. Every item is something the wider programme says and this paper
does not, because including it would widen the claim past what one paper can carry — and breadth is
what draws reclassification.

| left out | why |
|---|---|
| **any mechanism for ε** | ε enters as a fitted amplitude. The ratio structure is the claim, and it survives whatever produces the shift. This is the paper's main defensive strength: it cannot be killed by a mechanism dispute. |
| **the value ε = 1.2543%** | It rests on a chain that has not converged, and on a counting assumption. Quoting it would import both problems and buy nothing — the ratios do not need it. |
| the H₀ tension resolution | a separate claim, separate paper |
| BBN rows (D/H, Y_p) | separate; they carry their own adverse tensions and would dominate referee attention |
| the neutrino, Koide, hierarchy and dark-energy results | different fields entirely; including any of them converts this into a "theory of everything" submission |
| the ε-dipole and the modulation comb | additional predictions on the same axis; they belong in a follow-up once the ratio structure is established |

## What drafting produced that the source file did not have

**The α weight vector, and a stronger claim than the source made.** The source argued the pattern
separates m_e from α because "α enters 21 cm at α⁴ but dispersion not at all". Computing the full
α column gives something sharper. In Gaussian units e ∝ α^½, so the weights are +4, +2, +1, +½,
+3/2 — **every one positive.** A varying α moves all five observables the same direction; a varying
m_e raises two and lowers three. The hypotheses therefore separate by the **sign of the correlation
between any two opposite-weight bands**, which is a qualitative test rather than a precision one.
The columns are not proportional (ratios 2, 2, −1, −½, −¾), so no rescaling maps one onto the
other. This is now Table I and is the paper's central argument.

**The sensitivity, derived rather than asserted.** With d_i = w_i·ε and Gaussian errors, the ML
amplitude has σ_ε = (Σ w_i²/σ_i²)^(−½). At common precision σ across all five bands, Σw² = 11 so
σ_ε = σ/√11 ≈ 0.30σ. Best pair (21 cm + Faraday): σ/√8 ≈ 0.35σ.

## Corrections already made while drafting

**A sensitivity claim in my own first draft was too optimistic by √2.** The falsification section
originally said a 21 cm + Faraday pair at precision σ constrains ε at "roughly σ/4". The correct
figure from Eq. (ML) is σ/√8 = 0.354σ. Caught by doing the Fisher arithmetic instead of eyeballing
the weight separation, which is exactly the sort of factor a referee checks first.

**The two-line lock does not discriminate m_e from α.** The source file claimed the preserved
H-to-D hyperfine ratio was something *"only a universal m_e shift does."* Both α⁴ and m_e² enter
the two lines identically and cancel from the ratio — verified by log-differentiation, both
derivatives zero to machine precision. The lock tests **universality** and excludes
species-dependent shifts; the m_e-versus-α separation is done by the five-band pattern alone. Source
file corrected, autopsy in the failures ledger.

## The bibliography pass (2026-07-28) — and the two things it found that matter more

**Bibliography complete.** 21 entries, every one resolved against Crossref and the arXiv API, all
carrying DOI and eprint. Nothing fabricated, nothing deleted. One entry was wrong: the Planck
reference had no volume and an incorrect title, and is now *Planck intermediate results. XXIV.
Constraints on variations in fundamental constants*, A&A **580**, A22 (2015), arXiv:1406.7482. All
21 are cited in the text; no undefined keys.

**Prior art exists on the dispersion row, and the paper now says so.** Kalita (2024) bounds α and
the proton-to-electron mass ratio against the dispersion-measure–redshift relation for localised
fast radio bursts; Wang & Xia (2025) bounds α from burst dispersion-measure clustering. This paper
is *not* first to use radio propagation for varying constants. Neither computes a multi-band weight
vector, so the claim survives — but an introduction omitting them would have read as uninformed,
which is the cheapest possible way to lose a referee.

**A methodological attack was already in the literature, and it aimed at Eq. (1).** Flambaum &
Porsev (PRL **105**, 039001) comment on Khatri & Wandelt's 21 cm paper that varying a *dimensionful*
quantity makes the magnitude and even the sign of the inferred effect depend on the choice of units.
Equation (1) as originally drafted was exactly that construction. **The claim survives, and it was
checked rather than assumed:** holding α and the strong scale fixed makes the shift a statement
about the dimensionless μ = m_p/m_e, and every row restates without a unit system — the two line
frequencies referred to the proton mass, the dispersion and rotation rows as ratios of reconstructed
to true quantity, the synchrotron row referred to the proton cyclotron frequency. Verified by
recomputation: the weight vector is unchanged at +2, +1, −1, −1, −2. A subsection now states this
before the weights are derived. Had the paper gone out silent on it, a referee who knows that
exchange would have opened with it.

## A possible novelty claim, unverified

No reference was found for how a varying m_e would bias published **rotation-measure** catalogues.
The dispersion side is covered by Kalita and Wang & Xia; the RM side appears unworked. **This has
not been checked against ADS** and must not be claimed in the text until it is.

## Open items before READY

1. ~~Literature engagement~~ — **done**, see above.
2. ~~Six sourcing citations~~ — **done**; all placed in the weight subsections where a referee
   looks first.
3. ~~Body text~~ — **done**: 8 sections, ~2100 words, 14 equations, one table.
4. **Observational section — the remaining substantive gap.** The sensitivity formalism is derived
   (σ_ε = (Σ wᵢ²/σᵢ²)^(−½); σ/√11 for all five bands at common precision, σ/√8 for the best pair),
   but the per-band observational precisions are absent, so σ_ε cannot be quoted in physical units
   and the paper proposes a test nobody can cost. The five needed are listed as a TODO in the
   source. **Do not estimate them.**
5. **Two smaller gaps from the bibliography pass.** No reference displays ν_hf ∝ g_p α⁴m_e²/m_p as a
   displayed equation — the 21 cm literature carries the combination x = α²g_p m_e/m_p instead — so
   Eq. (3) derives it and the citations corroborate rather than substitute. Rybicki & Lightman
   chapter numbers were not verified, so none are cited.
6. **No ADS search has been run.** Everything went through Crossref, the arXiv API and web search.
   ADS indexes the older radio and pulsar literature better, and the two book entries plus Wolfe
   (1976) are what it would most improve.
7. `pdflatex` and `bibtex` are not installed on this machine; the document has never been built.

## Verified so far

All five weights confirmed independently by log-differentiation (+2, +1, −1, −1, −2), with the
fixed-energy synchrotron reading at −3. Abstract 1602 characters, within arXiv's 1920 limit, with no
reference to any other document.

---

## Per-band precisions — sourcing begun 2026-07-28 (two of five done)

The TODO in `main.tex` requires each band's current observational precision **sourced, not
estimated**. Two rows are now sourced from the papers themselves (abstracts fetched and read, not
taken from search summaries — see the warning below).

### (i) 21 cm — the +2 weight row

**Rahmani et al. (2012), arXiv:1206.2653**, MNRAS 425, 556. Constrains x ≡ g_p α²/μ by comparing
21-cm absorption against optical metal lines.

- **weighted mean Δx/x = −(0.1 ± 1.3) × 10⁻⁶**; simple mean (0.0 ± 1.5) × 10⁻⁶
- four systems, 1.17 < z < 1.56, mean lookback ~9 Gyr
- VLT/UVES + GMRT + GBT, with VLBA used to select milliarcsec-unresolved sightlines

**Kanekar et al. (2010), arXiv:1003.0444**, on the same combination via HI 21 cm against C I:

- **ΔX/X = [+6.8 ± 1.0 (statistical) ± 6.7 (max. systematic)] × 10⁻⁶**, 0 < z ≤ 1.46, two systems
- consistent with no variation once the systematic is included

**What to quote, and the distinction that matters.** Under this paper's convention — α and the
strong scale held fixed, so the statement is about μ = m_p/m_e alone — Δx/x = −δμ/μ = ε. The
**statistical** precision available on the 21 cm row is therefore **σ ≈ 1.3 × 10⁻⁶**. But the
**systematic floor** from the same measurement class is **6.7 × 10⁻⁶**, five times larger, and it is
sightline-dependent (radio and optical absorption need not sample the same gas — which is why
Rahmani selects milliarcsec-unresolved sources). **Quote both.** A σ_ε built on the statistical
number alone would overstate the band's reach by a factor of five.

### (v) Faraday RM — the −2 weight row

**LoTSS DR2 RM grid, arXiv:2301.07697**, MNRAS 519, 5723.

- **median RM uncertainty 0.06 rad m⁻²**
- **systematic up to 0.3 rad m⁻²** after ionospheric RM correction
- 2461 extragalactic RMs over 5720 deg², areal density ~0.43 deg⁻²

Same shape as the 21 cm row: the systematic is 5× the statistical, and it is the ionosphere.

### A warning for whoever finishes rows (ii)–(iv)

The Kanekar number was very nearly mis-entered. A search summary returned it as
"ΔX/X = [+6.8 ± 1.0] × 10⁻⁶" — omitting the ± 6.7 systematic — which reads as a **6.8σ detection of
varying constants**. Fetching the abstract showed the systematic dominates and the result is a null.
**Read the abstract, never the summary.** In a paper whose whole argument is that a null is
informative, importing a phantom detection would have been fatal.

### Still owed: (ii) RRL, (iii) DM, (iv) synchrotron

### (ii) RRL — sourcing attempted, and the row needs a different treatment

The literature sweep did **not** return a "rest-frequency precision" of the kind the TODO assumes,
and the reason is structural rather than a gap in the search.

**RRL rest frequencies are computed, not measured.** They come from the Rydberg formula with
R_H = 109677.58 cm⁻¹, itself derived from R_∞ = 109737.31568 cm⁻¹ and the electron-to-nucleus mass
ratio. So an RRL rest frequency already carries m_e by construction. **Comparing an observed RRL
against a rest frequency computed from m_e cannot test m_e** — the dependence cancels, and any
apparent shift is a velocity.

This does not kill the row; it changes what the row is. The RRL band earns its +1 weight only in
*differential* comparison against a line with different m_e dependence — which is what the paper's
Table already encodes, and which is why the weights matter more than any single band. But the entry
in the sensitivity budget must be a **differential** precision, not an absolute rest-frequency one.

What the sweep did return, as the observational limit on the differential:

- fitted-velocity uncertainties for RRL measurements of order **2 km s⁻¹**, i.e. a fractional
  frequency precision of **≈ 6.7 × 10⁻⁶**
- calibration good to ~10% (noise-diode systems), affecting line and continuum similarly
- frequency-integrated flux uncertainties need to be below 3–5% for physical-parameter work

**So the usable number for the budget is σ ≈ 7 × 10⁻⁶ from velocity fitting** — comparable to the
21 cm systematic floor, and five times weaker than the 21 cm statistical figure. It should be
entered with the note that it is a velocity precision, since that is what limits it.

**Owed before this row can be quoted:** a source giving the differential RRL-vs-other-line precision
directly, rather than my inference from a fitted-velocity uncertainty quoted in a different context.
Marked as inference, not as sourced.

### (iii) DM — sourced, and it is the tightest band statistically by a wide margin

Pulsar dispersion-measure precision, from the pulsar-timing-array literature:

- **LOFAR: median DM uncertainty ~10⁻⁵ pc cm⁻³** for a substantial fraction of the sample
- **uGMRT, multi-band combined: ~10⁻⁴ pc cm⁻³**
- systematic, and this is the binding one: NANOGrav's DMX analysis finds infinite-frequency TOA
  offsets of **~22 μs** for the highest-DM pulsar in the array (J1643−1224) and **~7 μs** for
  low-DM pulsars, from DM mis-estimation, correlated over ~1 month timescales

**Converted to the fractional precision the budget needs.** Typical PTA DMs are 10–100 pc cm⁻³, so

| DM | σ_DM = 10⁻⁵ (LOFAR) | σ_DM = 10⁻⁴ (uGMRT) |
|---|---|---|
| 10 pc cm⁻³ | 1.0 × 10⁻⁶ | 1.0 × 10⁻⁵ |
| 30 pc cm⁻³ | 3.3 × 10⁻⁷ | 3.3 × 10⁻⁶ |
| 100 pc cm⁻³ | 1.0 × 10⁻⁷ | 1.0 × 10⁻⁶ |

**σ ≈ 10⁻⁷–10⁻⁶ statistically**, an order of magnitude tighter than the 21 cm row and three to four
orders tighter than the RRL row. That matters for the weighting argument: the −1 DM row is not a
makeweight, it is potentially the most constraining single band.

**But the systematic is what will bind**, and it is not expressible as a DM error. The ~22 μs and
~7 μs offsets are *timing* systematics with month-scale correlation, and converting them into an
equivalent σ_ε requires the timing model, not just the DM. **Do not fold the 10⁻⁷ into σ_ε until
that conversion is done** — quoting the statistical figure alone would make the DM row look decisive
when its real limit is a correlated timing systematic nobody has expressed in these units.

That is the same shape as the other two sourced rows: statistical precision five to fifty times
better than the systematic floor, and the floor is what the paper must quote.

### (iv) synchrotron — structurally different, like RRL, and for a sharper reason

The TODO asks "how the emitting population is labelled in practice". The literature answer is that
**it is not measured; it is assumed**, and the assumption is what sets the row's uncertainty.

Synchrotron observations carry a **formal strict degeneracy** between the magnetic field strength
and the cosmic-ray electron population. It is broken by *assuming energy equipartition* between
cosmic rays and the field. Consequences, from the field-estimation literature:

- for extragalactic sources the relative normalisation and spectral shape of the proton and electron
  spectra "typically must be assumed", except where gamma-ray and radio data are both available
- the assumed cosmic-ray electron spectral index measurably changes the inferred field
- every extragalactic estimator carries an **uncertainty in the overall normalisation** of the
  inferred field against the true one
- revised estimators give *larger* fields than classical ones for flat spectra (α ≈ 0.5–0.6) and
  *smaller* for steep spectra and fields above ~10 μG — i.e. the correction does not even have a
  fixed sign

**So this row cannot carry a statistical σ in the sense the other three do.** Its error is dominated
by a modelling assumption whose uncertainty is not a measurement uncertainty, and which is
degenerate with exactly the quantity the row is supposed to weigh.

## Consequence for §"Sensitivity" — the section needs restructuring, not just numbers

Sourcing all five rows reveals they are **not five instances of one kind of measurement**:

| row | weight | kind | budget |
|---|---|---|---|
| 21 cm | +2 | frequency comparison | σ_stat 1.3e−6, σ_sys 6.7e−6 |
| RRL | +1 | **differential only** — rest frequencies are computed from m_e | ≈7e−6 (velocity-limited; inferred, not sourced) |
| DM | −1 | timing | σ_stat 1e−7–1e−6, systematic is a correlated timing offset |
| synchrotron | −1 | **assumption-limited** — field/population degeneracy broken by equipartition | no statistical σ; normalisation uncertainty of unfixed sign |
| RM | −2 | frequency comparison | σ_stat 0.06, σ_sys 0.3 rad m⁻² |

The formalism σ_ε = (Σ wᵢ²/σᵢ²)^(−½) **assumes every band contributes an independent Gaussian σ**.
Two of five do not. Quoting σ/√11 for "all five bands at common precision" is therefore a statement
about a situation that does not exist, and the honest version of the section is:

1. give the three measurable bands their statistical and systematic figures, separately;
2. state that RRL enters only differentially and synchrotron only under an assumed equipartition,
   and that neither admits a clean σ;
3. compute the achievable σ_ε from the three measurable rows, and quote the five-band figure only
   as an upper bound on what the method could reach if the other two were ever made measurable.

**This is a better paper than the one with five numbers in it.** The multi-band argument survives —
it survives *better*, because the three usable systematics are physically independent (gas-sightline
mismatch, ionosphere, timing correlation) in a way five statistical errors would not have been.

---

## Bibliography: two of the four ADS-flagged entries closed without ADS (2026-07-28)

The earlier pass flagged four entries as needing ADS, which nobody has a token for. Two of them
turn out to be verifiable through the **Crossref REST API** (`api.crossref.org/works/<doi>`), which
serves metadata as JSON and is not rate-limited for single lookups.

**`WolfeBrownRoberts1976` — verified, every field exact.**

| field | bib entry | Crossref |
|---|---|---|
| title | Limits on the Variation of Fundamental Atomic Quantities over Cosmic Time Scales | identical |
| authors | Wolfe, A. M.; Brown, Robert L.; Roberts, Morton S. | identical |
| journal | Phys. Rev. Lett. | Physical Review Letters |
| volume / pages / year | 37 / 179–181 / 1976 | 37 / 179–181 / 1976 (26 July) |

**`GordonSorochenko2009` — verified except one field.** Title, authors, publisher (Springer New
York), series (Astrophysics and Space Science Library), ISBN 978-0-387-09604-9 print /
978-0-387-09691-9 electronic, and year 2009 all confirmed. **The series volume `282` is NOT in the
Crossref metadata** — it is the one unverified field in that entry, and should either be sourced or
dropped, since a wrong series number is the kind of thing a copy-editor catches and an author does
not.

**The technique, worth keeping.** APS returned HTTP 403 to a direct fetch of the DOI landing page —
publishers commonly block automated access — but `api.crossref.org/works/<doi>` returned the full
record immediately. **For citation verification, go to Crossref's API, not the publisher's page.**
It gives the registered metadata rather than a rendered page, which is what a bib entry should match
anyway.

**Still needing ADS or a physical copy:** `LorimerKramer2004` and `RybickiLightman1979` (books with
ISBNs but no DOI in the entry; Rybicki & Lightman's Wiley-VCH reissue carries
doi 10.1002/9783527618170 and is dated 1985 in Crossref, so that DOI must not be attached to the
1979 entry). Chapter numbers remain unverified and are still not cited anywhere.

**`LorimerKramer2004` — Crossref attempted and FAILED, do not retry.** A bibliographic query on
"Handbook of Pulsar Astronomy Lorimer Kramer" returns only journal articles by those authors
(O'Brien et al. 2006, Smits et al. 2008 and 2009) — not the book. Cambridge University Press does
not appear to have registered this title with Crossref, so the API route that closed the other two
entries does not reach it. **ADS or a physical copy remains the only option for its ISBN and
edition-year confirmation.** Recorded as a negative result so the query is not run a third time.

**`(ii) RRL` — my earlier ~7e-6 inference is WRONG and is withdrawn (same day).** A targeted search
for an RRL-based constraint on electron-mass variation returns **nothing** — the comparison has not
been done in the literature, which is itself the finding. What the search does return is the reason:

- RRLs in ultra-compact H II regions have **intrinsic widths of 20–50 km s⁻¹**, and up to
  **80 km s⁻¹** where bulk gas motions contribute
- electron pressure broadening is significant below ~8 GHz, with wings reaching **200 km s⁻¹**
- each hydrogen line is accompanied by helium and carbon lines offset by 121 and 150 km s⁻¹ from
  atomic-weight differences — so the neighbouring species are *further away* than the line is wide,
  which is what makes species comparison possible at all

**So the row is width-limited, not rest-frequency-limited.** Centroid precision goes as width/SNR:
a 20 km s⁻¹ line at SNR 100 centroids to 0.2 km s⁻¹ ≈ 6.7 × 10⁻⁷, which sounds excellent — but the
**systematic floor is bulk gas motion**, which is not reduced by SNR and sits at the 20–80 km s⁻¹
scale, i.e. **6.7 × 10⁻⁵ to 2.7 × 10⁻⁴**.

**That is one to two orders WORSE than my earlier 7 × 10⁻⁶ inference, and makes RRL the weakest
band in the table by a wide margin** — weaker than 21 cm's systematic by a factor of 10–40. The
earlier figure came from a fitted-velocity uncertainty quoted in an unrelated context and should
never have been carried forward even as an inference. Withdrawn.

**Consequence for the paper:** the +1 RRL row contributes almost nothing to σ_ε at present
precision. That strengthens rather than weakens the restructuring already noted — the measurable
set is really the 21 cm, DM and RM rows, and RRL belongs with synchrotron among the rows that
cannot yet be entered.

---

## 2026-07-28 — the two book entries verified; owed item (a) discharged, with its method limit stated

**Both entries were already correct.** The check confirmed rather than corrected them, which is
worth recording explicitly — a verification pass that changes nothing is still a result, and the
alternative (leaving them flagged) would have carried an unnecessary caveat into submission.

| entry | verified how | outcome |
|---|---|---|
| `GordonSorochenko2009` | Crossref record for DOI 10.1007/978-0-387-09691-9 | title, authors, Springer New York, 2009, series, and both ISBNs (978-0-387-09604-9 print / 978-0-387-09691-9 electronic) all confirmed |
| `LorimerKramer2004` | ADS bibcode `2004hpa..book.....L` | **2004 confirmed**, which was the open question |

**The two caveats, kept rather than buried.**

1. **Gordon & Sorochenko's series volume number is absent from Crossref.** The record carries the
   series name but no volume. The `282` in the entry is corroborated by the publisher's own
   catalogue listing against that ISBN — good enough to keep, not good enough to call
   Crossref-verified, and the bib note now says which.
2. **The Lorimer & Kramer year genuinely conflicts across sources.** Cambridge's catalogue and
   several secondary indexes give **2005**; ADS gives **December 2004**. The pulsar literature
   cites the ADS form, so the `2004` key stands and the pre-existing note in `refs.bib`
   ("first publication 2004; widely cited as 2005") is vindicated rather than overturned.

**Method limit, stated so item (a) is not over-claimed.** The ADS bibcode was read from a **search
listing**. The ADS record page itself could not be fetched — the interface is script-rendered and
returns empty content to a plain fetch, and no ADS API token is available in this environment. So
ADS has been *consulted for these two entries*, not *searched systematically for the paper*. If a
full ADS sweep matters before submission it still needs a token or a browser, and that is a
different job from the one just done.

**Bibliography integrity, checked while here:** 26 entries, every `\cite` key resolves to an entry,
and every entry is cited — no orphans in either direction.

**Note for arXiv prep (#54): there is no LaTeX toolchain on this box.** `pdflatex` and `latexmk`
are both absent, so the paper has never been compile-tested here. That is a prerequisite for
submission and cannot be discharged from this machine as configured.

**Still owed, unchanged:** σ_ε in physical units, which awaits the DM timing-model conversion —
the binding limit there is a ~20 μs month-correlated timing offset rather than a DM error, and
converting it needs the full timing model.

## Comment blocks moved out of main.tex for submission (2026-07-29)

arXiv distributes the LaTeX source, so anyone who downloads the paper reads its comments.
Two blocks were removed from `main.tex` on that ground and are preserved verbatim here.

**Why they had to go.** The template scaffolding gave authoring instructions and discussed
what "a moderator reads", which reads as managing moderation rather than doing physics. The
"STILL OWED before submission" block is self-evidently stale once submitted. Neither is
discreditable, but neither belongs in a public source file. The substantive verification
record survives in `refs.bib` and in this file.

```
% ---------------------------------------------------------------------------
% Template for a single-claim submission.
%
% revtex4-2 is the default because most of the target categories (hep-ph,
% astro-ph.CO, gr-qc) read as APS-style. Swap to `article` for math-ph.
%
% BEFORE WRITING ANY PROSE, fill in the abstract. If the abstract cannot be
% written without pointing at another document, the paper's boundary is wrong
% and the scope needs cutting, not explaining.
% ---------------------------------------------------------------------------
% ---------------------------------------------------------------------------
% ABSTRACT. Hard limit 1920 characters in arXiv metadata; aim well under.
% A moderator reads this and nothing else. It must contain, in order:
%   (1) the setting, in one sentence a non-specialist in the subfield follows;
%   (2) the specific claim, with its number;
%   (3) how it is obtained;
%   (4) what would falsify it;
%   (5) what is assumed and not derived --- stated here, not buried.
% Point (5) is not a weakness to hide. A paper that names its own assumptions
% in the abstract reads as competent; one that does not reads as overclaiming,
% and overclaiming is what draws reclassification.
% ---------------------------------------------------------------------------
```

```
% STILL OWED before submission:
% (a) RESOLVED 2026-07-28 --- both remaining book entries verified, and both were already
%     CORRECT; the check confirmed rather than corrected them.
%       * GordonSorochenko2009: verified against the Crossref record for DOI
%         10.1007/978-0-387-09691-9 --- title, authors, Springer New York, 2009, series, and
%         both ISBNs confirmed. Caveat recorded in refs.bib rather than hidden: the series
%         VOLUME NUMBER (282) is ABSENT from the Crossref record and rests on the publisher's
%         catalogue listing for that ISBN.
%       * LorimerKramer2004: the year was the open question, since Cambridge's catalogue and
%         several secondary indexes say 2005. ADS records bibcode 2004hpa..book.....L with a
%         December 2004 date, which is the form the pulsar literature cites, so the 2004 key
%         stands. Series (Cambridge Observing Handbooks, vol. 4) and ISBN independently confirmed.
%     METHOD LIMIT, stated so this is not read as a full ADS pass: the bibcode was read from an
%     ADS search listing. The ADS record page itself could NOT be fetched --- its interface is
%     script-rendered and returned empty content, and no ADS API token is available here. So ADS
%     has been consulted for these two entries, not searched systematically for the paper.
% (b) RESOLVED 2026-07-29 --- and the answer was that the conversion does not exist. A constant
%     eps is EXACTLY degenerate with the fitted dispersion measure: it rescales the delay's
%     coefficient and leaves its nu^-2 shape untouched, so the timing fit absorbs it completely
%     (DM_fit = N_e/(1+eps), t_inf unchanged, residuals at machine precision, at every frequency
%     coverage tested). So there was never a sigma_eps to convert TO. The 20 us figure bounds eps
%     VARIATION, ~2e-6 to ~3e-4 depending on band and column, and that is now stated in the text.
%     CONSEQUENCE, applied 2026-07-29 by owner ruling: the dispersion row is DEMOTED into the
%     set-aside group, the measurable set is two rows, and the forecast is sigma/sqrt(8) not
%     sigma/sqrt(11). scripts/dm_row_sigma_eps.py, 9 controls.
%     PROMOTION CONDITION: an independent determination of the same electron column at a
%     precision competitive with the other rows. Until then this row carries the pattern but
%     not a measurement.
%
% RESOLVED 2026-07-28 --- the RRL row. An earlier note here carried "~7e-6, inferred, not
% sourced" as its differential precision. That figure is WITHDRAWN and was wrong by one to two
% orders. A targeted search finds NO RRL-based constraint on electron-mass variation in the
% literature, and the reason is that the row is width-limited rather than rest-frequency-limited:
% RRLs in ultra-compact HII regions have intrinsic widths of 20-50 km/s, up to 80 km/s with bulk
% motions, and pressure-broadened wings reaching 200 km/s below 8 GHz. Centroid precision scales
% as width/SNR and can look excellent, but the systematic floor is bulk gas motion, which SNR
% does not reduce: 6.7e-5 to 2.7e-4, i.e. 10-40x WEAKER than the 21 cm systematic. The RRL row
% therefore contributes essentially nothing to sigma_eps at present precision and belongs with
% synchrotron among the rows that cannot yet be entered --- now for a quantitative reason as
% well as a structural one. See NOTES.md.
```

---

## The ADS gap, closed by substitution (2026-07-29)

**ADS itself was never queried.** `api.adsabs.harvard.edu` returns **401** without a token and no
token exists on this machine. That is stated plainly: item 6 above is *not* discharged by running an
ADS search. What was done instead is to verify, one at a time, the specific entries ADS was wanted
for — which is the end that item was a means to.

| entry | outcome |
|---|---|
| **Wolfe, Brown & Roberts 1976** | **CONFIRMED independently** — Phys. Rev. Lett. **37**, 179 (1976), DOI 10.1103/PhysRevLett.37.179, source AO 0235+164 at z = 0.5. The entry already carried exactly this. Nothing to fix. |
| **Gordon & Sorochenko 2009** | already Crossref-verified 2026-07-28, with the series-volume caveat recorded in the entry |
| **Lorimer & Kramer 2004** | already verified, with the 2004-vs-2005 discrepancy resolved and the read-from-listing method caveat recorded |
| **Rybicki & Lightman 1979** | **the one entry that had no verification note, and now has one.** Crossref carries **no record of the 1979 Wiley original** — only the 1985 Wiley-VCH reissue (DOI 10.1002/9783527618170), whose record does confirm title and both authors. The 1979 year and the ISBN rest on the field-standard citation form, not on a registered record. Recorded in the entry. |

**So item 6 shrinks to a single residual:** the 1979 printing of one textbook is attested by
convention rather than by a registry. Nothing in the paper depends on it beyond one standard formula
for the synchrotron characteristic frequency, and no chapter numbers are cited.

### The rotation-measure novelty question, swept a second time

Still **nothing found** on how a varying electron mass would bias published rotation-measure
catalogues. Two independent searches now, including one aimed squarely at it; both return ordinary
Faraday-rotation physics and varying-constants work that does not touch the RM reconstruction.

**This does not license a novelty claim, and none is made.** Absence in two searches is weak
evidence, and the standing rule holds: the text claims nothing about the RM row's priority. What has
changed is only that the gap is better characterised — it is not that nobody has thought about
Faraday rotation and constants, it is that the *reconstruction bias* specifically appears unworked.
