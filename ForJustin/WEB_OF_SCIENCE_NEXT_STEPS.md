# Web of Science + ORCID — do all (A–D)

**ORCID:** https://orcid.org/0009-0003-8018-9869  
**ResearcherID (from Clarivate):** `QUT-6978-2026`  
**WoS author record:** https://www.webofscience.com/wos/author/record/QUT-6978-2026  

**Public API snapshot (2026-08-10):** ORCID linked; ResearcherID present; **works = 0**; **employment = empty**; **education = empty**.  
You must click these yourself (no one else can authorize your login). Use this as a single pass.

---

## A) Add publications by DOI on ORCID (source of truth)

Do this **first**. Empty ORCID → empty WoS after sync.

1. Open https://orcid.org/0009-0003-8018-9869 and **Sign in**.
2. Go to **Works** (left or main profile section).
3. **+ Add** → **Add DOI**.
4. Paste a DOI (form `10.xxxx/...`) → **Retrieve DOI metadata** / continue.
5. Check title, year, journal, your name in authors → **Save to my works** (visibility: **Everyone** if you want them public).
6. Repeat for each published paper.

### If you only have arXiv (no journal DOI yet)

1. **Works** → **+ Add** → **Add manually** (or arXiv search if offered).
2. Work type: **Preprint**.
3. Title, authors, year; identifier type **arXiv** + e.g. `2501.01234`.
4. Visibility **Everyone**.
5. When a journal DOI appears later, **add that DOI** and merge/duplicate-clean if ORCID offers it.

### Optional bulk

- **Works** → **+ Add** → **Import BibTeX** if you have a `.bib` from Zotero/EndNote/ADS.

### After ORCID has works

1. [webofscience.com](https://www.webofscience.com) → sign in.
2. **Researcher Profile** → **Edit** → **Settings** → **ORCID Syncing**.
3. Confirm toggles: **Export records from ORCID → Web of Science** = ON.
4. **Manual sync** once.
5. **Publications** list should refresh (can take a few minutes).

**Blocker for me filling A for you:** public ORCID currently has **zero works**, and the PRTOE repo has **no author DOI list** for Justin Pulford. Paste DOIs/arXiv IDs here and I will turn them into a numbered “paste these” checklist.

---

## B) Claim publications inside Web of Science

Use when papers are already in Core Collection under your name (or a close name).

1. Sign in → open **Researcher Profile** (`QUT-6978-2026`).
2. Find **Publications** / **Add publications** / **Claim publications** (wording varies).
3. Search by:
   - **DOI**, or  
   - **Author name:** `Pulford J` / `Pulford Justin`, or  
   - Title keywords.
4. Open each candidate → confirm **you are a coauthor** → **Claim** / **Add to profile**.
5. Reject lookalikes (common surname collisions).
6. If two records are the same paper, **merge** if the UI offers it.

### If search finds nothing

Normal when:

- papers are only arXiv, or  
- not yet indexed, or  
- name form never appeared in WoS metadata.

Then rely on **A (ORCID DOI)** and re-sync; do not invent claims.

---

## C) Affiliation + name variants (hygiene)

### On ORCID (do both places)

1. Sign in → **Employment** → **+ Add employment**  
   - Organization (ROR lookup if shown)  
   - City / country  
   - Start date  
   - Role/title if you want  
   - Visibility: **Everyone**
2. **Education** → **+ Add** the same way if relevant.
3. **Names** / **Also known as**: add variants you publish under, e.g.  
   - `J. Pulford`  
   - middle initial if used  
4. Optional: **Keywords** — `cosmology`, `BAO`, `Hubble tension`, `neutrino mass`, `BBN`.
5. Optional: **Websites** — personal site, GitHub, arXiv author page when you have them.

### On Web of Science Researcher Profile

1. Profile → **Edit** (next to name).
2. Set **primary affiliation** to match ORCID employment.
3. Add **name variants** / alternative names if the field exists.
4. Confirm **ResearcherID** still shows `QUT-6978-2026`.
5. Save.

This stops citation metrics splitting across “J Pulford” vs “Justin Pulford” profiles.

---

## D) Literature alerts (saved searches)

Needs **Web of Science search access** (often via university library VPN / institutional login). If pure personal login is paywalled, use library access first, then create alerts while that session is open.

1. Sign in → **Documents** / Core Collection search.
2. Open **Advanced Search** (if available).
3. Run one query at a time, then **Create alert** / **Save search** → email frequency weekly.

### Ready-to-paste queries (edit as needed)

**Hubble tension**

```text
TS=("Hubble tension" OR "H0 tension" OR "Hubble constant tension") AND PY=(2020-2026)
```

**DESI BAO / DR2**

```text
TS=(DESI AND (BAO OR "baryon acoustic") AND (DR2 OR "Year 3" OR Y3 OR "Data Release 2")) AND PY=(2023-2026)
```

**Neutrino mass sum (cosmology)**

```text
TS=(("sum of neutrino masses" OR "Sigma m_nu" OR "Σmν" OR "m_nu") AND (cosmology OR CMB OR BAO)) AND PY=(2020-2026)
```

**Optional fourth (BBN / D/H)**

```text
TS=(BBN OR "Big Bang nucleosynthesis") AND TS=("deuterium" OR "D/H" OR "primordial abundance") AND PY=(2018-2026)
```

4. Name alerts clearly, e.g. `PRTOE-H0`, `PRTOE-DESI`, `PRTOE-mnu`.
5. Confirm the alert email is one you read.

---

## Suggested single sitting (~30–45 min)

| Step | Action | Done when |
|---|---|---|
| 1 | ORCID employment + education + name variants (C) | Public profile shows affiliation |
| 2 | ORCID add every DOI you own (A) | Works count > 0 |
| 3 | WoS ORCID **manual sync** | Publications appear or stay empty if unindexed |
| 4 | WoS claim search by name/DOI (B) | No obvious missing Core papers |
| 5 | Create 3 alerts (D) | Email confirmation or alert list shows them |

---

## What I cannot do from here

- Log into ORCID or Web of Science as you  
- Claim papers without DOIs and your confirmation  
- Bypass institutional paywall for Core Collection search  

**Send me:** list of DOIs and/or arXiv IDs (and preferred affiliation string). I will return a paste-ready “click these exact fields” list for A and C.

*Desk process only — not a PRTOE physics claim.*
