# EC2 quota increase requests — 2026-08-08

Region: **us-east-1**  
Account: **691687038930**

## Requests (PENDING / CASE_OPENED)

| Pool | Code | Was | Requested | Request Id |
|---|---|---:|---:|---|
| On-Demand Standard vCPUs | `L-1216C47A` | 96 | **512** | `ea6c7cc3d0c3403c96040d56a0f5448d2k6gGjJv` |
| Spot Standard vCPUs | `L-34B43A08` | 96 | **512** | `abac48e4f0fe43988b1ffd0267527a749cvjvsRN` |

There is **no fixed AWS “max”** for this quota — it is adjustable; approval is case-by-case. Prior closed case set the limit to 96 (from default 5).

## What 512 enables (if fully approved)

| Workload | vCPU each | Example parallel set |
|---|---:|---|
| DESI-DR2 MCMC pair | 32 (`c7i.8xlarge`) | 1 box |
| PolyChord leg | 96 (`c7i.24xlarge`) | up to **5** simultaneous nested boxes |
| **Total example** | | 32 + 5×96 = **512** |

Practical “all polychords at once” for the evidence twin pair only needs **2×96 + 32 = 224**. 512 is headroom for more stacks (old-BAO nested, DESI nested, etc.).

## Check status

```bash
aws service-quotas get-requested-service-quota-change \
  --region us-east-1 --request-id ea6c7cc3d0c3403c96040d56a0f5448d2k6gGjJv
```

Or console: Service Quotas → EC2 → request history.

## Notes

- Approval may take hours–days; AWS may grant a **partial** amount (e.g. 192–256).
- On-demand cost: each `c7i.24xlarge` ~\$4+/hr — parallel nested multiplies burn rate.
- Do not launch until quota shows Value ≥ needed sum of vCPUs.
