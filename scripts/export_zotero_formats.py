#!/usr/bin/env python3
"""Export MEM papers.json to BibTeX and RIS for Zotero import."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def bib_escape(s: str) -> str:
    return (s or "").replace("&", r"\&").replace("%", r"\%").replace("#", r"\#")


def bib_key(p: dict) -> str:
    first = (p.get("authors") or ["anon"])[0].split()[-1].lower()
    first = re.sub(r"[^a-z0-9]", "", first) or "anon"
    year = p.get("year") or "0000"
    return f"{first}{year}{p['id']}"


def entry_type(p: dict) -> str:
    v = (p.get("venue_short") or "").lower()
    if "findings" in v or "conference" in v or "neurips" in v or "icml" in v or "iclr" in v or "aaai" in v or "colm" in v or "mlsys" in v or "acl" in v:
        return "inproceedings"
    return "article"


def to_bib(p: dict) -> str:
    fields = [
        ("title", p.get("title")),
        ("author", " and ".join(p.get("authors") or [])),
        ("year", str(p.get("year") or "")),
        ("booktitle", p.get("venue_short")),
        ("doi", p.get("DOI")),
        ("url", p.get("openreview_url") or p.get("pdf_url")),
        ("eprint", p.get("arXiv")),
        ("archivePrefix", "arXiv" if p.get("arXiv") else None),
        ("note", p.get("venue_tier")),
    ]
    body = ",\n".join(f"  {k} = {{{bib_escape(str(v))}}}" for k, v in fields if v)
    return f"@{entry_type(p)}{{{bib_key(p)},\n{body}\n}}\n"


def to_ris(p: dict) -> str:
    lines = ["TY  - CP" if entry_type(p) == "inproceedings" else "TY  - JOUR"]
    lines.append(f"TI  - {p.get('title','')}")
    for a in p.get("authors") or []:
        lines.append(f"AU  - {a}")
    lines.append(f"PY  - {p.get('year','')}")
    lines.append(f"T2  - {p.get('venue_short','')}")
    if p.get("DOI"):
        lines.append(f"DO  - {p['DOI']}")
    if p.get("openreview_url") or p.get("pdf_url"):
        lines.append(f"UR  - {p.get('openreview_url') or p.get('pdf_url')}")
    if p.get("abstract"):
        lines.append(f"AB  - {p['abstract']}")
    lines.append(f"N1  - {p.get('venue_tier','')}")
    lines.append("ER  - ")
    return "\n".join(line.rstrip() for line in lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--stem", default="agent-memory-2025")
    args = ap.parse_args()
    papers = json.loads(Path(args.papers).read_text(encoding="utf-8"))
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{args.stem}.bib").write_text("\n".join(to_bib(p) for p in papers), encoding="utf-8")
    (out / f"{args.stem}.ris").write_text("\n".join(to_ris(p) for p in papers), encoding="utf-8")
    print(f"wrote {out / (args.stem + '.bib')}")
    print(f"wrote {out / (args.stem + '.ris')}")


if __name__ == "__main__":
    main()
