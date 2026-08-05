> **PROVENANCE:** background `claude -p` subagent (blue-launched), **not** interactive red seat. See `PROVENANCE.md`. Unverified until interactive red post-hoc.

# RED PRE-AUDIT — Page D4 microphysics only, no densify

**Seat:** Claude (red) · **Date:** 2026-08-04 · **Mode:** pre-audit, fences only
**Target package:** `page_d4_microphysics_20260804` (not on disk at write time; no new script found)
**Priors read:** `page_t8/` · `page_t8_residual_demand/` · `page_full_freeze_20260804/SCORECARD_SNAPSHOT.md` · `next_queue_20260804/PAGE_D4_STATUS.md`

---

## 0. Champion artifact — red re-verified, unchanged

```
sha256(docs/.../page_curve/coevolve_v13.json)
  = 048de43e1bc766c8f420c54f565a33166c0792c23291ba567cdc6c772f92fca8
```

Matches the stamp blue filed as red's AGREE cure (`page_t8/REPORT.md:117-125`) and the
freeze record (`SCORECARD_SNAPSHOT.md:17`). **Write-once discipline holding.** File
mtime Aug 4 00:20, untouched by today's work. Red says this plainly because it is the
one thing in this door that is currently *verified* rather than *asserted*.

---

## 1. The finding red brings to this door: **T8 has a denominator**

T8 is a **ratio**: \(\big(\max S-\min S\big)/S_\star \le 0.10\) per \(\Delta u = 0.01\)
bin, with \(S_\star\) the **global** peak of \(S_\mathrm{rad}\) (`DIAGNOSIS.md:16-18`).

Champion v13, recomputed by red from the recorded values:

| quantity | value |
|---|---|
| early-bin S range, [0.10, 0.11) | 0.0018883423986319587 |
| \(S_\star\) (global peak, at \(i_\mathrm{peak}=104\), \(u^\star\approx0.267\)) | 0.016688199517780646 |
| range / \(S_\star\) | **0.11315435176934464** |
| bar | ≤ 0.10 |

Two arithmetically **identical** ways to convert this FAIL into a PASS:

| route | requirement | factor |
|---|---|---|
| **numerator** — lower early-bin range, \(S_\star\) fixed | range ≤ 0.0016688199517780646 | **÷ 1.13154** |
| **denominator** — raise \(S_\star\), early range fixed | \(S_\star\) ≥ 0.018883423986319585 | **× 1.13154** |

**A 13.16% increase in the global peak clears T8 with the early window completely
unchanged.** The failing bin is frames **43–54** (`DIAGNOSIS.md:42,70-74`); \(S_\star\)
is attained at frame **104** (`PAGE_D4_STATUS.md:67`). They are disjoint regions of the
history. A law that raises mid/late entanglement without touching frames 43–54 clears
T8 by moving a number that has nothing to do with what T8 is for.

**Why this is a hole and not a covered case.** `DEAD_LANES.md:29` fences \(G_\mathrm{TMS}\)
scale scans on the grounds that they are *"ratio sticky ~0.11 under pure scale"* — i.e.
the fence assumes levers move numerator and denominator **together**. It does not fence a
lever that moves the denominator **alone**. Nor does the protocol-break table
(`DEAD_LANES.md §1.3`), which covers threshold loosening, \(\Delta u\) widening, bin
subsampling, machine-T1–T6-implies-candidate, co-writing, tool claim-flip, and "almost
candidate". **S\(_\star\) inflation is not on that list.**

It is also **gate-silent**: raising the global peak *helps* T3 (`S_rise_credited` = 0.0166874
≈ \(S_\star\), `PAGE_D4_STATUS.md:40`) and preserves T1 interior max. Nothing else in the
stack would flag it.

The named survivor levers that could produce exactly this are already on the board:
**R2/L2** — *"cap early dS/du **while preserving midband Page peak**"*
(`CONSTRUCTION_LEVERS.md:45`) — and **R5** co-modulation (`SURVIVORS.md:39`).

> **PRE-REGISTERED KILL (P-K1):** any future write-once artifact reporting `T8_pass`
> must report, disaggregated:
> 1. the **absolute** \(S\) range in the early bin, against v13's **0.0018883**;
> 2. \(S_\star\), against v13's **0.0166882**;
> 3. which of the two moved, and by how much.
>
> If the pass is carried by \(S_\star\) rising ≳13% while the early-bin absolute range is
> flat, red grades it **DENIED — denominator inflation / fake pass**. T8's stated intent
> is *"single-valued \(S(u)\) — entropy is not multivalued over a fixed evaporation-coordinate
> window"* (`DIAGNOSIS.md:22`). A larger global peak does not make the early window less
> multivalued.
>
> **Fairness clause:** a legitimate law may raise \(S_\star\) **and** lower early range
> together. That is not the kill. The kill is a pass that is *only* the denominator, and
> the remedy is disclosure, not prohibition — red is asking blue to **show which moved**,
> not to avoid moving it.

---

## 2. Scope fences for a "D4 microphysics" package

D4 is a **disposition**, not a lever: *"accept near-miss"*, **ACTIVE-DISPOSITION**
(`page_t8_residual_demand/SURVIVORS.md:42`), *"honesty / thrash-stop only"*
(`page_t8/NON_CLAIMS.md:18`), *"L5 ... not a lever to close Page"*
(`CONSTRUCTION_LEVERS.md:48`).

### P-K2 — densify laundering

`DEAD_LANES.md:88` names it exactly: *"'Densify is continuum (R4)' without law text →
D3 launder → Densify kill."* R4 and R6 are **FRAGILE-SCHEMA**, densify form **DEAD**
(`SURVIVORS.md:38,40`). D3 record: v35–v36 `u_late~0.899`, `stall~554`, **DC3 FAIL**;
v37 late T8 fail; v38 `u_late~0.869` (`DEAD_LANES.md:44-46`).

> **DENIED** on: any mode-count change, band change, or continuum move presented as
> microphysics without a **named law text preceding it**. The law comes first
> (`SURVIVORS.md:52`, `PROTOCOL.md:26` step 0), the implementation second.

### P-K3 — no production campaign from this desk

Stop conditions `CONSTRUCTION_LEVERS.md:77-81`: no coevolve_v39+ campaign without a
licensed new law writeup; no densify; no CANDIDATE packet while T8 = 0.113; no
`page_curve_claimed: true`; champion stays v13.

> **DENIED** on: a coevolve production sweep launched under a "microphysics" heading.
> A microphysics package writes **law text**. If it also produces a run, that run is
> write-once, versioned, never overwriting v13, and scored arrays-only (`PROTOCOL.md:23-35`).

### P-K4 — schema ≠ content

`SURVIVORS.md:112`: *"Schemas ≠ deferred success without content."* R1/R2/R3/R5 are
**SURVIVOR-SCHEMA** — statement *shapes* with the law still **empty**.

> **AGREE-IF / DENIED:** a package that elaborates R1–R5 prose without writing a named
> law has produced **more schema**, and must say so. Presenting elaborated schema as
> "microphysics delivered" is grade inflation. Red will ask: **is there an equation, and
> what fixes its constants?**

### P-K5 — the claim flag and the packet

`page_curve_claimed` **false** until a separate claim step after red AGREE
(`PROTOCOL.md:15`, `NON_CLAIMS.md:13`). The scorecard tool **never** sets it
(`SCORECARD_SNAPSHOT.md:48`). No packet while T8 > 0.10 (`PROTOCOL.md:53,79`).
`CANDIDATE_TURN_binding` requires `T8_pass` (`DIAGNOSIS.md:19`).

> **DENIED** on: any of — claim flag true · CANDIDATE packet filed · "almost candidate"
> used as a grade (`DEAD_LANES.md:60`) · machine T1–T6 True cited as candidacy
> (`NON_CLAIMS.md:15`) · Q2 area-law payment cited as Q6 (`DEAD_LANES.md:69`).

### P-K6 — namespace collision on "D4"

Two different **D4**s are live in this corpus at once:

| ID | program | meaning | source |
|---|---|---|---|
| **D4** | Page | *accept instrument near-miss* (disposition) | `page_t8/REPORT.md:85`, `PAGE_D4_STATUS.md` |
| **D4** | bounce | *written re-entry bookkeeping* — graded **"PAID as RECONSTRUCTED dictionary"** | `n2_match_book/SURVIVORS.md:54` |

> **FLAG:** these are unrelated, and one of them is graded **PAID**. A cross-citation of
> the form "D4 is paid" would silently import a bounce-ledger payment into the Page
> ledger, where D4 is an admission of *not* paying. Red will read every "D4" in the new
> package for which one it means, and requires the Page package to qualify the ID
> (e.g. *Page-D4*) at least once.

---

## 3. Standing numbers red will re-check on any new artifact

| pin | v13 value | source |
|---|---|---|
| T8 range/\(S_\star\) | 0.113154 (**FAIL**, need ≤0.10) | `SCORECARD_SNAPSHOT.md:44` |
| early-bin absolute range | 0.0018883423986319587 | `DIAGNOSIS.md:45` |
| \(S_\star\) | 0.016688199517780646 | `DIAGNOSIS.md:49` |
| failing bins / occupied | 1 / 83 | `SCORECARD_SNAPSHOT.md:46` |
| \(u_\mathrm{late}\) | 0.902078 (T2 bar 0.9) | `SCORECARD_SNAPSHOT.md:31` |
| longest stall | 10 (cap 10 — **at the bar**) | `SCORECARD_SNAPSHOT.md:38` |
| DC3 | PASS, `e_c_raw_stored` | `SCORECARD_SNAPSHOT.md:42` |
| artifact sha256 | `048de43e…` — **red re-verified today** | §0 above |

Note `longest_stall_frames = 10` against a cap of **≤10**: T2 reach and stall both sit
**exactly on their bars**. Any lever that buys early-T8 headroom by slowing the early
dump has **zero** margin on stall and 0.002 on \(u_\mathrm{late}\). This is the D1 lesson
already recorded (`DEAD_LANES.md:41`, early T8 passes, T2 not joint) and red will check
these two first on any new artifact, before T8.

---

## 4. Grade conditions when blue files TASK COMPLETE

| grade | conditions |
|---|---|
| **AGREE** | `page_curve_claimed` false; no packet; champion v13 + hash restated; D4 described as **disposition, not close**; any lever work is **named law text** with its constants' provenance; zero densify; zero production campaign; Page-D4 disambiguated from bounce-D4; T8 still 0.113 and said to be a **FAIL** |
| **AGREE-IF** | Fences held but ≥1 of: elaborated schema presented as microphysics · "D4" unqualified · near-miss language softening toward "essentially passing" · stall/T2 margins not restated |
| **DENIED** | Any of: **T8 pass carried by \(S_\star\) inflation without disaggregation (P-K1)** · densify under a continuum/microphysics heading (P-K2) · coevolve production campaign (P-K3) · claim flag true or packet filed (P-K5) · 0.113 called a pass, "close enough", or "≈0.10" (`NON_CLAIMS.md:16`) · v13.json overwritten or hash changed · threshold/Δu/bin games (`DEAD_LANES.md §1.3`) |

**Red's prior:** T8 stays 0.113154, `page_curve_claimed` stays false, Q6 stays OPEN,
COMPLETE = 0.

---

## 5. Non-claims of this red note

- Red has **not** proposed a Page law, a lever, or a route to T8 ≤ 0.10.
- P-K1 is a **disclosure requirement and a fake-pass fence**, not a physics suggestion —
  red is closing an audit hole in the ratio, not telling blue how to move the numerator.
- Red has **not** graded a package (none on disk at write time).
- Red re-verified the champion hash; everything else in §3 is quoted from blue's records,
  not independently recomputed from the arrays.
- `exit 0` ≠ PASS. Delivered ≠ graded. Machine True ≠ candidate.

*NO FABRICATIONS. `page_curve_claimed: false`. Pre-audit ≠ verdict.*
