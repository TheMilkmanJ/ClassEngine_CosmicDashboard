# Owner run-now (currency 2026-08-12)

## Do not thrash

- Nested mid-run logZ (UltraNest or PolyChord)
- Mixing SH0ES / TRGB / old-BAO H₀ without labels
- Another soft-mode Laplace as if nested

## Live fleet (leave alone unless cost emergency)

| job | instance | notes |
|---|---|---|
| UltraNest dyad ×96 | `i-04ead482af737e7bf` | multi-day |
| UltraNest lcdm ×96 | `i-0e353f38544397a6d` | multi-day |
| PolyChord dyad ×96 | `i-0c65cc61a575bdfa7` | GIL + 1.22.2 |
| PolyChord lcdm ×48 | `i-096d08d2dc9d8f42c` | GIL; tuple-return fix |

Idle hessian 48 (`i-090c0275…`) **stopped**.

## MCMC dual-gates (done)

| pair | status |
|---|---|
| old-BAO bbnfix | BOOKED |
| DESI SH0ES | BOOKED |
| DESI TRGB | **BOOKED Stage A** 2026-08-12 |
| RouteD | BOOKED Stage A |

## Nested still open

Gold Bayes factor only after both nested engines finish.

## Optional owner chores (non-nested)

1. **Catherine reply (she answered 2026-08-12):**  
   - CosmoMC/MCMC full-stack smoke **done** → `docs/working_logs/_runs/catherine_cosmomc_smoke_20260812/` (evaluate PASS; MH sampling PASS)  
   - Send `docs/working_logs/_runs/catherine_triage_20260811/REPLY_TO_CATHERINE_20260812.md` (includes smoke results)  
   - Open PolyChordLite issue from `docs/working_logs/_runs/polychord_lite_issue_draft_20260811/GITHUB_ISSUE_v2.md`  
   - Attach `Cobaya/pypolychord_GIL_callbacks.patch` if not already  
   - Handley Cobaya PRs noted: #231 (NaN Cl), #233 (priors) — related debt, not the hang  
2. ORCID / Web of Science (see `WEB_OF_SCIENCE_NEXT_STEPS.md`) if still pending
3. Celebrate BYU — Software Engineering + IT path

## Quick check commands

```bash
# UN progress
aws ssm send-command --instance-ids i-04ead482af737e7bf --document-name AWS-RunShellScript \
  --parameters 'commands=["tail -5 /home/ubuntu/docs_runs/ultranest_20260811/un_dyad_ev_prod/debug.log"]'

# PC dyad
aws ssm send-command --instance-ids i-0c65cc61a575bdfa7 --document-name AWS-RunShellScript \
  --parameters 'commands=["pgrep -c -f pypolychord_cobaya; tail -3 /home/ubuntu/docs_runs/gold_pc_gil_mpi1_prod_*/dyad*/run.log"]'
```
