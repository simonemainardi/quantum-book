# Quantum Computing for Practical Engineers

## Preface

This book began as a conversation between a curious engineer and a teacher.

The engineer did not ask for a list of quantum facts. The request was more precise and more human:

> I understand math, but I need a recap of the fundamental concepts, such as complex numbers, cosine, and sine. Start from the physical principles of quantum: interference that can cancel while probabilities do not. Then introduce qubits, transformations, and circuits. I want the math needed to describe quantum, and I want real examples behind the technology and its applicability.

That request is the spine of the book.

This book is allowed to be conversational because the conversation is where the understanding lives. A clean formula matters, but the moment before the formula matters too: the moment where something seems contradictory, where the classical intuition protests, where the engineer asks, "What would I actually observe?"

The book should feel like a good lecture where the student keeps asking the right uncomfortable question and the teacher keeps returning to the physical meaning until the algebra stops feeling detached.

## The Contract

Every important idea should pass three tests:

1. **Physical test.** What does this correspond to in an experiment or device?
2. **Algebra test.** What is the exact formula that describes it?
3. **Readout test.** What changes in the measured counts?

If an explanation cannot pass all three tests, it is not yet practical enough for this book.

## The Learner's Hat

Wearing the learner's hat, the important questions are not decorative. They are the engine of the course:

- If probabilities are positive, how can quantum effects cancel?
- If phase does not change $|e^{i\phi}|^2$, how can phase create a dark fringe?
- If a real device only returns 0 or 1, what does it mean to measure in X or Y?
- If two states have the same $P(0)$ and $P(1)$, in what sense are they different?
- How does the elegant ket notation become the concrete $2 \times 2$ matrices used in circuits?
- What is physically happening in real hardware when a "rotation" is applied?

These are the questions of someone who does not want slogans. They want to know where the moving parts are.

## The Teacher's Hat

Wearing the teacher's hat, the job is not to make quantum mechanics sound mystical. The job is to repeat one deep idea in enough representations that it becomes usable:

```text
complex amplitude -> phase -> recombination -> squared magnitude -> observed probability
```

The same idea appears as:

- two paths in the double slit,
- two coordinates in a qubit,
- two arrows in the complex plane,
- two columns in a matrix,
- two branches of a circuit before final readout,
- two experimental count bins after many shots.

Whenever the book returns to the same idea, that is intentional. Quantum intuition is not built by hearing the sentence once. It is built by seeing the same mechanism survive translation from physics to algebra to circuit diagrams to hardware.

The teacher's promise is to avoid hiding behind words like "weird", "mysterious", or "spooky" when a careful amplitude calculation will do. Quantum mechanics is strange, but the strangeness has structure.

## How to Read This Book

Read the chapters in order the first time:

1. [Physical Principles](01_physical_principles.md)
2. [Math and Algebra Prerequisites](02_math_prerequisites.md)
3. [Double Slit and Amplitudes](03_double_slit_and_amplitudes.md)
4. [Qubits and the Bloch Sphere](04_qubits_and_bloch_sphere.md)
5. [Measurement Bases](05_measurement_bases.md)
6. [Gates, Matrices, and Rotations](06_gates_matrices_rotations.md)
7. [Circuits and Readout](07_circuits_and_readout.md)
8. [Practical Examples](08_practical_examples.md)
9. [Worked Labs](09_worked_labs.md)
10. [Glossary](10_glossary.md)

The math chapter is not an appendix. It is the toolkit you will keep reaching for:

- complex numbers explain phase,
- sine and cosine explain rotations,
- Euler's formula connects oscillation with complex amplitudes,
- vectors explain states,
- bases explain questions,
- inner products compute overlaps,
- matrices represent gates,
- unitary transformations preserve total probability,
- the Born rule turns amplitudes into experimental statistics.

## The One Idea to Carry

Do not begin with "a qubit is both 0 and 1." That phrase is too loose to do engineering work.

Begin here instead:

> A quantum computer is a programmable interference machine. It stores complex amplitudes, transforms them with probability-preserving operations, and arranges the final measurement so useful amplitude has been reinforced while unwanted amplitude has been cancelled.

Everything else in the book is a careful unpacking of that sentence.
