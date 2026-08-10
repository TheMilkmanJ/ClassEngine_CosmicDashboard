# CORPUS_INVENTORY — every stocked junction / Israel / matching equation

**Package:** `israel_junction_content_20260804/`  
**Date:** 2026-08-04  
**Rule:** file:line only; **no** invented surface stress; **no** desk-made Israel identities sold as stocked.  
**Israel-class \(S_{ab}\) / \([K_{ab}]\) content stocked in corpus?** **No.**

---

## 0. How to read grades

| grade | meaning |
|---|---|
| **PAID** | equation / number computed or recorded and used as legal input |
| **PARTIAL** | form written; domain incomplete or one sector open |
| **CANDIDATE declaration** | matching rule licensed under P1+P2; not Derived |
| **CONSTRAINT** | bound any future matching must satisfy; not a mechanism |
| **FABRICATED** | labeled free knob / toy; **not** legal land |
| **MISSING_INPUT** | named as needed; **no** stocked equation |
| **DEAD / RETIRED** | attempted close failed with proof |

---

## 1. Phase I exterior / door (metric-ON)

| # | equation / statement | grade | file:line |
|---|---|---|---|
| I-1 | \(H^2 = 8\pi G\rho/3 + \sigma^2/3\) | **PAID** shear-corrected Friedmann | `scripts/bounce_m2_junction.py:64` · `scripts/bounce_rpA_scaffold.py:21,155` · `scripts/bounce_fa3_hcross_attempt.py:76` |
| I-2 | \(\sigma \propto a^{-3}\) (shear decay on expansion; inverse on contraction) | **PAID** | `scripts/bounce_m2_junction.py:62` · `scripts/bounce_rpA_scaffold.py:22,153` |
| I-3 | Local door: \(\sigma = 1/\xi\) \(\Rightarrow\) \(a_\mathrm{loc}=(\sigma_0\xi)^{1/3}\) | **PAID** | `scripts/bounce_m2_junction.py:78–79` · `scripts/bounce_fa3_hcross_attempt.py:73` |
| I-4 | Shear-dom door: \(H_\mathrm{door}=1/(\sqrt{3}\,\xi)\), \(R_H/\xi\to\sqrt{3}\) | **PAID** | `scripts/bounce_fa3_hcross_attempt.py:319–320` · `scripts/bounce_m4_arrow_boundary.py:40` · `scripts/bounce_n2_match_book_check.py:116` |
| I-5 | \(\rho_\mathrm{bounce}=m^4/\lambda\) (floor number, not turn) | **PAID** | `scripts/bounce_fa3_hcross_attempt.py:56–57` · `scripts/bounce_rpA_scaffold.py:88–89` |
| I-6 | \(c_s=\sqrt{3\alpha}\) | **PAID** recorded | `scripts/bounce_fa1_transphononic_table.py:43` · `scripts/bounce_fa3_hcross_attempt.py:48–49` |
| I-7 | \(\xi\) anchor \(402\,\mathrm{AU}\) → \(\xi\) in \(\mathrm{eV}^{-1}\) | **PAID** | `scripts/bounce_m2_junction.py:34,58` · `scripts/bounce_fa3_hcross_attempt.py:40,60–61` |

**Reconfirm anchors (2026-08-04, `bounce_n2_match_book_check`):**  
\(c_s\approx0.14796\), \(H_\mathrm{door}\approx1.894\times10^{-21}\,\mathrm{eV}\), \(|H_\mathrm{kin}(\Theta=1,d=3)|/H_\mathrm{door}\approx0.08542\), \(\Theta_\mathrm{lock}(d=3)\approx11.71\).

---

## 2. Acoustic kinematic map (when metric defined)

| # | equation / statement | grade | file:line |
|---|---|---|---|
| A-1 | \(H_\mathrm{kin}=\langle\Theta\rangle_\mathrm{phys}/d=\Theta_\mathrm{heal}\,c_s/(d\,\xi)\) | **PARTIAL** domain: Phase I (and Phase III diagnostic only) | `scripts/bounce_fa3_hcross_attempt.py:8–13,183–185` · `scripts/bounce_n2_match_book_check.py:77–78` · package dict: `n2_match_book_20260804/MATCHING_DICTIONARY.md:11–14` |
| A-2 | \(\|H_\mathrm{kin}(\Theta=1,d=3)\|/H_\mathrm{door}=c_s/\sqrt{3}\approx0.0854\) | **PAID** arithmetic | `scripts/bounce_fa3_hcross_attempt.py:336–337,414` · `scripts/bounce_n2_match_book_check.py:128–132` |
| A-3 | \(\Theta_\mathrm{lock}(d=3)=H_\mathrm{door}\cdot 3\cdot\xi/c_s\approx11.71\) for door-magnitude lock | **PAID** inversion bookkeeping | `scripts/bounce_fa3_hcross_attempt.py:323–326` · `scripts/bounce_n2_match_book_check.py:130–133` |
| A-4 | \(H_F(\rho)=\sqrt{8\pi G\rho/3}/M_\mathrm{Pl}\) (magnitude, flat) | **PAID** | `scripts/bounce_fa3_hcross_attempt.py:64–66` · `scripts/bounce_n2_match_book_check.py:53–54` |
| A-5 | Obstruction A: \(H_\mathrm{kin}=0\) at finite \(\rho\) \(\Rightarrow\) Friedmann conflict metric-ON | **PAID nogo** | `scripts/bounce_fa3_hcross_attempt.py:264–271,371–378` · `scripts/bounce_n2_match_book_check.py:156–169` |

**Forbidden application:** \(H=\langle\Theta\rangle/d\) as **exterior** \(H\) through Phase II — domain fence (`n2_match_book_20260804/DOMAIN.md:79–86`, `MATCHING_DICTIONARY.md:20–25`).

---

## 3. F-A1 medium-sector translation table

| # | equation / statement | grade | file:line |
|---|---|---|---|
| F1-1 | \(\varepsilon(x)=x\sqrt{1+x^2/4}\), \(x=k\xi\) | **PAID** medium sector | `scripts/bounce_fa1_transphononic_table.py:46–47,10` |
| F1-2 | \(v_g/c_s=(1+x^2/2)/\sqrt{1+x^2/4}\); \(v_g>c_s\) for \(x\gtrsim1\) (metric end quantified) | **PAID** | `scripts/bounce_fa1_transphononic_table.py:50–51,11–14,87–89` |
| F1-3 | Coherence \(v^2=\tfrac12[(1+x^2/2)/\varepsilon-1]\), \(u^2=1+v^2\) | **PAID** | `scripts/bounce_fa1_transphononic_table.py:54–55,15–19` |
| F1-4 | \(\omega/H_\mathrm{door}=\sqrt{3}\,c_s\,\varepsilon(x)\); quench iff \(\omega/H<1\) | **PAID** | `scripts/bounce_fa1_transphononic_table.py:58–59,20–24` |
| F1-5 | Adiabatic/quench split \(x^*\approx2.46\) | **PAID** | `scripts/bounce_fa1_transphononic_table.py:75–84` · reconfirm `bounce_n2_match_book_check.py:185–191` |
| F1-6 | SM photon inverse at boundary | **OPEN** named corner | `scripts/bounce_fa1_transphononic_table.py:26–32,100–101` |
| F1-7 | Inverse \(g\to\) medium as closed F-A1 | **RETIRED** (underdetermined) | `docs/PRTOE_FAILURES_LEDGER.md:1251–1262` |

---

## 4. Medium Phase II dynamics (fluid only — not exterior junction)

| # | equation / statement | grade | file:line |
|---|---|---|---|
| M-1 | Averaging identity: \(\mathrm{d}\langle\Theta\rangle/\mathrm{d}t=-\langle\Theta\rangle^2-\mathrm{Var}(\Theta)+\mathrm{Stress}\) (stress from interaction + quantum gradient) | **PAID** 1D identity class | `scripts/bounce_averaging_decomposition.py:8–15` · scaffold `bounce_rpA_scaffold.py:29–33` |
| M-2 | Repulsive GPE: \(i\partial_t\psi=-\frac12\nabla^2\psi+(|\psi|^2-1)\psi\) | **PAID** toy form | `scripts/bounce_rpA_scaffold.py:27` |
| M-3 | 0D stand-in: \(\dot n=-n\Theta\), \(\dot\Theta=-\Theta^2+\kappa(n-1)-\gamma\Theta\) | **PAID toy** | `scripts/bounce_fa3_hcross_attempt.py:107–110` |
| M-4 | Medium \(\langle\Theta\rangle:-\to0\to+\) with \(\dot\Theta>0\) at cross (0D/1D class) | **PAID medium layer** | `scripts/bounce_fa3_hcross_attempt.py:120–131,222–234` |
| M-5 | Homogeneous average kills stress channel | **PAID** (nogo consistent) | `scripts/bounce_averaging_decomposition.py:12–15` · FA3 report |

---

## 5. Boundary / handoff joints (constraints, not Israel \(S_{ab}\))

| # | equation / statement | grade | file:line |
|---|---|---|---|
| B-1 | Spacelike door (shear-dom): \(\delta < 6\,(L/R_H)\) with \(R_H=\sqrt{3}\,\xi\) | **CONSTRAINT** | `scripts/bounce_m4_arrow_boundary.py:12–19,46–48` |
| B-2 | Crossing offset: \(\mathrm{d}t_\mathrm{cross}=\delta\,R_H/6\) | **CONSTRAINT** | `scripts/bounce_m4_arrow_boundary.py:21–23` |
| B-3 | Achronal re-entry: non-metric hold \(\ge\mathrm{d}t_\mathrm{cross}(\delta_\mathrm{max})\) | **CONSTRAINT** | `scripts/bounce_m4_arrow_boundary.py:25–28,51–54` |
| B-4 | Task4 J1: \(\mathrm{Mach}=v/c_s=(H_\mathrm{fast}/H_\mathrm{mean})/(\sqrt{3}\,c_s)\); \(H_\mathrm{mean}\xi=1/\sqrt{3}\) | **CONSTRAINT/joint** | `scripts/bounce_task4_handoff_joints.py:11–17,82–83` |
| B-5 | Task4 J2: hold \(\ge0.0427\,\delta\,t_\mathrm{heal}\); self-consistency \(\delta\lesssim23\) | **CONSTRAINT/joint** | `scripts/bounce_task4_handoff_joints.py:19–23,45,100–104` |
| B-6 | Task4 J3: planarity / axis ratios at first crossing | **CONSTRAINT/joint** | `scripts/bounce_task4_handoff_joints.py:25–28,106–109` |
| B-7 | Quench energy budget \(\rho_\mathrm{quench}\approx0.5\,m c_s^2/\xi^3\) (MeV ledger; **fails** O6) | **PAID dead channel** | `scripts/bounce_task5_door_budget.py:8–13,32–45` |

**Named open (task4):** wall between rebounding pocket and still-contracting exterior — “M4 boundary problem, unresolved” (`bounce_task4_handoff_joints.py:112–114`). **Not** filled by Israel content.

---

## 6. Phase III re-entry matching (declaration)

| # | equation / statement | grade | file:line |
|---|---|---|---|
| R-1 | Gate: \(\langle\Theta\rangle>0\;\wedge\;\ell_\mathrm{grad}\gtrsim\xi\) | **CANDIDATE declaration** (P2 form) | `scripts/bounce_rpA_scaffold.py:40–43` · `fa3_metric_off/CONSTRUCTION.md:39–51` · `scripts/bounce_n2_match_book_check.py:197–200` |
| R-2 | \(H_\mathrm{re}=+\sqrt{8\pi G\rho_\mathrm{re}/3+\sigma_\mathrm{re}^2/3}\) | **CANDIDATE declaration** expanding root | `fa3_metric_off/CONSTRUCTION.md:31–35,41–49` · `n2_match_book_20260804/MATCHING_DICTIONARY.md:30–33` |
| R-3 | \(H_\mathrm{kin}\) at re-entry = **target / diagnostic**, not derivation of square-root sign | **CANDIDATE-REFRAME** (R1) | `n2_match_book_20260804/ALTERNATE_MATCH_RULES.md:7–12` · `MATCHING_DICTIONARY.md:35` |
| R-4 | \(\rho_\mathrm{re}\) closed law (F-A2) | **OPEN** | N1 hunt `scripts/bounce_n1_fa2_amplitude_hunt.py` · n2 DOMAIN §4 |
| R-5 | `can_derive_H_re_without_declaration` | **false** (asserted) | `scripts/bounce_fa3_hcross_attempt.py:350–362,407` · `scripts/bounce_n2_match_book_check.py:201–203` |

---

## 7. Fabricated toy junction (M2) — **not** legal matching

| # | equation / statement | grade | file:line |
|---|---|---|---|
| X-1 | \(\rho_\mathrm{out}=\eta\,\rho_\mathrm{in}\,e^{4N_\mathrm{med}}\) | **FABRICATED** | `scripts/bounce_m2_junction.py:131–141` |
| X-2 | \(T_\mathrm{reh}\) from radiation invert of \(\rho_\mathrm{out}\); \(H_\mathrm{reh}=\sqrt{8\pi G\rho_\mathrm{out}/3}/M_\mathrm{Pl}\) with \(H>0\) **by hand** | **FABRICATED** | `scripts/bounce_m2_junction.py:142–145` |
| X-3 | \(N_\mathrm{med}^\mathrm{needed}=\frac14\ln(\rho_\mathrm{MeV}/\rho_\mathrm{eff})\) | **FABRICATED** sensitivity | `scripts/bounce_m2_junction.py:124–127,196` |
| X-4 | \(N_\mathrm{med}=1/c_s\) as Derived identity | **RETIRED coincidence** | `scripts/bounce_m2b_mixmaster_nmed.py:91–98` · `docs/PRTOE_FAILURES_LEDGER.md:1237–1249` |
| X-5 | Task5: “compression free param (retired) \(N_\mathrm{med}\gtrsim6.2\) fabricated” | **RETIRED as free param** | `scripts/bounce_task5_door_budget.py:46` |

---

## 8. Israel / surface-stress class — **empty**

| # | equation / statement | grade | file:line / search |
|---|---|---|---|
| J-0 | Israel: \([K_{ab}]-[K]h_{ab}=-8\pi G\,S_{ab}\) (or Darmois–Israel thin shell) | **MISSING_INPUT** | **no** bounce-corpus equation; grep over `docs/**/*bounce*` for `Israel`, \(S_{ab}\), \([K]\) → no stocked form |
| J-1 | Surface stress \(S_{ab}\) from medium \(n,v,\Theta\) at re-entry | **MISSING_INPUT** | named need only: `debt_bounce_FA3_20260803/REPORT.md:136–138` · `bounce_full_freeze_20260804/REPORT.md:135` · `n2_match_book_20260804/ALTERNATE_MATCH_RULES.md:19–23` (R3) |
| J-2 | Continuous exterior \(H:-\to0\to+\) at finite \(\rho\) metric-ON | **DEAD** (A) | FA3 + n2 Domain |
| J-3 | Theorem: acoustic re-emergence **forces** expanding root without free branch | **MISSING_INPUT** (N4) | `bounce_residual_demand/CANDIDATE_NEXT.md:163–196` |
| J-4 | Inverse acoustic matching as closed F-A1 | **RETIRED** | `docs/PRTOE_FAILURES_LEDGER.md:1251–1262` |

**Prose mentions of “Israel / junction” without equation content** (demand only, not inventory of stocked physics):

- `docs/working_logs/_runs/debt_bounce_FA3_20260803/REPORT.md:14,136–138`
- `docs/working_logs/_runs/bounce_full_freeze_20260804/REPORT.md:135`
- `docs/working_logs/_runs/theory_construction_20260804/fa3_metric_off/KILL_AND_FALSIFIERS.md:25,57`
- `docs/working_logs/_runs/theory_construction_20260804/bounce_residual_demand/CANDIDATE_NEXT.md:163–196`
- `docs/working_logs/_runs/theory_construction_20260804/n2_match_book_20260804/REPORT.md:36,55`
- `docs/working_logs/_runs/theory_construction_20260804/N2_N3_S2_WAVE_MASTER.md:21`

---

## 9. Match-book alternate rules (inventory of *rules*, not new eqns)

| ID | rule | grade | closes C? | source |
|---|---|---|---|---|
| R0 | \(H_\mathrm{kin}=H_F(\rho)\) default | STOCKED-DEFAULT | **no** | n2 ALTERNATE |
| R1 | \(H_\mathrm{kin}\) target only | CANDIDATE-REFRAME | **no** | n2 |
| R2 | shear-corrected \(H^2=\ldots+\sigma^2/3\) | STOCKED-SHEAR | **no** | I-1 |
| R3 | Israel surface across Phase II | **MISSING_INPUT** | **no** | n2 |
| R4 | continuous H through 0 metric-ON | **DEAD** | no | A |
| R5 | free dial \(H_\mathrm{re}\) | **FORBIDDEN** | no | fence |

Full: `n2_match_book_20260804/ALTERNATE_MATCH_RULES.md`.

---

## 10. Count stamp

| class | count of stocked *equations/statements* above | land as Israel close? |
|---|---|---|
| PAID exterior/door | 7 (I-1…I-7) | no |
| Acoustic map + nogo | 5 (A-1…A-5) | no |
| FA1 table | 5 paid + 2 open/retired | no |
| Medium fluid | 5 | no |
| Boundary constraints | 7 | no |
| Phase III declaration | 3 (R-1…R-3) + opens | no |
| Fabricated M2 | 5 labeled | **forbid as Derived** |
| Israel \(S_{ab}/[K]\) | **0** | **MISSING_INPUT** |

**Inventory verdict:** corpus has a **RECONSTRUCTED match-book** (phases I–III), **PAID door geometry**, **PARTIAL F-A1 medium table**, **CONSTRAINT** boundary joints, and a **declared** expanding root. It does **not** stock any Israel surface stress or force-branch theorem.

---

*End CORPUS_INVENTORY.md*
