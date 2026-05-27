# 7. Circuits and Readout

A quantum circuit is a sequence of operations applied to quantum states, followed by measurement. The useful part of the circuit usually happens before measurement, while amplitudes are still free to interfere.

This chapter connects the earlier ideas:

- amplitudes,
- basis changes,
- gates,
- rotations,
- final readout.

The learner's question here was direct: if everything ends as 0 or 1, why did we spend so much effort on phase and basis? The answer is that the final 0/1 counts are the readout of an interference process that happened before the measurement.

## 7.1 The Circuit Pattern

Most introductory single-qubit circuits follow this structure:

```text
prepare -> transform -> maybe change basis -> measure
```

In equations:

```math
|\psi_{\text{out}}\rangle =
U_n \cdots U_2 U_1 |\psi_{\text{in}}\rangle
```

Then measurement converts the final amplitudes into classical outcome probabilities.

The order matters. Measurement too early destroys the phase relationships that later gates would have used.

If you want a practical rule of thumb:

```text
unitary gates keep the calculation quantum;
measurement cashes it out into classical data.
```

Once you cash it out, the later part of the circuit is no longer manipulating the same coherent amplitudes.

## 7.2 Native Z Readout

Many real devices naturally measure something equivalent to the Z basis:

```math
\{|0\rangle, |1\rangle\}
```

This gives:

```math
P(0) = |\alpha|^2
\qquad
P(1) = |\beta|^2
```

But a state can contain information in phase, which Z readout may not see.

So the practical strategy is:

> Rotate the state so the desired information becomes Z-basis population, then perform native readout.

![Rotation before readout](../figures/11_rotation_before_readout.svg?v=greek-2026-05-27)

## 7.3 Measuring X Using H Then Z

The X basis is:

```math
|+\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
\qquad
|-\rangle =
\frac{|0\rangle - |1\rangle}{\sqrt{2}}
```

Hadamard maps:

```math
H|+\rangle = |0\rangle
\qquad
H|-\rangle = |1\rangle
```

Therefore, to measure in X:

1. Apply $H$.
2. Measure in Z.

The probability of observing 0 after the $H$ gate equals the original probability of $X=+$.

This is not a trick. It is how a circuit asks the X-basis question using a Z-basis detector.

In hardware language, the detector may be fixed, but the pre-measurement rotation changes what the detector's 0 and 1 mean.

## 7.4 Measuring Y Using $S^\dagger$, H, Then Z

The Y basis is:

```math
|+i\rangle =
\frac{|0\rangle + i|1\rangle}{\sqrt{2}}
\qquad
|-i\rangle =
\frac{|0\rangle - i|1\rangle}{\sqrt{2}}
```

To measure in Y, one common circuit is:

1. Apply $S^\dagger$.
2. Apply $H$.
3. Measure in Z.

The $S^\dagger$ removes the $i$-phase relationship, and $H$ converts the resulting X-like basis into Z readout.

Operationally:

```text
Y basis -> S dagger -> X basis -> H -> Z basis
```

## 7.5 Why Final Rotations Reveal Phase

**Question.** If the hardware always gives 0 or 1, what is the point of saying phase was measured?

**Teacher.** Phase is not read directly as a label on the screen. It is converted into a probability bias.

For:

```math
|\psi\rangle =
\frac{|0\rangle + e^{i\phi}|1\rangle}{\sqrt{2}}
```

Z measurement gives:

```math
P(0) = P(1) = \frac{1}{2}
```

No phase dependence.

Apply $H$ first:

```math
H|\psi\rangle =
\frac{1}{2}
\left[
(1+e^{i\phi})|0\rangle
+
(1-e^{i\phi})|1\rangle
\right]
```

Now:

```math
P(0) =
\left|
\frac{1+e^{i\phi}}{2}
\right|^2
=
\cos^2\frac{\phi}{2}
```

The final bit still says 0 or 1. But the frequency of 0 across many repetitions depends on the phase.

That is the circuit version of the double-slit screen.

**Learner's checkpoint.** The phase was never printed directly. It changed the probability distribution after the final recombination. In the lab, that means phase becomes a difference in counts.

## 7.6 Shots and Statistics

A quantum measurement is sampled. A single run gives one outcome. To estimate probabilities, repeat the same circuit many times.

Each repetition is often called a shot.

If the true probability is:

```math
P(0) = 0.75
```

then 1000 shots might produce approximately:

```text
0: 750 counts
1: 250 counts
```

with statistical fluctuation.

This is why quantum programming outputs histograms and expectation values, not hidden amplitudes directly.

## 7.7 Expectation Values

For a single qubit, the expectation values of Pauli observables are connected to the Bloch vector:

```math
\langle Z\rangle = r_z
```

```math
\langle X\rangle = r_x
```

```math
\langle Y\rangle = r_y
```

The measurement probabilities are:

```math
P(Z=0)=\frac{1+\langle Z\rangle}{2}
\qquad
P(Z=1)=\frac{1-\langle Z\rangle}{2}
```

Similarly:

```math
P(X=+)=\frac{1+\langle X\rangle}{2}
```

and:

```math
P(Y=+i)=\frac{1+\langle Y\rangle}{2}
```

This is why measuring along different axes reconstructs different components of the state.

## 7.8 A Minimal Interference Circuit

Start with:

```math
|0\rangle
```

Apply $H$:

```math
H|0\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
=
|+\rangle
```

Apply $Z$:

```math
Z|+\rangle =
\frac{|0\rangle - |1\rangle}{\sqrt{2}}
=
|-\rangle
```

Apply $H$ again:

```math
H|-\rangle = |1\rangle
```

So the circuit:

```text
|0> -- H -- Z -- H -- measure
```

returns 1 with probability 1.

But if the middle $Z$ were absent:

```text
|0> -- H -- H -- measure
```

then:

```math
H H |0\rangle = |0\rangle
```

so the circuit returns 0 with probability 1.

The only difference is a phase flip in the middle. That phase flip becomes a deterministic output change after recombination by the final $H$.

This is a small quantum algorithm in miniature.

It is worth feeling how strange and practical that is. The middle operation did not change the immediate Z probabilities of the superposition, yet it changed the final answer from certainly 0 to certainly 1 after recombination.

## 7.9 Circuit as an Interferometer

The circuit:

```text
H -> phase -> H -> measurement
```

is analogous to an interferometer:

1. First $H$: split amplitude into alternatives.
2. Phase operation: change the relative phase.
3. Second $H$: recombine alternatives.
4. Measurement: sample the result.

The double slit has physical paths. The circuit has basis-state paths. The mathematics is the same: relative phase becomes observable only after recombination.

## 7.10 Practical Readout in Real Hardware

In superconducting devices, readout can be implemented by coupling the qubit to a resonator. The resonator response depends on the qubit state, and classical electronics infer whether the qubit was closer to $|0\rangle$ or $|1\rangle$.

In trapped-ion devices, state-dependent fluorescence can distinguish internal states.

In photonic devices, detectors count photons in output modes or polarizations.

The details differ, but the operational pattern is shared:

```text
quantum amplitudes -> controlled transformations -> measurement statistics
```

## 7.11 Summary

Key points:

- circuits transform amplitudes before measurement,
- many devices naturally perform Z-like readout,
- measuring X or Y can be implemented by rotating first,
- phase becomes a classical probability bias only after recombination,
- repeated shots estimate probabilities,
- a simple $H$-phase-$H$ circuit is the circuit analogue of an interferometer.
