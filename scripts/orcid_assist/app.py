#!/usr/bin/env python3
"""Local ORCID OAuth assistant for Justin Pulford / PRTOE desk.

Security model:
  - Runs only on 127.0.0.1
  - You authorize in the browser (password never shared with Grok/agents)
  - Tokens cached in token.json (gitignored)
  - Default is dry-run; use --apply to write

Usage:
  cp scripts/orcid_assist/.env.example scripts/orcid_assist/.env   # edit secrets
  edit scripts/orcid_assist/profile.yaml
  edit scripts/orcid_assist/works_to_add.yaml                      # add DOIs
  python3 scripts/orcid_assist/app.py                # dry-run plan
  python3 scripts/orcid_assist/app.py --apply        # OAuth + write
  python3 scripts/orcid_assist/app.py --apply --works-only
  python3 scripts/orcid_assist/app.py --status       # show public profile summary

Scopes requested:
  /authenticate /read-limited /activities/update /person/update
"""
from __future__ import annotations

import argparse
import json
import os
import secrets
import sys
import threading
import time
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

try:
    import requests
except ImportError:
    print("Need requests: pip install -r scripts/orcid_assist/requirements.txt", file=sys.stderr)
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("Need PyYAML: pip install -r scripts/orcid_assist/requirements.txt", file=sys.stderr)
    sys.exit(1)

HERE = Path(__file__).resolve().parent
ENV_PATH = HERE / ".env"
TOKEN_PATH = HERE / "token.json"
PROFILE_PATH = HERE / "profile.yaml"
WORKS_PATH = HERE / "works_to_add.yaml"
REPORT_PATH = HERE / "last_run_report.json"

REDIRECT_URI = "http://127.0.0.1:8765/callback"
LISTEN_PORT = 8765

PROD = {
    "auth": "https://orcid.org/oauth/authorize",
    "token": "https://orcid.org/oauth/token",
    "api": "https://api.orcid.org/v3.0",
    "public": "https://pub.orcid.org/v3.0",
}
SANDBOX = {
    "auth": "https://sandbox.orcid.org/oauth/authorize",
    "token": "https://sandbox.orcid.org/oauth/token",
    "api": "https://api.sandbox.orcid.org/v3.0",
    "public": "https://pub.sandbox.orcid.org/v3.0",
}

SCOPES = "/authenticate /read-limited /activities/update /person/update"


def load_env(path: Path = ENV_PATH) -> dict:
    env = {}
    if path.is_file():
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    # also allow real environment override
    for k in ("ORCID_CLIENT_ID", "ORCID_CLIENT_SECRET", "ORCID_ENV", "ORCID_ID"):
        if os.environ.get(k):
            env[k] = os.environ[k]
    return env


def endpoints(env: dict) -> dict:
    return SANDBOX if env.get("ORCID_ENV", "production").lower() == "sandbox" else PROD


def load_yaml(path: Path) -> dict:
    if not path.is_file():
        return {}
    return yaml.safe_load(path.read_text()) or {}


def save_token(tok: dict) -> None:
    TOKEN_PATH.write_text(json.dumps(tok, indent=2) + "\n")
    try:
        os.chmod(TOKEN_PATH, 0o600)
    except OSError:
        pass


def load_token() -> dict | None:
    if not TOKEN_PATH.is_file():
        return None
    try:
        return json.loads(TOKEN_PATH.read_text())
    except json.JSONDecodeError:
        return None


def token_valid(tok: dict | None) -> bool:
    if not tok or not tok.get("access_token"):
        return False
    exp = tok.get("expires_at")
    if exp and time.time() > float(exp) - 60:
        return False
    return True


class _OAuthHandler(BaseHTTPRequestHandler):
    code: str | None = None
    error: str | None = None
    state_expected: str = ""

    def log_message(self, fmt, *args):  # quiet
        return

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path != "/callback":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"not found")
            return
        qs = urllib.parse.parse_qs(parsed.query)
        if qs.get("error"):
            _OAuthHandler.error = qs["error"][0]
            body = b"<html><body><h1>Authorization failed</h1><p>You can close this window.</p></body></html>"
        else:
            state = (qs.get("state") or [""])[0]
            if state != _OAuthHandler.state_expected:
                _OAuthHandler.error = "state_mismatch"
                body = b"<html><body><h1>State mismatch</h1></body></html>"
            else:
                _OAuthHandler.code = (qs.get("code") or [""])[0]
                body = (
                    b"<html><body><h1>ORCID authorized</h1>"
                    b"<p>Return to the terminal. You can close this window.</p></body></html>"
                )
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def oauth_authorize(env: dict, ep: dict) -> dict:
    client_id = env.get("ORCID_CLIENT_ID", "")
    client_secret = env.get("ORCID_CLIENT_SECRET", "")
    if not client_id or not client_secret or "XXXX" in client_id:
        raise SystemExit(
            "Missing ORCID_CLIENT_ID / ORCID_CLIENT_SECRET.\n"
            "1) https://orcid.org/developer-tools  (Public API)\n"
            "2) Redirect URI exactly: http://127.0.0.1:8765/callback\n"
            "3) cp scripts/orcid_assist/.env.example scripts/orcid_assist/.env and edit"
        )

    state = secrets.token_urlsafe(24)
    _OAuthHandler.state_expected = state
    _OAuthHandler.code = None
    _OAuthHandler.error = None

    params = {
        "client_id": client_id,
        "response_type": "code",
        "scope": SCOPES,
        "redirect_uri": REDIRECT_URI,
        "state": state,
    }
    url = ep["auth"] + "?" + urllib.parse.urlencode(params)

    server = HTTPServer(("127.0.0.1", LISTEN_PORT), _OAuthHandler)
    thread = threading.Thread(target=server.handle_request, daemon=True)
    thread.start()
    print("Opening browser for ORCID authorize…")
    print(url)
    try:
        webbrowser.open(url)
    except Exception:
        print("Open the URL above manually.")

    # wait up to 5 minutes
    deadline = time.time() + 300
    while time.time() < deadline:
        if _OAuthHandler.code or _OAuthHandler.error:
            break
        time.sleep(0.2)
    server.server_close()

    if _OAuthHandler.error:
        raise SystemExit(f"OAuth error: {_OAuthHandler.error}")
    if not _OAuthHandler.code:
        raise SystemExit("Timed out waiting for OAuth callback")

    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "authorization_code",
        "code": _OAuthHandler.code,
        "redirect_uri": REDIRECT_URI,
    }
    r = requests.post(
        ep["token"],
        data=data,
        headers={"Accept": "application/json"},
        timeout=60,
    )
    if r.status_code != 200:
        raise SystemExit(f"Token exchange failed {r.status_code}: {r.text[:500]}")
    tok = r.json()
    # expires_in is seconds
    tok["expires_at"] = time.time() + float(tok.get("expires_in", 3600))
    save_token(tok)
    print(f"Authorized as ORCID iD: {tok.get('orcid')}")
    return tok


def api_headers(tok: dict, content: str | None = "application/vnd.orcid+json") -> dict:
    h = {
        "Authorization": f"Bearer {tok['access_token']}",
        "Accept": "application/vnd.orcid+json",
    }
    if content:
        h["Content-Type"] = content
    return h


def fetch_crossref(doi: str) -> dict | None:
    doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "").strip()
    r = requests.get(
        f"https://api.crossref.org/works/{urllib.parse.quote(doi)}",
        headers={"User-Agent": "prtoe-orcid-assist/1.0 (mailto:local@localhost)"},
        timeout=30,
    )
    if r.status_code != 200:
        return None
    msg = r.json().get("message") or {}
    title = (msg.get("title") or [""])[0]
    year = None
    for key in ("published-print", "published-online", "created"):
        parts = (msg.get(key) or {}).get("date-parts") or []
        if parts and parts[0]:
            year = parts[0][0]
            break
    journal = (msg.get("container-title") or [""])[0]
    return {
        "doi": doi,
        "title": title,
        "year": year,
        "journal": journal,
        "type": "journal-article",
    }


def work_xml(work: dict) -> str:
    """Minimal ORCID work XML for Member/Public API create."""
    title = (work.get("title") or "Untitled").replace("&", "&amp;").replace("<", "&lt;")
    wtype = work.get("type") or "journal-article"
    # ORCID work-type vocabulary subset
    type_map = {
        "journal-article": "journal-article",
        "preprint": "preprint",
        "other": "other",
        "book": "book",
        "book-chapter": "book-chapter",
        "conference-paper": "conference-paper",
    }
    wtype = type_map.get(wtype, "other")
    year = work.get("year")
    journal = work.get("journal")
    doi = work.get("doi")
    arxiv = work.get("arxiv")
    url = work.get("url")

    ext = []
    if doi:
        d = doi.replace("https://doi.org/", "")
        ext.append(
            f"""<common:external-id>
  <common:external-id-type>doi</common:external-id-type>
  <common:external-id-value>{d}</common:external-id-value>
  <common:external-id-url>https://doi.org/{d}</common:external-id-url>
  <common:external-id-relationship>self</common:external-id-relationship>
</common:external-id>"""
        )
    if arxiv:
        a = str(arxiv).replace("arXiv:", "").replace("arxiv:", "").strip()
        ext.append(
            f"""<common:external-id>
  <common:external-id-type>arxiv</common:external-id-type>
  <common:external-id-value>{a}</common:external-id-value>
  <common:external-id-url>https://arxiv.org/abs/{a}</common:external-id-url>
  <common:external-id-relationship>self</common:external-id-relationship>
</common:external-id>"""
        )
    if url and not doi and not arxiv:
        ext.append(
            f"""<common:external-id>
  <common:external-id-type>uri</common:external-id-type>
  <common:external-id-value>{url}</common:external-id-value>
  <common:external-id-url>{url}</common:external-id-url>
  <common:external-id-relationship>self</common:external-id-relationship>
</common:external-id>"""
        )

    journal_xml = ""
    if journal:
        j = str(journal).replace("&", "&amp;").replace("<", "&lt;")
        journal_xml = f"<work:journal-title>{j}</work:journal-title>"

    year_xml = ""
    if year:
        year_xml = f"""<common:publication-date>
  <common:year>{int(year)}</common:year>
</common:publication-date>"""

    ext_block = ""
    if ext:
        ext_block = "<common:external-ids>\n" + "\n".join(ext) + "\n</common:external-ids>"

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<work:work xmlns:common="http://www.orcid.org/ns/common"
           xmlns:work="http://www.orcid.org/ns/work">
  <work:title>
    <common:title>{title}</common:title>
  </work:title>
  {journal_xml}
  <work:type>{wtype}</work:type>
  {year_xml}
  {ext_block}
</work:work>
"""


def employment_xml(emp: dict) -> str:
    org = (emp.get("organization") or "Unknown").replace("&", "&amp;")
    city = (emp.get("city") or "Unknown").replace("&", "&amp;")
    region = emp.get("region") or ""
    country = (emp.get("country") or "US")[:2].upper()
    role = emp.get("role_title") or ""
    dept = emp.get("department") or ""
    start = emp.get("start_year")
    end = emp.get("end_year")
    ror = emp.get("ror_id")

    disambig = ""
    if ror:
        disambig = f"""<common:disambiguated-organization>
  <common:disambiguated-organization-identifier>{ror}</common:disambiguated-organization-identifier>
  <common:disambiguation-source>ROR</common:disambiguation-source>
</common:disambiguated-organization>"""

    region_xml = f"<common:region>{region}</common:region>" if region else ""
    role_xml = f"<employment:role-title>{role}</employment:role-title>" if role else ""
    dept_xml = f"<employment:department-name>{dept}</employment:department-name>" if dept else ""
    start_xml = ""
    if start:
        start_xml = f"""<common:start-date>
  <common:year>{int(start)}</common:year>
</common:start-date>"""
    end_xml = ""
    if end:
        end_xml = f"""<common:end-date>
  <common:year>{int(end)}</common:year>
</common:end-date>"""

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<employment:employment xmlns:common="http://www.orcid.org/ns/common"
                       xmlns:employment="http://www.orcid.org/ns/employment">
  {role_xml}
  {dept_xml}
  <employment:organization>
    <common:name>{org}</common:name>
    <common:address>
      <common:city>{city}</common:city>
      {region_xml}
      <common:country>{country}</common:country>
    </common:address>
    {disambig}
  </employment:organization>
  {start_xml}
  {end_xml}
</employment:employment>
"""


def post_xml(ep: dict, tok: dict, orcid: str, path: str, xml: str) -> tuple[int, str]:
    url = f"{ep['api']}/{orcid}/{path}"
    r = requests.post(
        url,
        data=xml.encode("utf-8"),
        headers=api_headers(tok, "application/vnd.orcid+xml"),
        timeout=60,
    )
    loc = r.headers.get("Location", "")
    return r.status_code, loc or r.text[:300]


def put_keyword(ep: dict, tok: dict, orcid: str, keyword: str) -> int:
    # keywords: create via POST activities-style person keywords
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<keyword:keyword xmlns:keyword="http://www.orcid.org/ns/keyword"
                 xmlns:common="http://www.orcid.org/ns/common">
  <keyword:content>{keyword}</keyword:content>
</keyword:keyword>
"""
    url = f"{ep['api']}/{orcid}/keywords"
    r = requests.post(
        url,
        data=xml.encode("utf-8"),
        headers=api_headers(tok, "application/vnd.orcid+xml"),
        timeout=60,
    )
    return r.status_code


def put_other_name(ep: dict, tok: dict, orcid: str, name: str) -> int:
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<other-name:other-name xmlns:other-name="http://www.orcid.org/ns/other-name"
                       xmlns:common="http://www.orcid.org/ns/common">
  <other-name:content>{name}</other-name:content>
</other-name:other-name>
"""
    url = f"{ep['api']}/{orcid}/other-names"
    r = requests.post(
        url,
        data=xml.encode("utf-8"),
        headers=api_headers(tok, "application/vnd.orcid+xml"),
        timeout=60,
    )
    return r.status_code


def put_url(ep: dict, tok: dict, orcid: str, name: str, url_val: str) -> int:
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<researcher-url:researcher-url xmlns:researcher-url="http://www.orcid.org/ns/researcher-url"
                               xmlns:common="http://www.orcid.org/ns/common">
  <researcher-url:url-name>{name}</researcher-url:url-name>
  <researcher-url:url>{url_val}</researcher-url:url>
</researcher-url:researcher-url>
"""
    url = f"{ep['api']}/{orcid}/researcher-urls"
    r = requests.post(
        url,
        data=xml.encode("utf-8"),
        headers=api_headers(tok, "application/vnd.orcid+xml"),
        timeout=60,
    )
    return r.status_code


def resolve_works(works_cfg: list) -> list[dict]:
    out = []
    for w in works_cfg or []:
        item = dict(w)
        if item.get("doi") and not item.get("title"):
            meta = fetch_crossref(item["doi"])
            if meta:
                item.update({k: v for k, v in meta.items() if v and not item.get(k)})
                print(f"  Crossref: {item.get('title')}")
            else:
                print(f"  WARNING: Crossref miss for DOI {item['doi']}")
        if not item.get("title") and item.get("arxiv"):
            item["title"] = f"arXiv:{item['arxiv']}"
        if not item.get("title"):
            print(f"  SKIP work without title: {item}")
            continue
        out.append(item)
    return out


def plan(profile: dict, works: list[dict]) -> dict:
    return {
        "orcid_id": profile.get("orcid_id"),
        "employment": profile.get("employment"),
        "educations": profile.get("educations") or [],
        "keywords": profile.get("keywords") or [],
        "other_names": profile.get("other_names") or [],
        "urls": profile.get("urls") or [],
        "works": [
            {"title": w.get("title"), "doi": w.get("doi"), "arxiv": w.get("arxiv"), "year": w.get("year")}
            for w in works
        ],
    }


def public_status(orcid: str, ep: dict) -> dict:
    h = {"Accept": "application/json"}
    out = {"orcid": orcid}
    for path, key in (
        ("works", "works"),
        ("employments", "employments"),
        ("keywords", "keywords"),
        ("other-names", "other_names"),
        ("researcher-urls", "urls"),
        ("external-identifiers", "external_ids"),
    ):
        r = requests.get(f"{ep['public']}/{orcid}/{path}", headers=h, timeout=30)
        out[key] = {"http": r.status_code}
        if r.status_code == 200:
            try:
                out[key]["body"] = r.json()
            except Exception:
                out[key]["raw"] = r.text[:200]
    # summarize
    works = out.get("works", {}).get("body") or {}
    groups = works.get("group") or []
    out["summary"] = {
        "work_groups": len(groups),
        "employment_groups": len(
            ((out.get("employments") or {}).get("body") or {}).get("affiliation-group") or []
        ),
    }
    return out


def apply_all(env: dict, ep: dict, tok: dict, profile: dict, works: list[dict], works_only: bool) -> dict:
    orcid = tok.get("orcid") or env.get("ORCID_ID") or profile.get("orcid_id")
    if not orcid:
        raise SystemExit("No ORCID iD in token or config")
    report = {"orcid": orcid, "actions": []}

    if not works_only:
        emp = profile.get("employment") or {}
        if emp.get("organization"):
            code, detail = post_xml(ep, tok, orcid, "employment", employment_xml(emp))
            report["actions"].append({"employment": emp.get("organization"), "http": code, "detail": detail})
            print(f"employment → HTTP {code}")
        for edu in profile.get("educations") or []:
            # reuse employment xml shape with education namespace via simple swap
            xml = employment_xml(edu).replace("employment:", "education:").replace(
                "xmlns:employment", "xmlns:education"
            ).replace("/employment\"", "/education\"")
            # fix root tags
            xml = xml.replace("<employment:employment", "<education:education").replace(
                "</employment:employment>", "</education:education>"
            )
            code, detail = post_xml(ep, tok, orcid, "education", xml)
            report["actions"].append({"education": edu.get("organization"), "http": code, "detail": detail})
            print(f"education {edu.get('organization')} → HTTP {code}")
        for kw in profile.get("keywords") or []:
            code = put_keyword(ep, tok, orcid, kw)
            report["actions"].append({"keyword": kw, "http": code})
            print(f"keyword {kw!r} → HTTP {code}")
        for name in profile.get("other_names") or []:
            code = put_other_name(ep, tok, orcid, name)
            report["actions"].append({"other_name": name, "http": code})
            print(f"other-name {name!r} → HTTP {code}")
        for u in profile.get("urls") or []:
            code = put_url(ep, tok, orcid, u.get("name") or "url", u.get("url") or "")
            report["actions"].append({"url": u, "http": code})
            print(f"url {u} → HTTP {code}")

    for w in works:
        xml = work_xml(w)
        code, detail = post_xml(ep, tok, orcid, "work", xml)
        report["actions"].append({"work": w.get("title"), "http": code, "detail": detail})
        print(f"work {w.get('title')!r} → HTTP {code}")

    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n")
    return report


def main():
    ap = argparse.ArgumentParser(description="Local ORCID OAuth assist")
    ap.add_argument("--apply", action="store_true", help="OAuth (if needed) and write to ORCID")
    ap.add_argument("--works-only", action="store_true", help="Only add works (skip profile)")
    ap.add_argument("--reauth", action="store_true", help="Force new OAuth even if token cached")
    ap.add_argument("--status", action="store_true", help="Public profile summary only")
    ap.add_argument("--dry-run", action="store_true", help="Force dry-run (default without --apply)")
    args = ap.parse_args()

    env = load_env()
    ep = endpoints(env)
    profile = load_yaml(PROFILE_PATH)
    works_cfg = load_yaml(WORKS_PATH).get("works") or []

    if args.status:
        oid = env.get("ORCID_ID") or profile.get("orcid_id") or "0009-0003-8018-9869"
        st = public_status(oid, ep)
        print(json.dumps({"summary": st.get("summary"), "orcid": oid}, indent=2))
        # external ids
        ext = ((st.get("external_ids") or {}).get("body") or {}).get("external-identifier") or []
        for e in ext:
            print(
                "external:",
                e.get("external-id-type"),
                e.get("external-id-value"),
                e.get("external-id-url", {}).get("value"),
            )
        return

    print("Resolving works metadata…")
    works = resolve_works(works_cfg)
    p = plan(profile, works)
    print("\n=== PLAN ===")
    print(json.dumps(p, indent=2))
    if not works and not (profile.get("employment") or {}).get("organization"):
        print(
            "\nNothing substantial to write yet.\n"
            f"  Edit {WORKS_PATH} (DOIs)\n"
            f"  Edit {PROFILE_PATH} (affiliation)\n"
            "Then re-run with --apply."
        )

    if not args.apply or args.dry_run:
        print("\nDry-run only. When ready:")
        print("  1) Fill .env from .env.example (ORCID developer-tools client)")
        print("  2) Edit profile.yaml + works_to_add.yaml")
        print("  3) python3 scripts/orcid_assist/app.py --apply")
        print("  4) Web of Science → ORCID Syncing → Manual sync")
        return

    tok = None if args.reauth else load_token()
    if not token_valid(tok):
        tok = oauth_authorize(env, ep)
    else:
        print(f"Using cached token for ORCID {tok.get('orcid')}")

    report = apply_all(env, ep, tok, profile, works, args.works_only)
    print("\n=== REPORT ===")
    print(json.dumps(report, indent=2))
    print(f"\nWrote {REPORT_PATH}")
    print(
        "\nNext (Web of Science — 30 seconds, must be you):\n"
        "  1) https://www.webofscience.com → sign in\n"
        "  2) Researcher Profile → Edit → ORCID Syncing\n"
        "  3) Manual sync: ORCID → Web of Science\n"
        "  4) Optional: claim any Core Collection hits by name/DOI\n"
        "  5) Optional: create saved-search alerts (see WEB_OF_SCIENCE_NEXT_STEPS.md)\n"
    )


if __name__ == "__main__":
    main()
