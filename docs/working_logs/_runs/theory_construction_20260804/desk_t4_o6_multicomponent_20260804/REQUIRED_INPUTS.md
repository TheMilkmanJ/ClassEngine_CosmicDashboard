# REQUIRED_INPUTS.md — O6 OPEN-SCHEMA deepen (no free dial)

**Package:** `desk_t4_o6_multicomponent_20260804`  
**Date:** 2026-08-04  
**Rules:** do **not** invent MeV; do **not** free \(N_\mathrm{med}/\eta\); do **not** free radiation fraction \(f\); do **not** free pre-door \(a\)-ratio to target; leave MCMCs  
**Schemas:** [`SCHEMAS.md`](./SCHEMAS.md)  
**Gap anchors (stocked, reconfirmed):** door \(T_\mathrm{eff}=2.827\,\mathrm{keV}\); \(\rho_\mathrm{MeV}/\rho_\mathrm{eff}=5.54\times10^{10}\)

---

## 0. Independence conditions (all schemas)

A candidate input is **legal** only if:

| # | Condition |
|---|---|
| I1 | Inputs do **not** include target \(T=1\,\mathrm{MeV}\) or \(\rho_\mathrm{MeV}\) as fit data |
| I2 | Inputs do **not** include free \(N_\mathrm{med}\), free \(\eta\), free focus \(F\) dialed to bar |
| I3 | Inputs do **not** use \(N_\mathrm{med}=1/c_s\) as identity (M2b coincidence) |
| I4 | Inputs do **not** silently set radiation fraction \(f\) so door hits MeV |
| I5 | Inputs do **not** free \(a_\mathrm{pre}/a_\mathrm{door}\) or blueshift factor to MeV |
| I6 | Late-lock / S2 suppression dial is **not** reused with opposite sign as MeV fund |
| I7 | P1+P2 sign premises are **not** sold as temperature |

Violating I1–I5 → **N_med rename / fabrication**. Violating I6 → **sign conflict**. Violating I7 → **wrong residual**.

---

## S1 — Genesis cascade (task #11)

### Missing objects (minimal package)

To promote S1 from OPEN-SCHEMA toward a scored land, **all** of the following must be supplied **without** MeV-target fitting:

| Symbol / object | Meaning | Corpus state | Independence |
|---|---|---|---|
| **Portal equilibration proof at genesis \(T\)** | \(\Gamma/H\gg1\) with **controlled** rate normalization (minimal vertex vs fuller gates) | Candidate priced; prefactor band open | Must not back-solve rates from BBN \(T\) |
| **\(T_\mathrm{dec}\) UV completion** | Freeze-out consistent with EFT when \(T_\mathrm{dec}>f\) | Caveat named; not closed | No free “effective \(N\) before dec” |
| **Genesis-era \(g_{*S}\) (or partial-equilibration map)** | Closes ζ gap vs committed \([0.25,0.35]\) | First pass overshoots \(\times1.2\)–\(1.9\); owners named, none chosen | **PROMOTE gate** of `genesis_cascade_assembly.py` |
| **Dark reheat chain** | If not single \(27\to14\), written alternate | Optional owner (c) of ζ gap | Not a free ζ dial |
| **Handoff to door / RP-A** | How genesis-funded SM bath presents at shear door without inventing door MeV from keV dial | Unwritten as closed dynamics | Must not reintroduce free \(N_\mathrm{med}\) at door |

### Already independent (do not re-derive as residual)

| Object | Status |
|---|---|
| \(\kappa=1.4\times10^{-31}\,\mathrm{eV}^{-2}\) operating point | Recorded |
| \(m_{e0}\), \(M_\mathrm{Pl}\), \(f\sim3\times10^{14}\,\mathrm{eV}\) | Recorded |
| Door/floor keV arithmetic | Stocked; **under** MeV |
| Free \(N_\mathrm{med}\) fabricated path | Reported only; **not** input |

### Minimal construction checklist (S1)

- [ ] Rate-controlled equilibration (band → number or kill)  
- [ ] \(T_\mathrm{dec}\) story UV-honest  
- [ ] ζ lands inside committed window **or** committed window revised with **independent** reason (not O6 target)  
- [ ] No free \(N_\mathrm{med}/\eta/F/f/a\)-ratio to MeV  
- [ ] Explicit non-claim: bounce O2 not closed  

Until boxes honest: **OPEN-SCHEMA / OPEN-BLOCKED**, not land.

---

## S2 — SM two-scale bath

### Missing objects

| Symbol / object | Meaning | Corpus state | Independence |
|---|---|---|---|
| **Pre-door temperature history \(T_\mathrm{SM}(a)\)** | Adiabatic (or computed non-adiabatic) SM bath through contraction | Schema only; door numbers cold | Must come from S1 or other **non-dial** dynamics |
| **Bath survival through local rebounds** | Patchy doors / joints do not destroy or recool bath below MeV if MeV was pre-funded | Named; uncomputed | Not free survival efficiency \(\eta_\mathrm{bath}\) to target |
| **Homogenization / Tolman bookkeeping** | How local \(T\) becomes BBN-compatible FRW radiation | Open if inhomogeneous | No free averaging factor to MeV |
| **Reconciliation language lock** | Metric-off vs hydro-exit naming (M4–M8) | §20 candidate | Does **not** price \(T\) |

### What S2 does **not** require (and must not invent)

- Free medium compression \(N_\mathrm{med}\) at door  
- Identification of door \(\rho_\mathrm{eff}\) with MeV bath  
- New portal dial “large enough to heat” (portals tiny is recorded)

### Collapse rule

If pre-door \(T_\mathrm{SM}\) is not independently MeV-class, S2 **cannot** fund O6. Residual either:

1. moves to **S1** (genesis), or  
2. remains **cold-at-door OPEN-BLOCKED**, or  
3. honest **under-fund disposition** of silhouette  

### Minimal construction checklist (S2)

- [ ] Written \(T_\mathrm{SM}(a)\) with I1–I5  
- [ ] Survival / joint computation or priced bound (no free \(\eta\))  
- [ ] Explicit: two-scale ≠ door heat bath  
- [ ] If \(T_\mathrm{SM}(\mathrm{door})\sim\) keV/eV on stocked anchors, **do not** claim MeV land  

---

## S3 — Multi-component radiation arrival law

### Missing objects (this is the empty core)

| Symbol / object | Meaning | Corpus state | Independence |
|---|---|---|---|
| **Radiation arrival law \(\mathcal{L}_\mathrm{rad}\)** | Equation or matching rule fixing \(\rho_\mathrm{rad}\) or \(T_\mathrm{rad}\) at re-entry / early expansion from **legal** parts | **Empty** — only named in `rho_bounce.py` | **Must not** contain MeV target, free \(f\), free \(N_\mathrm{med}\) |
| **Component split definition** | What is condensate vs radiation (stress-energy projectors / species) | Sketch only | Floor remains CSW ceiling, not heat |
| **Matching across door / hydro exit** | Israel or continuous-substrate matching for radiation leg | Israel \(S_{ab}\) content open elsewhere; not O6 land | No free junction heat |
| **BBN-facing \(g_*\) and species content** | Standard or derived | \(g_*=10.75\) bar used in gap script | Not a dial to close \(\rho\) gap |

### Forbidden “inputs” (killed as rename)

| Pseudo-input | Why forbidden |
|---|---|
| \(T_\mathrm{rad,door}:=1\,\mathrm{MeV}\) | Invent MeV |
| \(f\) with \(f\rho_\mathrm{eff}=\rho_\mathrm{MeV}\) | Free fraction = compression dial |
| \(N_\mathrm{med}\) in radiation leg | K1 fabricated |
| \(\eta\) heat efficiency to MeV | K1 |
| \(N_\mathrm{med}=1/c_s\) | K2 coincidence |

### Minimal construction checklist (S3)

- [ ] Write \(\mathcal{L}_\mathrm{rad}\) with **zero** free dials to MeV  
- [ ] Show floor and radiation are **different objects** (wrong-object kill stays)  
- [ ] Score \(T_\mathrm{rad}\) **after** law is fixed — not before  
- [ ] If law is “import S1 adiabatics,” say so and grade under S1, not as independent land  

---

## Shared stocked anchors (reference only — not free)

| Anchor | Value | Role |
|---|---|---|
| \(m\) | \(2.24\times10^{-20}\,\mathrm{eV}\) | Floor PAID |
| \(\lambda\) | \(2\times10^{-91}\) | Floor PAID |
| \(\rho_\mathrm{bounce}^{1/4}\) | \(1.059\,\mathrm{keV}\) | Not heat bath |
| Door \(T_\mathrm{eff}\) | \(2.827\,\mathrm{keV}\) | Legal M2; under MeV |
| Door \(T_\mathrm{rad}\) | \(146.4\,\mathrm{eV}\) | Radiation piece; colder |
| MeV bar | \(1\,\mathrm{MeV}\), \(g_*=10.75\) | Demand, **not** input to fit |
| Fab \(N_\mathrm{med}\) (\(\eta=1\)) | \(+6.184\) | Fabricated report only |
| Late-lock \(N_\mathrm{med}\) (diagnostic) | \(-2.621\) | Opposite sign; demoted window; conflict strengthens as \(\Theta\to0\) |

---

## One-line demand

**Every surviving schema’s next content must price temperature history or radiation law from legal micro / recorded portals without free \(N_\mathrm{med}\), free \(f\), free \(a\)-ratio, or inventing MeV — or the residual stays OPEN-BLOCKED / honest under-fund.**

---

*End REQUIRED_INPUTS.md*
