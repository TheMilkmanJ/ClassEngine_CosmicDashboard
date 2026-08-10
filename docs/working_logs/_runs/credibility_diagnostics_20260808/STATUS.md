# Credibility package status — 2026-08-08

## AWS reauth

**Blocked on interactive browser login.** CLI 2.36 OK; session expired.  
Run locally (you must complete the browser step):

```bash
aws login --remote
# open the printed URL, paste the code back into the terminal
aws sts get-caller-identity
```

Then DESI-DR2 check:

```bash
# on-demand box was i-096d08d2dc9d8f42c / prtoe-pc-probe
aws ec2 describe-instances --region us-east-1 \
  --filters Name=instance-state-name,Values=running \
  --query 'Reservations[].Instances[].[InstanceId,InstanceType,PublicIpAddress,Tags[?Key==`Name`].Value|[0]]' \
  --output table
```

## Done this session

| deliverable | path |
|---|---|
| Checklist | `CHECKLIST.md` |
| Nested plan | `NESTED_SAMPLING_PLAN.md` |
| GetDist diagnostics script | `scripts/bbnfix_posterior_diagnostics.py` |
| GetDist results | `posterior_diagnostics.json` |
| Hessian Laplace script | `scripts/bbnfix_hessian_laplace.py` |
| Sample-cov Laplace (prior) | `../laplace_docs_chains_bbnfix_20260808/` |

## Posterior health (B1–B3) — old-BAO docs/chains

| leg | progress R−1 | GetDist GR | ESS_total | H0 |
|---|---:|---:|---:|---|
| dyad | 0.0481 | 0.039 | **492** | 70.05 ± 0.72 |
| lcdm | 0.0493 | 0.055 | **288** | 68.35 ± 0.34 |

ESS ≥ 200 on both (dyad healthier). **Pass B2 at minimum bar.**  
Sample-cov Laplace still soft (cond ~1e8, ΔlnZ ≈ +0.21).

## Evidence next (C2)

Full FD Hessian is O(d²) CLASS calls (~13²×2 legs). Launch:

```bash
python3 scripts/bbnfix_hessian_laplace.py --chain-dir docs/chains --which both \
  --out docs/working_logs/_runs/credibility_diagnostics_20260808/hessian_laplace.json
```

Smoke (3-D only, not bookable): add `--max-fd`.

## Honest readout

Posterior sampling looks **real and usable**. Evidence for “model better than ΛCDM” is **still not there** under volume-aware Laplace. Nested remains the clean next bar after DESI-DR2 MCMCs and Hessian C2.

## AWS reauth (update)

**OK** as of 2026-08-08T18:56Z — root account `691687038930`.

DESI-DR2 twins **live** on `i-096d08d2dc9d8f42c`:
- dyad R−1 ≈ 0.109 @ N≈21827
- lcdm R−1 ≈ 0.140 @ N≈22848
- both `converged: false` — gate closed

