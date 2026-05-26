# Quantum Computing for Practical Engineers

This package is a Markdown textbook built from the learning path in the original conversation. It keeps the focus on the questions that drove the discussion:

- Why can quantum effects cancel while probabilities cannot?
- How does the double-slit experiment connect to qubits?
- When does phase become measurable probability?
- Why do different measurement bases reveal different information?
- How do gates, matrices, rotations, circuits, and readout fit together?

## Structure

- `book/*.md` contains the textbook chapters.
- `figures/*.svg` contains generated figures referenced by the chapters.
- `scripts/build_figures.py` regenerates all figures using only the Python standard library.
- `Makefile` creates a local virtual environment and rebuilds the figures.

## Rebuild

```bash
make figures
make book
```

`make book` also assembles a single Markdown file at:

```text
dist/quantum-computing-practical-textbook.md
```

No external datasets or network downloads are required.
