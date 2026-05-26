# Quantum Computing for Engineers

This repository contains a standalone textbook page for learning the practical foundations of quantum computing.

Open `index.html` directly in a browser. The page is self-contained except for local assets in this directory.

## Rebuild Figures

From the repository root:

```sh
make quantum-book
```

This regenerates the deterministic SVG textbook figures. The Makefile creates `.venv/` when needed.

## Contents

- `index.html`: the polished textbook page.
- `assets/figures/`: generated SVG figures.
- `scripts/build_quantum_book_assets.py`: standard-library figure generator.
