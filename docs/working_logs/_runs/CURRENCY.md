# Working-logs `_runs/` currency pointer — **2026-08-15**

**Purpose:** Dated packages under `_runs/` are **historical receipts**. Their body text often
still says “DESI not bookable”, “nested not launched”, “bounce OPEN-BLOCKED”, “zon not running”,
or “bbnfix NOT YET” because that was true **on the stamp date**. Those lines are **not** live truth.

## Live authority (use these)

| Domain | Live package / file |
|--------|---------------------|
| Bounce claims | [`bounce_desk_freeze_20260812/`](bounce_desk_freeze_20260812/) |
| Bounce honesty | [`bounce_e9_honest_partial_20260812/`](bounce_e9_honest_partial_20260812/) (**PAPER_CLAIM_LOCKED**) |
| Bounce terminal | [`bounce_fa3suf_israel_e8e9_terminal_20260813/`](bounce_fa3suf_israel_e8e9_terminal_20260813/) |
| Docs closeout | [`docs_full_closeout_20260813/`](docs_full_closeout_20260813/) |
| Docs line audit (2026-08-15) | [`docs_line_audit_20260815/`](docs_line_audit_20260815/) |
| Invention + external dual track (six residuals) | [`invention_and_external_20260815/`](invention_and_external_20260815/) |
| Invention kill-or-derive (APPROVE battery) | [`invention_kill_derive_20260815/`](invention_kill_derive_20260815/) |
| Non-PC open execute | [`open_nonpc_execute_20260815/`](open_nonpc_execute_20260815/) |
| Nested ops | [`dual_nested_runbook_20260812/`](dual_nested_runbook_20260812/) |
| Nested PC ETA stamps | [`nested_pc_eta_20260815/`](nested_pc_eta_20260815/) |
| zon retune (ops stop) | [`zon_disp_retune_20260814/`](zon_disp_retune_20260814/) |
| zon GetDist grade | [`zon_disp_retune_grade_20260821/`](zon_disp_retune_grade_20260821/) |
| conv_desi GetDist grade | [`conv_desi_retune_grade_20260824/`](conv_desi_retune_grade_20260824/) |
| Stage A chains | [`../../PRTOE_CHAIN_TABLES.md`](../../PRTOE_CHAIN_TABLES.md) (archive GetDist **fenced**) |
| Desk closeout | [`deskwork_closeout_20260812/`](deskwork_closeout_20260812/) |
| Full-corpus scan | [`docs_full_currency_scan_20260812/`](docs_full_currency_scan_20260812/) |

## Live machine facts (2026-08-24)

- Nested: LCDM UltraNest one-legs **FINISHED** (SH0ES −1413.4857 ± 0.5842, TRGB −1374.3615 ± 0.3982, noH0 −1374.4346 ± 0.3765). Dyad UN + PolyChord still live. Mid-run logZ **forbidden**. No twin ΔlnZ.
- zon_disp retune **STOPPED** (R−1=0.036); GetDist **INCONCLUSIVE** on `log10_zon` (7.57±0.51). Package `zon_disp_retune_grade_20260821`
- Stage A MCMC **BOOKED** for three stacks (old-BAO SH0ES; DESI-DR2 SH0ES; DESI-DR2 TRGB)
- conv_desi retune **STOPPED** (R−1=0.0447); GetDist **INCONCLUSIVE** on `dcdf_conv_g` (0.080±0.072). Package `conv_desi_retune_grade_20260824`. Not a KiDS shear fit.

## What not to do

- Do **not** rewrite historical REPORT bodies to match today’s grades (breaks audit trail).
- Do **not** quote mid-run nested logZ as ΔlnZ.
- Do **not** promote O2 magnitude from E7 2D peaks.

## Invention fence (owner, 2026-08-12)

- Full project permissions for desk/machine work.
- **Invent physics only if the model is calling for it** (named gap after stocked kill/obstruction).
- **No bullshit physics.** If invention is required, **go over it with the owner first** before landing.
- Detail: [`bounce_construction_20260812/CHARTER.md`](bounce_construction_20260812/CHARTER.md)

## Scan tools

```bash
# live shelf only (must be CLEAN)
python3 scripts/docs_stale_currency_scan.py

# full ~1700-file corpus (historical hits expected)
python3 scripts/docs_full_currency_scan.py
```

**Rule:** if a `_runs` file and a live shelf file disagree, the **later freeze / Stage A receipt /
desk freeze** wins for live claims.
