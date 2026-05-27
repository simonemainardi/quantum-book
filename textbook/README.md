# Quantum Computing for Practical Engineers

This package is a Markdown textbook built from the learning path in the original conversation between a curious engineer and a quantum teacher.

The book is organized as chapters in `book/*.md`, with reproducible SVG figures in `figures/*.svg`.

## Structure

- `book/README.md` is the book-facing preface that GitHub renders when opening the chapter folder.
- `book/01_physical_principles.md` through `book/10_glossary.md` contain the textbook chapters.
- `figures/*.svg` contains generated figures referenced by the chapters.
- `scripts/build_figures.py` regenerates all figures using only the Python standard library.
- `dist/quantum-computing-practical-textbook.md` is the assembled single-file Markdown version.

## Rebuild

```bash
make figures
make book
```

`make figures` creates a local `.venv/` if needed and regenerates the SVGs. `make book` also assembles:

```text
dist/quantum-computing-practical-textbook.md
```

No external datasets or network downloads are required.
