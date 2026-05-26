# Quantum Computing for Practical Engineers

## Preface

This book is written for an engineer who wants to understand quantum computing from the inside, not as a list of mystical slogans and not as a pile of formalism detached from physical meaning.

The original learning goal was precise:

> I understand math, but I need a recap of the fundamental concepts, such as complex numbers, cosine, and sine. Start from the physical principles of quantum: interference that can cancel while probabilities do not. Then introduce qubits, transformations, and circuits. I want the math needed to describe quantum, and I want real examples behind the technology and its applicability.

So the book follows that route.

It does not begin with "a qubit is both 0 and 1." That phrase is too loose to be useful. Instead, it begins with the physical fact that quantum systems do not add probabilities first. They add **amplitudes** first. Those amplitudes can have signs and phases. They can reinforce or cancel. Only after measurement do we square magnitudes and obtain probabilities.

That single difference explains why:

- a double-slit experiment has dark fringes,
- a qubit can have an invisible phase,
- a basis change can make that phase visible,
- a quantum circuit is mostly a way of arranging interference before readout,
- real devices often measure only one native basis, then use rotations to expose the information we want.

## How to Read This Book

The chapters are meant to be read in order at least once:

1. [Physical Principles](book/01_physical_principles.md)
2. [Math and Algebra Prerequisites](book/02_math_prerequisites.md)
3. [Double Slit and Amplitudes](book/03_double_slit_and_amplitudes.md)
4. [Qubits and the Bloch Sphere](book/04_qubits_and_bloch_sphere.md)
5. [Measurement Bases](book/05_measurement_bases.md)
6. [Gates, Matrices, and Rotations](book/06_gates_matrices_rotations.md)
7. [Circuits and Readout](book/07_circuits_and_readout.md)
8. [Practical Examples](book/08_practical_examples.md)
9. [Worked Labs](book/09_worked_labs.md)
10. [Glossary](book/10_glossary.md)

The math chapter is not an appendix to ignore. It is a toolkit. Later chapters refer back to it whenever a concept is reused:

- complex numbers and phases,
- Euler's formula,
- vectors and bases,
- inner products,
- matrices,
- unitary transformations,
- the Born rule.

## The Style of the Book

The book keeps the rhythm of a good tutorial conversation. Many sections begin with a question in the voice of the learner, followed by a teacher's answer. This is deliberate. The goal is not only to state the correct equations, but to resolve the conceptual pressure points that came up in the original discussion:

- If phase does not affect ordinary probability, how can it create interference?
- If all measurements return classical 0/1 bits, why talk about measuring in X or Y?
- If a qubit has the same `P(0)` and `P(1)`, how can it still be a different state?
- How does a ket become a column vector?
- How does a gate become a matrix?
- What does "measurement is choosing an axis" mean physically?

## Reproducible Figures

Every chart and diagram used by the chapters is generated locally.

Run:

```bash
make figures
```

The figure generator uses only the Python standard library and writes SVG files into `figures/`.

To assemble all chapters into one Markdown file:

```bash
make book
```

The assembled output appears at:

```text
dist/quantum-computing-practical-textbook.md
```

## One Sentence Summary

A quantum computer is a programmable interference machine: it stores complex amplitudes, transforms them with unitary operations, and arranges the final measurement so useful amplitude has been reinforced while unwanted amplitude has been cancelled.

