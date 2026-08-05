# Blocked lane audit — bbnfix booking gate (2026-08-05)

Purpose: freeze one shared blocked lane exactly, so `PRTOE_hubble_tension.md` and
`PRTOE_neutrino_home.md` stop drifting into repeated prose variants of the same machine gate.

## Lane

Shared booking gate for:

- `docs/PRTOE_hubble_tension.md`
- `docs/PRTOE_neutrino_home.md`
- supporting live board: `docs/PRTOE_CHAIN_TABLES.md`

This lane controls whether the desk may quote **booked** live-pair:

- `H0`
- `Sigma m_nu`
- pairwise `Delta chi2` / `Delta ln Z`

## Authority run

Latest booking artifact on disk from `python3 scripts/book_bbnfix_when_ready.py`:

- `docs/working_logs/_runs/bbnfix_booking_20260805_222942/REPORT.md`

The script result there is:

- `REFUSED — booking blocked (gate closed).`

## Gate definition

The gate is:

- both legs must have progress `R−1 < 0.05`
- both legs must have checkpoint `converged: true`
- progress `R−1` is the gate authority, not offline GetDist diagnostics

## Exact failing state

| leg | N | progress R−1 | timestamp | checkpoint `converged` | gate state |
|---|---:|---:|---|---|---|
| `dyad_mnu_bbnfix` | 26135 | `0.060201` | `2026-08-05T15:50:02.745947` | `false` | **FAIL** |
| `cmp_lcdm_mnu_bbnfix` | 26294 | `0.049324` | `2026-08-05T11:52:10.194879` | `true` | PASS |

`dyad_mnu_bbnfix` fails twice:

1. `R−1` is still above the bar
2. the sampler has not self-stopped

`dyad_mnu_bbnfix` moved **away** from the bar from `0.056889 @ N=24677` earlier the same day to
`0.060201 @ N=26135`.

So the lane is blocked by the **dyad** leg alone.

## What this means

### Allowed

- quote the gate exactly as blocked
- quote the live pair state with `N`, `R−1`, timestamp, and `converged`
- keep pre-bbnfix production claims explicitly labeled as pre-bbnfix

### Forbidden

- quote booked live-pair `H0`
- quote booked live-pair `Sigma m_nu`
- quote booked live-pair `Delta chi2` or `Delta ln Z`
- treat offline GetDist `GR` or crude param `R−1` as the booking gate
- silently replace pre-bbnfix numbers with unconverged peeks

## Real unblock path

There is only one honest closure path:

1. let `dyad_mnu_bbnfix` continue until progress `R−1 < 0.05`
2. let the sampler self-stop so checkpoint `converged: true`
3. rerun `python3 scripts/book_bbnfix_when_ready.py`
4. refresh dependent docs from the new booking card only

No docs-only polish cures this lane.

## Dependent docs

Use this audit as the shared blocker reference for:

- `docs/PRTOE_hubble_tension.md`
- `docs/PRTOE_neutrino_home.md`

If the gate changes, update this audit first, then propagate the exact new booked state into the
dependent docs.
