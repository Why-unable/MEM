#!/usr/bin/env python3
"""Validate MEM paper and edge data before building a research map."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

REQUIRED = {"id", "title", "year", "venue_short", "venue_tier", "category", "priority", "role_zh", "authors", "abstract", "openreview_url", "pdf_url", "status"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers", required=True)
    ap.add_argument("--edges", required=True)
    args = ap.parse_args()
    papers = json.loads(Path(args.papers).read_text(encoding="utf-8"))
    edges = json.loads(Path(args.edges).read_text(encoding="utf-8"))
    errors = []
    warnings = []
    ids = Counter(p.get("id") for p in papers)
    for pid, n in ids.items():
        if n > 1:
            errors.append(f"duplicate id: {pid} ({n})")
    titles = Counter(p.get("title", "").strip().lower() for p in papers)
    for title, n in titles.items():
        if n > 1:
            warnings.append(f"duplicate title: {title} ({n})")
    for p in papers:
        missing = REQUIRED - set(p)
        if missing:
            errors.append(f"{p.get('id','?')}: missing {sorted(missing)}")
        if not (2025 <= int(p.get("year", 0)) <= 2026):
            warnings.append(f"{p.get('id')}: year outside 2025-2026: {p.get('year')}")
        if p.get("status") != "published":
            warnings.append(f"{p.get('id')}: status is {p.get('status')}")
        if not p.get("DOI") and not p.get("arXiv") and not p.get("openreview_url"):
            warnings.append(f"{p.get('id')}: no DOI/arXiv/OpenReview identifier")
    known = {p.get("id") for p in papers}
    for e in edges:
        if e.get("from") not in known or e.get("to") not in known:
            errors.append(f"unknown edge endpoint: {e}")
        if not e.get("type"):
            errors.append(f"edge missing type: {e}")
    print(f"papers: {len(papers)}")
    print(f"edges: {len(edges)}")
    print("venue tiers:", dict(Counter(p.get("venue_tier") for p in papers)))
    print("categories:", dict(Counter(p.get("category") for p in papers)))
    if warnings:
        print("\nWARNINGS")
        for w in warnings:
            print(" -", w)
    if errors:
        print("\nERRORS")
        for e in errors:
            print(" -", e)
        raise SystemExit(1)
    print("\nOK")


if __name__ == "__main__":
    main()
