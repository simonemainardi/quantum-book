# 3. Double Slit and Amplitudes

The double-slit experiment is where the physical and mathematical stories meet.

In [Chapter 1](01_physical_principles.md), we introduced it as a physical fact: particles fired one at a time still build an interference pattern. In [Chapter 2](02_math_prerequisites.md), we introduced complex amplitudes, inner products, and squared magnitudes. Now we combine them.

Keep one diagnostic question active throughout the chapter:

```text
Are the alternatives being distinguished, or are they being allowed to meet at the same answer?
```

The soul of this chapter is the learner's apparent contradiction:

> You told me phase can be invisible. But the double slit says phase can make an outcome disappear. Which one is true?

Both are true, and the difference is whether the measurement separates alternatives or recombines them.

## 3.1 Two Questions, Two Bases

**Question.** I see why the double slit has interference, but I am confused by this: sometimes phase seems invisible, and sometimes phase changes probabilities. Which is it?

**Teacher.** It depends on what question you ask the system.

In the double slit there are at least two natural questions:

1. Which slit?
2. Which screen position?

These correspond to different measurement bases.

The which-slit basis is:

```math
|L\rangle
\qquad
|R\rangle
```

The screen-position basis is a set of states:

```math
|x\rangle
```

where $x$ labels a detector position on the screen.

The same physical setup can be interrogated in these different ways. The difference is not cosmetic. It changes whether amplitudes are kept separate or recombined.

![Path basis versus screen basis](../figures/04_path_vs_screen_basis.svg?v=greek-2026-05-27)

## 3.2 Which-Slit Measurement

Assume the two slits are equally illuminated. A simple state after the slits is:

```math
|\psi\rangle =
\frac{|L\rangle + |R\rangle}{\sqrt{2}}
```

If you measure in the which-slit basis, the amplitudes are:

```math
\langle L|\psi\rangle = \frac{1}{\sqrt{2}}
\qquad
\langle R|\psi\rangle = \frac{1}{\sqrt{2}}
```

By the Born rule from [Section 2.12](02_math_prerequisites.md#212-the-born-rule):

```math
P(L) =
\left|\frac{1}{\sqrt{2}}\right|^2
=
\frac{1}{2}
```

and:

```math
P(R) =
\left|\frac{1}{\sqrt{2}}\right|^2
=
\frac{1}{2}
```

There is no interference in this measurement because the alternatives are distinct outcomes. We do not add the left-path amplitude to the right-path amplitude when asking "which slit?"

**Teacher's pause.** This is the first time basis choice becomes physical. The which-slit basis prevents the two alternatives from arriving at the same answer. No shared answer means no amplitude sum, and no amplitude sum means no interference term.

In learner language: the experiment has been forced to answer "left or right?" before the two contributions can cooperate or cancel at the screen.

## 3.3 Screen-Position Measurement

Now ask where the particle lands on the screen.

The amplitude for landing at position $x$ is:

```math
\langle x|\psi\rangle
=
\frac{1}{\sqrt{2}}
\left(
\langle x|L\rangle
+
\langle x|R\rangle
\right)
```

This expression is the crucial difference.

The amplitude for outcome $x$ is a sum of two contributions:

- one contribution from the left slit,
- one contribution from the right slit.

Each contribution is a complex number. In a simplified wave model:

```math
\langle x|L\rangle \propto e^{ikr_L(x)}
```

and:

```math
\langle x|R\rangle \propto e^{ikr_R(x)}
```

Read $e^{ikr}$ as a compact phase clock. The distance $r$ changes how far the arrow has rotated when it reaches the screen. If the two path lengths rotate the arrows into alignment, the spot is bright. If they rotate them into opposition, the spot is dark.

Here:

- $k$ is the wave number,
- $r_L(x)$ is the path length from the left slit to screen position $x$,
- $r_R(x)$ is the path length from the right slit to screen position $x$.

Different path lengths produce different phases.

This is the physical origin of the algebra. The left-path contribution and right-path contribution are not merely two labels. They are wave-like contributions that arrive with different phase angles because the distances are different.

At one screen position, the two arrows line up. At another, they point against each other. The particle still lands as a dot, but the chance of a dot at each position is governed by those arrow sums.

## 3.4 The Cross Term

The screen probability is:

```math
P(x)
=
|\langle x|\psi\rangle|^2
```

Substitute the expression above:

```math
P(x)
=
\frac{1}{2}
\left|
\langle x|L\rangle
+
\langle x|R\rangle
\right|^2
```

Let:

```math
A = \langle x|L\rangle
\qquad
B = \langle x|R\rangle
```

Then:

```math
|A+B|^2
=
|A|^2 + |B|^2 + 2\mathrm{Re}(A^*B)
```

The last term is the interference term.

It can be positive, producing a bright band. It can be negative, producing a dark band. At a dark fringe:

```math
A + B \approx 0
```

so:

```math
P(x) \approx 0
```

This is not probability cancellation. It is amplitude cancellation before probability is computed.

## 3.5 The Student's Confusion, Made Precise

**Question.** Earlier we said phase does not affect probability because $|e^{i\phi}|^2 = 1$. But now phase causes dark and bright fringes. How do both statements coexist?

**Teacher.** Phase does not change the squared magnitude of a single isolated unit amplitude. But phase changes the result of a sum.

Compare:

```math
|e^{i\phi}|^2 = 1
```

No phase dependence.

But:

```math
|1 + e^{i\phi}|^2
```

does depend on $\phi$, because the two terms can point in the same or opposite directions in the complex plane.

In fact:

```math
|1 + e^{i\phi}|^2
=
2 + 2\cos\phi
```

So:

- if $\phi = 0$, the result is $4$,
- if $\phi = \pi$, the result is $0$.

That is exactly the difference between an isolated amplitude and recombined amplitudes.

This is the line that should dissolve the contradiction:

```text
phase is invisible when you square one arrow;
phase is visible when you add arrows and then square.
```

## 3.6 The Same Pattern in a Qubit

The double-slit state:

```math
\frac{|L\rangle + |R\rangle}{\sqrt{2}}
```

has the same structure as:

```math
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
```

Now insert a relative phase:

```math
|\psi\rangle =
\frac{|0\rangle + e^{i\phi}|1\rangle}{\sqrt{2}}
```

If we measure in the Z basis $\{|0\rangle, |1\rangle\}$, the probabilities are:

```math
P(0) = \frac{1}{2}
\qquad
P(1) = \frac{1}{2}
```

regardless of $\phi$.

The phase is invisible in that basis.

But if we measure in the X basis:

```math
|+\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
\qquad
|-\rangle =
\frac{|0\rangle - |1\rangle}{\sqrt{2}}
```

then the amplitude for $+$ is:

```math
\langle +|\psi\rangle
=
\frac{1 + e^{i\phi}}{2}
```

The probability is:

```math
P(+) =
\left|
\frac{1 + e^{i\phi}}{2}
\right|^2
=
\cos^2\frac{\phi}{2}
```

At $\phi = \pi$, this is zero.

That is single-qubit interference.

The notation changed from paths to qubit states, but the emotional point is the same: the phase was not visible when we asked one question, and it became visible when we asked a question that added the components.

This is why the double slit belongs in a practical quantum computing book. It teaches the habit of asking:

> Are these alternatives being kept separate, or are they being recombined before measurement?

That one question will explain many circuit diagrams later.

For a circuit engineer, this is the bridge: a basis state can play the role of a path. A gate can play the role of a recombining optical element. The measurement basis decides which recombination is visible in the final counts.

## 3.7 The Practical Lesson

Quantum computing does not need a literal pair of slits. It needs the same logical structure:

1. Prepare alternatives as amplitudes.
2. Let transformations change their relative phases.
3. Recombine amplitudes with gates.
4. Measure in a basis that reveals the desired interference.

If you skip step 3, phase may remain invisible. If you measure in the wrong basis, you may see flat probabilities even though the state contains useful phase information.

This will be central in [Measurement Bases](05_measurement_bases.md) and [Circuits and Readout](07_circuits_and_readout.md).

## 3.8 A Minimal Numerical Example

Here is the amplitude-only calculation:

```python
import cmath

psi1 = cmath.exp(1j * 0)
psi2 = cmath.exp(1j * cmath.pi)

psi = psi1 + psi2
probability = abs(psi) ** 2

print(psi, probability)
```

The result is:

```text
0j 0.0
```

There were two nonzero contributions. They cancelled because their phases differed by $\pi$.

## 3.9 Summary

The double slit is the physical template for quantum computation:

- which-path measurement separates alternatives and removes interference,
- screen-position measurement recombines alternatives,
- recombination produces cross terms,
- cross terms can be positive or negative,
- phase becomes visible only through a measurement basis or circuit that recombines amplitudes.

The next chapter introduces the qubit as the simplest engineered system that contains this logic.
