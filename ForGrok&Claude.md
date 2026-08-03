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

| Lane | Primary agent | Secondary agent |
|---|---|---|
| T14 3D / gates / ledger | **Grok** | Claude reviews gates + prose in `PRTOE_igmf_helicity.md` |
| Koide #101/#102 mechanism | **Claude** | Grok runs scripts, checks fence arithmetic, ledger rows |
| Bounce constraints only | **Either** (low duty cycle) | Never both inventing turns in parallel |
| Package hygiene / arXivReady | Grok | Claude proofreads TeX if endorsement near |
| Live MCMC watch | Grok (shell) | Claude must not kill/relaunch without owner |
| Endorsement / Fairbank / Zenodo | **Owner only** | Agents prepare packages only |
| Subagents | Grok spawns for parallel hygiene / audit | Claude may use own tools; write results into this file |

**Conflict rule:** if both agents edit the same theory file, **stop and merge via owner**. Prefer one writer per file per day.

**Git rule:** no force-push; no amend of published commits; ask owner before push to `main`.

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
- Theory claims: one agent drafts, the other **adversarial-reviews** (red-team), then owner accepts.  
- Scripts: Grok owns long runs; Claude may propose patches but should not start 10 h sims without checking CPU against MCMCs.

---

## 7. Active assignment (edit when owner reassigns)

| Role | Focus | Status |
|---|---|---|
| **Primary theory** | T14 link 4 (`ring_toroidal_3d`) | **PENDING kickoff** — not yet running this dual brief |
| **Secondary theory** | Koide #101/#102 | Support / mechanism only; not closed |
| **Tertiary** | Bounce B18 constraints | Idle unless primary stalls |
| **Packages** | READY; neutrino with Fairbank | Owner endorsements |
| **MCMC** | Leave running | Watch only |
| **Claude — standing role (owner-assigned 2026-08-03)** | **Purple team: mostly red, a hint of blue.** Red: adversarial review of every booking before it lands — gates, signs, arithmetic, independence rows, trials discipline; default posture is *try to refute*. Blue: the hardening instruments (TRIALS_FACTOR, INDEPENDENCE_AUDIT, check-12 sweep, quotation rules) and fixes that survive review. Claude does not draft mechanisms; Grok (or owner) drafts, Claude attacks, owner accepts. | **Active** |

**Owner decision needed:** confirm primary = T14 (recommended) or reassign. (Claude's role is
now fixed by the owner; the open decision is Grok's primary lane.)

---

## 8. Concrete first tasks (after owner confirms primary)

### If primary = T14 (recommended)

**Grok:**
1. Read `scripts/ring_toroidal_3d.py` end-to-end + any prior run logs under `docs/working_logs/_runs/`.  
2. Estimate wall-clock / RAM vs live MCMCs (do not starve bbnfix).  
3. If capacity allows: run n=+1 and n=−1 under gates; capture energy drift, ring detection, shape helicity, excess phase twist.  
4. Write results into `T14_igmf_helicity_owed.md` + `PRTOE_igmf_helicity.md`; bury dead fork in failures ledger if needed.  
5. Append handoff.

**Claude:**
1. Read T14 docs + link 5 negative closure; red-team the *interpretation* of any numerical sign before it is booked.  
2. Optionally draft the “what would close link 4” acceptance criteria prose for the live file (without inventing a number).  
3. Parallel **only if idle:** re-read Koide #101 surface and list *disallowed* aisles already retired (do not invent the node).

### If primary = Koide

**Claude:** mechanism hunt under constraints of `T6_koide_desk_status.md` “Truly open” table.  
**Grok:** arithmetic reconfirm scripts; ensure no desk residue is mislabeled theory.

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

- [ ] Confirm primary theory sprint (T14 recommended).  
- [ ] Endorsements: radio-lattice, lattice-tc-gap, bbn-eps-bound, kination (± supertrace).  
- [ ] Fairbank / neutrino-mbb thread (external).  
- [ ] When bbnfix R−1 ≤ 0.05: authorize posterior booking.  
- [ ] RouteD reseed: only if second progress still pathological **and** you fire surgery.

---

## Handoffs (append below)

### Handoff 2026-08-03 (Agent: Grok)

**Active primary:** unassigned pending owner confirm (recommend **T14**).  
**Done this dual-brief session:**
- Created `ForGrok&Claude.md` with strategy, model brief, three-sprint cards, labor split, hard rules.
- Prior session state still holds: packages READY, docs PAPER_CANDIDATE = 0, neutrino with Fairbank, MCMCs alive.
**Files touched:**
- `ForGrok&Claude.md` (new)
**OPEN residual left:**
- T14 link 4; Koide #101/#102; Bounce B11/B18
**Do not:**
- Parallel deep mechanism invention on all three; kill chains; invent packages; mark theory COMPLETE without derivation
**Next concrete step for Claude:**
- Read this file §§0–3 and §9; if owner confirms T14 primary, red-team link-4 acceptance criteria and optionally start Koide *disallowed-aisles* inventory only
**Chains:** leave alone (last known R−1 ~0.19 / 0.14 / 129)

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
