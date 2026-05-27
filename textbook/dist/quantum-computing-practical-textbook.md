# Quantum Computing for Practical Engineers

## Preface

This book began as a conversation between a curious engineer and a teacher.

The engineer did not ask for a list of quantum facts. The request was more precise and more human:

> I understand math, but I need a recap of the fundamental concepts, such as complex numbers, cosine, and sine. Start from the physical principles of quantum: interference that can cancel while probabilities do not. Then introduce qubits, transformations, and circuits. I want the math needed to describe quantum, and I want real examples behind the technology and its applicability.

That request is the spine of the book.

This book is allowed to be conversational because the conversation is where the understanding lives. A clean formula matters, but the moment before the formula matters too: the moment where something seems contradictory, where the classical intuition protests, where the engineer asks, "What would I actually observe?"

The book should feel like a good lecture where the student keeps asking the right uncomfortable question and the teacher keeps returning to the physical meaning until the algebra stops feeling detached.

It is also a book about keeping two truths in view at the same time:

- before measurement, the useful object is an amplitude, which behaves like a directed arrow;
- after measurement, the only thing you see is classical data, built from repeated counts.

Much of the difficulty of quantum computing is learning not to collapse those two truths into one vague sentence. The book keeps them separate on purpose.

## The Contract

Every important idea should pass three tests:

1. **Physical test.** What does this correspond to in an experiment or device?
2. **Algebra test.** What is the exact formula that describes it?
3. **Readout test.** What changes in the measured counts?

If an explanation cannot pass all three tests, it is not yet practical enough for this book.

Beside every formula, keep asking:

- What are the alternatives or basis states?
- Which amplitudes are being kept separate?
- Which amplitudes are being recombined?
- What would change in the final histogram?

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

At the start, do not worry if "complex amplitude" is not yet formal. The first picture is simpler: an amplitude is an arrow-like contribution, and probability is the squared length of the final arrow after the relevant contributions have been added.

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

The first read should be linear. Later, the book becomes a map: when a chapter says "phase", return to complex numbers and Euler's formula; when it says "basis", return to vectors and inner products; when it says "readout", return to the Born rule and shots.

## The One Idea to Carry

Do not begin with "a qubit is both 0 and 1." That phrase is too loose to do engineering work.

Begin here instead:

> A quantum computer is a programmable interference machine. It stores complex amplitudes, transforms them with probability-preserving operations, and arranges the final measurement so useful amplitude has been reinforced while unwanted amplitude has been cancelled.

Everything else in the book is a careful unpacking of that sentence.

# 1. Physical Principles

## 1.0 Conversation Thread

The original learner did not begin by asking for a definition of a qubit. The first pressure point was more basic:

> Probabilities do not cancel. But quantum interference can cancel. What, exactly, is cancelling?

This chapter keeps that question in front of us. The aim is not to decorate classical probability with quantum vocabulary. The aim is to identify the new object that quantum theory asks us to track before measurement: the complex amplitude.

The word "complex" will become precise in [Chapter 2](02_math_prerequisites.md). For now, use a physical picture: an amplitude is like an arrow contribution. It has a size and a direction. Directions can line up, oppose, or sit at angles. That is why amplitudes can cancel while probabilities cannot.

If you have seen phasors in signals or AC circuits, the feeling is similar: you do not only keep a strength; you also keep a phase. The detector will not show you the phasor directly, but the phasor determines what survives when contributions are combined.

## 1.1 The Engineer's Starting Point

**Question.** I know how classical systems behave. A bit is 0 or 1. A probability is a positive number. Why does quantum computing need a different language?

**Teacher.** Because the thing that evolves in quantum mechanics is not a probability. It is an amplitude.

In a classical model, if two mutually exclusive ways lead to an event, probabilities add:

```math
P = P_1 + P_2
```

Since probabilities are nonnegative real numbers, they cannot cancel.

Before writing the quantum formula, pause on the word **amplitude**.

For the first pass through the idea, think:

```text
amplitude = arrow-like contribution
```

The arrow's length says how strong the contribution is. The arrow's direction is its phase. A complex number is the algebraic way to store that arrow on a plane.

Probability is not the arrow itself. Probability is obtained after the relevant arrows have been added:

```text
probability = squared length of the final arrow
```

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

Read the next figure from left to right. The left side is already in probability-land, so the bars only add upward. The right side is still in amplitude-land, so direction matters before the final probability is computed.

![Amplitudes versus probabilities](../figures/01_amplitudes_vs_probabilities.svg?v=greek-2026-05-27)

## 1.2 The Core Rule

Quantum theory has many formalisms, but for this book we begin with the rule that carries most of the intuition:

1. A quantum system has a state.
2. The state contains amplitudes: arrow-like quantities with size and phase.
3. Evolution changes amplitudes smoothly and reversibly, as long as we are not measuring.
4. Measurement converts amplitudes into probabilities.
5. After measurement, the result is classical.

The engineering version is:

> Design transformations so the amplitude of useful outcomes is large and the amplitude of unwanted outcomes is small.

This is why the phrase "programmable interference machine" is correct, but it is not enough by itself. It only becomes useful when you can say what is interfering, when it is allowed to interfere, and how the final measurement turns that interference into ordinary counts.

**Teacher's pause.** A probability is what you can estimate after repeated measurements. An amplitude is the bookkeeping object that evolves before measurement. Mixing those two levels is the fastest way to become confused.

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

If you are wearing the engineer's hat, read that line as a signal chain. Before measurement, the system carries complex-valued signals. The circuit or physical setup combines them. The detector sees only the squared magnitude of the result.

That is why quantum mechanics feels slippery at first: the thing we manipulate is not the thing we finally observe.

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

Do not picture a tiny classical pellet secretly choosing a slit while a separate wave draws the pattern. The operational statement is more careful: when the experiment does not record which slit was taken, the model assigns amplitudes to the alternatives and combines them before predicting the screen probabilities.

So the experiment has two layers at once:

- one run gives one dot on the screen,
- many runs reveal a wave-like pattern of probabilities.

This is exactly the rhythm of quantum computing later: one circuit shot returns one bit string, but many shots reveal the probability pattern created by the amplitudes.

![Double slit interference](../figures/02_double_slit_interference.svg?v=greek-2026-05-27)

## 1.5 What the Double Slit Teaches

The double-slit experiment teaches four lessons that reappear inside quantum computing.

First, a quantum state is not simply ignorance about a classical trajectory. If the particle really had a definite slit path and we merely did not know it, we would add probabilities. But the observed dark fringes require amplitude cancellation.

Second, alternatives can interfere only when they are not distinguished by measurement. If a detector tells us which slit the particle used, the interference pattern disappears. The alternatives become classical alternatives, and probabilities add.

Third, phase matters. The left-path and right-path contributions arrive at a given screen position with phases determined by path length. At some positions the phases line up; at others they are opposite.

Fourth, measurement basis matters. Asking "which slit?" and asking "which screen position?" are different questions. They correspond to different ways of extracting classical information from the same quantum state.

Here "basis" just means the set of answers a measurement is prepared to distinguish. The which-slit basis has answers "left" and "right." The screen-position basis has answers "this pixel", "that pixel", and so on.

That fourth lesson is the bridge to qubits.

**Learner's checkpoint.** If the pattern changes when you ask "which slit?", the particle was not simply carrying a hidden classical answer that you uncovered. The experimental question changed the quantum situation.

## 1.6 From Double Slit to Qubits

**Question.** What does a double slit have to do with a qubit?

**Teacher.** A two-path system is already qubit-like.

Use two basis states:

```math
|L\rangle = \text{the left path}
\qquad
|R\rangle = \text{the right path}
```

For now, a basis state simply means one clean alternative in the description we have chosen. Here the alternatives are the two paths. Later, for a qubit, the alternatives will be $|0\rangle$ and $|1\rangle$.

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

The rest of the book is essentially this move repeated with more control: replace the two literal slits by two engineered basis states, replace the screen by a chosen measurement, and replace fixed path lengths by gates you can program.

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

This is not because measurement is morally bad or philosophically forbidden. It is because measurement turns the amplitude-level calculation into a classical sample. Once that happens, the later gates no longer have phase relationships to use.

So the practical question is never simply "what is the qubit?" It is:

```text
what amplitude information is still alive, and what will the next operation do with it?
```

## 1.8 Practical Engineering Relevance

The same physical principle drives multiple quantum technologies.

In quantum algorithms, gates arrange interference so that wrong answers cancel and right answers become more likely. The details differ by algorithm, but the broad mechanism is amplitude steering.

In quantum sensing, a tiny physical effect can change phase. A carefully designed measurement then converts that phase shift into a probability shift. This is why quantum sensors can be extremely sensitive to fields, forces, time, or acceleration.

In quantum cryptography, measurement disturbance matters. If an eavesdropper measures a quantum signal in the wrong basis, the disturbance can be detected statistically.

In quantum machine learning feature maps, classical data may be encoded into phases and rotations. The later circuit then recombines those amplitudes, making phase relationships observable in measurement statistics.

That last example is more advanced, so keep only the pattern for now: information is written into amplitudes or phase, transformed, and finally read out as statistics.

![Practical quantum technology examples](../figures/12_practical_quantum_technology.svg?v=greek-2026-05-27)

## 1.9 What Comes Next

The physical story gives us the target:

> Understand how amplitudes, phase, basis, and measurement interact.

The next chapter builds the math needed to say that precisely. It covers complex numbers, sine and cosine, Euler's formula, vectors, inner products, matrices, and probability-preserving transformations called unitaries.

Do not treat that chapter as detached algebra. Every piece will be used again:

- complex numbers explain phase,
- vectors explain states,
- bases explain what a measurement is asking,
- inner products compute amplitudes,
- matrices represent gates,
- unitaries preserve total probability.

# 2. Math and Algebra Prerequisites

This chapter is the mathematical toolkit for the rest of the book. It is deliberately practical. The goal is not abstract elegance for its own sake, but fluency with the objects that quantum mechanics uses every few lines.

The previous chapter used the arrow picture. This chapter gives that picture coordinates. When the notation starts to feel heavier, translate it back into the same story: arrows have lengths, arrows have directions, arrows can be added, and squared lengths become probabilities.

The core objects are:

- complex numbers,
- sine and cosine,
- Euler's formula,
- vectors and bases,
- inner products,
- matrices,
- unitary transformations,
- probability from squared magnitude.

Whenever a later chapter says "phase", "basis", "projection", "gate", or "unitary", it is using material from this chapter.

## 2.0 Why This Math Is Here

The learner's request was not "teach me abstract linear algebra." It was "I understand math, but remind me of the pieces that make quantum understandable."

So this chapter is a repair bench. Every tool here has a job later:

- complex numbers carry phase,
- sine and cosine describe rotations,
- vectors hold amplitudes,
- bases define the possible answers to a measurement,
- inner products compute the amplitude of an answer,
- matrices describe gates,
- unitaries explain why gates preserve total probability.

When the later chapters refer back here, the intent is not to interrupt the physics. It is to keep the physics honest.

You do not need to love every symbol on first contact. You do need to know what job it performs in the signal chain from amplitude to observed count.

## 2.1 Complex Numbers

**Question.** Why do quantum amplitudes use complex numbers instead of ordinary real numbers?

**Teacher.** Because quantum states need a built-in notion of phase, and phase is naturally represented as rotation in the complex plane.

Here "complex" does not mean complicated. It means a number with two coordinates: one horizontal, one vertical. That two-coordinate form is exactly what lets an amplitude behave like an arrow instead of only like a positive weight.

A complex number has the form:

```math
z = a + ib
```

where:

```math
i^2 = -1
```

The number $a$ is the real part. The number $b$ is the imaginary part.

The magnitude is:

```math
|z| = \sqrt{a^2 + b^2}
```

The squared magnitude is:

```math
|z|^2 = a^2 + b^2
```

Quantum probabilities come from squared magnitudes:

```math
P = |\psi|^2
```

This is why a complex amplitude can be negative, imaginary, or phase-shifted, while the final probability remains a nonnegative real number.

## 2.2 The Complex Plane

You can picture $z = a + ib$ as a point or vector:

- horizontal coordinate $a$,
- vertical coordinate $b$.

For example:

```math
1 = 1 + 0i
```

points to the right, while

```math
i = 0 + 1i
```

points upward.

The number

```math
-1 = -1 + 0i
```

points left.

This matters because amplitudes can cancel as vectors:

```math
1 + (-1) = 0
```

They can also cancel after rotating through phases, not only by being literally positive and negative real numbers.

Here is the first small mental picture to keep:

```text
amplitude = arrow
probability = squared length of the final arrow
```

Two arrows pointing in the same direction make a longer arrow. Two arrows pointing in opposite directions can leave no arrow at all. The detector does not see the individual arrows; it sees the squared length after the arrows have been added.

## 2.3 Sine and Cosine as Coordinates

The trigonometric functions $\cos\theta$ and $\sin\theta$ are coordinates on the unit circle.

If a point lies on a circle of radius 1 at angle $\theta$, then:

```math
x = \cos\theta
\qquad
y = \sin\theta
```

The identity:

```math
\cos^2\theta + \sin^2\theta = 1
```

is the statement that the point remains on the unit circle.

This identity reappears in qubits. A single-qubit state often uses:

```math
\cos\frac{\theta}{2}
\quad\text{and}\quad
\sin\frac{\theta}{2}
```

as amplitude magnitudes. The squared magnitudes add to 1:

```math
\cos^2\frac{\theta}{2} + \sin^2\frac{\theta}{2} = 1
```

That is exactly what we need for probabilities to sum to 1.

The half-angle is not a typographical flourish. It is what makes a full trip from the north pole to the south pole of the Bloch sphere correspond to changing the probability from all $|0\rangle$ to all $|1\rangle$:

```math
\theta = 0
\Rightarrow
P(0)=1
```

```math
\theta = \pi
\Rightarrow
P(1)=1
```

## 2.4 Euler's Formula

Euler's formula is the bridge between trigonometry and complex phase:

```math
e^{i\phi} = \cos\phi + i\sin\phi
```

This says that $e^{i\phi}$ is a unit-length complex number at angle $\phi$.

Its magnitude is always 1:

```math
|e^{i\phi}| = 1
```

So multiplying an amplitude by $e^{i\phi}$ changes its direction in the complex plane without changing its magnitude.

That is phase.

![Complex phase clock](../figures/03_complex_phase_clock.svg?v=greek-2026-05-27)

## 2.5 Why Phase Can Be Invisible

Suppose:

```math
\psi = e^{i\phi}
```

Then:

```math
|\psi|^2 = |e^{i\phi}|^2 = 1
```

So if you look only at this one amplitude's magnitude, the phase does not change the probability.

That is the origin of a common phrase:

> Phase does not affect probability.

But that phrase is incomplete. Phase may be invisible when measuring one component directly. It becomes visible when amplitudes are added before squaring.

For example:

```math
\left|\frac{1 + e^{i\phi}}{2}\right|^2
=
\cos^2\frac{\phi}{2}
```

At $\phi = 0$, this equals 1. At $\phi = \pi$, this equals 0.

Same magnitude for the individual phase factor, completely different probability after recombination.

This is the algebraic heart of interference.

**Teacher's pause.** The safe sentence is not "phase never affects probability." The safe sentence is "phase does not affect the probability of one isolated amplitude, but it can affect probability when amplitudes are recombined before squaring."

## 2.6 Vectors

A vector is an ordered list of numbers. In quantum mechanics, those numbers are often complex.

This is the first place where the arrow picture becomes a state description. A single amplitude is one arrow. A qubit state is a pair of arrows, one attached to the $|0\rangle$ alternative and one attached to the $|1\rangle$ alternative.

The computational basis states of a qubit are written:

```math
|0\rangle =
\begin{pmatrix}
1 \\
0
\end{pmatrix}
\qquad
|1\rangle =
\begin{pmatrix}
0 \\
1
\end{pmatrix}
```

A general qubit is:

```math
|\psi\rangle =
\alpha |0\rangle + \beta |1\rangle
=
\begin{pmatrix}
\alpha \\
\beta
\end{pmatrix}
```

The coefficients $\alpha$ and $\beta$ are complex amplitudes.

The normalization condition is:

```math
|\alpha|^2 + |\beta|^2 = 1
```

This condition ensures that measurement probabilities sum to 1.

The state vector is therefore not a list of two probabilities. It is a list of two amplitude coordinates from which probabilities can later be computed.

## 2.7 Basis

A basis is a set of reference vectors used to describe a state.

The same vector can be described in different bases, just as the same physical direction in space can be described using north/east coordinates or using rotated axes.

This is where the learner's practical instinct matters. A basis is not merely notation. In quantum mechanics, a basis is tied to the question a measurement is asking.

For qubits, the most important bases are:

The Z basis:

```math
|0\rangle
\qquad
|1\rangle
```

The X basis:

```math
|+\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
\qquad
|-\rangle =
\frac{|0\rangle - |1\rangle}{\sqrt{2}}
```

Why those formulas?

First, the X-basis states are still being written using the Z-basis coordinates $|0\rangle$ and $|1\rangle$. That is like describing a rotated pair of axes using the old horizontal and vertical coordinates.

The raw vector

```math
|0\rangle + |1\rangle
=
\begin{pmatrix}
1 \\
1
\end{pmatrix}
```

has squared length:

```math
1^2 + 1^2 = 2
```

So it is too long to be a normalized quantum state. We divide by $\sqrt{2}$ because:

```math
\left|\frac{1}{\sqrt{2}}\right|^2
+
\left|\frac{1}{\sqrt{2}}\right|^2
=
\frac{1}{2} + \frac{1}{2}
=
1
```

That is why the denominator is $\sqrt{2}$, not $2$. Amplitudes are squared to become probabilities.

Second, the two basis states must be mutually exclusive measurement answers. Mathematically, that means they must be orthogonal:

```math
\langle +|-\rangle
=
\frac{1}{2}(1 - 1)
=
0
```

The plus state and minus state contain the same Z-basis magnitudes, but their relative sign is different. That relative sign is a phase difference. Measuring in the X basis asks:

```text
Is the state aligned with |+> or with |->?
```

It is not asking whether the state is $|0\rangle$ or $|1\rangle$.

You can also reverse the equations:

```math
|0\rangle =
\frac{|+\rangle + |-\rangle}{\sqrt{2}}
\qquad
|1\rangle =
\frac{|+\rangle - |-\rangle}{\sqrt{2}}
```

So neither basis is more real than the other. They are two coordinate systems for the same two-dimensional state space.

The Y basis:

```math
|+i\rangle =
\frac{|0\rangle + i|1\rangle}{\sqrt{2}}
\qquad
|-i\rangle =
\frac{|0\rangle - i|1\rangle}{\sqrt{2}}
```

The Y basis follows the same pattern as the X basis, except the relative phase is $\pm i$ instead of $\pm 1$. Multiplication by $i$ is a 90-degree phase rotation. So the Y basis is another pair of normalized, orthogonal axes:

```math
|+i\rangle =
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1 \\
i
\end{pmatrix}
\qquad
|-i\rangle =
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1 \\
-i
\end{pmatrix}
```

The important idea is:

> A measurement basis is a choice of questions. The basis vectors are the possible answers to that question.

Read these as:

- "ket plus",
- "ket minus",
- "ket plus i",
- "ket minus i".

These states will become the axes of the Bloch sphere in [Chapter 4](04_qubits_and_bloch_sphere.md), and the measurement bases in [Chapter 5](05_measurement_bases.md).

## 2.8 Inner Products

An inner product measures overlap between vectors.

For complex vectors, the bra corresponding to a ket is the conjugate transpose. If:

```math
|\psi\rangle =
\begin{pmatrix}
\alpha \\
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

The star means complex conjugate:

```math
(a + ib)^* = a - ib
```

The amplitude for state $|\psi\rangle$ to be found in basis state $|\phi\rangle$ is:

```math
\langle \phi|\psi\rangle
```

The probability is:

```math
P(\phi) = |\langle \phi|\psi\rangle|^2
```

This is how we compute measurement probabilities in any basis.

Read $\langle \phi|\psi\rangle$ as a question:

> How much of $|\psi\rangle$ points in the $|\phi\rangle$ direction?

The answer is an amplitude, not yet a probability. Only after taking the squared magnitude do we get the probability for that measurement answer.

## 2.9 Matrices

A matrix is a linear transformation. A single-qubit gate is represented by a $2 \times 2$ matrix:

```math
U =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
```

It acts on a state vector:

```math
U|\psi\rangle
```

For example, if:

```math
|\psi\rangle =
\begin{pmatrix}
\alpha \\
\beta
\end{pmatrix}
```

then:

```math
U|\psi\rangle =
\begin{pmatrix}
a\alpha + b\beta \\
c\alpha + d\beta
\end{pmatrix}
```

Notice the sums. Matrix multiplication is one place where amplitudes naturally recombine.

This is why matrices are not just a notation tax. They are the machinery that takes the two stored amplitude arrows, mixes them, and produces new arrows for the next step of the circuit.

## 2.10 How a Gate Becomes a Matrix

**Question.** How do we get the actual matrix of a gate from ket notation?

**Teacher.** A linear map is determined by what it does to basis vectors. The images of the basis vectors become the columns of the matrix.

Suppose:

```math
U|0\rangle = a|0\rangle + c|1\rangle
```

and:

```math
U|1\rangle = b|0\rangle + d|1\rangle
```

Then:

```math
U =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
```

The first column is $U|0\rangle$. The second column is $U|1\rangle$.

This will be used repeatedly in [Gates, Matrices, and Rotations](06_gates_matrices_rotations.md).

## 2.11 Unitary Matrices

Quantum evolution without measurement is represented by unitary matrices.

A matrix $U$ is unitary if:

```math
U^\dagger U = I
```

Here $U^\dagger$ is the conjugate transpose of $U$.

The practical meaning is:

> Unitary transformations preserve total probability.

If:

```math
|\alpha|^2 + |\beta|^2 = 1
```

then after applying a unitary gate:

```math
|\psi'\rangle = U|\psi\rangle
```

the new amplitudes still satisfy:

```math
|\alpha'|^2 + |\beta'|^2 = 1
```

That is why ordinary gates are reversible. Measurement is the non-unitary step where a classical outcome is produced.

## 2.12 The Born Rule

The Born rule is the rule that converts quantum amplitude into probability.

If a state is:

```math
|\psi\rangle =
\alpha |0\rangle + \beta |1\rangle
```

then measurement in the Z basis gives:

```math
P(0) = |\alpha|^2
\qquad
P(1) = |\beta|^2
```

More generally, if measuring in a basis containing $|\phi\rangle$:

```math
P(\phi) = |\langle \phi|\psi\rangle|^2
```

This is the formula that connects all the later examples:

- double slit screen probabilities,
- X-basis measurement,
- Y-basis measurement,
- final circuit readout,
- phase-sensitive sensing.

## 2.13 Summary

Keep this compact map nearby:

| Concept | Formula | Meaning |
|---|---|---|
| Complex number | $z=a+ib$ | amplitude with direction and magnitude |
| Magnitude | $\lvert z\rvert=\sqrt{a^2+b^2}$ | length in complex plane |
| Probability | $P=\lvert\psi\rvert^2$ | squared amplitude magnitude |
| Phase | $e^{i\phi}$ | unit rotation in complex plane |
| Qubit | $\lvert\psi\rangle=\alpha\lvert0\rangle+\beta\lvert1\rangle$ | two complex amplitudes |
| Normalization | $\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1$ | total probability equals 1 |
| Inner product | $\langle \phi\vert\psi\rangle$ | amplitude of overlap |
| Matrix gate | $U\lvert\psi\rangle$ | linear transformation of amplitudes |
| Unitary | $U^\dagger U=I$ | probability-preserving evolution |

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

# 4. Qubits and the Bloch Sphere

The qubit is the simplest quantum information unit. It is not merely a bit that is "both 0 and 1." A better engineering definition is:

> A qubit is a two-dimensional quantum state whose coordinates are complex amplitudes.

This chapter keeps one guardrail in place: whenever a phrase sounds mystical, translate it back into amplitudes, phase, basis, and measurement statistics.

The previous chapter used two slits as the two alternatives. This chapter replaces the slits with two controllable labels, $|0\rangle$ and $|1\rangle$. That is the whole shift: the logic is still two alternatives with amplitudes, but now the alternatives are the states of an engineered two-level system.

## 4.1 The Computational Basis

The standard basis states are:

```math
|0\rangle =
\begin{pmatrix}
1 \\
0
\end{pmatrix}
\qquad
|1\rangle =
\begin{pmatrix}
0 \\
1
\end{pmatrix}
```

These are also called the computational basis or Z basis.

A general pure qubit state is:

```math
|\psi\rangle =
\alpha |0\rangle + \beta |1\rangle
```

In column-vector form:

```math
|\psi\rangle =
\begin{pmatrix}
\alpha \\
\beta
\end{pmatrix}
```

The amplitudes $\alpha$ and $\beta$ are complex numbers, and they must satisfy:

```math
|\alpha|^2 + |\beta|^2 = 1
```

This is the normalization rule from [Section 2.6](02_math_prerequisites.md#26-vectors).

![Qubit state vector](../figures/05_qubit_state_vector.svg?v=greek-2026-05-27)

## 4.2 Measurement in the Z Basis

If you measure:

```math
|\psi\rangle =
\alpha |0\rangle + \beta |1\rangle
```

in the Z basis, the Born rule gives:

```math
P(0) = |\alpha|^2
\qquad
P(1) = |\beta|^2
```

The device returns one classical bit: 0 or 1.

The important engineering point is that a single measurement does not reveal $\alpha$ and $\beta$. It samples from a distribution. To estimate probabilities experimentally, you prepare and measure many identical copies of the circuit.

So when a circuit diagram says a qubit is in state $|\psi\rangle$, do not imagine the measurement display will print that state. The display prints one classical result. The state is inferred from patterns across repeated preparations, measurements in chosen bases, and the circuit model that connects them.

## 4.3 Parameterizing a Qubit

Any single-qubit pure state can be written, up to an unobservable global phase, as:

```math
|\psi(\theta,\phi)\rangle =
\cos\frac{\theta}{2}|0\rangle
+
e^{i\phi}\sin\frac{\theta}{2}|1\rangle
```

This is the most important formula in the chapter.

Read it as a compact control panel:

- $\theta$ sets how much probability can appear in $|0\rangle$ versus $|1\rangle$ if you read in Z;
- $\phi$ sets the relative phase that later gates or non-Z measurements can reveal.

The angle $\theta$ controls the Z-basis probabilities:

```math
P(0) =
\cos^2\frac{\theta}{2}
\qquad
P(1) =
\sin^2\frac{\theta}{2}
```

The angle $\phi$ is the relative phase between the $|0\rangle$ and $|1\rangle$ components.

That phase may be invisible in Z measurement, but it affects what happens under later gates or measurements in other bases.

**Learner's checkpoint.** At fixed $\theta$, the Z-basis probabilities are fixed. Changing $\phi$ can still change the state because it changes how the two components will interfere later.

## 4.4 Global Phase versus Relative Phase

**Question.** If phase is so important, is every phase physically meaningful?

**Teacher.** No. A global phase is not observable, but a relative phase is.

If every amplitude is multiplied by the same phase:

```math
|\psi'\rangle =
e^{i\gamma}|\psi\rangle
```

then all measurement probabilities are unchanged:

```math
|\langle \phi|\psi'\rangle|^2
=
|e^{i\gamma}\langle \phi|\psi\rangle|^2
=
|\langle \phi|\psi\rangle|^2
```

But the relative phase in:

```math
\alpha |0\rangle + e^{i\phi}\beta |1\rangle
```

is meaningful, because it changes how the two components recombine.

This is exactly the lesson from [Chapter 3](03_double_slit_and_amplitudes.md): phase matters when amplitudes are added before squaring.

## 4.5 The Reference States

The six most useful single-qubit reference states are:

Z basis:

```math
|0\rangle
\qquad
|1\rangle
```

X basis:

```math
|+\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
\qquad
|-\rangle =
\frac{|0\rangle - |1\rangle}{\sqrt{2}}
```

Y basis:

```math
|+i\rangle =
\frac{|0\rangle + i|1\rangle}{\sqrt{2}}
\qquad
|-i\rangle =
\frac{|0\rangle - i|1\rangle}{\sqrt{2}}
```

Pronunciation:

- $|+\rangle$: "ket plus"
- $|-\rangle$: "ket minus"
- $|+i\rangle$: "ket plus i"
- $|-i\rangle$: "ket minus i"

These are not decorative names. They are the eigenstates of the three measurement axes:

- Z axis: $|0\rangle$, $|1\rangle$
- X axis: $|+\rangle$, $|-\rangle$
- Y axis: $|+i\rangle$, $|-i\rangle$

![Bloch reference states](../figures/06_bloch_reference_states.svg?v=greek-2026-05-27)

In the figure, each colored line is one basis axis. The two endpoints of the same axis are orthogonal states:

```math
\langle 0|1\rangle = 0
\qquad
\langle +|-\rangle = 0
\qquad
\langle +i|-i\rangle = 0
```

The X, Y, and Z axes themselves are mutually perpendicular directions on the Bloch sphere. A state from one axis is not generally orthogonal to a state from another axis: for example, $|0\rangle$ and $|+\rangle$ have overlap $1/\sqrt{2}$, which is why measuring $|+\rangle$ in the Z basis gives a 50/50 result.

This sentence is worth slowing down over. Opposite endpoints of the same axis are mutually exclusive answers to one measurement question. Points from different axes are different questions, so they can overlap.

## 4.6 The Bloch Sphere

The Bloch sphere is a geometric picture of a single qubit state.

The state:

```math
|\psi(\theta,\phi)\rangle =
\cos\frac{\theta}{2}|0\rangle
+
e^{i\phi}\sin\frac{\theta}{2}|1\rangle
```

corresponds to a point on a sphere with coordinates:

```math
r_x = \sin\theta\cos\phi
```

```math
r_y = \sin\theta\sin\phi
```

```math
r_z = \cos\theta
```

The vector:

```math
\vec r = (r_x,r_y,r_z)
```

is called the Bloch vector.

This formula is the bridge between:

- amplitude notation,
- phase,
- geometric axes,
- measurement probabilities.

If $\theta$ feels like "how much $|0\rangle$ versus $|1\rangle$" and $\phi$ feels like "which way the relative phase points around the equator," you have the right first picture. The Bloch vector packages those two feelings into coordinates that predict measurement statistics.

## 4.7 Reading the Bloch Sphere

The poles are:

```math
\theta = 0
\quad\Rightarrow\quad
|\psi\rangle = |0\rangle
```

```math
\theta = \pi
\quad\Rightarrow\quad
|\psi\rangle \sim |1\rangle
```

The equator contains equal Z-basis probabilities:

```math
P(0) = P(1) = \frac{1}{2}
```

But different equator points have different phases:

```math
\phi = 0
\quad\Rightarrow\quad
|+\rangle
```

```math
\phi = \pi
\quad\Rightarrow\quad
|-\rangle
```

```math
\phi = \frac{\pi}{2}
\quad\Rightarrow\quad
|+i\rangle
```

```math
\phi = \frac{3\pi}{2}
\quad\Rightarrow\quad
|-i\rangle
```

So two states can have identical Z-basis probabilities and still be different quantum states.

That is not a philosophical technicality. It is exactly why phase control is useful: two states that look identical to one detector can behave differently after the next gate.

## 4.8 Same Theta, Different Phi

This was one of the central points in the original conversation.

The reason it mattered is practical: if you only look at $P(0)$ and $P(1)$, you can miss information stored in phase. A quantum circuit can carry that information forward and reveal it only after a later rotation.

Take:

```math
\theta = 60^\circ
```

Then:

```math
\cos\frac{\theta}{2}
=
\cos 30^\circ
=
\frac{\sqrt{3}}{2}
```

and:

```math
\sin\frac{\theta}{2}
=
\sin 30^\circ
=
\frac{1}{2}
```

So:

```math
P(0) =
\left(\frac{\sqrt{3}}{2}\right)^2
=
\frac{3}{4}
```

and:

```math
P(1) =
\left(\frac{1}{2}\right)^2
=
\frac{1}{4}
```

Those probabilities do not depend on $\phi$.

But the states:

```math
\frac{\sqrt{3}}{2}|0\rangle
+
\frac{1}{2}|1\rangle
```

```math
\frac{\sqrt{3}}{2}|0\rangle
+
i\frac{1}{2}|1\rangle
```

```math
\frac{\sqrt{3}}{2}|0\rangle
-
\frac{1}{2}|1\rangle
```

and:

```math
\frac{\sqrt{3}}{2}|0\rangle
-
i\frac{1}{2}|1\rangle
```

are different states.

Z measurement cannot distinguish them. X and Y measurements can.

![Same theta phase ring](../figures/07_same_theta_phase_ring.svg?v=greek-2026-05-27)

The engineering lesson is blunt: a measurement that is blind to the difference is not evidence that the difference is absent. It is evidence that you asked a question that cannot see it.

This is exactly what happens in real experiments. If phase information matters, the circuit must rotate or recombine the state before readout. Otherwise, the histogram can look boring while the state still carries useful structure.

## 4.9 Physical Meaning

**Question.** What does the Bloch sphere mean physically? Is it a real sphere inside the hardware?

**Teacher.** No. It is a state-space picture, not a tiny physical ball.

For a superconducting qubit, $|0\rangle$ and $|1\rangle$ can correspond to two energy levels of an artificial atom. For an ion qubit, they may correspond to two internal states of an ion. For a photon, they may correspond to polarization states.

The Bloch sphere does not say the particle is literally located at a point on a sphere. It says the two-level quantum state has:

- a population imbalance, represented by $r_z$,
- a relative phase, represented by $r_x$ and $r_y$,
- measurement statistics determined by projections onto axes.

This is why the Bloch sphere is so useful for engineers. It turns amplitude algebra into a control picture:

- pulses rotate the state,
- phases move the state around the equator,
- readout extracts a component.

## 4.10 Summary

A qubit state is:

```math
|\psi\rangle =
\alpha|0\rangle + \beta|1\rangle
```

A useful parameterization is:

```math
|\psi(\theta,\phi)\rangle =
\cos\frac{\theta}{2}|0\rangle
+
e^{i\phi}\sin\frac{\theta}{2}|1\rangle
```

The Bloch vector is:

```math
\vec r =
(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)
```

Z measurement sees $r_z$. X measurement sees $r_x$. Y measurement sees $r_y$. This is the topic of the next chapter.

# 5. Measurement Bases

This chapter resolves the central conceptual tension of the conversation:

> Phase can be invisible in one measurement basis and visible in another.

The reason is not mysterious. A measurement basis determines which amplitudes are selected and which amplitudes are recombined before squaring.

In the original discussion, this is where the teacher slowed down and computed the same family of states three ways: Z, X, and Y. That repetition is the point. You are not learning three unrelated measurement tricks. You are watching the same hidden phase become visible from different angles.

The previous chapter gave the Bloch sphere as a map of the state. This chapter asks how to interrogate that map. Z, X, and Y are not decorations on the sphere; they are different experimental questions.

## 5.1 What "Measuring in a Basis" Means

**Question.** If real hardware eventually returns 0 or 1, why do people say "measure in X" or "measure in Y"?

**Teacher.** Because the hardware result is classical, but the question you ask the quantum state can be changed before readout.

Measuring in the Z basis means asking:

```math
\{|0\rangle, |1\rangle\}
```

Measuring in the X basis means asking:

```math
\{|+\rangle, |-\rangle\}
```

Measuring in the Y basis means asking:

```math
\{|+i\rangle, |-i\rangle\}
```

The physical detector may still report a bit, but by applying a rotation before measurement, we can make that bit correspond to a different basis.

This is covered operationally in [Circuits and Readout](07_circuits_and_readout.md). Here we focus on the probability formulas.

**Teacher's pause.** "Measure in X" does not mean the lab screen prints a plus sign instead of a 0. It means the circuit has been arranged so that a final 0 corresponds to the original state being aligned with $|+\rangle$.

## 5.2 Measurement as Projection

From [Section 2.8](02_math_prerequisites.md#28-inner-products), the amplitude for observing basis state $|\phi\rangle$ is:

```math
\langle \phi|\psi\rangle
```

The probability is:

```math
P(\phi) =
|\langle \phi|\psi\rangle|^2
```

For Z measurement:

```math
P(0) = |\langle 0|\psi\rangle|^2
\qquad
P(1) = |\langle 1|\psi\rangle|^2
```

For X measurement:

```math
P(+) = |\langle +|\psi\rangle|^2
\qquad
P(-) = |\langle -|\psi\rangle|^2
```

For Y measurement:

```math
P(+i) = |\langle +i|\psi\rangle|^2
\qquad
P(-i) = |\langle -i|\psi\rangle|^2
```

The same state can give different distributions in these bases.

This is the place to stop and notice the shift in language. A measurement basis is not a camera angle on a pre-existing classical bit. It is a choice of which quantum alternatives are allowed to interfere into the final answers.

So projection is not a passive lookup. It is the calculation of how much of the prepared state lines up with the answer you decided to test.

## 5.3 A State with Fixed Theta and Changing Phi

Use the state from the original discussion:

```math
|\psi(\theta,\phi)\rangle =
\cos\frac{\theta}{2}|0\rangle
+
e^{i\phi}\sin\frac{\theta}{2}|1\rangle
```

Set:

```math
\theta = 60^\circ
```

Then:

```math
\cos\frac{\theta}{2}
=
\frac{\sqrt{3}}{2}
\qquad
\sin\frac{\theta}{2}
=
\frac{1}{2}
```

So:

```math
|\psi\rangle =
0.866|0\rangle
+
0.5e^{i\phi}|1\rangle
```

The magnitudes are fixed. Only the relative phase changes.

This was chosen deliberately. If the Z probabilities change, it is too easy to think phase is just another way of changing population. Here the populations are fixed, so any change in X or Y must come from recombination of phase.

That makes this example a diagnostic tool. If a later histogram changes while the Z histogram stays fixed, the change is coming from phase-sensitive readout rather than from a different amount of $|0\rangle$ or $|1\rangle$.

## 5.4 Bloch-Vector Bridge

The Bloch vector is:

```math
\vec r =
(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)
```

Write:

```math
\vec r = (r_x,r_y,r_z)
```

For $\theta = 60^\circ$:

```math
\sin\theta =
\frac{\sqrt{3}}{2}
\approx 0.866
```

and:

```math
\cos\theta =
\frac{1}{2}
```

Therefore:

```math
r_z = 0.5
```

```math
r_x = 0.866\cos\phi
```

```math
r_y = 0.866\sin\phi
```

The measurement probabilities are:

```math
P(Z=0) =
\frac{1+r_z}{2}
\qquad
P(Z=1) =
\frac{1-r_z}{2}
```

```math
P(X=+) =
\frac{1+r_x}{2}
\qquad
P(X=-) =
\frac{1-r_x}{2}
```

```math
P(Y=+i) =
\frac{1+r_y}{2}
\qquad
P(Y=-i) =
\frac{1-r_y}{2}
```

This is what "choosing an axis" means mathematically: you choose which component of the Bloch vector becomes the measurement bias.

![Z X Y measurement probabilities](../figures/08_zxy_measurement_probabilities.svg?v=greek-2026-05-27)

Read the figure like an engineer debugging a signal path: Z is blind to the changing phase here, X sees the cosine part, and Y sees the sine part. Same state family, different readout question.

## 5.5 Z Basis: Phase Is Invisible

In Z measurement:

```math
P(Z=0) =
\frac{1+r_z}{2}
```

For our state:

```math
r_z = 0.5
```

So:

```math
P(Z=0) =
\frac{1+0.5}{2}
=
0.75
```

and:

```math
P(Z=1) =
0.25
```

This does not depend on $\phi$.

Interpretation:

Z measurement reads the magnitudes of the $|0\rangle$ and $|1\rangle$ components. It does not recombine them. Therefore the relative phase between them is not visible.

If you ran this experiment with many shots, the Z histogram would keep returning approximately:

```text
0: 75%
1: 25%
```

for every value of $\phi$ in this example. That flatness is not a failure of quantum theory. It is the signature of asking a phase-blind question.

## 5.6 X Basis: Phase Becomes Cosine

For X measurement:

```math
P(X=+) =
\frac{1+r_x}{2}
```

But:

```math
r_x = \sin\theta\cos\phi
```

For $\theta = 60^\circ$:

```math
P(X=+) =
\frac{1 + 0.866\cos\phi}{2}
```

At $\phi = 0$:

```math
P(X=+) \approx 0.933
```

At $\phi = \pi$:

```math
P(X=+) \approx 0.067
```

This swing is interference.

In algebraic form:

```math
\langle +|\psi\rangle
=
\frac{1}{\sqrt{2}}
\left(
\cos\frac{\theta}{2}
+
e^{i\phi}\sin\frac{\theta}{2}
\right)
```

That is a sum. When you square its magnitude, a cross term appears, and that cross term depends on $\cos\phi$.

In count language, the same prepared states that looked identical in Z now produce different X histograms. The phase has not become a new output label. It has become a bias in how often the ordinary outcomes occur.

## 5.7 Y Basis: Phase Becomes Sine

For Y measurement:

```math
P(Y=+i) =
\frac{1+r_y}{2}
```

But:

```math
r_y = \sin\theta\sin\phi
```

For $\theta = 60^\circ$:

```math
P(Y=+i) =
\frac{1 + 0.866\sin\phi}{2}
```

At $\phi = \frac{\pi}{2}$:

```math
P(Y=+i) \approx 0.933
```

At $\phi = \frac{3\pi}{2}$:

```math
P(Y=+i) \approx 0.067
```

So Y measurement sees the sine component of phase, shifted by 90 degrees relative to X.

Together, X and Y are like two phase-sensitive probes in quadrature: one sees the cosine part of the relative phase, the other sees the sine part. This is why both axes matter when reconstructing or controlling a qubit.

## 5.8 Where Interference Hides in the Algebra

This diagram summarizes the key contrast.

![Basis recombination algebra](../figures/09_basis_recombination_algebra.svg?v=greek-2026-05-27)

In Z measurement, the amplitude for outcome $0$ is:

```math
\langle 0|\psi\rangle = \alpha
```

It selects one component.

In X measurement, the amplitude for outcome $+$ is:

```math
\langle +|\psi\rangle
=
\frac{\alpha + \beta}{\sqrt{2}}
```

It adds components.

In Y measurement, the amplitude for outcome $+i$ is:

```math
\langle +i|\psi\rangle
=
\frac{\alpha - i\beta}{\sqrt{2}}
```

It also adds components, but with a phase shift.

The rule is:

> If the amplitude for a measurement outcome is a sum, then the probability can contain interference.

## 5.9 The Hardware Translation

**Question.** In real devices, do we physically build three different detectors for Z, X, and Y?

**Teacher.** Usually no.

Many platforms have a native readout that is effectively Z-like. For example, a superconducting qubit readout often distinguishes two energy-like states. That is naturally aligned with a computational basis.

To measure X or Y, you rotate the qubit first and then perform the standard Z readout.

Conceptually:

```text
measure X = rotate X information into Z, then measure Z
measure Y = rotate Y information into Z, then measure Z
```

This is why basis changes are not a decorative mathematical trick. They are how real quantum circuits convert hidden phase information into ordinary bits.

## 5.10 Summary

The original confusion is resolved as follows:

- Phase may be invisible in Z measurement because Z selects amplitudes separately.
- Phase becomes visible in X or Y measurement because those bases recombine amplitudes.
- X measurement is sensitive to the cosine component of relative phase.
- Y measurement is sensitive to the sine component of relative phase.
- Real hardware can often use one native readout basis plus rotations to implement other measurement bases.

The next chapter shows those rotations and gates as matrices.

# 6. Gates, Matrices, and Rotations

Quantum gates are transformations of amplitudes. For a single qubit, a gate is a $2 \times 2$ unitary matrix. On the Bloch sphere, many gates can be understood as rotations.

This chapter connects three languages:

- ket notation,
- matrices,
- geometric rotations.

The learner's practical question underneath all three languages is simple:

> If a gate is written as a symbol in a circuit, what does it actually do to the amplitudes?

The answer is: it linearly mixes amplitudes while preserving total probability. The matrix tells you exactly how.

The previous chapter changed the measurement question by changing basis before readout. This chapter shows the operations that make those basis changes possible. A gate is not a label placed on a wire; it is a rule for moving amplitude from old coordinates into new ones.

## 6.1 A Gate Is a Linear Map

From [Section 2.9](02_math_prerequisites.md#29-matrices), a matrix acts on a vector by linear combination.

For a qubit:

```math
|\psi\rangle =
\alpha|0\rangle + \beta|1\rangle
=
\begin{pmatrix}
\alpha \\
\beta
\end{pmatrix}
```

A gate $U$ produces:

```math
|\psi'\rangle = U|\psi\rangle
```

Because $U$ is linear:

```math
U(\alpha|0\rangle + \beta|1\rangle)
=
\alpha U|0\rangle + \beta U|1\rangle
```

That is why knowing what a gate does to $|0\rangle$ and $|1\rangle$ determines the whole gate.

This is a comforting fact for an engineer: you do not need to memorize what a gate does to every possible superposition. If you know its action on the basis states and you trust linearity, the action on every superposition follows.

## 6.2 Building the Matrix from Columns

**Question.** How does a ket rule become a matrix?

**Teacher.** The output of the first basis vector becomes the first column. The output of the second basis vector becomes the second column.

Suppose:

```math
U|0\rangle = a|0\rangle + c|1\rangle
```

and:

```math
U|1\rangle = b|0\rangle + d|1\rangle
```

Then:

```math
U =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
```

![Hadamard matrix columns](../figures/10_hadamard_matrix_columns.svg?v=greek-2026-05-27)

## 6.3 The Hadamard Gate

The Hadamard gate is:

```math
H =
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}
```

It acts on the computational basis as:

```math
H|0\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
=
|+\rangle
```

and:

```math
H|1\rangle =
\frac{|0\rangle - |1\rangle}{\sqrt{2}}
=
|-\rangle
```

It also maps back:

```math
H|+\rangle = |0\rangle
\qquad
H|-\rangle = |1\rangle
```

This is why applying $H$ before Z readout implements X-basis measurement.

## 6.4 Hadamard as Recombination

Hadamard is one of the clearest gates for seeing interference.

Apply $H$ to:

```math
|\psi\rangle =
\alpha|0\rangle + \beta|1\rangle
```

Using matrix multiplication:

```math
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
```

The new $|0\rangle$ amplitude is:

```math
\frac{\alpha+\beta}{\sqrt{2}}
```

The new $|1\rangle$ amplitude is:

```math
\frac{\alpha-\beta}{\sqrt{2}}
```

So $H$ explicitly creates sums and differences of amplitudes. It is a recombination gate.

If $\alpha = 1/\sqrt{2}$ and $\beta = -1/\sqrt{2}$, then:

```math
\alpha+\beta = 0
```

and the $|0\rangle$ output disappears.

**Teacher's pause.** This is the double slit in circuit clothing. Hadamard is not magic; it is a controlled way of making amplitudes meet in the same output coordinate.

## 6.5 Pauli Gates

The Pauli gates are:

```math
X =
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
```

```math
Y =
\begin{pmatrix}
0 & -i \\
i & 0
\end{pmatrix}
```

```math
Z =
\begin{pmatrix}
1 & 0 \\
0 & -1
\end{pmatrix}
```

Their basic actions are:

```math
X|0\rangle = |1\rangle
\qquad
X|1\rangle = |0\rangle
```

So $X$ is the quantum analogue of a bit flip.

The $Z$ gate leaves $|0\rangle$ unchanged and flips the sign of $|1\rangle$:

```math
Z(\alpha|0\rangle + \beta|1\rangle)
=
\alpha|0\rangle - \beta|1\rangle
```

This is a phase flip. It does not change Z-basis probabilities, but it changes future interference.

This is the same pattern again: a phase operation can look like "nothing happened" if you immediately measure in Z. But if a later gate recombines amplitudes, that hidden sign can become a deterministic change in the output.

The $Y$ gate combines bit flip and phase factors.

Do not worry if $Y$ feels less intuitive than $X$ and $Z$ at first. In practice, the key point is that it mixes the two earlier ideas: it swaps the basis states and adds phase factors, so it participates in both population movement and phase control.

## 6.6 The Phase Gate S

The $S$ gate is:

```math
S =
\begin{pmatrix}
1 & 0 \\
0 & i
\end{pmatrix}
```

It acts as:

```math
S(\alpha|0\rangle + \beta|1\rangle)
=
\alpha|0\rangle + i\beta|1\rangle
```

It adds a relative phase of $\pi/2$ to the $|1\rangle$ component.

Its inverse is:

```math
S^\dagger =
\begin{pmatrix}
1 & 0 \\
0 & -i
\end{pmatrix}
```

The $S^\dagger$ gate is used when converting Y-basis information into Z-basis readout.

In the language of Chapter 5, $S$ and $S^\dagger$ are phase-reference tools. They do not merely decorate the state with an $i$; they change which later recombinations will be constructive or destructive.

## 6.7 Rotation Gates

Single-qubit rotations are usually written:

```math
R_x(\theta) =
e^{-i\theta X/2}
```

```math
R_y(\theta) =
e^{-i\theta Y/2}
```

```math
R_z(\theta) =
e^{-i\theta Z/2}
```

If the exponential notation feels sudden, do not let it interrupt the story. Here it is compact notation for "the operation generated by this axis." The matrices below are the concrete version you can multiply by a state vector.

Their matrices are:

```math
R_x(\theta)
=
\begin{pmatrix}
\cos(\theta/2) & -i\sin(\theta/2) \\
-i\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
```

```math
R_y(\theta)
=
\begin{pmatrix}
\cos(\theta/2) & -\sin(\theta/2) \\
\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
```

```math
R_z(\theta)
=
\begin{pmatrix}
e^{-i\theta/2} & 0 \\
0 & e^{i\theta/2}
\end{pmatrix}
```

These gates rotate the Bloch vector around the X, Y, and Z axes.

The notation $e^{-i\theta X/2}$ is compact, but its practical meaning is simple: choose an axis, choose an angle, and move the state around the Bloch sphere while preserving total probability.

This is one of those places where the algebra is denser than the idea. The dense notation matters for calculation, but the first mental image should be a calibrated rotation command.

## 6.8 Rotations Have Physical Meaning

**Question.** Are these rotations just math, or do they correspond to real hardware controls?

**Teacher.** They correspond to real controls.

In many quantum devices, gates are implemented by applying controlled pulses. The pulse amplitude, duration, phase, and frequency determine the rotation axis and angle in the qubit's state space.

For example:

- a pulse resonant with a superconducting qubit transition can rotate the state around an equatorial axis,
- the phase of the microwave drive changes the rotation axis in the X-Y plane,
- virtual Z rotations can often be implemented by updating a phase reference rather than physically pulsing the qubit.

The Bloch sphere is therefore not just a teaching picture. It is also a control picture.

This is the engineering payoff of the geometry. A rotation on the page corresponds to a calibrated control action in the device, even though the sphere itself is a state-space diagram rather than a physical ball.

## 6.9 Unitarity and Probability Conservation

Every ideal gate above is unitary:

```math
U^\dagger U = I
```

This means:

```math
\|U|\psi\rangle\|^2 =
\||\psi\rangle\|^2
```

In ordinary language:

> Gates move probability amplitude around, but they do not create or destroy total probability.

Measurement is different. Measurement produces a classical outcome and changes the state in a non-unitary way.

## 6.10 Why Gates Matter for Interference

The double-slit experiment has physical paths and a screen that recombines them.

A quantum circuit has basis states and gates that recombine amplitudes.

The Hadamard gate is the simplest example:

```math
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
```

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

# 7. Circuits and Readout

A quantum circuit is a sequence of operations applied to quantum states, followed by measurement. The useful part of the circuit usually happens before measurement, while amplitudes are still free to interfere.

This chapter connects the earlier ideas:

- amplitudes,
- basis changes,
- gates,
- rotations,
- final readout.

The learner's question here was direct: if everything ends as 0 or 1, why did we spend so much effort on phase and basis? The answer is that the final 0/1 counts are the readout of an interference process that happened before the measurement.

The previous chapters taught the pieces separately: amplitudes, bases, gates, and rotations. A circuit is the sentence that puts those words in order.

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

This is the discipline of circuit design: keep information quantum while it needs to interfere, then deliberately convert it to classical data only when the useful bias has been created.

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

That line is easy to skim, but it is the whole hardware trick: if the detector is fixed, move the state instead of replacing the detector.

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

A histogram is not a disappointing substitute for the state. It is the experimental footprint left by the state after the chosen circuit has turned amplitude relationships into count frequencies.

## 7.7 Expectation Values

For a single qubit, the expectation values of Pauli observables are connected to the Bloch vector:

An observable is a measurable quantity. A Pauli observable is the idealized question "what is the state biased toward along this axis?" So $\langle Z\rangle$, $\langle X\rangle$, and $\langle Y\rangle$ are not hidden labels on one shot. They are averages estimated from many repeated measurements.

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

# 8. Practical Examples

The conversation asked for practical perspective, not only formal quantum mechanics. This chapter connects the same amplitude-and-phase ideas to real technology.

The goal is not to survey every quantum technology. The goal is to show how the book's core ideas reappear in practical settings.

The practical thread is this: a real device does not give us a private view of amplitudes. It gives us control knobs, noise, calibration, pulses, detectors, and count histograms. The theory is useful when it tells us how those knobs steer amplitudes before the counts appear.

So the examples below should not be read as a catalog of buzzwords. Read each one as a translation exercise: where are the amplitudes, what physical process changes their phase, and what measurement makes the change visible?

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

![Practical quantum technology examples](../figures/12_practical_quantum_technology.svg?v=greek-2026-05-27)

When reading the examples below, keep asking the same practical question:

> Where is the information stored before readout, and what operation makes it visible?

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

is the smallest model of this idea. The first $H$ creates alternatives. The phase operation changes the relative phase. The final $H$ recombines alternatives so phase becomes a measurable bias.

Larger algorithms use higher-dimensional versions of the same idea.

**Teacher's pause.** This is why the one-qubit examples are not toys to discard. They are the smallest circuit diagrams in which the central mechanism is visible without hiding it under many qubits.

For example, in Grover-style search, the details become multi-qubit and geometric, but the story is still amplitude steering: mark useful structure with phase, then use transformations that make the useful amplitude grow relative to the rest.

That sentence is intentionally modest. It does not claim that every problem becomes easy. It says that when a quantum algorithm helps, the help comes through a carefully arranged amplitude landscape, not through reading all answers at once.

## 8.3 Quantum Sensing

Quantum sensing is often the most physically intuitive application of phase.

Imagine a qubit prepared in an equal superposition:

```math
|+\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
```

Suppose the environment causes the $|1\rangle$ component to acquire a phase:

```math
|\psi\rangle =
\frac{|0\rangle + e^{i\phi}|1\rangle}{\sqrt{2}}
```

The phase $\phi$ may depend on a magnetic field, electric field, acceleration, time, or another physical quantity.

This is where the physical world enters the math. The environment has written a tiny change into relative phase, and the experimenter's job is to choose a pulse sequence that converts that hidden phase into a count difference.

Z measurement alone gives:

```math
P(0)=P(1)=\frac{1}{2}
```

But applying $H$ before measurement gives:

```math
P(0)=\cos^2\frac{\phi}{2}
```

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

In the language of the earlier chapters: nature writes information into $\phi$, and the experimenter chooses rotations that make $\phi$ show up in $P(0)$ and $P(1)$.

## 8.5 Superconducting Qubits

In a superconducting qubit, $|0\rangle$ and $|1\rangle$ can be two energy levels of an engineered electrical circuit.

The state is still described as:

```math
|\psi\rangle =
\alpha|0\rangle + \beta|1\rangle
```

Control pulses change $\alpha$, $\beta$, and their relative phase. Measurement typically distinguishes the two basis states through a coupled readout resonator.

From the viewpoint of this book:

- pulses implement rotations,
- detuning and phase references affect $R_z$-like behavior,
- readout is often Z-like,
- X and Y information is accessed by pre-rotations.

The math in Chapters 4 through 7 is therefore directly connected to laboratory control.

If you have worked with classical control systems, the analogy is not perfect, but the instinct helps: pulses are not decorative commands. They are calibrated interventions that move the system through a state space so that the final measurement has the bias you intended.

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

```math
|H\rangle
\qquad
|V\rangle
```

or in paths/modes:

```math
|L\rangle
\qquad
|R\rangle
```

This connects directly to the double-slit discussion.

Optical elements such as beam splitters and phase shifters perform transformations analogous to gates. Detectors then measure output modes.

A beam splitter is an especially physical version of "split and recombine amplitudes." It is the optical cousin of the Hadamard-like operation.

This makes photonics a helpful mental bridge: the paths can be literal optical paths, the phase shifter can be a real optical element, and the detectors count output modes. The qubit circuit notation is more abstract, but the amplitude logic is the same.

## 8.8 Quantum Cryptography

Quantum cryptography uses measurement disturbance and basis choice.

This is the same basis lesson in a security setting. If someone asks the wrong quantum question, they may not merely learn the wrong answer; they may change the state in a way that later statistics reveal.

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

The phrase "feature map" means a data-to-state recipe: take ordinary input numbers and use them to choose gates. The result is a quantum state whose amplitudes and phases now depend on the data.

For example, a feature value $x$ might determine a rotation:

```math
R_z(x)
```

or:

```math
R_y(x)
```

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

That is the practical humility to keep: the clean model is not the finished machine, but it is the map that tells you what the machine is trying to preserve.

## 8.11 Summary

The same ideas reappear across applications:

- Algorithms use gates to arrange constructive and destructive interference.
- Sensors convert physical phase shifts into measurable probability shifts.
- Cryptography uses basis choice and measurement disturbance.
- Hardware control implements rotations of two-level systems.
- Feature maps encode data into phases or amplitudes before measurement.

The unifying question is always:

> What information is stored in amplitude or phase, and what transformation will make it visible in measurement statistics?

# 9. Worked Labs

This chapter gives small calculations you can reproduce without a quantum SDK. The point is to make the algebra tangible.

The examples use ordinary Python complex numbers and matrix multiplication.

Treat these labs as a replay of the conversation, not as programming exercises detached from the book. Each lab answers a specific doubt:

- Can two nonzero amplitudes really sum to zero?
- Can phase be invisible in Z but visible in X?
- Can one matrix turn a phase difference into a bit difference?

The labs are deliberately small because the first practical skill is not running a large framework. It is predicting what should happen before software or hardware hides the mechanism.

## 9.1 Lab 1: Perfect Amplitude Cancellation

Compute:

```math
\psi_1 = e^{i0}
\qquad
\psi_2 = e^{i\pi}
```

Since:

```math
e^{i0}=1
\qquad
e^{i\pi}=-1
```

we have:

```math
\psi_1+\psi_2 = 0
```

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

What you should feel: the zero did not come from deleting a path. It came from adding two valid contributions with opposite phase.

## 9.2 Lab 2: Phase Invisible in Z

Consider:

```math
|\psi\rangle =
\frac{|0\rangle + e^{i\phi}|1\rangle}{\sqrt{2}}
```

The amplitudes are:

```math
\alpha = \frac{1}{\sqrt{2}}
\qquad
\beta = \frac{e^{i\phi}}{\sqrt{2}}
```

Z-basis probabilities:

```math
P(0) = |\alpha|^2 = \frac{1}{2}
```

```math
P(1) = |\beta|^2 = \frac{1}{2}
```

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

What you should feel: Z measurement is blind to this phase, even though the state is changing.

## 9.3 Lab 3: Phase Visible in X

For the same state:

```math
|\psi\rangle =
\frac{|0\rangle + e^{i\phi}|1\rangle}{\sqrt{2}}
```

the X-basis $+$ amplitude is:

```math
\langle +|\psi\rangle
=
\frac{1 + e^{i\phi}}{2}
```

So:

```math
P(+) =
\left|
\frac{1 + e^{i\phi}}{2}
\right|^2
```

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

What you should feel: the same phase that was invisible in Lab 2 becomes visible once the X-basis calculation adds the two components.

## 9.4 Lab 4: Theta 60 Degrees in Z, X, and Y

Use:

```math
|\psi(\theta,\phi)\rangle =
\cos\frac{\theta}{2}|0\rangle
+
e^{i\phi}\sin\frac{\theta}{2}|1\rangle
```

with:

```math
\theta = 60^\circ
```

The Bloch components are:

```math
r_x = \sin\theta\cos\phi
```

```math
r_y = \sin\theta\sin\phi
```

```math
r_z = \cos\theta
```

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

- $P(Z=0)$ stays at 0.75.
- $P(X=+)$ changes with $\cos\phi$.
- $P(Y=+i)$ changes with $\sin\phi$.

This is exactly the plot generated in:

```text
figures/08_zxy_measurement_probabilities.svg
```

What you should feel: Z, X, and Y are not three unrelated calculations. They are three different probes of the same Bloch vector.

## 9.5 Lab 5: Hadamard as a Matrix

Use:

```math
H =
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}
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

Those are $|+\rangle$ and $|-\rangle$.

What you should feel: the matrix columns are not arbitrary numbers. They are the images of the basis states.

## 9.6 Lab 6: H-Z-H Interference

Start with $|0\rangle$.

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

The middle $Z$ gate only changed phase in the computational basis. The final $H$ converted that phase change into a bit flip.

This is the practical point of the whole book in one toy circuit.

What you should feel: a phase that looked hidden became a certain classical outcome because the circuit recombined amplitudes before measuring.

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

   ```math
   |\psi\rangle =
   \frac{|0\rangle - |1\rangle}{\sqrt{2}}
   ```

   compute $P(0)$, $P(1)$, $P(+)$, and $P(-)$.

2. For

   ```math
   |\psi\rangle =
   \frac{|0\rangle + i|1\rangle}{\sqrt{2}}
   ```

   compute $P(+i)$ and $P(-i)$.

3. Show that $H^2 = I$.

4. Show that $Z|+\rangle = |-\rangle$.

5. Use Python to plot $P(X=+)$ as a function of $\phi$ for:

   ```math
   |\psi\rangle =
   \cos\frac{\theta}{2}|0\rangle
   +
   e^{i\phi}\sin\frac{\theta}{2}|1\rangle
   ```

   with $\theta = 30^\circ$, $60^\circ$, and $90^\circ$.

## 9.9 Answers in Brief

1. For $|-\rangle$, Z gives $1/2,1/2$, and X gives $P(+)=0$, $P(-)=1$.
2. For $|+i\rangle$, Y gives $P(+i)=1$, $P(-i)=0$.
3. $H^2=I$ by direct matrix multiplication.
4. $Z|+\rangle=(|0\rangle-|1\rangle)/\sqrt{2}=|-\rangle$.
5. Increasing $\theta$ increases the swing in X-basis probability, because the swing amplitude is $\sin\theta$.

# 10. Glossary

This glossary is meant to be read as a conversational index, not a replacement for the chapters. Each definition points back to the pressure points of the book: what evolves before measurement, what is observed after measurement, and what transformations make hidden phase visible.

## Amplitude

A complex, arrow-like number associated with a possible outcome or contribution. Amplitudes can add or cancel before measurement. Probabilities are computed from squared magnitudes of the final amplitudes.

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
