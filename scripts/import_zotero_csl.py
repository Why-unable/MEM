#!/usr/bin/env python3
"""Convert a Zotero CSL JSON export into a MEM review CSV.

This is intentionally a review step, not an automatic merge into papers.json.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def first_author(item: dict) -> str:
    authors = item.get("author") or []
    if not authors:
        return ""
    a = authors[0]
    return " ".join(x for x in [a.get("given"), a.get("family")] if x)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Zotero CSL JSON export")
    ap.add_argument("--out", required=True, help="CSV review output")
    args = ap.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = [data]
    fields = ["title", "year", "venue", "authors", "DOI", "URL", "type", "zotero_key"]
    with Path(args.out).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for item in data:
            issued = item.get("issued", {}).get("date-parts", [[None]])[0][0]
            authors = item.get("author") or []
            w.writerow({
                "title": item.get("title", ""),
                "year": issued or "",
                "venue": item.get("container-title", ""),
                "authors": "; ".join(" ".join(x for x in [a.get("given"), a.get("family")] if x) for a in authors),
                "DOI": item.get("DOI", ""),
                "URL": item.get("URL", ""),
                "type": item.get("type", ""),
                "zotero_key": item.get("id", ""),
            })
    print(f"wrote {args.out} ({len(data)} items)")


if __name__ == "__main__":
    main()
