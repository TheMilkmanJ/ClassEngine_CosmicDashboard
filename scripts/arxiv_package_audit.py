#!/usr/bin/env python3
"""
Audit every papers/*/ folder for arXiv packaging hygiene.

For each package directory under papers/:
  - list tarball contents (papers/<name>/<name>.tar.gz or any *.tar.gz)
  - grep PRTOE in *.tex
  - grep note= in refs.bib
  - grep bibinfo note in *.bbl
  - report page count if main.pdf exists

Prints a markdown table to stdout and writes
docs/working_logs/_PACKAGE_AUDIT.md.

Usage:
  python3 scripts/arxiv_package_audit.py
  python3 scripts/arxiv_package_audit.py --root /path/to/repo
"""

from __future__ import annotations

import argparse
import re
import subprocess
import tarfile
from datetime import date
from pathlib import Path


NOTE_EQ_RE = re.compile(r"\bnote\s*=", re.IGNORECASE)
BIBINFO_NOTE_RE = re.compile(r"\\bibinfo\s*\{\s*note\s*\}", re.IGNORECASE)
PAGES_PDFINFO_RE = re.compile(r"^Pages:\s*(\d+)\s*$", re.MULTILINE)
PAGES_LOG_RE = re.compile(
    r"Output written on\s+\S+\s+\((\d+)\s+pages?", re.IGNORECASE
)


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parent.parent


def package_dirs(papers: Path) -> list[Path]:
    return sorted(p for p in papers.iterdir() if p.is_dir() and not p.name.startswith("."))


def find_tarball(pkg: Path) -> Path | None:
    preferred = pkg / f"{pkg.name}.tar.gz"
    if preferred.is_file():
        return preferred
    tars = sorted(pkg.glob("*.tar.gz"))
    return tars[0] if tars else None


def tar_contents(tar_path: Path | None) -> list[str]:
    if tar_path is None:
        return []
    try:
        with tarfile.open(tar_path, "r:gz") as tf:
            names = [m.name for m in tf.getmembers() if m.name not in (".", "./")]
            # Prefer files over directory-only entries for the summary.
            files = [n for n in names if not n.endswith("/")]
            return sorted(files) if files else sorted(names)
    except (tarfile.TarError, OSError) as exc:
        return [f"<error reading tarball: {exc}>"]


def count_hits(paths: list[Path], pattern: re.Pattern[str]) -> list[str]:
    hits: list[str] = []
    for path in paths:
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            hits.append(f"{path.name}: <read error: {exc}>")
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if pattern.search(line):
                hits.append(f"{path.name}:{i}")
    return hits


def grep_prtoe(pkg: Path) -> list[str]:
    tex_files = sorted(pkg.rglob("*.tex"))
    hits: list[str] = []
    for path in tex_files:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = path.relative_to(pkg).as_posix()
        for i, line in enumerate(text.splitlines(), 1):
            if "PRTOE" in line:
                hits.append(f"{rel}:{i}")
    return hits


def grep_note_eq(pkg: Path) -> list[str]:
    bib = pkg / "refs.bib"
    if not bib.is_file():
        return []
    return count_hits([bib], NOTE_EQ_RE)


def grep_bibinfo_note(pkg: Path) -> list[str]:
    bbls = sorted(pkg.rglob("*.bbl"))
    hits: list[str] = []
    for path in bbls:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = path.relative_to(pkg).as_posix()
        for i, line in enumerate(text.splitlines(), 1):
            if BIBINFO_NOTE_RE.search(line):
                hits.append(f"{rel}:{i}")
    return hits


def pdf_page_count(pdf: Path) -> str | None:
    if not pdf.is_file():
        return None
    try:
        proc = subprocess.run(
            ["pdfinfo", str(pdf)],
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
        if proc.returncode == 0:
            m = PAGES_PDFINFO_RE.search(proc.stdout)
            if m:
                return m.group(1)
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        pass

    log = pdf.with_suffix(".log")
    if log.is_file():
        try:
            text = log.read_text(encoding="utf-8", errors="replace")
            m = PAGES_LOG_RE.search(text)
            if m:
                return m.group(1) + " (from log)"
        except OSError:
            pass
    return "?"


def fmt_list(items: list[str], empty: str = "none") -> str:
    if not items:
        return empty
    # Keep table cells short.
    if len(items) <= 4:
        return ", ".join(items)
    return f"{len(items)} hits: " + ", ".join(items[:3]) + ", …"


def audit_package(pkg: Path) -> dict:
    tar = find_tarball(pkg)
    contents = tar_contents(tar)
    prtoe = grep_prtoe(pkg)
    notes = grep_note_eq(pkg)
    bibinfo = grep_bibinfo_note(pkg)
    pages = pdf_page_count(pkg / "main.pdf")
    has_tex = (pkg / "main.tex").is_file() or (pkg / "submission" / "main.tex").is_file()
    has_pdf = (pkg / "main.pdf").is_file()
    return {
        "name": pkg.name,
        "tar": tar.name if tar else "—",
        "tar_contents": contents,
        "tar_cell": fmt_list(contents, empty="— (no tarball)"),
        "prtoe": prtoe,
        "prtoe_cell": fmt_list(prtoe),
        "note_eq": notes,
        "note_cell": fmt_list(notes) if (pkg / "refs.bib").is_file() else "n/a (no refs.bib)",
        "bibinfo": bibinfo,
        "bibinfo_cell": fmt_list(bibinfo) if list(pkg.rglob("*.bbl")) else "n/a (no .bbl)",
        "pages": pages if pages is not None else "— (no main.pdf)",
        "has_tex": has_tex,
        "has_pdf": has_pdf,
        "path": pkg,
    }


def render_markdown(rows: list[dict], root: Path) -> str:
    today = date.today().isoformat()
    lines: list[str] = [
        f"# Package audit — `papers/*/` ({today})",
        "",
        f"Generated by `scripts/arxiv_package_audit.py` from repo root `{root}`.",
        "",
        "Checks per package folder:",
        "",
        "- **tar contents** — members of `*.tar.gz` (prefer `<name>.tar.gz`)",
        "- **PRTOE in tex** — any `PRTOE` substring under `*.tex`",
        "- **`note=` in refs.bib** — live BibTeX note fields (apsrev typesets them)",
        "- **`\\bibinfo{note}` in bbl** — shipped note leakage",
        "- **pages** — `pdfinfo` on `main.pdf` (falls back to `main.log`)",
        "",
        "## Summary table",
        "",
        "| package | pages | tarball | tar contents | PRTOE in tex | `note=` in refs.bib | `\\bibinfo{note}` in bbl |",
        "|---|---:|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| `{r['name']}` | {r['pages']} | `{r['tar']}` | {r['tar_cell']} "
            f"| {r['prtoe_cell']} | {r['note_cell']} | {r['bibinfo_cell']} |"
        )

    lines += ["", "## Per-package detail", ""]
    for r in rows:
        lines.append(f"### `{r['name']}`")
        lines.append("")
        lines.append(f"- path: `papers/{r['name']}/`")
        lines.append(f"- main.tex present: **{'yes' if r['has_tex'] else 'no'}**")
        lines.append(f"- main.pdf pages: **{r['pages']}**")
        lines.append(f"- tarball: `{r['tar']}`")
        if r["tar_contents"]:
            lines.append("- tar members:")
            for m in r["tar_contents"]:
                lines.append(f"  - `{m}`")
        else:
            lines.append("- tar members: *(none / missing)*")
        lines.append(
            f"- PRTOE in tex: {fmt_list(r['prtoe']) if r['prtoe'] else '**none**'}"
        )
        if (r["path"] / "refs.bib").is_file():
            lines.append(
                f"- `note=` in refs.bib: {fmt_list(r['note_eq']) if r['note_eq'] else '**none**'}"
            )
        else:
            lines.append("- `note=` in refs.bib: n/a (no refs.bib)")
        bbls = list(r["path"].rglob("*.bbl"))
        if bbls:
            lines.append(
                f"- `\\bibinfo{{note}}` in bbl: "
                f"{fmt_list(r['bibinfo']) if r['bibinfo'] else '**none**'}"
            )
        else:
            lines.append("- `\\bibinfo{note}` in bbl: n/a (no .bbl)")
        lines.append("")

    # Pass/fail rollup for shippable packages (have tex + tar).
    shippable = [r for r in rows if r["has_tex"]]
    clean = [
        r
        for r in shippable
        if not r["prtoe"] and not r["note_eq"] and not r["bibinfo"] and r["tar"] != "—"
    ]
    lines += [
        "## Hygiene rollup",
        "",
        f"- package folders scanned: **{len(rows)}**",
        f"- with main.tex (or submission/main.tex): **{len(shippable)}**",
        f"- clean for PRTOE / note-field / tarball presence: **{len(clean)}** / {len(shippable)}",
        "",
    ]
    dirty = [r for r in shippable if r not in clean]
    if dirty:
        lines.append("Flags:")
        for r in dirty:
            flags = []
            if r["tar"] == "—":
                flags.append("missing tarball")
            if r["prtoe"]:
                flags.append(f"PRTOE×{len(r['prtoe'])}")
            if r["note_eq"]:
                flags.append(f"note=×{len(r['note_eq'])}")
            if r["bibinfo"]:
                flags.append(f"bibinfo note×{len(r['bibinfo'])}")
            lines.append(f"- `{r['name']}`: {', '.join(flags) if flags else 'other'}")
        lines.append("")
    else:
        lines.append("All TeX packages pass PRTOE / note-field greps and have a tarball.")
        lines.append("")

    lines.append(f"*End of audit ({today}).*")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repo root (default: parent of scripts/)",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output markdown path (default: docs/working_logs/_PACKAGE_AUDIT.md)",
    )
    args = ap.parse_args()
    root = (args.root or repo_root_from_script()).resolve()
    papers = root / "papers"
    if not papers.is_dir():
        print(f"error: papers/ not found under {root}", flush=True)
        return 1

    rows = [audit_package(p) for p in package_dirs(papers)]
    md = render_markdown(rows, root)

    out = args.out or (root / "docs" / "working_logs" / "_PACKAGE_AUDIT.md")
    out = out.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")

    print(md, end="")
    print(f"\nWrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
