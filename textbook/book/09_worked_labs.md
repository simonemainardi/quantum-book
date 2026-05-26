# 9. Worked Labs

This chapter gives small calculations you can reproduce without a quantum SDK. The point is to make the algebra tangible.

The examples use ordinary Python complex numbers and matrix multiplication.

## 9.1 Lab 1: Perfect Amplitude Cancellation

Compute:

$$
\psi_1 = e^{i0},
\qquad
\psi_2 = e^{i\pi}.
$$

Since:

$$
e^{i0}=1,
\qquad
e^{i\pi}=-1,
$$

we have:

$$
\psi_1+\psi_2 = 0.
$$

Python:

```python
import cmath

psi1 = cmath.exp(1j * 0)
psi2 = cmath.exp(1j * cmath.pi)

psi = psi1 + psi2
probability = abs(psi) ** 2

print(psi)
print(probability)
```

Expected result:

```text
approximately 0j
approximately 0.0
```

The small numerical residue you may see comes from floating-point precision.

## 9.2 Lab 2: Phase Invisible in Z

Consider:

$$
|\psi\rangle =
\frac{|0\rangle + e^{i\phi}|1\rangle}{\sqrt{2}}.
$$

The amplitudes are:

$$
\alpha = \frac{1}{\sqrt{2}},
\qquad
\beta = \frac{e^{i\phi}}{\sqrt{2}}.
$$

Z-basis probabilities:

$$
P(0) = |\alpha|^2 = \frac{1}{2},
$$

$$
P(1) = |\beta|^2 = \frac{1}{2}.
$$

Python:

```python
import cmath
import math

for phi in [0, math.pi / 2, math.pi, 3 * math.pi / 2]:
    alpha = 1 / math.sqrt(2)
    beta = cmath.exp(1j * phi) / math.sqrt(2)
    print(phi, abs(alpha) ** 2, abs(beta) ** 2)
```

Every line gives the same probabilities.

## 9.3 Lab 3: Phase Visible in X

For the same state:

$$
|\psi\rangle =
\frac{|0\rangle + e^{i\phi}|1\rangle}{\sqrt{2}},
$$

the X-basis \(+\) amplitude is:

$$
\langle +|\psi\rangle
=
\frac{1 + e^{i\phi}}{2}.
$$

So:

$$
P(+) =
\left|
\frac{1 + e^{i\phi}}{2}
\right|^2.
$$

Python:

```python
import cmath
import math

for phi in [0, math.pi / 2, math.pi, 3 * math.pi / 2]:
    amp_plus = (1 + cmath.exp(1j * phi)) / 2
    p_plus = abs(amp_plus) ** 2
    print(phi, p_plus)
```

Expected pattern:

```text
phi = 0       -> P(+) = 1
phi = pi/2    -> P(+) = 1/2
phi = pi      -> P(+) = 0
phi = 3pi/2   -> P(+) = 1/2
```

This is the single-qubit analogue of bright and dark fringes.

## 9.4 Lab 4: Theta 60 Degrees in Z, X, and Y

Use:

$$
|\psi(\theta,\phi)\rangle =
\cos\frac{\theta}{2}|0\rangle
+
e^{i\phi}\sin\frac{\theta}{2}|1\rangle,
$$

with:

$$
\theta = 60^\circ.
$$

The Bloch components are:

$$
r_x = \sin\theta\cos\phi,
$$

$$
r_y = \sin\theta\sin\phi,
$$

$$
r_z = \cos\theta.
$$

Python:

```python
import math

theta = math.radians(60)

for phi in [0, math.pi / 2, math.pi, 3 * math.pi / 2]:
    rx = math.sin(theta) * math.cos(phi)
    ry = math.sin(theta) * math.sin(phi)
    rz = math.cos(theta)

    p_z0 = (1 + rz) / 2
    p_xp = (1 + rx) / 2
    p_yp = (1 + ry) / 2

    print(phi, "P(Z=0)", p_z0, "P(X=+)", p_xp, "P(Y=+i)", p_yp)
```

Interpretation:

- \(P(Z=0)\) stays at 0.75.
- \(P(X=+)\) changes with \(\cos\phi\).
- \(P(Y=+i)\) changes with \(\sin\phi\).

This is exactly the plot generated in:

```text
figures/08_zxy_measurement_probabilities.svg
```

## 9.5 Lab 5: Hadamard as a Matrix

Use:

$$
H =
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}.
$$

Python:

```python
import math

def matvec(M, v):
    return [
        M[0][0] * v[0] + M[0][1] * v[1],
        M[1][0] * v[0] + M[1][1] * v[1],
    ]

s = 1 / math.sqrt(2)
H = [
    [s, s],
    [s, -s],
]

zero = [1, 0]
one = [0, 1]

print("H|0> =", matvec(H, zero))
print("H|1> =", matvec(H, one))
```

Expected:

```text
H|0> = [1/sqrt(2), 1/sqrt(2)]
H|1> = [1/sqrt(2), -1/sqrt(2)]
```

Those are \(|+\rangle\) and \(|-\rangle\).

## 9.6 Lab 6: H-Z-H Interference

Start with \(|0\rangle\).

Apply:

```text
H -> Z -> H
```

Python:

```python
import math

def matvec(M, v):
    return [
        M[0][0] * v[0] + M[0][1] * v[1],
        M[1][0] * v[0] + M[1][1] * v[1],
    ]

s = 1 / math.sqrt(2)

H = [
    [s, s],
    [s, -s],
]

Z = [
    [1, 0],
    [0, -1],
]

state = [1, 0]
state = matvec(H, state)
state = matvec(Z, state)
state = matvec(H, state)

print(state)
print("P(0) =", abs(state[0]) ** 2)
print("P(1) =", abs(state[1]) ** 2)
```

Expected:

```text
state = [0, 1]
P(0) = 0
P(1) = 1
```

The middle \(Z\) gate only changed phase in the computational basis. The final \(H\) converted that phase change into a bit flip.

This is the practical point of the whole book in one toy circuit.

## 9.7 Lab 7: Rebuild the Figures

From the package root:

```bash
make figures
```

This regenerates the SVGs in `figures/`.

The script uses only standard Python:

```text
scripts/build_figures.py
```

To assemble the book:

```bash
make book
```

The assembled Markdown is:

```text
dist/quantum-computing-practical-textbook.md
```

## 9.8 Exercises

1. For the state

   $$
   |\psi\rangle =
   \frac{|0\rangle - |1\rangle}{\sqrt{2}},
   $$

   compute \(P(0)\), \(P(1)\), \(P(+)\), and \(P(-)\).

2. For

   $$
   |\psi\rangle =
   \frac{|0\rangle + i|1\rangle}{\sqrt{2}},
   $$

   compute \(P(+i)\) and \(P(-i)\).

3. Show that \(H^2 = I\).

4. Show that \(Z|+\rangle = |-\rangle\).

5. Use Python to plot \(P(X=+)\) as a function of \(\phi\) for:

   $$
   |\psi\rangle =
   \cos\frac{\theta}{2}|0\rangle
   +
   e^{i\phi}\sin\frac{\theta}{2}|1\rangle
   $$

   with \(\theta = 30^\circ\), \(60^\circ\), and \(90^\circ\).

## 9.9 Answers in Brief

1. For \(|-\rangle\), Z gives \(1/2,1/2\), and X gives \(P(+)=0\), \(P(-)=1\).
2. For \(|+i\rangle\), Y gives \(P(+i)=1\), \(P(-i)=0\).
3. \(H^2=I\) by direct matrix multiplication.
4. \(Z|+\rangle=(|0\rangle-|1\rangle)/\sqrt{2}=|-\rangle\).
5. Increasing \(\theta\) increases the swing in X-basis probability, because the swing amplitude is \(\sin\theta\).

