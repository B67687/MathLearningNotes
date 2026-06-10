---
title: "Understanding the Epsilon-Delta Definition, Limits, Continuity, and Polynomials"
source_notebook: "calculus/advancements-report-20th-march-2025.ipynb"
archived_notebook: "archive/notebooks/calculus/advancements-report-20th-march-2025.ipynb"
original_human_author: B67687
conversion: exported from original notebook
canonical_status: markdown-mirror
---

# Understanding the Epsilon-Delta Definition, Limits, Continuity, and Polynomials

## Introduction

This notebook provides a comprehensive summary of the epsilon-delta definition of a limit, addressing key concepts, distinctions, and common challenges.

# 1. The Epsilon-Delta (E.D.) Definition of a Limit

### The Epsilon-Delta Definition

The epsilon-delta definition of a limit states:

For a function $f(x)$ defined on an open interval containing $a$ (except possibly at $a$), the limit of $f(x)$ as $x$ approaches $a$ is $L$, written as:

$$
\lim_{x \to a} f(x) = L
$$

if and only if for every $\epsilon > 0$, there exists a $\delta > 0$ such that if $0 < |x - a| < \delta$, then $|f(x) - L| < \epsilon$.

## The Logic of the Definition

The epsilon-delta definition formalizes the idea of a function approaching a limit. It states that for any desired level of closeness to the limit ($\epsilon$), we can find a neighborhood around the input value ($a$) such that all points in that neighborhood (except possibly $a$ itself) map to function values within the desired closeness to the limit ($L$).

In simpler terms:

-   You give me a target accuracy ($\epsilon$).
-   I need to show you that I can make the function's output meet that accuracy by restricting the input to a small enough neighborhood around $a$ ($\delta$).

## Why the Different Conditions for $\epsilon$ and $\delta$?
- **$\delta$: Input Condition: $0 < |x - a| < \delta$**:
  - The $0 < |x - a|$ ensures $x \neq a$, because the limit is about the behavior of $f(x)$ as $x$ approaches $a$ from either side, not at $x = a$.
  - This is necessary to exclude $f(a)$, which may not equal $L$ or may be undefined.
- **$\epsilon$: Output Condition: $|f(x) - L| < \epsilon$**:
  - We don’t need $0 < |f(x) - L|$ because the limit only requires $f(x)$ to be close to $L$, and $f(x) = L$ (i.e., $|f(x) - L| = 0$) is acceptable.
  - The limit doesn’t evaluate $f$ at $x = a$, but in the interval $0 < |x - a| < \delta$, $f(x)$ may equal $L$ at some points, and that’s allowed.

## What does this imply for finding the limit:
- **$ L $: Existence of the Limit**:
    - If the limit exists, for any $\epsilon > 0$, we can find a $\delta > 0$ that satisfies the condition. If there exists some $\epsilon > 0$ for which no $\delta$ works, the limit does not exist.

### Why Is $0 < |f(x) - L| < \epsilon$ Too Restrictive?
- **Over-Restricting the Output**:
  - Requiring $0 < |f(x) - L| < \epsilon$ means $f(x) \neq L$ for all $x$ in $0 < |x - a| < \delta$, which restricts the overall tendency of $f(x)$.
  - This invalidates functions that oscillate toward $L$, such as $f(x) = x \sin(1/x)$ at $x = 0$, which equals $0$ at some points but still tends to $0$.

- **Examples**:
  - **Constant Function**: $f(x) = 2$, $\lim_{x \to 1} 2 = 2$. $|f(x) - 2| = 0$, so $0 < |f(x) - L|$ fails.
  - **Oscillatory Function**: $f(x) = x \sin(1/x)$ at $x = 0$. At $x = 1/(\pi k)$, $f(x) = 0$, so $|f(x) - 0| = 0$, violating $0 < |f(x) - L|$, but the limit is $0$.
  - **Polynomial**: $f(x) = (x - 1)^2$ at $x = 2$, limit is $1$. At $x = 0$, $f(0) = 1$, so $|f(0) - 1| = 0$, violating $0 < |f(x) - L|$.

- **Conclusion**: The standard condition $|f(x) - L| < \epsilon$ allows $f(x) = L$, capturing the true tendency of $f(x)$ without invalidating functions that oscillate or hit $L$ near $a$.

## Real-Life Analogy: $\sin(1/x)$ and Quantum Superposition
- $\sin(1/x)$ oscillates between $-1$ and $1$ as $x \to 0$, so the limit doesn’t exist.
- Analogized this to quantum superposition, where a system exists in multiple states simultaneously.
- In calculus, however, a limit requires convergence to a single value, so $\sin(1/x)$ has no limit at $x = 0$.

# 2. Logics of the Definition

## Why the E.D. Definition Is Unidirectional
- **Unidirectional Implication**:
  - The e.d. definition uses a unidirectional implication: $(0 < |x - a| < \delta) \implies (|f(x) - L| < \epsilon)$.
  - This means: if $x$ is close to $a$, then $f(x)$ must be close to $L$. It focuses on the behavior of $f(x)$ when $x$ is near $a$.
- **Why Not Bidirectional ($\iff$)?**:
  - A bidirectional condition would require: $(0 < |x - a| < \delta) \iff (|f(x) - L| < \epsilon)$.
  - The converse ($|f(x) - L| < \epsilon \implies 0 < |x - a| < \delta$) means all $x$ where $|f(x) - L| < \epsilon$ must have $0 < |x - a| < \delta$.
  - **Example**: For $f(x) = x \sin(1/x)$ at $x = 0$, $\epsilon = 0.01$, $\delta = 0.01$:
    - $|x \sin(1/x)| < 0.01$ holds for $|x| < 0.01$, but also at $x = 1/(\pi k)$, e.g., $x = 1/\pi \approx 0.318$.
    - The converse fails because $x = 1/\pi$ has $|f(x)| = 0 < 0.01$, but $0 < |x| < 0.01$ is false.
  - **Problem**: The converse is too restrictive—it requires all $x$ where $f(x) \approx L$ to be near $a$, but functions can be close to $L$ far from $a$.
- **Conclusion**: The unidirectional implication ensures the limit only cares about $x$ values near $a$, making it general enough for all functions, including oscillatory ones.

## Can We Replace "Whenever" with $\land$ to Determine the Limit?
- **Proposed Statement**: Replace "whenever" in $|x^2 - 0| < \epsilon$ whenever $0 < |x - 0| < \delta$ with $\land$, so it becomes $(|x^2| < \epsilon) \land (0 < |x| < \delta)$.
- **Proposed Conclusion**:
  - If the statement is true, the limit exists.
  - If the statement is false, the limit does not exist (DNE).
- **Why This Doesn’t Work**:
  - The e.d. definition uses an implication: $(0 < |x| < \delta) \implies (|x^2| < \epsilon)$, which must hold for all $x$, and there must exist a $\delta$ for every $\epsilon$.
  - Using $\land$ creates a conjunction for a specific $x$. The statement’s truth for one $x$ doesn’t tell us if the implication holds for all $x$.
  - **Example**: For $f(x) = x^2$, $\epsilon = 0.01$, $\delta = 0.1$:
    - At $x = 0.05$: $(0.05^2 < 0.01) \land (0 < 0.05 < 0.1)$ is true.
    - At $x = 0.2$: $(0.2^2 < 0.01) \land (0 < 0.2 < 0.1)$ is false (because $0.2 < 0.1$ is false).
    - The truth value depends on $x$, but the e.d. definition requires the implication to hold for all $x$ in the interval.
  - **Conclusion**: Evaluating the $\land$ statement for specific $x$ values doesn’t determine the limit’s existence. We must check the implication for all $x$ and ensure a $\delta$ exists for every $\epsilon$.

## Writing the E.D. Definition in Logical Form
- **Statement**: $|x^2 - 0| < \epsilon$ whenever $0 < |x - 0| < \delta$ (for $\lim_{x \to 0} x^2 = 0$).
- **Implication**: The "whenever" means an implication:
  $
  (0 < |x| < \delta) \implies (|x^2| < \epsilon).
  $
- **For All $x$**: The implication must hold for all $x$:
  $
  \forall x, (0 < |x| < \delta) \implies (|x^2| < \epsilon).
  $
- **Full E.D. Definition**: Add the quantifiers for $\epsilon$ and $\delta$:
  $
  \forall \epsilon > 0, \exists \delta > 0, \forall x, (0 < |x| < \delta) \implies (|x^2| < \epsilon).
  $
- **Limit Statement**:
  $
  \lim_{x \to 0} x^2 = 0 \iff \forall \epsilon > 0, \exists \delta > 0, \forall x, (0 < |x| < \delta) \implies (|x^2| < \epsilon).
  $
- **Verification**: For $f(x) = x^2$, choose $\delta = \sqrt{\epsilon}$. The implication holds for all $x$, so the limit is $0$.

## Preserving the Order of the Original Statement
- **Original Order**: The statement $|x^2 - 0| < \epsilon$ whenever $0 < |x - 0| < \delta$ has the input condition ($0 < |x| < \delta$) leading to the output condition ($|x^2| < \epsilon$).
- **Logical Form**: The implication $(0 < |x| < \delta) \implies (|x^2| < \epsilon)$ preserves this order:
  - The "if" part ($0 < |x| < \delta$) comes first.
  - The "then" part ($|x^2| < \epsilon$) comes second.
- **Quantifiers**: The $\forall \epsilon > 0, \exists \delta > 0, \forall x$ are added before the implication to provide context, but they don’t change the order of the core "whenever" relationship.

## Does the Implication Indicate Direction of Causation?
- **Implication as Logical Dependency**:
  - The implication $(0 < |x| < \delta) \implies (|x^2| < \epsilon)$ means: if the input condition is true, the output condition must be true.
  - In this context, it’s a form of "mathematical causation": the input constraint ($x$ being close to $0$) forces the output ($x^2$ being close to $0$).
  - However, in logic, $\implies$ is about truth values, not physical causation: it ensures that whenever the input condition holds, the output condition holds.
- **Direction**: The arrow $\implies$ indicates the direction of this dependency: from the input to the output, matching the "whenever" in the original statement.

## Does $b$ Being True Imply $a$ Is True?
- **Question**: In $a \implies b$, if $b$ is true, does that mean $a$ is true?
- **Answer**: No.
- **Truth Table for Implication**:
  \
  \begin{array}{|c|c|c|}
  \hline
  a & b & a \implies b \\
  \hline
  \text{True} & \text{True} & \text{True} \\
  \text{True} & \text{False} & \text{False} \\
  \text{False} & \text{True} & \text{True} \\
  \text{False} & \text{False} & \text{True} \\
  \hline
  \end{array}

- **Explanation**:
  - Let $a$: $0 < |x| < \delta$, $b$: $|x^2| < \epsilon$.
  - The implication $(0 < |x| < \delta) \implies (|x^2| < \epsilon)$ means: if $a$ is true, then $b$ must be true.
  - **When $a$ is False**:
    - If $a$ is false (e.g., $|x| \geq \delta$ or $x = 0$), the implication is true regardless of $b$.
    - This is called "vacuous truth": since the premise $a$ isn’t satisfied, the implication can’t be violated.
    - Example: For $\epsilon = 0.01$, $\delta = 0.01$:
      - At $x = 0.05$: $a$: $0 < 0.05 < 0.01$ (False), $b$: $|0.05^2| = 0.0025 < 0.01$ (True). Implication: False $\implies$ True, which is True.
      - At $x = 0.2$: $a$: $0 < 0.2 < 0.01$ (False), $b$: $|0.2^2| = 0.04 < 0.01$ (False). Implication: False $\implies$ False, which is True.
  - **Why $a$ Being False Implies Both $b$ True and False**:
    - When $a$ is false, the implication $a \implies b$ is true by definition (vacuous truth), because the premise isn’t satisfied, and the implication can’t be violated.
    - This isn’t a contradiction: it reflects that the e.d. definition only cares about $x$ values where $a$ is true.
  - **Does $b$ Imply $a$?**:
    - If $b$ is true (e.g., $|x^2| < \epsilon$), $a$ doesn’t have to be true.
    - From the truth table: when $b$ is true, $a$ can be true (row 1) or false (row 3).
    - Example: At $x = 0.05$, $|x^2| < 0.01$ is true, but $0 < 0.05 < 0.01$ is false.
- **Conclusion**: $b$ being true doesn’t guarantee $a$ is true. The implication is unidirectional, and the converse ($b \implies a$) doesn’t hold.

# 3. Proving a Limit Using the Epsilon-Delta Definition

## Epsilon-Delta Limit Proof: Correct vs. Incorrect

**Correct Method (Standard Epsilon-Delta Definition)**

When proving a limit using the epsilon-delta definition, we must follow a specific structure:

1.  **State the Limit:** Clearly state the limit you want to prove (e.g., lim (x→a) f(x) = L).
2.  **Write the Full Definition:** Explicitly write the epsilon-delta definition:

    $$ \text{For all } ε > 0, \text{there exists a } δ > 0 \text{ such that if } 0 < |x - a| < δ, \text{ then } |f(x) - L| < ε $$

    $$\text{OR}$$

    $$∀ε > 0, ∃δ > 0 : 0 < |x - a| < δ ⇒ |f(x) - L| < ε $$


4.  **Find a Relationship Between δ and ε:** Manipulate the inequality |f(x) - L| < ε to find a relationship between |x - a| and ε. This involves finding a suitable δ in terms of ε.
5.  **Determine δ:** Choose δ based on the relationship you found. δ will typically be a function of ε.
6.  **Write the Formal Proof:** Show that if 0 < |x - a| < δ, then |f(x) - L| < ε, using the δ you found.
7.  **Conclude:** State that the limit exists.

**Why This Method Is Correct:**

-   **Clear Structure:** It follows the standard epsilon-delta definition.
-   **Explicit Quantifiers:** It clearly states the "for all ε" and "there exists δ" quantifiers, emphasizing the dependency of δ on ε.
-   **Correct Order:** It establishes the correct order of operations: for any ε, we find a suitable δ.
-   **Unidirectional Control:** It correctly shows the unidirectional control: input (δ) -> output (ε).
-   **Mathematical Rigor:** It adheres to mathematical conventions and ensures a rigorous proof.
-   **Explicit Generality:** The use of "for all ε" makes it clear that the limit must hold for *any* positive epsilon, not just a specific one.

**Incorrect Method (Your Original Representation)**

Your original representation in the image, while containing correct calculations, had the following flaws:

1.  **Separated Quantifiers:** You placed "∀ε > 0" and "δ > 0" separately above the right and left sides of the implication, respectively, instead of before the entire implication.
2.  **Lack of Explicit "There Exists":** You didn't explicitly write "there exists δ," suggesting that any δ > 0 would work.
3.  **Implied Bidirectionality:** Your representation implied a bidirectional relationship between δ and ε, which is not how limits work.

**Why This Method Is Incorrect:**

-   **Ambiguity:** It creates ambiguity about the relationship between δ and ε.
-   **Loss of Dependency:** It doesn't clearly show the dependency of δ on ε.
-   **Incorrect Control:** It suggests a general relationship or bidirectional control, which is not the essence of a limit.
-   **Deviation from Convention:** It deviates from the standard way of writing the epsilon-delta definition.
-   **Failure in Non-Uniform Convergence:** It would fail to accurately describe limits in cases where δ depends on x, not just ε.
-   **Lack of Explicit Generality:** "ε > 0" alone doesn't mean "for all ε > 0." It only states that ε is positive, not that the implication holds for *any* positive ε.

**In essence:**

Your calculations were correct, but the representation of the quantifiers and the implication lacked the clarity and rigor of the standard epsilon-delta definition. It didn't explicitly show the dependency of δ on ε, implied a bidirectional control, and failed to capture the generality of "for all ε > 0."

## Example of wrong definition (Input Positive Approach to Output Negative Infinity)
<img src="epsilon-delta-proof-wrong-definition-positive-approach-result-negative-infinity.jpg" width=430>

# Examples

## Polynomial

### $\lim_{x \to 1} (2x + 1) = 3$
- **Definition:** We want to show that for every $\epsilon > 0$, there exists a $\delta > 0$ such that if $0 < |x - 2| < \delta$, then $|x^2 - 4| < \epsilon$.
- Need: If $0 < |x - 1| < \delta$, then $|(2x + 1) - 3| < \epsilon$.
- Simplify: $|(2x + 1) - 3| = 2|x - 1|$.
- Require: $2|x - 1| < \epsilon \implies |x - 1| < \epsilon/2$.
- Choose $\delta = \epsilon/2$.
- **Stopping Here**: The transformation directly gives a $\delta$ for any $\epsilon > 0$, so the limit exists and is $3$. The relationship between $\epsilon$ and $\delta$ is not circular—it’s a direct functional dependence: $\delta$ is determined by $\epsilon$.

### $\lim_{x \to 2} x^2 = 4$

1.  **Definition:** We want to show that for every $\epsilon > 0$, there exists a $\delta > 0$ such that if $0 < |x - 2| < \delta$, then $|x^2 - 4| < \epsilon$.
2.  **Start with $\epsilon$:** Let $\epsilon > 0$ be given.
3.  **Find $\delta$:**
    -   We have $|x^2 - 4| = |(x - 2)(x + 2)| = |x - 2| |x + 2|$.
    -   Assume $|x - 2| < 1$. Then $-1 < x - 2 < 1$, so $3 < x < 5$, and $5 < x + 2 < 7$. Thus, $|x + 2| < 7$.
    -   We want $|x^2 - 4| < \epsilon$, so $|x - 2| |x + 2| < \epsilon$. Since $|x + 2| < 7$, we have $|x - 2| |x + 2| < 7|x - 2|$.
    -   If we choose $|x - 2| < \frac{\epsilon}{7}$, then $7|x - 2| < \epsilon$.
    -   Choose $\delta = \min\{1, \frac{\epsilon}{7}\}$.
4.  **Show the implication:**
    -   Suppose $0 < |x - 2| < \delta$.
    -   Since $\delta \le 1$, we have $|x - 2| < 1$, so $|x + 2| < 7$.
    -   Since $\delta \le \frac{\epsilon}{7}$, we have $|x - 2| < \frac{\epsilon}{7}$.
    -   Therefore, $|x^2 - 4| = |x - 2| |x + 2| < \frac{\epsilon}{7} \cdot 7 = \epsilon$.
5.  **Conclusion:** We have shown that for every $\epsilon > 0$, there exists a $\delta > 0$ such that if $0 < |x - 2| < \delta$, then $|x^2 - 4| < \epsilon$. Therefore, $\lim_{x \to 2} x^2 = 4$.

### $\lim_{x \to 1} x^4 = 1$

1.  **Definition:** We want to show that for every $\epsilon > 0$, there exists a $\delta > 0$ such that if $0 < |x - 1| < \delta$, then $|x^4 - 1| < \epsilon$.

2.  **Start with $\epsilon$:** Let $\epsilon > 0$ be given.

3.  **Find $\delta$:**
    - We have $|x^4 - 1| = |(x^2 - 1)(x^2 + 1)| = |(x - 1)(x + 1)(x^2 + 1)| = |x - 1| |x + 1| |x^2 + 1|$.
    - Assume $|x - 1| < 1$. Then $-1 < x - 1 < 1$, so $0 < x < 2$.
    - Thus, $1 < x + 1 < 3$, and $1 < x^2 < 4$, so $2 < x^2 + 1 < 5$. Therefore, $|x + 1| < 3$ and $|x^2 + 1| < 5$.
    - We want $|x^4 - 1| < \epsilon$, so $|x - 1| |x + 1| |x^2 + 1| < \epsilon$. Since $|x + 1| < 3$ and $|x^2 + 1| < 5$, we have $|x - 1| |x + 1| |x^2 + 1| < 15|x - 1|$.
    - If we choose $|x - 1| < \frac{\epsilon}{15}$, then $15|x - 1| < \epsilon$.
    - Choose $\delta = \min\{1, \frac{\epsilon}{15}\}$.

4.  **Show the implication:**
    - Suppose $0 < |x - 1| < \delta$.
    - Since $\delta \le 1$, we have $|x - 1| < 1$, so $|x + 1| < 3$ and $|x^2 + 1| < 5$.
    - Since $\delta \le \frac{\epsilon}{15}$, we have $|x - 1| < \frac{\epsilon}{15}$.
    - Therefore, $|x^4 - 1| = |x - 1| |x + 1| |x^2 + 1| < \frac{\epsilon}{15} \cdot 3 \cdot 5 = \epsilon$.

5.  **Conclusion:** We have shown that for every $\epsilon > 0$, there exists a $\delta > 0$ such that if $0 < |x - 1| < \delta$, then $|x^4 - 1| < \epsilon$. Therefore, $\lim_{x \to 1} x^4 = 1$.

# Worked Examples

## Constant
<img src="epsilon-delta-proof-constant.png" width=430>

## Normal Polynomial
<img src="epsilon-delta-proof-normal-polynomial.png" width=430>

## Multi-Factored Polynomial
<img src="epsilon-delta-proof-multi-factored-polynomial-normal-approach.png" width=430>

## Cube Root Rational Expression, Input Infinity
<img src="epsilon-delta-proof-cuberoot-rational-expression-input-approach-infinity.png" width=430>

## Input Positive Approach to Output Negative Infinity
<img src="epsilon-delta-proof-positive-approach-result-negative-infinity.png" width=430>

## Oscillatory


### $\lim_{x \to 0} \sin(1/x) = 0$
- Need: If $0 < |x| < \delta$, then $|\sin(1/x)| < \epsilon$.
- For $\epsilon = 0.5$, $\sin(1/x)$ oscillates between $-1$ and $1$ in any interval $(0, \delta)$.
- Since $|\sin(1/x)| = 1 > 0.5$ at some points, no $\delta$ works.
- The limit does not exist.

---

## Common Challenges and Misconceptions

-   **Confusing $\epsilon$ and $\delta$:** $\epsilon$ is related to the function's output, while $\delta$ is related to the input.
-   **Assuming $\epsilon = 0$ or $\delta = 0$:** Both $\epsilon$ and $\delta$ must be strictly positive.
-   **Not showing the dependence of $\delta$ on $\epsilon$:** A proper proof must demonstrate how $\delta$ is chosen based on $\epsilon$.
-   **Difficulty in finding $\delta$:** Finding the appropriate $\delta$ often requires algebraic manipulation and a good understanding of inequalities.
-   **Thinking the limit is about what happens *at* a point:** The limit is about the behavior of a function *near* a point.

## The Importance of Bounding

-   For functions more complex than linear ones, it's generally not possible to avoid some form of restriction or bounding argument.
-   This is because many functions have terms whose values depend on $x$.
-   To show that $|f(x) - L|$ can be made arbitrarily small, these terms need to be controlled.
-   The "assume $|x - a| < c$" step is a way to put a limit on how large these terms can be.

## Choosing the Restriction Constant

-   The choice of the constant (e.g., 1) in the restriction $|x - a| < \text{constant}$ is not unique.
-   It's a matter of strategy and convenience.
-   The goal is to find *a* $\delta$ that works, not necessarily the largest possible $\delta$.
-   Common choices like 1 often simplify calculations.
-   Other values would also lead to a valid proof.

## Bounding and Absolute Values

**Key Idea:** When you have an inequality of the form $a < x < b$, you can bound the absolute value of $x$, $|x|$, by the maximum of the absolute values of $a$ and $b$.

**In other words:** $|x| < \max(|a|, |b|)$.

**Example:**

We have $-3 < x + 1 < -1$.

To find a bound for $|x + 1|$, we take the absolute values of -3 and -1, which are 3 and 1, respectively.

The maximum of these is 3.

Therefore, $|x + 1| < 3$.

**Explanation:**

The inequality $-3 < x + 1 < -1$ means that $x + 1$ lies between -3 and -1 on the number line. The distance of $x + 1$ from zero is therefore less than the distance of -3 from zero.

# 4. Generalization of the Epsilon-Delta Restriction

###  The Standard Approach

In many epsilon-delta proofs, particularly when dealing with polynomials or rational functions, a common step involves introducing a temporary restriction of the form:

$$
|x - a| < 1
$$

where 'a' is the point at which the limit is being evaluated. This restriction is used to bound terms in the expression $|f(x) - L|$ that depend on 'x'.

### The Generalized Approach

A more general approach is to use an arbitrary positive constant 'c' instead of 1:

$$
|x - a| < c
$$

where $ c \in \mathbb R,  c > 0 $

### Why This Generalization Is Valid

1.  **Arbitrary Choice:** The epsilon-delta definition requires us to show that for any given ε > 0, we can find a δ > 0. The specific value of the constant used in the temporary restriction does not affect the validity of the proof, as long as it's a positive number.

2.  **Flexibility:** Using 'c' provides more flexibility in manipulating the inequalities and finding a suitable δ.  The choice of 'c' can be made to simplify the algebra in a particular proof.

3.  **Correctness:** If a δ is found using the restriction |x - a| < c, it can always be shown that this δ satisfies the epsilon-delta definition without relying on the restriction.  The restriction is merely a tool to help us find δ.

### Acceptance of the Generalized Approach

-   **Mathematically Correct:** This approach is mathematically correct. The constant 'c' is an arbitrary positive number, and the logic of the epsilon-delta proof remains valid.
-   **Accepted Alternative:** This is an accepted alternative.  Mathematicians and textbooks often use '1' for simplicity, but using a general 'c' is equally valid and demonstrates a deeper understanding of the proof technique.

### Conclusion

Using a general constant 'c' in the temporary restriction of an epsilon-delta proof is a valid and more general approach. It provides more flexibility and emphasizes that the specific value of the constant is not crucial to the proof's correctness.

# 5. Continuity

### Limits Are More Fundamental Than Continuity
- **Limits**: The foundation of calculus, used to define continuity, derivatives, and integrals.
- **Continuity**: A function $f$ is continuous at $x = a$ if:
  1. $\lim_{x \to a} f(x)$ exists,
  2. $f(a)$ is defined,
  3. $\lim_{x \to a} f(x) = f(a)$.
- The e.d. definition is used to verify the limit in the first condition, making limits more fundamental.


### Proving Continuity Using the E.D. Definition
To prove a function is continuous at a point, we need:
- The limit to exist (via the e.d. definition).
- The function to be defined at the point.
- The limit to equal the function’s value at the point.

### Polynomials: Definition vs. Continuity
- **Definition of Polynomials**:
  - A polynomial is a function of the form $p(x) = a_n x^n + \cdots + a_1 x + a_0$, where $a_i$ are constants and $n$ is a non-negative integer.
  - This is a purely algebraic definition—no mention of limits or continuity.
- **Continuity of Polynomials**:
  - Polynomials are continuous everywhere, but this is a property we *prove*, not part of their definition.
  - **Proof Process**:
    1. Use the e.d. definition to show $\lim_{x \to a} p(x) = p(a)$ for any point $a$.
    2. Note that $p(a)$ is always defined (polynomials are defined everywhere).
    3. Since the limit equals $p(a)$, the polynomial is continuous at $a$.
  - This holds for all $a$, so polynomials are continuous on their entire domain (all real numbers).
