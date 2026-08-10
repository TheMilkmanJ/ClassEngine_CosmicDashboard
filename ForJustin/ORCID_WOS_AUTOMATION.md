# ORCID / Web of Science automation — what is safe and real

## Short answer

| Idea | Verdict |
|---|---|
| Give Grok your password | **No.** Never. |
| Browser extension that stores your password | **No.** |
| **OAuth app you authorize** (you click “Allow”) | **Yes** for ORCID; limited for WoS |
| Me driving your desktop while you watch | Possible with screenshare tools, still **you** approve each step |

You do **not** need to invent a password-stealing “setup bot.” Use **OAuth**: the industry-standard way for apps to act *with your consent* without ever seeing your password.

---

## What works well: ORCID OAuth app

ORCID is designed for this.

1. You (or we) register a free **ORCID Public API** application at  
   https://orcid.org/developer-tools  
   (Member API if you later get institutional member access.)
2. The app has: Client ID, Client Secret, redirect URI (e.g. `http://127.0.0.1:8765/callback`).
3. You open a browser link → log in as yourself → **Authorize**.
4. The app receives a **short-lived token** and can (with scopes you grant):
   - read works / employment
   - **add or update works** (with write scopes)
   - set keywords, URLs, external IDs
5. Token can be revoked anytime on ORCID → Account settings → Trusted organizations.

### Minimal local app we could build in this repo

```
scripts/orcid_assist/
  app.py              # local Flask/FastAPI on 127.0.0.1
  works_to_add.yaml   # your DOIs / arXiv list (you edit)
  README.md
```

Flow:

1. `python scripts/orcid_assist/app.py`
2. Browser opens ORCID authorize
3. App writes DOIs from `works_to_add.yaml` into your ORCID works
4. You still click **one** manual sync in Web of Science (ORCID → WoS)

That is the right design: **I prepare the YAML and code; you authorize once; no password leaves your machine.**

---

## Web of Science / Clarivate — harder

| Capability | Reality |
|---|---|
| Researcher Profile claim UI | Mostly **interactive**; not a clean public write API for “add all my papers” |
| ORCID → WoS sync | **Already on** for you; best automated path |
| Core Collection search / alerts | Often needs **institutional** session; APIs are commercial (Clarivate APIs / WoS API) and key-gated |
| ResearcherID | Already assigned: `QUT-6978-2026` |

So the practical automation split is:

1. **Automate ORCID** (OAuth app + DOI list) ← high value  
2. **One-click WoS** “ORCID Syncing → manual sync” ← 10 seconds human  
3. **Alerts** ← you create once under library login; hard to automate without Clarivate API contract  

Building a “full WoS robot” that pretends to be a browser with your password is **not** something we should design.

---

## Implemented (2026-08-10)

**Phase 1 is in the repo:** `scripts/orcid_assist/`

| File | Role |
|---|---|
| `app.py` | Local OAuth + dry-run + `--apply` writes |
| `profile.yaml` | Employment, keywords, other names |
| `works_to_add.yaml` | DOIs / arXiv list |
| `.env.example` | Client ID/secret template |
| `README.md` | Full run instructions |

Owner path: `ForJustin/OWNER_RUN_NOW.md`.

**Still need from you (cannot invent):**

- ORCID **Client ID + Secret** (developer-tools, redirect `http://127.0.0.1:8765/callback`)
- Preferred **affiliation** string (edit `profile.yaml`)
- **DOI / arXiv list** (edit `works_to_add.yaml`)
- One browser **Authorize** + WoS **Manual sync**

**Phase 2 (optional later):** BibTeX import, richer education XML, Zotero.

---

## Security rules (non-negotiable)

1. No passwords in chat, files, or env committed to git.  
2. OAuth tokens only on your machine; `.gitignore` for `.env` and `token.json`.  
3. Scopes least-privilege (`/activities/update` only if adding works).  
4. You can revoke Clarivate + any custom app on ORCID anytime.  

*Desk process — not a PRTOE physics claim.*
