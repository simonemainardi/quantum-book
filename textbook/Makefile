PYTHON := .venv/bin/python

.PHONY: help venv figures book clean

help:
	@echo "Targets:"
	@echo "  make figures  - create a local venv and regenerate all SVG figures"
	@echo "  make book     - regenerate figures and assemble dist/quantum-computing-practical-textbook.md"
	@echo "  make clean    - remove generated figures and dist outputs"

venv: $(PYTHON)

$(PYTHON):
	python3 -m venv .venv

figures: venv
	$(PYTHON) scripts/build_figures.py

book: figures
	mkdir -p dist
	awk 'FNR == 1 && NR != 1 { print "" } { print }' \
	    book/00_preface.md \
	    book/01_physical_principles.md \
	    book/02_math_prerequisites.md \
	    book/03_double_slit_and_amplitudes.md \
	    book/04_qubits_and_bloch_sphere.md \
	    book/05_measurement_bases.md \
	    book/06_gates_matrices_rotations.md \
	    book/07_circuits_and_readout.md \
	    book/08_practical_examples.md \
	    book/09_worked_labs.md \
	    book/10_glossary.md > dist/quantum-computing-practical-textbook.md

clean:
	rm -rf figures/*.svg dist/*
