# For Grok & Claude — dual-agent coordination brief

**Created:** 2026-08-03  
**Audience:** Grok (this repo’s interactive agent) and Claude (owner’s other session).  
**Owner:** Justin Pulford.  
**Repo root:** `/home/themilkmanj/prtoe_class`  
**Branch (typical):** `coderabbit-review-2` / `main` — check `git status` before editing.

This file is the **shared briefing**. Either agent should read it at session start and
**append a dated handoff block at the bottom** when finishing a substantial turn.

---

## 0. Recommendation (read first)

### Do we run all three theory sprints at once?

**No — not as three deep simultaneous mechanism hunts.**

Project rule (roadmap, unchanged):

> Theory sprints **one at a time** (Koide **OR** bounce **OR** T14 3D), never all three half-done.

**Why:** each OPEN-THEORY residual has already eaten weeks of partial work. Parallel *deep*
mechanism invention produces three half-stories and zero closed rows. Fake-complete is
forbidden.

### What *does* work with Grok + Claude + subagents

| Mode | When to use | How |
|---|---|---|
| **A — Primary + support (recommended)** | Default | One **primary** theory debt owns the week. The other agent does **support only** (scripts, logs, no-go pricing, literature, package hygiene) on the *other* two — no mechanism claims. |
| **B — Compute // theory split** | When T14 is primary | One agent owns **T14 numerics** (`ring_toroidal_3d.py`, gates, ledger burial). The other owns **Koide reading** or **bounce no-go tightening** as *analysis*, not promotion. |
| **C — Full parallel of three** | **Avoid** | Only if owner explicitly accepts three open notebooks and zero closures. |

**Suggested default for this week:**

1. **Primary:** **T14 link 4** — most *closable* residual (script exists, gates written, fork rule clear).  
2. **Secondary (Claude or Grok, not both inventing):** **Koide #101/#102** — pure mechanism; desk walks already done; only a real node/conservation idea can move it.  
3. **Tertiary (constraint-only, not promotion):** **Bounce B11** — already a wall of DONE no-gos; allowed work is tighter constraints / DESK_NEXT B18, **not** inventing a turn.

Owner can reorder. If you reorder, update the “Active assignment” table in §7.

---

## 1. What this project is (for Claude)

**PRTOE** is a private research corpus (docs + CLASS/Cobaya code + scripts) exploring a
dark-sector / medium picture: ultralight rotating condensate, electron-mass transition window,
neutrino–DE scale tie, etc.

**Discipline that matters more than the story:**

- **COMPLETE ≠ publishable.** Most finished docs are **CORPUS_ONLY**.
- **One narrow falsifiable claim per arXiv paper**; prefer framework-independent extracts.
- **Do not invent mechanisms** to close OPEN-THEORY. Prefer no-gos, priced residuals, honest
  OPEN tags.
- **Do not kill live MCMC** casually. Three production chains are running.
- **Do not invent arXiv endorsement** or claim public status the owner has not created.
- **neutrino-mbb** was submitted to **William Fairbank** — leave that package alone unless asked.
- House voice: short, graded, ledger-honest. No AI filler. No “robust framework” marketing.

**Entry maps (start here if cold):**

| Role | File |
|---|---|
| Shelf map | `docs/PRTOE_INDEX.md` |
| Reader orientation | `docs/PRTOE_READERS_GUIDE.md` |
| Outsider risk / kill conditions | `docs/PRTOE_READERS_RISK.md` |
| Completion tags (64 docs) | `docs/working_logs/_FILE_COMPLETION_STATUS.md` |
| Paper candidacy | `docs/working_logs/_ARXIV_CANDIDACY.md` |
| Finish roadmap | `docs/working_logs/_PROJECT_FINISH_ROADMAP.md` |
| Residual T-debts | `docs/working_logs/_RESIDUAL_DEBT_CENSUS.md` |
| Failures / killed routes | `docs/PRTOE_FAILURES_LEDGER.md` |
| Live chain bookkeeping | `docs/PRTOE_CHAIN_TABLES.md`, `docs/PRTOE_CODE_MANIFEST.md` |
| This dual-agent brief | `ForGrok&Claude.md` (this file) |
| Older collab note | `COLLABORATION.md` (general; this file is the live dual brief) |

---

## 2. Desk state snapshot (2026-08-03)

### Papers (`papers/`) — packaging done; endorsement is external

| Package | pp | Status | Owner action |
|---|---:|---|---|
| `supertrace-note` | 3 | **SHIPPED** Zenodo | optional gr-qc arXiv |
| `neutrino-mbb` | 3 | **With Fairbank** | packaging paused |
| `radio-lattice` | 7 | READY | astro-ph endorsement |
| `lattice-tc-gap` | 2 | READY | hep-lat endorsement |
| `bbn-eps-bound` | 3 | READY | astro-ph endorsement; optional dense ε_max(T_c) |
| `kination-tracking-note` | 2 | READY | gr-qc endorsement |
| `fairbank-0nubb` | — | NOT_READY | **do not invent TeX** |

Staged copies: `docs/arXivReady/`. Hygiene: `python3 scripts/arxiv_package_audit.py`.

**Further docs→paper extractions:** **0 candidates** after 2026-08-03 re-audit. Do not force
LV / nulls / scorecards into packages.

### Live machines — **do not kill**

| Chain | Last R−1 | Stop | Note |
|---|---:|---:|---|
| `dyad_mnu_bbnfix` | ~0.192 | 0.05 | leave alone |
| `cmp_lcdm_mnu_bbnfix` | ~0.141 | 0.05 | closest |
| `cmp_prtoe_routeD` | ~129 (1 progress row) | 0.1 | basin-split; reseed only owner-gated |

Booking when bbnfix pair hits R−1 ≤ 0.05: `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`.

---

## 3. The three OPEN-THEORY sprints (detail)

### 3A. T14 — IGMF helicity, link 4, sign(H_kin)  ★ recommended primary

| | |
|---|---|
| **Ask** | What is sign(H_kin) of the genesis roll-up flow? Poloidal half paid; **toroidal–poloidal relative bit** open. |
| **Why it matters** | Harrison battery: sign(helicity_B) = sign(H_kin). Link 5 (matter lock) already **closed negative**. Only link 4 remains for reading a sky helicity as a medium property. |
| **Entry docs** | `docs/PRTOE_igmf_helicity.md`, `docs/working_logs/T14_igmf_helicity_owed.md`, `docs/working_logs/T14_link5_joint_draw.md` |
| **Entry code** | `scripts/ring_toroidal_3d.py` (fork A shape helicity / B excess phase twist), also `scripts/ring_toroidal_circulation.py` |
| **Success** | Quotable only if gates pass: ring detected, n=±1 parity flip, energy drift ≤2%. Survivor → candidate grade; dead reading → failures ledger. |
| **Forbidden** | Quoting sign without gates; inventing a matter lock after link 5 died; claiming Fermi ~2σ is a detection. |
| **Good agent fit** | **Grok** (local scripts, long runs, log parsing) + optional Claude review of gate logic / prose. |

### 3B. Koide — #101 / #102 one node residual

| | |
|---|---|
| **Ask** | What *enforces* the graded null f₀² = \|f₁\|² + \|f₂\|² to ~10⁻⁵? Phase θ_B = 2/9 is holonomy Q/3 — **not independently sourced**. |
| **Paid already** | Protection, fence/Q arithmetic, #101 classification, #102 measurement table, pacing/sign-chain **desk walks**. |
| **Entry docs** | `docs/PRTOE_koide_relation.md`, `docs/working_logs/T6_koide_desk_status.md`, `docs/working_logs/T6_koide_owed.md`, related `docs/PRTOE_forced_combination.md` |
| **Success** | A mechanism (constraint / index / conservation) that forces the null **without** inventing a free potential that lands A=√2 by hand. Or an honest **stronger no-go** that retires a false aisle. |
| **Forbidden** | Marking OPEN-THEORY COMPLETE; inventing X to fit numbers; promoting forced_combination past candidate grade without the node. |
| **Good agent fit** | **Claude** (deep mechanism reasoning, careful prose) with Grok verifying arithmetic scripts / greps. |

### 3C. Bounce — classical turn (B11) wall

| | |
|---|---|
| **Ask** | Classical bounce: H = 0 **and** Ḣ > 0 from the **recorded** Lagrangian — or written FRW-exit. Floor ρ_bounce^(1/4) = **1.06 keV** is paid; **turn is not**. |
| **Paid already** | B1–B10 mostly DONE or no-go (thermal, CSW floor, kination tracking, bare vacuum+Tolman, toys…). Kination negative **packaged** as `papers/kination-tracking-note/`. |
| **Entry docs** | `docs/working_logs/bounce_derivation_workplan.md` (§ Remaining open list), `docs/PRTOE_bigbang_no_singularity.md`, `docs/PRTOE_white_holes.md`, failures ledger |
| **Entry code** | `scripts/rho_bounce.py`, `scripts/bounce_bkl_stiff_check.py`, various bounce_* scripts |
| **Allowed now** | B18: tighter no-go pricing / constraint hands. B17 only as *search*, not claim. |
| **Forbidden** | Story-grade promotion; inventing ρ(1−ρ/ρ_c) as derived; promoting white-hole global ID past provisional without B11. |
| **Good agent fit** | **Either**, as **constraint accountant** — not as “write the bounce this week.” |

---

## 4. Division of labor (default assignment)

### Color code (owner 2026-08-03)

| Agent | Color | Meaning |
|---|---|---|
| **Grok** | **Blue team** | Build: machine runs, scripts, logs, constructive desk fixes that land after review. Default posture: *make progress that can be checked*. |
| **Claude** | **Purple team** | **Mostly red, a hint of blue.** Default posture: *try to refute* every proposed booking (gates, signs, arithmetic, independence, trials factor). The blue hint is only: hardening instruments (TRIALS_FACTOR, INDEPENDENCE_AUDIT, check-12, quotation rules) and fixes that *survive* adversarial review — not drafting new mechanisms or inventing closures. |
| **Owner** | Final accept | Endorsements, Fairbank, chain kills/reseeds, what gets booked as theory COMPLETE. |

| Lane | Primary agent | Secondary agent |
|---|---|---|
| T14 3D / gates / machine | **Grok (blue)** | Claude **red-teams** any number before booking; may propose probe/gate tests (blue hint) |
| T14 prose / “what is bookable” | Grok drafts if needed | **Claude attacks** overclaim; optional one-line safe wording if red-team found a bug |
| Koide #101/#102 | Grok only if primary reassigned | Claude **red-teams** any proposed node; does **not** invent the mechanism |
| Bounce constraints | Grok (if assigned) | Claude red-teams promotion attempts |
| Package hygiene / arXivReady | Grok | Claude red-teams claims in TeX if near submission |
| Live MCMC watch | Grok (shell) | Claude must not kill/relaunch without owner |
| Endorsement / Fairbank / Zenodo | **Owner only** | Agents prepare packages only |
| Hardening docs (trials, independence, check-12) | **Claude (blue hint)** | Grok implements if code needed |
| Subagents | Grok spawns for parallel build/audit | Claude may use own tools; write results into this file |

**Conflict rule:** if both agents edit the same theory file, **stop and merge via owner**. Prefer one writer per file per day.

**Git rule:** no force-push; no amend of published commits; ask owner before push to `main`.

**Booking rule:** Grok (or owner) proposes a grade change → Claude red-teams → owner accepts. Claude does not self-book OPEN-THEORY → COMPLETE.

---

## 5. Hard rules (both agents)

1. **Do not kill** `dyad_mnu_bbnfix`, `cmp_lcdm_mnu_bbnfix`, or `cmp_prtoe_routeD` without explicit owner order.  
2. **Do not mark OPEN-THEORY COMPLETE** without a closed derivation or closed no-go that the file’s own grade system accepts.  
3. **Do not invent** `papers/*` packages from CORPUS_ONLY files. Candidacy re-audit 2026-08-03: **0** new candidates.  
4. **Do not invent TeX** under `papers/fairbank-0nubb/`.  
5. **Do not** put working notes in BibTeX `note` fields; no empty `acknowledgments`; no “PRTOE” in arXiv TeX.  
6. **Failures go in** `docs/PRTOE_FAILURES_LEDGER.md` — append-only honesty.  
7. Prefer **priced residual** over hopeful prose.  
8. When unsure whether a result is bookable: leave the OPEN tag and write the gap.

---

## 6. How to talk to the other agent (protocol)

### Starting a session

1. `git status` + read the latest handoff at the bottom of this file.  
2. Confirm **Active assignment** table (§7).  
3. Do not re-open packaging of READY papers unless hygiene broke.  
4. Do not re-audit candidacy unless owner asks (already 0 candidates).

### Ending a session (append handoff)

Copy this template to the bottom:

```markdown
### Handoff YYYY-MM-DD HH:MM (Agent: Grok|Claude)

**Active primary:** T14 | Koide | Bounce | other
**Done:**
- …
**Files touched:**
- …
**OPEN residual left:**
- …
**Do not:**
- …
**Next concrete step for the other agent:**
- …
**Chains:** alive? last R−1 if checked
```

### Cross-talk without collision

- Prefer **disjoint files**.  
- Theory claims: **Grok (blue) drafts** → **Claude (purple/red) attacks** → owner accepts.  
- Claude’s blue hint: check-12 / trials / independence hygiene and *surviving* wording fixes — not parallel mechanism invention.  
- Scripts: Grok owns long runs; Claude may propose patches or attack gate logic but should not start 10 h sims without checking CPU against MCMCs.

---

## 7. Active assignment (edit when owner reassigns)

| Role | Focus | Status |
|---|---|---|
| **Primary theory** | **T14 link 4** | **ACTIVE 2026-08-03** — owner chose option 1 |
| **Grok** | **Blue team** — MACHINE: energy gate ✓; next single-instrument H / Wr+Tw | Live |
| **Claude** | **Purple team — mostly red, hint of blue** | Live — paste §12 |
| **Secondary** | Koide #101/#102 | Only if T14 idle; Claude does not invent the node |
| **Tertiary** | Bounce B18 | Idle |
| **Packages / MCMC** | READY / leave running | Owner endorsements; do not kill chains |

**Owner decisions (2026-08-03):**
1. Primary = **T14** (not all three deep).  
2. **Claude = purple team** (mostly red-team, a hint of blue-team). Grok builds; Claude attacks bookings and keeps hardening instruments honest.

**Claude purple posture on T14 this week:**
- **Red (default):** attack any claim that “link 4 closed” means overall sign known; attack ±sign(n) quotes; attack (A)×#19 products; attack Fermi-as-datum; attack energy-gate handwaving; try to break proposed single-instrument H acceptance criteria before Grok books a number.  
- **Blue (hint only):** tighten *external-safe* wording when a red-team hit finds a real bug; keep TRIALS_FACTOR / INDEPENDENCE_AUDIT / check-12 alive; propose gate tests Grok should run — do not draft the bounce/Koide/sign mechanism.

---

## 8. Concrete first tasks (after owner confirms primary)

### If primary = T14 (recommended)

**Grok:**
1. Read `scripts/ring_toroidal_3d.py` end-to-end + any prior run logs under `docs/working_logs/_runs/`.  
2. Estimate wall-clock / RAM vs live MCMCs (do not starve bbnfix).  
3. If capacity allows: run n=+1 and n=−1 under gates; capture energy drift, ring detection, shape helicity, excess phase twist.  
4. Write results into `T14_igmf_helicity_owed.md` + `PRTOE_igmf_helicity.md`; bury dead fork in failures ledger if needed.  
5. Append handoff.

**Claude (purple — mostly red):**
1. Read T14 docs + §11 acceptance card; **attack** any overclaim (overall sign, Fermi, (B) unbury, energy absolutes).  
2. Red-team Grok’s proposed machine acceptance criteria *before* numbers land; list kill conditions.  
3. Blue hint only: one-pass external-safe wording fixes if red-team finds a real doc bug; optional Koide *disallowed-aisles* inventory (no mechanism draft).

### If primary = Koide

**Grok (blue):** mechanism *attempts* only under `T6_koide_desk_status.md` constraints; arithmetic reconfirm.  
**Claude (purple):** red-team any proposed node/conservation law before booking; list disallowed aisles; do **not** invent the mechanism.

### If primary = Bounce

**Either:** only B18-style constraint tightening / inventory honesty.  
**Neither:** invent B11 this week unless a derivation actually appears from recorded Lagrangian.

---

## 9. Model discussion (for Claude — what “the model” is, without the whole shelf)

Claude: if you only have time for a **short physics picture**, use this.

**Objects (schematic):**
- A dark **rotating** condensate / superfluid sector (complex scalar, conserved charge) that can act as dark matter / medium.
- An **electron-coupled** scalar sector that can shift \(m_e\) in a redshift window (radio lattice, BBN witness) — amplitude ε often treated free in public notes.
- A **DE floor** / vacuum structure with a registered branch: rigid \(w=-1\) vs late thaw (Route-D), adjudicated by data + chains — **do not quote thaw ≠ 0** from unconverged RouteD.
- **Neutrino home:** exploratory tie of lightest mass to DE scale → 0νββ window (packaged as neutrino-mbb; now with Fairbank).
- **Chirality family:** integer winding \(n\) may sign magnetic helicity *if* seeding link closes (T14); matter lock **does not** (link 5 dead).

**What is already public / package-shaped:** supertrace counting comment; m_ββ window under a hypothesis; radio ratio lattice; lattice \(T_c/\sqrt{\sigma}\) gap note; BBN ε bound at measured \(T_c\); kination tracking no-go for rotating condensate.

**What is not:** a finished bounce, a closed Koide node, a bookable RouteD thaw, a completed model paper. Do not write as if they are.

**Honesty grade language used in-repo:** COMPLETE, COMPLETE-CONDITIONAL, OPEN-MACHINE, OPEN-THEORY, WATCH-EXTERNAL, CORPUS_ONLY, READY_PACKAGE, NOT_READY. Prefer those tags over vibes.

---

## 10. Owner checklist (not agent work)

- [x] Confirm primary theory sprint — **T14** (2026-08-03).  
- [x] Claude role — **purple team** (mostly red, hint of blue) (2026-08-03).  
- [ ] Endorsements: radio-lattice, lattice-tc-gap, bbn-eps-bound, kination (± supertrace).  
- [ ] Fairbank / neutrino-mbb thread (external).  
- [ ] When bbnfix R−1 ≤ 0.05: authorize posterior booking.  
- [ ] RouteD reseed: only if second progress still pathological **and** you fire surgery.

---

## 11. T14 blue-team acceptance card (2026-08-03) — authoritative for both agents

| Claim | Grade |
|---|---|
| Harrison: sign(H_B) = sign(H_kin) | **Booked** |
| Link 5 matter lock | **CLOSED NEGATIVE** |
| Link 4 **branch** (tracks n; not universal) | **CLOSED** via (A) shape helicity exact flip |
| Link 4 **overall** sign(H_kin) vs n | **OPEN** — quote only: **∝ sign(n), prop. sign undetermined** |
| Reading (B) as Tw / toroidal circ. | **Ledger-dead** (earned after off-core re-run) |
| Fermi IGMF as genome datum via this chain | **Unreadable permanently** |

**Assembly (this config):** \(H_\mathrm{kin} \sim 2n + \mathrm{Wr} + \mathrm{Tw}\). Near-cancellation warning; Tw not in hand.

**Energy gate (2026-08-03 diagnostic):** sponge ON drift 3.83% vs OFF 0.0003% at reduced grid — cause is **designed dissipation**, not integrator failure. Log: `docs/working_logs/_runs/toroidal_energy_gate_2026-08-03.log`. Re-scope absolute 2% gate to physical region; parity of integer (A) still licensed under common-mode pre-reg.

**Do not:** multiply #19 poloidal × (A) and call it \(H_\mathrm{kin}\); quote \(\pm\)sign(n); re-open convention audit by inspection; unbury (B) without adaptive-probe data.

**Next MACHINE (Grok, blue):** single-instrument \(H_\mathrm{kin}\) (preferred) or adaptive-probe Tw + numerical Wr — sibling script, short \(T_\mathrm{MAX}\sim 1.5\), nice vs MCMCs. Propose acceptance criteria *before* booking any overall sign.

**Next DESK (Claude, purple):** paste prompt in §12 — mostly attack, hint of fix.

Full T14 status synthesis: explore subagent 2026-08-03 + owed file `T14_igmf_helicity_owed.md`.

---

## 12. Claude paste-ready prompt (**purple team** — mostly red, hint of blue)

```text
You are PURPLE TEAM on the PRTOE repo (prtoe_class): mostly RED-TEAM, a hint of blue.
Grok is BLUE TEAM (builds machine work on T14). You do not invent mechanisms or book
OPEN-THEORY complete. Owner accepts grade changes.

Read first:
  ForGrok&Claude.md §§4, 7, 11, 12
  docs/working_logs/T14_igmf_helicity_owed.md from "## LINK 4 — CLOSED" through 2026-08-02 desk bits
  docs/PRTOE_igmf_helicity.md seeding / link sections
  docs/PRTOE_FAILURES_LEDGER.md entry for reading (B)
  (if present) docs/PRTOE_TRIALS_FACTOR.md, docs/PRTOE_INDEPENDENCE_AUDIT.md

Authoritative status (attack anyone who over-reads these):
- Link 5 CLOSED NEGATIVE. Fermi IGMF is NOT a genome datum through this chain.
- Link 4 BRANCH closed: (A) flips exactly with n. Universal handedness EXCLUDED.
- Overall sign(H_kin) OPEN. Safe quote only: ∝ sign(n), prop. sign undetermined.
- (B) ledger-dead after off-core fix (earned burial). Do not unbury without new data.
- Assembly: H ~ 2n + Wr + Tw. Product of #19 poloidal × (A) is NOT H_kin.
- Energy: sponge causes drift (2026-08-03 diagnostic); kills absolute energy claims.
  Integer (A) parity is only as strong as the pre-reg common-mode argument — attack it if weak.

RED tasks (default — spend most of the session here):
1. List every way Grok could falsely book overall sign(H_kin) from the next single-instrument
   H or Wr+Tw run. For each: kill condition + what evidence would actually be needed.
2. Attack the claim "branch closed" if any doc still equates it with overall-sign closed.
3. Attack energy-gate re-scope if it smuggles absolute energetic claims back in.
4. Score §11 acceptance card: which rows are over-strong? Which under-strong?
5. If Grok posts a number: try to refute before owner books.

BLUE hint only (≤20% of effort):
6. If red-team finds a real wording bug in PRTOE_igmf_helicity.md, propose a minimal fix
   (do not rewrite the file as a promotional pass).
7. Keep trials/independence/check-12 hygiene if you find live defects while reading.

Do NOT: start long GP runs; edit ring_toroidal_3d.py; invent Koide #101; invent bounce B11;
mark anything COMPLETE-THEORY closed; invent endorsement.

Append a handoff block at the bottom of ForGrok&Claude.md when done.
```

---

## Handoffs (append below)

### Handoff 2026-08-03 (Agent: Grok) — dual brief created

**Active primary:** unassigned at that moment (recommended T14).  
**Done:** created this file.

### Handoff 2026-08-03 ~01:30 (Agent: Grok) — T14 primary kickoff

**Active primary:** **T14** (owner chose 1)  
**Done:** inventory + acceptance card §11 + energy gate diagnostic  
**Note:** mode later corrected to Grok=blue / Claude=purple (see next handoff)

### Handoff 2026-08-03 (Agent: Grok) — Claude = purple team

**Active primary:** T14  
**Roles:** **Grok = blue team** (build). **Claude = purple team** (mostly red, hint of blue).  
**Done:**
- Updated `ForGrok&Claude.md` §§4, 6, 7, 8, 10, 11, 12 for purple-team posture
- Rewrote §12 Claude paste prompt as red-primary with ≤20% blue-hint tasks
**Files touched:**
- `ForGrok&Claude.md`
**OPEN residual left:**
- Overall sign(H_kin); single-instrument H / Wr+Tw still machine-open
**Do not:**
- Treat Claude as co-builder of mechanisms; quote ±sign(n); kill MCMCs
**Next concrete step for Claude:**
- Paste **§12 purple prompt** — attack §11 card + pre-kill Grok’s next machine booking paths
**Next concrete step for Grok:**
- After Claude red-team of acceptance criteria (or in parallel on scripts only): sibling H/Wr instrument
**Chains:** leave alone

---

### Handoff 2026-08-03 (Agent: Claude)

**Active primary:** still unassigned — I second **T14 primary**; Koide secondary fits my lane per §4.

**Done (same session, before reading this brief):**
- **Red-team hardening wave** (owner-directed, commit `92874db8`): two new documents that now
  bind quotation practice — `docs/PRTOE_TRIALS_FACTOR.md` (look-elsewhere accounting from the
  ledger's own records; a lone percent-class match carries ≈ zero weight quoted alone) and
  `docs/PRTOE_INDEPENDENCE_AUDIT.md` (ten multi-way agreements audited, data-side vs
  assumption-side; exactly one fully independent external validation stands today). Linked from
  READERS_RISK §4's new scoreboard paragraph.
- **Check-12 sweep at 11/53** files read whole, 35+ defects fixed (latest: hierarchy_problem ×4
  + a DERIVATION_HUNT quote, commit `c58c03d0`). Watch for the recurring failure mode when
  editing: *a correction written near the defect rather than on it.*
- **Fairbank update for §1/§2:** owner made contact 2026-08-02 evening and sent
  `papers/neutrino-mbb/main.pdf`. Endorsement packet staged at
  `docs/working_logs/fairbank_endorsement_packet_2026-08-02.md`. Package frozen, agreed.
- **Funnel-edge quotation rule in force:** never the bare "0.45%" — full budget is ~0.04σ today
  (σ(m₁\*) ≈ 0.24 meV dominates); it becomes a ~3%-level test at JUNO. Registry annotation to
  P-2026-012 and neutrino_sector carry the framing.

**Files touched today (collision guard — check git log before editing):** hierarchy_problem,
DERIVATION_HUNT, fairbank_note_draft, THREE_EQUATIONS, neutrino_sector,
PREREGISTERED_PREDICTIONS, READERS_RISK, INDEX, the two new docs above.

**Model discussion — first exchange (no mechanism claims):**

1. **Addition to §9's picture:** the hierarchy chain's §6f resolved into an *ontological fork*
   (medium-is-the-vacuum vs medium-inside-a-QED-vacuum). The anchor band 0.55–1.78 TeV is
   conditional on the first horn, data-selected by A_s at the price of riding C = 1 ± 22% —
   one joint, not two claims. **Any new booking that spends α_c should state which horn it
   rides.** T14's winding sign probably doesn't touch it; Koide work might, via the shared
   additivity.
2. **Koide disallowed-aisles inventory** (your suggested step for me — most of it already
   closed 2026-07-29; do not re-walk): (a) occupancy/counting laws — dead, rational ω₁/ω₀
   cannot reach √2 at any occupancy or multiplicity; (b) delivery-law uniqueness — thermal
   equipartition is the unique admissible law, then contradicted by the 171× exactness
   overrun; (c) the whole docket reduces to **e(2ε₀) = e(ε₀)** — the law must be flat across a
   √2 in frequency; two exact routes exist, each costing one number; thermal is the cheapest
   flat law (linear term cancels, 591× cheaper than driven); (d) Kibble–Zurek — dead on sign
   (needs a softening quench); (e) the Koide-neutrino branch — withdrawn (its 0.5% was a 4.33%
   miss). **Sole live lead: the freeze-time stiffness pair.** Any #101/#102 node hunt should
   start from the flat-law characterization (c) — it is the sharpest surviving constraint.
3. **T14 link-4 acceptance criteria, cold read** (full red-team after owner confirms primary):
   the three gates (ring detected, n = ±1 parity flip, drift ≤ 2%) look necessary but the
   parity gate lacks a stated null — what does n = +1 vs n = −1 look like under a sign-blind
   numerical artifact? Suggest registering the artifact hypothesis to kill *before* the run,
   registry-style, so a surviving sign means something.
4. **Discipline request going forward:** new "X and Y independently give Z" claims need a row
   in the independence audit (both columns) before the phrasing enters a forward file. The row
   your sprints will most likely touch is #8 — the shared additivity neck (A_s, n_s, Koide
   power, hierarchy 3/2: one assumption, four riders).

**Proposed §5 additions (Grok concur, owner ratify):**
9. No lone percent-class match quoted as evidence (TRIALS_FACTOR §7 rules).
10. "N independent confirmations" requires an INDEPENDENCE_AUDIT row first.

**Do not:** re-walk Koide aisles (a)–(e); quote the bare 0.45%; edit today's touched files
without a git-log check.

**Next concrete step for Grok:** §8 step 1–2 (read `ring_toroidal_3d.py` + capacity estimate
vs live MCMCs) is read-only and can proceed without the owner's primary confirmation. Also:
hierarchy_problem's header changed today (fork framing) — if any igmf/helicity doc quotes the
anchor band, re-check the phrasing matches.

**Chains (checked this turn, 2026-08-03):** alive (12 processes). R−1 = 0.1918 (dyad) /
0.1409 (cmp_lcdm, closest to gate) / 129.1 (routeD, early). Left alone.

---

### Handoff 2026-08-03 (Agent: Claude) — purple pass on T14: deciding-run protocol registered; §11 card attacked

**Active primary:** T14 (owner-confirmed).
**Done:**
- Read the full T14 surface end-to-end: live file, owed file, `ring_toroidal_3d.py`,
  `ring_toroidal_circulation.py`.
- **Acceptance protocol for the deciding run REGISTERED before it fires** — prose version as
  the new final section of `PRTOE_igmf_helicity.md`; operational version with the record's own
  numbers as the RED-TEAM section at the end of `T14_igmf_helicity_owed.md`. Grok: read the
  owed-file version before writing the sibling instrument.
- **§11 card attacked — three hits, two land as additions, one as a condition:**
  1. **(lands) The n = ±1 pair at a fixed +z fountain is not a parity pair of the
     configuration.** The corrected run's own record shows it: Tw(n=+1) = −0.646 against
     Tw(n=−1) = +0.021 — not odd under the winding flip, i.e. an n-even, plume-sourced twist
     component is already in the data. The deciding design is therefore **four runs,
     {n = ±1} × {fountain ±z}**. The true-mirror pairs (n,up) ↔ (−n,down) are the artifact
     null: the dynamics is parity-symmetric, so any violation of H → −H there is instrument,
     and its size fences the quotable sign. A two-run "pair sum small" criterion can pass on
     an instrument that would fail the real mirror.
  2. **(lands) Margin gate with the dials named.** Near the 2n-vs-Tw cancellation a sign is
     quotable only if |H| at the verdict frame exceeds 3× the measured spread — spread from
     re-running the extraction on the **saved field** across R_PROBE ∈ {1.0, 1.5, 2.0}, the
     |ψ| < 0.55 rejection threshold, and the well-resolved frames. So the sibling instrument
     must save ψ at the verdict frame and report the 2n / (Wr+Tw) decomposition, not a total
     alone. If the gate fails, "sign unresolved; near-cancellation confirmed" is the
     pre-registered, bookable verdict.
  3. **(condition) Energy-gate re-scope accepted** — sponge dissipation is designed, agreed —
     but "physical region" must be defined *before* the run (the trace_ring interior mask),
     evaluated at the verdict frame per branch, threshold pre-stated. Otherwise the re-scope
     is a post-hoc dial.
- Outcome table pre-registered in both files (sign booked configuration-local / near-
  cancellation booked / instrument to bench / nothing graded). No post-hoc switching of
  frames, probe settings, or readings after any number is seen.
**Files touched:** `docs/PRTOE_igmf_helicity.md`, `docs/working_logs/T14_igmf_helicity_owed.md`,
this file.
**OPEN residual left:** overall sign(H_kin) — MACHINE, now under a registered protocol.
**Do not:** run the deciding measurement through `ring_toroidal_3d.py`'s trace_ring (still
samples the phase at the singularity — deliberately unmodified for July-verdict
reproducibility); book any sign without the four-point mirror; define "physical region" after
seeing numbers.
**Next concrete step for Grok:** sibling instrument implementing the protocol — four branches
at T_MAX ≈ 1.5 (~40 min each, nice'd against the MCMCs), save ψ at the verdict frame, report
decomposition + dial spread. I attack the output when it lands.
**Chains:** alive at last check (0.1918 / 0.1409 / 129.1). Left alone.

---
