# Owner run-now checklist (2026-08-10)

## 1) ORCID + Web of Science (you — ~15 min after DOIs)

App is ready at `scripts/orcid_assist/`.

```bash
cd /home/themilkmanj/prtoe_class
pip install -r scripts/orcid_assist/requirements.txt
cp scripts/orcid_assist/.env.example scripts/orcid_assist/.env
```

1. Create Public API client: https://orcid.org/developer-tools  
   Redirect URI: `http://127.0.0.1:8765/callback`  
2. Put Client ID + Secret in `.env`  
3. `profile.yaml` / `works_to_add.yaml` — **no affiliation, no DOIs yet** (parked until arXiv/journal)  
4. Optional: run `--apply` only for keywords/other-names after OAuth client exists  
5. Run (optional until you have papers):

```bash
python3 scripts/orcid_assist/app.py           # dry-run plan
python3 scripts/orcid_assist/app.py --apply   # browser Authorize
```

6. Web of Science → Researcher Profile → **ORCID Syncing → Manual sync**  
7. Create alerts (library login if needed) — queries in `WEB_OF_SCIENCE_NEXT_STEPS.md`

**Cannot be finished by Grok alone:** Client secret + your DOIs + one browser Authorize.

---

## 2) Hessian status (machine)

| Job | Instance | Status |
|---|---|---|
| Old-BAO FD Hessian v2 | `i-090c0275d8198ae14` | **DONE** — JSON at `credibility_diagnostics_20260808/hessian_laplace_v2.json`; instance **stopped** |
| DESI-DR2 FD Hessian | `i-096d08d2dc9d8f42c` 48 | **DONE** — JSON peeled (`hessian_laplace_desi.json`); ΔlnZ_H≈−25 vs samplecov +1.5 — **not bookable** |

Still **not nested**. **Stop the 48-box** when convenient (MCMC booked + Hessian done) to save cost.

---

## 3) Still running (leave alone)

| Job | Instance | Notes |
|---|---|---|
| Gold PC SH0ES dyad | `i-04ead482af737e7bf` 96 | nested sampling (resume) — leave alone |
| Gold PC SH0ES lcdm | `i-0e353f38544397a6d` 96 | nested sampling (resume) — leave alone |

Quota 300; ~192 in use if DESI 48 stopped (PC pair only). TRGB needs free ≥96.

### MCMC dual-gates (done)

| Pair | Receipt |
|---|---|
| Old-BAO bbnfix | Stage A+B `bbnfix_booking_20260808_005626` |
| DESI-DR2 bbnfix | Stage A `desidr2_bbnfix_booking_20260810_053127` + peel |

Stage B old-BAO published (Grok red). Nested still open.

---

## 4) Paste back when ready

- Affiliation line for `profile.yaml`  
- DOI / arXiv list for `works_to_add.yaml`  

Grok can then pre-fill those files and re-run dry-run verification.

*NO FABRICATIONS on physics. OAuth only for identity tools.*
