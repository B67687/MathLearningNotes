---
title: "**Summary of Key Learnings**"
source_notebook: "calculus/advancements-report-19th-march-2025.ipynb"
archived_notebook: "archive/notebooks/calculus/advancements-report-19th-march-2025.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# **Summary of Key Learnings**

# Leading Term Analysis for Limits

- **Variable in the Base**: For expressions like $e^{\frac{p(x)}{q(x)}}$, apply leading term analysis to the polynomials $p(x)$ and $q(x)$ by comparing highest-degree terms, then evaluate the resulting exponential.
- **Variable in the Exponent**: For sums like $a e^{kx}$, the leading term depends on the sign of $k$ and the direction of $x$: positive $k$ dominates as $x \to +\infty$, negative $k$ dominates as $x \to -\infty$.

## 1. Leading-Term Analysis vs. Standard Way

#### Leading-Term Analysis
- **Method**: Focus on the term with the largest power.
- **Application**: The dominant term is $4x^7$. As $x \to -\infty$, $x^7 \to -\infty$, so $4x^7 \to -\infty$. Smaller terms ($-18x^3$, $9$) are negligible.
- **Result**: The limit is $-\infty$.

#### My Proposed Method for Rational Expressions
- **Method**: For rational expressions, take the largest term in the numerator and divide by the denominator, replacing approximate equality with exact equality.
- **Justification**: Smaller terms become negligible at large $|x|$, so the largest term dictates the tendency.

#### Standard Approach
- **Method**: Divide numerator and denominator by the highest power of $x$ in the denominator ($x^{-3}$).
- **Application**:
  - Numerator: $4 - \frac{18}{x^4} + \frac{9}{x^7} \to 4$.
  - Denominator: $\frac{2}{x^3} + \frac{5}{x^5} + \frac{1}{x^7} \to \frac{2}{x^3} \cdot x^3 = 2$.
  - Limit: $\frac{4}{2} = 2$.
- **Polarity Check**: Leading terms are $-\frac{18}{x^4}$ (numerator) and $\frac{2}{x^3}$ (denominator). As $x \to -\infty$, numerator is negative, denominator is negative, so the overall polarity is positive, confirming the limit is $2$.

#### Comparison
- **Leading-Term Analysis**: Faster, skips polarity of smaller terms.
- **Standard Approach**: More rigorous, requires an extra polarity check.
- **Conclusion**: Both methods can yield correct results, but leading-term analysis is more efficient for quick evaluations.

## Leading-Term Analysis for Fractions

#### Realization
- **Reason**: A fraction represents a relationship between numerator and denominator. Focusing only on one part ignores the fraction as a whole.
- **Example**: For $\frac{x^7}{x^3}$:
  - Largest term overall: $x^7$, suggests limit is $-\infty$ as $x \to -\infty$.
  - Correct method: $\frac{x^7}{x^3} = x^4$, limit is $+\infty$ (even power).
- **Conclusion**: Leading-term analysis works best for non-fractions (denominator = 1). Fractions require considering two relative rates: within numerator/denominator and between them.

## Limit Analysis of Exponential Functions

We evaluate the limits of the given functions as $x \to +\infty$ and $x \to -\infty$.

#### Question 2: $f(x) = e^{\frac{6x^2 + x}{5 + 3x}}$

- **As $x \to +\infty$**: Exponent $\frac{6x^2}{3x} = 2x \to +\infty$, so $f(x) \to +\infty$.
- **As $x \to -\infty$**: Exponent $2x \to -\infty$, so $f(x) \to 0$.

#### Question 3: $f(x) = 2e^{6x} - e^{-7x} - 10e^{4x}$

- **As $x \to +\infty$**: Dominated by $2e^{6x}$, so $f(x) \to +\infty$.
- **As $x \to -\infty$**: Dominated by $-e^{-7x}$, so $f(x) \to -\infty$.

#### Question 4: $f(x) = 3e^{-x} - 8e^{-5x} - e^{10x}$

- **As $x \to +\infty$**: Dominated by $-e^{10x}$, so $f(x) \to -\infty$.
- **As $x \to -\infty$**: Dominated by $-8e^{-5x}$, so $f(x) \to -\infty$.

#### Question 5: $f(x) = \frac{e^{-3x} - 2e^{8x}}{9e^{8x} - 7e^{-3x}}$

- **As $x \to +\infty$**: $f(x) \to -\frac{2}{9}$.
- **As $x \to -\infty$**: $f(x) \to -\frac{1}{7}$.

#### Question 6: $f(x) = \frac{e^{-7x} - 2e^{3x} - e^{x}}{e^{-x} + 16e^{10x} + 2e^{-4x}}$

- **As $x \to +\infty$**: $f(x) \to 0$.
- **As $x \to -\infty$**: $f(x) \to +\infty$.

### Main Lesson: Identifying the Leading Term

- **Variable in the base (e.g., Question 2)**: For $f(x) = e^{\frac{6x^2 + x}{5 + 3x}}$, apply leading term analysis to the polynomials in the exponent. The leading terms are $6x^2$ (numerator) and $3x$ (denominator), so the exponent becomes $\frac{6x^2}{3x} = 2x$. Then evaluate $e^{2x}$ based on the direction of $x$.
- **Variable in the exponent (e.g., Questions 3–6)**: For $f(x) = 2e^{6x} - e^{-7x} - 10e^{4x}$, the leading term depends on the sign of the exponent and the direction of $x$:
  - As $x \to +\infty$, terms with positive exponents dominate (e.g., $e^{6x}$ with the largest exponent $6x$).
  - As $x \to -\infty$, terms with negative exponents dominate (e.g., $e^{-7x}$).
- **Key Difference**: When $x$ is in the base, use polynomial leading term analysis inside the exponent. When $x$ is in the exponent, focus on the sign and magnitude of the exponents, determined by the direction of $x$.

### Limits of $g(z) = 7 + 8z + \sqrt{z^{4/3}}$

## Initial Misconception
I thought $\sqrt{z^{4/3}}$ was the dominant term, leading to limits of $+\infty$ in both directions due to its even power.

## Corrected Analysis
- **Dominant Term**: $8z$ (degree 1) dominates over $\sqrt{z^{4/3}}$ (degree $\frac{4}{3} \div 2 = \frac{2}{3}$).
- **Limits**:
  - $\lim_{z \to \infty} g(z) = +\infty$.
  - $\lim_{z \to -\infty} g(z) = -\infty$.
- **Range**: $(-\infty, \infty)$, as $g(z)$ is continuous and unbounded.

---

## 2. Asymptotes: Definitions and Methods

#### Methods to Find Asymptotes
- **Vertical Asymptotes**: Substitute $x$ values where the function is undefined (e.g., division by 0 in rational expressions).
- **Horizontal Asymptotes**:
  - **Limit Method**: Evaluate $\lim_{x \to \pm \infty} f(x)$. If the limit is a finite value, that’s the horizontal asymptote.
  - **Substitution Method**: Redefine $x$ in terms of $y$, then let $y \to \pm \infty$.

#### Success of Leading-Term Analysis
For the equation $2yx^4 = 4x^7$:
- **Limit Method**: Already determined limits as $x \to \pm \infty$, so no need to analyze the inverse function.
- **Factoring Method**:
  - Rewrite: $x^7 \left( \frac{2}{x^3} y - 4 \right) = 0$.
  - Ignore $x^7$, solve: $\frac{2}{x^3} y - 4 = 0$, so $y = 2x^3$.
  - Inverse: $x = \sqrt[3]{\frac{y}{2}}$.
  - Simplified: From $2yx^4 = 4x^7$, reduce to $2y = 4x^3$, so $x = \sqrt[3]{\frac{y}{2}}$.
- **Range of Inverse**: The cube root has a range of all real numbers, confirming the values of $y$ for which $x$ is undefined.

#### Dividing by $x$
- **Question**: Why can we divide by $x$ when finding asymptotes?
- **Answer**: Asymptotes describe tendencies as $x \to \pm \infty$, so $x = 0$ is irrelevant. We focus on large $|x|$, making division by $x$ safe.

#### Trigonometric Functions
- **Note**: When finding inverse trigonometric functions, reintroduce periodicity to preserve the correct structure.

### Asymptotes and Range Misconception

#### Misconception
I assumed that no horizontal asymptote meant the range is all real numbers.

#### Correction
- **Clarification**: The absence of an asymptote only means no asymptote exists, not that the range is all real numbers.
- **Example**: Functions may tend to one side of infinity without an asymptote (e.g., $x^2$, range $[0, \infty)$).

#### Application
- **$g(z)$**: No horizontal asymptotes, range $(-\infty, \infty)$.
- **$f(x)$**: Horizontal asymptotes at $\pm \frac{3}{2}$, range $(-\infty, \infty)$ due to vertical asymptote at $x = \frac{1}{2}$.

---

## 3. Square Root Definition and Polarity

### Clarification
- **Definition**: $\sqrt{x^2} = |x|$, not $x$, because the square root always outputs a positive value.

#### Misconception in Evaluating $f(x) = \frac{\sqrt{7 + 9x^2}}{1 - 2x}$
- **Mistake**: I tried to rewrite the denominator $1 - 2x$ as $\sqrt{(1 - 2x)^2}$, thinking $a = \sqrt{a^2}$, but this changes the function since $\sqrt{(1 - 2x)^2} = |1 - 2x|$.
- **Correction**: Since $\sqrt{a^2} = |a|$, $a = \sqrt{a^2}$ or $a = -\sqrt{a^2}$, depending on polarity. For $1 - 2x$, which is negative for large $x$, I should have used $-\sqrt{(1 - 2x)^2}$.

#### Reflection
- **Surprise**: I hadn’t caught this before calculus, questioning the comprehensiveness of my resources (Paul’s Math Notes).
- **Resolution**: I’ll write square roots as moduli (e.g., $\sqrt{x^2} = |x|$) and simplify to $x$ or $-x$ as needed, advocating for earlier, rigorous education.

#### Faster Method Using Leading-Term Analysis
- **Method**: Avoid radicals in the denominator. For $f(x)$:
  - Numerator: $\sqrt{7 + 9x^2} \sim 3|x|$.
  - Denominator: $1 - 2x \sim -2x$.
  - Simplified: $\frac{3|x|}{-2x}$.
  - Limits: $\frac{3x}{-2x} = -\frac{3}{2}$ as $x \to \infty$, $\frac{3(-x)}{-2x} = \frac{3}{2}$ as $x \to -\infty$.
- **Benefit**: Skips quadratic expansion, reducing complexity.

#### Importance of Polarity in Leading-Term Analysis
- **Note**: When using leading-term analysis, carry the polarity of the highest term, not just its magnitude.

---

## 4. Learning Reflections and Goals

#### Self-Reflection
- **Foundation Gaps**: I was shocked to find gaps in my foundational knowledge (e.g., square root definition), despite my best efforts.
- **Comparison with Peers**: My math-savvy friends excel due to passion, practice, and rigorous training (e.g., Olympiads). I feel slower but have time, interest, and motivation to improve before university.
- **Natural Ability**: Natural skill amplifies both success and errors, like a fast RAM needing a smart program. Slow learners develop efficient strategies out of necessity.

#### Having a Growth Mindset

#### Revised Goals
- **Math Focus**: Complete calculus via Paul’s Math Notes, then study linear algebra, discrete math, combinatorics, sequences and series, and vectors.
- **Coding**: Incorporate small projects to build a portfolio for my computer science major, using iterative coding to overcome perfectionism.
- **Advanced Learning**: Consider Olympiad-level math and geometric proofs to develop rigorous thinking.

#### Perfectionism Challenge
- **Issue**: I seek perfect understanding, preferring math over coding because I aim for clean code on the first try.
- **Solution**: Adopt iterative coding to balance perfectionism with progress.

---

## 5. Rationalization Preferences

#### Initial Question
I questioned whether final answers should be rationalized (e.g., $\frac{1}{\sqrt{2}} \to \frac{\sqrt{2}}{2}$), unsure why rationalization is preferred despite my training.

#### Conditional Strategy
- **Initial Rule**: Rationalize only if the answer is needed for subsequent questions; otherwise, leave it unrationalized.

#### Revised Preference
- **Preference**: I prefer rationalized forms due to familiarity (e.g., $\sin 45^\circ = \frac{\sqrt{2}}{2}$) and because multiplication is simpler than division.
- **Conclusion**: Rationalizing makes sense to move the irrational part to the numerator.

---

## 6. Behavior of $x$ in Numerator vs. Denominator

#### Observation
- **Denominator**: If $x$ is in the denominator (e.g., $\frac{1}{x}$), the limit is 0 as $x \to \pm \infty$, regardless of polarity.
- **Numerator**: If $x$ is in the numerator, the limit diverges to $\pm \infty$, and polarity matters.

#### Application
- **$g(z)$**: $8z$ in the numerator, limits $\pm \infty$.
- **$f(x)$**: Degrees match, finite limits $\pm \frac{3}{2}$.

---

## 7. Square Roots and Opposite Limits

#### Observation
Expressions with square roots (e.g., $\sqrt{x^2} = |x|$) often lead to opposite limits as $x \to \pm \infty$, due to the absolute value changing behavior based on $x$’s sign.

#### Application
- **$g(z)$**: Limits driven by $8z$, not the square root term.
- **$f(x)$**: Limits $\pm \frac{3}{2}$, reflecting $\sqrt{9x^2} = 3|x|$.

---

### Insights from Problems 14–17

#### Problem 14: $f(x) = \frac{\sqrt{9x^4 + 2x^2 + 3}}{5x - 2x^2}$
- **Limits**: As $x \to \pm \infty$, $f(x) \approx \frac{\sqrt{9x^4}}{-2x^2} = \frac{3x^2}{-2x^2} = -\frac{3}{2}$.
- **Insight**: Even powers under square roots (e.g., $\sqrt{9x^4} = 3x^2$) simplify without modulus.

#### Problem 15: $f(x) = \frac{6 + x^3}{\sqrt{8 + 4x^6}}$
- **Limits**:
  - As $x \to \infty$, $f(x) \approx \frac{x^3}{\sqrt{4x^6}} = \frac{x^3}{2x^3} = \frac{1}{2}$.
  - As $x \to -\infty$, $f(x) \approx \frac{x^3}{2|x|^3} = -\frac{1}{2}$.
- **Insight**: Odd powers in the numerator with even roots in the denominator depend on polarity.

#### Problem 16: $f(x) = \frac{\sqrt[3]{2 - 8x^3}}{4 + 7x}$
- **Limits**: As $x \to \pm \infty$, $f(x) \approx \frac{\sqrt[3]{-8x^3}}{7x} = \frac{-2x}{7x} = -\frac{2}{7}$.
- **Insight**: Odd roots (cube root) preserve the sign, simplifying analysis.

#### Problem 17: $f(x) = \frac{1 + x}{\sqrt[4]{5 + 2x^4}}$
- **Limits**:
  - As $x \to \infty$, $f(x) \approx \frac{x}{\sqrt[4]{2x^4}} = \frac{1}{\sqrt[4]{2}}$.
  - As $x \to -\infty$, $f(x) \approx \frac{-|x|}{\sqrt[4]{2} \cdot |x|} = -\frac{1}{\sqrt[4]{2}}$.
- **Rationalization**: $\frac{1}{\sqrt[4]{2}} = \frac{\sqrt[4]{8}}{2}$, and similarly for the negative case.
- **Insight**: Even roots require modulus, rationalization aligns with my preference.

---

## 8. Rationalizing a 4th Root Denominator

#### Problem
Rationalize $\frac{1}{\sqrt[4]{2}}$.

#### Solution
- Multiply by $(\sqrt[4]{2})^3$:
  $
  \frac{1}{\sqrt[4]{2}} \times \frac{(\sqrt[4]{2})^3}{(\sqrt[4]{2})^3} = \frac{(\sqrt[4]{2})^3}{(\sqrt[4]{2})^4} = \frac{\sqrt[4]{8}}{2}
  $

#### Fallacy
- **Mistake**: I interpreted “multiply by 3 more times” as $3 \cdot \sqrt[4]{2}$ (addition), but meant $(\sqrt[4]{2})^3$ (exponentiation).
- **Correction**: “Times” refers to repeated multiplication, i.e., exponentiation.

#### General Method
For $\frac{1}{\sqrt[n]{a}}$, multiply by $(\sqrt[n]{a})^{n-1}$ to get $\frac{\sqrt[n]{a^{n-1}}}{a}$.

## 9. Logarithm Behavior

- For $\ln(y)$:
  - If $y \to 0^+$, then $\ln(y) \to -\infty$.
  - If $y \to \infty$, then $\ln(y) \to \infty$.
  - If $y \to 1$, then $\ln(y) \to 0$.

#### Logarithm Simplification

- Simplify $\ln(8)$ to $3\ln(2)$ in academic settings to show understanding of properties like $\ln(a^b) = b \ln(a)$, unless numerical computation is required or simplification adds no value.

---

## 10. Arctangent and Arccotangent Properties

- **Arctangent** $\tan^{-1}(x)$:
  - Range: $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$.
  - As $x \to +\infty$, $\tan^{-1}(x) \to \frac{\pi}{2}$; as $x \to -\infty$, $\tan^{-1}(x) \to -\frac{\pi}{2}$.
- **Arccotangent** $\cot^{-1}(x)$:
  - Range: $(0, \pi)$.
  - As $x \to +\infty$, $\cot^{-1}(x) \to 0$; as $x \to -\infty$, $\cot^{-1}(x) \to \pi$.

#### Visualization of $\tan^{-1}$ and $\cot^{-1}$

- **$\tan^{-1}(x)$**: S-shaped curve, passes through $(0, 0)$, approaches $y = \frac{\pi}{2}$ as $x \to +\infty$, $y = -\frac{\pi}{2}$ as $x \to -\infty$.
- **$\cot^{-1}(x)$**: Decreasing curve, from $y = \pi$ as $x \to -\infty$ to $y = 0$ as $x \to +\infty$, crosses $y = \frac{\pi}{2}$ at $x = 0$.

---

## Limit Evaluations and Visualization of Inverse Trigonometric Functions

We evaluate limits involving logarithms and arctangent functions and reinforce the visualization of $\tan^{-1}$ and $\cot^{-1}$ graphs.

## Visualization of $\tan^{-1}$ and $\cot^{-1}$ (Mental Picture)

### Arctangent: $y = \tan^{-1}(x)$

- **Shape**: S-shaped curve, flattened at the top and bottom.
- **Range**: $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ (from $-1.57$ to $1.57$).
- **Key Points**:
  - At $x = 0$, $y = 0$.
  - At $x = 1$, $y = \frac{\pi}{4} \approx 0.785$.
  - At $x = -1$, $y = -\frac{\pi}{4} \approx -0.785$.
- **Asymptotes**:
  - As $x \to +\infty$, $y \to \frac{\pi}{2} \approx 1.57$.
  - As $x \to -\infty$, $y \to -\frac{\pi}{2} \approx -1.57$.
- **Mental Picture**: Starts at $(0, 0)$, rises gently to $(1, \frac{\pi}{4})$, flattens near $y = \frac{\pi}{2}$ as $x$ increases; dips symmetrically to $(-1, -\frac{\pi}{4})$, flattens near $y = -\frac{\pi}{2}$ as $x$ decreases.

### Arccotangent: $y = \cot^{-1}(x)$

- **Shape**: Decreasing curve, high on the left, low on the right.
- **Range**: $(0, \pi)$ (from 0 to $3.14$).
- **Key Points**:
  - At $x = 0$, $y = \frac{\pi}{2} \approx 1.571$.
  - At $x = 1$, $y = \frac{\pi}{4} \approx 0.785$.
  - At $x = -1$, $y = \frac{3\pi}{4} \approx 2.356$.
- **Asymptotes**:
  - As $x \to +\infty$, $y \to 0$.
  - As $x \to -\infty$, $y \to \pi \approx 3.14$.
- **Mental Picture**: Starts near $y = \pi$ on the left, decreases through $(-1, \frac{3\pi}{4})$, $(0, \frac{\pi}{2})$, $(1, \frac{\pi}{4})$, and flattens near $y = 0$ as $x$ increases.

## Previous Lessons (Recap)

- **Logarithm Simplification**: Simplify $\ln(8)$ to $3\ln(2)$ in academic settings unless numerical computation is required.
- **Logarithm Behavior**: For $\ln(y)$, if $y \to 0^+$, $\ln(y) \to -\infty$; if $y \to \infty$, $\ln(y) \to \infty$; if $y \to 1$, $\ln(y) \to 0$.
- **Leading Term Analysis**:
  - Variable in the base: Compare highest-degree terms.
  - Variable in the exponent: Leading term depends on the sign of the exponent and direction of $x$.

## Resolving Discrepancy in Discontinuities of $\tan(2x)$

We address the discrepancy in the solution’s presentation of discontinuities for $g(x) = \tan(2x)$.

#### Discrepancy Analysis

- **Correct Discontinuities**:
  - $\cos(2x) = 0 \implies 2x = \frac{\pi}{2} + m\pi \implies x = \frac{\pi}{4} + \frac{m\pi}{2}$, $m \in \mathbb{Z}$, matching the direct approach using the period $\frac{\pi}{2}$.
- **Solution’s Presentation**:
  - Split into $x = \frac{\pi}{4} + \pi n$ or $x = \frac{3\pi}{4} + \pi n$, $n \in \mathbb{Z}$.
  - The period $\pi$ in each sequence covers all points when combined, as the two sequences are offset by $\frac{\pi}{2}$.
- **Resolution**:
  - The solution’s form is equivalent to $x = \frac{\pi}{4} + \frac{m\pi}{2}$, but less intuitive due to the split and use of $\pi n$ instead of $\frac{\pi}{2} n$.

#### Lesson Learned: Importance of Fundamental Period

- **Direct Approach**: Use the fundamental period of $\tan(kx)$, which is $\frac{\pi}{k}$, to directly find discontinuities.
- **Solution’s Approach**: Splitting into two sequences with a larger period can work but is less clear; always simplify to the fundamental period for clarity.

## Discontinuities of Trigonometric Functions

We analyze the discontinuities of trigonometric functions and note the use of the inverse for the secant function.

#### Trigonometric Discontinuities

- **Problem 17: $f(x) = \frac{4x + 1}{5 \cos\left(\frac{x}{2}\right) + 1}$**:
  - Discontinuous where $5 \cos\left(\frac{x}{2}\right) + 1 = 0 \implies x = \pm 2 \arccos\left(-\frac{1}{5}\right) + 4\pi n$, $n \in \mathbb{Z}$.
- **Problem 18: $h(x) = \frac{1 - x}{x \sin(x - 1)}$**:
  - Discontinuous where $x \sin(x - 1) = 0 \implies x = 0$ or $x = 1 + \pi n$, $n \in \mathbb{Z}$.
- **Problem 21: $g(x) = \cot(4x)$**:
  - Discontinuous where $\sin(4x) = 0 \implies x = \frac{\pi n}{4}$, $n \in \mathbb{Z}$.
- **Problem 22: $f(t) = \sec(\sqrt{t})$**:
  - Discontinuous where $\cos(\sqrt{t}) = 0 \implies \sqrt{t} = \frac{\pi}{2} + \pi n \implies t = \left(\frac{\pi}{2} + \pi n\right)^2$, $n = 0, 1, 2, \ldots$ (since $t \geq 0$).
  - **Note on Inverse**: Solve $\cos(\sqrt{t}) = 0$ using $\arccos(0) = \frac{\pi}{2}$, add $\pi n$ for periodicity, then square to find $t$, respecting the domain.

#### Lesson Learned

- **Trigonometric Discontinuities**: Occur where the denominator (e.g., $\sin$, $\cos$) is zero, adjusted for periodicity.
- **Secant and Inverse**: Rewrite $\sec$ as $\frac{1}{\cos}$, solve using the inverse cosine, and ensure domain constraints are met.

## 11. Continuity of Polynomials: A Deliberate Construction

We explore why polynomials are continuous everywhere due to their construction from continuous operations.

#### Understanding Continuity of Polynomials

- **Building Blocks**:
  - Constants ($f(x) = c$) are continuous: $\lim_{x \to a} c = c$.
  - The identity function $f(x) = x$ is continuous: $\lim_{x \to a} x = a$.
  - Power functions $x^n$ are continuous, as they are products of $x$ with itself $n$ times, and products of continuous functions are continuous.
- **Operations**:
  - Multiplication by a constant (e.g., $a_k x^k$) preserves continuity.
  - Addition of terms (e.g., $a_n x^n + \cdots + a_0$) preserves continuity, as the sum of continuous functions is continuous.
- **Deliberate Choice**: Polynomials are constructed from continuous functions (constants, powers of $x$) using only addition and multiplication, which preserve continuity, ensuring no discontinuities arise.


- **Proof of Polynomial Continuity**: For $p(x) = a_n x^n + \cdots + a_0$, $\lim_{x \to a} p(x) = p(a)$ by applying limit laws term by term, confirming continuity everywhere.
- **Continuity of Rational Functions**: A rational function $\frac{p(x)}{q(x)}$ is continuous where $q(x) \neq 0$.

## 12. Significance of the Intermediate Value Theorem

We explore the Intermediate Value Theorem (IVT) and why it’s significant despite seeming obvious.

### Intermediate Value Theorem

- **Statement**: If $f(x)$ is continuous on $[a, b]$ and $M$ is between $f(a)$ and $f(b)$, then there exists $c \in [a, b]$ such that $f(c) = M$.
- **Intuition**: A continuous function takes all values between $f(a)$ and $f(b)$ as $x$ moves from $a$ to $b$.

#### Why It Seems Obvious

- Continuous functions have no breaks, so they must pass through every y-value between $f(a)$ and $f(b)$, making the IVT feel intuitive.

#### Why It’s Significant

- **Existence**: Guarantees a $c$ exists without specifying how to find it, useful in proofs (e.g., root finding).
- **Continuity**: Only holds for continuous functions, emphasizing the role of continuity.
- **Applications**: Used in root finding (e.g., bisection method), real-world problems (e.g., speed, stock prices), and as a foundation for other theorems.
- **Generality**: Applies to all continuous functions on closed intervals, not just simple ones.

## Confirming IVT Application on Smallest Intervals

We apply the IVT by breaking intervals into the smallest continuous subintervals and checking for sign changes, concluding if a root exists

#### Solutions

- **Problem 31: $f(-4) = -10$, $f(5) = 17$, $\lim_{x \to 1^-} f(x) = -2$, $\lim_{x \to 1^+} f(x) = 4$ on $[-4, 5]$**:
  - Subintervals: $[-4, 1)$, $(1, 5]$.
  - $[-4, 1)$: $f(-4) < 0$, $\lim_{x \to 1^-} f(x) < 0$, no sign change.
  - $(1, 5]$: $\lim_{x \to 1^+} f(x) > 0$, $f(5) > 0$, no sign change.
  - Across $x = 1$: Sign change, but discontinuous.
  - Conclusion: A root likely exists in $[-4, 5]$ based on overall sign change.

- **Problem 32: $f(-8) = 2$, $f(1) = 23$, $\lim_{x \to -4^-} f(x) = 35$, $\lim_{x \to -4^+} f(x) = 1$ on $[-8, 1]$**:
  - Subintervals: $[-8, -4)$, $(-4, 1]$.
  - $[-8, -4)$: $f(-8) > 0$, $\lim_{x \to -4^-} f(x) > 0$, no sign change.
  - $(-4, 1]$: $\lim_{x \to -4^+} f(x) > 0$, $f(1) > 0$, no sign change.
  - Conclusion: No root in $[-8, 1]$ via IVT.

- **Problem 33: $f(0) = -1$, $f(9) = 10$, $\lim_{x \to 2^-} f(x) = -12$, $\lim_{x \to 2^+} f(x) = -3$ on $[0, 9]$**:
  - Subintervals: $[0, 2)$, $(2, 9]$.
  - $[0, 2)$: $f(0) < 0$, $\lim_{x \to 2^-} f(x) < 0$, no sign change.
  - $(2, 9]$: $\lim_{x \to 2^+} f(x) < 0$, $f(9) > 0$, sign change.
  - Conclusion: A root exists in $(2, 9] \subset [0, 9]$.

## 13. The Power of "Duh" Theorems in Mathematics

We reflect on the significance of "obvious" theorems like the Intermediate Value Theorem (IVT) and Squeeze Theorem.

#### Comparison: IVT and Squeeze Theorem

- **Squeeze Theorem**: If $g(x) \leq f(x) \leq h(x)$ near $a$ and $\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$, then $\lim_{x \to a} f(x) = L$. Used for determining limits.
- **IVT**: If $f(x)$ is continuous on $[a, b]$ and $M$ is between $f(a)$ and $f(b)$, then there exists $c \in [a, b]$ such that $f(c) = M$. Used for continuity checks and existence.
- **Similarity**: Both seem intuitive but are powerful when logic is complex.

#### Why "Duh" Theorems Are Clutch

- **Bridge Intuition and Rigor**: Formalize intuitive ideas into rigorous tools.
- **Handle Edge Cases**: Solve problems where direct methods fail (e.g., oscillatory limits, existence of roots).
- **Foundation**: Enable advanced results (e.g., Mean Value Theorem, limit evaluations).
- **Catch Mistakes**: Ensure we don’t miss obvious properties (e.g., continuity, boundedness).
- **Clutch in Proofs**: Provide reliable tools when logic is pushed to the limit (e.g., proving existence, convergence).

#### Reflection: Importance of the Obvious

- "Duh" theorems are often missed but become critical in complex problems, grounding our reasoning in fundamental properties.
