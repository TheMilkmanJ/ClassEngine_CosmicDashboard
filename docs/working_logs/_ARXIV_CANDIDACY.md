# arXiv CANDIDACY report — ruthless inventory (2026-08-02)

> **Purpose.** Classify every top-level `docs/PRTOE_*.md` and every living package under
> `papers/` for *publication* readiness — not document-completion status.
> Completion ≠ paper. Most COMPLETE files remain **CORPUS_ONLY**.
>
> **Related logs.** Desk packaging of the TeX packages lives in
> [`_ARXIV_READINESS.md`](_ARXIV_READINESS.md) and [`papers/README.md`](../../papers/README.md).
> Live package hygiene table: [`_PACKAGE_AUDIT.md`](_PACKAGE_AUDIT.md)
> (`scripts/arxiv_package_audit.py`). Document completion tags live in
> [`_FILE_COMPLETION_STATUS.md`](_FILE_COMPLETION_STATUS.md).
> This file answers a different question: *what should become a public short paper?*
>
> **Governing rule (from readiness strategy).** One narrow, falsifiable claim per paper.
> Prefer claims a referee can check without the full framework. Multi-problem hub documents
> and ledger/history objects never ship.

> **2026-08-03 re-audit.** New **PAPER_CANDIDATE** count from top-level `docs/` = **0**.
> All borderline COMPLETE files rechecked and **REJECTED** (LV, H0 ceiling, stability, GW
> nulls, direct/indirect detection, lab cousins, coincidence, 2loop Veff, CMB map, entropy,
> strong_cp, forced_combination, Fairbank, QG remainder, fingerprint, baryogenesis,
> information, arrow, no-singularities, exploratory). No new short papers invented.
> **neutrino-mbb:** owner submitted to William Fairbank — packaging work paused; do **not**
> invent a second Fairbank TeX (`papers/fairbank-0nubb/` stays README-only).
> Package hygiene (same day): supertrace **SHIPPED**; radio-lattice (7 pp), lattice-tc-gap,
> bbn-eps-bound (optional dense ε_max(T_c) residual), kination-tracking-note (2 pp) all
> **READY_PACKAGE**. Staging shelf `docs/arXivReady/` refreshing to include the three newer
> packages alongside the original three.

---


> **2026-08-03 evening — derivation EXIT GATE.** Seats agree: **no desk-runnable derivations remain**
> (`DERIVATION_EXHAUSTION_MAP.md`: 42 blocked / 28 paid). arXiv-ready pass P1–P2:
> packages 6/6 clean; docs grade CORPUS_ONLY 43 / NOT_READY 24 / **new PAPER_CANDIDATE 0**.
> Detail: `_runs/arxiv_ready_pass_20260803/`. No new short paper without new closed science.
> Derivation hunting **stopped** unless a new missing derivation is discovered during file work.

## Status values

| status | meaning |
|---|---|
| **SHIPPED** | Already public (Zenodo etc.) and/or fully packaged for public distribution |
| **READY_PACKAGE** | TeX package exists, content holds closed; only external endorsement (or equivalent) blocks arXiv |
| **PAPER_CANDIDATE** | Science complete enough that a *new* short paper could be drafted; packaging work still owed |
| **CORPUS_ONLY** | Legitimate corpus note / scorecard / identity file / ledger — not a paper |
| **NOT_READY** | Open theory, open machine, provisional identification, or unconverged chain — do not paper |

---

## A. Re-verification of existing packages (`papers/`)

Re-checked 2026-08-02 against build logs, `submission/`, `refs.bib` / `.bbl`, and source greps;
re-audited by `scripts/arxiv_package_audit.py` → [`_PACKAGE_AUDIT.md`](_PACKAGE_AUDIT.md).
(Does **not** invent endorsement; page counts from `pdfinfo` on current `main.pdf`.)

| check | `supertrace-note` | `neutrino-mbb` | `radio-lattice` | `lattice-tc-gap` | `bbn-eps-bound` |
|---|---|---|---|---|---|
| **Status** | **SHIPPED** | **READY_PACKAGE** | **READY_PACKAGE** | **READY_PACKAGE** | **READY_PACKAGE** |
| **Title** | Two gravitational counting conditions for three generations are the same condition | If the lightest neutrino mass is the dark-energy scale: a narrow window for neutrinoless double-beta decay | A ratio-locked radio signature of a universal shift in the electron mass | A well-posed gap in the two-color lattice literature: T_c/√σ for SU(2) with N_f=3 light fundamental flavours | Primordial helium bounds on a leptonic electron-mass transition inside the BBN window |
| **Category** | gr-qc | hep-ph | astro-ph.CO (+ .IM) | hep-lat (optional hep-ph) | astro-ph.CO |
| **Pages / PDF** | **3** pp | **3** pp | **7** pp | **2** pp | **3** pp |
| **`submission/` contents** | `main.tex` alone | `main.tex` + `main.bbl` | `main.tex` + `main.bbl` | `main.tex` alone | `main.tex` alone |
| **Tarball** | `supertrace-note.tar.gz` | `neutrino-mbb.tar.gz` | `radio-lattice.tar.gz` | `lattice-tc-gap.tar.gz` | `bbn-eps-bound.tar.gz` |
| **Live BibTeX `note =`** | n/a (inline) | **none** | **none** | n/a (inline) | n/a (inline) |
| **`\bibinfo{note}` in shipped `.bbl`** | n/a | **none** | **none** | n/a | n/a |
| **Empty `acknowledgments`** | **none** | **none** | **none** | **none** | **none** |
| **"PRTOE" in tex** | **none** | **none** | **none** | **none** | **none** |
| **Public distribution** | Zenodo 10.5281/zenodo.21763188 | not yet | not yet | not yet | not yet |
| **arXiv external gate** | gr-qc (optional) | **hep-ph** | **astro-ph** | **hep-lat** | **astro-ph** |
| **Framework dependence** | **None** | **None as written** | Motivated; claim independent | **None** as gap note | **None** (ε free; Aver Y_p) |

**Non-packages under `papers/` (index only):**

| folder | status | note |
|---|---|---|
| `papers/fairbank-0nubb/` | **NOT_READY** | README only. Duplicate of neutrino-mbb arithmetic + model-tied scaffolding + unconverged-chain numbers. Do not invent TeX. |

**Verdict on TeX packages:** all five with `main.tex` are technically clean (PRTOE / note-field
greps clean; tarballs present). Content holds closed except optional dense ε_max(T_c) curve on
bbn-eps-bound (bound currently at measured T_c). Remaining blockers are endorsement-only.
Staged copies under `docs/arXivReady/` are being refreshed (2026-08-03) to cover all six
packages with `main.tex` (original three + lattice-tc-gap, bbn-eps-bound, kination-tracking-note).

---

## B. PAPER_CANDIDATE and READY_PACKAGE detail cards

Only rows in these two status buckets get proposed titles / categories / pages / claims / blockers.

### B1. SHIPPED / READY_PACKAGE (already drafted)

#### 1. `papers/supertrace-note/` — **SHIPPED**

| | |
|---|---|
| **Proposed title** | Two gravitational counting conditions for three generations are the same condition *(final)* |
| **Category** | gr-qc (optional hep-th / hep-ph) |
| **Pages** | 3 |
| **Main claim** | Navarro-Salas anomaly cancellation and Pauli/Visser finiteness are the *same* constraint once conventional scalars drop out (N₀ = 0 or ξ = 1/6); they differ on the Higgs sector. |
| **Blockers** | None for public record (Zenodo live). arXiv optional: gr-qc endorsement. |
| **Red-team hardening (2026-08-02/03)** | Framed as literature *comment*, not discovery; ξ=1/6 called out as extra naturalness input; Pauli mass m^{2k} sum rules distinguished from curvature-weighted str[k₁]. Detail: [`_PAPER_REDTEAM_FIXES.md`](_PAPER_REDTEAM_FIXES.md). |

#### 2. `papers/neutrino-mbb/` — **READY_PACKAGE** *(owner → Fairbank 2026-08-03)*

| | |
|---|---|
| **Proposed title** | If the lightest neutrino mass is the dark-energy scale: a narrow window for neutrinoless double-beta decay *(final)* |
| **Category** | hep-ph |
| **Pages** | 3 |
| **Main claim** | Under the hypothesis m₁ = ρ_Λ¼ ≃ 2.25 meV + normal ordering + NuFIT mixings, m_ββ ∈ [0.04, 5.30] meV; useful statement is the upper edge vs minimal-ordering ceiling 3.69 meV. |
| **Blockers** | **hep-ph endorsement** still the arXiv gate. **Owner submitted package to William Fairbank (2026-08-03)** — further packaging work **paused** pending that thread. Do not invent a second Fairbank TeX. Optional residual (not a hold): lower edge knife-edge under NuFIT 1σ — already stated in prose. |
| **Red-team hardening (2026-08-02/03)** | Coincidence stated as hypothesis not evidence; lower edge fragile/unprotected; nEXO overlap probability ~10.8% explicit; cosmology graded first. Detail: [`_PAPER_REDTEAM_FIXES.md`](_PAPER_REDTEAM_FIXES.md). |

#### 3. `papers/radio-lattice/` — **READY_PACKAGE**

| | |
|---|---|
| **Proposed title** | A ratio-locked radio signature of a universal shift in the electron mass *(final)* |
| **Category** | astro-ph.CO primary, astro-ph.IM cross-list |
| **Pages** | 7 |
| **Main claim** | A universal m_e shift imprints five radio observables at fixed weights +2:+1:−1:−1:−2; pattern discriminates from varying-α by sign arithmetic; only 21 cm + Faraday presently measurable (σ_ε = σ/√8). |
| **Blockers** | **astro-ph endorsement only.** DM demotion written into text; methanol tighter amplitude bound stated; no novelty claim for SZ methods. |
| **Red-team hardening (2026-08-02/03)** | Methanol ~35× tighter is front-loaded; two rows only; DM degeneracy; synchrotron −1/−3 convention; template not survey; ε free / no mechanism. Detail: [`_PAPER_REDTEAM_FIXES.md`](_PAPER_REDTEAM_FIXES.md). |

#### 4. `papers/lattice-tc-gap/` — **READY_PACKAGE** *(promoted from PAPER_CANDIDATE 2026-08-02)*

| | |
|---|---|
| **Proposed title** | A well-posed gap in the two-color lattice literature: T_c/√σ for SU(2) with N_f=3 light fundamental flavours *(final)* |
| **Category** | hep-lat (optional hep-ph) |
| **Pages** | 2 |
| **Main claim** | No published T_c/√σ exists for SU(2), N_f=3 light fundamentals; the calculation is conventional and scientifically interesting independent of any dark-sector model; optional pre-registered stake is transparency only, not the result. |
| **Blockers** | **hep-lat endorsement only.** No lattice result is claimed. Source note: `docs/PRTOE_lattice_note.md`. |
| **Red-team hardening (2026-08-02/03)** | Knowledge-limit gap only; stake demoted to transparency; no lattice result claimed. Detail: [`_PAPER_REDTEAM_FIXES.md`](_PAPER_REDTEAM_FIXES.md). |

#### 5. `papers/bbn-eps-bound/` — **READY_PACKAGE** *(promoted from PAPER_CANDIDATE 2026-08-02)*

| | |
|---|---|
| **Proposed title** | Primordial helium bounds on a leptonic electron-mass transition inside the BBN window *(packaged)* |
| **Category** | astro-ph.CO |
| **Pages** | 3 |
| **Main claim** | With ε free, Aver Y_p implies ε < 3.2% (2σ) for a leptonic m_e transition inside the BBN window; EMPRESS cannot be used (standard BBN already +2.9σ). D/H model predictions stay out. |
| **Blockers** | **astro-ph endorsement.** Optional content residual: dense ε_max(T_c) curve over [70, 500] keV not produced (bound at measured T_c only). Source note: `docs/PRTOE_bbn_witness.md`. |
| **Red-team hardening (2026-08-02/03)** | Prior literature cited; Aver vs EMPRESS separation explicit; T_c scan residual stated (bound at measured T_c only). Detail: [`_PAPER_REDTEAM_FIXES.md`](_PAPER_REDTEAM_FIXES.md). |

---

### B2. PAPER_CANDIDATE — new short papers still worth drafting

Only **one** corpus object still clears the bar for a *new* paper with a sharp, checkable
claim that can be framed without the full framework (lattice gap + BBN ε bound now packaged).
Everything else that is COMPLETE is still **CORPUS_ONLY**.

#### 6. `papers/kination-tracking-note/` — **READY_PACKAGE** *(promoted from PAPER_CANDIDATE 2026-08-02)*

| | |
|---|---|
| **Proposed title** | A rotating condensate tracking $V\propto r^{n}$ cannot reach kination: exact equation of state $w=(n-2)/(n+2)$ *(draft packaged)* |
| **Category** | gr-qc (optional hep-th) |
| **Pages** | **2** |
| **Main claim** | For a rotating condensate tracking the minimum of $V_{\mathrm{eff}}$ with $V\propto r^{n}$, the EOS is exactly $w=(n-2)/(n+2)$; no polynomial $n$ reaches the stiff (kination) limit, and freeze-out requires a trans-Planckian amplitude. |
| **Blockers** | **gr-qc endorsement only.** Optional residual: deeper literature engagement on charged Q-ball / complex-scalar cosmology (not required for the claim). |
| **Independence** | High (textbook field equation + conserved charge). Source: `docs/PRTOE_MATH_SPINE.md` §7 BKL block + `scripts/bounce_bkl_stiff_check.py`. Framework genesis/bounce narrative cut; negative sector only. |
| **Package** | `papers/kination-tracking-note/` — `main.tex` only; tarball present; PRTOE-name clean. |

#### Fairbank addendum (2026-08-02/03) — **NOT_READY** as a separate package

`docs/PRTOE_fairbank_note_draft.md` / `papers/fairbank-0nubb/`: personal experimental letter
whose checkable arithmetic is already packaged as `papers/neutrino-mbb/`. Remaining layers
are model-tied or chain-dependent. **Do not invent a second TeX package.**
**2026-08-03:** owner submitted `neutrino-mbb` to William Fairbank; Fairbank-folder packaging
stays paused (README only).

### Explicitly rejected as PAPER_CANDIDATE despite COMPLETE status

| file | why not |
|---|---|
| `PRTOE_quantum_gravity.md` (full) | Emergent-gravity programme paper; multi-route, multi-grade. The *independent* supertrace algebra is already **SHIPPED** as supertrace-note. Remaining content is framework. |
| `PRTOE_neutrino_sector.md` / Fairbank draft | Independent 0νββ window is already **READY_PACKAGE** as neutrino-mbb. Full sector + Fairbank letter are model-tied. |
| `PRTOE_radio_lattice.md` | Already packaged. |
| `PRTOE_fingerprint_lattice.md` | Too wide (CMB+BBN+ν+radio+axis). Exactly the multi-problem shape that draws gen-ph reclassification. |
| `PRTOE_cosmological_constant.md` | Existence claim inseparable from portal + α_c + lattice τ referee. Not a short checkable paper without the framework stack. |
| `PRTOE_hubble_tension.md` / `H0_CEILING` | Core empirical story, but ΔlnZ is Laplace-on-unconverged-chains; residual to SH0ES owned. Paper only after chain hygiene (R−1 ≤ 0.05) and evidence decision. |
| `PRTOE_stability.md` / `LV_pricing.md` | Model certificates — sections of a future model paper, not standalone claims about nature. **LV ruthlessness card: §B3.** |
| `PRTOE_direct_detection.md` / `indirect_detection.md` / `gravitational_waves.md` | Forced nulls *given* the constitution. Without the model they are unmotivated. |
| `PRTOE_laboratory_cousins.md` | Mapping table + proposals; no single new result. |
| `PRTOE_build_2loop_Veff_spec.md` | Real negative QFT result, but claim is about this model’s T_c pinning route — not exportable without the DE scaling story. Keep as corpus record. |
| `PRTOE_coincidence_problem.md` | Era *width* derived; occupancy honestly not. Incomplete “why now.” |
| `PRTOE_entropy.md` / information / BH / no-singularity synthesis | Structural consolidations; Page curve still OPEN on information file. |
| `PRTOE_forced_combination.md` | Exact algebra inside candidate-grade Koide program — inherits OPEN-THEORY. |
| `PRTOE_CMB_map.md` | Scorecard, not a claim. |
| All ledgers / guides / calendars | Internal machinery. |

### B3. Ruthless recheck (2026-08-02): `docs/PRTOE_LV_pricing.md` — still **CORPUS_ONLY**

**Question asked.** Can a short framework-independent (or minimally dependent) LV bounds
table note be a **PAPER_CANDIDATE**? If yes, draft `papers/lv-pricing-note/`. If only
meaningful inside the full model, document why and **do not force a package**.

**Decision: CORPUS_ONLY. No package.** Do not create `papers/lv-pricing-note/`.

#### What the source file actually is

`PRTOE_LV_pricing.md` is M3 bookkeeping: for each LV-sensitive sector, it lists
**(sector / operator) → (this model's coefficient) → (experimental bound) → (margin)**.
The verdict is “every sector clears, margins 12–29 orders; two exact zeros are
constitutional.” That is a **certificate that the model’s preferred frame is priced**,
not a claim about nature independent of the constitution.

#### Attempted independent extractions (all fail)

| reframing | why it is not a paper |
|---|---|
| **Bounds-only table** (drop “model’s value”) | Already the content of Living Reviews [Mattingly2005], [Liberati2013], [Will2014] plus [GW170817], [Herrmann2009], [DamourDyson1996]. Compilation, no new claim, no new bound. |
| **“Planck-suppressed LV vs data leaves large margins”** | Textbook; the field’s actual worry is the opposite (Collins-class naturalness: loops regenerate unsuppressed dim-3/4). Restating margins without a protection mechanism is review filler. |
| **“One-metric + no vector/tensor matter bridge ⇒ LV safe”** | Still a *model-class constitution* certificate. Referees read it as “if we forbid the dangerous operators by hand, they are absent.” Not a result. |
| **Keep numerical margins, strip house name** | Margins are ratio (model value)/(bound). Every non-trivial model value is framework-tied: EM-neutrality ⇒ photon tree 0; grav-induced \(b_\mu\sim\rho_{\rm inf}^{1/2}/M_{\rm Pl}\); Majoron channel \((m_\nu/f)\dot\theta\) with \(f\geq 100\,{\rm TeV}\), \(\dot\theta\leq H_0\); PPN \(\alpha_{1,2}\sim\rho_{\rm cosmo}/\rho_\odot\); \(\dot m_e=0\) because the ε-window closed at \(z\approx 50\); window-era ε as “evidence not bound.” Without those inputs the margin column is empty or arbitrary. |
| **Shield alone (operators unwritable, not suppressed)** | Conditional on the no-bridge constitution the file itself states. Exporting it is philosophy of the Lagrangian, not a falsifiable short note. Collins locator is also **unrecorded** in BIBLIOGRAPHY (needs external verification) — cannot cite a clean “answer to Collins” without fixing that first, and fixing the citation still does not create independence. |

#### Contrast with real PAPER_CANDIDATEs

| candidate | independent claim shape |
|---|---|
| lattice gap | Missing published lattice number — literature fact |
| BBN ε bound | Free parameters ε, \(T_c\) scanned; data → bound on nature’s parameters |
| kination negative | Field equation + conserved charge → exact EOS |
| **LV pricing** | Model coefficients vs published bounds → model clears |

LV pricing matches **stability / direct-detection / forced-null** certificates, not the
exportable claim shapes above.

#### What would change the verdict (do not pre-package on hope)

A **PAPER_CANDIDATE** could appear only if a *new* checkable object is added, e.g.:

- a model-independent re-derivation of an experimental bound (new analysis of data), or
- a sharp phenomenological limit on a *named free operator* with scanned parameters and
  no appeal to constitutional zeros, or
- a genuine literature gap in LV phenomenology comparable to the lattice \(T_c/\sqrt{\sigma}\) gap.

None of those exist in the current file. The experimental citations that *are* in
BIBLIOGRAPHY ([Mattingly2005], [Liberati2013], [Will2014], [GW170817], [Herrmann2009],
[DamourDyson1996]) support the corpus table; they do not supply a standalone paper claim.

#### Packaging rule applied

**Do not force `papers/lv-pricing-note/`.** This material belongs as a section of a future
full model paper (or remains an internal scorecard). Status remains **CORPUS_ONLY** in
inventory row `PRTOE_LV_pricing.md`.

---

## C. Full inventory — every top-level `docs/PRTOE_*.md` (64)

| file | candidacy | one-line reason |
|---|---|---|
| `PRTOE_INDEX.md` | CORPUS_ONLY | Shelf map |
| `PRTOE_READERS_GUIDE.md` | CORPUS_ONLY | Orientation |
| `PRTOE_READERS_RISK.md` | CORPUS_ONLY | Internal risk page |
| `PRTOE_THREE_EQUATIONS.md` | CORPUS_ONLY | Elevator / multi-claim hub — §0 anti-pattern |
| `PRTOE_MATH_SPINE.md` | CORPUS_ONLY *(§7 kination → READY_PACKAGE via `papers/kination-tracking-note/`)* | Hub; kination negative extracted 2026-08-02 |
| `PRTOE_THE_AMPLITUDE.md` | CORPUS_ONLY | Conditional stack; production fit provisional |
| `PRTOE_DEPENDENCY_TREE.md` | CORPUS_ONLY | Living map |
| `PRTOE_DERIVATION_HUNT.md` | CORPUS_ONLY | Open numbers registry |
| `PRTOE_DOMAIN_COVERAGE.md` | CORPUS_ONLY | Domain census |
| `PRTOE_FAILURES_LEDGER.md` | CORPUS_ONLY | Graveyard; meta-paper only *after* physics lands |
| `PRTOE_PREREGISTERED_PREDICTIONS.md` | CORPUS_ONLY | Registry, not a derivation |
| `PRTOE_CODE_MANIFEST.md` | CORPUS_ONLY | Pipeline inventory |
| `PRTOE_CHAIN_TABLES.md` | NOT_READY | Live chains unconverged (R−1 > 0.05) |
| `PRTOE_REFEREE_CALENDAR.md` | CORPUS_ONLY | Process |
| `PRTOE_honest_status.md` | CORPUS_ONLY | Private board |
| `PRTOE_strong_cp.md` | CORPUS_ONLY | Complete abstention — not a paper |
| `PRTOE_stability.md` | CORPUS_ONLY | Model certificates |
| `PRTOE_LV_pricing.md` | CORPUS_ONLY | Model LV margins table; framework-independent extract fails — see §B3 (2026-08-02) |
| `PRTOE_build_2loop_Veff_spec.md` | CORPUS_ONLY | Negative hunt record; framework-tied T_c |
| `PRTOE_lattice_note.md` | **READY_PACKAGE** *(via `papers/lattice-tc-gap/`)* | Source note for packaged gap paper |
| `PRTOE_fairbank_note_draft.md` | CORPUS_ONLY | Experimental letter; superseded for arXiv by neutrino-mbb |
| `PRTOE_hubble_tension.md` | NOT_READY | Evidence asterisk + chain hygiene |
| `PRTOE_H0_CEILING.md` | CORPUS_ONLY | Companion formula; not standalone |
| `PRTOE_dcdf_superfluid.md` | CORPUS_ONLY | Identity file; residuals open |
| `PRTOE_dyad_gas.md` | CORPUS_ONLY | Identity file; UV/T_c open |
| `PRTOE_me_mechanism_math.md` | CORPUS_ONLY | Mechanism companion; radio rows already packaged |
| `PRTOE_bbn_witness.md` | **READY_PACKAGE** *(via `papers/bbn-eps-bound/`)* | Source note for packaged ε bound; dense T_c curve residual |
| `PRTOE_deuterium_row.md` | NOT_READY | Absolute row WATCH-EXTERNAL (LUNA); liability row |
| `PRTOE_fingerprint_lattice.md` | CORPUS_ONLY | Capstone correlation — too wide for one paper |
| `PRTOE_radio_lattice.md` | READY_PACKAGE *(via `papers/radio-lattice/`)* | Source note for shipped package |
| `PRTOE_cosmological_constant.md` | NOT_READY | Lattice τ referee + full stack required |
| `PRTOE_coincidence_problem.md` | CORPUS_ONLY | Width yes, occupancy no |
| `PRTOE_s8_growth.md` | NOT_READY | OPEN-MACHINE (conv_desi, lensing) |
| `PRTOE_s8_tension.md` | NOT_READY | Companion; same machine debt |
| `PRTOE_neutrino_home.md` | NOT_READY | OPEN-MACHINE joint Σm_ν |
| `PRTOE_neutrino_sector.md` | READY_PACKAGE *(§3 via `papers/neutrino-mbb/`)* | Full sector CORPUS; m_ββ window packaged |
| `PRTOE_direct_detection.md` | CORPUS_ONLY | Forced nulls given constitution |
| `PRTOE_indirect_detection.md` | CORPUS_ONLY | Forced nulls given constitution |
| `PRTOE_laboratory_cousins.md` | CORPUS_ONLY | Analog mapping, no single claim |
| `PRTOE_gravitational_waves.md` | CORPUS_ONLY | Structural nulls + open helicity link |
| `PRTOE_galactic_atoms.md` | NOT_READY | OPEN-MACHINE (α_c, GC budget) |
| `PRTOE_smbh_atoms.md` | NOT_READY | OPEN-MACHINE (α_g chain-gated) |
| `PRTOE_lowell_anomalies.md` | NOT_READY | WATCH-EXTERNAL (BipoSH data) |
| `PRTOE_cmb_anomalies.md` | NOT_READY | WATCH-EXTERNAL joint referee |
| `PRTOE_CMB_map.md` | CORPUS_ONLY | Six-spectra scorecard |
| `PRTOE_lss_parity.md` | NOT_READY | Amplitude short; DESI 4PCF WATCH |
| `PRTOE_igmf_helicity.md` | NOT_READY | OPEN-THEORY (sign link 4) |
| `PRTOE_cosmic_magnetism.md` | NOT_READY | OPEN-THEORY; void floor OPEN; RM geometric paid / amplitude open |
| `PRTOE_koide_relation.md` | NOT_READY | OPEN-THEORY (#101/#102, pacing, sign-chain) |
| `PRTOE_forced_combination.md` | NOT_READY | Inherits Koide program grade |
| `PRTOE_quartet_clock.md` | NOT_READY | OPEN-MACHINE (zon_disp parked) |
| `PRTOE_hierarchy_problem.md` | NOT_READY | OPEN-THEORY (anchor band, basement μ5) |
| `PRTOE_quantum_gravity.md` | CORPUS_ONLY *(supertrace piece SHIPPED)* | Full file framework; independent algebra already public |
| `PRTOE_entropy.md` | CORPUS_ONLY | Consolidation / literature synthesis |
| `PRTOE_no_singularities.md` | CORPUS_ONLY | Structural synthesis; bounce open in components |
| `PRTOE_blackholes_no_singularity.md` | CORPUS_ONLY | Conditional structural; echoes optional |
| `PRTOE_bigbang_no_singularity.md` | NOT_READY | OPEN-THEORY bounce dynamics |
| `PRTOE_white_holes.md` | NOT_READY | Provisional global ID; bounce open |
| `PRTOE_information_paradox.md` | CORPUS_ONLY | Structural; Page *curve* still OPEN |
| `PRTOE_arrow_of_time.md` | CORPUS_ONLY | Our-cycle gap not desk-closeable |
| `PRTOE_baryogenesis.md` | CORPUS_ONLY | COMPLETE-CONDITIONAL; ω_J back-target open |
| `PRTOE_inflation_replacement.md` | NOT_READY | OPEN-THEORY bounce + tilt residual |
| `PRTOE_cyclic_torus_genesis.md` | NOT_READY | Self-graded story-grade |
| `PRTOE_granule_scoping.md` | NOT_READY | OPEN-MACHINE (sims not started) |

### Counts (top-level docs only, primary candidacy)

| status | n | notes |
|---|---:|---|
| SHIPPED | 0 | SHIPPED lives under `papers/`, not as a bare `.md` |
| READY_PACKAGE | 5 | radio_lattice, neutrino_sector, lattice_note, bbn_witness, MATH_SPINE §7 (via packages) |
| PAPER_CANDIDATE | **0** | kination extracted 2026-08-02; no further docs export without new closed science |
| CORPUS_ONLY | ~41 | majority of COMPLETE / COMPLETE-CONDITIONAL / LEDGER |
| NOT_READY | ~18 | OPEN-THEORY + OPEN-MACHINE + WATCH that cannot paper yet |
| **Total** | **64** | |

*(READY_PACKAGE on source notes is bookkeeping; the shippable objects are the six TeX
folders under `papers/` with `main.tex`.)*

---

## D. Existing `papers/*` summary

| package | candidacy | public? | next step |
|---|---|---|---|
| `papers/supertrace-note/` | **SHIPPED** | Zenodo 10.5281/zenodo.21763188 | Optional arXiv gr-qc if endorsed |
| `papers/neutrino-mbb/` | **READY_PACKAGE** | no | Owner → Fairbank (2026-08-03); packaging paused; hep-ph endorsement still for arXiv |
| `papers/radio-lattice/` | **READY_PACKAGE** | no | astro-ph endorsement → upload (7 pp READY) |
| `papers/lattice-tc-gap/` | **READY_PACKAGE** | no | hep-lat endorsement → upload |
| `papers/bbn-eps-bound/` | **READY_PACKAGE** | no | astro-ph endorsement → upload; optional dense T_c curve |
| `papers/kination-tracking-note/` | **READY_PACKAGE** | no | gr-qc endorsement → upload; 2 pp READY |
| `papers/fairbank-0nubb/` | **NOT_READY** | no | Keep README only; do not invent TeX; ship claim via neutrino-mbb |

Hygiene table: [`_PACKAGE_AUDIT.md`](_PACKAGE_AUDIT.md) (`scripts/arxiv_package_audit.py`).

---

## E. Ruthless summary judgment

1. **Most COMPLETE files are not papers.** Completion means the *document finished its internal job*. Papers need one sharp claim, external literature engagement, self-contained notation, and no chain asterisks.
2. **Six objects can leave the desk as manuscripts today** (supertrace public; five endorsement-gated TeX packages including kination-tracking-note). Hygiene 2026-08-03 confirms READY/SHIPPED as above.
3. **No further *new* short paper** remains on the docs shelf without new closed science. Kination negative (MATH_SPINE §7) was extracted 2026-08-02. **2026-08-03 re-audit:** new PAPER_CANDIDATEs from `docs/` still **0** — borderline COMPLETE list rechecked and rejected (LV, H0 ceiling, stability, GW nulls, direct/indirect, lab cousins, coincidence, 2loop Veff, CMB map, entropy, strong_cp, forced_combination, Fairbank, QG remainder, fingerprint, baryogenesis, information, arrow, no-singularities, exploratory). Everything else is either open, multi-claim, framework-only, or already packaged.
4. **Do not paper:** Koide mechanism, hierarchy anchor, IGMF sign, S₈ conversion, galactic/SMBH atoms, bounce/cyclic sector, cosmological constant precision, Hubble evidence number, Fairbank as a second neutrino note — until their named debts close (or never, for duplicates). **neutrino-mbb is with Fairbank (owner submission 2026-08-03); do not invent second Fairbank TeX.**
5. **Do not invent endorsement.** Endorsement is per archive and is the owner’s external task.
6. **LV pricing is not a candidate.** Ruthless recheck 2026-08-02 (§B3): bounds-only is review; margins require model coefficients; shield is constitutional. **CORPUS_ONLY — no `papers/lv-pricing-note/`.**

---

## F. Top candidates ranked

| rank | object | status | why this rank |
|---:|---|---|---|
| **1** | `papers/supertrace-note/` | **SHIPPED** | Fully independent literature algebra; public on Zenodo; easiest referee check in the set. |
| **2** | `papers/neutrino-mbb/` | **READY_PACKAGE** | Single hypothesis → m_ββ window; no chain; package clean; hep-ph endorsement only. |
| **3** | `papers/radio-lattice/` | **READY_PACKAGE** | Atomic-physics ratio pattern; ε free; content hold closed; astro-ph endorsement only. |
| **4** | `papers/lattice-tc-gap/` | **READY_PACKAGE** | Literature gap; independent; 2 pp TeX clean; hep-lat endorsement only. |
| **5** | `papers/bbn-eps-bound/` | **READY_PACKAGE** | Chain-free ε bound from Aver Y_p; 3 pp; optional dense T_c curve residual. |
| **6** | `papers/kination-tracking-note/` | **READY_PACKAGE** | Negative sector EOS; 2 pp; gr-qc; extracted from MATH_SPINE §7 2026-08-02. |

**Explicit non-ranking of hub “big results”:** Hubble tension, cosmological constant, full quantum gravity, fingerprint lattice — too conditional, too wide, or already partially shipped in narrower form.

---

## G. Recommended action order

1. **Owner:** pursue endorsements (astro-ph for radio-lattice + bbn-eps-bound; hep-lat for lattice-tc-gap; gr-qc for supertrace and/or kination-tracking-note). **neutrino-mbb / hep-ph:** packaging paused — owner submitted to William Fairbank (2026-08-03).
2. **Desk (optional):** dense ε_max(T_c) curve for bbn-eps-bound; deepen kination literature citations if desired. **No further docs→paper extractions** until OPEN-THEORY/MACHINE close. (2026-08-03 re-audit: PAPER_CANDIDATE still 0.)
3. **Do not** invent TeX for Fairbank — neutrino-mbb already owns that claim; Fairbank packaging stays paused.
4. **Do not** start a multi-claim “PRTOE overview” paper.
5. **Do not** promote OPEN-THEORY / OPEN-MACHINE files on completion status alone.
6. **Hygiene:** re-run `python3 scripts/arxiv_package_audit.py` after any package add/edit. Stage/refresh `docs/arXivReady/` for all six packages.

---

*Report filed 2026-08-02. LV pricing recheck (§B3) same day: CORPUS_ONLY, no package.
Package index refreshed same day for lattice-tc-gap, bbn-eps-bound, and fairbank-0nubb.
Hygiene: `scripts/arxiv_package_audit.py` → `_PACKAGE_AUDIT.md`.
Re-verify packages against build logs and greps; do not treat this file as an endorsement
or submission authorization.*

**Red-team hardening (2026-08-02/03):** nineteen paper-facing attacks audited against live
`papers/*/main.tex`; all FIXED in prose (bbn dense ε_max(T_c) remains optional content residual).
Ledger: [`_PAPER_REDTEAM_FIXES.md`](_PAPER_REDTEAM_FIXES.md). Short notes added on each B1 card.

**2026-08-03 re-audit:** PAPER_CANDIDATE still **0** (full borderline COMPLETE reject list in
header note). neutrino-mbb with Fairbank; no second Fairbank TeX. Package READY/SHIPPED
hygiene confirmed; `docs/arXivReady/` expansion in progress.

---

## H. Addendum 2026-08-02/03 — Fairbank note extract audit

**Object:** `docs/PRTOE_fairbank_note_draft.md`  
**Package path:** `papers/fairbank-0nubb/`  
**Verdict:** **NOT_READY** (no TeX created)

### Assessment

Asked whether a short arXiv-style extract can be cut from the Fairbank draft **without**
depending on unconverged chains, stripping the framework name, and keeping only standard
m_ββ / experimental framing already in the draft and consistent with `papers/neutrino-mbb`.

| layer in draft | chain-free? | framework-free? | already packaged? |
|---|---|---|---|
| m_ββ window, triangle floor, nEXO/LEGEND/CUPID overlay, Ba-tagging discrimination | **yes** | **yes** if m₁ is a hypothesis | **yes** — entire claim of `papers/neutrino-mbb/` |
| dark fluid + ε + Majorana-as-structural, BBN/D/H, m_e recombination “squeeze relaxes” | n/a / partial | **no** | no (and should not be) |
| H₀ / multi-chain best-fit / Laplace evidence language | **no** (draft forbids quoting) | **no** | blocked by chain hygiene |

**Conclusion.** The only extract that satisfies the independence rules is a near-copy of
neutrino-mbb. That package already holds the closed claim (READY_PACKAGE; external gate =
hep-ph endorsement only). Creating a second manuscript would be duplicate packaging, not a
new paper. Residual Fairbank-only material is either model-tied or chain-dependent; neither
may ship under the governing rule.

**Action taken:** `papers/fairbank-0nubb/README.md` records **NOT_READY** and the reasons.
No `main.tex`, no `submission/`, no tarball.

**Inventory alignment (unchanged):** inventory row already had  
`PRTOE_fairbank_note_draft.md` → CORPUS_ONLY (“Experimental letter; superseded for arXiv by
neutrino-mbb”). Explicit reject table already listed Fairbank with the same reason. This
addendum is a dedicated packaging audit, not a status upgrade.

**Do not:** invent TeX for fairbank-0nubb; do not re-paper the m_ββ window under a second
folder name; do not promote the Status-section chain comparison as a result.

---

## H. Addendum (2026-08-02) — GW structural nulls as an independent short note?

**Question.** Can the two structural nulls in `docs/PRTOE_gravitational_waves.md` —
(1) vortex-network Gμ silence, (2) chiral stochastic-background amplitude null because
the carrier is missing — ship as a short standalone note under something like
`papers/gw-structural-nulls/` (revtex, no framework name, honest grade, clean-room tar)?

**Decision: NO.** Status remains **CORPUS_ONLY**. Do **not** create
`papers/gw-structural-nulls/`. Candidacy addendum only.

### What the corpus already holds (numbers only as written in the GW file)

| object | value / statement in file | role |
|---|---|---|
| vortex tension (local-density max.) | **Gμ ~ 3×10⁻²¹** (cosmic mean lower); from μ ~ πħ²ρ/m² · ln(R/ξ) | model input → null |
| CMB comparison | Gμ < 10⁻⁷ | literature bound cited in file |
| PTA network sensitivity scale | ~10⁻¹⁰ | comparison cited in file |
| kill threshold (file) | demonstrated cosmic-string-network component with Gμ ≳ 10⁻¹¹ would kill | model prediction |
| network Ω_GW h² | **≈ 3×10⁻¹⁸** | structural-null carrier |
| margins (file prose only) | ~8 orders under pulsar timing; ~4 under LISA / ground 3G; ~1.5 under inflationary B-mode floor | same carrier |
| residual swirl today | θ̇ ~ 10⁻² H₀ → every band 12+ orders below instrument reach | post-freeze residual |
| open coefficient | θ·R·R̃ magnitude still **open computation**; break-threshold priced coeff·θ̇ ~ 10¹⁰ H₀ | not closed |
| chirality family | polarization asymmetry may be O(1) and still unobservable because **carrier absent** | formal prediction |

No detector bound beyond those already written in the GW note is used or invented here.

### Why this fails the independent-note bar

1. **Forced nulls given the constitution.** Same rejection already on the inventory
   (section B, explicit reject table with direct/indirect detection): without the model
   they are unmotivated. A referee who has never seen the corpus gets only
   "if Gμ ~ 10⁻²¹ then PTA is silent," which is standard string-network arithmetic, not a
   new claim about nature.

2. **The load-bearing number is model-internal.** Gμ ~ 3×10⁻²¹ is set by the condensate
   density and vortex scale (μ ~ πħ²ρ/m² · ln(R/ξ)), not by a publicly checkable external
   input stated as a hypothesis (contrast: neutrino-mbb states m₁ = ρ_Λ¼ as hypothesis and
   exports only the m_ββ window).

3. **The two "nulls" are one fact twice.** The chiral-amplitude structural null is the
   vortex carrier amplitude under every instrument; the polarization channel does not
   supply an independent amplitude. Packaging both as a note would sell one silence under
   two names.

4. **Open prong remains open.** The θ·R·R̃ coefficient is still the open computation in
   the file (docket: paid object is carrier Ω_GW only; coefficient parked). A note cannot
   honestly claim a closed chiral-GW *prediction* beyond "carrier missing → formal."

5. **Split prediction is framework biography.** Clean polarization on all resolved binaries
   (LIGO/LISA/PTA redshifts as written) and chirality confined to the primordial stochastic
   background is the settling-clock story — not checkable without the freeze narrative.

6. **Governing rule.** One narrow, falsifiable claim a referee can check *without* the full
   framework. These silences are corpus self-checks turned formal predictions inside the
   model scorecard — legitimate COMPLETE thread material (`_FILE_COMPLETION_STATUS`), not
   PAPER_CANDIDATE.

### Grade (honest)

| grade axis | mark |
|---|---|
| Internal thread job (T10) | **COMPLETE** — vortex Gμ null + chiral carrier null paid |
| Exportable short paper | **CORPUS_ONLY** — not PAPER_CANDIDATE, not READY_PACKAGE |
| Independence without framework name | **Fails** — claim collapses to trivial string Gμ scaling once ρ/m are stripped |
| Action | **No TeX package.** No tar. No `papers/gw-structural-nulls/`. |

### Contrast (what *does* ship)

Independent packages (supertrace algebra; m₁ hypothesis → m_ββ; radio ratio weights;
lattice T_c/√σ gap) either use only published literature, or free external parameters, or a
named literature hole. GW structural nulls do none of those.

*Addendum filed 2026-08-02 against `docs/PRTOE_gravitational_waves.md` only. Inventory row
for that file is unchanged: CORPUS_ONLY — structural nulls + open helicity link.*
