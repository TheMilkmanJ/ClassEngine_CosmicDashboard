# ORCID assist (local OAuth)

Sets up **your** ORCID record with consent. Passwords never leave your browser.

**ORCID:** `0009-0003-8018-9869`  
**WoS ResearcherID:** `QUT-6978-2026`

## One-time: create ORCID API client (5 minutes)

1. Sign in at [orcid.org](https://orcid.org) → [Developer tools](https://orcid.org/developer-tools)
2. **Register a Public API client**
3. **Redirect URI** (exact):

   ```text
   http://127.0.0.1:8765/callback
   ```

4. Copy **Client ID** and **Client Secret**

## Install + configure

```bash
cd /home/themilkmanj/prtoe_class
pip install -r scripts/orcid_assist/requirements.txt
cp scripts/orcid_assist/.env.example scripts/orcid_assist/.env
# edit .env with Client ID + Secret
```

Edit:

- `scripts/orcid_assist/profile.yaml` — affiliation, keywords, other names  
- `scripts/orcid_assist/works_to_add.yaml` — DOIs / arXiv IDs  

## Run

```bash
# see public status + planned actions (no write)
python3 scripts/orcid_assist/app.py --status
python3 scripts/orcid_assist/app.py

# authorize in browser and write
python3 scripts/orcid_assist/app.py --apply
```

After works land on ORCID:

1. [webofscience.com](https://www.webofscience.com) → Researcher Profile  
2. **Edit → ORCID Syncing → Manual sync** (ORCID → WoS)  
3. Optional: claim Core Collection papers; create alerts  

## Security

| File | Commit? |
|---|---|
| `.env` | **Never** (gitignored) |
| `token.json` | **Never** (gitignored) |
| `profile.yaml` / `works_to_add.yaml` | OK if no secrets |
| `last_run_report.json` | gitignored |

Revoke access anytime: ORCID → Account settings → Trusted organizations.

## Limits

- Public API write works for personal records you own after OAuth.  
- Web of Science claim UI / alerts still need **you** in the browser (no safe password automation).  
- Empty `works: []` means nothing to publish until you add DOIs.
