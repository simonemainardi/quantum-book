# 8. Practical Examples

The conversation asked for practical perspective, not only formal quantum mechanics. This chapter connects the same amplitude-and-phase ideas to real technology.

The goal is not to survey every quantum technology. The goal is to show how the book's core ideas reappear in practical settings.

## 8.1 The Common Pattern

Across quantum computing, sensing, cryptography, and feature-map style quantum machine learning, the recurring pattern is:

```text
prepare a state
encode information into amplitude or phase
transform/recombine amplitudes
measure statistics
interpret the classical results
```

The physical platform changes. The logic remains.

![Practical quantum technology examples](../figures/12_practical_quantum_technology.svg)

## 8.2 Quantum Algorithms as Engineered Interference

**Question.** When people say a quantum algorithm uses interference, what do they mean concretely?

**Teacher.** They mean the circuit is arranged so that amplitudes leading to useful outputs add constructively, while amplitudes leading to unwanted outputs cancel or become small.

At a high level:

1. Prepare a superposition.
2. Apply operations that encode the problem into phases or signs.
3. Recombine amplitudes with gates.
4. Measure.

The final measurement is still classical. The quantum advantage, when present, comes from how the amplitudes were transformed before that measurement.

The single-qubit circuit:

```text
H -> phase -> H -> measure
```

is the smallest model of this idea. The first \(H\) creates alternatives. The phase operation changes the relative phase. The final \(H\) recombines alternatives so phase becomes a measurable bias.

Larger algorithms use higher-dimensional versions of the same idea.

## 8.3 Quantum Sensing

Quantum sensing is often the most physically intuitive application of phase.

Imagine a qubit prepared in an equal superposition:

$$
|+\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

Suppose the environment causes the \(|1\rangle\) component to acquire a phase:

$$
|\psi\rangle =
\frac{|0\rangle + e^{i\phi}|1\rangle}{\sqrt{2}}
$$

The phase \(\phi\) may depend on a magnetic field, electric field, acceleration, time, or another physical quantity.

Z measurement alone gives:

$$
P(0)=P(1)=\frac{1}{2}
$$

But applying \(H\) before measurement gives:

$$
P(0)=\cos^2\frac{\phi}{2}
$$

So a tiny physical phase shift becomes a measurable change in output frequency.

This is the same structure as [Section 7.5](07_circuits_and_readout.md#75-why-final-rotations-reveal-phase).

## 8.4 Ramsey Interferometry as a Qubit Example

Ramsey interferometry is a standard phase-measurement pattern:

```text
prepare |0>
apply pi/2 pulse
wait while phase accumulates
apply pi/2 pulse
measure
```

In quantum-circuit language, it resembles:

```text
|0> -- H -- phase accumulation -- H -- measure
```

The waiting period lets the qubit acquire a phase relative to the control reference. The second pulse converts that phase into a population difference.

This is not a separate trick from quantum computing. It is the same basis-change logic applied for sensing and calibration.

## 8.5 Superconducting Qubits

In a superconducting qubit, \(|0\rangle\) and \(|1\rangle\) can be two energy levels of an engineered electrical circuit.

The state is still described as:

$$
|\psi\rangle =
\alpha|0\rangle + \beta|1\rangle
$$

Control pulses change \(\alpha\), \(\beta\), and their relative phase. Measurement typically distinguishes the two basis states through a coupled readout resonator.

From the viewpoint of this book:

- pulses implement rotations,
- detuning and phase references affect \(R_z\)-like behavior,
- readout is often Z-like,
- X and Y information is accessed by pre-rotations.

The math in Chapters 4 through 7 is therefore directly connected to laboratory control.

## 8.6 Trapped Ions

In trapped-ion systems, a qubit can be stored in two internal states of an ion.

Laser pulses implement rotations between these states. Measurement may use fluorescence: one state scatters light under the measurement laser, while the other does not.

Again the same structure appears:

- the qubit is a two-level system,
- amplitudes evolve under controlled pulses,
- relative phase matters,
- measurement converts state information into classical data.

The physical hardware is very different from superconducting circuits, but the vector and matrix description is shared.

## 8.7 Photonic Qubits

A photonic qubit can be encoded in polarization:

$$
|H\rangle
\qquad
|V\rangle
$$

or in paths/modes:

$$
|L\rangle
\qquad
|R\rangle
$$

This connects directly to the double-slit discussion.

Optical elements such as beam splitters and phase shifters perform transformations analogous to gates. Detectors then measure output modes.

A beam splitter is an especially physical version of "split and recombine amplitudes." It is the optical cousin of the Hadamard-like operation.

## 8.8 Quantum Cryptography

Quantum cryptography uses measurement disturbance and basis choice.

A simplified intuition:

- A sender prepares states in different bases.
- A receiver measures in selected bases.
- If an eavesdropper measures in the wrong basis, the state is disturbed.
- The disturbance appears as an increased error rate.

The key concept from this book is not the full protocol detail. It is the basis principle:

> Measuring a quantum state is not a passive lookup of a pre-existing classical label. The basis matters.

That is why incompatible bases can expose unwanted measurement.

## 8.9 Quantum Feature Maps

In some quantum machine learning approaches, classical data is encoded into quantum states by rotations or phases.

For example, a feature value \(x\) might determine a rotation:

$$
R_z(x)
$$

or:

$$
R_y(x)
$$

The circuit then entangles, rotates, and measures. The resulting measurement statistics depend on how phases and amplitudes recombine.

This does not mean every such model is automatically useful. It means the mechanism, when used, is the same:

```text
data -> phase/amplitude encoding -> interference -> measured statistics
```

## 8.10 What This Book Does Not Claim

Practical quantum computing is difficult.

Real devices have:

- noise,
- calibration drift,
- finite coherence time,
- imperfect gates,
- readout errors,
- limited connectivity.

The ideal math in this book is the starting model, not the whole engineering stack.

However, without the ideal model, the engineering details have no structure. You need to understand amplitudes, phase, basis, gates, and readout before noise models and error correction can make sense.

## 8.11 Summary

The same ideas reappear across applications:

- Algorithms use gates to arrange constructive and destructive interference.
- Sensors convert physical phase shifts into measurable probability shifts.
- Cryptography uses basis choice and measurement disturbance.
- Hardware control implements rotations of two-level systems.
- Feature maps encode data into phases or amplitudes before measurement.

The unifying question is always:

> What information is stored in amplitude or phase, and what transformation will make it visible in measurement statistics?

