# 10. Glossary

## Amplitude

A complex number associated with a possible outcome or contribution. Probabilities are computed from squared magnitudes of amplitudes.

## Basis

A set of reference states used to describe or measure a quantum state. For one qubit, important bases are Z, X, and Y.

## Bloch Sphere

A geometric representation of a single-qubit pure state. The coordinates of the Bloch vector are:

```math
(r_x,r_y,r_z)
=
(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)
```

## Born Rule

The rule that turns quantum amplitudes into probabilities:

```math
P(\phi)=|\langle \phi|\psi\rangle|^2
```

For Z-basis qubit measurement:

```math
P(0)=|\alpha|^2
\qquad
P(1)=|\beta|^2
```

## Bra

The conjugate-transpose version of a ket. If:

```math
|\psi\rangle =
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}
```

then:

```math
\langle \psi| =
\begin{pmatrix}
\alpha^* & \beta^*
\end{pmatrix}
```

## Computational Basis

The standard qubit basis:

```math
|0\rangle
\qquad
|1\rangle
```

Also called the Z basis.

## Cross Term

The interference term that appears when squaring a sum:

```math
|A+B|^2
=
|A|^2 + |B|^2 + 2\mathrm{Re}(A^*B)
```

The cross term can be positive or negative.

## Gate

A transformation applied to a quantum state. In ideal single-qubit theory, gates are $2 \times 2$ unitary matrices.

## Global Phase

A phase factor multiplying the whole state:

```math
e^{i\gamma}|\psi\rangle
```

Global phase does not change measurement probabilities.

## Hadamard Gate

The gate:

```math
H =
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1 & 1\\
1 & -1
\end{pmatrix}
```

It maps:

```math
|0\rangle \mapsto |+\rangle
\qquad
|1\rangle \mapsto |-\rangle
```

It also recombines amplitudes by forming sums and differences.

## Inner Product

The overlap amplitude:

```math
\langle \phi|\psi\rangle
```

Its squared magnitude gives the probability of finding $|\psi\rangle$ as $|\phi\rangle$.

## Interference

The effect produced when amplitudes add before probabilities are computed. Interference can be constructive or destructive.

## Ket

A quantum state vector, written:

```math
|\psi\rangle
```

## Measurement

The process that produces a classical outcome from a quantum state. In the ideal model, measurement probabilities are determined by the Born rule.

## Phase

The angle of a complex amplitude. A phase factor is written:

```math
e^{i\phi}
```

Relative phase affects interference.

## Qubit

A two-dimensional quantum state:

```math
|\psi\rangle =
\alpha|0\rangle + \beta|1\rangle
```

with:

```math
|\alpha|^2 + |\beta|^2 = 1
```

## Relative Phase

The phase difference between components of a state. For example:

```math
|0\rangle + e^{i\phi}|1\rangle
```

contains relative phase $\phi$. Relative phase can affect future measurement probabilities after recombination.

## Shot

One execution and measurement of a quantum circuit. Many shots are used to estimate probabilities.

## Superposition

A linear combination of basis states:

```math
\alpha|0\rangle + \beta|1\rangle
```

The word is useful only when remembered together with amplitudes and measurement basis.

## Unitary

A probability-preserving matrix:

```math
U^\dagger U = I
```

Ideal quantum gates are unitary.

## X Basis

The basis:

```math
|+\rangle =
\frac{|0\rangle+|1\rangle}{\sqrt{2}}
\qquad
|-\rangle =
\frac{|0\rangle-|1\rangle}{\sqrt{2}}
```

It reveals the cosine component of relative phase.

## Y Basis

The basis:

```math
|+i\rangle =
\frac{|0\rangle+i|1\rangle}{\sqrt{2}}
\qquad
|-i\rangle =
\frac{|0\rangle-i|1\rangle}{\sqrt{2}}
```

It reveals the sine component of relative phase.

## Z Basis

The computational basis:

```math
|0\rangle
\qquad
|1\rangle
```

It directly reads the component magnitudes $|\alpha|^2$ and $|\beta|^2$.
