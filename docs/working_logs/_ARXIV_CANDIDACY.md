# arXiv CANDIDACY report — ruthless inventory (2026-08-02)

> **Purpose.** Classify every top-level `docs/PRTOE_*.md` and every living package under
> `papers/` for *publication* readiness — not document-completion status.
> Completion ≠ paper. Most COMPLETE files remain **CORPUS_ONLY**.
>
> **Related logs.** Desk packaging of the three TeX packages lives in
> [`_ARXIV_READINESS.md`](_ARXIV_READINESS.md) and [`papers/README.md`](../../papers/README.md).
> Document completion tags live in [`_FILE_COMPLETION_STATUS.md`](_FILE_COMPLETION_STATUS.md).
> This file answers a different question: *what should become a public short paper?*
>
> **Governing rule (from readiness strategy).** One narrow, falsifiable claim per paper.
> Prefer claims a referee can check without the full framework. Multi-problem hub documents
> and ledger/history objects never ship.

---

## Status values

| status | meaning |
|---|---|
| **SHIPPED** | Already public (Zenodo etc.) and/or fully packaged for public distribution |
| **READY_PACKAGE** | TeX package exists, content holds closed; only external endorsement (or equivalent) blocks arXiv |
| **PAPER_CANDIDATE** | Science complete enough that a *new* short paper could be drafted; packaging work still owed |
| **CORPUS_ONLY** | Legitimate corpus note / scorecard / identity file / ledger — not a paper |
| **NOT_READY** | Open theory, open machine, provisional identification, or unconverged chain — do not paper |

---

## A. Re-verification of the three existing packages (`papers/`)

Re-checked 2026-08-02 against build logs, `submission/`, `refs.bib` / `.bbl`, and source greps.
(Does **not** invent endorsement; does **not** re-run pdflatex in this pass — page counts and
byte sizes are from the last recorded clean builds in `main.log`.)

| check | `supertrace-note` | `neutrino-mbb` | `radio-lattice` |
|---|---|---|---|
| **Status** | **SHIPPED** | **READY_PACKAGE** | **READY_PACKAGE** |
| **Title** | Two gravitational counting conditions for three generations are the same condition | If the lightest neutrino mass is the dark-energy scale: a narrow window for neutrinoless double-beta decay | A ratio-locked radio signature of a universal shift in the electron mass |
| **Category** | gr-qc | hep-ph | astro-ph.CO (+ .IM) |
| **Pages / PDF** | **3** pp, 229842 B | **3** pp, 254556 B | **6** pp, 309217 B |
| **`submission/` contents** | `main.tex` alone | `main.tex` + `main.bbl` | `main.tex` + `main.bbl` |
| **Tarball** | `supertrace-note.tar.gz` present | `neutrino-mbb.tar.gz` present | `radio-lattice.tar.gz` present |
| **Live BibTeX `note =`** | n/a (inline `thebibliography`) | **none** in `refs.bib` | **none** in `refs.bib` |
| **`\bibinfo{note}` in shipped `.bbl`** | n/a | **none** | **none** |
| **Empty `acknowledgments`** | **none** | **none** | **none** |
| **"PRTOE" in `main.tex` / `submission/`** | **none** | **none** | **none** |
| **Public distribution** | Zenodo DOI [10.5281/zenodo.21763188](https://zenodo.org/records/21763188) (2026-08-02) | not yet | not yet |
| **arXiv external gate** | gr-qc endorsement (optional; Zenodo already public) | **hep-ph endorsement** | **astro-ph endorsement** |
| **Framework dependence** | **None** (literature algebra only) | **None as written** (m₁ hypothesis stated) | Motivated by corpus; **claim independent** (ε free fit, atomic weights) |

**Verdict on packages:** all three remain technically clean. Content holds are closed. Remaining
blockers are endorsement-only for the two unpublished packages. Staged copies under
`docs/arXivReady/` mirror these three.

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

#### 2. `papers/neutrino-mbb/` — **READY_PACKAGE**

| | |
|---|---|
| **Proposed title** | If the lightest neutrino mass is the dark-energy scale: a narrow window for neutrinoless double-beta decay *(final)* |
| **Category** | hep-ph |
| **Pages** | 3 |
| **Main claim** | Under the hypothesis m₁ = ρ_Λ¼ ≃ 2.25 meV + normal ordering + NuFIT mixings, m_ββ ∈ [0.04, 5.30] meV; useful statement is the upper edge vs minimal-ordering ceiling 3.69 meV. |
| **Blockers** | **hep-ph endorsement only.** Optional owner note (not a hold): lower edge knife-edge under NuFIT 1σ — already stated in prose. |

#### 3. `papers/radio-lattice/` — **READY_PACKAGE**

| | |
|---|---|
| **Proposed title** | A ratio-locked radio signature of a universal shift in the electron mass *(final)* |
| **Category** | astro-ph.CO primary, astro-ph.IM cross-list |
| **Pages** | 6 |
| **Main claim** | A universal m_e shift imprints five radio observables at fixed weights +2:+1:−1:−1:−2; pattern discriminates from varying-α by sign arithmetic; only 21 cm + Faraday presently measurable (σ_ε = σ/√8). |
| **Blockers** | **astro-ph endorsement only.** DM demotion written into text; methanol tighter amplitude bound stated; no novelty claim for SZ methods. |

---

### B2. PAPER_CANDIDATE — new short papers worth drafting (ruthless short list)

Only three corpus objects clear the bar for a *new* paper with a sharp, checkable claim that
can be framed without the full framework. Everything else that is COMPLETE is still
**CORPUS_ONLY**.

#### 4. `docs/PRTOE_lattice_note.md` — **PAPER_CANDIDATE** *(best unshipped new paper)*

| | |
|---|---|
| **Proposed title** | A well-posed gap in the two-color lattice literature: T_c/√σ for SU(2) with N_f = 3 light fundamental flavours |
| **Category** | hep-lat (optional hep-ph) |
| **Pages** | ~3–5 |
| **Main claim** | No published T_c/√σ exists for SU(2), N_f = 3 light fundamentals; the gap is scientifically interesting independent of any dark-sector model (pseudo-real chiral pattern, flavour-saturation comparison to SU(3)); a pre-registered numerical stake is stated for transparency, not as the paper’s result. |
| **Blockers** | Full LaTeX conversion (L); abstract; standard bibliography (already half-built in file); strip pre-registration house IDs (P-2026-048 → plain language); keep model stake as *one optional transparency paragraph*, not the headline; **no computation is claimed** — this is a gap/motivation note, so it must not oversell. External: lattice group to run the campaign (#67) is orthogonal to publishing the *gap note*. |
| **Independence** | High if framed as a literature gap. The ½ln2 bet is optional colour, not the claim. |

#### 5. `docs/PRTOE_bbn_witness.md` (constraint half only) — **PAPER_CANDIDATE**

| | |
|---|---|
| **Proposed title** | Primordial helium bounds on a leptonic electron-mass transition inside the BBN window |
| **Category** | astro-ph.CO |
| **Pages** | ~4–6 |
| **Main claim** | With ε free and T_c *scanned* over [70, 500] keV (not fixed to any model value), Aver Y_p implies ε < 3.2% (2σ) for a transition switching on inside the BBN window; EMPRESS cannot be used (2.9σ from SBBN independently). |
| **Blockers** | Must **not** quote chain-dependent central D/H as a prediction; D/H and ΔN_eff stay out of the bound (file already says so); produce the T_c-scan *curve* (currently bound quoted at window T_c only); LaTeX + external BBN/Y_p literature engagement; strip house dialect and pipeline filenames; PRyM run provenance must be reproducible from public scripts. |
| **Independence** | Medium–high if ε and T_c are free parameters. Dies if the paper sells a fixed T_c = 177 keV as derived. |

#### 6. `docs/PRTOE_MATH_SPINE.md` §7 fragment only — **PAPER_CANDIDATE** *(thin but real)*

| | |
|---|---|
| **Proposed title** | A rotating condensate tracking V ∝ rⁿ cannot reach kination: exact equation of state w = (n−2)/(n+2) |
| **Category** | gr-qc / hep-th |
| **Pages** | ~2–3 |
| **Main claim** | For a rotating condensate tracking the minimum of V_eff with V ∝ rⁿ, the EOS is exactly w = (n−2)/(n+2); no polynomial n reaches the stiff (kination) limit, and freeze-out requires a trans-Planckian amplitude. |
| **Blockers** | Extract §7 into a self-contained note; cut all framework genesis/bounce narrative; cite classical BKL / stiff-fluid literature; re-derive tracking result in the paper’s own appendix or cite the integration script; must not claim to solve the bounce problem — it is a *negative* sector result. |
| **Independence** | High (textbook field equation + conserved charge). |

### Explicitly rejected as PAPER_CANDIDATE despite COMPLETE status

| file | why not |
|---|---|
| `PRTOE_quantum_gravity.md` (full) | Emergent-gravity programme paper; multi-route, multi-grade. The *independent* supertrace algebra is already **SHIPPED** as supertrace-note. Remaining content is framework. |
| `PRTOE_neutrino_sector.md` / Fairbank draft | Independent 0νββ window is already **READY_PACKAGE** as neutrino-mbb. Full sector + Fairbank letter are model-tied. |
| `PRTOE_radio_lattice.md` | Already packaged. |
| `PRTOE_fingerprint_lattice.md` | Too wide (CMB+BBN+ν+radio+axis). Exactly the multi-problem shape that draws gen-ph reclassification. |
| `PRTOE_cosmological_constant.md` | Existence claim inseparable from portal + α_c + lattice τ referee. Not a short checkable paper without the framework stack. |
| `PRTOE_hubble_tension.md` / `H0_CEILING` | Core empirical story, but ΔlnZ is Laplace-on-unconverged-chains; residual to SH0ES owned. Paper only after chain hygiene (R−1 ≤ 0.05) and evidence decision. |
| `PRTOE_stability.md` / `LV_pricing.md` | Model certificates — sections of a future model paper, not standalone claims about nature. |
| `PRTOE_direct_detection.md` / `indirect_detection.md` / `gravitational_waves.md` | Forced nulls *given* the constitution. Without the model they are unmotivated. |
| `PRTOE_laboratory_cousins.md` | Mapping table + proposals; no single new result. |
| `PRTOE_build_2loop_Veff_spec.md` | Real negative QFT result, but claim is about this model’s T_c pinning route — not exportable without the DE scaling story. Keep as corpus record. |
| `PRTOE_coincidence_problem.md` | Era *width* derived; occupancy honestly not. Incomplete “why now.” |
| `PRTOE_entropy.md` / information / BH / no-singularity synthesis | Structural consolidations; Page curve still OPEN on information file. |
| `PRTOE_forced_combination.md` | Exact algebra inside candidate-grade Koide program — inherits OPEN-THEORY. |
| `PRTOE_CMB_map.md` | Scorecard, not a claim. |
| All ledgers / guides / calendars | Internal machinery. |

---

## C. Full inventory — every top-level `docs/PRTOE_*.md` (64)

| file | candidacy | one-line reason |
|---|---|---|
| `PRTOE_INDEX.md` | CORPUS_ONLY | Shelf map |
| `PRTOE_READERS_GUIDE.md` | CORPUS_ONLY | Orientation |
| `PRTOE_READERS_RISK.md` | CORPUS_ONLY | Internal risk page |
| `PRTOE_THREE_EQUATIONS.md` | CORPUS_ONLY | Elevator / multi-claim hub — §0 anti-pattern |
| `PRTOE_MATH_SPINE.md` | CORPUS_ONLY *(§7 fragment → PAPER_CANDIDATE #6)* | Hub; only kination negative exports |
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
| `PRTOE_LV_pricing.md` | CORPUS_ONLY | Model LV margins table |
| `PRTOE_build_2loop_Veff_spec.md` | CORPUS_ONLY | Negative hunt record; framework-tied T_c |
| `PRTOE_lattice_note.md` | **PAPER_CANDIDATE** | Independent literature gap + optional stake |
| `PRTOE_fairbank_note_draft.md` | CORPUS_ONLY | Experimental letter; superseded for arXiv by neutrino-mbb |
| `PRTOE_hubble_tension.md` | NOT_READY | Evidence asterisk + chain hygiene |
| `PRTOE_H0_CEILING.md` | CORPUS_ONLY | Companion formula; not standalone |
| `PRTOE_dcdf_superfluid.md` | CORPUS_ONLY | Identity file; residuals open |
| `PRTOE_dyad_gas.md` | CORPUS_ONLY | Identity file; UV/T_c open |
| `PRTOE_me_mechanism_math.md` | CORPUS_ONLY | Mechanism companion; radio rows already packaged |
| `PRTOE_bbn_witness.md` | **PAPER_CANDIDATE** | Constraint half chain-free if reframed |
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
| `PRTOE_cosmic_magnetism.md` | NOT_READY | OPEN-THEORY; RM formula missing |
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
| READY_PACKAGE | 2 | radio_lattice.md, neutrino_sector.md (via packages) |
| PAPER_CANDIDATE | 3 | lattice_note, bbn_witness, MATH_SPINE §7 |
| CORPUS_ONLY | ~41 | majority of COMPLETE / COMPLETE-CONDITIONAL / LEDGER |
| NOT_READY | ~18 | OPEN-THEORY + OPEN-MACHINE + WATCH that cannot paper yet |
| **Total** | **64** | |

*(READY_PACKAGE on two source notes is bookkeeping; the shippable objects are the three `papers/` folders.)*

---

## D. Existing `papers/*` summary

| package | candidacy | public? | next step |
|---|---|---|---|
| `papers/supertrace-note/` | **SHIPPED** | Zenodo 10.5281/zenodo.21763188 | Optional arXiv gr-qc if endorsed |
| `papers/neutrino-mbb/` | **READY_PACKAGE** | no | hep-ph endorsement → upload |
| `papers/radio-lattice/` | **READY_PACKAGE** | no | astro-ph endorsement → upload |

---

## E. Ruthless summary judgment

1. **Most COMPLETE files are not papers.** Completion means the *document finished its internal job*. Papers need one sharp claim, external literature engagement, self-contained notation, and no chain asterisks.
2. **The only three objects that should leave the desk as manuscripts today are already written** (supertrace public; neutrino-mbb and radio-lattice endorsement-gated).
3. **At most three *new* short papers** are worth drafting before a first model-paper programme: lattice gap note, BBN ε-constraint (reframed), kination negative. Everything else is either open, multi-claim, or framework-only.
4. **Do not paper:** Koide mechanism, hierarchy anchor, IGMF sign, S₈ conversion, galactic/SMBH atoms, bounce/cyclic sector, cosmological constant precision, Hubble evidence number — until their named debts close.
5. **Do not invent endorsement.** Endorsement is per archive and is the owner’s external task.

---

## F. Top 5 candidates ranked

| rank | object | status | why this rank |
|---:|---|---|---|
| **1** | `papers/supertrace-note/` | **SHIPPED** | Fully independent literature algebra; public on Zenodo; easiest referee check in the set. |
| **2** | `papers/neutrino-mbb/` | **READY_PACKAGE** | Single hypothesis → m_ββ window; no chain; package clean; hep-ph endorsement only. |
| **3** | `papers/radio-lattice/` | **READY_PACKAGE** | Atomic-physics ratio pattern; ε free; content hold closed; astro-ph endorsement only. |
| **4** | `docs/PRTOE_lattice_note.md` | **PAPER_CANDIDATE** | Best *new* paper: real literature gap, independent of the framework if framed as gap + optional stake. |
| **5** | `docs/PRTOE_bbn_witness.md` (constraint reframing) | **PAPER_CANDIDATE** | Chain-free ε bound from Aver Y_p with scanned T_c; sharp and checkable if model T_c is not smuggled in. |

**Honorable mention (not top 5):** MATH_SPINE §7 kination negative — publishable gr-qc note after extraction, thinner novelty than #4–#5.

**Explicit non-ranking of hub “big results”:** Hubble tension, cosmological constant, full quantum gravity, fingerprint lattice — too conditional, too wide, or already partially shipped in narrower form.

---

## G. Recommended action order

1. **Owner:** pursue endorsements (astro-ph for radio-lattice; hep-ph for neutrino-mbb; optional gr-qc for supertrace).
2. **Desk (only if drafting new work):** convert lattice note → TeX short note (hep-lat).
3. **Desk (second new):** BBN constraint paper only after T_c-scan curve exists and chain-dependent numbers are banned from the manuscript.
4. **Do not** start a multi-claim “PRTOE overview” paper.
5. **Do not** promote OPEN-THEORY / OPEN-MACHINE files on completion status alone.

---

*Report filed 2026-08-02. Re-verify packages against build logs and greps; do not treat this file as an endorsement or submission authorization.*
