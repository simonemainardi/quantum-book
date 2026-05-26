PYTHON ?= .venv/bin/python
WEBARCHIVE ?= /Users/simone/Downloads/Quantum Book.webarchive

.PHONY: help venv quantum-book quantum-assets quantum-extract

help:
	@printf "Targets:\n"
	@printf "  make venv             Create the local Python virtualenv\n"
	@printf "  make quantum-book     Rebuild generated figures\n"
	@printf "  make quantum-assets   Rebuild SVG figures only\n"
	@printf "  make quantum-extract  Re-extract source conversation and archive images\n"

venv:
	python3 -m venv .venv

.venv/bin/python:
	python3 -m venv .venv

quantum-book: quantum-assets

quantum-assets: .venv/bin/python
	$(PYTHON) scripts/build_quantum_book_assets.py --out assets/figures

quantum-extract: .venv/bin/python
	$(PYTHON) scripts/extract_quantum_webarchive.py --webarchive "$(WEBARCHIVE)" --conversation source/conversation.md --images assets/archive
