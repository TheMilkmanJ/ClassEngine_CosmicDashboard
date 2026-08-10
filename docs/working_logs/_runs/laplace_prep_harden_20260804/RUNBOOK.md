# RUNBOOK (harden package) — post-gate Stage A / B only

**Use when both bbnfix legs grade.** Until then every entrypoint must refuse (exit 2).  
Working directory: repo root `/home/themilkmanj/prtoe_class`.

Full detail: `../laplace_booking_full_20260804/RUNBOOK.md` +  
`docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`.

---

## Gate (both required)

- progress R−1 **< 0.05** on `dyad_mnu_bbnfix` **and** `cmp_lcdm_mnu_bbnfix`
- checkpoint **`converged: true`** on both
- ranks `.1 .2 .3` present; chains **idle** for GetDist
- Safe check anytime: `python3 scripts/book_bbnfix_when_ready.py` → must be BOOKED (exit 0)

---

## Stage A — book / finalize (default; no forward shelf)

```bash
cd /home/themilkmanj/prtoe_class
bash scripts/bbnfix_when_ready_all.sh
# WRITE_TABLES=0 → book + finalize (+ Δχ² proxy); tables BLOCKED
```

Outputs: private `_runs/bbnfix_booking_<stamp>/` only; letter sentence on stdout.

---

## Red audit (required before publish)

Write on the booking package:

```text
docs/working_logs/_runs/bbnfix_booking_<id>/RED_AUDIT.md
```

Containing a line:

```text
red: AGREE
```

(or `red: AGREE-IF`).

---

## Stage B — tables (publish; needs RED_AUDIT)

```bash
bash scripts/bbnfix_when_ready_all.sh --write-tables
# refuses without red stamp (exit 1)
# owner emergency only: --force-tables
```

Restore `docs/PRTOE_CHAIN_TABLES.md` live banner if clobbered.

---

## Step C — Laplace (after Stage A book; not nested)

| ready prep | waits for bbnfix book |
|------------|------------------------|
| CosmicForge Hessian formula in `run_cosmicforge.py` | Bookable ΔlnZ under BBN-fixed yamls |
| `bbnfix_delta_chi2_proxy.py` (proxy only) | Proxy number |
| Pre-bbnfix ΔlnZ ≈ +2.6 (historical; **fenced**) | Must **not** rebrand as bbnfix final |

```bash
# only after self-stop / capacity; confirm CLI first
python3 run_cosmicforge.py --help | head -40
# no --polychord / nested
```

Label method **Laplace (Hessian)** + stack **BBN-fixed**.  
**Do not invent a number. Do not promote pre-bbnfix ΔlnZ ≈ +2.6 without fence.**

---

## Kill criteria (stop; do not claim done)

| # | kill if… |
|---|----------|
| K1 | Book while either R−1 ≥ 0.05 |
| K2 | Book before both self-stop |
| K3 | Quote peeks / force GetDist / force Δχ² as results |
| K4 | Living shelf from `--force-bbnfix` |
| K5 | Stage B without RED_AUDIT (except owner `--force-tables`) |
| K6 | PolyChord / nested for booking |
| K7 | Kill live MCMCs without owner order |
| K8 | Promote pre-bbnfix ΔlnZ ≈ +2.6 as final bbnfix evidence without fence |
| K9 | RouteD substitute for letter pair |
| K10 | Invent Laplace number / invent `scripts/laplace_bbnfix.py` |

---

## Refuse codes

| exit | meaning |
|-----:|---------|
| 0 | Stage A book ok / Stage B tables written |
| 2 | gate refuse (not ready) |
| 1 | post-gate error **or** Stage B missing RED_AUDIT |

*NO FABRICATIONS. NO EARLY BOOK. NO POLYCHORD. booking ≠ publishing.*
