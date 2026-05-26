# 6. Gates, Matrices, and Rotations

Quantum gates are transformations of amplitudes. For a single qubit, a gate is a \(2 \times 2\) unitary matrix. On the Bloch sphere, many gates can be understood as rotations.

This chapter connects three languages:

- ket notation,
- matrices,
- geometric rotations.

## 6.1 A Gate Is a Linear Map

From [Section 2.9](02_math_prerequisites.md#29-matrices), a matrix acts on a vector by linear combination.

For a qubit:

$$
|\psi\rangle =
\alpha|0\rangle + \beta|1\rangle
=
\begin{pmatrix}
\alpha \\
\beta
\end{pmatrix}
$$

A gate \(U\) produces:

$$
|\psi'\rangle = U|\psi\rangle
$$

Because \(U\) is linear:

$$
U(\alpha|0\rangle + \beta|1\rangle)
=
\alpha U|0\rangle + \beta U|1\rangle
$$

That is why knowing what a gate does to \(|0\rangle\) and \(|1\rangle\) determines the whole gate.

## 6.2 Building the Matrix from Columns

**Question.** How does a ket rule become a matrix?

**Teacher.** The output of the first basis vector becomes the first column. The output of the second basis vector becomes the second column.

Suppose:

$$
U|0\rangle = a|0\rangle + c|1\rangle
$$

and:

$$
U|1\rangle = b|0\rangle + d|1\rangle
$$

Then:

$$
U =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

![Hadamard matrix columns](../figures/10_hadamard_matrix_columns.svg)

## 6.3 The Hadamard Gate

The Hadamard gate is:

$$
H =
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}
$$

It acts on the computational basis as:

$$
H|0\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
=
|+\rangle
$$

and:

$$
H|1\rangle =
\frac{|0\rangle - |1\rangle}{\sqrt{2}}
=
|-\rangle
$$

It also maps back:

$$
H|+\rangle = |0\rangle
\qquad
H|-\rangle = |1\rangle
$$

This is why applying \(H\) before Z readout implements X-basis measurement.

## 6.4 Hadamard as Recombination

Hadamard is one of the clearest gates for seeing interference.

Apply \(H\) to:

$$
|\psi\rangle =
\alpha|0\rangle + \beta|1\rangle
$$

Using matrix multiplication:

$$
H|\psi\rangle =
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}
\begin{pmatrix}
\alpha \\
\beta
\end{pmatrix}
=
\frac{1}{\sqrt{2}}
\begin{pmatrix}
\alpha + \beta \\
\alpha - \beta
\end{pmatrix}
$$

The new \(|0\rangle\) amplitude is:

$$
\frac{\alpha+\beta}{\sqrt{2}}
$$

The new \(|1\rangle\) amplitude is:

$$
\frac{\alpha-\beta}{\sqrt{2}}
$$

So \(H\) explicitly creates sums and differences of amplitudes. It is a recombination gate.

If \(\alpha = 1/\sqrt{2}\) and \(\beta = -1/\sqrt{2}\), then:

$$
\alpha+\beta = 0
$$

and the \(|0\rangle\) output disappears.

## 6.5 Pauli Gates

The Pauli gates are:

$$
X =
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
$$

$$
Y =
\begin{pmatrix}
0 & -i \\
i & 0
\end{pmatrix}
$$

$$
Z =
\begin{pmatrix}
1 & 0 \\
0 & -1
\end{pmatrix}
$$

Their basic actions are:

$$
X|0\rangle = |1\rangle
\qquad
X|1\rangle = |0\rangle
$$

So \(X\) is the quantum analogue of a bit flip.

The \(Z\) gate leaves \(|0\rangle\) unchanged and flips the sign of \(|1\rangle\):

$$
Z(\alpha|0\rangle + \beta|1\rangle)
=
\alpha|0\rangle - \beta|1\rangle
$$

This is a phase flip. It does not change Z-basis probabilities, but it changes future interference.

The \(Y\) gate combines bit flip and phase factors.

## 6.6 The Phase Gate S

The \(S\) gate is:

$$
S =
\begin{pmatrix}
1 & 0 \\
0 & i
\end{pmatrix}
$$

It acts as:

$$
S(\alpha|0\rangle + \beta|1\rangle)
=
\alpha|0\rangle + i\beta|1\rangle
$$

It adds a relative phase of \(\pi/2\) to the \(|1\rangle\) component.

Its inverse is:

$$
S^\dagger =
\begin{pmatrix}
1 & 0 \\
0 & -i
\end{pmatrix}
$$

The \(S^\dagger\) gate is used when converting Y-basis information into Z-basis readout.

## 6.7 Rotation Gates

Single-qubit rotations are usually written:

$$
R_x(\theta) =
e^{-i\theta X/2}
$$

$$
R_y(\theta) =
e^{-i\theta Y/2}
$$

$$
R_z(\theta) =
e^{-i\theta Z/2}
$$

Their matrices are:

$$
R_x(\theta)
=
\begin{pmatrix}
\cos(\theta/2) & -i\sin(\theta/2) \\
-i\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
$$

$$
R_y(\theta)
=
\begin{pmatrix}
\cos(\theta/2) & -\sin(\theta/2) \\
\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
$$

$$
R_z(\theta)
=
\begin{pmatrix}
e^{-i\theta/2} & 0 \\
0 & e^{i\theta/2}
\end{pmatrix}
$$

These gates rotate the Bloch vector around the X, Y, and Z axes.

## 6.8 Rotations Have Physical Meaning

**Question.** Are these rotations just math, or do they correspond to real hardware controls?

**Teacher.** They correspond to real controls.

In many quantum devices, gates are implemented by applying controlled pulses. The pulse amplitude, duration, phase, and frequency determine the rotation axis and angle in the qubit's state space.

For example:

- a pulse resonant with a superconducting qubit transition can rotate the state around an equatorial axis,
- the phase of the microwave drive changes the rotation axis in the X-Y plane,
- virtual Z rotations can often be implemented by updating a phase reference rather than physically pulsing the qubit.

The Bloch sphere is therefore not just a teaching picture. It is also a control picture.

## 6.9 Unitarity and Probability Conservation

Every ideal gate above is unitary:

$$
U^\dagger U = I
$$

This means:

$$
\|U|\psi\rangle\|^2 =
\||\psi\rangle\|^2
$$

In ordinary language:

> Gates move probability amplitude around, but they do not create or destroy total probability.

Measurement is different. Measurement produces a classical outcome and changes the state in a non-unitary way.

## 6.10 Why Gates Matter for Interference

The double-slit experiment has physical paths and a screen that recombines them.

A quantum circuit has basis states and gates that recombine amplitudes.

The Hadamard gate is the simplest example:

$$
\begin{pmatrix}
\alpha \\
\beta
\end{pmatrix}
\mapsto
\frac{1}{\sqrt{2}}
\begin{pmatrix}
\alpha+\beta \\
\alpha-\beta
\end{pmatrix}
$$

If the phases line up, one output is reinforced. If they oppose, one output is cancelled.

This is the practical circuit version of interference.

## 6.11 Summary

The chapter's key points:

- a gate is a linear map on amplitudes,
- its matrix columns are the images of basis states,
- Hadamard recombines amplitudes by sums and differences,
- Pauli and phase gates manipulate bit value and phase,
- rotation gates implement controlled movement on the Bloch sphere,
- ideal gates are unitary and preserve total probability,
- real hardware gates correspond to physical controls such as pulses and phase references.

Next we put these gates into circuits and connect them to final 0/1 readout.

