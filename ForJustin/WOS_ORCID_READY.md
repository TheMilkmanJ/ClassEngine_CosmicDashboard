# ORCID + Web of Science — what is finished vs what needs you

**Date:** 2026-08-10  
**Your ORCID:** https://orcid.org/0009-0003-8018-9869  
**Your WoS ResearcherID:** `QUT-6978-2026`  
**WoS author page:** https://www.webofscience.com/wos/author/record/QUT-6978-2026

---

## Honest limit (important)

**Grok cannot log into Web of Science or ORCID as you and “post” publications.**

There is no safe way for an AI to:

- hold your password, or  
- click **Authorize** / **Manual sync** for you, or  
- invent DOIs you do not have  

What *is* ready is a **local OAuth helper** that writes **after you authorize once in the browser**.

---

## What is already done for you

| Item | Status |
|---|---|
| ORCID account linked to WoS | **Done** (you synced; ResearcherID on ORCID) |
| Local helper app | **Built:** `scripts/orcid_assist/` |
| Profile config | **No fake affiliation**, **no fake DOIs** |
| Keywords / other-names prepared | In `profile.yaml` (optional apply) |
| Works list | **Empty on purpose** — no PRTOE DOI/arXiv yet |
| Dry-run of helper | Works (`python3 scripts/orcid_assist/app.py`) |

---

## What “posting” can mean for you right now

### A) Profile hygiene only (no papers) — optional today

After you create ORCID API client + `.env`:

```bash
python3 scripts/orcid_assist/app.py --apply
```

That can write **keywords** + **other names** only (no employment, no works).

Then in WoS: nothing new appears for publications (expected — nothing published).

### B) Publications — only when you have something public

| Content | How it gets to ORCID | How it gets to WoS |
|---|---|---|
| Journal paper | DOI → helper or ORCID “Add DOI” | ORCID → WoS **Manual sync**, or claim in Core Collection |
| arXiv preprint | arXiv id on ORCID | Usually **not** in WoS Core until journal DOI |
| This private PRTOE repo | **Not a publication** | Cannot “post” |

### C) Literature alerts (not “your papers”)

You run searches inside WoS and click **Create alert**.  
I can keep giving you the query text; I cannot create alerts in your account.

Suggested queries stay in `ForJustin/WEB_OF_SCIENCE_NEXT_STEPS.md`.

---

## What I need from you to go further

1. **ORCID Public API Client ID + Secret** in local  
   `scripts/orcid_assist/.env`  
   (never paste the secret in chat — only on your machine)  
2. Say whether you want **keywords applied** now (`--apply` profile only)  
3. When you have an arXiv id or DOI later, paste it → I fill `works_to_add.yaml` → you run `--apply` → you click WoS Manual sync  

---

## Bottom line

| Question | Answer |
|---|---|
| Is ORCID/WoS setup “finished”? | **Accounts yes; publication list empty (correct).** |
| Can Grok post papers to WoS for you? | **No** — not without your OAuth click, and not without real DOIs. |
| Can Grok prepare everything for later? | **Yes — already done.** |
| What should you do today? | Optional: keywords via helper after `.env`; otherwise wait for arXiv/journal. |

*Desk process only — not a physics claim.*
