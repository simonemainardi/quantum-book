PYTHON ?= .venv/bin/python

.PHONY: help venv quantum-book quantum-assets

help:
	@printf "Targets:\n"
	@printf "  make venv             Create the local Python virtualenv\n"
	@printf "  make quantum-book     Rebuild generated figures\n"
	@printf "  make quantum-assets   Rebuild SVG figures only\n"

venv:
	python3 -m venv .venv

.venv/bin/python:
	python3 -m venv .venv

quantum-book: quantum-assets

quantum-assets: .venv/bin/python
	$(PYTHON) scripts/build_quantum_book_assets.py --out assets/figures

