# Fairbank desk workload — full freeze (2026-08-10)

> **Workload:** re-derive every lab-facing neutrino number that would justify a physical
> 0νββ test under the model relation \(m_1 = \rho_\Lambda^{1/4}\).
>
> **Verdict:** **LAB WINDOW GREEN.** Baseline nEXO at favourable ME remains the decisive
> instrument. Nulls do not confirm. Cosmology scaffolding is directionally supportive but
> **not** a Bayes win. Fairbank letter / arXiv post remain **owner HOLD**.

## 0. One-page certificate (signable)

Under the hypothesis \(m_1 = \rho_\Lambda^{1/4} \approx 2.25\,\mathrm{meV}\), normal
ordering, free Majorana phases, and paper NuFIT-class mixings
(\(\sin^2\theta_{12}=0.307\), \(\sin^2\theta_{13}=0.022\),
\(\Delta m^2_{21}=7.42\times10^{-5}\,\mathrm{eV}^2\),
\(\Delta m^2_{31}=2.51\times10^{-3}\,\mathrm{eV}^2\)):

| Quantity | Value | Grade |
|---|---|---|
| Phasor contributions \(\lvert U_{ei}\rvert^2 m_i\) | **(1.525, 2.673, 1.103) meV** | machine-reproduced |
| \(m_{\beta\beta}\) window | **[0.045, 5.301] meV** → quote **[0.04, 5.3] meV** | machine-reproduced |
| \(\Sigma m_\nu\) | **61.30 meV** (relation ~61.35) | machine-reproduced; **not a discriminator** |
| Minimal NO (\(m_1=0\)) window | **[1.48, 3.69] meV** | machine-reproduced |
| Discriminating band | **3.69–5.30 meV** | machine-reproduced |
| Flat-phase P(\(m_{\beta\beta}>4.7\,\mathrm{meV}\)) | **10.8%** | machine-reproduced |
| Flat-phase P(in discriminating band) | **31.7–31.8%** | machine-reproduced |
| Ba-tag 2.35 meV: model / min-NO | **69.1% / 63.7%** | no discrimination |
| Ceiling under ±1σ one-param NuFIT shifts | **5.220–5.383 meV** (span **0.163 meV**) | **stable** |
| Inverted ordering window (anti-control) | **[18.6, 49.1] meV** | no overlap with model ceiling |
| Green-light lab window | **TRUE** | `adversarial_desk.json` |

**Kill structure (phases free; frozen):**

| Outcome | Verdict on model |
|---|---|
| Confirmed \(0\nu\beta\beta\) with \(m_{\beta\beta} > 5.3\,\mathrm{meV}\) | **Killed** |
| Confirmed signal in **3.69–5.3 meV** | Minimal NO impossible; model gains weight |
| Confirmed signal ~1.5–3.7 meV | Compatible with min-NO **and** much of model phase space — **weak** |
| Null at any planned sensitivity | **Does not confirm; does not kill** |
| Independent proof neutrinos are Dirac | **Kills** Majorana requirement (P-2026-020) |

**Certificate sentence:**

> Minimal normal ordering cannot exceed **3.69 meV**. This hypothesis reaches **5.30 meV**.
> Baseline nEXO at favourable \(^{136}\)Xe ME (quoted reach **4.7 meV**) sits entirely inside
> the discriminating band; flat-phase detection probability is **~11%**, and **all** of that
> probability is discriminatory. A detection above **5.3 meV** kills the model. A null does
> not confirm it. \(\Sigma m_\nu \approx 61\,\mathrm{meV}\) is scaffolding, not the lab story.

---

## 1. Workload execution log

| Step | Command / action | Result |
|---|---|---|
| 1a | `python3 scripts/mbb_paper_verify.py` | **ALL CONTROLS PASS** (M-A…M-I) |
| 1b | `python3 scripts/funnel_edge_identity.py` | **ALL CONTROLS PASS** (F-A…F-I) |
| 1c | `python3 scripts/neutrino_cone_margin.py` | PASS — \(Q_\nu\) never reaches 2/3 (all-positive) |
| 1d | `python3 scripts/neutrino_fork_decide.py` | PASS — P-2026-012 stands; Koide-ν branch withdrawn |
| 1e | `python3 scripts/neutrino_Q_sign_branch.py` | PASS — sign-branch honesty recorded |
| 2 | Adversarial layer → `adversarial_desk.json` | **green_light_lab_window: true** |
| 3 | This REPORT + `TODO.md` | frozen |

Logs live next to this file. Reproducible adversarial script:
`scripts/fairbank_desk_adversarial.py`.

---

## 2. Mass ladder and \(m_{\beta\beta}\) envelope

### 2.1 Contributions at \(m_1 = 2.25\,\mathrm{meV}\) (paper parameters)

| term | meV |
|---|---:|
| \(\lvert U_{e1}\rvert^2 m_1\) | 1.525 |
| \(\lvert U_{e2}\rvert^2 m_2\) | 2.673 |
| \(\lvert U_{e3}\rvert^2 m_3\) | 1.103 |
| floor = middle − others | **0.0448** |
| ceiling = sum | **5.301** |
| \(\Sigma m_\nu\) | **61.30** |

Floor exists only because the middle term exceeds the other two. Margin **0.045 meV** on
\(O(2)\) terms — not symmetry-protected. **Conclusions use the ceiling.**

### 2.2 Minimal normal ordering (\(m_1 = 0\))

Window **[1.484, 3.688] meV**. Ceiling **3.69 meV** is the hard wall for discrimination.

### 2.3 Anti-controls (`mbb_paper_verify`)

| Control | Result |
|---|---|
| Derived anchor 2.2599 vs observed 2.25 | Floor moves (0.045 → 0.039); **ceiling stable** (5.301 → 5.309) |
| Inverted ordering | Window **[18.6, 49.1] meV** — far above model ceiling |

### 2.4 \(m_1\) scan (paper mixings)

| \(m_1\) (meV) | floor | ceiling | \(\Sigma\) | margin |
|---:|---:|---:|---:|---:|
| 0.00 | 1.484 | 3.688 | 58.71 | +1.484 |
| 1.00 | 0.823 | 4.384 | 59.78 | +0.823 |
| 2.00 | 0.197 | 5.114 | 60.98 | +0.197 |
| **2.25** | **0.045** | **5.301** | **61.30** | **+0.045** |
| 2.3245 (paper funnel edge) | 0.000 | 5.358 | 61.40 | ~0 |
| 3.00 | 0.000 | 5.876 | 62.31 | −0.399 |
| 5.00 | 0.000 | 7.487 | 65.31 | −1.506 |
| 10.00 | 1.691 | 11.864 | 74.29 | −3.938 |

Ceiling rises ~44% from min-NO (3.69) to model \(m_1\) (5.30). That rise **is** the lab claim.

---

## 3. Experiment overlay

### 3.1 Projected reaches (letter literature; **4.7 meV is owner-owned**)

| experiment | isotope | reach (meV) | vs 5.30 ceiling | discriminatory? |
|---|---|---|---|---|
| **nEXO** | \(^{136}\)Xe | **4.7 – 20.3** | overlaps **4.7–5.3** | **YES** (favourable ME) |
| LEGEND-1000 | \(^{76}\)Ge | 9 – 21 | entirely above | no discovery overlap |
| CUPID | \(^{100}\)Mo | 12 – 34 | entirely above | no discovery overlap |

### 3.2 Flat-phase detection probabilities

| reach | this model | minimal NO | separates? |
|---|---:|---:|---|
| **4.7 meV** (baseline nEXO) | **10.8%** | **0%** | **yes** |
| **2.35 meV** (Ba tagging ×2 in \(m_{\beta\beta}\)) | **69.1%** | **63.7%** | **no** |

Discriminating band occupancy: **31.7–31.8%**. Entire baseline nEXO 10.8% sits in that band.

**Rule of thumb frozen here:** barium tagging makes the test *likely*; baseline nEXO makes it
*decisive*.

### 3.3 Phase-prior stability (adversarial)

| grid | P(>4.7) | P(band) |
|---|---:|---:|
| n=400 | 0.1082 | 0.3175 |
| n=800 | 0.1082 | 0.3175 |
| n=1200 | 0.1082 | 0.3175 |
| n=800 + π/4 offset | 0.1082 | 0.3175 |

Order-of-magnitude stable; sub-percent variation. Flat-phase convention stated, not hidden.

### 3.4 NuFIT ±1σ one-parameter extremes (ceiling stability)

| shift | model ceiling (meV) | min-NO ceiling (meV) | floor (meV) |
|---|---:|---:|---:|
| s12 +1σ | 5.383 | 3.794 | 0.181 |
| s12 −1σ | 5.220 | 3.583 | 0.000 |
| s13 ±1σ | 5.271–5.331 | 3.658–3.719 | thrash |
| dm21 ±1σ | 5.266–5.337 | 3.652–3.725 | thrash |
| dm31 ±1σ | 5.295–5.307 | 3.683–3.694 | thrash |

- Model ceiling range: **5.220 – 5.383 meV** (span **0.163 meV**) → **stable weapon**.
- Floor thrash includes exact zero — **do not sell the floor**.
- Min-NO ceiling always **≤ 3.794 < 5.220** → discriminating band **never collapses** under these shifts.

---

## 4. Cosmology scaffolding (booked; do not mix)

### 4.1 Old-BAO production pair — Stage B BOOKED

Authority: `bbnfix_booking_20260808_005626` · `PRTOE_CHAIN_TABLES.md`

| chain | \(m_{\mathrm{ncdm}}\) | \(H_0\) |
|---|---|---|
| dyad | **0.0671 ± 0.0583** | 70.052 ± 0.716 |
| lcdm | **0.0192 ± 0.0174** | 68.345 ± 0.343 |

Evidence honesty: sample-cov Laplace **ΔlnZ ≈ +0.21** (soft modes). **Not nested.**

### 4.2 DESI-DR2 twins — Stage A BOOKED (separate instrument)

Authority: `desidr2_bbnfix_booking_20260810_053127`

| chain | \(m_{\mathrm{ncdm}}\) | \(H_0\) |
|---|---|---|
| dyad | **0.0508 ± 0.0473** | 70.299 ± 0.541 |
| lcdm | **0.0138 ± 0.0128** | 68.729 ± 0.250 |

Direction: model keeps mass **up** relative to ΛCDM twin. Soft errors. Hessian ΔlnZ_H
diagnostic fail — **not bookable as evidence**.

### 4.3 Forbidden

- Mixing old-BAO and DESI posteriors into one “joint” number.
- Quoting Hessian ΔlnZ_H as Bayes factor.
- Claiming nested ΔlnZ (gold PolyChord **OPEN-MACHINE**).
- Selling \(\Sigma m_\nu \approx 61.35\,\mathrm{meV}\) as a lab discriminator (~2.6 meV above
  min-NO floor vs ~20 meV planned cosmological resolution).

### 4.4 Cosmology kill board (track; not closed today)

| Outcome | Effect |
|---|---|
| Robust inverted ordering | Kills NO + \(m_1=\rho_\Lambda^{1/4}\) package |
| Robust \(\Sigma m_\nu \gtrsim 70\,\mathrm{meV}\) | Kills 61.35 relation |
| Model-conditional upper limit that still forbids ~61 meV | Relation under lethal pressure |
| Nested decisive loss on DESI gold | Cosmology scaffolding weakens; **lab window arithmetic unchanged** |

---

## 5. Funnel edge and mechanism integrity

### 5.1 Funnel-edge identity (`funnel_edge_identity.py` — all controls pass)

| Object | Value |
|---|---|
| Paper margin \(M(2.25\,\mathrm{meV})\) | **+0.0448 meV** |
| NuFIT 5.0 margin | **−0.00022 meV** (sign flips) |
| Funnel edge \(m_1^*\) paper / NuFIT | **2.3245 / 2.2496 meV** |
| \(\rho_\Lambda^{1/4}\) (Planck 2018 path in script) | **2.2395 ± 0.0108 meV** |
| Identity gap \(m_1^* - \rho_\Lambda^{1/4}\) | **+0.010 meV ≈ 0.04σ** of \(\sigma(m_1^*)\) |
| \(\sigma(m_1^*)\) today / JUNO-era | **0.246 / 0.062 meV** (θ₁₃ bottleneck post-JUNO) |
| Closure phases on edge | \((\alpha_{21},\alpha_{31})=(\pi,0)\) CP-conserving |

**Honesty:** central-value coincidence only; **not** a precision discovery. Floor existence is a
~50/50 coin on today’s θ₁₂. Do **not** adopt ee-texture-zero closure as a paper strategy — it
predicts \(m_{\beta\beta}\lesssim 0.05\,\mathrm{meV}\) and **inverts** the discriminating band
into a falsifier; constitution also treats flavor structure as not writable.

### 5.2 Majoron mode (wrong instrument for discovery)

\(\langle g_{ee}\rangle = m_{\beta\beta}/v_L\) at \(m_{\beta\beta}\sim 3.05\,\mathrm{meV}\):

| \(v_L\) point | \(g_{ee}\) | vs KLZ-class \(\sim 10^{-5}\) |
|---|---:|---:|
| MeV-scale (4.18 MeV) | \(7.3\times 10^{-10}\) | \(\sim 7\times 10^{-5}\) of limit |
| GeV | \(3.1\times 10^{-12}\) | \(\sim 3\times 10^{-7}\) |
| 2.4 TeV ceiling | \(1.3\times 10^{-15}\) | \(\sim 10^{-10}\) |

**No observable Majoron continuum mode** at surviving points — kill-only bet. CMB-S4 remains the
\(g\sim 10^{-8}\)–\(10^{-9}\) selector for the MeV-scale \(v_L\) corner (P-2026-025).

### 5.3 Fork decision

`neutrino_fork_decide.py`: **P-2026-012 stands** (\(\Sigma \approx 61.3\,\mathrm{meV}\),
\(m_1 \approx 2.24\,\mathrm{meV}\)). Koide-neutrino branch withdrawn as a prediction (parameter-free
ratio test misses ~4%; charge-selector arguments). Do not quote 58.5 meV as the model number.

### 5.4 Open mechanism (does **not** block lab green light)

- Exact \(\mu = 2.25\,\mathrm{meV}\) un-derived (state as relation, not derivation of DE value).
- Flavor distribution among eigenstates open; **phases free until proven otherwise**.
- \(\rho_{\mathrm{inf}}\) closure / \(\alpha_c\) instrument offline.

---

## 6. What Fairbank still owns (external)

Letter asks (a–c) remain valid:

1. Is the meV-window form useful to the 0νββ community (two-sided kill + soft floor stated up front)?
2. Critical eye on BBN (self-adverse; not neutrino kill).
3. **Are 4.7 meV (nEXO favourable ME) and Ba-tagging ×4 half-life → ×2 in \(m_{\beta\beta}\)** still correct?

Every probability in §3 moves with those two experimental numbers.

---

## 7. Forbidden claims after this freeze

- “We have nested evidence for the neutrino sector.”
- Mixing DESI + old-BAO \(\Sigma m_\nu\) posteriors.
- Null 0νββ as confirmation.
- Floor 0.04 meV as a protected prediction.
- \(\Sigma m_\nu = 61.35\,\mathrm{meV}\) as a near-term lab discriminator.
- Posting `neutrino-mbb` without Fairbank / endorsement path (owner HOLD).
- Inventing arXiv IDs.

---

## 8. Artifacts

```
docs/working_logs/_runs/fairbank_desk_workload_20260810/
  REPORT.md                 ← this freeze
  TODO.md                   ← checklist (all desk items DONE)
  adversarial_desk.json     ← machine tables + green_light
  mbb_paper_verify.log
  funnel_edge_identity.log
  neutrino_cone_margin.log
  neutrino_fork_decide.log
  neutrino_Q_sign_branch.log

scripts/fairbank_desk_adversarial.py   ← reproducible adversarial layer
scripts/mbb_paper_verify.py            ← paper number controls
scripts/funnel_edge_identity.py        ← funnel / coin honesty
```

## 9. Bottom line

| Question | Answer |
|---|---|
| Is the lab arithmetic real? | **Yes** — every paper number reproduces from oscillation data. |
| Is the ceiling stable? | **Yes** — ±0.16 meV under ±1σ one-param shifts. |
| Is there discrimination vs min-NO? | **Yes** — band 3.69–5.30 meV; baseline nEXO only. |
| Does cosmology already win the case? | **No** — upward \(m_{\mathrm{ncdm}}\) direction only; Laplace weak; nested open. |
| Worth a physical test? | **Yes, as a falsifiable 0νββ target** — not as a confirmation machine. |
| Owner next step? | Fairbank letter (HOLD) → endorsement → `neutrino-mbb` post only. |

**Desk workload: COMPLETE. Lab window: GREEN. Physical-test case: stands.**
