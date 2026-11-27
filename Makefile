PYTHON ?= python3
TOPIC ?= agent-memory-2025
TOPIC_NAME ?= Agent Memory 2025+
PAPERS ?= data/$(TOPIC)/papers.json
EDGES ?= data/$(TOPIC)/edges.json
VAULT ?= vault
OUT ?= maps/$(TOPIC)

.PHONY: validate schemas build export evidence-index baseline-timeline venue-audit docs-check check sync clean-cache

validate:
	$(PYTHON) scripts/validate_mem.py --papers $(PAPERS) --edges $(EDGES)

schemas:
	$(PYTHON) -m json.tool schemas/paper.schema.json >/dev/null
	$(PYTHON) -m json.tool schemas/graph.schema.json >/dev/null

build:
	$(PYTHON) scripts/build_research_map.py --papers $(PAPERS) --edges $(EDGES) --vault $(VAULT) --out $(OUT) --topic '$(TOPIC_NAME)'

export:
	$(PYTHON) scripts/export_zotero_formats.py --papers $(PAPERS) --out-dir data/$(TOPIC) --stem $(TOPIC)

evidence-index:
	$(PYTHON) scripts/build_evidence_index.py

baseline-timeline:
	$(PYTHON) scripts/build_baseline_timeline.py

venue-audit:
	$(PYTHON) scripts/build_venue_audit.py --papers $(PAPERS)

docs-check:
	$(PYTHON) scripts/check_docs.py

check: schemas validate build export evidence-index baseline-timeline venue-audit docs-check
	git diff --check

sync:
	git pull --rebase

clean-cache:
	find scripts -type d -name __pycache__ -prune -exec rm -r {} + 2>/dev/null || true
