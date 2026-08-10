# WHAT_RESIDUAL_DEMANDS — What Page T8 keeps forcing

**Package:** `docs/working_logs/_runs/theory_construction_20260804/page_t8_residual_demand/`  
**Date:** 2026-08-04  
**Protocol:** exploratory “laws as suggestions” + Rule 1 (CANDIDATE only; can-exist + kill-seeking should-not-exist; band fixed before land)  
**Parents:** `page_t8/` · `page_full_freeze_20260804/` · `open_board_split_20260803/PAGE_DEEPER_CONSTRUCTION_NOTE.md` · D1–D3 attempt notes · `PAGE_TURN_ACCEPTANCE_PROTOCOL.md` §4.3  
**Champion:** `coevolve_v13.json` · `input_sha256 = 048de43e1bc766c8f420c54f565a33166c0792c23291ba567cdc6c772f92fca8`  
**Grade of this file:** residual inventory only — **not** a land, **not** a CANDIDATE packet, **not** Page closed  
**`page_curve_claimed`:** **false**

---

## 0. Residual identity

| Field | Value |
|---|---|
| Residual | **T8 early-bin single-valued \(S(u)\)** on dynamical Page instrument |
| Living grade | **OPEN** (Q6); instrument near-miss under D4 freeze |
| Binding definition | For every occupied bin of \(u=\max_{s\le t}v(s)\) with \(\Delta u=0.01\): \(\max S-\min S\le 0.1\cdot S_\star\) |
| Champion sole fail | Bin **\([0.10,0.11)\)**: range/\(S_\star\) = **0.113154…** (need ≤ **0.10**) |
| Joint already PASS | T1–T6 · T2 \(u_{\mathrm{late}}\ge0.9\) · stall_cap≤10 · coevo · **DC3** |
| What does **not** pass binding | `CANDIDATE_TURN_binding` (needs T8_pass); claim flag stays false |
| Prior construction | D1–D3 **exhausted** without joint clear; pure \(G_{\mathrm{TMS}}\) **sticky** |

**Band locked before any future land / packet** (protocol pins; not renegotiated here):

| Outcome | Criterion |
|---|---|
| **ACCEPT joint instrument** | T1–T6 + stall + coevo + DC3 **and** **all** T8 bins range/\(S_\star\) **≤ 0.10** |
| **FAIL / no packet** | Any occupied bin > 0.10, or any joint gate regresses |
| **CANDIDATE packet** | Only after joint ACCEPT **and** claim-decoupling **and** red AGREE |
| **Claim** | Separate step; scorecard **never** sets `page_curve_claimed` true |

---

## 1. What T8 keeps forcing (demand list)

Each line is a **“the instrument keeps pointing at X”** statement from scored arrays + attempt history.  
These are **demands**, not lands. No free header knob is dialed to fake ≤0.10.

### 1.1 Core dynamical demand

| # | Instrument is pointing at… | Why forced | Evidence anchor |
|---|---|---|---|
| **RD1** | A **lower early \(\mathrm{d}S/\mathrm{d}u\)** while crossing \(\Delta u=0.01\) at low evaporation coordinate | Sole fail bin is **monotone** \(S\uparrow,u\uparrow\) (not frozen-\(u\) vertical); range/\(S_\star\) = \(\approx\frac{1}{S_\star}\int \mathrm{d}S/\mathrm{d}u\,\mathrm{d}u\) exceeds 0.10 | `DIAGNOSIS.md`; frames 43–54; this package scorecard re-run |
| **RD2** | Specifically, range in **\([0.10,0.11)\)** must drop from **0.11315…** to **≤0.10** (~**13%** relative cut in bin range, or equivalent shape change) | Only failing bin among 83 occupied; neighbors pass | scorecard `worst_bin` |
| **RD3** | A change that is **not pure \(G_{\mathrm{TMS}}\) rescale** | \(G_{\mathrm{TMS}}\) multiplies early \(\Delta S\) and global \(S_\star\) together → ratio **sticky ~0.11** | `B_A_COEVOLVE_V13_BEST.md`; `PAGE_DEEPER_CONSTRUCTION_NOTE.md` |
| **RD4** | A law that acts in the **early TMS+BS overlap** window \(f\sim0.057\)–\(0.072\) (schedule fraction), not only at late freeze | Fail frames sit in early build; peak \(S\) later at \(i=104\), \(u^*\approx0.267\) | history frames; schedule pins TMS_START=0, TMS_END=0.52 |

Independent arrays diagnostic (same JSON; not a new simulation):

| quantity | value |
|---|---|
| fail frames | 43–54 (n=12) |
| \(\Delta u\) in bin path | ≈ 0.00878 |
| \(\Delta S\) in bin | ≈ 0.001888 |
| rough \(\mathrm{d}S/\mathrm{d}u\) | ≈ 0.215 |
| max \(\Delta S\) for T8 pass | \(0.1\cdot S_\star\) ≈ 0.001669 |
| \(S_\star\) | 0.016688199517780646 |

### 1.2 Joint-gate demand (what residual refuses to trade away)

| # | Instrument is pointing at… | Why forced | Kill if abandoned |
|---|---|---|---|
| **RD5** | **T2** unit-weight reach \(u_{\mathrm{late}}\ge0.9\) (champion 0.9021) | Soften-early-TMS / D1 soft phase flatten early T8 but lose reach | binding false even if T8 green |
| **RD6** | **stall_cap** longest stall ≤10 frames (champion =10, on the wire) | Late dump thrash / densify reintroduce long stalls | coevo gate fail |
| **RD7** | **DC3** weight-invariant reach PASS | D3 densify broke DC3; free-\(w_c\) games risk weight-borne reach | DC3-gated binding false |
| **RD8** | T1–T6 machine + co_frac / swap / peak_in_motion + nulls N1–N4 | Already PASS on champion; residual must not “win T8 by burning unitarity / thermal / continuum” | machine false |

**Compression:** residual is **joint** — early slope fix **and** T2+stall+DC3. Solo T8 green without joint is already documented (D1 family) and is **not** success.

### 1.3 Negative demands (what residual refuses)

| # | Instrument is pointing **away from**… | Why refused | Status |
|---|---|---|---|
| **RD9** | Header thrash on `G_TMS`, `BS_MILD`, `TMS_SHAPE_POWER`, TMS delay, late EXTRA_BS | Post-v13 single-knob: regress T2/stall or sticky ratio | **FORBIDDEN thrash** |
| **RD10** | Pure two-phase header (`PHASE_BS_ONLY_UNTIL_U`) as “the” fix | D1: early T8 better; **T2 not joint** | **EXHAUSTED** |
| **RD11** | Free \(w_c\equiv1\) flip alone | D2: **no-op** on champion path (freeze before former decay) | **EXHAUSTED / no-op** |
| **RD12** | Mode densify / midband retune without new dump law | D3 v35–v38: \(u_{\mathrm{late}}<0.9\), stall/DC3 fail | **EXHAUSTED → thrash** |
| **RD13** | Loosen T8 threshold or subsample bins | Protocol-breaking fake pass | **FORBIDDEN** |
| **RD14** | Treat machine T1–T6 True as CANDIDATE | Binding requires T8; claim-decoupling separate | **FORBIDDEN** |
| **RD15** | Invent an unnamed “island formula” for \(S(u)\) without microphysics license | NO FABRICATIONS; scorecard gates dynamics, not invented closed form | **FORBIDDEN** |
| **RD16** | PolyChord / MCMC as Page instrument path | Fenced; wrong tool class | **FORBIDDEN** |

### 1.4 Process / honesty demands (meta)

| # | Protocol is pointing at… | Why forced |
|---|---|---|
| **RD17** | **Licensed new microphysics** (named coupling / dump / free-Hamiltonian / continuum law) before any coevolve_v39+ production | D4 freeze; header space exhausted |
| **RD18** | Write-once versioned JSON → arrays-only scorecard → joint gates → claim-decoupling → red → claim | PAGE_TURN + claim-decoupling checklist |
| **RD19** | CANDIDATE **levers** only (this package); **no** CANDIDATE **packet** while T8=0.113 | Mission fence |
| **RD20** | Double scrutiny on every lever: can-exist + kill-seeking should-not-exist; band fixed | Exploratory premise protocol |
| **RD21** | Either joint clear under band **or** honest D4 / failures-style near-miss — not “almost green” theater | Residual closes by land *or* freeze honesty |

---

## 2. What the residual is *not* demanding

| Non-demand | Reason |
|---|---|
| Late envelope-stall cure | That was older artifact class; v13 late stall/DC3 already PASS |
| Q2 area-law payment | Distinct ledger row; not dynamical Page (Q6) |
| Strong CP physics | Complete abstention this desk |
| Owner-ship / arXiv tasks | Owner lane |
| Re-running D1–D3 thrash “one more knob” | Exhausted |
| Changing \(\Delta u\) or \(0.1\cdot S_\star\) | Protocol pins fixed |

---

## 3. Compression: single demand sentence

**T8 keeps forcing one dynamical object:** a **licensed microphysical law** that lowers **early \(\mathrm{d}S/\mathrm{d}u\)** through the \(\Delta u=0.01\) window at \(u\sim0.10\)–\(0.11\) so range/\(S_\star\le0.10\), **jointly** with T2 reach, stall_cap, DC3, and T1–T6 — without pure \(G_{\mathrm{TMS}}\) rescaling, densify thrash, threshold games, or invented island formulas.

Everything else on the Page instrument is either **already paid structure** (joint near-miss stack on v13), **exhausted construction** (D1–D3), or **forbidden thrash**.

---

## 4. Why current stocked constructions block the demand

| Stocked construction | What it supplies | Why it does not close T8 joint |
|---|---|---|
| Continuous TMS+BS v23 pins | Best joint near-miss (T8 0.113 only) | Early slope sticky under pure TMS scale |
| \(G_{\mathrm{TMS}}\) / shape edge-tune | Can soften rise | Loses T2 or stalls; ratio sticky if pure scale |
| D1 two-phase | Early flat \(S(u)\) possible | T2 not recovered jointly |
| D2 free \(w_c\equiv1\) | DC hygiene | No-op on scored trajectory |
| D3 densify | Changes \(S(u)\) shape | Reach / stall / DC3 break |
| D4 freeze | Honesty / thrash-stop | Does not close Q6 |

**Exploratory protocol trigger:** residual points at a missing piece **current knobs block** → treat header schedule as **suggestion**, invent **CANDIDATE dynamical/micro levers**, double-scrutinize, ledger deaths.  
That work lives in [`CANDIDATE_LEVERS.md`](./CANDIDATE_LEVERS.md) · [`DEAD_LANES.md`](./DEAD_LANES.md) · [`SURVIVORS.md`](./SURVIVORS.md).

---

## 5. Explicit non-claims

- No derivation of a Page law.  
- No claim that any lever “will” clear T8.  
- No CANDIDATE packet; `page_curve_claimed` false.  
- No invented closed-form \(S(u)\).  
- Champion remains **v13**; residual **OPEN**.

---

*End WHAT_RESIDUAL_DEMANDS.md*
