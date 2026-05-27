# 1. Physical Principles

## 1.1 The Engineer's Starting Point

**Question.** I know how classical systems behave. A bit is 0 or 1. A probability is a positive number. Why does quantum computing need a different language?

**Teacher.** Because the thing that evolves in quantum mechanics is not a probability. It is an amplitude.

In a classical model, if two mutually exclusive ways lead to an event, probabilities add:

```math
P = P_1 + P_2
```

Since probabilities are nonnegative real numbers, they cannot cancel.

In a quantum model, each alternative contributes a complex amplitude:

```math
\psi = \psi_1 + \psi_2
```

Only after adding amplitudes do we compute probability:

```math
P = |\psi|^2
```

That order matters. If

```math
\psi_1 = 1
\qquad
\psi_2 = -1
```

then

```math
\psi = \psi_1 + \psi_2 = 0
\qquad
P = |\psi|^2 = 0
```

Two possible contributions produced an impossible outcome.

That is the first structural difference between classical and quantum reasoning.

![Amplitudes versus probabilities](../figures/01_amplitudes_vs_probabilities.svg?v=greek-2026-05-27)

## 1.2 The Core Rule

Quantum theory has many formalisms, but for this book we begin with the rule that carries most of the intuition:

1. A quantum system has a state.
2. The state contains complex amplitudes.
3. Evolution changes amplitudes smoothly and reversibly, as long as we are not measuring.
4. Measurement converts amplitudes into probabilities.
5. After measurement, the result is classical.

The engineering version is:

> Design transformations so the amplitude of useful outcomes is large and the amplitude of unwanted outcomes is small.

This is why the earlier website phrase "programmable interference machine" is still correct, but it was not enough. To understand it, we must unpack what interference means physically and algebraically.

## 1.3 Probabilities Do Not Interfere; Amplitudes Do

**Question.** If probabilities cannot cancel, but quantum effects can cancel, where is the cancellation hiding?

**Teacher.** It is hiding before probability exists.

The cancellation is not:

```math
P_1 + P_2 = 0
```

That would be impossible if both probabilities are positive.

The cancellation is:

```math
\psi_1 + \psi_2 = 0
```

Then probability is computed afterward:

```math
P = |\psi_1 + \psi_2|^2 = 0
```

This distinction is the key to the rest of the book. Later, in [Math and Algebra Prerequisites](02_math_prerequisites.md), we will make precise what complex amplitudes and magnitudes mean. For now, keep the physical sequence in mind:

```text
alternatives -> amplitudes -> add amplitudes -> square magnitude -> probability
```

## 1.4 The Double-Slit Experiment

The double-slit experiment is the cleanest physical example.

Imagine firing photons or electrons one at a time toward a barrier with two slits, then recording where each particle lands on a screen.

Classically, you might expect:

- some particles go through the left slit,
- some particles go through the right slit,
- the screen pattern is the sum of two single-slit patterns.

Quantum mechanically, with no which-slit measurement, the screen shows interference fringes:

- bright bands where amplitudes reinforce,
- dark bands where amplitudes cancel,
- a statistical pattern built from many single detection events.

The striking point is that each particle is detected as one localized event, but the probability distribution of many such events is shaped by amplitude interference.

![Double slit interference](../figures/02_double_slit_interference.svg?v=greek-2026-05-27)

## 1.5 What the Double Slit Teaches

The double-slit experiment teaches four lessons that reappear inside quantum computing.

First, a quantum state is not simply ignorance about a classical trajectory. If the particle really had a definite slit path and we merely did not know it, we would add probabilities. But the observed dark fringes require amplitude cancellation.

Second, alternatives can interfere only when they are not distinguished by measurement. If a detector tells us which slit the particle used, the interference pattern disappears. The alternatives become classical alternatives, and probabilities add.

Third, phase matters. The left-path and right-path contributions arrive at a given screen position with phases determined by path length. At some positions the phases line up; at others they are opposite.

Fourth, measurement basis matters. Asking "which slit?" and asking "which screen position?" are different questions. They correspond to different ways of extracting classical information from the same quantum state.

That fourth lesson is the bridge to qubits.

## 1.6 From Double Slit to Qubits

**Question.** What does a double slit have to do with a qubit?

**Teacher.** A two-path system is already qubit-like.

Use two basis states:

```math
|L\rangle = \text{the left path}
\qquad
|R\rangle = \text{the right path}
```

If the illumination is balanced, the state just after the slits can be approximated by:

```math
|\psi\rangle =
\frac{|L\rangle + |R\rangle}{\sqrt{2}}
```

That is the same mathematical pattern as a qubit in a superposition:

```math
|\psi\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
```

The labels are different, but the structure is the same: two basis alternatives, each with an amplitude.

This is why the double slit is not just a historical curiosity. It is the physical prototype for the amplitude logic used by qubits and circuits.

## 1.7 The Measurement Problem We Actually Need

For this book, we do not need to solve every philosophical question about quantum measurement. We need the operational rule used by quantum engineering:

Before measurement:

```math
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle
```

At measurement in the computational basis:

```math
P(0) = |\alpha|^2
\qquad
P(1) = |\beta|^2
```

After measurement, the device reports one classical result, either 0 or 1.

The phase information that existed in the quantum state is generally destroyed by that readout. That is why useful quantum programs delay measurement until the end, after gates have arranged the amplitudes.

## 1.8 Practical Engineering Relevance

The same physical principle drives multiple quantum technologies.

In quantum algorithms, gates arrange interference so that wrong answers cancel and right answers become more likely. The details differ by algorithm, but the broad mechanism is amplitude steering.

In quantum sensing, a tiny physical effect can change phase. A carefully designed measurement then converts that phase shift into a probability shift. This is why quantum sensors can be extremely sensitive to fields, forces, time, or acceleration.

In quantum cryptography, measurement disturbance matters. If an eavesdropper measures a quantum signal in the wrong basis, the disturbance can be detected statistically.

In quantum machine learning feature maps, classical data may be encoded into phases and rotations. The later circuit then recombines those amplitudes, making phase relationships observable in measurement statistics.

![Practical quantum technology examples](../figures/12_practical_quantum_technology.svg?v=greek-2026-05-27)

## 1.9 What Comes Next

The physical story gives us the target:

> Understand how amplitudes, phase, basis, and measurement interact.

The next chapter builds the math needed to say that precisely. It covers complex numbers, sine and cosine, Euler's formula, vectors, inner products, matrices, and unitary transformations.

Do not treat that chapter as detached algebra. Every piece will be used again:

- complex numbers explain phase,
- vectors explain states,
- bases explain what a measurement is asking,
- inner products compute amplitudes,
- matrices represent gates,
- unitaries preserve total probability.
